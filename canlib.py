##############################################################################
#                                                                            #
# Module: canlib                                                             #
# Author: Maximilian Prindl                                                  #
#                                                                            #
# A library to send event messages and cyclic messages on CAN and CAN FD     #
# via a supported Vector Network Device. Inspired by python-can              #
# (https://github.com/hardbyte/python-can).                                  #
#                                                                            #
##############################################################################
import ctypes
import os
import sys
import time

try:
    from _winapi import WaitForSingleObject, WaitForMultipleObjects, INFINITE
except ImportError:
    try:
        from win32events import WaitForSingleObject, WaitForMultipleObjects, INFINITE
    except ImportError:
        print("Package pywin32 not installed.")
        WaitForSingleObject, WaitForMultipleObjects, INFINITE = None, None, None

try:
    import xlapi
except Exception as error:
    print("Could not import Vector XL Driver Library API: {0}".format(error))
    sys.exit(-1)

DEBUG = False

class CanParameters(object):
    def __init__(
        self,
        bitrate=500000,
        sjw=3,
        tseg1=None,
        tseg2=None,
        samples=1,
        sample_point=None,
        bit_cycles=None,
    ):
        self.bitrate = bitrate
        self.sjw = sjw
        self.samples = samples # CAN-Sample-Mode 1:3 Sample
        if sample_point and bit_cycles:
            self.sample_point = sample_point
            self.bit_cycles = bit_cycles
            self.tseg1 = int(sample_point * bit_cycles) - 1
            self.tseg2 = bit_cycles - 1 - self.tseg1
        elif tseg1 and tseg2:
            self.tseg1 = tseg1
            self.tseg2 = tseg2
            self.bit_cycles = 1 + tseg1 + tseg2
            self.sample_point = (1 + tseg1)/self.bit_cycles
        else:
            # Calculation of baudrate
            # Baudrate = f/(2*presc*(1+tseg1+tseg2))
            # f: crystal frequency is 16 MHz
            # presc: CAN-Prescaler [1..64] (will be conformed autom.)
            # sjw: CAN-Synchronization-Jump-Width [1..4]
            # tseg1: CAN-Time-Segment-1 [1..16]
            # tseg2: CAN-Time-Segment-2 [1..8]
            if bit_cycles:
                self.bit_cycles = bit_cycles
            else:
                self.bit_cycles = int(16e6 / bitrate / 2)
            if sample_point:
                self.sample_point = sample_point
            else:
                self.sample_point = 0.8125
            self.tseg1 = int(self.sample_point * self.bit_cycles) - 1
            self.tseg2 = self.bit_cycles - 1 - self.tseg1

    def __str__(self):
        return "\n".join([
            "CAN Parameters:",
            "  Bitrate: {0}".format(self.bitrate),
            "  Samples: {0}".format(self.samples),
            "  SJW: {0}".format(self.sjw),
            "  Tseg1: {0}".format(self.tseg1),
            "  Tseg2: {0}".format(self.tseg2),
            "  Sample Point: {0}".format(self.sample_point),
            "  Bit Cycles: {0}".format(self.bit_cycles),
        ])

    def build_xl_class(self):
        bus_params = xlapi.XLchipParams()
        bus_params.bitRate = self.bitrate
        bus_params.sjw = self.sjw
        bus_params.tseg1 = self.tseg1
        bus_params.tseg2 = self.tseg2
        bus_params.sam = self.samples
        return bus_params

class CanFdParameters(CanParameters):
    def __init__(
        self,
        is_can_fd=True,
        is_iso_fd=True,
        bitrate_abr=500000,
        sjw_abr=3,
        tseg1_abr=None,
        tseg2_abr=None,
        samples_abr=1,
        sample_point_abr=None,
        bit_cycles_abr=None,
        bitrate_dbr=2000000,
        sjw_dbr=1,
        tseg1_dbr=None,
        tseg2_dbr=None,
        sample_point_dbr=None,
        bit_cycles_dbr=None,
    ):
        if(sample_point_abr and bit_cycles_abr or
           tseg1_abr and tseg1_abr
        ):
            super(CanFdParameters, self).__init__(
                bitrate=bitrate_abr,
                sjw=sjw_abr,
                tseg1=tseg1_abr,
                tseg2=tseg2_abr,
                samples=samples_abr,
                sample_point=sample_point_abr,
                bit_cycles=bit_cycles_abr
            )
        else:
            super(CanFdParameters, self).__init__(
                bitrate=bitrate_abr,
                sjw=1,
                samples=samples_abr,
                sample_point=0.8,
                bit_cycles=80
            )
        self.is_can_fd = is_can_fd
        self.is_iso_fd = is_iso_fd
        self.bitrate_dbr = bitrate_dbr
        self.sjw_dbr = sjw_dbr
        if sample_point_dbr and bit_cycles_dbr:
            self.sample_point_dbr = sample_point_dbr
            self.bit_cycles_dbr = bit_cycles_dbr
            self.tseg1_dbr = int(sample_point_dbr * bit_cycles_dbr) - 1
            self.tseg2_dbr = bit_cycles_dbr - 1 - self.tseg1_dbr
        elif tseg1_dbr and tseg2_dbr:
            self.tseg1_dbr = tseg1_dbr
            self.tseg2_dbr = tseg2_dbr
            self.bit_cycles_dbr = 1 + tseg1_dbr + tseg2_dbr
            self.sample_point_dbr = (1 + tseg1_dbr)/self.bit_cycles_dbr
        else:
            # The hardware attempts to determine a prescaler >= 1, such that
            # (tseg1+tseg2+1)*actualBitrate*prescaler = 80MHz. Where the
            # actual bitrate differs by less than 1:256 from the requested
            # bitrate.
            if bit_cycles_dbr:
                self.bit_cycles_dbr = bit_cycles_dbr
            else:
                self.bit_cycles_dbr = int(80e6 / bitrate_dbr)
            if sample_point_dbr:
                self.sample_point_dbr = sample_point_dbr
            else:
                self.sample_point_dbr = 0.7
            self.tseg1_dbr = int(self.sample_point_dbr * self.bit_cycles_dbr) - 1
            self.tseg2_dbr = self.bit_cycles_dbr - 1 - self.tseg1_dbr

    def __str__(self):
        tmp = [super(CanFdParameters, self).__str__()]
        if self.is_can_fd:
            tmp += [
                "  FD Parameters:",
                "    ISO FD: {0}".format(self.is_iso_fd),
                "    Data Bitrate: {0}".format(self.bit_cycles_dbr),
                "    Data SJW: {0}".format(self.sjw_dbr),
                "    Data Tseg1: {0}".format(self.tseg1_dbr),
                "    Data Tseg2: {0}".format(self.tseg2_dbr),
                "    Data Sample Point: {0}".format(self.sample_point_dbr),
                "    Data Bit Cycles: {0}".format(self.bit_cycles_dbr),
            ]
        return "\n".join(tmp)

    def build_xl_class(self):
        if self.is_can_fd:
            bus_params = xlapi.XLcanFdConf()
            bus_params.arbitrationBitRate = self.bitrate
            bus_params.sjwAbr = self.sjw
            bus_params.tseg1Abr = self.tseg1
            bus_params.tseg2Abr = self.tseg2
            bus_params.dataBitRate = self.bitrate_dbr
            bus_params.sjwDbr = self.sjw_dbr
            bus_params.tseg1Dbr = self.tseg1_dbr
            bus_params.tseg2Dbr = self.tseg2_dbr
            if not self.is_iso_fd:
                bus_params.options = xlapi.CANFD_CONFOPT_NO_ISO
            return bus_params
        else:
            return super(CanFdParameters, self).build_xl_class()

class CanMessage(object):
    can_fd_dlc = [0, 1, 2, 3, 4, 5, 6, 7, 8, 12, 16, 20, 24, 32, 48, 64]

    def nof_bytes2dlc(self, dlc=None):
        if dlc is None:
            dlc = self.dlc
        for i, num_bytes in enumerate(self.can_fd_dlc):
            if dlc <= num_bytes:
                return i
        return i

    def __init__(
        self,
        is_can_fd=False,
        timestamp=0.0,
        arbitration_id=None,
        is_extended_id=False,
        is_remote_frame=False,
        is_error_frame=False,
        is_rx_frame=False,
        bitrate_switch=False,
        error_state_indicator=False,
        dlc=None,
        data=[],
    ):
        # Argument Checks:
        if is_remote_frame:
            if is_can_fd:
                raise ValueError("Can FD doesn't support remote frames.")
            if is_error_frame:
                raise ValueError("Frame can't be a remote and error frame at the same time.")
        if is_extended_id and not 0 <= arbitration_id <= 0x1FFFFFFF:
            raise ValueError("Ext. Can Ids must be between 0 - 0x1FFFFFFF (2^29)")
        elif not 0 <= arbitration_id <= 0x7FF:
            raise ValueError("Std. Can Ids must be between 0 - 0x7FF (2^11)")
        if is_can_fd:
            if len(data) > 64:
                raise ValueError("CAN FD Frames can only transport up to 64 bytes.")
        elif len(data) > 8:
            raise ValueError("Classical CAN Frames can only transport up to 8 bytes.")

        self.is_can_fd = is_can_fd
        self.timestamp = timestamp
        self.arbitration_id = arbitration_id
        self.is_extended_id = is_extended_id
        self.is_remote_frame = is_remote_frame
        self.bitrate_switch = bitrate_switch
        self.error_state_indicator = error_state_indicator
        self.is_rx_frame = is_rx_frame
        self.is_error_frame = is_error_frame
        if is_remote_frame:
            self.data = bytearray()
        else:
            self.data = bytearray(data)
        if dlc is None:
            self.dlc = self.nof_bytes2dlc(len(self.data))
        else:
            self.dlc = self.nof_bytes2dlc(dlc)
        #Override values for Classical CAN Frame over CAN FD (Tx Frames only)
        if not self.is_rx_frame:
            if not is_can_fd:
                if self.dlc > 8:
                    self.dlc = 8
                self.bitrate_switch = False
                self.error_state_indicator = False
            elif self.dlc > 8:
                self.bitrate_switch = True
        dlc_length = xlapi.CANFD_GET_NUM_DATABYTES(
            self.dlc, self.is_can_fd, self.is_remote_frame
        )
        length_diff = dlc_length - len(self.data)
        if length_diff > 0:
            self.data += bytearray([0xAA for i in range(length_diff)])

    def __str__(self):
        return "{0:.6f}  {1}  0x{2:X}({3})   {4}  {5}{6}{7}{8} {9}".format(
                    self.timestamp,
                    "Rx" if self.is_rx_frame else "Tx",
                    self.arbitration_id,
                    "EXT" if self.is_extended_id else "STD",
                    "FD" if self.is_can_fd else "CC",
                    "R" if self.is_remote_frame else " ",
                    "X" if self.is_error_frame else " ",
                    "B" if self.bitrate_switch else " ",
                    "E" if self.error_state_indicator else " ",
                    "".join(["{0:02X}".format(x) for x in self.data])
                )

    def __repr__(self):
        return "\n".join([
            ("Can FD" if self.is_can_fd else "Can") + " Message:",
            "  Timestamp: {0:.6f}".format(self.timestamp),
            "  Arbitration ID: 0x{0:X}".format(self.arbitration_id),
            "  Is ext. ID: {0}".format(self.is_extended_id),
            "  Remote Frame: {0}".format(self.is_remote_frame),
            "  Error Frame: {0}".format(self.is_error_frame),
            "  Bitrate Switch: {0}".format(self.bitrate_switch),
            "  Error State Indicator: {0}".format(self.error_state_indicator),
            "  DLC: {0}".format(self.dlc),
            "  Data: 0x{0}".format("".join(["{0:02X}".format(x) for x in self.data])),
        ])

    def build_xl_class(self, build_fd=False):
        mid = self.arbitration_id
        if self.is_extended_id:
            mid |= xlapi.XL_CAN_EXT_MSG_ID
        if build_fd:
            flags = 0
            if self.is_can_fd:
                flags |= xlapi.XL_CAN_TXMSG_FLAG.EDL
            if self.bitrate_switch:
                flags |= xlapi.XL_CAN_TXMSG_FLAG.BRS
            if self.is_remote_frame:
                flags |= xlapi.XL_CAN_TXMSG_FLAG.RTR

            event = xlapi.XLcanTxEvent()
            event.tag = xlapi.XL_EVENT_TAGS.CAN_EV_TAG_TX_MSG
            event.transId = 0xFFFF
            event.canMsg.canId = mid
            event.canMsg.msgFlags = flags
            event.canMsg.dlc = self.dlc
            event.canMsg.data = tuple(self.data)
            return event
        else:
            flags = 0
            if self.is_remote_frame:
                flags |= xlapi.XL_CAN_MSG_FLAG.REMOTE_FRAME

            event = xlapi.XLevent()
            event.tag = xlapi.XL_EVENT_TYPE.TRANSMIT_MSG
            event.msg.id = mid
            event.msg.dlc = self.dlc
            event.msg.flags = flags
            event.msg.data = tuple(self.data)
            return event

class CanBus(object):
    def __init__(
        self,
        poll_interval_ms=15,
        recv_own_messages=False,
        is_can_fd=False,
        is_iso_fd=True,
        rx_queue_size=2**14,
        bus_params=None
    ):
        self.poll_interval = poll_interval_ms/1000.0
        self.recv_own_messages = recv_own_messages
        self.is_can_fd = is_can_fd
        self.is_iso_fd = is_iso_fd
        self.rx_queue_size = rx_queue_size
        self.bus_params = bus_params

        #Open the xl driver
        xlapi.xlOpenDriver()
        self.mask, permission_mask = 0, xlapi.XLaccess()
        self.channels = []
        self.idx_to_channel, i = {}, 0
        for channel in self.get_can_channels():
            if channel.hwType == xlapi.XL_HWTYPE.VIRTUAL:
                if DEBUG:
                    pass
                else:
                    continue
            if is_can_fd:
                if (not is_iso_fd and not
                    channel.channelCapabilities & xlapi.XL_CHANNEL_FLAG.CANFD_BOSCH_SUPPORT
                ):
                    continue
                elif (is_iso_fd and not
                    channel.channelCapabilities & xlapi.XL_CHANNEL_FLAG.CANFD_ISO_SUPPORT
                ):
                    continue
            self.mask |= channel.channelMask
            if not channel.isOnBus:
                permission_mask.value |= channel.channelMask
                if bus_params or is_can_fd:
                    break
            self.channels.append(channel.channelIndex)
            self.idx_to_channel[i], i = channel.channelIndex, i+1
        else:
            raise ValueError("Couldn't find a bus.")

        if is_can_fd:
            interface_version = xlapi.XL_INTERFACE_VERSION.V4
        else:
            interface_version = xlapi.XL_INTERFACE_VERSION.V3
        self.port = xlapi.XLportHandle(xlapi.XL_INVALID_PORTHANDLE)
        try:
            xlapi.xlOpenPort(
                self.port,
                b"",
                self.mask,
                permission_mask,
                rx_queue_size,
                interface_version,
                xlapi.XL_BUS_TYPE.CAN
            )
        except xlapi.VectorError as error:
            self.shutdown()
            raise error
        if permission_mask != 0 and bus_params:
            #Got init access, setting bus params for all available init access channels
            xl_bus_params = bus_params.build_xl_class()
            if is_can_fd:
                xlapi.xlCanFdSetConfiguration(
                    self.port, permission_mask, xl_bus_params
                )
            else:
                xlapi.xlCanSetChannelParams(
                    self.port, permission_mask, xl_bus_params
                )

        tx_receipts = 1 if recv_own_messages else 0
        xlapi.xlCanSetChannelMode(self.port, self.mask, tx_receipts, 0)
        if WaitForSingleObject:
            self.event_handle = xlapi.XLhandle()
            xlapi.xlSetNotification(self.port, self.event_handle, 1)
        else:
            self.event_handle = None

        #Set acceptance filters according to ISO 15765-4
        can_ids = [
            0x7df,
            0x7e0, 0x7e8,
            0x7e1, 0x7e9,
            0x7e2, 0x7ea,
            0x7e3, 0x7eb,
            0x7e4, 0x7ec,
            0x7e5, 0x7ed,
            0x7e6, 0x7ee,
            0x7e7, 0x7ef,
        ]
        for can_id in can_ids:
            is_extended_id = can_id & xlapi.XL_CAN_EXT_MSG_ID
            try:
                xlapi.xlCanSetChannelAcceptance(
                    self.port,
                    self.mask,
                    can_id,
                    0x1FFFFFFF if is_extended_id else 0x7FF,
                    xlapi.XL_ACCEPTANCE_FILTER.CAN_EXT
                    if is_extended_id else
                    xlapi.XL_ACCEPTANCE_FILTER.CAN_STD,
                )
            except xlapi.VectorError:
                print(f"Could not set CAN ID: {can_id}")
                xlapi.xlCanResetAcceptance(self.port, self.mask, xlapi.XL_ACCEPTANCE_FILTER.CAN_STD)
                xlapi.xlCanResetAcceptance(self.port, self.mask, xlapi.XL_ACCEPTANCE_FILTER.CAN_EXT)
                break

        try:
            xlapi.xlActivateChannel(
                self.port, self.mask, xlapi.XL_BUS_TYPE.CAN, xlapi.XL_ACTIVATE.RESET_CLOCK
            )
        except xlapi.ValueError as error:
            self.shutdown()
            raise error
        #Calculate the offset between sync time and PC time
        offset = xlapi.XLuint64()
        try:
            try:
                xlapi.xlGetSyncTime(self.port, offset)
            except xlapi.VectorError:
                xlapi.xlGetChannelTime(self.port, self.mask, offset)
            self._time_offset = time.perf_counter() - offset.value * 1e-9
        except xlapi.VectorError:
            self._time_offset = 0.0

    def __iter__(self):
        return self

    def __next__(self):
        msg = self.recv(timeout=0.1)
        if msg is None:
            raise StopIteration
        else:
            return msg

    def shutdown(self):
        if self.port.value != xlapi.XL_INVALID_PORTHANDLE:
            xlapi.xlDeactivateChannel(self.port, self.mask)
            xlapi.xlClosePort(self.port)
        #Close the xl driver
        xlapi.xlCloseDriver()

    def send(self, messages):
        if isinstance(messages, CanMessage):
            messages = [messages]
        if self.is_can_fd:
            self._send_can_fd_msgs(messages)
        else:
            self._send_can_msgs(messages)

    def _send_can_msgs(self, messages):
        msg_count = ctypes.c_uint(len(messages))

        xl_msg_array = (msg.build_xl_class(build_fd=False) for msg in messages)
        xl_event_array = (xlapi.XLevent * msg_count.value)(*xl_msg_array)

        xlapi.xlCanTransmit(
            self.port, self.mask, msg_count, xl_event_array
        )
        return msg_count.value

    def _send_can_fd_msgs(self, messages):
        mask = self.mask
        msg_count = len(messages)

        xl_msg_array = (msg.build_xl_class(build_fd=True) for msg in messages)
        xl_can_fd_event_array = (xlapi.XLcanTxEvent * msg_count)(*xl_msg_array)

        msg_count_sent = ctypes.c_uint(0)
        xlapi.xlCanTransmitEx(
            self.port, self.mask, msg_count, msg_count_sent, xl_can_fd_event_array
        )
        return msg_count_sent.value

    def flush_tx_buffer(self):
        xlapi.xlCanFlushTransmitQueue(self.port, self.mask)

    def recv(self, timeout=None):
        if timeout:
            end_time = time.perf_counter() + timeout
        else:
            end_time = None

        while True:
            try:
                if self.is_can_fd:
                    msg = self._recv_canfd()
                else:
                    msg = self._recv_can()
            except xlapi.VectorError as error:
                if error.error_code != xlapi.XL_DRIVER_STATUS.ERR_QUEUE_IS_EMPTY:
                    raise error
            else:
                if msg:
                    return msg

            # if no message was received, wait or return on timeout
            if end_time is not None and time.perf_counter() > end_time:
                return None

            if self.event_handle:
                # Wait for receive event to occur
                if end_time is None:
                    time_left_ms = INFINITE
                else:
                    time_left = end_time - time.perf_counter()
                    time_left_ms = max(0, int(time_left * 1000))
                WaitForSingleObject(self.event_handle.value, time_left_ms)
            else:
                time.sleep(self.poll_interval)

    def _recv_can(self):
        xl_event = xlapi.XLevent()
        event_count = ctypes.c_uint(1)
        xlapi.xlReceive(self.port, event_count, xl_event)

        if xl_event.tag != xlapi.XL_EVENT_TAGS.RECEIVE_MSG:
            return None

        mid = xl_event.msg.id
        dlc = xl_event.msg.dlc
        flags = xl_event.msg.flags
        timestamp = xl_event.timeStamp * 1e-9
        channel = xl_event.chanIndex

        return CanMessage(
            is_can_fd=False,
            timestamp=timestamp + self._time_offset,
            arbitration_id=mid & 0x1FFFFFFF,
            is_extended_id=bool(mid & xlapi.XL_CAN_EXT_MSG_ID),
            is_remote_frame=bool(flags & xlapi.XL_CAN_MSG_FLAG.REMOTE_FRAME),
            is_error_frame=bool(flags & xlapi.XL_CAN_MSG_FLAG.ERROR_FRAME),
            is_rx_frame=not bool(flags & xlapi.XL_CAN_MSG_FLAG.TX_COMPLETED),
            dlc=dlc,
            data=xl_event.msg.data[:dlc],
        )

    def _recv_canfd(self):
        xl_can_rx_event = xlapi.XLcanRxEvent()
        xlapi.xlCanReceive(self.port, xl_can_rx_event)

        if xl_can_rx_event.tag == xlapi.XL_EVENT_TAGS.CAN_EV_TAG_RX_OK:
            is_rx_frame = True
            msg = xl_can_rx_event.canRxOkMsg
        elif xl_can_rx_event.tag == xlapi.XL_EVENT_TAGS.CAN_EV_TAG_TX_OK:
            is_rx_frame = False
            msg = xl_can_rx_event.canTxOkMsg
        else:
            return None

        mid = msg.canId
        flags = msg.msgFlags
        is_can_fd = bool(flags & xlapi.XL_CAN_RXMSG_FLAG.EDL)
        is_remote_frame = bool(flags & xlapi.XL_CAN_RXMSG_FLAG.RTR)
        dlc = xlapi.CANFD_GET_NUM_DATABYTES(msg.dlc, is_can_fd, is_remote_frame)
        timestamp = xl_can_rx_event.timeStampSync * 1e-9
        channel = xl_can_rx_event.channelIndex

        return CanMessage(
            is_can_fd=is_can_fd,
            timestamp=timestamp + self._time_offset,
            arbitration_id=mid & 0x1FFFFFFF,
            is_extended_id=bool(mid & xlapi.XL_CAN_EXT_MSG_ID),
            is_remote_frame=is_remote_frame,
            is_error_frame=bool(flags & xlapi.XL_CAN_RXMSG_FLAG.EF),
            is_rx_frame=is_rx_frame,
            bitrate_switch=bool(flags & xlapi.XL_CAN_RXMSG_FLAG.BRS),
            error_state_indicator=bool(flags & xlapi.XL_CAN_RXMSG_FLAG.ESI),
            dlc=dlc,
            data=msg.data[:dlc],
        )

    def reset(self):
            xlapi.xlDeactivateChannel(self.port, self.mask)
            try:
                xlapi.xlActivateChannel(
                    self.port, self.mask, xlapi.XL_BUS_TYPE.CAN, xlapi.XL_ACTIVATE.NONE
                )
            except xlapi.ValueError as error:
                self.shutdown()
                raise error

    @staticmethod
    def get_can_channels():
        driver_config = xlapi.XLdriverConfig()
        try:
            xlapi.xlGetDriverConfig(driver_config)
        except VectorError:
            return []
        channels = []
        for i in range(driver_config.channelCount):
            channel = driver_config.channel[i]
            if xlapi.XL_BUS_ACTIVE_CAP.CAN|channel.channelBusCapabilities:
                channels.append(channel)
        return channels

if __name__ == "__main__":
    DEBUG = True
    def test_bus(p, fd=False):
        bus = CanBus(bus_params=p, is_can_fd=fd, recv_own_messages=True)
        msg = CanMessage(
            arbitration_id=0x7e1,
            is_can_fd=fd,
            dlc=32,
            data=[0xFF, 0x00]
        )
        bus.send(msg)
        for msg in bus:
            print(msg)
        bus.shutdown()
    test_bus(CanParameters())
    test_bus(CanFdParameters(), True)
    # xlapi.xlSetTimerRate(bus.port, 100)


    # def _get_tx_channel_mask(self, msgs: Sequence[Message]) -> int:
        # if len(msgs) == 1:p
            # return self.channel_masks.get(msgs[0].channel, self.mask)
        # else:
            # return self.mask
    # def set_timer_rate(self, timer_rate_ms: int) -> None:
        # """Set the cyclic event rate of the port.

        # Once set, the port will generate a cyclic event with the tag XL_EventTags.XL_TIMER.
        # This timer can be used to keep an application alive. See XL Driver Library Description
        # for more information

        # :param timer_rate_ms:
            # The timer rate in ms. The minimal timer rate is 1ms, a value of 0 deactivates
            # the timer events.
        # """
        # timer_rate_10us = timer_rate_ms * 100
        # self.xldriver.xlSetTimerRate(self.port_handle, timer_rate_10us)



