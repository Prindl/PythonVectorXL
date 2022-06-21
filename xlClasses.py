##############################################################################
#                                                                            #
# Module: xlClasses                                                          #
# Author: Maximilian Prindl                                                  #
#                                                                            #
# Part of a python ctypes wrapper lib for the Vector XL Driver Library.      #
# Contains all of the typedef instructions of the 'vxlapi.h'.                #
# They are classed as ctypes.Structure and ctypes.Union.                     #
#                                                                            #
##############################################################################
import sys
import enum
import ctypes

import xlDefines

XLuint64 = ctypes.c_ulonglong

XLlong = ctypes.c_long

XLulong = ctypes.c_ulong

class s_xl_application_notification(ctypes.Structure):
  _fields_ = [
    ("notifyReason", ctypes.c_uint),
    ("reserved", ctypes.c_uint*7),
  ]
XL_APPLICATION_NOTIFICATION_EV = s_xl_application_notification

class s_xl_sync_pulse_ev(ctypes.Structure):
  _fields_ = [
    ("triggerSource", ctypes.c_uint),
    ("reserved", ctypes.c_uint),
    ("time", XLuint64),
  ]
XL_SYNC_PULSE_EV = s_xl_sync_pulse_ev
XL_MOST_SYNC_PULSE_EV = XL_SYNC_PULSE_EV
XL_FR_SYNC_PULSE_EV = XL_SYNC_PULSE_EV
XL_CAN_EV_SYNC_PULSE = XL_SYNC_PULSE_EV
XL_A429_EV_SYNC_PULSE = XL_SYNC_PULSE_EV

XLstringType = ctypes.c_char_p

XLaccess, pXLaccess = XLuint64, ctypes.POINTER(XLuint64)

XLhandle = ctypes.c_void_p

class s_xl_sync_pulse(ctypes.Structure):
  _fields_ = [
    ("pulseCode", ctypes.c_ubyte),
    ("time", XLuint64),
  ]

class s_xl_lin_stat_param(ctypes.Structure):
  _fields_ = [
    ("LINMode", ctypes.c_uint),
    ("baudrate", ctypes.c_int),
    ("LINVersion", ctypes.c_uint),
    ("reserved", ctypes.c_uint),
  ]
XLlinStatPar = s_xl_lin_stat_param

class s_xl_can_msg(ctypes.Structure):
  _fields_ = [
    ("id", ctypes.c_uint),
    ("flags", ctypes.c_ushort),
    ("dlc", ctypes.c_ushort),
    ("res1", XLuint64),
    ("res2", XLuint64),
  ]

class s_xl_daio_data(ctypes.Structure):
  _fields_ = [
    ("flags", ctypes.c_ushort),
    ("timestamp_correction", ctypes.c_uint),
    ("mask_digital", ctypes.c_ubyte),
    ("value_digital", ctypes.c_ubyte),
    ("mask_analog", ctypes.c_ubyte),
    ("reserved0", ctypes.c_ubyte),
    ("value_analog", ctypes.c_ushort*4),
    ("pwm_frequency", ctypes.c_uint),
    ("pwm_value", ctypes.c_ushort),
    ("reserved1", ctypes.c_uint),
    ("reserved2", ctypes.c_uint),
  ]

class s_xl_io_digital_data(ctypes.Structure):
  _fields_ = [
    ("digitalInputData", ctypes.c_uint),
  ]
XL_IO_DIGITAL_DATA = s_xl_io_digital_data

class s_xl_io_analog_data(ctypes.Structure):
  _fields_ = [
    ("measuredAnalogData0", ctypes.c_uint),
    ("measuredAnalogData1", ctypes.c_uint),
    ("measuredAnalogData2", ctypes.c_uint),
    ("measuredAnalogData3", ctypes.c_uint),
  ]
XL_IO_ANALOG_DATA = s_xl_io_analog_data

class u_xl_digital_analogue(ctypes.Union):
  _fields_ = [
    ("digital", XL_IO_DIGITAL_DATA),
    ("analog", XL_IO_ANALOG_DATA),
  ]

class s_xl_daio_piggy_data(ctypes.Structure):
  _anonymous_ = ("data",)
  _fields_ = [
    ("daioEvtTag", ctypes.c_uint),
    ("triggerType", ctypes.c_uint),
    ("data", u_xl_digital_analogue),
  ]

class s_xl_chip_state(ctypes.Structure):
  _fields_ = [
    ("busStatus", ctypes.c_ubyte),
    ("txErrorCounter", ctypes.c_ubyte),
    ("rxErrorCounter", ctypes.c_ubyte),
  ]

class s_xl_transceiver(ctypes.Structure):
  _fields_ = [
    ("event_reason", ctypes.c_ubyte),
    ("is_present", ctypes.c_ubyte),
  ]

class s_xl_lin_msg(ctypes.Structure):
  _fields_ = [
    ("id", ctypes.c_ubyte),
    ("dlc", ctypes.c_ubyte),
    ("flags", ctypes.c_ushort),
    ("data", ctypes.c_ubyte*8),
    ("crc", ctypes.c_ubyte),
  ]

class s_xl_lin_sleep(ctypes.Structure):
  _fields_ = [
    ("flag", ctypes.c_ubyte),
  ]

class s_xl_lin_no_ans(ctypes.Structure):
  _fields_ = [
    ("id", ctypes.c_ubyte),
  ]

class s_xl_lin_wake_up(ctypes.Structure):
  _fields_ = [
    ("flag", ctypes.c_ubyte),
    ("unused", ctypes.c_ubyte*3),
    ("startOffs", ctypes.c_uint),
    ("width", ctypes.c_uint),
  ]

class s_xl_lin_crc_info(ctypes.Structure):
  _fields_ = [
    ("id", ctypes.c_ubyte),
    ("flags", ctypes.c_ubyte),
  ]

class s_xl_lin_msg_api(ctypes.Union):
  _fields_ = [
    ("linMsg", s_xl_lin_msg),
    ("linNoAns", s_xl_lin_no_ans),
    ("linWakeUp", s_xl_lin_wake_up),
    ("linSleep", s_xl_lin_sleep),
    ("linCRCinfo", s_xl_lin_crc_info),
  ]

class s_xl_kline_rx_data(ctypes.Structure):
  _fields_ = [
    ("timeDiff", ctypes.c_uint),
    ("data", ctypes.c_uint),
    ("error", ctypes.c_uint),
  ]
XL_KLINE_RX_DATA = s_xl_kline_rx_data

class s_xl_kline_tx_data(ctypes.Structure):
  _fields_ = [
    ("timeDiff", ctypes.c_uint),
    ("data", ctypes.c_uint),
    ("error", ctypes.c_uint),
  ]
XL_KLINE_TX_DATA = s_xl_kline_tx_data

class s_xl_kline_tester_5bd(ctypes.Structure):
  _fields_ = [
    ("tag5bd", ctypes.c_uint),
    ("timeDiff", ctypes.c_uint),
    ("data", ctypes.c_uint),
  ]
XL_KLINE_TESTER_5BD = s_xl_kline_tester_5bd

class s_xl_kline_ecu_5bd(ctypes.Structure):
  _fields_ = [
    ("tag5bd", ctypes.c_uint),
    ("timeDiff", ctypes.c_uint),
    ("data", ctypes.c_uint),
  ]
XL_KLINE_ECU_5BD = s_xl_kline_ecu_5bd

class s_xl_kline_tester_fastinit_wu_pattern(ctypes.Structure):
  _fields_ = [
    ("timeDiff", ctypes.c_uint),
    ("fastInitEdgeTimeDiff", ctypes.c_uint),
  ]
XL_KLINE_TESTER_FI_WU_PATTERN = s_xl_kline_tester_fastinit_wu_pattern

class s_xl_kline_ecu_fastinit_wu_pattern(ctypes.Structure):
  _fields_ = [
    ("timeDiff", ctypes.c_uint),
    ("fastInitEdgeTimeDiff", ctypes.c_uint),
  ]
XL_KLINE_ECU_FI_WU_PATTERN = s_xl_kline_ecu_fastinit_wu_pattern

class s_xl_kline_confirmation(ctypes.Structure):
  _fields_ = [
    ("channel", ctypes.c_uint),
    ("confTag", ctypes.c_uint),
    ("result", ctypes.c_uint),
  ]
XL_KLINE_CONFIRMATION = s_xl_kline_confirmation

class s_xl_kline_error_rxtx(ctypes.Structure):
  _fields_ = [
    ("rxtxErrData", ctypes.c_uint),
  ]
XL_KLINE_ERROR_RXTX = s_xl_kline_error_rxtx

class s_xl_kline_error_5bd_tester(ctypes.Structure):
  _fields_ = [
    ("tester5BdErr", ctypes.c_uint),
  ]
XL_KLINE_ERROR_TESTER_5BD = s_xl_kline_error_5bd_tester

class s_xl_kline_error_5bd_ecu(ctypes.Structure):
  _fields_ = [
    ("ecu5BdErr", ctypes.c_uint),
  ]
XL_KLINE_ERROR_ECU_5BD = s_xl_kline_error_5bd_ecu

class s_xl_kline_error_ibs(ctypes.Structure):
  _fields_ = [
    ("ibsErr", ctypes.c_uint),
    ("rxtxErrData", ctypes.c_uint),
  ]
XL_KLINE_ERROR_IBS = s_xl_kline_error_ibs

class u_xl_kline_error(ctypes.Union):
  _fields_ = [
    ("rxtxErr", XL_KLINE_ERROR_RXTX),
    ("tester5BdErr", XL_KLINE_ERROR_TESTER_5BD),
    ("ecu5BdErr", XL_KLINE_ERROR_ECU_5BD),
    ("ibsErr", XL_KLINE_ERROR_IBS),
    ("reserved", ctypes.c_uint*4),
  ]

class s_xl_kline_error(ctypes.Structure):
  _anonymous_ = ("data",)
  _fields_ = [
    ("klineErrorTag", ctypes.c_uint),
    ("reserved", ctypes.c_uint),
    ("data", u_xl_kline_error),
  ]
XL_KLINE_ERROR = s_xl_kline_error

class u_xl_kline_data(ctypes.Union):
  _fields_ = [
    ("klineRx", XL_KLINE_RX_DATA),
    ("klineTx", XL_KLINE_TX_DATA),
    ("klineTester5Bd", XL_KLINE_TESTER_5BD),
    ("klineEcu5Bd", XL_KLINE_ECU_5BD),
    ("klineTesterFiWu", XL_KLINE_TESTER_FI_WU_PATTERN),
    ("klineEcuFiWu", XL_KLINE_ECU_FI_WU_PATTERN),
    ("klineConfirmation", XL_KLINE_CONFIRMATION),
    ("klineError", XL_KLINE_ERROR),
  ]

class s_xl_kline_data(ctypes.Structure):
  _anonymous_ = ("data",)
  _fields_ = [
    ("klineEvtTag", ctypes.c_uint),
    ("reserved", ctypes.c_uint),
    ("data", u_xl_kline_data),
  ]
XL_KLINE_DATA = s_xl_kline_data

class s_xl_tag_data(ctypes.Union):
  _anonymous_ = ("linMsgApi",)
  _fields_ = [
    ("msg", s_xl_can_msg),
    ("chipState", s_xl_chip_state),
    ("linMsgApi", s_xl_lin_msg_api),
    ("syncPulse", s_xl_sync_pulse),
    ("daioData", s_xl_daio_data),
    ("transceiver", s_xl_transceiver),
    ("daioPiggyData", s_xl_daio_piggy_data),
    ("klineData", s_xl_kline_data),
  ]

XLeventTag = ctypes.c_ubyte

class s_xl_event(ctypes.Structure):
  _anonymous_ = ("tagData",)
  _fields_ = [
    ("tag", XLeventTag),
    ("chanIndex", ctypes.c_ubyte),
    ("transId", ctypes.c_ushort),
    ("portHandle", ctypes.c_ushort),
    ("flags", ctypes.c_ubyte),
    ("reserved", ctypes.c_ubyte),
    ("timeStamp", XLuint64),
    ("tagData", s_xl_tag_data),
  ]
XLevent = s_xl_event

XLstatus = ctypes.c_short

class s_xl_canfd_conf(ctypes.Structure):
  _fields_ = [
    ("arbitrationBitRate", ctypes.c_uint),
    ("sjwAbr", ctypes.c_uint), #CAN bus timing for nominal / arbitration bit rate
    ("tseg1Abr", ctypes.c_uint),
    ("tseg2Abr", ctypes.c_uint),
    ("dataBitRate", ctypes.c_uint),
    ("sjwDbr", ctypes.c_uint), #CAN bus timing for data bit rate
    ("tseg1Dbr", ctypes.c_uint),
    ("tseg2Dbr", ctypes.c_uint),
    ("reserved", ctypes.c_ubyte), #has to be zero
    ("options", ctypes.c_ubyte), #configuration option CANFD-BOSCH (ISO/NON-ISO)
    ("reserved1", ctypes.c_ubyte*2), #has to be zero
    ("reserved2", ctypes.c_uint), #has to be zero
  ]
XLcanFdConf = s_xl_canfd_conf

class s_xl_chip_params(ctypes.Structure):
  _fields_ = [
    ("bitRate", ctypes.c_uint),
    ("sjw", ctypes.c_ubyte),
    ("tseg1", ctypes.c_ubyte),
    ("tseg2", ctypes.c_ubyte),
    ("sam", ctypes.c_ubyte), #1 or 3
  ]
XLchipParams = s_xl_chip_params

class s_xl_bus_params_can(ctypes.Structure):
  _fields_ = [
    ("bitRate", ctypes.c_uint),
    ("sjw", ctypes.c_ubyte),
    ("tseg1", ctypes.c_ubyte),
    ("tseg2", ctypes.c_ubyte),
    ("sam", ctypes.c_ubyte),
    ("outputMode", ctypes.c_ubyte),
    ("reserved1", ctypes.c_ubyte*7),
    ("canOpMode", ctypes.c_ubyte),
  ]

class s_xl_bus_params_canFD(ctypes.Structure):
  _fields_ = [
    ("arbitrationBitRate", ctypes.c_uint), #CAN bus timing for nominal / arbitration bit rate
    ("sjwAbr", ctypes.c_ubyte),
    ("tseg1Abr", ctypes.c_ubyte),
    ("tseg2Abr", ctypes.c_ubyte),
    ("samAbr", ctypes.c_ubyte),
    ("outputMode", ctypes.c_ubyte),
    ("sjwDbr", ctypes.c_ubyte), #CAN bus timing for data bit rate 
    ("tseg1Dbr", ctypes.c_ubyte),
    ("tseg2Dbr", ctypes.c_ubyte),
    ("dataBitRate", ctypes.c_uint),
    ("canOpMode", ctypes.c_ubyte),
  ]

class s_xl_bus_params_most(ctypes.Structure):
  _fields_ = [
    ("activeSpeedGrade", ctypes.c_uint),
    ("compatibleSpeedGrade", ctypes.c_uint),
    ("inicFwVersion", ctypes.c_uint),
  ]

class s_xl_bus_params_flexray(ctypes.Structure):
  _fields_ = [
    ("status", ctypes.c_uint), #XL_FR_CHANNEL_CFG_STATUS_xxx
    ("cfgMode", ctypes.c_uint), #XL_FR_CHANNEL_CFG_MODE_xxx
    ("baudrate", ctypes.c_uint), #FlexRay baudrate in kBaud
  ]

class s_xl_bus_params_ethernet(ctypes.Structure):
  _fields_ = [
    ("macAddr", ctypes.c_ubyte*6), #MAC address (starting with MSB!)
    ("connector", ctypes.c_ubyte), #XL_ETH_STATUS_CONNECTOR_xxx
    ("phy", ctypes.c_ubyte), #XL_ETH_STATUS_PHY_xxx
    ("link", ctypes.c_ubyte), #XL_ETH_STATUS_LINK_xxx
    ("speed", ctypes.c_ubyte), #XL_ETH_STATUS_SPEED_xxx
    ("clockMode", ctypes.c_ubyte), #XL_ETH_STATUS_CLOCK_xxx
    ("bypass", ctypes.c_ubyte), #XL_ETH_BYPASS_xxx
  ]

class s_xl_a429_params_tx(ctypes.Structure):
  _fields_ = [
    ("bitrate", ctypes.c_uint),
    ("parity", ctypes.c_uint),
    ("minGap", ctypes.c_uint),
  ]

class s_xl_a429_params_rx(ctypes.Structure):
  _fields_ = [
    ("bitrate", ctypes.c_uint),
    ("minBitrate", ctypes.c_uint),
    ("maxBitrate", ctypes.c_uint),
    ("parity", ctypes.c_uint),
    ("minGap", ctypes.c_uint),
    ("autoBaudrate", ctypes.c_uint),
  ]

class u_xl_a429_params(ctypes.Union):
  _fields_ = [
    ("tx", s_xl_a429_params_tx),
    ("rx", s_xl_a429_params_rx),
    ("raw", ctypes.c_ubyte*24),
  ]

class s_xl_bus_params_a429(ctypes.Structure):
  _anonymous_ = ("dir",)
  _fields_ = [
    ("channelDirection", ctypes.c_ushort),
    ("res1", ctypes.c_ushort),
    ("dir", u_xl_a429_params),
  ]

class u_xl_bus_params(ctypes.Union):
  _fields_ = [
    ("can", s_xl_bus_params_can),
    ("canFD", s_xl_bus_params_canFD),
    ("most", s_xl_bus_params_most),
    ("flexray", s_xl_bus_params_flexray),
    ("ethernet", s_xl_bus_params_ethernet),
    ("a429", s_xl_bus_params_a429),
    ("raw", ctypes.c_ubyte*28),
  ]

class s_xl_bus_params(ctypes.Structure):
  _anonymous_ = ("data",)
  _fields_ = [
    ("busType", ctypes.c_uint),
    ("data", u_xl_bus_params),
  ]
XLbusParams = s_xl_bus_params

XLportHandle, pXLportHandle = XLlong, ctypes.POINTER(XLlong)

class s_xl_license_info(ctypes.Structure):
  _fields_ = [
    ("bAvailable", ctypes.c_ubyte),
    ("licName", ctypes.c_char*65),
  ]
XL_LICENSE_INFO = s_xl_license_info
XLlicenseInfo = XL_LICENSE_INFO

class s_xl_channel_config(ctypes.Structure):
  _fields_ = [
    ("name", ctypes.c_char * (xlDefines.XL_MAX_LENGTH+1)),
    ("hwType", ctypes.c_ubyte),
    ("hwIndex", ctypes.c_ubyte),
    ("hwChannel", ctypes.c_ubyte),
    ("transceiverType", ctypes.c_ushort),
    ("transceiverState", ctypes.c_ushort),
    ("configError", ctypes.c_ushort),
    ("channelIndex", ctypes.c_ubyte),
    ("channelMask", XLuint64),
    ("channelCapabilities", ctypes.c_uint),
    ("channelBusCapabilities", ctypes.c_uint),
    #Channel
    ("isOnBus", ctypes.c_ubyte),
    ("connectedBusType", ctypes.c_uint),
    ("busParams", XLbusParams),
    ("_doNotUse", ctypes.c_uint),
    ("driverVersion", ctypes.c_uint),
    ("interfaceVersion", ctypes.c_uint),
    ("raw_data", ctypes.c_uint*10),
    ("serialNumber", ctypes.c_uint),
    ("articleNumber", ctypes.c_uint),
    ("transceiverName", ctypes.c_char * (xlDefines.XL_MAX_LENGTH+1)),
    ("specialCabFlags", ctypes.c_uint),
    ("dominantTimeout", ctypes.c_uint),
    ("dominantRecessiveDelay", ctypes.c_ubyte),
    ("recessiveDominantDelay", ctypes.c_ubyte),
    ("connectionInfo", ctypes.c_ubyte),
    ("currentlyAvailableTimestamps", ctypes.c_ubyte),
    ("minimalSupplyVoltage", ctypes.c_ushort),
    ("maximalSupplyVoltage", ctypes.c_ushort),
    ("maximalBaudrate", ctypes.c_uint),
    ("fpgaCoreCapabilities", ctypes.c_ubyte),
    ("specialDeviceStatus", ctypes.c_ubyte),
    ("channelBusActiveCapabilities", ctypes.c_ushort),
    ("breakOffset", ctypes.c_ushort),
    ("delimiterOffset", ctypes.c_ushort),
    ("reserved", ctypes.c_uint*3),
  ]
XL_CHANNEL_CONFIG = s_xl_channel_config
XLchannelConfig, pXLchannelConfig = XL_CHANNEL_CONFIG, ctypes.POINTER(XL_CHANNEL_CONFIG)

class s_xl_driver_config(ctypes.Structure):
  _fields_ = [
    ("dllVersion", ctypes.c_uint),
    ("channelCount", ctypes.c_uint),
    ("reserved", ctypes.c_uint*10),
    ("channel", XLchannelConfig*xlDefines.XL_CONFIG_MAX_CHANNELS),
  ]
XL_DRIVER_CONFIG = s_xl_driver_config
XLdriverConfig, pXLdriverConfig = XL_DRIVER_CONFIG, ctypes.POINTER(XL_DRIVER_CONFIG)

class s_xl_acc_filter(ctypes.Structure):
  _fields_ = [
    ("isSet", ctypes.c_ubyte),
    ("code", ctypes.c_uint),
    ("mask", ctypes.c_uint), #relevant = 1
  ]
XLaccFilt = s_xl_acc_filter

class s_xl_acceptance(ctypes.Structure):
  _fields_ = [
    ("std", XLaccFilt),
    ("xtd", XLaccFilt),
  ]
XLacceptance = s_xl_acceptance

XLuserHandle = ctypes.c_ushort

XLremoteHandle = ctypes.c_uint

XLdeviceAccess = ctypes.c_uint

XLremoteStatus = ctypes.c_uint

class u_xl_ip(ctypes.Union):
  _fields_ = [
    ("v4", ctypes.c_uint),
    ("v6", ctypes.c_uint*4),
  ]


class s_xl_ip_address(ctypes.Structure):
  _anonymous_ = ("ip",)
  _fields_ = [
    ("ip", u_xl_ip),
    ("prefixLength", ctypes.c_uint),
    ("ipVersion", ctypes.c_uint),
    ("configPort", ctypes.c_uint),
    ("eventPort", ctypes.c_uint),
  ]
XLipAddress = s_xl_ip_address

class s_xl_remote_location_config(ctypes.Structure):
  _fields_ = [
    ("hostName", ctypes.c_char*64),
    ("alias", ctypes.c_char*64),
    ("ipAddress", XLipAddress),
    ("userIpAddress", XLipAddress),
    ("deviceType", ctypes.c_uint),
    ("serialNumber", ctypes.c_uint),
    ("articleNumber", ctypes.c_uint),
    ("remoteHandle", XLremoteHandle),
  ]
XLremoteLocationConfig = s_xl_remote_location_config

class s_xl_remote_device(ctypes.Structure):
  _fields_ = [
    ("deviceName", ctypes.c_char*32),
    ("hwType", ctypes.c_uint),
    ("articleNumber", ctypes.c_uint),
    ("serialNumber", ctypes.c_uint),
    ("reserved", ctypes.c_uint),
  ]
XLremoteDevice = s_xl_remote_device

class s_xl_remote_device_info(ctypes.Structure):
  _fields_ = [
    ("locationConfig", XLremoteLocationConfig),
    ("flags", ctypes.c_uint),
    ("reserved", ctypes.c_uint),
    ("nbrOfDevices", ctypes.c_uint),
    ("deviceInfo", XLremoteDevice*xlDefines.XL_MAX_REMOTE_DEVICE_INFO),
  ]
XLremoteDeviceInfo = s_xl_remote_device_info

class s_xl_most_ctrl_spy(ctypes.Structure):
  _fields_ = [
    ("arbitration", ctypes.c_uint),
    ("targetAddress", ctypes.c_ushort),
    ("sourceAddress", ctypes.c_ushort),
    ("ctrlType", ctypes.c_ubyte),
    ("ctrlData", ctypes.c_ubyte*17),
    ("crc", ctypes.c_ushort),
    ("txStatus", ctypes.c_ushort),
    ("ctrlRes", ctypes.c_ushort),
    ("spyRxStatus", ctypes.c_uint),
  ]
XL_MOST_CTRL_SPY_EV = s_xl_most_ctrl_spy

class s_xl_most_ctrl_msg(ctypes.Structure):
  _fields_ = [
    ("ctrlPrio", ctypes.c_ubyte),
    ("ctrlType", ctypes.c_ubyte),
    ("targetAddress", ctypes.c_ushort),
    ("sourceAddress", ctypes.c_ushort),
    ("ctrlData", ctypes.c_ubyte*17),
    ("direction", ctypes.c_ubyte), #transmission or real receiption
    ("status", ctypes.c_uint), #unused for real rx msgs
  ]
XL_MOST_CTRL_MSG_EV = s_xl_most_ctrl_msg
XLmostCtrlMsg = XL_MOST_CTRL_MSG_EV

class s_xl_most_async_msg(ctypes.Structure):
  _fields_ = [
    ("status", ctypes.c_uint), #read as last data from PLD but stored first
    ("crc", ctypes.c_uint), #not used
    ("arbitration", ctypes.c_ubyte),
    ("length", ctypes.c_ubyte), #real length of async data in quadlets
    ("targetAddress", ctypes.c_ushort),
    ("sourceAddress", ctypes.c_ushort),
    ("asyncData", ctypes.c_ubyte*1018), #max size but only used data is transmitted to pc
  ]
XL_MOST_ASYNC_MSG_EV = s_xl_most_async_msg

class s_xl_most_async_tx(ctypes.Structure):
  _fields_ = [
    ("arbitration", ctypes.c_ubyte),
    ("length", ctypes.c_ubyte), #real length of async data in quadlets
    ("targetAddress", ctypes.c_ushort),
    ("sourceAddress", ctypes.c_ushort),
    ("asyncData", ctypes.c_ubyte*1014), #worst case
  ]
XL_MOST_ASYNC_TX_EV = s_xl_most_async_tx
XLmostAsyncMsg = XL_MOST_ASYNC_TX_EV

class s_xl_most_special_register(ctypes.Structure):
  _fields_ = [
    ("changeMask", ctypes.c_uint), #see defines "XL_MOST_..._CHANGED"
    ("lockStatus", ctypes.c_uint),
    ("register_bNAH", ctypes.c_ubyte),
    ("register_bNAL", ctypes.c_ubyte),
    ("register_bGA", ctypes.c_ubyte),
    ("register_bAPAH", ctypes.c_ubyte),
    ("register_bAPAL", ctypes.c_ubyte),
    ("register_bNPR", ctypes.c_ubyte),
    ("register_bMPR", ctypes.c_ubyte),
    ("register_bNDR", ctypes.c_ubyte),
    ("register_bMDR", ctypes.c_ubyte),
    ("register_bSBC", ctypes.c_ubyte),
    ("register_bXTIM", ctypes.c_ubyte),
    ("register_bXRTY", ctypes.c_ubyte),
  ]
XL_MOST_SPECIAL_REGISTER_EV = s_xl_most_special_register

class s_xl_most_event_source(ctypes.Structure):
  _fields_ = [
    ("mask", ctypes.c_uint),
    ("state", ctypes.c_uint),
  ]
XL_MOST_EVENT_SOURCE_EV = s_xl_most_event_source

class s_xl_most_all_bypass(ctypes.Structure):
  _fields_ = [
    ("bypassState", ctypes.c_uint),
  ]
XL_MOST_ALL_BYPASS_EV = s_xl_most_all_bypass

class s_xl_most_timing_mode(ctypes.Structure):
  _fields_ = [
    ("timingmode", ctypes.c_uint),
  ]
XL_MOST_TIMING_MODE_EV = s_xl_most_timing_mode

class s_xl_most_timing_mode_spdif(ctypes.Structure):
  _fields_ = [
    ("timingmode", ctypes.c_uint),
  ]
XL_MOST_TIMING_MODE_SPDIF_EV = s_xl_most_timing_mode_spdif

class s_xl_most_frequency(ctypes.Structure):
  _fields_ = [
    ("frequency", ctypes.c_uint),
  ]
XL_MOST_FREQUENCY_EV = s_xl_most_frequency

class s_xl_most_register_bytes(ctypes.Structure):
  _fields_ = [
    ("number", ctypes.c_uint),
    ("address", ctypes.c_uint),
    ("value", ctypes.c_ubyte*16),
  ]
XL_MOST_REGISTER_BYTES_EV = s_xl_most_register_bytes

class s_xl_most_register_bits(ctypes.Structure):
  _fields_ = [
    ("address", ctypes.c_uint),
    ("value", ctypes.c_uint),
    ("mask", ctypes.c_uint),
  ]
XL_MOST_REGISTER_BITS_EV = s_xl_most_register_bits

class s_xl_most_sync_alloc(ctypes.Structure):
  _fields_ = [
    ("allocTable", ctypes.c_ubyte*xlDefines.MOST_ALLOC_TABLE_SIZE),
  ]
XL_MOST_SYNC_ALLOC_EV = s_xl_most_sync_alloc

class s_xl_most_ctrl_sync_audio(ctypes.Structure):
  _fields_ = [
    ("channelMask", ctypes.c_uint*4),
    ("device", ctypes.c_uint),
    ("mode", ctypes.c_uint),
  ]
XL_MOST_CTRL_SYNC_AUDIO_EV = s_xl_most_ctrl_sync_audio

class s_xl_most_ctrl_sync_audio_ex(ctypes.Structure):
  _fields_ = [
    ("channelMask", ctypes.c_uint*16),
    ("device", ctypes.c_uint),
    ("mode", ctypes.c_uint),
  ]
XL_MOST_CTRL_SYNC_AUDIO_EX_EV = s_xl_most_ctrl_sync_audio_ex

class s_xl_most_sync_volume_status(ctypes.Structure):
  _fields_ = [
    ("device", ctypes.c_uint),
    ("volume", ctypes.c_uint),
  ]
XL_MOST_SYNC_VOLUME_STATUS_EV = s_xl_most_sync_volume_status

class s_xl_most_sync_mutes_status(ctypes.Structure):
  _fields_ = [
    ("device", ctypes.c_uint),
    ("mute", ctypes.c_uint),
  ]
XL_MOST_SYNC_MUTES_STATUS_EV = s_xl_most_sync_mutes_status

class s_xl_most_rx_light(ctypes.Structure):
  _fields_ = [
    ("light", ctypes.c_uint),
  ]
XL_MOST_RX_LIGHT_EV = s_xl_most_rx_light

class s_xl_most_tx_light(ctypes.Structure):
  _fields_ = [
    ("light", ctypes.c_uint),
  ]
XL_MOST_TX_LIGHT_EV = s_xl_most_tx_light

class s_xl_most_light_power(ctypes.Structure):
  _fields_ = [
    ("lightPower", ctypes.c_uint),
  ]
XL_MOST_LIGHT_POWER_EV = s_xl_most_light_power

class s_xl_most_lock_status(ctypes.Structure):
  _fields_ = [
    ("lockStatus", ctypes.c_uint),
  ]
XL_MOST_LOCK_STATUS_EV = s_xl_most_lock_status

class s_xl_most_supervisor_lock_status(ctypes.Structure):
  _fields_ = [
    ("supervisorLockStatus", ctypes.c_uint),
  ]
XL_MOST_SUPERVISOR_LOCK_STATUS_EV = s_xl_most_supervisor_lock_status

class s_xl_most_gen_light_error(ctypes.Structure):
  _fields_ = [
    ("lightOnTime", ctypes.c_uint),
    ("lightOffTime", ctypes.c_uint),
    ("repeat", ctypes.c_uint),
  ]
XL_MOST_GEN_LIGHT_ERROR_EV = s_xl_most_gen_light_error

class s_xl_most_gen_lock_error(ctypes.Structure):
  _fields_ = [
    ("lockOnTime", ctypes.c_uint),
    ("lockOffTime", ctypes.c_uint),
    ("repeat", ctypes.c_uint),
  ]
XL_MOST_GEN_LOCK_ERROR_EV = s_xl_most_gen_lock_error

class s_xl_most_rx_buffer(ctypes.Structure):
  _fields_ = [
    ("mode", ctypes.c_uint),
  ]
XL_MOST_RX_BUFFER_EV = s_xl_most_rx_buffer

class s_xl_most_error(ctypes.Structure):
  _fields_ = [
    ("errorCode", ctypes.c_uint),
    ("parameter", ctypes.c_uint*3),
  ]
XL_MOST_ERROR_EV = s_xl_most_error

class s_xl_most_ctrl_busload(ctypes.Structure):
  _fields_ = [
    ("busloadCtrlStarted", ctypes.c_uint),
  ]
XL_MOST_CTRL_BUSLOAD_EV = s_xl_most_ctrl_busload

class s_xl_most_async_busload(ctypes.Structure):
  _fields_ = [
    ("busloadAsyncStarted", ctypes.c_uint),
  ]
XL_MOST_ASYNC_BUSLOAD_EV = s_xl_most_async_busload

class s_xl_most_stream_state(ctypes.Structure):
  _fields_ = [
    ("streamHandle", ctypes.c_uint),
    ("streamState", ctypes.c_uint), #see XL_MOST_STREAM_STATE_...
    ("streamError", ctypes.c_uint), #see XL_MOST_STREAM_STATE_...
    ("reserved", ctypes.c_uint),
  ]
XL_MOST_STREAM_STATE_EV = s_xl_most_stream_state

class s_xl_most_stream_buffer(ctypes.Structure):
  _fields_ = [
    ("streamHandle", ctypes.c_uint),
#ifdef _MSC_VER
    #("pBuffer", POINTER_32), #32bit LSDW of buffer pointer
#else
    ("pBuffer", ctypes.c_uint), #32bit LSDW of buffer pointer
    ("validBytes", ctypes.c_uint),
    ("status", ctypes.c_uint), #see XL_MOST_STREAM_ERR_...
    ("pBuffer_highpart", ctypes.c_uint),
  ]
XL_MOST_STREAM_BUFFER_EV = s_xl_most_stream_buffer

class s_xl_most_sync_tx_underflow(ctypes.Structure):
  _fields_ = [
    ("streamHandle", ctypes.c_uint),
    ("reserved", ctypes.c_uint),
  ]
XL_MOST_SYNC_TX_UNDERFLOW_EV = s_xl_most_sync_tx_underflow

class s_xl_most_sync_rx_overflow(ctypes.Structure):
  _fields_ = [
    ("streamHandle", ctypes.c_uint),
    ("reserved", ctypes.c_uint),
  ]
XL_MOST_SYNC_RX_OVERFLOW_EV = s_xl_most_sync_rx_overflow

class s_xl_most_tag_data(ctypes.Union):
  _fields_ = [
    ("mostCtrlSpy", s_xl_most_ctrl_spy), #XL_MOST_CTRL_SPY_EV
    ("mostCtrlMsg", s_xl_most_ctrl_msg), #XL_MOST_CTRL_MSG_EV
    ("mostAsyncMsg", s_xl_most_async_msg), #XL_MOST_ASYNC_MSG_EV, received async frame
    ("mostAsyncTx", s_xl_most_async_tx), #XL_MOST_ASYNC_TX_EV, async frame tx acknowledge
    ("mostSpecialRegister", s_xl_most_special_register), #XL_MOST_SPECIAL_REGISTER_EV
    ("mostEventSource", s_xl_most_event_source), #XL_MOST_EVENT_SOURCE_EV
    ("mostAllBypass", s_xl_most_all_bypass), #XL_MOST_ALL_BYPASS_EV
    ("mostTimingMode", s_xl_most_timing_mode), #XL_MOST_TIMING_MODE_EV
    ("mostTimingModeSpdif", s_xl_most_timing_mode_spdif), #XL_MOST_TIMING_MODE_SPDIF_EV
    ("mostFrequency", s_xl_most_frequency), #XL_MOST_FREQUENCY_EV
    ("mostRegisterBytes", s_xl_most_register_bytes), #XL_MOST_REGISTER_BYTES_EV
    ("mostRegisterBits", s_xl_most_register_bits), #XL_MOST_REGISTER_BITS_EV
    ("mostSyncAlloc", s_xl_most_sync_alloc), #XL_MOST_SYNC_ALLOC_EV
    ("mostCtrlSyncAudio", s_xl_most_ctrl_sync_audio), #XL_MOST_CTRL_SYNC_AUDIO_EV
    ("mostCtrlSyncAudioEx", s_xl_most_ctrl_sync_audio_ex), #XL_MOST_CTRL_SYNC_AUDIO_EX_EV
    ("mostSyncVolumeStatus", s_xl_most_sync_volume_status), #XL_MOST_SYNC_VOLUME_STATUS_EV
    ("mostSyncMuteStatus", s_xl_most_sync_mutes_status), #XL_MOST_SYNC_MUTES_STATUS_EV
    ("mostRxLight", s_xl_most_rx_light), #XL_MOST_RX_LIGHT_EV
    ("mostTxLight", s_xl_most_tx_light), #XL_MOST_TX_LIGHT_EV
    ("mostLightPower", s_xl_most_light_power), #XL_MOST_LIGHT_POWER_EV
    ("mostLockStatus", s_xl_most_lock_status), #XL_MOST_LOCK_STATUS_EV
    ("mostGenLightError", s_xl_most_gen_light_error), #XL_MOST_GEN_LIGHT_ERROR_EV
    ("mostGenLockError", s_xl_most_gen_lock_error), #XL_MOST_GEN_LOCK_ERROR_EV
    ("mostRxBuffer", s_xl_most_rx_buffer), #XL_MOST_RX_BUFFER_EV
    ("mostError", s_xl_most_error), #XL_MOST_ERROR_EV
    ("mostSyncPulse", s_xl_sync_pulse_ev), #XL_MOST_SYNC_PULSE_EV
    ("mostCtrlBusload", s_xl_most_ctrl_busload), #XL_MOST_CTRL_BUSLOAD_EV
    ("mostAsyncBusload", s_xl_most_async_busload), #XL_MOST_ASYNC_BUSLOAD_EV
    ("mostStreamState", s_xl_most_stream_state), #XL_MOST_STREAM_STATE_EV
    ("mostStreamBuffer", s_xl_most_stream_buffer), #XL_MOST_STREAM_BUFFER_EV
    ("mostSyncTxUnderflow", s_xl_most_sync_tx_underflow), #XL_MOST_SYNC_TX_UNDERFLOW_EV
    ("mostSyncRxOverflow", s_xl_most_sync_rx_overflow), #XL_MOST_SYNC_RX_OVERFLOW_EV
  ]

XLmostEventTag = ctypes.c_ushort

class s_xl_most_event(ctypes.Structure):
  _anonymous_ = ("tagData",)
  _fields_ = [
    ("size", ctypes.c_uint),
    ("tag", XLmostEventTag),
    ("channelIndex", ctypes.c_ushort),
    ("userHandle", ctypes.c_uint),
    ("flagsChip", ctypes.c_ushort),
    ("reserved", ctypes.c_ushort),
    ("timeStamp", XLuint64),
    ("timeStampSync", XLuint64),
    ("tagData", s_xl_most_tag_data),
  ]
XLmostEvent = s_xl_most_event

class s_xl_most_ctrl_busload_configuration(ctypes.Structure):
  _fields_ = [
    ("transmissionRate", ctypes.c_uint),
    ("counterType", ctypes.c_uint),
    ("counterPosition", ctypes.c_uint),
    ("busloadCtrlMsg", XL_MOST_CTRL_MSG_EV),
  ]
XL_MOST_CTRL_BUSLOAD_CONFIGURATION = s_xl_most_ctrl_busload_configuration
XLmostCtrlBusloadConfiguration = XL_MOST_CTRL_BUSLOAD_CONFIGURATION

class s_xl_most_async_busload_configuration(ctypes.Structure):
  _fields_ = [
    ("transmissionRate", ctypes.c_uint),
    ("counterType", ctypes.c_uint),
    ("counterPosition", ctypes.c_uint),
    ("busloadAsyncMsg", XL_MOST_ASYNC_TX_EV),
  ]
XL_MOST_ASYNC_BUSLOAD_CONFIGURATION = s_xl_most_async_busload_configuration
XLmostAsyncBusloadConfiguration = XL_MOST_ASYNC_BUSLOAD_CONFIGURATION

class s_xl_most_device_state(ctypes.Structure):
  _fields_ = [
    #XL_MOST_STATESEL_LIGHTLOCK
    ("selectionMask", ctypes.c_uint),
    ("lockState", ctypes.c_uint), #see XL_MOST_LOCK_STATUS_EV
    ("rxLight", ctypes.c_uint), #see XL_MOST_RX_LIGHT_EV
    ("txLight", ctypes.c_uint), #see XL_MOST_TX_LIGHT_EV
    ("txLightPower", ctypes.c_uint), #see XL_MOST_LIGHT_POWER_EV
    #XL_MOST_STATESEL_REGISTERBUNCH1
    ("registerBunch1", ctypes.c_ubyte*16), #16 OS8104 registers (0x87...0x96 -> NPR...SBC)
    #XL_MOST_STATESEL_BYPASSTIMING
    ("bypassState", ctypes.c_uint), #see XL_MOST_ALL_BYPASS_EV
    ("timingMode", ctypes.c_uint), #see XL_MOST_TIMING_MODE_EV
    ("frequency", ctypes.c_uint), #frame rate (if master); see XL_MOST_FREQUENCY_EV
    #XL_MOST_STATESEL_REGISTERBUNCH2
    ("registerBunch2", ctypes.c_ubyte*2), #2 OS8104 registers (0xBE, 0xBF -> XTIM, XRTY)
    #XL_MOST_STATESEL_REGISTERBUNCH3
    ("registerBunch3", ctypes.c_ubyte*2), #2 OS8104 registers (0xE8, 0xE9 -> APAH, APAL)
    #XL_MOST_STATESEL_VOLUMEMUTE
    ("volume", ctypes.c_uint*2), #volume state for DEVICE_CASE_LINE_IN, DEVICE_CASE_LINE_OUT
    ("mute", ctypes.c_uint*2), #mute state for DEVICE_CASE_LINE_IN, DEVICE_CASE_LINE_OUT
    #XL_MOST_STATESEL_EVENTSOURCE
    ("eventSource", ctypes.c_uint), #see XL_MOST_EVENT_SOURCE_EV
    #XL_MOST_STATESEL_RXBUFFERMODE
    ("rxBufferMode", ctypes.c_uint), #see XL_MOST_RX_BUFFER_EV
    #XL_MOST_STATESEL_ALLOCTABLE
    ("allocTable", ctypes.c_ubyte*xlDefines.MOST_ALLOC_TABLE_SIZE), #see XL_MOST_SYNC_ALLOC_EV
    #XL_MOST_STATESEL_SUPERVISOR_LOCKSTATUS
    ("supervisorLockStatus", ctypes.c_uint),
    #XL_MOST_STATESEL_SUPERVISOR_MESSAGE
    ("broadcastedConfigStatus", ctypes.c_uint),
    ("adrNetworkMaster", ctypes.c_uint),
    ("abilityToWake", ctypes.c_uint),
  ]
XL_MOST_DEVICE_STATE = s_xl_most_device_state

class s_xl_most_stream_open(ctypes.Structure):
  _fields_ = [
    ("pStreamHandle", ctypes.POINTER(ctypes.c_uint)),
    ("numSyncChannels", ctypes.c_uint),
    ("direction", ctypes.c_uint),
    ("options", ctypes.c_uint),
    ("latency", ctypes.c_uint),
  ]
XL_MOST_STREAM_OPEN = s_xl_most_stream_open
XLmostStreamOpen = XL_MOST_STREAM_OPEN

class s_xl_most_stream_info(ctypes.Structure):
  _fields_ = [
    ("streamHandle", ctypes.c_uint),
    ("numSyncChannels", ctypes.c_uint),
    ("direction", ctypes.c_uint),
    ("options", ctypes.c_uint),
    ("latency", ctypes.c_uint),
    ("streamState", ctypes.c_uint),
    ("reserved", ctypes.c_uint),
    ("syncChannels", ctypes.c_ubyte*60),
  ]
XL_MOST_STREAM_INFO = s_xl_most_stream_info
XLmostStreamInfo = XL_MOST_STREAM_INFO

class s_xl_fr_cluster_configuration(ctypes.Structure):
  _fields_ = [
    ("busGuardianEnable", ctypes.c_uint),
    ("baudrate", ctypes.c_uint),
    ("busGuardianTick", ctypes.c_uint),
    ("externalClockCorrectionMode", ctypes.c_uint),
    ("gColdStartAttempts", ctypes.c_uint),
    ("gListenNoise", ctypes.c_uint),
    ("gMacroPerCycle", ctypes.c_uint),
    ("gMaxWithoutClockCorrectionFatal", ctypes.c_uint),
    ("gMaxWithoutClockCorrectionPassive", ctypes.c_uint),
    ("gNetworkManagementVectorLength", ctypes.c_uint),
    ("gNumberOfMinislots", ctypes.c_uint),
    ("gNumberOfStaticSlots", ctypes.c_uint),
    ("gOffsetCorrectionStart", ctypes.c_uint),
    ("gPayloadLengthStatic", ctypes.c_uint),
    ("gSyncNodeMax", ctypes.c_uint),
    ("gdActionPointOffset", ctypes.c_uint),
    ("gdDynamicSlotIdlePhase", ctypes.c_uint),
    ("gdMacrotick", ctypes.c_uint),
    ("gdMinislot", ctypes.c_uint),
    ("gdMiniSlotActionPointOffset", ctypes.c_uint),
    ("gdNIT", ctypes.c_uint),
    ("gdStaticSlot", ctypes.c_uint),
    ("gdSymbolWindow", ctypes.c_uint),
    ("gdTSSTransmitter", ctypes.c_uint),
    ("gdWakeupSymbolRxIdle", ctypes.c_uint),
    ("gdWakeupSymbolRxLow", ctypes.c_uint),
    ("gdWakeupSymbolRxWindow", ctypes.c_uint),
    ("gdWakeupSymbolTxIdle", ctypes.c_uint),
    ("gdWakeupSymbolTxLow", ctypes.c_uint),
    ("pAllowHaltDueToClock", ctypes.c_uint),
    ("pAllowPassiveToActive", ctypes.c_uint),
    ("pChannels", ctypes.c_uint),
    ("pClusterDriftDamping", ctypes.c_uint),
    ("pDecodingCorrection", ctypes.c_uint),
    ("pDelayCompensationA", ctypes.c_uint),
    ("pDelayCompensationB", ctypes.c_uint),
    ("pExternOffsetCorrection", ctypes.c_uint),
    ("pExternRateCorrection", ctypes.c_uint),
    ("pKeySlotUsedForStartup", ctypes.c_uint),
    ("pKeySlotUsedForSync", ctypes.c_uint),
    ("pLatestTx", ctypes.c_uint),
    ("pMacroInitialOffsetA", ctypes.c_uint),
    ("pMacroInitialOffsetB", ctypes.c_uint),
    ("pMaxPayloadLengthDynamic", ctypes.c_uint),
    ("pMicroInitialOffsetA", ctypes.c_uint),
    ("pMicroInitialOffsetB", ctypes.c_uint),
    ("pMicroPerCycle", ctypes.c_uint),
    ("pMicroPerMacroNom", ctypes.c_uint),
    ("pOffsetCorrectionOut", ctypes.c_uint),
    ("pRateCorrectionOut", ctypes.c_uint),
    ("pSamplesPerMicrotick", ctypes.c_uint),
    ("pSingleSlotEnabled", ctypes.c_uint),
    ("pWakeupChannel", ctypes.c_uint),
    ("pWakeupPattern", ctypes.c_uint),
    ("pdAcceptedStartupRange", ctypes.c_uint),
    ("pdListenTimeout", ctypes.c_uint),
    ("pdMaxDrift", ctypes.c_uint),
    ("pdMicrotick", ctypes.c_uint),
    ("gdCASRxLowMax", ctypes.c_uint),
    ("gChannels", ctypes.c_uint),
    ("vExternOffsetControl", ctypes.c_uint),
    ("vExternRateControl", ctypes.c_uint),
    ("pChannelsMTS", ctypes.c_uint),
    ("framePresetData", ctypes.c_uint), #16-bit value with data for pre-initializing the Flexray payload data words
    ("reserved", ctypes.c_uint*15),
  ]
XLfrClusterConfig = s_xl_fr_cluster_configuration

class s_xl_fr_channel_config(ctypes.Structure):
  _fields_ = [
    ("status", ctypes.c_uint), #XL_FR_CHANNEL_CFG_STATUS_xxx
    ("cfgMode", ctypes.c_uint), #XL_FR_CHANNEL_CFG_MODE_xxx
    ("reserved", ctypes.c_uint*6),
    ("xlFrClusterConfig", s_xl_fr_cluster_configuration), #same as used in function xlFrSetConfig
  ]
XLfrChannelConfig = s_xl_fr_channel_config

class s_xl_fr_set_modes(ctypes.Structure):
  _fields_ = [
    ("frMode", ctypes.c_uint),
    ("frStartupAttributes", ctypes.c_uint),
    ("reserved", ctypes.c_uint*30),
  ]
XLfrMode = s_xl_fr_set_modes

class s_xl_fr_acceptance_filter(ctypes.Structure):
  _fields_ = [
    ("filterStatus", ctypes.c_uint), #defines if the specified frame should be blocked or pass the filter
    ("filterTypeMask", ctypes.c_uint), #specifies the frame type that should be filtered
    ("filterFirstSlot", ctypes.c_uint), #beginning of the slot range
    ("filterLastSlot", ctypes.c_uint), #end of the slot range (can be the same as filterFirstSlot)
    ("filterChannelMask", ctypes.c_uint), #channel A, B for PC, channel A, B for COB
  ]
XLfrAcceptanceFilter = s_xl_fr_acceptance_filter

class s_xl_fr_start_cycle(ctypes.Structure):
  _fields_ = [
    ("cycleCount", ctypes.c_uint),
    ("vRateCorrection", ctypes.c_int),
    ("vOffsetCorrection", ctypes.c_int),
    ("vClockCorrectionFailed", ctypes.c_uint),
    ("vAllowPassivToActive", ctypes.c_uint),
    ("reserved", ctypes.c_uint*3),
  ]
XL_FR_START_CYCLE_EV = s_xl_fr_start_cycle

class s_xl_fr_rx_frame(ctypes.Structure):
  _fields_ = [
    ("flags", ctypes.c_ushort),
    ("headerCRC", ctypes.c_ushort),
    ("slotID", ctypes.c_ushort),
    ("cycleCount", ctypes.c_ubyte),
    ("payloadLength", ctypes.c_ubyte),
    ("data", ctypes.c_ubyte*xlDefines.XL_FR_MAX_DATA_LENGTH),
  ]
XL_FR_RX_FRAME_EV = s_xl_fr_rx_frame

class s_xl_fr_tx_frame(ctypes.Structure):
  _fields_ = [
    ("flags", ctypes.c_ushort),
    ("slotID", ctypes.c_ushort),
    ("offset", ctypes.c_ubyte),
    ("repetition", ctypes.c_ubyte),
    ("payloadLength", ctypes.c_ubyte),
    ("txMode", ctypes.c_ubyte),
    ("incrementSize", ctypes.c_ubyte),
    ("incrementOffset", ctypes.c_ubyte),
    ("reserved0", ctypes.c_ubyte),
    ("reserved1", ctypes.c_ubyte),
    ("data", ctypes.c_ubyte*xlDefines.XL_FR_MAX_DATA_LENGTH),
  ]
XL_FR_TX_FRAME_EV = s_xl_fr_tx_frame

class s_xl_fr_wakeup(ctypes.Structure):
  _fields_ = [
    ("cycleCount", ctypes.c_ubyte), #Actual cyclecount.
    ("wakeupStatus", ctypes.c_ubyte), #XL_FR_WAKEUP_UNDEFINED, ...
    ("reserved", ctypes.c_ubyte*6),
  ]
XL_FR_WAKEUP_EV = s_xl_fr_wakeup

class s_xl_fr_symbol_window(ctypes.Structure):
  _fields_ = [
    ("symbol", ctypes.c_uint), #XL_FR_SYMBOL_MTS, ...
    ("flags", ctypes.c_uint), #XL_FR_SYMBOL_STATUS_SESA, ...
    ("cycleCount", ctypes.c_ubyte), #Actual cyclecount.
    ("reserved", ctypes.c_ubyte*7),
  ]
XL_FR_SYMBOL_WINDOW_EV = s_xl_fr_symbol_window

class s_xl_fr_status(ctypes.Structure):
  _fields_ = [
    ("statusType", ctypes.c_uint), #POC status XL_FR_STATUS_ defines like, normal, active...
    ("reserved", ctypes.c_uint),
  ]
XL_FR_STATUS_EV = s_xl_fr_status

class s_xl_fr_nm_vector(ctypes.Structure):
  _fields_ = [
    ("nmVector", ctypes.c_ubyte*12),
    ("cycleCount", ctypes.c_ubyte), #Actual cyclecount.
    ("reserved", ctypes.c_ubyte*3),
  ]
XL_FR_NM_VECTOR_EV = s_xl_fr_nm_vector

class s_xl_fr_error_poc_mode(ctypes.Structure):
  _fields_ = [
    ("errorMode", ctypes.c_ubyte), #error mode like: active, passive, comm_halt
    ("reserved", ctypes.c_ubyte*3),
  ]
XL_FR_ERROR_POC_MODE_EV = s_xl_fr_error_poc_mode

class s_xl_fr_error_sync_frames(ctypes.Structure):
  _fields_ = [
    ("evenSyncFramesA", ctypes.c_ushort), #valid RX/TX sync frames on frCh A for even cycles
    ("oddSyncFramesA", ctypes.c_ushort), #valid RX/TX sync frames on frCh A for odd cycles
    ("evenSyncFramesB", ctypes.c_ushort), #valid RX/TX sync frames on frCh B for even cycles
    ("oddSyncFramesB", ctypes.c_ushort), #valid RX/TX sync frames on frCh B for odd cycles
    ("reserved", ctypes.c_uint),
  ]
XL_FR_ERROR_SYNC_FRAMES_EV = s_xl_fr_error_sync_frames

class s_xl_fr_error_clock_corr_failure(ctypes.Structure):
  _fields_ = [
    ("evenSyncFramesA", ctypes.c_ushort), #valid RX/TX sync frames on frCh A for even cycles
    ("oddSyncFramesA", ctypes.c_ushort), #valid RX/TX sync frames on frCh A for odd cycles
    ("evenSyncFramesB", ctypes.c_ushort), #valid RX/TX sync frames on frCh B for even cycles
    ("oddSyncFramesB", ctypes.c_ushort), #valid RX/TX sync frames on frCh B for odd cycles
    ("flags", ctypes.c_uint), #missing/maximum rate/offset correction flags.
    ("clockCorrFailedCounter", ctypes.c_uint), #E-Ray: CCEV register (CCFC value)
    ("reserved", ctypes.c_uint),
  ]
XL_FR_ERROR_CLOCK_CORR_FAILURE_EV = s_xl_fr_error_clock_corr_failure

class s_xl_fr_error_nit_failure(ctypes.Structure):
  _fields_ = [
    ("flags", ctypes.c_uint), #flags for NIT boundary, syntax error...
    ("reserved", ctypes.c_uint),
  ]
XL_FR_ERROR_NIT_FAILURE_EV = s_xl_fr_error_nit_failure

class s_xl_fr_error_cc_error(ctypes.Structure):
  _fields_ = [
    ("ccError", ctypes.c_uint), #internal CC errors (Transmit Across Boundary, Transmit Violation...)
    ("reserved", ctypes.c_uint),
  ]
XL_FR_ERROR_CC_ERROR_EV = s_xl_fr_error_cc_error

class s_xl_fr_error_info(ctypes.Union):
  _fields_ = [
    ("frPocMode", s_xl_fr_error_poc_mode), #E-RAY: EIR_PEMC
    ("frSyncFramesBelowMin", s_xl_fr_error_sync_frames), #E-RAY: EIR_SFBM
    ("frSyncFramesOverload", s_xl_fr_error_sync_frames), #E-RAY: EIR_SFO
    ("frClockCorrectionFailure", s_xl_fr_error_clock_corr_failure), #E-RAY: EIR_CCF
    ("frNitFailure", s_xl_fr_error_nit_failure), #NIT part of the E_RAY: SWNIT register
    ("frCCError", s_xl_fr_error_cc_error), #internal CC error flags (E-RAY: EIR)
  ]

class s_xl_fr_error(ctypes.Structure):
  _fields_ = [
    ("tag", ctypes.c_ubyte),
    ("cycleCount", ctypes.c_ubyte),
    ("reserved", ctypes.c_ubyte*6),
    ("errorInfo", s_xl_fr_error_info),
  ]
XL_FR_ERROR_EV = s_xl_fr_error

class s_xl_fr_spy_frame(ctypes.Structure):
  _fields_ = [
    ("frameLength", ctypes.c_uint),
    ("frameError", ctypes.c_ubyte), #XL_FR_SPY_FRAMEFLAG_XXX values
    ("tssLength", ctypes.c_ubyte),
    ("headerFlags", ctypes.c_ushort),
    ("slotID", ctypes.c_ushort),
    ("headerCRC", ctypes.c_ushort),
    ("payloadLength", ctypes.c_ubyte),
    ("cycleCount", ctypes.c_ubyte),
    ("frameFlags", ctypes.c_ubyte),
    ("reserved", ctypes.c_ubyte),
    ("frameCRC", ctypes.c_uint),
    ("data", ctypes.c_ubyte*xlDefines.XL_FR_MAX_DATA_LENGTH),
  ]
XL_FR_SPY_FRAME_EV = s_xl_fr_spy_frame

class s_xl_fr_spy_symbol(ctypes.Structure):
  _fields_ = [
    ("lowLength", ctypes.c_ushort),
    ("reserved", ctypes.c_ushort),
  ]
XL_FR_SPY_SYMBOL_EV = s_xl_fr_spy_symbol

class s_xl_fr_tag_data(ctypes.Union):
  _fields_ = [
    ("frStartCycle", s_xl_fr_start_cycle), #XL_FR_START_CYCLE_EV
    ("frRxFrame", s_xl_fr_rx_frame), #XL_FR_RX_FRAME_EV
    ("frTxFrame", s_xl_fr_tx_frame), #XL_FR_TX_FRAME_EV
    ("frWakeup", s_xl_fr_wakeup), #XL_FR_WAKEUP_EV
    ("frSymbolWindow", s_xl_fr_symbol_window), #XL_FR_SYMBOL_WINDOW_EV
    ("frError", s_xl_fr_error), #XL_FR_ERROR_EV
    ("frStatus", s_xl_fr_status), #XL_FR_STATUS_EV
    ("frNmVector", s_xl_fr_nm_vector), #XL_FR_NM_VECTOR_EV
    ("frSyncPulse", s_xl_sync_pulse_ev), #XL_FR_SYNC_PULSE_EV
    ("frSpyFrame", s_xl_fr_spy_frame), #XL_FR_SPY_FRAME_EV
    ("frSpySymbol", s_xl_fr_spy_symbol), #XL_FR_SPY_SYMBOL_EV
    ("applicationNotification", s_xl_application_notification), #XL_APPLICATION_NOTIFICATION_EV
  ]

XLfrEventTag = ctypes.c_ushort

class s_xl_fr_event(ctypes.Structure):
  _anonymous_ = ("tagData",)
  _fields_ = [
    ("size", ctypes.c_uint), #overall size of the complete event
    ("tag", XLfrEventTag), #type of the event
    ("channelIndex", ctypes.c_ushort),
    ("userHandle", ctypes.c_uint),
    ("flagsChip", ctypes.c_ushort), #frChannel e.g. XL_FR_CHANNEL_A (lower 8 bit), queue overflow (upper 8bit)
    ("reserved", ctypes.c_ushort),
    ("timeStamp", XLuint64), #raw timestamp
    ("timeStampSync", XLuint64), #timestamp which is synchronized by the driver
    ("tagData", s_xl_fr_tag_data),
  ]
XLfrEvent = s_xl_fr_event;

class s_xl_daio_trigger_type_params_digital(ctypes.Structure):
  _fields_ = [
    ("portMask", ctypes.c_uint),
    ("type", ctypes.c_uint), # Use defines XL_DAIO_TRIGGER_TYPE_xxx(RISIONG|FALLING|BOTH)
  ]

class u_xl_trigger_type_params(ctypes.Union):
  _fields_ = [
    ("cycleTime", ctypes.c_uint), #specify time in microseconds
    ("digital", s_xl_daio_trigger_type_params_digital),
  ]

class s_xl_daio_trigger_mode(ctypes.Structure):
  _anonymous_ = ("param",)
  _fields_ = [
    ("portTypeMask", ctypes.c_uint), #Use defines XL_DAIO_PORT_TYPE_MASK_xxx. Unused for VN1630/VN1640.
    ("triggerType", ctypes.c_uint), #Use defines XL_DAIO_TRIGGER_TYPE_xxx(CYCLIC|PORT)
    ("param", u_xl_trigger_type_params),
  ]
XLdaioTriggerMode = s_xl_daio_trigger_mode

class xl_daio_set_port(ctypes.Structure):
  _fields_ = [
    ("portType", ctypes.c_uint), #Only one signal group is allowed. One of the defines XL_DAIO_PORT_TYPE_MASK_*
    ("portMask", ctypes.c_uint), #Mask of affected ports.
    ("portFunction", ctypes.c_uint*8), #Special function of port. One of the defines XL_DAIO_PORT_DIGITAL_* or XL_DAIO_PORT_ANALOG_*
    ("reserved", ctypes.c_uint*8), #Set this parameters to zero!
  ]
XLdaioSetPort = xl_daio_set_port

class xl_daio_digital_params(ctypes.Structure):
  _fields_ = [
    ("portMask", ctypes.c_uint), #Use defines XL_DAIO_PORT_MASK_DIGITAL_*
    ("valueMask", ctypes.c_uint), #Specify the port value (ON/HIGH 1 | OFF/LOW - 0)
  ]
XLdaioDigitalParams = xl_daio_digital_params

class xl_daio_analog_params(ctypes.Structure):
  _fields_ = [
    ("portMask", ctypes.c_uint), #Use defines XL_DAIO_PORT_MASK_ANALOG_*
    ("value", ctypes.c_uint*8), #12-bit values
  ]
XLdaioAnalogParams = xl_daio_analog_params

class s_xl_kline_uart_params(ctypes.Structure):
  _fields_ = [
    ("databits", ctypes.c_uint),
    ("stopbits", ctypes.c_uint),
    ("parity", ctypes.c_uint),
  ]
XLklineUartParameter = s_xl_kline_uart_params

class s_xl_kline_init_tester(ctypes.Structure):
  _fields_ = [
    ("TiniL", ctypes.c_uint), #us
    ("Twup", ctypes.c_uint), #us
    ("reserved", ctypes.c_uint),
  ]
XLklineInitTester = s_xl_kline_init_tester

class s_xl_kline_init_5BdTester(ctypes.Structure):
  _fields_ = [
    ("addr", ctypes.c_uint),
    ("rate5bd", ctypes.c_uint),
    ("W1min", ctypes.c_uint), #us
    ("W1max", ctypes.c_uint), #us
    ("W2min", ctypes.c_uint), #us
    ("W2max", ctypes.c_uint), #us
    ("W3min", ctypes.c_uint), #us
    ("W3max", ctypes.c_uint), #us
    ("W4", ctypes.c_uint), #us
    ("W4min", ctypes.c_uint), #us
    ("W4max", ctypes.c_uint), #us
    ("kb2Not", ctypes.c_uint),
    ("reserved", ctypes.c_uint),
  ]
XLkline5BdTester = s_xl_kline_init_5BdTester

class s_xl_kline_init_5BdEcu(ctypes.Structure):
  _fields_ = [
    ("configure", ctypes.c_uint),
    ("addr", ctypes.c_uint),
    ("rate5bd", ctypes.c_uint),
    ("syncPattern", ctypes.c_uint),
    ("W1", ctypes.c_uint), #us
    ("W2", ctypes.c_uint), #us
    ("W3", ctypes.c_uint), #us
    ("W4", ctypes.c_uint), #us
    ("W4min", ctypes.c_uint), #us
    ("W4max", ctypes.c_uint), #us
    ("kb1", ctypes.c_uint),
    ("kb2", ctypes.c_uint),
    ("addrNot", ctypes.c_uint),
    ("reserved", ctypes.c_uint),
  ]
XLkline5BdEcu = s_xl_kline_init_5BdEcu

class s_xl_kline_set_com_tester(ctypes.Structure):
  _fields_ = [
    ("P1min", ctypes.c_uint), #us
    ("P4", ctypes.c_uint), #us
    ("reserved", ctypes.c_uint),
  ]
XLklineSetComTester = s_xl_kline_set_com_tester

class s_xl_kline_set_com_ecu(ctypes.Structure):
  _fields_ = [
    ("P1", ctypes.c_uint), #us
    ("P4min", ctypes.c_uint), #us
    ("TinilMin", ctypes.c_uint), #us
    ("TinilMax", ctypes.c_uint), #us
    ("TwupMin", ctypes.c_uint), #us
    ("TwupMax", ctypes.c_uint), #us
    ("reserved", ctypes.c_uint),
  ]
XLklineSetComEcu = s_xl_kline_set_com_ecu

XLnetworkId, pXLnetworkId = ctypes.c_int, ctypes.POINTER(ctypes.c_int)

XLswitchId, pXLswitchId = ctypes.c_int, ctypes.POINTER(ctypes.c_int)

XLnetworkHandle, pXLnetworkHandle = XLlong, ctypes.POINTER(XLlong)

XLethPortHandle, pXLethPortHandle = XLlong, ctypes.POINTER(XLlong)

XLrxHandle, pXLrxHandle = XLlong, ctypes.POINTER(XLlong)

XLethEventTag = ctypes.c_ushort


class s_xl_eth_frame(ctypes.Structure):
  _fields_ = [
    ("etherType", ctypes.c_ushort), #Ethernet type in network byte order
    ("payload", ctypes.c_ubyte*xlDefines.XL_ETH_PAYLOAD_SIZE_MAX),
  ]
T_XL_ETH_FRAME = s_xl_eth_frame

class s_xl_eth_framedata(ctypes.Union):
  _fields_ = [
    ("rawData", ctypes.c_ubyte*xlDefines.XL_ETH_RAW_FRAME_SIZE_MAX),
    ("ethFrame", s_xl_eth_frame),
  ]
T_XL_ETH_FRAMEDATA = s_xl_eth_framedata

class s_xl_eth_dataframe_rx(ctypes.Structure):
  _anonymous_ = ("frameData",)
  _fields_ = [
    ("frameIdentifier", ctypes.c_uint), #FPGA internal identifier unique to every received frame
    ("frameDuration", ctypes.c_uint), #transmit duration of the Ethernet frame, in nanoseconds
    ("dataLen", ctypes.c_ushort), #Overall data length of <frameData>
    ("reserved", ctypes.c_ushort), #currently reserved field - not used, ignore
    ("reserved2", ctypes.c_uint*3), #currently reserved field - not used, ignore
    ("fcs", ctypes.c_uint), #Frame Check Sum
    ("destMAC", ctypes.c_ubyte*xlDefines.XL_ETH_MACADDR_OCTETS), #Destination MAC address
    ("sourceMAC", ctypes.c_ubyte*xlDefines.XL_ETH_MACADDR_OCTETS), #Source MAC address
    ("frameData", s_xl_eth_framedata),
  ]
T_XL_ETH_DATAFRAME_RX = s_xl_eth_dataframe_rx

class s_xl_eth_dataframe_rxerror(ctypes.Structure):
  _anonymous_ = ("frameData",)
  _fields_ = [
    ("frameIdentifier", ctypes.c_uint), #FPGA internal identifier unique to every received frame
    ("frameDuration", ctypes.c_uint), #transmit duration of the Ethernet frame, in nanoseconds
    ("errorFlags", ctypes.c_uint), #Error information (XL_ETH_RX_ERROR_*)
    ("dataLen", ctypes.c_ushort), #Overall data length of <frameData>
    ("reserved", ctypes.c_ushort), #currently reserved field - not used, ignore
    ("reserved2", ctypes.c_uint*3), #currently reserved field - not used, ignore
    ("fcs", ctypes.c_uint), #Frame Check Sum
    ("destMAC", ctypes.c_ubyte*xlDefines.XL_ETH_MACADDR_OCTETS), #Destination MAC address
    ("sourceMAC", ctypes.c_ubyte*xlDefines.XL_ETH_MACADDR_OCTETS), #Source MAC address
    ("frameData", s_xl_eth_framedata),
  ]
T_XL_ETH_DATAFRAME_RX_ERROR = s_xl_eth_dataframe_rxerror

class s_xl_eth_dataframe_tx(ctypes.Structure):
  _anonymous_ = ("frameData",)
  _fields_ = [
    ("frameIdentifier", ctypes.c_uint), #FPGA internal identifier unique to every frame sent
    ("flags", ctypes.c_uint), #Flags to specify (see XL_ETH_DATAFRAME_FLAGS_)
    ("dataLen", ctypes.c_ushort), #Overall data length of <frameData>
    ("reserved", ctypes.c_ushort), #currently reserved field - must be set to "0"
    ("reserved2", ctypes.c_uint*4), #reserved field - must be set to "0"
    ("destMAC", ctypes.c_ubyte*xlDefines.XL_ETH_MACADDR_OCTETS), #Destination MAC address
    ("sourceMAC", ctypes.c_ubyte*xlDefines.XL_ETH_MACADDR_OCTETS), #Source MAC address
    ("frameData", s_xl_eth_framedata),
  ]
T_XL_ETH_DATAFRAME_TX = s_xl_eth_dataframe_tx

class s_xl_eth_dataframe_tx_event(ctypes.Structure):
  _anonymous_ = ("frameData",)
  _fields_ = [
    ("frameIdentifier", ctypes.c_uint), #FPGA internal identifier unique to every frame sent
    ("flags", ctypes.c_uint), #Flags (see XL_ETH_DATAFRAME_FLAGS_)
    ("dataLen", ctypes.c_ushort), #Overall data length of <frameData>
    ("reserved", ctypes.c_ushort), #currently reserved field - not used, ignore
    ("frameDuration", ctypes.c_uint), #transmit duration of the Ethernet frame, in nanoseconds
    ("reserved2", ctypes.c_uint*2), #currently reserved field - not used, ignore
    ("fcs", ctypes.c_uint), #Frame Check Sum
    ("destMAC", ctypes.c_ubyte*xlDefines.XL_ETH_MACADDR_OCTETS), #Destination MAC address
    ("sourceMAC", ctypes.c_ubyte*xlDefines.XL_ETH_MACADDR_OCTETS), #Source MAC address
    ("frameData", s_xl_eth_framedata),
  ]
T_XL_ETH_DATAFRAME_TX_EVENT = s_xl_eth_dataframe_tx_event
T_XL_ETH_DATAFRAME_TXACK = T_XL_ETH_DATAFRAME_TX_EVENT
T_XL_ETH_DATAFRAME_TXACK_SW = T_XL_ETH_DATAFRAME_TX_EVENT
T_XL_ETH_DATAFRAME_TXACK_OTHERAPP = T_XL_ETH_DATAFRAME_TX_EVENT

class s_xl_eth_dataframe_txerror(ctypes.Structure):
  _fields_ = [
    ("errorType", ctypes.c_uint),
    ("txFrame", s_xl_eth_dataframe_tx_event),
  ]
T_XL_ETH_DATAFRAME_TX_ERROR = s_xl_eth_dataframe_txerror
T_XL_ETH_DATAFRAME_TX_ERR_SW = T_XL_ETH_DATAFRAME_TX_ERROR
T_XL_ETH_DATAFRAME_TX_ERR_OTHERAPP = T_XL_ETH_DATAFRAME_TX_ERROR

class s_xl_eth_config_result(ctypes.Structure):
  _fields_ = [
    ("result", ctypes.c_uint),
  ]
T_XL_ETH_CONFIG_RESULT = s_xl_eth_config_result

class s_xl_eth_channel_status(ctypes.Structure):
  _fields_ = [
    ("link", ctypes.c_uint), #(XL_ETH_STATUS_LINK_*)      Ethernet connection status
    ("speed", ctypes.c_uint), #(XL_ETH_STATUS_SPEED_*)     Link connection speed
    ("duplex", ctypes.c_uint), #(XL_ETH_STATUS_DUPLEX_*)    Ethernet duplex mode. 1000Base-T always uses full duplex.
    ("mdiType", ctypes.c_uint), #(XL_ETH_STATUS_MDI_*)       Currently active MDI-mode
    ("activeConnector", ctypes.c_uint), #(XL_ETH_STATUS_CONNECTOR_*) Connector (plug) to use (BroadR-REACH or RJ-45)
    ("activePhy", ctypes.c_uint), #(XL_ETH_STATUS_PHY_*)       Currently active physical layer
    ("clockMode", ctypes.c_uint), #(XL_ETH_STATUS_CLOCK_*)     When in 1000Base-T or BroadR-mode, currently active mode
    ("brPairs", ctypes.c_uint), #(XL_ETH_STATUS_BR_PAIR_*)   When in BroadR-mode, number of used cable pairs
  ]
T_XL_ETH_CHANNEL_STATUS = s_xl_eth_channel_status

class s_xl_eth_txAck(ctypes.Structure):
  _fields_ = [
    ("frameIdentifier", ctypes.c_uint), #FPGA internal identifier unique to every frame sent
    ("fcs", ctypes.c_uint), #Frame Check Sum
    ("sourceMAC", ctypes.c_ubyte*xlDefines.XL_ETH_MACADDR_OCTETS), #Source MAC address
    ("reserved", ctypes.c_ubyte*2), #currently reserved field - not used
  ]
s_xl_eth_txAckSw = s_xl_eth_txAck

class s_xl_eth_txError(ctypes.Structure):
  _fields_ = [
    ("errorType", ctypes.c_uint),
    ("frameIdentifier", ctypes.c_uint), #FPGA internal identifier unique to every frame sent
    ("fcs", ctypes.c_uint), #Frame Check Sum
    ("sourceMAC", ctypes.c_ubyte*xlDefines.XL_ETH_MACADDR_OCTETS), #Source MAC address
    ("reserved", ctypes.c_ubyte*2), #currently reserved field - not used
  ]
s_xl_eth_txErrorSw = s_xl_eth_txError

class u_xl_eth_eventInfo(ctypes.Union):
  _fields_ = [
    ("txAck", s_xl_eth_txAck),
    ("txAckSw", s_xl_eth_txAckSw),
    ("txError", s_xl_eth_txError),
    ("txError", s_xl_eth_txErrorSw),
    ("reserved", ctypes.c_uint*20),
  ]

class s_xl_eth_lostevent(ctypes.Structure):
  _anonymous_ = ("eventInfo",)
  _fields_ = [
    ("eventTypeLost", XLethEventTag), #Type of event lost
    ("reserved", ctypes.c_ushort), #currently reserved field - not used
    ("reason", ctypes.c_uint), #Reason code why the events were lost (0 means unknown)
    ("eventInfo", u_xl_eth_eventInfo),
  ]
T_XL_ETH_LOSTEVENT = s_xl_eth_lostevent

class s_xl_eth_tag_data(ctypes.Union):
  _fields_ = [
    ("rawData", ctypes.c_ubyte*xlDefines.XL_ETH_EVENT_SIZE_MAX),
    ("frameRxOk", s_xl_eth_dataframe_rx), #(tag==XL_ETH_EVENT_TAG_FRAMERX) - Frame received from network
    ("frameRxError", s_xl_eth_dataframe_rxerror), #(tag==XL_ETH_EVENT_TAG_FRAMERX_ERROR) - Erroneous frame received from network
    ("frameTxAck", s_xl_eth_dataframe_tx_event), #(tag==XL_ETH_EVENT_TAG_FRAMETX_ACK) - ACK for frame sent by application
    ("frameTxAckSw", s_xl_eth_dataframe_tx_event), #(tag==XL_ETH_EVENT_TAG_FRAMETX_ACK_SWITCH) - ACK for frame sent by switch
    ("frameTxAckOtherApp", s_xl_eth_dataframe_tx_event), #(tag==XL_ETH_EVENT_TAG_FRAMETX_ERROR_OTHER_APP) - ACK for frame sent by another application
    ("frameTxError", s_xl_eth_dataframe_txerror), #(tag==XL_ETH_EVENT_TAG_FRAMETX_ERROR) - NACK for frame sent by application (frame could not be transmitted)
    ("frameTxErrorSw", s_xl_eth_dataframe_txerror), #(tag==XL_ETH_EVENT_TAG_FRAMETX_ERROR_SWITCH) - NACK for frame sent by switch. May indicate internal processing failure (e.g. queue full condition)
    ("frameTxErrorOtherApp", s_xl_eth_dataframe_txerror), #(tag==XL_ETH_EVENT_TAG_FRAMETX_ERROR_OTHER_APP) - NACK for frame sent by another application
    ("configResult", s_xl_eth_config_result),
    ("channelStatus", s_xl_eth_channel_status),
    ("syncPulse", s_xl_sync_pulse_ev),
    ("lostEvent", s_xl_eth_lostevent), #(tag==XL_ETH_EVENT_TAG_LOSTEVENT) - Indication that one or more events have been lost
  ]

class s_xl_eth_event(ctypes.Structure):
  _anonymous_ = ("tagData",)
  _fields_ = [
    ("size", ctypes.c_uint), #overall size of the complete event, depending on event type and piggybacked data
    ("tag", XLethEventTag), #type of the event
    ("channelIndex", ctypes.c_ushort),
    ("userHandle", ctypes.c_uint),
    ("flagsChip", ctypes.c_ushort),
    ("reserved", ctypes.c_ushort),
    ("reserved1", XLuint64),
    ("timeStampSync", XLuint64), #timestamp which is synchronized by the driver
    ("tagData", s_xl_eth_tag_data),
  ]
T_XL_ETH_EVENT = s_xl_eth_event

class s_xl_net_eth_dataframe_rx(ctypes.Structure):
  _anonymous_ = ("frameData",)
  _fields_ = [
    ("frameDuration", ctypes.c_uint), #Transmit duration of the Ethernet frame, in nanoseconds
    ("dataLen", ctypes.c_ushort), #Overall data length of <frameData>
    ("reserved1", ctypes.c_ubyte), #currently reserved field - not used, ignore
    ("reserved2", ctypes.c_ubyte), #currently reserved field - not used, ignore
    ("errorFlags", ctypes.c_uint), #see XL_ETH_NETWORK_RX_ERROR_xxx and XL_ETH_NETWORK_TX_ERROR_xxx
    ("reserved3", ctypes.c_uint), #currently reserved field - not used, ignore
    ("fcs", ctypes.c_uint), #Frame Check Sum
    ("destMAC", ctypes.c_ubyte*xlDefines.XL_ETH_MACADDR_OCTETS), #Destination MAC address
    ("sourceMAC", ctypes.c_ubyte*xlDefines.XL_ETH_MACADDR_OCTETS), #Source MAC address
    ("frameData", s_xl_eth_framedata),
  ]
T_XL_NET_ETH_DATAFRAME_RX =s_xl_net_eth_dataframe_rx
T_XL_NET_ETH_DATAFRAME_SIMULATION_TX_ACK = T_XL_NET_ETH_DATAFRAME_RX
T_XL_NET_ETH_DATAFRAME_MEASUREMENT_RX = T_XL_NET_ETH_DATAFRAME_RX
T_XL_NET_ETH_DATAFRAME_MEASUREMENT_TX = T_XL_NET_ETH_DATAFRAME_RX

class s_xl_net_eth_dataframe_rx_error(ctypes.Structure):
  _anonymous_ = ("frameData",)
  _fields_ = [
    ("frameDuration", ctypes.c_uint), #Transmit duration of the Ethernet frame, in nanoseconds
    ("errorFlags", ctypes.c_uint), #see XL_ETH_NETWORK_RX_ERROR_xxx and XL_ETH_NETWORK_TX_ERROR_xxx
    ("dataLen", ctypes.c_ushort), #Overall data length of <frameData>
    ("reserved1", ctypes.c_ubyte), #currently reserved field - not used, ignore
    ("reserved2", ctypes.c_ubyte), #currently reserved field - not used, ignore
    ("reserved3", ctypes.c_uint*2), #currently reserved field - not used, ignore
    ("fcs", ctypes.c_uint), #Frame Check Sum
    ("destMAC", ctypes.c_ubyte*xlDefines.XL_ETH_MACADDR_OCTETS), #Destination MAC address
    ("sourceMAC", ctypes.c_ubyte*xlDefines.XL_ETH_MACADDR_OCTETS), #Source MAC address
    ("frameData", s_xl_eth_framedata),
  ]
T_XL_NET_ETH_DATAFRAME_RX_ERROR =s_xl_net_eth_dataframe_rx_error
T_XL_NET_ETH_DATAFRAME_SIMULATION_TX_ERROR = T_XL_NET_ETH_DATAFRAME_RX_ERROR
T_XL_NET_ETH_DATAFRAME_MEASUREMENT_RX_ERROR = T_XL_NET_ETH_DATAFRAME_RX_ERROR
T_XL_NET_ETH_DATAFRAME_MEASUREMENT_TX_ERROR = T_XL_NET_ETH_DATAFRAME_RX_ERROR

T_XL_NET_ETH_DATAFRAME_TX = T_XL_ETH_DATAFRAME_TX

T_XL_NET_ETH_CHANNEL_STATUS = T_XL_ETH_CHANNEL_STATUS

class s_xl_eth_net_tag_data(ctypes.Union):
  _fields_ = [
    ("rawData", ctypes.c_ubyte*xlDefines.XL_ETH_EVENT_SIZE_MAX),
    ("frameSimRx", s_xl_net_eth_dataframe_rx),
    ("frameSimRxError", s_xl_net_eth_dataframe_rx_error),
    ("frameSimTxAck", s_xl_net_eth_dataframe_rx),
    ("frameSimTxError", s_xl_net_eth_dataframe_rx_error),
    ("frameMeasureRx", s_xl_net_eth_dataframe_rx),
    ("frameMeasureRxError", s_xl_net_eth_dataframe_rx_error),
    ("frameMeasureTx", s_xl_net_eth_dataframe_rx),
    ("frameMeasureTxError", s_xl_net_eth_dataframe_rx_error),
    ("channelStatus", s_xl_eth_channel_status),
  ]

class s_xl_net_eth_event(ctypes.Structure):
  _anonymous_ = ("tagData",)
  _fields_ = [
    ("size", ctypes.c_uint), #overall size of the complete event
    ("tag", XLethEventTag), #type of the event
    ("channelIndex", ctypes.c_ushort), #channel index
    ("userHandle", ctypes.c_uint), #application specific user handle
    ("flagsChip", ctypes.c_ushort), #flags
    ("reserved", ctypes.c_ushort), #currently reserved field - not used
    ("reserved1", XLuint64), #currently reserved field - not used
    ("timeStampSync", XLuint64), #synchronized TS by the driver
    ("tagData", s_xl_eth_net_tag_data),
  ]
T_XL_NET_ETH_EVENT = s_xl_net_eth_event

class s_xl_eth_config(ctypes.Structure):
  _fields_ = [
    ("speed", ctypes.c_uint), #(XL_ETH_MODE_SPEED_*)       Connection speed setting
    ("duplex", ctypes.c_uint), #(XL_ETH_MODE_DUPLEX_*)      Duplex mode setting. Not relevant for BroadR-REACH mode, set to "nochange" or "auto".
    ("connector", ctypes.c_uint), #(XL_ETH_MODE_CONNECTOR_*)   Connector to use
    ("phy", ctypes.c_uint), #(XL_ETH_MODE_PHY_*)         Physical interface to enable
    ("clockMode", ctypes.c_uint), #(XL_ETH_MODE_CLOCK_*)       Master or slave clock mode setting (1000Base-T/BroadR-REACH mode only).
    ("mdiMode", ctypes.c_uint), #(XL_ETH_MODE_MDI_*)         Currently active MDI-mode
    ("brPairs", ctypes.c_uint), #(XL_ETH_MODE_BR_PAIR_*)     Number of cable pairs to use (BroadR-REACH mode only).
  ]
T_XL_ETH_CONFIG = s_xl_eth_config

class s_xl_eth_mac_address(ctypes.Structure):
  _fields_ = [
    ("address", ctypes.c_ubyte*xlDefines.XL_ETH_MACADDR_OCTETS),
  ]
T_XL_ETH_MAC_ADDRESS = s_xl_eth_mac_address

class s_xl_most150_event_source(ctypes.Structure):
  _fields_ = [
    ("sourceMask", ctypes.c_uint),
  ]
XL_MOST150_EVENT_SOURCE_EV = s_xl_most150_event_source

class s_xl_most150_device_mode(ctypes.Structure):
  _fields_ = [
    ("deviceMode", ctypes.c_uint),
  ]
XL_MOST150_DEVICE_MODE_EV = s_xl_most150_device_mode

class s_xl_most150_frequency(ctypes.Structure):
  _fields_ = [
    ("frequency", ctypes.c_uint),
  ]
XL_MOST150_FREQUENCY_EV = s_xl_most150_frequency

class s_xl_most150_special_node_info(ctypes.Structure):
  _fields_ = [
    ("changeMask", ctypes.c_uint),
    ("nodeAddress", ctypes.c_ushort),
    ("groupAddress", ctypes.c_ushort),
    ("npr", ctypes.c_ubyte),
    ("mpr", ctypes.c_ubyte),
    ("sbc", ctypes.c_ubyte),
    ("ctrlRetryTime", ctypes.c_ubyte),
    ("ctrlSendAttempts", ctypes.c_ubyte),
    ("asyncRetryTime", ctypes.c_ubyte),
    ("asyncSendAttempts", ctypes.c_ubyte),
    ("macAddr", ctypes.c_ubyte*6),
    ("nprSpy", ctypes.c_ubyte),
    ("mprSpy", ctypes.c_ubyte),
    ("sbcSpy", ctypes.c_ubyte),
    ("inicNIState", ctypes.c_ubyte),
    ("reserved1", ctypes.c_ubyte*3),
    ("reserved2", ctypes.c_uint*3),
  ]
XL_MOST150_SPECIAL_NODE_INFO_EV = s_xl_most150_special_node_info

class s_xl_most150_ctrl_rx(ctypes.Structure):
  _fields_ = [
    ("targetAddress", ctypes.c_ushort),
    ("sourceAddress", ctypes.c_ushort),
    ("fblockId", ctypes.c_ubyte),
    ("instId", ctypes.c_ubyte),
    ("functionId", ctypes.c_ushort),
    ("opType", ctypes.c_ubyte),
    ("telId", ctypes.c_ubyte),
    ("telLen", ctypes.c_ushort),
    ("ctrlData", ctypes.c_ubyte*45),
  ]
XL_MOST150_CTRL_RX_EV = s_xl_most150_ctrl_rx

class s_xl_most150_ctrl_spy(ctypes.Structure):
  _fields_ = [
    ("frameCount", ctypes.c_uint),
    ("msgDuration", ctypes.c_uint), #duration of message transmission in [ns]
    ("priority", ctypes.c_ubyte),
    ("targetAddress", ctypes.c_ushort),
    ("pAck", ctypes.c_ubyte),
    ("ctrlDataLenAnnounced", ctypes.c_ushort),
    ("reserved0", ctypes.c_ubyte),
    ("pIndex", ctypes.c_ubyte),
    ("sourceAddress", ctypes.c_ushort),
    ("reserved1", ctypes.c_ushort),
    ("crc", ctypes.c_ushort),
    ("crcCalculated", ctypes.c_ushort),
    ("cAck", ctypes.c_ubyte),
    ("ctrlDataLen", ctypes.c_ushort), #number of bytes contained in ctrlData[]
    ("reserved2", ctypes.c_ubyte),
    ("status", ctypes.c_uint), #currently not used
    ("validMask", ctypes.c_uint),
    ("ctrlData", ctypes.c_ushort*51),
  ]
XL_MOST150_CTRL_SPY_EV = s_xl_most150_ctrl_spy

class s_xl_most150_async_rx_msg(ctypes.Structure):
  _fields_ = [
    ("length", ctypes.c_ushort),
    ("targetAddress", ctypes.c_ushort),
    ("sourceAddress", ctypes.c_ushort),
    ("asyncData", ctypes.c_ubyte*1524),
  ]
XL_MOST150_ASYNC_RX_EV = s_xl_most150_async_rx_msg

class s_xl_most150_async_spy_msg(ctypes.Structure):
  _fields_ = [
    ("frameCount", ctypes.c_uint),
    ("pktDuration", ctypes.c_uint), #duration of data packet transmission in [ns]
    ("asyncDataLenAnnounced", ctypes.c_ushort),
    ("targetAddress", ctypes.c_ushort),
    ("pAck", ctypes.c_ubyte),
    ("pIndex", ctypes.c_ubyte),
    ("sourceAddress", ctypes.c_ushort),
    ("crc", ctypes.c_uint),
    ("crcCalculated", ctypes.c_uint),
    ("cAck", ctypes.c_ubyte),
    ("asyncDataLen", ctypes.c_ushort), #number of bytes contained in asyncData[]
    ("reserved", ctypes.c_ubyte),
    ("status", ctypes.c_uint), #currently not used
    ("validMask", ctypes.c_uint),
    ("asyncData", ctypes.c_ushort*1524),
  ]
XL_MOST150_ASYNC_SPY_EV = s_xl_most150_async_spy_msg

class s_xl_most150_ethernet_rx(ctypes.Structure):
  _fields_ = [
    ("sourceAddress", ctypes.c_ubyte*6),
    ("targetAddress", ctypes.c_ubyte*6),
    ("length", ctypes.c_uint),
    ("ethernetData", ctypes.c_ubyte*1510),
  ]
XL_MOST150_ETHERNET_RX_EV = s_xl_most150_ethernet_rx

class s_xl_most150_ethernet_spy(ctypes.Structure):
  _fields_ = [
    ("frameCount", ctypes.c_uint),
    ("pktDuration", ctypes.c_uint), #duration of ethernet packet transmission in [ns]
    ("ethernetDataLenAnnounced", ctypes.c_ushort),
    ("targetAddress", ctypes.c_ubyte*6),
    ("pAck", ctypes.c_ubyte),
    ("sourceAddress", ctypes.c_ubyte*6),
    ("reserved0", ctypes.c_ubyte),
    ("crc", ctypes.c_uint),
    ("crcCalculated", ctypes.c_uint),
    ("cAck", ctypes.c_ubyte),
    ("ethernetDataLen", ctypes.c_ushort), #number of bytes contained in ethernetData[]
    ("reserved1", ctypes.c_ubyte),
    ("status", ctypes.c_uint), #currently not used
    ("validMask", ctypes.c_uint),
    ("ethernetData", ctypes.c_ushort*1506),
  ]
XL_MOST150_ETHERNET_SPY_EV = s_xl_most150_ethernet_spy

class s_xl_most150_cl_info(ctypes.Structure):
  _fields_ = [
    ("label", ctypes.c_ushort),
    ("channelWidth", ctypes.c_ushort),
  ]
XL_MOST150_CL_INFO = s_xl_most150_cl_info

class s_xl_most150_sync_alloc_info(ctypes.Structure):
  _fields_ = [
    ("allocTable", s_xl_most150_cl_info*xlDefines.MOST150_SYNC_ALLOC_INFO_SIZE),
  ]
XL_MOST150_SYNC_ALLOC_INFO_EV = s_xl_most150_sync_alloc_info

class s_xl_most150_sync_volume_status(ctypes.Structure):
  _fields_ = [
    ("device", ctypes.c_uint),
    ("volume", ctypes.c_uint),
  ]
XL_MOST150_SYNC_VOLUME_STATUS_EV = s_xl_most150_sync_volume_status

class s_xl_most150_tx_light(ctypes.Structure):
  _fields_ = [
    ("light", ctypes.c_uint),
  ]
XL_MOST150_TX_LIGHT_EV = s_xl_most150_tx_light

class s_xl_most150_rx_light_lock_status(ctypes.Structure):
  _fields_ = [
    ("status", ctypes.c_uint),
  ]
XL_MOST150_RXLIGHT_LOCKSTATUS_EV = s_xl_most150_rx_light_lock_status

class s_xl_most150_error(ctypes.Structure):
  _fields_ = [
    ("errorCode", ctypes.c_uint),
    ("parameter", ctypes.c_uint*3),
  ]
XL_MOST150_ERROR_EV = s_xl_most150_error

class s_xl_most150_configure_rx_buffer(ctypes.Structure):
  _fields_ = [
    ("bufferType", ctypes.c_uint),
    ("bufferMode", ctypes.c_uint),
  ]
XL_MOST150_CONFIGURE_RX_BUFFER_EV = s_xl_most150_configure_rx_buffer

class s_xl_most150_ctrl_sync_audio(ctypes.Structure):
  _fields_ = [
    ("label", ctypes.c_uint),
    ("width", ctypes.c_uint),
    ("device", ctypes.c_uint),
    ("mode", ctypes.c_uint),
  ]
XL_MOST150_CTRL_SYNC_AUDIO_EV = s_xl_most150_ctrl_sync_audio

class s_xl_most150_sync_mute_status(ctypes.Structure):
  _fields_ = [
    ("device", ctypes.c_uint),
    ("mute", ctypes.c_uint),
  ]
XL_MOST150_SYNC_MUTE_STATUS_EV = s_xl_most150_sync_mute_status

class s_xl_most150_tx_light_power(ctypes.Structure):
  _fields_ = [
    ("lightPower", ctypes.c_uint),
  ]
XL_MOST150_LIGHT_POWER_EV = s_xl_most150_tx_light_power

class s_xl_most150_gen_light_error(ctypes.Structure):
  _fields_ = [
    ("stressStarted", ctypes.c_uint),
  ]
XL_MOST150_GEN_LIGHT_ERROR_EV = s_xl_most150_gen_light_error

class s_xl_most150_gen_lock_error(ctypes.Structure):
  _fields_ = [
    ("stressStarted", ctypes.c_uint),
  ]
XL_MOST150_GEN_LOCK_ERROR_EV = s_xl_most150_gen_lock_error

class s_xl_most150_ctrl_busload(ctypes.Structure):
  _fields_ = [
    ("busloadStarted", ctypes.c_uint),
  ]
XL_MOST150_CTRL_BUSLOAD_EV = s_xl_most150_ctrl_busload

class s_xl_most150_async_busload(ctypes.Structure):
  _fields_ = [
    ("busloadStarted", ctypes.c_uint),
  ]
XL_MOST150_ASYNC_BUSLOAD_EV = s_xl_most150_async_busload

class s_xl_most150_systemlock_flag(ctypes.Structure):
  _fields_ = [
    ("state", ctypes.c_uint),
  ]
XL_MOST150_SYSTEMLOCK_FLAG_EV = s_xl_most150_systemlock_flag

class s_xl_most150_shutdown_flag(ctypes.Structure):
  _fields_ = [
    ("state", ctypes.c_uint),
  ]
XL_MOST150_SHUTDOWN_FLAG_EV = s_xl_most150_shutdown_flag

class s_xl_most150_spdif_mode(ctypes.Structure):
  _fields_ = [
    ("spdifMode", ctypes.c_uint),
    ("spdifError", ctypes.c_uint),
  ]
XL_MOST150_SPDIF_MODE_EV = s_xl_most150_spdif_mode

class s_xl_most150_ecl(ctypes.Structure):
  _fields_ = [
    ("eclLineState", ctypes.c_uint),
  ]
XL_MOST150_ECL_EV = s_xl_most150_ecl

class s_xl_most150_ecl_termination(ctypes.Structure):
  _fields_ = [
    ("resistorEnabled", ctypes.c_uint),
  ]
XL_MOST150_ECL_TERMINATION_EV = s_xl_most150_ecl_termination

class s_xl_most150_nw_startup(ctypes.Structure):
  _fields_ = [
    ("error", ctypes.c_uint),
    ("errorInfo", ctypes.c_uint),
  ]
XL_MOST150_NW_STARTUP_EV = s_xl_most150_nw_startup

class s_xl_most150_nw_shutdown(ctypes.Structure):
  _fields_ = [
    ("error", ctypes.c_uint),
    ("errorInfo", ctypes.c_uint),
  ]
XL_MOST150_NW_SHUTDOWN_EV = s_xl_most150_nw_shutdown

class s_xl_most150_stream_state(ctypes.Structure):
  _fields_ = [
    ("streamHandle", ctypes.c_uint),
    ("streamState", ctypes.c_uint),
    ("streamError", ctypes.c_uint),
  ]
XL_MOST150_STREAM_STATE_EV = s_xl_most150_stream_state

class s_xl_most150_stream_tx_buffer(ctypes.Structure):
  _fields_ = [
    ("streamHandle", ctypes.c_uint),
    ("numberOfBytes", ctypes.c_uint),
    ("status", ctypes.c_uint),
  ]
XL_MOST150_STREAM_TX_BUFFER_EV = s_xl_most150_stream_tx_buffer

class s_xl_most150_stream_rx_buffer(ctypes.Structure):
  _fields_ = [
    ("streamHandle", ctypes.c_uint),
    ("numberOfBytes", ctypes.c_uint),
    ("status", ctypes.c_uint),
    ("labelInfo", ctypes.c_uint),
  ]
XL_MOST150_STREAM_RX_BUFFER_EV = s_xl_most150_stream_rx_buffer

class s_xl_most150_stream_tx_underflow(ctypes.Structure):
  _fields_ = [
    ("streamHandle", ctypes.c_uint),
    ("reserved", ctypes.c_uint),
  ]
XL_MOST150_STREAM_TX_UNDERFLOW_EV = s_xl_most150_stream_tx_underflow

class s_xl_most150_stream_tx_label(ctypes.Structure):
  _fields_ = [
    ("streamHandle", ctypes.c_uint),
    ("errorInfo", ctypes.c_uint),
    ("connLabel", ctypes.c_uint),
    ("width", ctypes.c_uint),
  ]
XL_MOST150_STREAM_TX_LABEL_EV = s_xl_most150_stream_tx_label

class s_xl_most150_gen_bypass_stress(ctypes.Structure):
  _fields_ = [
    ("stressStarted", ctypes.c_uint),
  ]
XL_MOST150_GEN_BYPASS_STRESS_EV = s_xl_most150_gen_bypass_stress

class s_xl_most150_ecl_sequence(ctypes.Structure):
  _fields_ = [
    ("sequenceStarted", ctypes.c_uint),
  ]
XL_MOST150_ECL_SEQUENCE_EV = s_xl_most150_ecl_sequence

class s_xl_most150_ecl_glitch_filter(ctypes.Structure):
  _fields_ = [
    ("duration", ctypes.c_uint),
  ]
XL_MOST150_ECL_GLITCH_FILTER_EV = s_xl_most150_ecl_glitch_filter

class s_xl_most150_sso_result(ctypes.Structure):
  _fields_ = [
    ("status", ctypes.c_uint),
  ]
XL_MOST150_SSO_RESULT_EV = s_xl_most150_sso_result

class s_xl_most150_ctrl_tx_ack(ctypes.Structure):
  _fields_ = [
    ("targetAddress", ctypes.c_ushort),
    ("sourceAddress", ctypes.c_ushort),
    ("ctrlPrio", ctypes.c_ubyte),
    ("ctrlSendAttempts", ctypes.c_ubyte),
    ("reserved", ctypes.c_ubyte*2),
    ("status", ctypes.c_uint),
    #ctrlData structure:
    #-----------------------------------------------------------------------
    #FBlockID | InstID | FunctionID | OpType | TelID | TelLen | Payload
    #-----------------------------------------------------------------------
    # 8 bit   | 8 bit  |   12 bit   | 4 bit  | 4 bit | 12 bit | 0 .. 45 byte
    #-----------------------------------------------------------------------
    #ctrlData[0]:   FBlockID
    #ctrlData[1]:   InstID
    #ctrlData[2]:   FunctionID (upper 8 bits)
    #ctrlData[3]:   FunctionID (lower 4 bits) + OpType (4 bits) 
    #ctrlData[4]:   TelId (4 bits) + TelLen (upper 4 bits)
    #ctrlData[5]:   TelLen (lower 8 bits)
    #ctrlData[6..50]: Payload
    ("ctrlData", ctypes.c_ubyte*51),
  ]
XL_MOST150_CTRL_TX_ACK_EV = s_xl_most150_ctrl_tx_ack

class s_xl_most150_async_tx_ack(ctypes.Structure):
  _fields_ = [
    ("priority", ctypes.c_ubyte),
    ("asyncSendAttempts", ctypes.c_ubyte),
    ("length", ctypes.c_ushort),
    ("targetAddress", ctypes.c_ushort),
    ("sourceAddress", ctypes.c_ushort),
    ("status", ctypes.c_uint),
    ("asyncData", ctypes.c_ubyte*1524),
  ]
XL_MOST150_ASYNC_TX_ACK_EV = s_xl_most150_async_tx_ack

class s_xl_most150_ethernet_tx(ctypes.Structure):
  _fields_ = [
    ("priority", ctypes.c_ubyte),
    ("ethSendAttempts", ctypes.c_ubyte),
    ("sourceAddress", ctypes.c_ubyte*6),
    ("targetAddress", ctypes.c_ubyte*6),
    ("reserved", ctypes.c_ubyte*2),
    ("length", ctypes.c_uint),
    ("ethernetData", ctypes.c_ubyte*1510),
  ]
XL_MOST150_ETHERNET_TX_ACK_EV = s_xl_most150_ethernet_tx

class s_xl_most150_hw_sync(ctypes.Structure):
  _fields_ = [
    ("pulseCode", ctypes.c_uint),
  ]
XL_MOST150_HW_SYNC_EV = s_xl_most150_hw_sync

class u_xl_most150_tag_data(ctypes.Union):
  _fields_ = [
    ("rawData", ctypes.c_ubyte*xlDefines.XL_MOST150_MAX_EVENT_DATA_SIZE),
    ("mostEventSource", s_xl_most150_event_source),
    ("mostDeviceMode", s_xl_most150_device_mode),
    ("mostFrequency", s_xl_most150_frequency),
    ("mostSpecialNodeInfo", s_xl_most150_special_node_info),
    ("mostCtrlRx", s_xl_most150_ctrl_rx),
    ("mostCtrlTxAck", s_xl_most150_ctrl_tx_ack),
    ("mostAsyncSpy", s_xl_most150_async_spy_msg),
    ("mostAsyncRx", s_xl_most150_async_rx_msg),
    ("mostSyncAllocInfo", s_xl_most150_sync_alloc_info),
    ("mostSyncVolumeStatus", s_xl_most150_sync_volume_status),
    ("mostTxLight", s_xl_most150_tx_light),
    ("mostRxLightLockStatus", s_xl_most150_rx_light_lock_status),
    ("mostError", s_xl_most150_error),
    ("mostConfigureRxBuffer", s_xl_most150_configure_rx_buffer),
    ("mostCtrlSyncAudio", s_xl_most150_ctrl_sync_audio),
    ("mostSyncMuteStatus", s_xl_most150_sync_mute_status),
    ("mostLightPower", s_xl_most150_tx_light_power),
    ("mostGenLightError", s_xl_most150_gen_light_error),
    ("mostGenLockError", s_xl_most150_gen_lock_error),
    ("mostCtrlBusload", s_xl_most150_ctrl_busload),
    ("mostAsyncBusload", s_xl_most150_async_busload),
    ("mostEthernetRx", s_xl_most150_ethernet_rx),
    ("mostSystemLockFlag", s_xl_most150_systemlock_flag),
    ("mostShutdownFlag", s_xl_most150_shutdown_flag),
    ("mostSpdifMode", s_xl_most150_spdif_mode),
    ("mostEclEvent", s_xl_most150_ecl),
    ("mostEclTermination", s_xl_most150_ecl_termination),
    ("mostCtrlSpy", s_xl_most150_ctrl_spy),
    ("mostAsyncTxAck", s_xl_most150_async_tx_ack),
    ("mostEthernetSpy", s_xl_most150_ethernet_spy),
    ("mostEthernetTxAck", s_xl_most150_ethernet_tx),
    ("mostHWSync", s_xl_most150_hw_sync),
    ("mostStartup", s_xl_most150_nw_startup),
    ("mostShutdown", s_xl_most150_nw_shutdown),
    ("mostStreamState", s_xl_most150_stream_state),
    ("mostStreamTxBuffer", s_xl_most150_stream_tx_buffer),
    ("mostStreamRxBuffer", s_xl_most150_stream_rx_buffer),
    ("mostStreamTxUnderflow", s_xl_most150_stream_tx_underflow),
    ("mostStreamTxLabel", s_xl_most150_stream_tx_label),
    ("mostGenBypassStress", s_xl_most150_gen_bypass_stress),
    ("mostEclSequence", s_xl_most150_ecl_sequence),
    ("mostEclGlitchFilter", s_xl_most150_ecl_glitch_filter),
    ("mostSsoResult", s_xl_most150_sso_result),
  ]

class s_xl_event_most150(ctypes.Structure):
  _anonymous_ = ("tagData",)
  _fields_ = [
    ("size", ctypes.c_uint),
    ("tag", XLmostEventTag),
    ("channelIndex", ctypes.c_ushort),
    ("userHandle", ctypes.c_uint),
    ("flagsChip", ctypes.c_ushort),
    ("reserved", ctypes.c_ushort),
    ("timeStamp", XLuint64),
    ("timeStampSync", XLuint64),
    ("tagData", u_xl_most150_tag_data),
  ]
XLmost150event = s_xl_event_most150

class s_xl_set_most150_special_node_info(ctypes.Structure):
  _fields_ = [
    ("changeMask", ctypes.c_uint), #see XL_MOST150_SPECIAL_NODE_MASK_CHANGED
    ("nodeAddress", ctypes.c_uint),
    ("groupAddress", ctypes.c_uint),
    ("sbc", ctypes.c_uint),
    ("ctrlRetryTime", ctypes.c_uint),
    ("ctrlSendAttempts", ctypes.c_uint),
    ("asyncRetryTime", ctypes.c_uint),
    ("asyncSendAttempts", ctypes.c_uint),
    ("macAddr", ctypes.c_ubyte*6),
  ]
XLmost150SetSpecialNodeInfo = s_xl_set_most150_special_node_info

class s_xl_most150_ctrl_tx_msg(ctypes.Structure):
  _fields_ = [
    ("ctrlPrio", ctypes.c_uint), #Prio: Currently fixed to 0x01 for Control Messages
    ("ctrlSendAttempts", ctypes.c_uint), #1..16 attempts, set an invalid value to use the default value set by xlMost150SetCtrlRetryParameters
    ("targetAddress", ctypes.c_uint),
    #ctrlData structure:
    #-----------------------------------------------------------------------
    #FBlockID | InstID | FunctionID | OpType | TelID | TelLen | Payload
    #-----------------------------------------------------------------------
    # 8 bit   | 8 bit  |   12 bit   | 4 bit  | 4 bit | 12 bit | 0 .. 45 byte
    #-----------------------------------------------------------------------
    #ctrlData[0]:   FBlockID
    #ctrlData[1]:   InstID
    #ctrlData[2]:   FunctionID (upper 8 bits)
    #ctrlData[3]:   FunctionID (lower 4 bits) + OpType (4 bits) 
    #ctrlData[4]:   TelId (4 bits) + TelLen (upper 4 bits)
    #ctrlData[5]:   TelLen (lower 8 bits)
    #ctrlData[6..50]: Payload
    ("ctrlData", ctypes.c_ubyte*51),
  ]
XLmost150CtrlTxMsg = s_xl_most150_ctrl_tx_msg

class s_xl_most150_async_tx_msg(ctypes.Structure):
  _fields_ = [
    ("priority", ctypes.c_uint), #Prio: Currently fixed to 0x00 for MDP /MEP
    ("asyncSendAttempts", ctypes.c_uint), #1..16 attempts,set an invalid value to use the default value set by xlMost150SetAsyncRetryParameters
    ("length", ctypes.c_uint), #max. 1600 bytes
    ("targetAddress", ctypes.c_uint),
    ("asyncData", ctypes.c_ubyte*xlDefines.XL_MOST150_ASYNC_SEND_PAYLOAD_MAX_SIZE),
  ]
XLmost150AsyncTxMsg = s_xl_most150_async_tx_msg

class s_xl_most150_ethernet_tx_msg(ctypes.Structure):
  _fields_ = [
    ("priority", ctypes.c_uint), #Prio: Currently fixed to 0x00 for MDP /MEP
    ("ethSendAttempts", ctypes.c_uint), #1..16 attempts, set an invalid value to use the default value set by xlMost150SetAsyncRetryParameters
    ("sourceAddress", ctypes.c_ubyte*6),
    ("targetAddress", ctypes.c_ubyte*6),
    ("length", ctypes.c_uint), #max. 1600 bytes
    ("ethernetData", ctypes.c_ubyte*xlDefines.XL_MOST150_ETHERNET_SEND_PAYLOAD_MAX_SIZE),
  ]
XLmost150EthernetTxMsg = s_xl_most150_ethernet_tx_msg

class s_xl_most150_sync_audio_parameter(ctypes.Structure):
  _fields_ = [
    ("label", ctypes.c_uint),
    ("width", ctypes.c_uint),
    ("device", ctypes.c_uint),
    ("mode", ctypes.c_uint),
  ]
XLmost150SyncAudioParameter = s_xl_most150_sync_audio_parameter

class s_xl_most150_ctrl_busload_config(ctypes.Structure):
  _fields_ = [
    ("transmissionRate", ctypes.c_uint),
    ("counterType", ctypes.c_uint),
    ("counterPosition", ctypes.c_uint), #counter can be only be set in the payload -> position 0 means first payload byte!
    ("busloadCtrlMsg", s_xl_most150_ctrl_tx_msg),
  ]
XLmost150CtrlBusloadConfig = s_xl_most150_ctrl_busload_config

class u_xl_most150_busloadPkt(ctypes.Union):
  _fields_ = [
    ("rawBusloadPkt", ctypes.c_ubyte*1540),
    ("busloadAsyncPkt", s_xl_most150_async_tx_msg),
    ("busloadEthernetPkt", s_xl_most150_ethernet_tx_msg),
  ]

class s_xl_most150_async_busload_config(ctypes.Structure):
  _anonymous_ = ("busloadPkt",)
  _fields_ = [
    ("busloadType", ctypes.c_uint),
    ("transmissionRate", ctypes.c_uint),
    ("counterType", ctypes.c_uint),
    ("counterPosition", ctypes.c_uint),
    ("busloadPkt", u_xl_most150_busloadPkt),
  ]
XLmost150AsyncBusloadConfig = s_xl_most150_async_busload_config

class s_xl_most150_stream_open(ctypes.Structure):
  _fields_ = [
    ("pStreamHandle", ctypes.POINTER(ctypes.c_uint)),
    ("direction", ctypes.c_uint),
    ("numBytesPerFrame", ctypes.c_uint),
    ("reserved", ctypes.c_uint),
    ("latency", ctypes.c_uint),
  ]
XLmost150StreamOpen = s_xl_most150_stream_open

class s_xl_most150_stream_get_info(ctypes.Structure):
  _fields_ = [
    ("streamHandle", ctypes.c_uint),
    ("numBytesPerFrame", ctypes.c_uint),
    ("direction", ctypes.c_uint),
    ("reserved", ctypes.c_uint),
    ("latency", ctypes.c_uint),
    ("streamState", ctypes.c_uint),
    ("connLabels", ctypes.c_uint*xlDefines.XL_MOST150_STREAM_RX_NUM_CL_MAX),
  ]
XLmost150StreamInfo = s_xl_most150_stream_get_info

class s_xl_can_tx_msg(ctypes.Structure):
  _fields_ = [
    ("canId", ctypes.c_uint),
    ("msgFlags", ctypes.c_uint),
    ("dlc", ctypes.c_ubyte),
    ("reserved", ctypes.c_ubyte*7),
    ("data", ctypes.c_ubyte*xlDefines.XL_CAN_MAX_DATA_LEN),
  ]
XL_CAN_TX_MSG = s_xl_can_tx_msg

class u_xl_can_event_tag_data(ctypes.Union):
  _fields_ = [
    ("canMsg", s_xl_can_tx_msg),
  ]

class s_xl_can_tx_event(ctypes.Structure):
  _anonymous_ = ("tagData",)
  _fields_ = [
    ("tag", ctypes.c_ushort), #type of the event
    ("transId", ctypes.c_ushort),
    ("channelIndex", ctypes.c_ubyte), #internal has to be 0
    ("reserved", ctypes.c_ubyte*3), #has to be zero
    ("tagData", u_xl_can_event_tag_data),
  ]
XLcanTxEvent = s_xl_can_tx_event

class s_xl_can_rx_msg(ctypes.Structure):
  _fields_ = [
    ("canId", ctypes.c_uint),
    ("msgFlags", ctypes.c_uint),
    ("crc", ctypes.c_uint),
    ("reserved1", ctypes.c_ubyte*12),
    ("totalBitCnt", ctypes.c_ushort),
    ("dlc", ctypes.c_ubyte),
    ("reserved", ctypes.c_ubyte*5),
    ("data", ctypes.c_ubyte*xlDefines.XL_CAN_MAX_DATA_LEN),
  ]
XL_CAN_EV_RX_MSG = s_xl_can_rx_msg

class s_xl_can_tx_request(ctypes.Structure):
  _fields_ = [
    ("canId", ctypes.c_uint),
    ("msgFlags", ctypes.c_uint),
    ("dlc", ctypes.c_ubyte),
    ("reserved1", ctypes.c_ubyte),
    ("reserved", ctypes.c_ushort),
    ("data", ctypes.c_ubyte*xlDefines.XL_CAN_MAX_DATA_LEN),
  ]
XL_CAN_EV_TX_REQUEST = s_xl_can_tx_request

class s_xl_can_chip_state(ctypes.Structure):
  _fields_ = [
    ("busStatus", ctypes.c_ubyte),
    ("txErrorCounter", ctypes.c_ubyte),
    ("rxErrorCounter", ctypes.c_ubyte),
    ("reserved", ctypes.c_ubyte),
    ("reserved0", ctypes.c_uint),
  ]
XL_CAN_EV_CHIP_STATE = s_xl_can_chip_state

class s_xl_can_error(ctypes.Structure):
  _fields_ = [
    ("errorCode", ctypes.c_ubyte),
    ("reserved", ctypes.c_ubyte*95),
  ]
XL_CAN_EV_ERROR = s_xl_can_error

class u_xl_can_msg_tag_data(ctypes.Union):
  _fields_ = [
    ("raw", ctypes.c_ubyte*(xlDefines.XL_CANFD_MAX_EVENT_SIZE - xlDefines.XL_CANFD_RX_EVENT_HEADER_SIZE)),
    ("canRxOkMsg", s_xl_can_rx_msg),
    ("canTxOkMsg", s_xl_can_rx_msg),
    ("canTxRequest", s_xl_can_tx_request),
    ("canError", s_xl_can_error),
    ("canChipState", s_xl_can_chip_state),
    ("canSyncPulse", s_xl_sync_pulse_ev),
  ]

class s_xl_can_rx_event(ctypes.Structure):
  _anonymous_ = ("tagData",)
  _fields_ = [
    ("size", ctypes.c_uint),
    ("tag", ctypes.c_ushort),
    ("channelIndex", ctypes.c_ushort),
    ("userHandle", ctypes.c_uint),
    ("flagsChip", ctypes.c_ushort),
    ("reserved0", ctypes.c_ushort),
    ("reserved1", XLuint64),
    ("timeStampSync", XLuint64),
    ("tagData", u_xl_can_msg_tag_data),
  ]
XLcanRxEvent = s_xl_can_rx_event

class s_xl_a429_tx_params(ctypes.Structure):
  _fields_ = [
    ("bitrate", ctypes.c_uint),
    ("parity", ctypes.c_uint),
    ("minGap", ctypes.c_uint),
  ]

class s_xl_a429_rx_params(ctypes.Structure):
  _fields_ = [
    ("bitrate", ctypes.c_uint),
    ("minBitrate", ctypes.c_uint),
    ("maxBitrate", ctypes.c_uint),
    ("parity", ctypes.c_uint),
    ("minGap", ctypes.c_uint),
    ("autoBaudrate", ctypes.c_uint),
  ]

class u_xl_a429_params(ctypes.Union):
  _fields_ = [
    ("tx", s_xl_a429_tx_params),
    ("rx", s_xl_a429_rx_params),
    ("raw", ctypes.c_ubyte*28),
  ]

class s_xl_a429_params(ctypes.Structure):
  _anonymous_ = ("data",)
  _fields_ = [
    ("channelDirection", ctypes.c_ushort),
    ("res1", ctypes.c_ushort),
    ("data", u_xl_a429_params),
  ]
XL_A429_PARAMS = s_xl_a429_params

class s_xl_a429_msg_tx(ctypes.Structure):
  _fields_ = [
    ("userHandle", ctypes.c_ushort),
    ("res1", ctypes.c_ushort),
    ("flags", ctypes.c_uint),
    ("cycleTime", ctypes.c_uint),
    ("gap", ctypes.c_uint),
    ("label", ctypes.c_ubyte),
    ("parity", ctypes.c_ubyte),
    ("res2", ctypes.c_ushort),
    ("data", ctypes.c_uint),
  ]
XL_A429_MSG_TX = s_xl_a429_msg_tx

class s_xl_a429_ev_tx_ok(ctypes.Structure):
  _fields_ = [
    ("frameLength", ctypes.c_uint),
    ("bitrate", ctypes.c_uint),
    ("label", ctypes.c_ubyte),
    ("msgCtrl", ctypes.c_ubyte),
    ("res1", ctypes.c_ushort),
    ("data", ctypes.c_uint),
  ]
XL_A429_EV_TX_OK = s_xl_a429_ev_tx_ok

class s_xl_a429_ev_tx_err(ctypes.Structure):
  _fields_ = [
    ("frameLength", ctypes.c_uint),
    ("bitrate", ctypes.c_uint),
    ("errorPosition", ctypes.c_ubyte),
    ("errorReason", ctypes.c_ubyte),
    ("label", ctypes.c_ubyte),
    ("res1", ctypes.c_ubyte),
    ("data", ctypes.c_uint),
  ]
XL_A429_EV_TX_ERR = s_xl_a429_ev_tx_err

class s_xl_a429_ev_rx_ok(ctypes.Structure):
  _fields_ = [
    ("frameLength", ctypes.c_uint),
    ("bitrate", ctypes.c_uint),
    ("label", ctypes.c_ubyte),
    ("res1", ctypes.c_ubyte*3),
    ("data", ctypes.c_uint),
  ]
XL_A429_EV_RX_OK = s_xl_a429_ev_rx_ok

class s_xl_a429_ev_rx_err(ctypes.Structure):
  _fields_ = [
    ("frameLength", ctypes.c_uint),
    ("bitrate", ctypes.c_uint),
    ("bitLengthOfLastBit", ctypes.c_uint),
    ("errorPosition", ctypes.c_ubyte),
    ("errorReason", ctypes.c_ubyte),
    ("label", ctypes.c_ubyte),
    ("res1", ctypes.c_ubyte),
    ("data", ctypes.c_uint),
  ]
XL_A429_EV_RX_ERR = s_xl_a429_ev_rx_err

class s_xl_a429_ev_bus_statistic(ctypes.Structure):
  _fields_ = [
    ("busLoad", ctypes.c_uint), #0.00-100.00%
    ("res1", ctypes.c_uint*3),
  ]
XL_A429_EV_BUS_STATISTIC = s_xl_a429_ev_bus_statistic

class u_xl_a429_rx_tag_data(ctypes.Union):
  _fields_ = [
    ("a429TxOkMsg", s_xl_a429_ev_tx_ok),
    ("a429TxErrMsg", s_xl_a429_ev_tx_err),
    ("a429RxOkMsg", s_xl_a429_ev_rx_ok),
    ("a429RxErrMsg", s_xl_a429_ev_rx_err),
    ("a429BusStatistic", s_xl_a429_ev_bus_statistic),
    ("a429SyncPulse", s_xl_sync_pulse_ev),
  ]

class s_xl_a429_rx_event(ctypes.Structure):
  _anonymous_ = ("tagData",)
  _fields_ = [
    ("size", ctypes.c_uint), #overall size of the complete event
    ("tag", ctypes.c_ushort), #type of the event
    ("channelIndex", ctypes.c_ubyte),
    ("reserved", ctypes.c_ubyte),
    ("userHandle", ctypes.c_uint), #(lower 12 bit available for CAN)
    ("flagsChip", ctypes.c_ushort), #queue overflow (upper 8bit)
    ("reserved0", ctypes.c_ushort),
    ("timeStamp", XLuint64), #raw timestamp
    ("timeStampSync", XLuint64), #timestamp which is synchronized by the driver
    ("tagData", u_xl_a429_rx_tag_data),
  ]
XLa429RxEvent = s_xl_a429_rx_event

class s_xl_channel_transceiver(ctypes.Structure):
  _fields_ = [
    ("name", ctypes.c_char_p), #name of the transceiver, NULL terminated UTF-8 encoded string
    ("type", ctypes.c_uint),
    ("configError", ctypes.c_uint), #XL_CHANNEL_CONFIG_ERROR_XXX
  ]

class s_xl_channel_drv_config_v1(ctypes.Structure):
  _fields_ = [
    ("hwChannel", ctypes.c_uint), #Index of the channel (same hardware) (0,1,...)
    ("channelIndex", ctypes.c_uint), #Global channel index (0,1,...) in the channel list, on remote devices this is the index of the local administrated channel
    ("deviceIndex", ctypes.c_uint), #The index of the device in the device list
    ("interfaceVersion", ctypes.c_uint), #version of interface with driver
    ("isOnBus", ctypes.c_uint), #The channel is on bus
    ("channelCapabilities", XLuint64), #capabilities which are supported (e.g CHANNEL_FLAG_XXX)
    ("channelCapabilities2", XLuint64),
    ("channelBusCapabilities", XLuint64), #what buses are supported
    ("channelBusActiveCapabilities", XLuint64), #and which are possible to be activated
    ("connectedBusType", XLuint64), #currently selected bus
    ("currentlyAvailableTimestamps", ctypes.c_uint),
    ("busParams", s_xl_bus_params),
    ("transceiver", s_xl_channel_transceiver),
  ]
s_xl_channel_drv_config_v1._fields_.append(("remoteChannel", ctypes.POINTER(s_xl_channel_drv_config_v1)))
XLchannelDrvConfigV1, pXLchannelDrvConfigV1 = s_xl_channel_drv_config_v1, ctypes.POINTER(s_xl_channel_drv_config_v1)

class s_channel_drv_config_list_v1(ctypes.Structure):
  _fields_ = [
    ("item", ctypes.POINTER(s_xl_channel_drv_config_v1)),
    ("count", ctypes.c_uint),
  ]
XLchannelDrvConfigListV1, pXLchannelDrvConfigListV1 = s_channel_drv_config_list_v1, ctypes.POINTER(s_channel_drv_config_list_v1)

class s_xl_device_drv_config_v1(ctypes.Structure):
  _fields_ = [
    ("name", ctypes.c_char_p), #NULL terminated UTF-8 encoded string
    ("hwType", ctypes.c_uint), #HWTYPE_xxxx
    ("hwIndex", ctypes.c_uint), #Index of the hardware (same type) (0,1,...)
    ("serialNumber", ctypes.c_uint),
    ("articleNumber", ctypes.c_uint),
    ("driverVersion", XLuint64), #version of the driver
    ("connectionInfo", ctypes.c_uint), #XL_CONNECTION_INFO_XXX
    ("isRemoteDevice", ctypes.c_uint), #indicates a device of the remote driver config
    ("channelList", s_channel_drv_config_list_v1), #device channel list
  ]
class s_xl_device_drv_config_remote_list(ctypes.Structure):
  _fields_ = [
    ("item", ctypes.POINTER(s_xl_device_drv_config_v1)),
    ("count", ctypes.c_uint),
  ]
#Insert structure
s_xl_device_drv_config_v1._fields_.insert(8, ("remoteDeviceList", s_xl_device_drv_config_remote_list))
XLdeviceDrvConfigV1, pXLdeviceDrvConfigV1 = s_xl_device_drv_config_v1, ctypes.POINTER(s_xl_device_drv_config_v1)

class s_device_drv_config_list_v1(ctypes.Structure):
  _fields_ = [
    ("item", ctypes.POINTER(s_xl_device_drv_config_v1)),
    ("count", ctypes.c_uint),
  ]
XLdeviceDrvConfigListV1, pXLdeviceDrvConfigListV1 = s_device_drv_config_list_v1, ctypes.POINTER(s_device_drv_config_list_v1)

class s_xl_virtual_port_drv_config_v1(ctypes.Structure):
  _fields_ = [
    ("virtualPortName", ctypes.c_char_p), #name of the virtual port, NULL terminated UTF-8 encoded string
    ("networkIdx", ctypes.c_uint), #the index of the network in the network list this vp belongs to
    ("switchId", XLswitchId), #ID of the switch in the network - switches in different networks may have the same switch ID
  ]
XLvirtualportDrvConfigV1, pXLvirtualportDrvConfigV1 = s_xl_virtual_port_drv_config_v1, ctypes.POINTER(s_xl_virtual_port_drv_config_v1)

class s_virtual_port_drv_config_list_v1(ctypes.Structure):
  _fields_ = [
    ("item", ctypes.POINTER(s_xl_virtual_port_drv_config_v1)),
    ("count", ctypes.c_uint),
  ]
XLvirtualportDrvConfigListV1, pXLvirtualportDrvConfigListV1 = s_virtual_port_drv_config_list_v1, ctypes.POINTER(s_virtual_port_drv_config_list_v1)

class s_xl_measurement_point_drv_config_v1(ctypes.Structure):
  _fields_ = [
    ("measurementPointName", ctypes.c_char_p), #name of the measurement point, NULL terminated UTF-8 encoded string
    ("networkIdx", ctypes.c_uint), #the index of the network in the network list this mp belongs to
    ("switchId", XLswitchId), #ID of the switch in the network - switches in different networks may have the same switch ID
    ("channel", s_xl_channel_drv_config_v1), #the hardware channel the MP is connected to
  ]
XLmeasurementpointDrvConfigV1, pXLmeasurementpointDrvConfigV1 = s_xl_measurement_point_drv_config_v1, ctypes.POINTER(s_xl_measurement_point_drv_config_v1)

class s_xl_measurement_point_drv_config_list_v1(ctypes.Structure):
  _fields_ = [
    ("item", ctypes.POINTER(s_xl_measurement_point_drv_config_v1)),
    ("count", ctypes.c_uint),
  ]
XLmeasurementpointDrvConfigListV1, pXLmeasurementpointDrvConfigListV1 = s_xl_measurement_point_drv_config_list_v1, ctypes.POINTER(s_xl_measurement_point_drv_config_list_v1)

class s_xl_switch_drv_config_v1(ctypes.Structure):
  _fields_ = [
    ("switchName", ctypes.c_char_p), #name of the switch, NULL terminated UTF-8 encoded string
    ("switchId", XLswitchId), #ID of the switch in the network - switches in different networks may have the same switch ID
    ("networkIdx", ctypes.c_uint), #the index of the network in the network list this switch belongs to
    ("device", s_xl_device_drv_config_v1), #the device the switch resides on
    ("switchCapability", ctypes.c_uint), #type of the switch "real", TAP or direct connection
    ("vpList", s_virtual_port_drv_config_list_v1), #Virtual Port list
    ("mpList", s_xl_measurement_point_drv_config_list_v1), #Measurement Point list
  ]
XLswitchDrvConfigV1, pXLswitchDrvConfigV1 = s_xl_switch_drv_config_v1, ctypes.POINTER(s_xl_switch_drv_config_v1)

class s_switch_drv_config_list_v1(ctypes.Structure):
  _fields_ = [
    ("item", ctypes.POINTER(s_xl_switch_drv_config_v1)),
    ("count", ctypes.c_uint),
  ]
XLswitchDrvConfigListV1, pXLswitchDrvConfigListV1 = s_switch_drv_config_list_v1, ctypes.POINTER(s_switch_drv_config_list_v1)

class e_xl_network_type(enum.IntEnum):
  ETH_NETWORK = 1
XLnetworkType = e_xl_network_type

class s_xl_network_drv_config_v1(ctypes.Structure):
  _fields_ = [
    ("networkName", ctypes.c_char_p), #name of the network, NULL terminated UTF-8 encoded string
    ("statusCode", ctypes.c_uint), #network configuration error XL_NET_CFG_*
    ("statusErrorString", ctypes.c_char_p), #NULL terminated UTF-8 encoded string that describes statusCode. NULL if no error string exists.
    ("networkType", ctypes.c_int), #ETH_NETWORK - e_xl_network_type
    ("switchList", s_switch_drv_config_list_v1),
  ]
XLnetworkDrvConfigV1, pXLnetworkDrvConfigV1 = s_xl_network_drv_config_v1, ctypes.POINTER(s_xl_network_drv_config_v1)

class s_xl_network_drv_config_list_v1(ctypes.Structure):
  _fields_ = [
    ("item", ctypes.POINTER(s_xl_network_drv_config_v1)),
    ("count", ctypes.c_uint),
  ]
XLnetworkDrvConfigListV1, pXLnetworkDrvConfigListV1 = s_xl_network_drv_config_list_v1, ctypes.POINTER(s_xl_network_drv_config_list_v1)

class s_xl_dll_drv_config_v1(ctypes.Structure):
  _fields_ = [
    ("dllVersion", XLuint64), #version of the loaded DLL instance
  ]
XLdllDrvConfigV1, pXLdllDrvConfigV1 = s_xl_dll_drv_config_v1, ctypes.POINTER(s_xl_dll_drv_config_v1)

class e_xl_driver_config_version(enum.IntEnum):
  IDRIVER_CONFIG_VERSION_1 = 0x8001
XLIdriverConfigVersion = e_xl_driver_config_version

class XLIDriverConfig(ctypes.Structure):
    pass
class _XLdriverConfig(ctypes.Structure):
    pass
XLdrvConfigHandle = ctypes.POINTER(_XLdriverConfig)

if sys.platform.startswith('win'):
    __func_ptr = ctypes.WINFUNCTYPE
else:
    __func_ptr = ctypes.CFUNCTYPE

TP_FCT_XLAPI_GET_CHANNEL_CONFIG_V1 = __func_ptr(XLstatus, XLdrvConfigHandle, pXLchannelDrvConfigListV1)
TP_FCT_XLAPI_GET_DEVICE_CONFIG_V1 = __func_ptr(XLstatus, XLdrvConfigHandle, pXLdeviceDrvConfigListV1)
TP_FCT_XLAPI_GET_VIRTUAL_PORT_CONFIG_V1 = __func_ptr(XLstatus, XLdrvConfigHandle, pXLvirtualportDrvConfigListV1)
TP_FCT_XLAPI_GET_MEASUREMENT_POINT_CONFIG_V1 = __func_ptr(XLstatus, XLdrvConfigHandle, pXLmeasurementpointDrvConfigListV1)
TP_FCT_XLAPI_GET_SWITCH_CONFIG_V1 = __func_ptr(XLstatus, XLdrvConfigHandle, pXLswitchDrvConfigListV1)
TP_FCT_XLAPI_GET_NETWORK_CONFIG_V1 = __func_ptr(XLstatus, XLdrvConfigHandle, pXLnetworkDrvConfigListV1)
TP_FCT_XLAPI_GET_DLL_CONFIG_V1 = __func_ptr(XLstatus, XLdrvConfigHandle, pXLdllDrvConfigV1)

class s_xlapi_driver_config_v1(ctypes.Structure):
  _fields_ = [
    ("configHandle", XLdrvConfigHandle),
    ("fctGetDeviceConfig", TP_FCT_XLAPI_GET_DEVICE_CONFIG_V1),
    ("fctGetChannelConfig", TP_FCT_XLAPI_GET_CHANNEL_CONFIG_V1),
    ("fctGetNetworkConfig", TP_FCT_XLAPI_GET_NETWORK_CONFIG_V1),
    ("fctGetSwitchConfig", TP_FCT_XLAPI_GET_SWITCH_CONFIG_V1),
    ("fctGetVirtualPortConfig", TP_FCT_XLAPI_GET_VIRTUAL_PORT_CONFIG_V1),
    ("fctGetMeasurementPointConfig", TP_FCT_XLAPI_GET_MEASUREMENT_POINT_CONFIG_V1),
    ("fctGetDllConfig", TP_FCT_XLAPI_GET_DLL_CONFIG_V1),
  ]
XLapiIDriverConfigV1, *pXLapiIDriverConfigV1 = s_xlapi_driver_config_v1, ctypes.POINTER(s_xlapi_driver_config_v1)
