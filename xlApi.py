##############################################################################
#                                                                            #
# Module: xlApi                                                              #
# Author: Maximilian Prindl                                                  #
#                                                                            #
# A complete python ctypes wrapper lib for the Vector XL Driver Library.     #
# Contains the #define instructions, struct/union typdef instructions and    #
# function definitions(loads the DLL as well) of the 'vxlapi.h'.             #
#   1)defines are classed into enums(Enum/IntEnum/IntFlag):                  #
#       -> #define XL_BUS_TYPE_CAN can be acessed through XL_BUS_TYPE.CAN    #
#   2)struct and union are classed into ctypes.Structure and ctypes.Union    #
#                                                                            #
##############################################################################
import ctypes
import enum
import sys

class XL_BUS_TYPE(enum.IntFlag):
    NONE     =    0
    CAN      =    1
    LIN      =    2
    FLEXRAY  =    4
    #former BUS_TYPE_BEAN
    AFDX     =    8
    MOST     =   16
    #IO cab/piggy
    DAIO     =   64
    J1708    =  256
    KLINE    = 2048
    ETHERNET = 4096
    A429     = 8192

class XL_TRANSCEIVER_TYPE(enum.IntEnum):
    #Can Cab
    NONE = 0
    CAN_251 = 1
    CAN_252 = 2
    CAN_DNOPTO = 3
    #Prototype. Driver may latch-up.
    CAN_SWC_PROTO = 5
    CAN_SWC = 6
    CAN_EVA = 7
    CAN_FIBER = 8
    #1054 with optical isolation
    CAN_1054_OPTO = 11
    #SWC with optical isolation
    CAN_SWC_OPTO = 12
    #B10011S truck-and-trailer
    CAN_B10011S = 13
    #1050
    CAN_1050 = 14
    #1050 with optical isolation
    CAN_1050_OPTO = 15
    #1041
    CAN_1041 = 16
    #1041 with optical isolation
    CAN_1041_OPTO = 17
    #Virtual CAN Transceiver for Virtual CAN Bus Driver
    CAN_VIRTUAL = 22
    #Vector LINcab 6258opto with transceiver Infineon TLE6258
    LIN_6258_OPTO = 23
    #Vector LINcab 6259opto with transceiver Infineon TLE6259
    LIN_6259_OPTO = 25
    #Vector IOcab 8444  (8 dig.Inp.; 4 dig.Outp.; 4 ana.Inp.; 4 ana.Outp.)
    DAIO_8444_OPTO = 29
    #1041A with optical isolation
    CAN_1041A_OPTO = 33
    #LIN transceiver 6259, with transceiver Infineon TLE6259, magnetically isolated, stress functionality
    LIN_6259_MAG = 35
    #LIN transceiver 7259, with transceiver Infineon TLE7259, magnetically isolated, stress functionality
    LIN_7259_MAG = 37
    #LIN transceiver 7269, with transceiver Infineon TLE7269, magnetically isolated, stress functionality
    LIN_7269_MAG = 39
    #TJA1054, magnetically isolated, with selectable termination resistor (via 4th IO line)
    CAN_1054_MAG = 51
    #82C250/251 or equivalent, magnetically isolated
    CAN_251_MAG = 53
    #TJA1050, magnetically isolated
    CAN_1050_MAG = 55
    #TJA1040, magnetically isolated
    CAN_1040_MAG = 57
    #TJA1041A, magnetically isolated
    CAN_1041A_MAG = 59
    #TWINcab with two TJA1041, magnetically isolated
    TWIN_CAN_1041A_MAG = 128
    #TWINcab with two 7259, Infineon TLE7259, magnetically isolated, stress functionality
    TWIN_LIN_7269_MAG = 129
    #TWINcab with two TJA1041, magnetically isolated
    TWIN_CAN_1041AV2_MAG = 130
    #TWINcab with TJA1054A and TJA1041A with magnetic isolation
    TWIN_CAN_1054_1041A_MAG = 131
    #Can PiggyBack
    PB_CAN_251 = 257
    PB_CAN_1054 = 259
    PB_CAN_251_OPTO = 261
    PB_CAN_SWC = 267
    PB_CAN_1054_OPTO = 277
    PB_CAN_SWC_OPTO = 279
    PB_CAN_TT_OPTO = 281
    PB_CAN_1050 = 283
    PB_CAN_1050_OPTO = 285
    PB_CAN_1041 = 287
    PB_CAN_1041_OPTO = 289
    #LIN piggy back with transceiver Infineon TLE6258
    PB_LIN_6258_OPTO = 297
    #LIN piggy back with transceiver Infineon TLE6259
    PB_LIN_6259_OPTO = 299
    #LIN piggy back with transceiver Infineon TLE6259, magnetically isolated, stress functionality
    PB_LIN_6259_MAG = 301
    #CAN transceiver 1041A
    PB_CAN_1041A_OPTO = 303
    #LIN piggy back with transceiver Infineon TLE7259, magnetically isolated, stress functionality
    PB_LIN_7259_MAG = 305
    #LIN piggy back with transceiver Infineon TLE7269, magnetically isolated, stress functionality
    PB_LIN_7269_MAG = 307
    #82C250/251 or compatible, magnetically isolated
    PB_CAN_251_MAG = 309
    #TJA 1050, magnetically isolated
    PB_CAN_1050_MAG = 310
    #TJA 1040, magnetically isolated
    PB_CAN_1040_MAG = 311
    #TJA 1041A, magnetically isolated
    PB_CAN_1041A_MAG = 312
    #optically isolated IO piggy
    PB_DAIO_8444_OPTO = 313
    #TJA1054, magnetically isolated, with selectable termination resistor (via 4th IO line)
    PB_CAN_1054_MAG = 315
    #TJA1051 - fixed transceiver on e.g. 16xx/8970
    CAN_1051_CAP_FIX = 316
    #Onboard IO of VN1630/VN1640
    DAIO_1021_FIX = 317
    #TLE7269 - fixed transceiver on VN1611
    LIN_7269_CAP_FIX = 318
    #TJA 1051, capacitive isolated
    PB_CAN_1051_CAP = 319
    #Single Wire NCV7356, capacitive isolated
    PB_CAN_SWC_7356_CAP = 320
    #TJA1055, capacitive isolated, with selectable termination resistor (via 4th IO line)
    PB_CAN_1055_CAP = 321
    #TJA 1057, capacitive isolated
    PB_CAN_1057_CAP = 322
    #Onboard HOLT 8596 TX transceiver on VN0601
    A429_HOLT8596_FIX = 323
    #Onboard HOLT 8455 RX transceiver on VN0601
    A429_HOLT8455_FIX = 324
    #TJA 1051HG, capacitive isolated
    PB_CAN_1051HG_CAP = 325
    #TJA 1057 - fixed transceiver on e.g. VN1530, VN4610
    CAN_1057_FIX = 326
    #TLE7269 - fixed transceiver on VN1531
    LIN_7269_FIX = 327
    PB_CAN_1462BT = 329
    #FlexRay PiggyBacks
    #TJA 1080
    PB_FR_1080 = 513
    #TJA 1080 magnetically isolated piggy
    PB_FR_1080_MAG = 514
    #TJA 1080A magnetically isolated piggy
    PB_FR_1080A_MAG = 515
    #TJA 1082 capacitive isolated piggy
    PB_FR_1082_CAP = 516
    #TJA 1082 capacitive isolated piggy with CANpiggy form factor
    PB_FRC_1082_CAP = 517
    #TJA 1082 capacitive isolated piggy fixed transceiver - e.g. 7610
    FR_1082_CAP_FIX = 518
    #Onboard MOST150 transceiver of VN2640
    MOST150_ONBOARD = 544
    #Ethernet Phys
    #Onboard Broadcom Ethernet PHY on VN5610 and VX0312
    ETH_BCM54810_FIX = 560
    #Onboard Atheros Ethernet PHY
    ETH_AR8031_FIX = 561
    #Onboard Broadcom Ethernet PHY
    ETH_BCM89810_FIX = 562
    #Onboard NXP Ethernet PHY
    ETH_TJA1100_FIX = 563
    #Onboard Broadcom Ethernet PHYs (e.g. VN5610A - BCM54810: RJ45, BCM89811: DSUB)
    ETH_BCM54810_89811_FIX = 564
    #Onboard TI 1000BASE-T1 Eth PHY
    ETH_DP83XG710Q1_FIX = 565
    #Onboard Broadcom Ethernet PHY on VN7640 and VH6501
    ETH_BCM54811S_FIX = 566
    #Onboard Realtek Eth PHY
    ETH_RTL9000AA_FIX = 567
    #Onboard Broadcom Ethernet PHY
    ETH_BCM89811_FIX = 568
    #Onboard Broadcom BCM54210
    ETH_BCM54210_FIX = 569
    #Onboard Marvell 88Q2112
    ETH_88Q2112_FIX = 570
    #Onboard Broadcom BCM84891
    ETH_BCM84891_FIX = 571
    #IOpiggy 8642
    #Iopiggy for VN8900
    PB_DAIO_8642 = 640
    #virtual piggy type for activation line only (e.g. VN8810ini)
    DAIO_AL_ONLY = 655
    #On board IO with Activation Line (e.g. VN5640)
    DAIO_1021_FIX_WITH_AL = 656
    #virtual piggy type for activation line and WakeUp Line only (e.g. VN5610A/VN5620)
    DAIO_AL_WU = 657
    #On board IO with 2nd output (e.g. 5V CMOS @ VN4610)
    DAIO_1021_FIX_WITH_5V = 658
    #Eth modules
    #BroadR-Reach Module with 2x Broadcom BCM89810
    ETH_MOD_BR_BCM89810 = 768
    #IEEE802.3 RGMII Module with 2x Atheros AR8031
    ETH_MOD_IEEE_RGMII_AR8031 = 769
    #IEEE802.3 SGMII Module with 2x Atheros AR8031
    ETH_MOD_IEEE_SGMII_AR8031 = 770
    #BroadR-Reach Module with 2x NXP TJA1100
    ETH_MOD_BR_TJA1100 = 771
    #BroadR-Reach Module with 2x Realtek RTL9000-AA
    ETH_MOD_BR_RTL9000AA = 772
    #1Gbit (1000BASE-T1) SGMII Module with 2x TI DP83GX710-Q1
    ETH_MOD_BR_SGMII_DP83XG710Q1 = 773
    #BroadR-Reach Module with 2x Marvell 88Q2112
    ETH_MOD_BR_88Q2112 = 774
    #BroadR-Reach Module with 2x Broadcom BCM89811
    ETH_MOD_BR_BCM89811 = 775
    #100BASE-T1 Module with 2x NXP TJA1101
    ETH_MOD_BR_TJA1101 = 776
    #AE modules
    #100/1000BASE-T1 Module with 4x Broadcom BCM89883
    AE_MOD_BR_BCM89883 = 1025
    #VT Ethernet piggy
    #100BASE-T1 piggy with 6x NXP TJA1101
    PB_ETH_100BASET1_TJA1101 = 8066
    #1000BASE-T1 piggy with 6x Marvell 88Q2112
    PB_ETH_1000BASET1_88Q2112 = 8067

class XL_TRANSCEIVER_LINEMODE(enum.IntEnum):
    NA = 0
    TWO_LINE = 1
    CAN_H = 2
    CAN_L = 3
    #SWC Sleep Mode
    SWC_SLEEP = 4
    #SWC Normal Mode
    SWC_NORMAL = 5
    #SWC High-Speed Mode
    SWC_FAST = 6
    #SWC Wakeup Mode
    SWC_WAKEUP = 7
    SLEEP = 8
    NORMAL = 9
    #Standby for those who support it
    STDBY = 10
    #truck & trailer: operating mode single wire using CAN high
    TT_CAN_H = 11
    #truck & trailer: operating mode single wire using CAN low
    TT_CAN_L = 12
    #CANcab Eva
    EVA_00 = 13
    #CANcab Eva
    EVA_01 = 14
    #CANcab Eva
    EVA_10 = 15
    #CANcab Eva
    EVA_11 = 16

class XL_TRANSCEIVER_STATUS(enum.IntFlag):
    PRESENT = 1
    POWER_GOOD = 16
    EXT_POWER_GOOD = 32
    NOT_SUPPORTED = 64

class XL_DRIVER_STATUS(enum.IntEnum):
    SUCCESS = 0
    PENDING = 1
    ERR_QUEUE_IS_EMPTY = 10
    ERR_QUEUE_IS_FULL = 11
    ERR_TX_NOT_POSSIBLE = 12
    ERR_NO_LICENSE = 14
    ERR_WRONG_PARAMETER = 101
    ERR_TWICE_REGISTER = 110
    ERR_INVALID_CHAN_INDEX = 111
    ERR_INVALID_ACCESS = 112
    ERR_PORT_IS_OFFLINE = 113
    ERR_CHAN_IS_ONLINE = 116
    ERR_NOT_IMPLEMENTED = 117
    ERR_INVALID_PORT = 118
    ERR_HW_NOT_READY = 120
    ERR_CMD_TIMEOUT = 121
    ERR_CMD_HANDLING = 122
    ERR_HW_NOT_PRESENT = 129
    ERR_NOTIFY_ALREADY_ACTIVE = 131
    ERR_INVALID_TAG = 132
    ERR_INVALID_RESERVED_FLD = 133
    ERR_INVALID_SIZE = 134
    ERR_INSUFFICIENT_BUFFER = 135
    ERR_ERROR_CRC = 136
    ERR_BAD_EXE_FORMAT = 137
    ERR_NO_SYSTEM_RESOURCES = 138
    ERR_NOT_FOUND = 139
    ERR_INVALID_ADDRESS = 140
    ERR_REQ_NOT_ACCEP = 141
    ERR_INVALID_LEVEL = 142
    ERR_NO_DATA_DETECTED = 143
    ERR_INTERNAL_ERROR = 144
    ERR_UNEXP_NET_ERR = 145
    ERR_INVALID_USER_BUFFER = 146
    ERR_INVALID_PORT_ACCESS_TYPE = 147
    ERR_NO_RESOURCES = 152
    ERR_WRONG_CHIP_TYPE = 153
    ERR_WRONG_COMMAND = 154
    ERR_INVALID_HANDLE = 155
    ERR_RESERVED_NOT_ZERO = 157
    ERR_INIT_ACCESS_MISSING = 158
    ERR_WRONG_VERSION = 160
    ERR_CANNOT_OPEN_DRIVER = 201
    ERR_WRONG_BUS_TYPE = 202
    ERR_DLL_NOT_FOUND = 203
    ERR_INVALID_CHANNEL_MASK = 204
    ERR_NOT_SUPPORTED = 205
    ERR_CONNECTION_BROKEN = 210
    ERR_CONNECTION_CLOSED = 211
    ERR_INVALID_STREAM_NAME = 212
    ERR_CONNECTION_FAILED = 213
    ERR_STREAM_NOT_FOUND = 214
    ERR_STREAM_NOT_CONNECTED = 215
    ERR_QUEUE_OVERRUN = 216
    ERROR = 255
    #Too many PDUs configured or too less system memory free
    ERR_PDU_OUT_OF_MEMORY = 260
    #No cluster configuration has been sent to the driver but is needed for the command which failed
    ERR_FR_CLUSTERCONFIG_MISSING = 261
    #Invalid offset and/or repetition value specified
    ERR_PDU_OFFSET_REPET_INVALID = 262
    #Specified PDU payload size is invalid (e.g. size is too large) Frame-API: size is different than static payload length configured in cluster config
    ERR_PDU_PAYLOAD_SIZE_INVALID = 263
    #Too many frames specified in parameter
    ERR_FR_NBR_FRAMES_OVERFLOW = 265
    #Specified slot-ID exceeds biggest possible ID specified by the cluster configuration
    ERR_FR_SLOT_ID_INVALID = 267
    #Specified slot cannot be used by Coldstart-Controller because it's already in use by the eRay
    ERR_FR_SLOT_ALREADY_OCCUPIED_BY_ERAY = 268
    #Specified slot cannot be used by eRay because it's already in use by the Coldstart-Controller
    ERR_FR_SLOT_ALREADY_OCCUPIED_BY_COLDC = 269
    #Specified slot cannot be used because it's already in use by another application
    ERR_FR_SLOT_OCCUPIED_BY_OTHER_APP = 270
    #Specified slot is not in correct segment. E.g.: A dynamic slot was specified for startup&sync
    ERR_FR_SLOT_IN_WRONG_SEGMENT = 271
    #The given frame-multiplexing rule (specified by offset and repetition) cannot be done because some of the slots are already in use
    ERR_FR_FRAME_CYCLE_MULTIPLEX_ERROR = 272
    #Unmapping of eRay startup/sync frames is not allowed
    ERR_PDU_NO_UNMAP_OF_SYNCFRAME = 278
    #Wrong txMode in sync frame
    ERR_SYNC_FRAME_MODE = 291
    #DLC with invalid value
    ERR_INVALID_DLC = 513
    #CAN Id has invalid bits set
    ERR_INVALID_CANID = 514
    #flag set that must not be set when configured for CAN20 (e.g. EDL)
    ERR_INVALID_FDFLAG_MODE20 = 515
    #RTR must not be set in combination with EDL
    ERR_EDL_RTR = 516
    #EDL is not set but BRS and/or ESICTRL is
    ERR_EDL_NOT_SET = 517
    #unknown bit in flags field is set
    ERR_UNKNOWN_FLAG = 518
    ERR_ETH_PHY_ACTIVATION_FAILED = 4352
    ERR_ETH_PHY_CONFIG_ABORTED = 4355
    ERR_ETH_RESET_FAILED = 4356
    #Requested config was stored but could not be immediately activated
    ERR_ETH_SET_CONFIG_DELAYED = 4357
    #Requested feature/function not supported by device
    ERR_ETH_UNSUPPORTED_FEATURE = 4358
    ERR_ETH_MAC_ACTIVATION_FAILED = 4359
    #Switch has already been activated
    ERR_NET_ETH_SWITCH_IS_ONLINE = 4364

class XL_EVENT_TYPE(enum.IntEnum):
    NO_COMMAND = 0
    RECEIVE_MSG = 1
    CHIP_STATE = 4
    TRANSCEIVER = 6
    TIMER = 8
    TRANSMIT_MSG = 10
    SYNC_PULSE = 11
    APPLICATION_NOTIFICATION = 15
    LIN_MSG = 20
    LIN_ERRMSG = 21
    LIN_SYNCERR = 22
    LIN_NOANS = 23
    LIN_WAKEUP = 24
    LIN_SLEEP = 25
    LIN_CRCINFO = 26
    #D/A IO data message
    RECEIVE_DAIO_DATA = 32
    #D/A IO Piggy data message
    RECEIVE_DAIO_PIGGY = 34
    KLINE_MSG = 36

class XL_EVENT_TAGS(enum.IntEnum):
    #Common event tags
    RECEIVE_MSG = 1
    CHIP_STATE = 4
    TRANSCEIVER_INFO = 6
    TRANSCEIVER = TRANSCEIVER_INFO
    TIMER_EVENT = 8
    TIMER = TIMER_EVENT
    TRANSMIT_MSG = 0xA
    SYNC_PULSE = 0xB
    APPLICATION_NOTIFICATION = 0xF
    #LIN event tags
    LIN_MSG = 0x0014
    LIN_ERRMSG = 0x0015
    LIN_SYNCERR = 0x0016
    LIN_NOANS = 0x0017
    LIN_WAKEUP = 0x0018
    LIN_SLEEP = 0x0019
    LIN_CRCINFO = 0x001A
    #DAIO event tags
    #D/A IO data message
    RECEIVE_DAIO_DATA = 0x20
    KLINE_MSG = 0x24
    #FlexRay event tags
    FR_START_CYCLE = 128
    FR_RX_FRAME = 129
    FR_TX_FRAME = 130
    FR_TXACK_FRAME = 131
    FR_INVALID_FRAME = 132
    FR_WAKEUP = 133
    FR_SYMBOL_WINDOW = 134
    FR_ERROR = 135
    FR_ERROR_POC_MODE = 1
    FR_ERROR_SYNC_FRAMES_BELOWMIN = 2
    FR_ERROR_SYNC_FRAMES_OVERLOAD = 3
    FR_ERROR_CLOCK_CORR_FAILURE = 4
    FR_ERROR_NIT_FAILURE = 5
    FR_ERROR_CC_ERROR = 6
    FR_STATUS = 136
    FR_NM_VECTOR = 138
    FR_TRANCEIVER_STATUS = 139
    FR_SPY_FRAME = 142
    FR_SPY_SYMBOL = 143
    #MOST25 event tags
    MOST_START = 257
    MOST_STOP = 258
    MOST_EVENTSOURCES = 259
    MOST_ALLBYPASS = 263
    MOST_TIMINGMODE = 264
    MOST_FREQUENCY = 265
    MOST_REGISTER_BYTES = 266
    MOST_REGISTER_BITS = 267
    MOST_SPECIAL_REGISTER = 268
    MOST_CTRL_RX_SPY = 269
    MOST_CTRL_RX_OS8104 = 270
    MOST_CTRL_TX = 271
    MOST_ASYNC_MSG = 272
    MOST_ASYNC_TX = 273
    MOST_SYNC_ALLOCTABLE = 274
    MOST_SYNC_VOLUME_STATUS = 278
    MOST_RXLIGHT = 279
    MOST_TXLIGHT = 280
    MOST_LOCKSTATUS = 281
    MOST_ERROR = 282
    MOST_CTRL_RXBUFFER = 284
    MOST_SYNC_TX_UNDERFLOW = 285
    MOST_SYNC_RX_OVERFLOW = 286
    MOST_CTRL_SYNC_AUDIO = 287
    MOST_SYNC_MUTE_STATUS = 288
    MOST_GENLIGHTERROR = 289
    MOST_GENLOCKERROR = 290
    MOST_TXLIGHT_POWER = 291
    MOST_CTRL_BUSLOAD = 294
    MOST_ASYNC_BUSLOAD = 295
    MOST_CTRL_SYNC_AUDIO_EX = 298
    MOST_TIMINGMODE_SPDIF = 299
    MOST_STREAM_STATE = 300
    MOST_STREAM_BUFFER = 301
    #MOST150 event tags
    START = 512
    STOP = 513
    MOST150_EVENT_SOURCE = 515
    MOST150_DEVICE_MODE = 516
    MOST150_SYNC_ALLOC_INFO = 517
    MOST150_FREQUENCY = 518
    MOST150_SPECIAL_NODE_INFO = 519
    MOST150_CTRL_RX = 520
    MOST150_CTRL_TX_ACK = 521
    MOST150_ASYNC_SPY = 522
    MOST150_ASYNC_RX = 523
    MOST150_SYNC_VOLUME_STATUS = 525
    MOST150_TX_LIGHT = 526
    MOST150_RXLIGHT_LOCKSTATUS = 527
    MOST150_ERROR = 528
    MOST150_CONFIGURE_RX_BUFFER = 529
    MOST150_CTRL_SYNC_AUDIO = 530
    MOST150_SYNC_MUTE_STATUS = 531
    MOST150_LIGHT_POWER = 532
    MOST150_GEN_LIGHT_ERROR = 533
    MOST150_GEN_LOCK_ERROR = 534
    MOST150_CTRL_BUSLOAD = 535
    MOST150_ASYNC_BUSLOAD = 536
    MOST150_ETHERNET_RX = 537
    MOST150_SYSTEMLOCK_FLAG = 538
    MOST150_SHUTDOWN_FLAG = 539
    MOST150_CTRL_SPY = 540
    MOST150_ASYNC_TX_ACK = 541
    MOST150_ETHERNET_SPY = 542
    MOST150_ETHERNET_TX_ACK = 543
    MOST150_SPDIFMODE = 544
    MOST150_ECL_LINE_CHANGED = 546
    MOST150_ECL_TERMINATION_CHANGED = 547
    MOST150_NW_STARTUP = 548
    MOST150_NW_SHUTDOWN = 549
    MOST150_STREAM_STATE = 550
    MOST150_STREAM_TX_BUFFER = 551
    MOST150_STREAM_RX_BUFFER = 552
    MOST150_STREAM_TX_LABEL = 553
    MOST150_STREAM_TX_UNDERFLOW = 555
    MOST150_GEN_BYPASS_STRESS = 556
    MOST150_ECL_SEQUENCE = 557
    MOST150_ECL_GLITCH_FILTER = 558
    MOST150_SSO_RESULT = 559
    #CAN/CAN-FD event tags (rx)
    CAN_EV_TAG_RX_OK = 1024
    CAN_EV_TAG_RX_ERROR = 1025
    CAN_EV_TAG_TX_ERROR = 1026
    CAN_EV_TAG_TX_REQUEST = 1027
    CAN_EV_TAG_TX_OK = 1028
    CAN_EV_TAG_CHIP_STATE = 1033
    #CAN/CAN-FD event tags (tx)
    CAN_EV_TAG_TX_MSG = 1088
    #Ethernet event tags
    #Event data type T_XL_ETH_DATAFRAME_RX
    ETH_EVENT_TAG_FRAMERX = 1280
    #Event data type T_XL_ETH_DATAFRAME_RX_ERROR
    ETH_EVENT_TAG_FRAMERX_ERROR = 1281
    #Event data type T_XL_ETH_DATAFRAME_TX_ERROR
    ETH_EVENT_TAG_FRAMETX_ERROR = 1286
    #Event data type T_XL_ETH_DATAFRAME_TX_ERR_SW
    ETH_EVENT_TAG_FRAMETX_ERROR_SWITCH = 1287
    #Event data type T_XL_ETH_DATAFRAME_TXACK
    ETH_EVENT_TAG_FRAMETX_ACK = 1296
    #Event data type T_XL_ETH_DATAFRAME_TXACK_SW
    ETH_EVENT_TAG_FRAMETX_ACK_SWITCH = 1297
    #Event data type T_XL_ETH_DATAFRAME_TXACK_OTHERAPP
    ETH_EVENT_TAG_FRAMETX_ACK_OTHER_APP = 1299
    #Event data type T_XL_ETH_DATAFRAME_TX_ERR_OTHERAPP
    ETH_EVENT_TAG_FRAMETX_ERROR_OTHER_APP = 1300
    #Event data type T_XL_ETH_CHANNEL_STATUS
    ETH_EVENT_TAG_CHANNEL_STATUS = 1312
    #Event data type T_XL_ETH_CONFIG_RESULT
    ETH_EVENT_TAG_CONFIGRESULT = 1328
    #Event data type T_XL_ETH_DATAFRAME_RX_SIMULATION  (with payload)
    ETH_EVENT_TAG_FRAMERX_SIMULATION = 1360
    #Event data type T_XL_ETH_DATAFRAME_RX_ERROR_SIMULATION (with payload)
    ETH_EVENT_TAG_FRAMERX_ERROR_SIMULATION = 1361
    #Event data type T_XL_ETH_DATAFRAME_TX_SIMULATION (with payload)
    ETH_EVENT_TAG_FRAMETX_ACK_SIMULATION = 1362
    #Event data type T_XL_ETH_DATAFRAME_TX_ERROR_SIMULATION (with payload)
    ETH_EVENT_TAG_FRAMETX_ERROR_SIMULATION = 1363
    #Event data type T_XL_ETH_DATAFRAME_RX_MEASUREMENT  (with payload)
    ETH_EVENT_TAG_FRAMERX_MEASUREMENT = 1376
    #Event data type T_XL_ETH_DATAFRAME_RX_ERROR_MEASUREMENT (with payload)
    ETH_EVENT_TAG_FRAMERX_ERROR_MEASUREMENT = 1377
    #Event data type T_XL_ETH_DATAFRAME_TX_MEASUREMENT (with payload)
    ETH_EVENT_TAG_FRAMETX_MEASUREMENT = 1378
    #Event data type T_XL_ETH_DATAFRAME_TX_ERROR_MEASUREMENT (with payload)
    ETH_EVENT_TAG_FRAMETX_ERROR_MEASUREMENT = 1379
    #Indication that one or more intended events could not be generated. Event data type T_XL_ETH_LOSTEVENT
    ETH_EVENT_TAG_LOSTEVENT = 1534
    #Generic error
    ETH_EVENT_TAG_ERROR = 1535
    #ARINC429 event tags
    A429_EV_TAG_TX_OK = 1536
    A429_EV_TAG_TX_ERR = 1537
    A429_EV_TAG_RX_OK = 1544
    A429_EV_TAG_RX_ERR = 1545
    A429_EV_TAG_BUS_STATISTIC = 1551

XLuint64 = ctypes.c_ulonglong

XLlong = ctypes.c_long

XLulong = ctypes.c_ulong

class XL_NOTIFY_REASON(enum.IntEnum):
    CHANNEL_ACTIVATION = 1
    CHANNEL_DEACTIVATION = 2
    PORT_CLOSED = 3

class s_xl_application_notification(ctypes.Structure):
    _fields_ = [
        ("notifyReason", ctypes.c_uint),
        ("reserved", ctypes.c_uint*7),
    ]
XL_APPLICATION_NOTIFICATION_EV = s_xl_application_notification

class XL_SYNC_PULSE(enum.IntEnum):
    EXTERNAL = 0
    OUR = 1
    OUR_SHARED = 2

#definition of the sync pulse event for xl interface versions V3 and higher
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
#definition of the sync pulse event for xl interface versions V1 and V2
class s_xl_sync_pulse(ctypes.Structure):
    _fields_ = [
        ("pulseCode", ctypes.c_ubyte),
        ("time", XLuint64),
    ]

class XL_HWTYPE(enum.IntEnum):
    NONE = 0
    VIRTUAL = 1
    CANCARDX = 2
    CANAC2PCI = 6
    CANCARDY = 12
    CANCARDXL = 15
    CANCASEXL = 21
    CANCASEXL_LOG_OBSOLETE = 23
    #CANboardXL, CANboardXL PCIe
    CANBOARDXL = 25
    #CANboardXL pxi
    CANBOARDXL_PXI = 27
    VN2600 = 29
    VN2610 = VN2600
    VN3300 = 37
    VN3600 = 39
    VN7600 = 41
    CANCARDXLE = 43
    VN8900 = 45
    VN8950 = 47
    VN2640 = 53
    VN1610 = 55
    VN1630 = 57
    VN1640 = 59
    VN8970 = 61
    VN1611 = 63
    VN5240 = 64
    VN5610 = 65
    VN5620 = 66
    VN7570 = 67
    VN5650 = 68
    IPCLIENT = 69
    IPSERVER = 71
    VX1121 = 73
    VX1131 = 75
    VT6204 = 77
    VN1630_LOG = 79
    VN7610 = 81
    VN7572 = 83
    VN8972 = 85
    VN0601 = 87
    VN5640 = 89
    VX0312 = 91
    VH6501 = 94
    VN8800 = 95
    IPCL8800 = 96
    IPSRV8800 = 97
    CSMCAN = 98
    VN5610A = 101
    VN7640 = 102
    VX1135 = 104
    VN4610 = 105
    VT6306 = 107
    VT6104A = 108
    VN5430 = 109
    VTSSERVICE = 110
    VN1530 = 112
    VN1531 = 113
    VX1161A = 114
    VX1161B = 115
    MAX_HWTYPE = 120

XLstringType = ctypes.c_char_p

XLaccess, pXLaccess = XLuint64, ctypes.POINTER(XLuint64)
XL_INVALID_CHANNEL_INDEX = 0xFFFFFFFF
XL_INVALID_DEVICE_INDEX = 0xFFFFFFFF

XLhandle = ctypes.c_void_p

class XL_LIN(enum.IntEnum):
    #channel is a LIN master
    MASTER = 1
    #channel is a LIN slave
    SLAVE = 2
    #LIN version 1.3
    VERSION_1_3 = 1
    #LIN version 2.0
    VERSION_2_0 = 2
    #LIN version 2.1
    VERSION_2_1 = 3
    #flag for automatic 'classic' checksum calculation
    CALC_CHECKSUM = 256
    #flag for automatic 'enhanced' checksum calculation
    CALC_CHECKSUM_ENHANCED = 512
    #set hardware into sleep mode
    SET_SILENT = 1
    #set hardware into sleep mode and send a request at wake-up
    SET_WAKEUPID = 3
    #Use classic CRC
    CHECKSUM_CLASSIC = 0
    #Use enhanced CRC
    CHECKSUM_ENHANCED = 1
    #Set the checksum calculation to undefined.
    CHECKSUM_UNDEFINED = 255
    #flag if nothing changes
    STAYALIVE = 0
    #flag if the hardware is set into the sleep mode
    SET_SLEEPMODE = 1
    #flag if the hardware comes from the sleep mode
    COMESFROM_SLEEPMODE = 2
    #flag to signal a internal WAKEUP (event)
    WAKUP_INTERNAL = 1
    #set the DLC to undefined
    UNDEFINED_DLC = 255
    #switch on the LIN slave
    SLAVE_ON = 255
    #switch off the LIN slave
    SLAVE_OFF = 0

class s_xl_lin_stat_param(ctypes.Structure):
    _fields_ = [
        #XL_LIN_SLAVE | XL_LIN_MASTER
        ("LINMode", ctypes.c_uint),
        #the baudrate will be calculated within the API. Here: e.g. 9600, 19200
        ("baudrate", ctypes.c_int),
        #define for the LIN version (actual V1.3 of V2.0)
        ("LINVersion", ctypes.c_uint),
        #for future use
        ("reserved", ctypes.c_uint),
    ]
XLlinStatPar = s_xl_lin_stat_param

MAX_MSG_LEN = 8

class XL_INTERFACE_VERSION(enum.IntEnum):
    V2 = 2
    V3 = 3
    V4 = 4
#Current Version
XL_CURRENT_INTERFACE_VERSION = XL_INTERFACE_VERSION.V3

XL_CAN_EXT_MSG_ID = 0x80000000

class XL_CAN_MSG_FLAG(enum.IntFlag):
    ERROR_FRAME = 1
    #Overrun in Driver or CAN Controller, previous msgs have been lost.
    OVERRUN = 2
    #Line Error on Lowspeed
    NERR = 4
    #High Voltage Message on Single Wire CAN
    WAKEUP = 8 #
    REMOTE_FRAME = 16
    RESERVED_1 = 32
    #Message Transmitted
    TX_COMPLETED = 64
    #Transmit Message stored into Controller
    TX_REQUEST = 128
    #SRR bit in CAN message is dominant
    SRR_BIT_DOM = 512

#Used in XLevent.flags
XL_EVENT_FLAG_OVERRUN = 1

class XL_LIN_MSGFLAG(enum.IntFlag):
    #LIN TX flag
    TX = XL_CAN_MSG_FLAG.TX_COMPLETED
    #Wrong LIN CRC
    CRCERROR = 129

class s_xl_can_msg(ctypes.Structure):
    _fields_ = [
        ("id", ctypes.c_uint),
        ("flags", ctypes.c_ushort),
        ("dlc", ctypes.c_ushort),
        ("res1", XLuint64),
        ("res2", XLuint64),
    ]

class XL_DAIO_DATA(enum.IntEnum):
    GET = 32768
    VALUE_DIGITAL = 1
    VALUE_ANALOG = 2
    PWM = 16

class XL_DAIO_MODE(enum.IntEnum):
    #generates pulse in values of PWM
    PULSE = 32

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

class XL_CHIPSTAT(enum.IntEnum):
    BUSOFF = 1
    ERROR_PASSIVE = 2
    ERROR_WARNING = 4
    ERROR_ACTIVE = 8

class s_xl_chip_state(ctypes.Structure):
    _fields_ = [
        ("busStatus", ctypes.c_ubyte),
        ("txErrorCounter", ctypes.c_ubyte),
        ("rxErrorCounter", ctypes.c_ubyte),
    ]

class XL_TRANSCEIVER_EVENT(enum.IntEnum):
    NONE = 0
    #cable was inserted
    INSERTED = 1
    #cable was removed
    REMOVED = 2
    #transceiver state changed
    STATE_CHANGE = 3

class s_xl_transceiver(ctypes.Structure):
    _fields_ = [
        ("event_reason", ctypes.c_ubyte),
        ("is_present", ctypes.c_ubyte),
    ]

class XL_OUTPUT_MODE(enum.IntEnum):
    #switch CAN trx into default silent mode
    SILENT = 0
    #switch CAN trx into normal mode
    XL_OUTPUT_MODE_NORMAL = 1
    #switch CAN trx into silent mode with tx pin off
    XL_OUTPUT_MODE_TX_OFF = 2
    #switch CAN trx into SJA1000 silent mode
    XL_OUTPUT_MODE_SJA_1000_SILENT = 3

class XL_TRANSCEIVER_MODE(enum.IntEnum):
    EVENT_ERROR = 1
    EVENT_CHANGED = 2

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

#LIN messages structure
class s_xl_lin_msg_api(ctypes.Union):
    _fields_ = [
        ("linMsg", s_xl_lin_msg),
        ("linNoAns", s_xl_lin_no_ans),
        ("linWakeUp", s_xl_lin_wake_up),
        ("linSleep", s_xl_lin_sleep),
        ("linCRCinfo", s_xl_lin_crc_info),
    ]

# K-Line messages structure
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

#BASIC bus message structure
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
#XL_EVENT structures - event type definition
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

#message name to acquire a unique message id from windows
DriverNotifyMessageName = "VectorCanDriverChangeNotifyMessage"

#build a channels mask from the channels index
XL_CHANNEL_MASK = lambda x: 1 << x

XL_MAX_APPNAME = 32

XLstatus = ctypes.c_short

#defines for xlGetDriverConfig structures
XL_MAX_LENGTH = 31
XL_CONFIG_MAX_CHANNELS = 64
XL_MAX_NAME_LENGTH = 48

#defines for xlSet/GetApplConfig
XL_APPLCONFIG_MAX_CHANNELS = 256
class XL_ACTIVATE(enum.IntEnum):
    NONE = 0
    #using this flag with time synchronisation protocols supported by Vector Timesync Service is not recommended
    RESET_CLOCK = 8

class XL_BUS_COMPATIBLE(enum.IntFlag):
    CAN      = XL_BUS_TYPE.CAN
    LIN      = XL_BUS_TYPE.LIN
    FLEXRAY  = XL_BUS_TYPE.FLEXRAY
    MOST     = XL_BUS_TYPE.MOST
    #io cab/piggy
    DAIO     = XL_BUS_TYPE.DAIO
    J1708    = XL_BUS_TYPE.J1708
    KLINE    = XL_BUS_TYPE.KLINE
    ETHERNET = XL_BUS_TYPE.ETHERNET
    A429     = XL_BUS_TYPE.A429

class XL_BUS_ACTIVE_CAP(enum.IntFlag):
    CAN      = XL_BUS_COMPATIBLE.CAN      << 16
    LIN      = XL_BUS_COMPATIBLE.LIN      << 16
    FLEXRAY  = XL_BUS_COMPATIBLE.FLEXRAY  << 16
    MOST     = XL_BUS_COMPATIBLE.MOST     << 16
    DAIO     = XL_BUS_COMPATIBLE.DAIO     << 16
    J1708    = XL_BUS_COMPATIBLE.J1708    << 16
    KLINE    = XL_BUS_COMPATIBLE.KLINE    << 16
    ETHERNET = XL_BUS_COMPATIBLE.ETHERNET << 16
    A429     = XL_BUS_COMPATIBLE.A429     << 16

class XL_BUS_CAPABILITIES(enum.IntFlag):
    COMPATIBLE_CAN      = XL_BUS_COMPATIBLE.CAN
    ACTIVE_CAP_CAN      = XL_BUS_ACTIVE_CAP.CAN
    CAN                 = COMPATIBLE_CAN | ACTIVE_CAP_CAN
    COMPATIBLE_LIN      = XL_BUS_COMPATIBLE.LIN
    ACTIVE_CAP_LIN      = XL_BUS_ACTIVE_CAP.LIN
    LIN                 = COMPATIBLE_LIN | ACTIVE_CAP_LIN
    COMPATIBLE_FLEXRAY  = XL_BUS_COMPATIBLE.FLEXRAY
    ACTIVE_CAP_FLEXRAY  = XL_BUS_ACTIVE_CAP.FLEXRAY
    FLEXRAY             = COMPATIBLE_FLEXRAY | ACTIVE_CAP_FLEXRAY
    COMPATIBLE_MOST     = XL_BUS_COMPATIBLE.MOST
    ACTIVE_CAP_MOST     = XL_BUS_ACTIVE_CAP.MOST
    MOST                = COMPATIBLE_MOST | ACTIVE_CAP_MOST
    COMPATIBLE_DAIO     = XL_BUS_COMPATIBLE.DAIO
    ACTIVE_CAP_DAIO     = XL_BUS_ACTIVE_CAP.DAIO
    DAIO                = COMPATIBLE_DAIO | ACTIVE_CAP_DAIO
    COMPATIBLE_J1708    = XL_BUS_COMPATIBLE.J1708
    ACTIVE_CAP_J1708    = XL_BUS_ACTIVE_CAP.J1708
    J1708               = COMPATIBLE_J1708 | ACTIVE_CAP_J1708
    COMPATIBLE_KLINE    = XL_BUS_COMPATIBLE.KLINE
    ACTIVE_CAP_KLINE    = XL_BUS_ACTIVE_CAP.KLINE
    KLINE               = COMPATIBLE_KLINE | ACTIVE_CAP_KLINE
    COMPATIBLE_ETHERNET = XL_BUS_COMPATIBLE.ETHERNET
    ACTIVE_CAP_ETHERNET = XL_BUS_ACTIVE_CAP.ETHERNET
    ETHERNET            = COMPATIBLE_ETHERNET | ACTIVE_CAP_ETHERNET
    COMPATIBLE_A429     = XL_BUS_COMPATIBLE.A429
    ACTIVE_CAP_A429     = XL_BUS_ACTIVE_CAP.A429
    A429                = COMPATIBLE_A429 | ACTIVE_CAP_A429

class XL_BUS_NAME(enum.Enum):
    NONE = ""
    CAN = "CAN"
    LIN = "LIN"
    FLEXRAY = "FlexRay"
    STREAM = "Stream"
    MOST = "MOST"
    DAIO = "DAIO"
    HWSYNC_KEYPAD = "HWSYNC_KEYPAD"
    J1708 = "J1708"
    KLINE = "K-Line"
    ETHERNET = "Ethernet"
    AFDX = "AFDX"
    A429 = "ARINC429"

#flag for standard ID's
XL_CAN_STD = 1
#flag for extended ID's
XL_CAN_EXT = 2
class XL_ACCEPTANCE_FILTER(enum.IntEnum):
    CAN_STD = XL_CAN_STD
    CAN_EXT = XL_CAN_EXT

#configuration option CANFD-BOSCH
CANFD_CONFOPT_NO_ISO = 8

class s_xl_canfd_conf(ctypes.Structure):
    _fields_ = [
        ("arbitrationBitRate", ctypes.c_uint),
        #CAN bus timing for nominal / arbitration bit rate
        ("sjwAbr", ctypes.c_uint),
        ("tseg1Abr", ctypes.c_uint),
        ("tseg2Abr", ctypes.c_uint),
        ("dataBitRate", ctypes.c_uint),
        #CAN bus timing for data bit rate
        ("sjwDbr", ctypes.c_uint),
        ("tseg1Dbr", ctypes.c_uint),
        ("tseg2Dbr", ctypes.c_uint),
        #has to be zero
        ("reserved", ctypes.c_ubyte),
        #configuration option CANFD-BOSCH (ISO/NON-ISO)
        ("options", ctypes.c_ubyte),
        #has to be zero
        ("reserved1", ctypes.c_ubyte*2),
        #has to be zero
        ("reserved2", ctypes.c_uint),
    ]
XLcanFdConf = s_xl_canfd_conf

class s_xl_chip_params(ctypes.Structure):
    _fields_ = [
        ("bitRate", ctypes.c_uint),
        ("sjw", ctypes.c_ubyte),
        ("tseg1", ctypes.c_ubyte),
        ("tseg2", ctypes.c_ubyte),
        #1 or 3
        ("sam", ctypes.c_ubyte),
    ]
XLchipParams = s_xl_chip_params

class XL_BUS_PARAMS_MOST_SPEED(enum.IntEnum):
    GRADE_25  = 1
    GRADE_150 = 2

class XL_BUS_PARAMS_CANOPMODE(enum.IntEnum):
    #channel operates in CAN20
    CAN20        = 1
    #channel operates in CANFD
    CANFD        = 2
    #channel operates in CANFD_NO_ISO
    CANFD_NO_ISO = 8

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
        #CAN bus timing for nominal / arbitration bit rate
        ("arbitrationBitRate", ctypes.c_uint),
        ("sjwAbr", ctypes.c_ubyte),
        ("tseg1Abr", ctypes.c_ubyte),
        ("tseg2Abr", ctypes.c_ubyte),
        ("samAbr", ctypes.c_ubyte),
        ("outputMode", ctypes.c_ubyte),
        #CAN bus timing for data bit rate
        ("sjwDbr", ctypes.c_ubyte),
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
        #XL_FR_CHANNEL_CFG_STATUS_xxx
        ("status", ctypes.c_uint),
        #XL_FR_CHANNEL_CFG_MODE_xxx
        ("cfgMode", ctypes.c_uint),
        #FlexRay baudrate in kBaud
        ("baudrate", ctypes.c_uint),
    ]

class s_xl_bus_params_ethernet(ctypes.Structure):
    _fields_ = [
        #MAC address (starting with MSB!)
        ("macAddr", ctypes.c_ubyte*6),
        #XL_ETH_STATUS_CONNECTOR_xxx
        ("connector", ctypes.c_ubyte),
        #XL_ETH_STATUS_PHY_xxx
        ("phy", ctypes.c_ubyte),
        #XL_ETH_STATUS_LINK_xxx
        ("link", ctypes.c_ubyte),
        #XL_ETH_STATUS_SPEED_xxx
        ("speed", ctypes.c_ubyte),
        #XL_ETH_STATUS_CLOCK_xxx
        ("clockMode", ctypes.c_ubyte),
        #XL_ETH_BYPASS_xxx
        ("bypass", ctypes.c_ubyte),
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

XL_INVALID_PORTHANDLE = -1
XLportHandle, pXLportHandle = XLlong, ctypes.POINTER(XLlong)

class XL_CONNECTION_INFO(enum.IntEnum):
    FAMILY_MASK    = 4278190080
    DETAIL_MASK    = 16777215
    #USB devices
    FAMILY_USB     = 0 << 24
    #Ethernet and WiFi devices
    FAMILY_NETWORK = 1 << 24
    #PCI-Express devices
    FAMILY_PCIE    = 2 << 24
    USB_UNKNOWN    = 0
    USB_FULLSPEED  = 1
    USB_HIGHSPEED  = 2
    USB_SUPERSPEED = 3

class XL_FPGA_CORE_TYPE(enum.IntEnum):
    NONE   = 0
    CAN    = 1
    LIN    = 2
    LIN_RX = 3
#automatic driver FPGA flashing done
XL_SPECIAL_DEVICE_STAT_FPGA_UPDATE_DONE = 1

class s_xl_license_info(ctypes.Structure):
    _fields_ = [
        ("bAvailable", ctypes.c_ubyte),
        ("licName", ctypes.c_char*65),
    ]
XL_LICENSE_INFO = s_xl_license_info
XLlicenseInfo = XL_LICENSE_INFO

class s_xl_channel_config(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
        ("name", ctypes.c_char * (XL_MAX_LENGTH+1)),
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
        ("transceiverName", ctypes.c_char * (XL_MAX_LENGTH+1)),
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
        ("channel", XLchannelConfig*XL_CONFIG_MAX_CHANNELS),
    ]
XL_DRIVER_CONFIG = s_xl_driver_config
XLdriverConfig, pXLdriverConfig = XL_DRIVER_CONFIG, ctypes.POINTER(XL_DRIVER_CONFIG)

#DAIO params definition
class XL_DAIO_DIGITAL(enum.IntEnum):
    #digital port is enabled
    ENABLED = 1
    #digital port is input, otherwise it is an output
    INPUT   = 2
    #digital port is trigger
    TRIGGER = 4

class XL_DAIO_ANALOG(enum.IntEnum):
    #analog port is enabled
    ENABLED   = 1
    #analog port is input, otherwise it is an output
    INPUT     = 2
    #analog port is trigger
    TRIGGER   = 4
    #analog port is in range 0..32,768V, otherwise 0..8,192V
    RANGE_32V = 8

class XL_DAIO_TRIGGER_MODE(enum.IntEnum):
    #no trigger configured
    NONE    = 0
    #trigger on preconfigured digital lines
    DIGITAL = 1
    #trigger on input 3 ascending
    ANALOG_ASCENDING  = 2
    #trigger on input 3 descending
    ANALOG_DESCENDING = 4
    #trigger on input
    ANALOG = ANALOG_ASCENDING|ANALOG_DESCENDING

#no trigger level is defined
XL_DAIO_TRIGGER_LEVEL_NONE = 0
#periodic measurement is disabled
XL_DAIO_POLLING_NONE = 0

class s_xl_acc_filter(ctypes.Structure):
    _fields_ = [
        ("isSet", ctypes.c_ubyte),
        ("code", ctypes.c_uint),
        #relevant = 1
        ("mask", ctypes.c_uint),
    ]
XLaccFilt = s_xl_acc_filter

class s_xl_acceptance(ctypes.Structure):
    _fields_ = [
        ("std", XLaccFilt),
        ("xtd", XLaccFilt),
    ]
XLacceptance = s_xl_acceptance

class XL_SET_TIMESYNC(enum.IntEnum):
    NO_CHANGE = 0
    ON        = 1
    OFF       = 2

#MOST lib
XLuserHandle = ctypes.c_ushort
#size of channel alloctaion table + 4Bytes (MPR, MDR; ?, ?)
MOST_ALLOC_TABLE_SIZE = 64
#Remote API
XL_IPv4 = 4
XL_IPv6 = 6
XL_MAX_REMOTE_DEVICE_INFO = 16
XL_ALL_REMOTE_DEVICES     = 4294967295
XL_MAX_REMOTE_ALIAS_SIZE  = 64

class  XL_REMOTE(enum.IntEnum):
    OFFLINE = 1
    ONLINE  = 2
    BUSY    = 3
    CONNECION_REFUSED = 4

class  XL_REMOTE_ADD(enum.IntEnum):
    PERMANENT = 0
    TEMPORARY = 1

class  XL_REMOTE_REGISTER(enum.IntEnum):
    NONE         = 0
    CONNECT      = 1
    TEMP_CONNECT = 2

class  XL_REMOTE_DISCONNECT(enum.IntEnum):
    NONE         = 0
    REMOVE_ENTRY = 1

class  XL_REMOTE_DEVICE(enum.IntEnum):
    #the device is present
    AVAILABLE       = 1
    #the device has a configuration entry in registry
    CONFIGURED      = 2
    #the device is connected to this client
    CONNECTED       = 4
    #the driver should open a connection to this client
    ENABLED         = 8
    #the device is used by another client
    BUSY            = 16
    #the device is temporary configured, it has not entry in registry
    TEMP_CONFIGURED = 32
    STATUS_MASK     = 63
    NO_NET_SEARCH   = 0
    NET_SEARCH      = 1

class  XL_REMOTE_DEVICE_TYPE(enum.IntEnum):
    UNKNOWN     = 0
    VN8900      = 1
    STANDARD_PC = 2
    #VX hardware
    VX          = 3
    VN8800      = 4
    #VN network interfaces
    VN          = 5
    #VT hardware
    VT          = 6

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
        ("deviceInfo", XLremoteDevice*XL_MAX_REMOTE_DEVICE_INFO),
    ]
XLremoteDeviceInfo = s_xl_remote_device_info

XL_CHANNEL_FLAG_EX_MASK = lambda n: 1 << n
#Flags for channelCapabilities
class  XL_CHANNEL_FLAG(enum.IntFlag):
    TIME_SYNC_RUNNING    = 0x00000001
    #Device is not capable of hardware-based time synchronization via Sync-line
    NO_HWSYNC_SUPPORT    = 0x00000400
    #used to distinguish between VN2600 (w/o SPDIF) and VN2610 (with S/PDIF)
    SPDIF_CAPABLE        = 0x00004000
    CANFD_BOSCH_SUPPORT  = 0x20000000
    CMACTLICENSE_SUPPORT = 0x40000000
    CANFD_ISO_SUPPORT    = 0x80000000
    EX1_TIME_SYNC_RUNNING   = XL_CHANNEL_FLAG_EX_MASK(0)
    EX1_HWSYNC_SUPPORT      = XL_CHANNEL_FLAG_EX_MASK(4)
    EX1_CANFD_ISO_SUPPORT   = XL_CHANNEL_FLAG_EX_MASK(10)
    EX1_SPDIF_CAPABLE       = XL_CHANNEL_FLAG_EX_MASK(20)
    EX1_CANFD_BOSCH_SUPPORT = XL_CHANNEL_FLAG_EX_MASK(35)
    #Ethernet device operates in network-based instead of channel-based mode
    EX1_NET_ETH_SUPPORT     = XL_CHANNEL_FLAG_EX_MASK(36)

class XL_MOST_SOURCE(enum.IntEnum):
    """Defines for xlMostSwitchEventSources"""
    ASYNC_SPY          = 32768
    ASYNC_RX           = 4096
    ASYNC_TX           = 2048
    CTRL_OS8104A       = 1024
    CTRL_SPY           = 256
    ALLOC_TABLE        = 128
    SYNC_RC_OVER       = 64
    SYNC_TX_UNDER      = 32
    SYNCLINE           = 16
    ASYNC_RX_FIFO_OVER = 8

class XL_MOST_ERROR(enum.IntEnum):
    OS8104_TX_LOCK_ERROR      = 1
    OS8104_SPDIF_LOCK_ERROR   = 2
    OS8104_ASYNC_BUFFER_FULL  = 3
    OS8104_ASYNC_CRC_ERROR    = 4
    ASYNC_TX_UNDERRUN         = 5
    CTRL_TX_UNDERRUN          = 6
    MCU_TS_CMD_QUEUE_UNDERRUN = 7
    MCU_TS_CMD_QUEUE_OVERRUN  = 8
    CMD_TX_UNDERRUN           = 9
    SYNCPULSE_ERROR           = 10
    OS8104_CODING_ERROR       = 11
    ERROR_UNKNOWN_COMMAND     = 12
    ASYNC_RX_OVERFLOW_ERROR   = 13
    FPGA_TS_FIFO_OVERFLOW     = 14
    SPY_OVERFLOW_ERROR        = 15
    CTRL_TYPE_QUEUE_OVERFLOW  = 16
    ASYNC_TYPE_QUEUE_OVERFLOW = 17
    CTRL_UNKNOWN_TYPE         = 18
    CTRL_QUEUE_UNDERRUN       = 19
    ASYNC_UNKNOWN_TYPE        = 20
    ASYNC_QUEUE_UNDERRUN      = 21

#data for demanded timstamps
XL_MOST_DEMANDED_START = 1
XL_MOST_RX_DATA_SIZE = 1028
XL_MOST_TS_DATA_SIZE = 12
XL_MOST_RX_ELEMENT_HEADER_SIZE = 32
XL_MOST_CTRL_RX_SPY_SIZE = 36
XL_MOST_CTRL_RX_OS8104_SIZE = 28
XL_MOST_SPECIAL_REGISTER_CHANGE_SIZE = 20
XL_MOST_ERROR_EV_SIZE_4 = 4
XL_MOST_ERROR_EV_SIZE = 16

class XL_MOST_DEVICE(enum.IntEnum):
    """defines for the audio devices"""
    CASE_LINE_IN      = 0
    CASE_LINE_OUT     = 1
    SPDIF_IN          = 7
    SPDIF_OUT         = 8
    SPDIF_IN_OUT_SYNC = 11

class XL_MOST_SPDIF(enum.IntEnum):
    """defines for xlMostCtrlSyncAudioEx, mode"""
    LOCK_OFF = 0
    LOCK_ON  = 1

class XL_MOST_SYNC_MUTES_STATUS(enum.IntEnum):
    """defines for the XL_MOST_SYNC_MUTES_STATUS event"""
    NO_MUTE = 0
    MUTE    = 1

class XL_MOST_EVENT_SOURCE(enum.IntEnum):
    """defines for the event sources in XLmostEvent"""
    XL_MOST_VN2600  = 1
    XL_MOST_OS8104A = 2
    XL_MOST_OS8104B = 4
    XL_MOST_SPY     = 8

class XL_MOST_MODE(enum.IntEnum):
    """defines for xlMostSetAllBypass and XL_MOST_ALLBYPASS"""
    DEACTIVATE       = 0
    ACTIVATE         = 1
    FORCE_DEACTIVATE = 2

XL_MOST_RX_BUFFER_CLEAR_ONCE = 2

class XL_MOST_TIMING(enum.IntEnum):
    """defines for xlMostSetTimingMode and the XL_MOST_TIMINGMODE(_SPDIF)_EV event."""
    SLAVE                   = 0
    MASTER                  = 1
    SLAVE_SPDIF_MASTER      = 2
    SLAVE_SPDIF_SLAVE       = 3
    MASTER_SPDIF_MASTER     = 4
    MASTER_SPDIF_SLAVE      = 5
    MASTER_FROM_SPDIF_SLAVE = 6

class XL_MOST_FREQUENCY(enum.IntEnum):
    """defines for xlMostSetFrequency and the XL_MOST_FREQUENCY_EV event."""
    FREQUENCY_44100 = 0
    FREQUENCY_48000 = 1
    FREQUENCY_ERROR = 2

class XL_MOST_LIGHT(enum.IntEnum):
    """defines for xlMostSetTxLight"""
    OFF       = 0
    #unmodulated on
    FORCE_ON  = 1
    #modulated light
    MODULATED = 2
    #xlMostSetTxLightPower
    FULL      = 100
    LIGHT_3DB = 50

class XL_MOST_LOCKSTATUS(enum.IntEnum):
    """defines for the XL_MOST_LOCKSTATUS event"""
    UNLOCK        = 5
    LOCK          = 6
    STATE_UNKNOWN = 9

class XL_MOST_CTRL_RX_OS8104(enum.IntEnum):
    """defines for the XL_MOST_CTRL_RX_OS8104 event (tx event)"""
    TX_WHILE_UNLOCKED = 2147483648
    TX_TIMEOUT        = 1073741824
    DIRECTION_RX = 0
    DIRECTION_TX = 1
    #No rx-queue overflow occured
    NO_QUEUE_OVERFLOW      = 0
    #Overflow of rx-queue in firmware when trying to add a rx-event
    QUEUE_OVERFLOW         = 32768
    COMMAND_FAILED         = 16384
    #Overflow of command-timestamp-queue in firmware
    INTERNAL_OVERFLOW      = 8192
    MEASUREMENT_NOT_ACTIVE = 4096
    #Overflow of async rx-queue in firmware when trying to add a packet
    QUEUE_OVERFLOW_ASYNC   = 2048
    #Overflow of rx-queue in firmware when trying to add a message
    QUEUE_OVERFLOW_CTRL    = 1024
    NOT_SUPPORTED          = 512
    #Overflow occured when trying to add an event to application rx-queue
    QUEUE_OVERFLOW_DRV     = 256
    #node address changed
    NA_CHANGED   = 1
    #group address changed
    GA_CHANGED   = 2
    #alternative packet address changed
    APA_CHANGED  = 4
    #node position register changed
    NPR_CHANGED  = 8
    #max position register changed
    MPR_CHANGED  = 16
    #node delay register changed
    NDR_CHANGED  = 32
    #max delay register changed
    MDR_CHANGED  = 64
    SBC_CHANGED  = 128
    XTIM_CHANGED = 256
    XRTY_CHANGED = 512

class XL_MOST_REGISTER(enum.IntEnum):
    """defines for the MOST register (xlMostWriteRegister)"""
    #Group Address
    bGA   = 137
    #Node Address High
    bNAH  = 138
    #Node Address Low
    bNAL  = 139
    #Source Data Control 2
    bSDC2 = 140
    #Source Data Control 3
    bSDC3 = 141
    #Clock Manager 2
    bCM2  = 142
    #Node Delay
    bNDR  = 143
    #Maximum Position
    bMPR  = 144
    #Maximum Delay
    bMDR  = 145
    #Clock Manager 4
    bCM4  = 147
    #Synchronous Bandwidth Control
    bSBC  = 150
    #Transceiver Status 2
    bXSR2 = 151
    #Receive Message Type
    bRTYP = 160
    #Source Address High
    bRSAH = 161
    #Source Address Low
    bRSAL = 162
    #Receive Control Data 0 --> bRCD16 = bRCD0+16
    bRCD0 = 163
    #Transmit Retry Time
    bXTIM = 190
    #Transmit Retries
    bXRTY = 191
    #Transmit Priority
    bXPRI = 192
    #Transmit Message Type
    bXTYP = 193
    #Target Address High
    bXTAH = 194
    #Target Address Low
    bXTAL = 195
    #Transmit Control Data 0 --> bXCD16 = bXCD0+16
    bXCD0 = 196
    #Transmit Transfer Status
    bXTS  = 213
    #Packet Control
    bPCTC = 226
    #Packet Status
    bPCTS = 227

class XL_MOST_SPY_RX_STATUS(enum.IntEnum):
    NO_LIGHT = 1
    NO_LOCK = 2
    BIPHASE_ERROR = 4
    MESSAGE_LENGTH_ERROR = 8
    PARITY_ERROR = 16
    FRAME_LENGTH_ERROR = 32
    PREAMBLE_TYPE_ERROR = 64
    CRC_ERROR = 128

class XL_MOST_ASYNC(enum.IntEnum):
    """defines for status of async frames"""
    NO_ERROR = 0
    SBC_ERROR = 12
    NEXT_STARTS_TO_EARLY = 13
    TO_LONG = 14
    #unlock occured within receiption of packet
    UNLOCK = 15

class XL_MOST_SYNC_PULSE(enum.IntEnum):
    """defines for XL_MOST_SYNC_PULSE_EV member trigger_source"""
    EXTERNAL = 0
    OUR = 1

class XL_MOST_CTRL_TYPE(enum.IntEnum):
    """ctrlType value within the XL_CTRL_SPY event"""
    NORMAL = 0
    REMOTE_READ = 1
    REMOTE_WRITE = 2
    RESOURCE_ALLOCATE = 3
    RESOURCE_DEALLOCATE = 4
    GET_SOURCE = 5

class XL_MOST_BUSLOAD_COUNTER(enum.IntEnum):
    """counterType for the xlMost****GenerateBusload function"""
    TYPE_NONE = 0
    TYPE_1_BYTE = 1
    TYPE_2_BYTE = 2
    TYPE_3_BYTE = 3
    TYPE_4_BYTE = 4

class XL_MOST_STATESEL(enum.IntFlag):
    """selection bits for xlMostGetDeviceStates / CMD_GET_DEVICE_STATE->selection_mask"""
    LIGHTLOCK = 1
    REGISTERBUNCH1 = 2
    BYPASSTIMING = 4
    REGISTERBUNCH2 = 8
    REGISTERBUNCH3 = 16
    VOLUMEMUTE = 32
    EVENTSOURCE = 64
    RXBUFFERMODE = 128
    ALLOCTABLE = 256
    SUPERVISOR_LOCKSTATUS = 512
    SUPERVISOR_MESSAGE = 1024

class XL_MOST_STREAM(enum.IntEnum):
    #RX streaming: MOST -> PC
    RX_DATA = 0
    #TX streaming: PC -> MOST
    TX_DATA = 1
    #only for RX: additionally the orig. TS + status information are reported
    ADD_FRAME_HEADER = 1

class XL_MOST_STREAM_STATE(enum.IntEnum):
    CLOSED = 1
    OPENED = 2
    STARTED = 3
    STOPPED = 4
    #waiting for result from hw
    START_PENDING = 5
    #waiting for result from hw
    STOP_PENDING = 6
    UNKNOWN = 255

class XL_MOST_STREAM_MODE(enum.IntEnum):
    ACTIVATE = 0
    DEACTIVATE = 1

XL_MOST_STREAM_INVALID_HANDLE = 0

class XL_MOST_STREAM_LATENCY(enum.IntEnum):
    VERY_LOW = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    VERY_HIGH = 4

class XL_MOST_STREAM_ERR(enum.IntEnum):
    """error defines for sync data streaming"""
    NO_ERROR = 0
    INVALID_HANDLE = 1
    NO_MORE_BUFFERS_AVAILABLE = 2
    ANY_BUFFER_LOCKED = 3
    WRITE_RE_FAILED = 4
    STREAM_ALREADY_STARTED = 5
    TX_BUFFER_UNDERRUN = 6
    RX_BUFFER_OVERFLOW = 7
    INSUFFICIENT_RESOURCES = 8

#max. size of rx fifo for rx event in bytes
XL_MOST_RX_FIFO_QUEUE_SIZE_MAX = 1048576
XL_MOST_RX_FIFO_QUEUE_SIZE_MIN = 8192

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
        #transmission or real receiption
        ("direction", ctypes.c_ubyte),
        #unused for real rx msgs
        ("status", ctypes.c_uint),
    ]
XL_MOST_CTRL_MSG_EV = s_xl_most_ctrl_msg
XLmostCtrlMsg = XL_MOST_CTRL_MSG_EV

class s_xl_most_async_msg(ctypes.Structure):
    _fields_ = [
        #read as last data from PLD but stored first
        ("status", ctypes.c_uint),
        #not used
        ("crc", ctypes.c_uint),
        ("arbitration", ctypes.c_ubyte),
        #real length of async data in quadlets
        ("length", ctypes.c_ubyte),
        ("targetAddress", ctypes.c_ushort),
        ("sourceAddress", ctypes.c_ushort),
        #max size but only used data is transmitted to pc
        ("asyncData", ctypes.c_ubyte*1018),
    ]
XL_MOST_ASYNC_MSG_EV = s_xl_most_async_msg

class s_xl_most_async_tx(ctypes.Structure):
    _fields_ = [
        ("arbitration", ctypes.c_ubyte),
        #real length of async data in quadlets
        ("length", ctypes.c_ubyte),
        ("targetAddress", ctypes.c_ushort),
        ("sourceAddress", ctypes.c_ushort),
        #worst case
        ("asyncData", ctypes.c_ubyte*1014),
    ]
XL_MOST_ASYNC_TX_EV = s_xl_most_async_tx
XLmostAsyncMsg = XL_MOST_ASYNC_TX_EV

class s_xl_most_special_register(ctypes.Structure):
    _fields_ = [
        #see defines "XL_MOST_..._CHANGED"
        ("changeMask", ctypes.c_uint),
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
        ("allocTable", ctypes.c_ubyte*MOST_ALLOC_TABLE_SIZE),
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
        #see XL_MOST_STREAM_STATE_...
        ("streamState", ctypes.c_uint),
        #see XL_MOST_STREAM_STATE_...
        ("streamError", ctypes.c_uint),
        ("reserved", ctypes.c_uint),
    ]
XL_MOST_STREAM_STATE_EV = s_xl_most_stream_state

class s_xl_most_stream_buffer(ctypes.Structure):
    _fields_ = [
        ("streamHandle", ctypes.c_uint),
#ifdef _MSC_VER
        #32bit LSDW of buffer pointer
        #("pBuffer", POINTER_32),
#else
        #32bit LSDW of buffer pointer
        ("pBuffer", ctypes.c_uint),
        ("validBytes", ctypes.c_uint),
        #see XL_MOST_STREAM_ERR_...
        ("status", ctypes.c_uint),
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

XL_MOST_EVENT_HEADER_SIZE = 32
XL_MOST_EVENT_MAX_DATA_SIZE = 1024
XL_MOST_EVENT_MAX_SIZE = XL_MOST_EVENT_HEADER_SIZE + XL_MOST_EVENT_MAX_DATA_SIZE

class s_xl_most_tag_data(ctypes.Union):
    _fields_ = [
        #XL_MOST_CTRL_SPY_EV
        ("mostCtrlSpy", s_xl_most_ctrl_spy),
        #XL_MOST_CTRL_MSG_EV
        ("mostCtrlMsg", s_xl_most_ctrl_msg),
        #XL_MOST_ASYNC_MSG_EV, received async frame
        ("mostAsyncMsg", s_xl_most_async_msg),
        #XL_MOST_ASYNC_TX_EV, async frame tx acknowledge
        ("mostAsyncTx", s_xl_most_async_tx),
        #XL_MOST_SPECIAL_REGISTER_EV
        ("mostSpecialRegister", s_xl_most_special_register),
        #XL_MOST_EVENT_SOURCE_EV
        ("mostEventSource", s_xl_most_event_source),
        #XL_MOST_ALL_BYPASS_EV
        ("mostAllBypass", s_xl_most_all_bypass),
        #XL_MOST_TIMING_MODE_EV
        ("mostTimingMode", s_xl_most_timing_mode),
        #XL_MOST_TIMING_MODE_SPDIF_EV
        ("mostTimingModeSpdif", s_xl_most_timing_mode_spdif),
        #XL_MOST_FREQUENCY_EV
        ("mostFrequency", s_xl_most_frequency),
        #XL_MOST_REGISTER_BYTES_EV
        ("mostRegisterBytes", s_xl_most_register_bytes),
        #XL_MOST_REGISTER_BITS_EV
        ("mostRegisterBits", s_xl_most_register_bits),
        #XL_MOST_SYNC_ALLOC_EV
        ("mostSyncAlloc", s_xl_most_sync_alloc),
        #XL_MOST_CTRL_SYNC_AUDIO_EV
        ("mostCtrlSyncAudio", s_xl_most_ctrl_sync_audio),
        #XL_MOST_CTRL_SYNC_AUDIO_EX_EV
        ("mostCtrlSyncAudioEx", s_xl_most_ctrl_sync_audio_ex),
        #XL_MOST_SYNC_VOLUME_STATUS_EV
        ("mostSyncVolumeStatus", s_xl_most_sync_volume_status),
        #XL_MOST_SYNC_MUTES_STATUS_EV
        ("mostSyncMuteStatus", s_xl_most_sync_mutes_status),
        #XL_MOST_RX_LIGHT_EV
        ("mostRxLight", s_xl_most_rx_light),
        #XL_MOST_TX_LIGHT_EV
        ("mostTxLight", s_xl_most_tx_light),
        #XL_MOST_LIGHT_POWER_EV
        ("mostLightPower", s_xl_most_light_power),
        #XL_MOST_LOCK_STATUS_EV
        ("mostLockStatus", s_xl_most_lock_status),
        #XL_MOST_GEN_LIGHT_ERROR_EV
        ("mostGenLightError", s_xl_most_gen_light_error),
        #XL_MOST_GEN_LOCK_ERROR_EV
        ("mostGenLockError", s_xl_most_gen_lock_error),
        #XL_MOST_RX_BUFFER_EV
        ("mostRxBuffer", s_xl_most_rx_buffer),
        #XL_MOST_ERROR_EV
        ("mostError", s_xl_most_error),
        #XL_MOST_SYNC_PULSE_EV
        ("mostSyncPulse", s_xl_sync_pulse_ev),
        #XL_MOST_CTRL_BUSLOAD_EV
        ("mostCtrlBusload", s_xl_most_ctrl_busload),
        #XL_MOST_ASYNC_BUSLOAD_EV
        ("mostAsyncBusload", s_xl_most_async_busload),
        #XL_MOST_STREAM_STATE_EV
        ("mostStreamState", s_xl_most_stream_state),
        #XL_MOST_STREAM_BUFFER_EV
        ("mostStreamBuffer", s_xl_most_stream_buffer),
        #XL_MOST_SYNC_TX_UNDERFLOW_EV
        ("mostSyncTxUnderflow", s_xl_most_sync_tx_underflow),
        #XL_MOST_SYNC_RX_OVERFLOW_EV
        ("mostSyncRxOverflow", s_xl_most_sync_rx_overflow),
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
        #see XL_MOST_LOCK_STATUS_EV
        ("lockState", ctypes.c_uint),
        #see XL_MOST_RX_LIGHT_EV
        ("rxLight", ctypes.c_uint),
        #see XL_MOST_TX_LIGHT_EV
        ("txLight", ctypes.c_uint),
        #see XL_MOST_LIGHT_POWER_EV
        ("txLightPower", ctypes.c_uint),
     #XL_MOST_STATESEL_REGISTERBUNCH1

        #16 OS8104 registers (0x87...0x96 -> NPR...SBC)
        ("registerBunch1", ctypes.c_ubyte*16),
     #XL_MOST_STATESEL_BYPASSTIMING

        #see XL_MOST_ALL_BYPASS_EV
        ("bypassState", ctypes.c_uint),
        #see XL_MOST_TIMING_MODE_EV
        ("timingMode", ctypes.c_uint),
        #frame rate (if master); see XL_MOST_FREQUENCY_EV
        ("frequency", ctypes.c_uint),
     #XL_MOST_STATESEL_REGISTERBUNCH2

        #2 OS8104 registers (0xBE, 0xBF -> XTIM, XRTY)
        ("registerBunch2", ctypes.c_ubyte*2),
     #XL_MOST_STATESEL_REGISTERBUNCH3

        #2 OS8104 registers (0xE8, 0xE9 -> APAH, APAL)
        ("registerBunch3", ctypes.c_ubyte*2),
     #XL_MOST_STATESEL_VOLUMEMUTE

        #volume state for DEVICE_CASE_LINE_IN, DEVICE_CASE_LINE_OUT
        ("volume", ctypes.c_uint*2),
        #mute state for DEVICE_CASE_LINE_IN, DEVICE_CASE_LINE_OUT
        ("mute", ctypes.c_uint*2),
     #XL_MOST_STATESEL_EVENTSOURCE

        #see XL_MOST_EVENT_SOURCE_EV
        ("eventSource", ctypes.c_uint),
     #XL_MOST_STATESEL_RXBUFFERMODE

        #see XL_MOST_RX_BUFFER_EV
        ("rxBufferMode", ctypes.c_uint),
     #XL_MOST_STATESEL_ALLOCTABLE

        #see XL_MOST_SYNC_ALLOC_EV
        ("allocTable", ctypes.c_ubyte*MOST_ALLOC_TABLE_SIZE),
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

### FlexRay XL API ###

XL_FR_MAX_DATA_LENGTH = 254

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
        #16-bit value with data for pre-initializing the Flexray payload data words
        ("framePresetData", ctypes.c_uint),
        ("reserved", ctypes.c_uint*15),
    ]
XLfrClusterConfig = s_xl_fr_cluster_configuration

class s_xl_fr_channel_config(ctypes.Structure):
    _fields_ = [
        #XL_FR_CHANNEL_CFG_STATUS_xxx
        ("status", ctypes.c_uint),
        #XL_FR_CHANNEL_CFG_MODE_xxx
        ("cfgMode", ctypes.c_uint),
        ("reserved", ctypes.c_uint*6),
        #same as used in function xlFrSetConfig
        ("xlFrClusterConfig", s_xl_fr_cluster_configuration),
    ]
XLfrChannelConfig = s_xl_fr_channel_config

class XL_FR_CHANNEL_CFG_STATUS(enum.IntFlag):
    INIT_APP_PRESENT = 1
    CHANNEL_ACTIVATED = 2
    VALID_CLUSTER_CFG = 4
    VALID_CFG_MODE = 8

class XL_FR_CHANNEL_CFG_MODE(enum.IntEnum):
    SYNCHRONOUS = 1
    COMBINED = 2
    ASYNCHRONOUS = 3

class XL_FR_MODE(enum.IntEnum):
    #setup the VN3000 (eRay) normal operation mode. (default mode)
    NORMAL = 0
    #setup the VN3000 (Fujitsu) normal operation mode. (default mode)
    COLD_NORMAL = 4

class XL_FR_MODE_STARTUP(enum.IntEnum):
    #for normal use
    NONE = 0
    #for wakeup
    WAKEUP = 1
    #Coldstart path initiating the schedule synchronization
    COLDSTART_LEADING = 2
    #Coldstart path joining other coldstart nodes
    COLDSTART_FOLLOWING = 3
    #Send Wakeup and Coldstart path initiating the schedule synchronization
    WAKEUP_AND_COLDSTART_LEADING = 4
    #Send Wakeup and Coldstart path joining other coldstart nodes
    WAKEUP_AND_COLDSTART_FOLLOWING = 5

class s_xl_fr_set_modes(ctypes.Structure):
    _fields_ = [
        ("frMode", ctypes.c_uint),
        ("frStartupAttributes", ctypes.c_uint),
        ("reserved", ctypes.c_uint*30),
    ]
XLfrMode = s_xl_fr_set_modes

class XL_FR_SYMBOL(enum.IntEnum):
    #defines a MTS (Media Access Test Symbol)
    MTS = 1
    #defines a CAS (Collision Avoidance Symbol)
    CAS = 2

class XL_FR_TRANSCEIVER_MODE(enum.IntEnum):
    SLEEP = 1
    NORMAL = 2
    RECEIVE_ONLY = 3
    STANDBY = 4

class XL_FR_SYNC_PULSE(enum.IntEnum):
    EXTERNAL = XL_SYNC_PULSE.EXTERNAL
    OUR = XL_SYNC_PULSE.OUR
    OUR_SHARED = XL_SYNC_PULSE.OUR_SHARED

XL_FR_SPY_MODE_ASYNCHRONOUS = 1

class XL_FR_FILTER_STATUS(enum.IntEnum):
    #maching frame passes the filter
    PASS = 0
    #maching frame is blocked
    BLOCK = 1

class XL_FR_FILTER_TYPE(enum.IntEnum):
    #specifies a data frame
    DATA = 1
    #specifies a null frame in an used cycle
    NF = 2
    #specifies a null frame in an unused cycle
    FILLUP_NF = 4

class XL_FR_FILTER_CHANNEL(enum.IntEnum):
    #specifies FlexRay channel A for the PC
    A = 1
    #specifies FlexRay channel B for the PC
    B = 2

class s_xl_fr_acceptance_filter(ctypes.Structure):
    _fields_ = [
        #defines if the specified frame should be blocked or pass the filter
        ("filterStatus", ctypes.c_uint),
        #specifies the frame type that should be filtered
        ("filterTypeMask", ctypes.c_uint),
        #beginning of the slot range
        ("filterFirstSlot", ctypes.c_uint),
        #end of the slot range (can be the same as filterFirstSlot)
        ("filterLastSlot", ctypes.c_uint),
        #channel A, B for PC, channel A, B for COB
        ("filterChannelMask", ctypes.c_uint),
    ]
XLfrAcceptanceFilter = s_xl_fr_acceptance_filter

class XL_FR_FLAGS_CHIP(enum.IntFlag):
    CHANNEL_A = 1
    CHANNEL_B = 2
    # 3
    CHANNEL_AB = CHANNEL_A|CHANNEL_B
    #second CC channel A to initiate the coldstart
    CC_COLD_A = 4
    #second CC channel B to initiate the coldstart
    CC_COLD_B = 8
    # 12
    CC_COLD_AB = CC_COLD_A|CC_COLD_B
    #Spy mode flags
    SPY_CHANNEL_A = 16
    #Spy mode flags
    SPY_CHANNEL_B = 32

#driver queue overflow
XL_FR_QUEUE_OVERFLOW = 256

class XL_FR_FRAMEFLAG(enum.IntEnum):
    #indicates a startup frame
    STARTUP = 1
    #indicates a sync frame
    SYNC = 2
    #indicates a null frame
    NULLFRAME = 4
    #indicates a present payload preamble bit
    PAYLOAD_PREAMBLE = 8
    #reserved by Flexray protocol
    FR_RESERVED = 16
    #used for Tx events only
    REQ_TXACK = 32
    #indicates TxAck of SingleShot; used for TxAck events only
    TXACK_SS = REQ_TXACK
    #indicates unexpected Rx frame; used for Rx events only
    RX_UNEXPECTED = REQ_TXACK
    #flag used with TxAcks to indicate first TxAck after data update
    NEW_DATA_TX = 64
    #flag used with TxAcks indicating that data update has been lost
    DATA_UPDATE_LOST = 128
    SYNTAX_ERROR = 512
    CONTENT_ERROR = 1024
    SLOT_BOUNDARY_VIOLATION = 2048
    TX_CONFLICT = 4096
    EMPTY_SLOT = 8192
    #Only used with TxAcks: Frame has been transmitted. If not set after transmission, an error has occurred.
    FRAME_TRANSMITTED = 32768

class XL_FR_SPY_FRAMEFLAG_ERROR(enum.IntEnum):
    FRAMING_ERROR = 1
    HEADER_CRC_ERROR = 2
    FRAME_CRC_ERROR = 4
    BUS_ERROR = 8

class XL_FR_SPY_FRAMEFLAG_FRAME_CRC(enum.IntEnum):
    NEW_LAYOUT = 2147483648

class XL_FR_SPY_FRAMEFLAG_FRAME_FLAGS(enum.IntEnum):
    STATIC_FRAME = 1

class XL_FR_TX_MODE(enum.IntEnum):
    #'normal' cyclic mode
    CYCLIC = 1
    #sends only a single shot
    SINGLE_SHOT = 2
    #switch off TX
    NONE = 255

class XL_FR_PAYLOAD_INCREMENT(enum.IntEnum):
    INCREMENT_8BIT = 8
    INCREMENT_16BIT = 16
    INCREMENT_32BIT = 32
    INCREMENT_NONE = 0

class XL_FR_STATUS(enum.IntEnum):
    #indicates the actual state of the POC in operation control
    DEFAULT_CONFIG = 0
    READY = 1
    NORMAL_ACTIVE = 2
    NORMAL_PASSIVE = 3
    HALT = 4
    MONITOR_MODE = 5
    CONFIG = 15
    #indicates the actual state of the POC in the wakeup path
    WAKEUP_STANDBY = 16
    WAKEUP_LISTEN = 17
    WAKEUP_SEND = 18
    WAKEUP_DETECT = 19
    #indicates the actual state of the POC in the startup path
    STARTUP_PREPARE = 32
    COLDSTART_LISTEN = 33
    COLDSTART_COLLISION_RESOLUTION = 34
    COLDSTART_CONSISTENCY_CHECK = 35
    COLDSTART_GAP = 36
    COLDSTART_JOIN = 37
    INTEGRATION_COLDSTART_CHECK = 38
    INTEGRATION_LISTEN = 39
    INTEGRATION_CONSISTENCY_CHECK = 40
    INITIALIZE_SCHEDULE = 41
    ABORT_STARTUP = 42
    STARTUP_SUCCESS = 43

class XL_FR_ERROR_POC(enum.IntEnum):
    #Indicates the actual error mode of the POC: active (green)
    ACTIVE = 0
    #Indicates the actual error mode of the POC: passive (yellow)
    PASSIVE = 1
    #Indicates the actual error mode of the POC: comm-halt (red)
    COMM_HALT = 2

class XL_FR_ERROR_NIT(enum.IntEnum):
    #Syntax Error during NIT Channel A
    SENA = 256
    #Slot Boundary Violation during NIT Channel A
    SBNA = 512
    #Syntax Error during NIT Channel B
    SENB = 1024
    #Slot Boundary Violation during NIT Channel B
    SBNB = 2048

class XL_FR_ERROR_CLOCK(enum.IntEnum):
    #Set if no sync frames were received. -> no offset correction possible.
    MISSING_OFFSET_CORRECTION = 1
    #Set if max. offset correction limit is reached.
    MAX_OFFSET_CORRECTION_REACHED = 2
    #Set if no even/odd sync frames were received -> no rate correction possible.
    MISSING_RATE_CORRECTION = 4
    #Set if max. rate correction limit is reached.
    MAX_RATE_CORRECTION_REACHED = 8

class XL_FR_ERROR_CC(enum.IntEnum):
    #Parity Error, data from MHDS (internal ERay error)
    PERR = 64
    #Illegal Input Buffer Access (internal ERay error)
    IIBA = 512
    #Illegal Output Buffer Access (internal ERay error)
    IOBA = 1024
    #Message Handler Constraints Flag data from MHDF (internal ERay error)
    MHF = 2048
    #Error Detection on channel A, data from ACS
    EDA = 65536
    #Latest Transmit Violation on channel A
    LTVA = 131072
    #Transmit Across Boundary on Channel A
    TABA = 262144
    #Error Detection on channel B, data from ACS
    EDB = 16777216
    #Latest Transmit Violation on channel B
    LTVB = 33554432
    #Transmit Across Boundary on Channel B
    TABB = 67108864

class XL_FR_WAKEUP(enum.IntEnum):
    #No wakeup attempt since CONFIG state was left. (e.g. when a wakeup pattern A|B is received)
    UNDEFINED = 0
    #Frame header without coding violation received.
    RECEIVED_HEADER = 1
    #Wakeup pattern on the configured wakeup channel received.
    RECEIVED_WUP = 2
    #Detected collision during wakeup pattern transmission received.
    COLLISION_HEADER = 3
    #Collision during wakeup pattern transmission received.
    COLLISION_WUP = 4
    #Set when the CC stops wakeup.
    COLLISION_UNKNOWN = 5
    #Completed the transmission of the wakeup pattern.
    TRANSMITTED = 6
    #wakeup comes from external
    EXTERNAL_WAKEUP = 7
    #wakeupt pattern received from flexray bus
    WUP_RECEIVED_WITHOUT_WUS_TX = 16
    RESERVED = 255 #

class XL_FR_SYMBOL_STATUS(enum.IntEnum):
    #Syntax Error in Symbol Window Channel A
    SESA = 1
    #Slot Boundary Violation in Symbol Window Channel A
    SBSA = 2
    #Transmission Conflict in Symbol Window Channel A
    TCSA = 4
    #Syntax Error in Symbol Window Channel B
    SESB = 8
    #Slot Boundary Violation in Symbol Window Channel B
    SBSB = 16
    #Transmission Conflict in Symbol Window Channel B
    TCSB = 32
    #MTS received in Symbol Window Channel A
    MTSA = 64
    #MTS received in Symbol Window Channel B
    MTSB = 128

XL_FR_RX_EVENT_HEADER_SIZE = 32
XL_FR_MAX_EVENT_SIZE = 512

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
        ("data", ctypes.c_ubyte*XL_FR_MAX_DATA_LENGTH),
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
        ("data", ctypes.c_ubyte*XL_FR_MAX_DATA_LENGTH),
    ]
XL_FR_TX_FRAME_EV = s_xl_fr_tx_frame

class s_xl_fr_wakeup(ctypes.Structure):
    _fields_ = [
        #Actual cyclecount.
        ("cycleCount", ctypes.c_ubyte),
        #XL_FR_WAKEUP_UNDEFINED, ...
        ("wakeupStatus", ctypes.c_ubyte),
        ("reserved", ctypes.c_ubyte*6),
    ]
XL_FR_WAKEUP_EV = s_xl_fr_wakeup

class s_xl_fr_symbol_window(ctypes.Structure):
    _fields_ = [
        #XL_FR_SYMBOL_MTS, ...
        ("symbol", ctypes.c_uint),
        #XL_FR_SYMBOL_STATUS_SESA, ...
        ("flags", ctypes.c_uint),
        #Actual cyclecount.
        ("cycleCount", ctypes.c_ubyte),
        ("reserved", ctypes.c_ubyte*7),
    ]
XL_FR_SYMBOL_WINDOW_EV = s_xl_fr_symbol_window

class s_xl_fr_status(ctypes.Structure):
    _fields_ = [
        #POC status XL_FR_STATUS_ defines like, normal, active...
        ("statusType", ctypes.c_uint),
        ("reserved", ctypes.c_uint),
    ]
XL_FR_STATUS_EV = s_xl_fr_status

class s_xl_fr_nm_vector(ctypes.Structure):
    _fields_ = [
        ("nmVector", ctypes.c_ubyte*12),
        #Actual cyclecount.
        ("cycleCount", ctypes.c_ubyte),
        ("reserved", ctypes.c_ubyte*3),
    ]
XL_FR_NM_VECTOR_EV = s_xl_fr_nm_vector

class s_xl_fr_error_poc_mode(ctypes.Structure):
    _fields_ = [
        #error mode like: active, passive, comm_halt
        ("errorMode", ctypes.c_ubyte),
        ("reserved", ctypes.c_ubyte*3),
    ]
XL_FR_ERROR_POC_MODE_EV = s_xl_fr_error_poc_mode

class s_xl_fr_error_sync_frames(ctypes.Structure):
    _fields_ = [
        #valid RX/TX sync frames on frCh A for even cycles
        ("evenSyncFramesA", ctypes.c_ushort),
        #valid RX/TX sync frames on frCh A for odd cycles
        ("oddSyncFramesA", ctypes.c_ushort),
        #valid RX/TX sync frames on frCh B for even cycles
        ("evenSyncFramesB", ctypes.c_ushort),
        #valid RX/TX sync frames on frCh B for odd cycles
        ("oddSyncFramesB", ctypes.c_ushort),
        ("reserved", ctypes.c_uint),
    ]
XL_FR_ERROR_SYNC_FRAMES_EV = s_xl_fr_error_sync_frames

class s_xl_fr_error_clock_corr_failure(ctypes.Structure):
    _fields_ = [
        #valid RX/TX sync frames on frCh A for even cycles
        ("evenSyncFramesA", ctypes.c_ushort),
        #valid RX/TX sync frames on frCh A for odd cycles
        ("oddSyncFramesA", ctypes.c_ushort),
        #valid RX/TX sync frames on frCh B for even cycles
        ("evenSyncFramesB", ctypes.c_ushort),
        #valid RX/TX sync frames on frCh B for odd cycles
        ("oddSyncFramesB", ctypes.c_ushort),
        #missing/maximum rate/offset correction flags.
        ("flags", ctypes.c_uint),
        #E-Ray: CCEV register (CCFC value)
        ("clockCorrFailedCounter", ctypes.c_uint),
        ("reserved", ctypes.c_uint),
    ]
XL_FR_ERROR_CLOCK_CORR_FAILURE_EV = s_xl_fr_error_clock_corr_failure

class s_xl_fr_error_nit_failure(ctypes.Structure):
    _fields_ = [
        #flags for NIT boundary, syntax error...
        ("flags", ctypes.c_uint),
        ("reserved", ctypes.c_uint),
    ]
XL_FR_ERROR_NIT_FAILURE_EV = s_xl_fr_error_nit_failure

class s_xl_fr_error_cc_error(ctypes.Structure):
    _fields_ = [
        #internal CC errors (Transmit Across Boundary, Transmit Violation...)
        ("ccError", ctypes.c_uint),
        ("reserved", ctypes.c_uint),
    ]
XL_FR_ERROR_CC_ERROR_EV = s_xl_fr_error_cc_error

class s_xl_fr_error_info(ctypes.Union):
    _fields_ = [
        #E-RAY: EIR_PEMC
        ("frPocMode", s_xl_fr_error_poc_mode),
        #E-RAY: EIR_SFBM
        ("frSyncFramesBelowMin", s_xl_fr_error_sync_frames),
        #E-RAY: EIR_SFO
        ("frSyncFramesOverload", s_xl_fr_error_sync_frames),
        #E-RAY: EIR_CCF
        ("frClockCorrectionFailure", s_xl_fr_error_clock_corr_failure),
        #NIT part of the E_RAY: SWNIT register
        ("frNitFailure", s_xl_fr_error_nit_failure),
        #internal CC error flags (E-RAY: EIR)
        ("frCCError", s_xl_fr_error_cc_error),
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
        #XL_FR_SPY_FRAMEFLAG_XXX values
        ("frameError", ctypes.c_ubyte),
        ("tssLength", ctypes.c_ubyte),
        ("headerFlags", ctypes.c_ushort),
        ("slotID", ctypes.c_ushort),
        ("headerCRC", ctypes.c_ushort),
        ("payloadLength", ctypes.c_ubyte),
        ("cycleCount", ctypes.c_ubyte),
        ("frameFlags", ctypes.c_ubyte),
        ("reserved", ctypes.c_ubyte),
        ("frameCRC", ctypes.c_uint),
        ("data", ctypes.c_ubyte*XL_FR_MAX_DATA_LENGTH),
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
        #XL_FR_START_CYCLE_EV
        ("frStartCycle", s_xl_fr_start_cycle),
        #XL_FR_RX_FRAME_EV
        ("frRxFrame", s_xl_fr_rx_frame),
        #XL_FR_TX_FRAME_EV
        ("frTxFrame", s_xl_fr_tx_frame),
        #XL_FR_WAKEUP_EV
        ("frWakeup", s_xl_fr_wakeup),
        #XL_FR_SYMBOL_WINDOW_EV
        ("frSymbolWindow", s_xl_fr_symbol_window),
        #XL_FR_ERROR_EV
        ("frError", s_xl_fr_error),
        #XL_FR_STATUS_EV
        ("frStatus", s_xl_fr_status),
        #XL_FR_NM_VECTOR_EV
        ("frNmVector", s_xl_fr_nm_vector),
        #XL_FR_SYNC_PULSE_EV
        ("frSyncPulse", s_xl_sync_pulse_ev),
        #XL_FR_SPY_FRAME_EV
        ("frSpyFrame", s_xl_fr_spy_frame),
        #XL_FR_SPY_SYMBOL_EV
        ("frSpySymbol", s_xl_fr_spy_symbol),
        #XL_APPLICATION_NOTIFICATION_EV
        ("applicationNotification", s_xl_application_notification),
    ]

XLfrEventTag = ctypes.c_ushort

class s_xl_fr_event(ctypes.Structure):
    _anonymous_ = ("tagData",)
    _fields_ = [
        #overall size of the complete event
        ("size", ctypes.c_uint),
        #type of the event
        ("tag", XLfrEventTag),
        ("channelIndex", ctypes.c_ushort),
        ("userHandle", ctypes.c_uint),
        #frChannel e.g. XL_FR_CHANNEL_A (lower 8 bit), queue overflow (upper 8bit)
        ("flagsChip", ctypes.c_ushort),
        ("reserved", ctypes.c_ushort),
        #raw timestamp
        ("timeStamp", XLuint64),
        #timestamp which is synchronized by the driver
        ("timeStampSync", XLuint64),
        ("tagData", s_xl_fr_tag_data),
    ]
XLfrEvent = s_xl_fr_event

### IO XL API ###

class XL_DAIO_PORT_TYPE_MASK(enum.IntEnum):
    DIGITAL = 1
    ANALOG = 2

class XL_DAIO_TRIGGER_MODE(enum.IntEnum):
    CYCLIC = 1
    PORT = 2

class s_xl_daio_trigger_type_params_digital(ctypes.Structure):
    _fields_ = [
        ("portMask", ctypes.c_uint),
        # Use defines XL_DAIO_TRIGGER_TYPE_xxx(RISIONG|FALLING|BOTH)
        ("type", ctypes.c_uint),
    ]

class u_xl_trigger_type_params(ctypes.Union):
    _fields_ = [
        #specify time in microseconds
        ("cycleTime", ctypes.c_uint),
        ("digital", s_xl_daio_trigger_type_params_digital),
    ]

class s_xl_daio_trigger_mode(ctypes.Structure):
    _anonymous_ = ("param",)
    _fields_ = [
        #Use defines XL_DAIO_PORT_TYPE_MASK_xxx. Unused for VN1630/VN1640.
        ("portTypeMask", ctypes.c_uint),
        #Use defines XL_DAIO_TRIGGER_TYPE_xxx(CYCLIC|PORT)
        ("triggerType", ctypes.c_uint),
        ("param", u_xl_trigger_type_params),
    ]
XLdaioTriggerMode = s_xl_daio_trigger_mode

class XL_DAIO_TRIGGER_TYPE(enum.IntEnum):
    RISING = 1
    FALLING = 2
    BOTH = 3

class xl_daio_set_port(ctypes.Structure):
    _fields_ = [
        #Only one signal group is allowed. One of the defines XL_DAIO_PORT_TYPE_MASK_*
        ("portType", ctypes.c_uint),
        #Mask of affected ports.
        ("portMask", ctypes.c_uint),
        #Special function of port. One of the defines XL_DAIO_PORT_DIGITAL_* or XL_DAIO_PORT_ANALOG_*
        ("portFunction", ctypes.c_uint*8),
        #Set this parameters to zero!
        ("reserved", ctypes.c_uint*8),
    ]
XLdaioSetPort = xl_daio_set_port

class XL_DAIO_PORT_DIGITAL(enum.IntEnum):
    IN = 0
    PUSHPULL = 1
    OPENDRAIN = 2
    #(only for digital pin 4..7)
    SWITCH = 5
    #(only for WakeUp line)
    IN_OUT = 6

class XL_DAIO_PORT_ANALOG(enum.IntEnum):
    IN = 0
    OUT = 1
    DIFF = 2
    OFF = 3

class XL_DAIO_DO_LEVEL(enum.IntEnum):
    LEVEL_0V = 0
    LEVEL_5V = 5
    LEVEL_12V = 12

class xl_daio_digital_params(ctypes.Structure):
    _fields_ = [
        #Use defines XL_DAIO_PORT_MASK_DIGITAL_*
        ("portMask", ctypes.c_uint),
        #Specify the port value (ON/HIGH 1 | OFF/LOW - 0)
        ("valueMask", ctypes.c_uint),
    ]
XLdaioDigitalParams = xl_daio_digital_params

class XL_DAIO_PORT_MASK_DIGITAL(enum.IntEnum):
    D0 = 1
    D1 = 2
    D2 = 4
    D3 = 8
    D4 = 16
    D5 = 32
    D6 = 64
    D7 = 128

class xl_daio_analog_params(ctypes.Structure):
    _fields_ = [
        #Use defines XL_DAIO_PORT_MASK_ANALOG_*
        ("portMask", ctypes.c_uint),
        #12-bit values
        ("value", ctypes.c_uint*8),
    ]
XLdaioAnalogParams = xl_daio_analog_params

class XL_DAIO_PORT_MASK_ANALOG(enum.IntEnum):
    A0 = 1
    A1 = 2
    A2 = 4
    A3 = 8

class XL_DAIO_EVT_ID(enum.IntEnum):
    #1
    XL_DAIO_EVT_ID_DIGITAL = XL_DAIO_PORT_TYPE_MASK.DIGITAL
    #2
    XL_DAIO_EVT_ID_ANALOG  = XL_DAIO_PORT_TYPE_MASK.ANALOG

### K-Line XL API ###

class XL_KLINE_EVT(enum.IntEnum):
    """K-Line event tags"""
    RX_DATA = 1
    TX_DATA = 2
    TESTER_5BD = 3
    ECU_5BD = 5
    TESTER_FI_WU_PATTERN = 7
    ECU_FI_WU_PATTERN = 8
    ERROR = 9
    CONFIRMATION = 10

class s_xl_kline_uart_params(ctypes.Structure):
    _fields_ = [
        ("databits", ctypes.c_uint),
        ("stopbits", ctypes.c_uint),
        ("parity", ctypes.c_uint),
    ]
XLklineUartParameter = s_xl_kline_uart_params

class s_xl_kline_init_tester(ctypes.Structure):
    _fields_ = [
        #us
        ("TiniL", ctypes.c_uint),
        #us
        ("Twup", ctypes.c_uint),
        ("reserved", ctypes.c_uint),
    ]
XLklineInitTester = s_xl_kline_init_tester

class s_xl_kline_init_5BdTester(ctypes.Structure):
    _fields_ = [
        ("addr", ctypes.c_uint),
        ("rate5bd", ctypes.c_uint),
        #us
        ("W1min", ctypes.c_uint),
        #us
        ("W1max", ctypes.c_uint),
        #us
        ("W2min", ctypes.c_uint),
        #us
        ("W2max", ctypes.c_uint),
        #us
        ("W3min", ctypes.c_uint),
        #us
        ("W3max", ctypes.c_uint),
        #us
        ("W4", ctypes.c_uint),
        #us
        ("W4min", ctypes.c_uint),
        #us
        ("W4max", ctypes.c_uint),
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
        #us
        ("W1", ctypes.c_uint),
        #us
        ("W2", ctypes.c_uint),
        #us
        ("W3", ctypes.c_uint),
        #us
        ("W4", ctypes.c_uint),
        #us
        ("W4min", ctypes.c_uint),
        #us
        ("W4max", ctypes.c_uint),
        ("kb1", ctypes.c_uint),
        ("kb2", ctypes.c_uint),
        ("addrNot", ctypes.c_uint),
        ("reserved", ctypes.c_uint),
    ]
XLkline5BdEcu = s_xl_kline_init_5BdEcu

class s_xl_kline_set_com_tester(ctypes.Structure):
    _fields_ = [
        #us
        ("P1min", ctypes.c_uint),
        #us
        ("P4", ctypes.c_uint),
        ("reserved", ctypes.c_uint),
    ]
XLklineSetComTester = s_xl_kline_set_com_tester

class s_xl_kline_set_com_ecu(ctypes.Structure):
    _fields_ = [
        #us
        ("P1", ctypes.c_uint),
        #us
        ("P4min", ctypes.c_uint),
        #us
        ("TinilMin", ctypes.c_uint),
        #us
        ("TinilMax", ctypes.c_uint),
        #us
        ("TwupMin", ctypes.c_uint),
        #us
        ("TwupMax", ctypes.c_uint),
        ("reserved", ctypes.c_uint),
    ]
XLklineSetComEcu = s_xl_kline_set_com_ecu


class XL_KLINE_UART_PARITY(enum.IntEnum):
    """defines for xlKlineSetUartParams"""
    NONE = 0
    EVEN = 1
    ODD = 2
    MARK = 3
    SPACE = 4

class XL_KLINE_TRXMODE(enum.IntEnum):
    """defines for xlKlineSwitchHighspeedMode"""
    NORMAL = 0
    HIGHSPEED = 1

class XL_KLINE_TESTERRESISTOR(enum.IntEnum):
    """defines for xlKlineSwitchTesterResistor"""
    OFF = 0
    ON = 1

XL_KLINE_UNCONFIGURE_ECU = 0
XL_KLINE_CONFIGURE_ECU = 1

class XL_KLINE_EVT_TAG_5BD(enum.IntEnum):
    """event defines 5bdTag"""
    ADDR = 1
    BAUDRATE = 2
    KB1 = 3
    KB2 = 4
    KB2NOT = 5
    ADDRNOT = 6

class XL_KLINE_BYTE_ERROR_MASK(enum.IntEnum):
    """defines for the tx/rx byte error mask"""
    FRAMING_ERROR_MASK = 1
    PARITY_ERROR_MASK = 2

class XL_KLINE_EVT_TAG(enum.IntEnum):
    """defines for confirmation event"""
    SET_COMM_PARAM_TESTER = 1
    COMM_PARAM_ECU = 2
    SWITCH_HIGHSPEED = 3

class XL_KLINE_FLAG(enum.IntEnum):
    """"""
    TAKE_KB2NOT  = 0x80000000
    TAKE_ADDRNOT = 0x80000000

class XL_KLINE_ERROR_TYPE(enum.IntEnum):
    """defines for T_KLINE_ERROR - errorType"""
    TYPE_RXTX_ERROR = 1
    TYPE_5BD_TESTER = 2
    TYPE_5BD_ECU = 3
    TYPE_IBS = 4
    TYPE_FI = 5

class XL_KLINE_ERR_RXTX(enum.IntEnum):
    """defines for XL_KLINE_ERROR_TYPE_RXTX_ERROR / XL_KLINE_ERROR_TYPE_FI"""
    #unexpected activity
    UA = 4
    #missing activity
    MA = 2
    #invalid sync byte
    ISB = 1

class XL_KLINE_ERR_TESTER(enum.IntEnum):
    """defines for XL_KLINE_ERROR_TYPE_5BD_TESTER"""
    W1MIN = 1
    W1MAX = 2
    W2MIN = 3
    W2MAX = 4
    W3MIN = 5
    W3MAX = 6
    W4MIN = 7
    W4MAX = 8

class XL_KLINE_ERR_ECU(enum.IntEnum):
    """defines for XL_KLINE_ERROR_TYPE_5BD_ECU"""
    W4MIN = 1
    W4MAX = 2

class XL_KLINE_ERR_IBS(enum.IntEnum):
    """defines for XL_KLINE_ERROR_TYPE_IBS"""
    P1 = 1
    P4 = 2

### Ethernet API ###

XL_ETH_EVENT_SIZE_HEADER = 32
XL_ETH_EVENT_SIZE_MAX = 2048
#Maximum size of ethernet receive queue: 64 MByte
XL_ETH_RX_FIFO_QUEUE_SIZE_MAX = 67108864
#Minimum size of ethernet receive queue: 64 KByte
XL_ETH_RX_FIFO_QUEUE_SIZE_MIN = 65536
#maximum payload length for sending an ethernet packet
XL_ETH_PAYLOAD_SIZE_MAX = 1500
#minimum payload length for sending an ethernet packet (42 octets with VLAN tag present)
XL_ETH_PAYLOAD_SIZE_MIN = 46
#maximum buffer size for storing a "raw" Ethernet frame (including VLAN tags, if present)
XL_ETH_RAW_FRAME_SIZE_MAX = 1600
#minimum buffer size for storing a "raw" Ethernet frame (including VLAN tags, if present)
XL_ETH_RAW_FRAME_SIZE_MIN = 24
XL_ETH_MACADDR_OCTETS = 6
XL_ETH_ETHERTYPE_OCTETS = 2
XL_ETH_VLANTAG_OCTETS = 4

class XL_ETH_CHANNEL_CAP(enum.IntEnum):
    #Channel supports IEEE 802.3pw (100BASE-T1) - Automotive Ethernet over single twisted pair
    IEEE100T1 = 1
    #Channel supports IEEE 802.3u (100-BASE-TX) and 802.3i (10BASE-T) - Ethernet and Fast Ethernet
    IEEE100TX = 2
    #Channel supports IEEE 802.3ab (1000BASE-T) - Gigabit Ethernet
    IEEE1000T = 4
    #Channel supports IEEE 802.3bp (1000BASE-T1) - Automotive Ethernet over single twisted pair
    IEEE1000T1 = 8

class XL_NET_ETH_SWITCH_CAP(enum.IntEnum):
    #Switch type is "normal" switch (learning is on)
    REALSWITCH = 0
    #Switch type is direct connection
    DIRECTCONN = 1
    #Switch type is TAP
    TAP_LINK = 2

class XL_ETH_FLAGS_CHIP(enum.IntEnum):
    CONNECTOR_RJ45 = 1
    CONNECTOR_DSUB = 2
    PHY_IEEE = 4
    PHY_BROADR = 8
    #For Rx and RxError events
    FRAME_BYPASSED = 16
    QUEUE_OVERFLOW = 256
    #MAC bypass queue full condition occurred, one or more packets dropped
    BYPASS_QUEUE_OVERFLOW = 32768

class XL_ETH_MODE_SPEED(enum.IntEnum):
    #Set connection speed set to 100 Mbps via auto-negotiation
    AUTO_100 = 2
    #Set connection speed to 1000 Mbps via auto-negotiation
    AUTO_1000 = 4
    #Set connection speed automatically to either 100 or 1000 Mbps
    AUTO_100_1000 = 5
    #Set connection speed to 100 Mbps. Auto-negotiation disabled.
    FIXED_100 = 8
    #Set connection speed to 1 Gbps. Auto-negotiation disabled.
    FIXED_1000 = 9

class XL_ETH_MODE_DUPLEX(enum.IntEnum):
    #Used for BroadR-Reach since only full duplex mode possible.
    DONT_CARE = 0
    #Duplex mode set via auto-negotiation. Requires connection speed set to an "auto" value. Only for IEEE 802.3
    AUTO = 1
    #Full duplex mode. Only for IEEE 802.3
    FULL = 3

class XL_ETH_MODE_CONNECTOR(enum.IntEnum):
    #Apart from VN5610(A), always only one connector available anyway
    DONT_CARE = 0
    #Using RJ-45 connector
    RJ45 = 1
    #Using D-Sub connector
    DSUB = 2

class XL_ETH_MODE_PHY(enum.IntEnum):
    #Set whatever PHY layer is available
    DONT_CARE = 0
    #Set IEEE 802.3
    IEEE_802_3 = 1
    #Set BroadR-Reach
    BROADR_REACH = 2

class XL_ETH_MODE_CLOCK(enum.IntEnum):
    #Used for IEEE 802.3 100 and 10 MBit
    DONT_CARE = 0
    #Clock mode set automatically via auto-negotiation. Only for 1000Base-T if speed mode is one of the "auto" modes
    AUTO = 1
    #Clock mode is master. Only for 1000Base-T or BroadR-Reach
    MASTER = 2
    #Clock mode is slave. Only for 1000Base-T or BroadR-Reach
    SLAVE = 3

class XL_ETH_MODE_MDI(enum.IntEnum):
    #Perform MDI auto detection
    AUTO = 1
    #Direct MDI (connected to switch)
    STRAIGHT = 2
    #Crossover MDI (connected to endpoint)
    CROSSOVER = 3

class XL_ETH_MODE_BR_PAIR(enum.IntEnum):
    #Used for IEEE 802.3
    DONT_CARE = 0
    #BR 1-pair connection. Only for BroadR-Reach
    BR_1PAIR = 1

class XL_ETH_STATUS_LINK(enum.IntEnum):
    #The link state could not be determined (e.g. lost connection to board)
    UNKNOWN = 0
    #Link is down (no cable attached, no configuration set, configuration does not match)
    DOWN = 1
    #Link is up
    UP = 2
    #Link is in error state (e.g. auto-negotiation failed)
    ERROR = 4

class XL_ETH_STATUS_SPEED(enum.IntEnum):
    #Connection speed could not be determined (e.g. during auto-negotiation or if link down)
    UNKNOWN = 0
    #Link speed is 10 Mbps
    SPEED_10 = 1
    #Link speed is 100 Mbps
    SPEED_100 = 2
    #Link speed is 1000 Mbps
    SPEED_1000 = 3
    #Link speed is 2500 Mbps
    SPEED_2500 = 4
    #Link speed is 5000 Mbps
    SPEED_5000 = 5
    #Link speed is 10000 Mbps
    SPEED_10000 = 6

class XL_ETH_STATUS_DUPLEX(enum.IntEnum):
    #Duplex mode could not be determined (e.g. during auto-negotiation or if link down)
    UNKNOWN = 0
    #Full duplex mode
    FULL = 2

class XL_ETH_STATUS_MDI(enum.IntEnum):
    #MDI mode could not be determined  (e.g. during auto-negotiation or if link down)
    UNKNOWN = 0
    #Direct MDI
    STRAIGHT = 1
    #Crossover MDI
    CROSSOVER = 2

class XL_ETH_STATUS_CONNECTOR(enum.IntEnum):
    #Using the only available connector on channel
    DEFAULT = 0
    #Using RJ-45 connector
    RJ45 = 1
    #Using D-Sub connector
    DSUB = 2

class XL_ETH_STATUS_PHY(enum.IntEnum):
    #PHY is currently unknown (e.g. if link is down)
    UNKNOWN = 0
    #PHY is IEEE 802.3
    IEEE_802_3 = 1
    #PHY is BroadR-Reach
    BROADR_REACH = 2
    #PHY is IEEE  100BASE-T1 (802.3bw) - intentionally same value as BroadR-Reach 100Bit
    PHY_100BASE_T1 = 2
    #PHY is IEEE 1000BASE-T1 (802.3bp)
    PHY_1000BASE_T1 = 4

class XL_ETH_STATUS_CLOCK(enum.IntEnum):
    #Clock mode not relevant. Only for IEEE 802.3 100/10 MBit
    DONT_CARE = 0
    #Clock mode is master. Only for 1000Base-T or BroadR-Reach
    MASTER = 1
    #Clock mode is slave. Only for 1000Base-T or BroadR-Reach
    SLAVE = 2

class XL_ETH_STATUS_BR_PAIR(enum.IntEnum):
    #No BR pair available. Only for IEEE 802.3 1000/100/10 MBit
    DONT_CARE = 0
    #BR 1-pair connection. Only for BroadR-Reach
    BR_1PAIR = 1

class XL_ETH_RX_ERROR(enum.IntEnum):
    #Invalid length error. Set when the receive frame has an invalid length as defined by IEEE802.3
    INVALID_LENGTH = 1
    #CRC error. Set when frame is received with CRC-32 error but valid length
    INVALID_CRC = 2
    #Corrupted receive frame caused by a PHY error
    PHY_ERROR = 4

#Use the given source MAC address (not set by hardware)
XL_ETH_DATAFRAME_FLAGS_USE_SOURCE_MAC = 1

class XL_ETH_BYPASS(enum.IntEnum):
    #Bypass inactive (default state)
    INACTIVE = 0
    #Bypass active via PHY loop
    PHY = 1
    #Bypass active via L2 switch (using MAC cores)
    MACCORE = 2

class XL_ETH_TX_ERROR(enum.IntEnum):
    #Bypass activated
    BYPASS_ENABLED = 1
    #No Link
    NO_LINK = 2
    #PHY not yet configured
    PHY_NOT_CONFIGURED = 3
    #Frame with invalid length transmitted
    INVALID_LENGTH = 7

class XL_ETH_NETWORK_TX_ERROR(enum.IntEnum):
    #No Link
    NO_LINK = 1
    #PHY not yet configured
    PHY_NOT_CONFIGURED = 2
    #PHY Bypass activated
    PHY_BRIDGE_ENABLED = 4
    #RGMII Converter in reset
    CONVERTER_RESET = 8
    #Invalid length error. Set when the frame has an invalid length as defined by IEEE802.3
    INVALID_LENGTH = 16
    #CRC error. Set when frame is transmitted with CRC-32 error but valid length
    INVALID_CRC = 32
    #Invalid src or dest MAC address
    MACADDR_ERROR = 64

class XL_ETH_NETWORK_RX_ERROR(enum.IntEnum):
    #Invalid length error. Set when the receive frame has an invalid length as defined by IEEE802.3
    INVALID_LENGTH = 1
    #CRC error. Set when frame is received with CRC-32 error but valid length
    INVALID_CRC = 2
    #Corrupted receive frame caused by a PHY error
    PHY_ERROR = 4
    #Invalid src or dest MAC address
    MACADDR_ERROR = 8

XL_NET_MAX_NAME_LENGTH = 32 #

class XL_ACCESS_TYPE(enum.IntEnum):
    #Only for Ethernet uplink, means UDP transfers. (Not supported yet)
    UNRELIABLE = 0
    #Always for USB uplink or TCP for Ethernet host uplink
    RELIABLE = 1

XL_INVALID_NETWORKID = -1
XLnetworkId, pXLnetworkId = ctypes.c_int, ctypes.POINTER(ctypes.c_int)
XL_INVALID_SWITCHID = -1
XLswitchId, pXLswitchId = ctypes.c_int, ctypes.POINTER(ctypes.c_int)
XL_INVALID_NETWORKHANDLE = -1
XLnetworkHandle, pXLnetworkHandle = XLlong, ctypes.POINTER(XLlong)
XL_INVALID_ETHPORTHANDLE = -1
XLethPortHandle, pXLethPortHandle = XLlong, ctypes.POINTER(XLlong)
XL_INVALID_RXHANDLE = -1
XLrxHandle, pXLrxHandle = XLlong, ctypes.POINTER(XLlong)

class XL_NET_CFG(enum.IntEnum):
    STAT_OK = 0
    DUPLICATE_SEGMENT_NAME = 1
    DUPLICATE_VP_NAME = 2
    DUPLICATE_MP_NAME = 3

XLethEventTag = ctypes.c_ushort

class s_xl_eth_frame(ctypes.Structure):
    _fields_ = [
        #Ethernet type in network byte order
        ("etherType", ctypes.c_ushort),
        ("payload", ctypes.c_ubyte*XL_ETH_PAYLOAD_SIZE_MAX),
    ]
T_XL_ETH_FRAME = s_xl_eth_frame

class s_xl_eth_framedata(ctypes.Union):
    _fields_ = [
        ("rawData", ctypes.c_ubyte*XL_ETH_RAW_FRAME_SIZE_MAX),
        ("ethFrame", s_xl_eth_frame),
    ]
T_XL_ETH_FRAMEDATA = s_xl_eth_framedata

class s_xl_eth_dataframe_rx(ctypes.Structure):
    _anonymous_ = ("frameData",)
    _fields_ = [
        #FPGA internal identifier unique to every received frame
        ("frameIdentifier", ctypes.c_uint),
        #transmit duration of the Ethernet frame, in nanoseconds
        ("frameDuration", ctypes.c_uint),
        #Overall data length of <frameData>
        ("dataLen", ctypes.c_ushort),
        #currently reserved field - not used, ignore
        ("reserved", ctypes.c_ushort),
        #currently reserved field - not used, ignore
        ("reserved2", ctypes.c_uint*3),
        #Frame Check Sum
        ("fcs", ctypes.c_uint),
        #Destination MAC address
        ("destMAC", ctypes.c_ubyte*XL_ETH_MACADDR_OCTETS),
        #Source MAC address
        ("sourceMAC", ctypes.c_ubyte*XL_ETH_MACADDR_OCTETS),
        ("frameData", s_xl_eth_framedata),
    ]
T_XL_ETH_DATAFRAME_RX = s_xl_eth_dataframe_rx

class s_xl_eth_dataframe_rxerror(ctypes.Structure):
    _anonymous_ = ("frameData",)
    _fields_ = [
        #FPGA internal identifier unique to every received frame
        ("frameIdentifier", ctypes.c_uint),
        #transmit duration of the Ethernet frame, in nanoseconds
        ("frameDuration", ctypes.c_uint),
        #Error information (XL_ETH_RX_ERROR_*)
        ("errorFlags", ctypes.c_uint),
        #Overall data length of <frameData>
        ("dataLen", ctypes.c_ushort),
        #currently reserved field - not used, ignore
        ("reserved", ctypes.c_ushort),
        #currently reserved field - not used, ignore
        ("reserved2", ctypes.c_uint*3),
        #Frame Check Sum
        ("fcs", ctypes.c_uint),
        #Destination MAC address
        ("destMAC", ctypes.c_ubyte*XL_ETH_MACADDR_OCTETS),
        #Source MAC address
        ("sourceMAC", ctypes.c_ubyte*XL_ETH_MACADDR_OCTETS),
        ("frameData", s_xl_eth_framedata),
    ]
T_XL_ETH_DATAFRAME_RX_ERROR = s_xl_eth_dataframe_rxerror

class s_xl_eth_dataframe_tx(ctypes.Structure):
    _anonymous_ = ("frameData",)
    _fields_ = [
        #FPGA internal identifier unique to every frame sent
        ("frameIdentifier", ctypes.c_uint),
        #Flags to specify (see XL_ETH_DATAFRAME_FLAGS_)
        ("flags", ctypes.c_uint),
        #Overall data length of <frameData>
        ("dataLen", ctypes.c_ushort),
        #currently reserved field - must be set to "0"
        ("reserved", ctypes.c_ushort),
        #reserved field - must be set to "0"
        ("reserved2", ctypes.c_uint*4),
        #Destination MAC address
        ("destMAC", ctypes.c_ubyte*XL_ETH_MACADDR_OCTETS),
        #Source MAC address
        ("sourceMAC", ctypes.c_ubyte*XL_ETH_MACADDR_OCTETS),
        ("frameData", s_xl_eth_framedata),
    ]
T_XL_ETH_DATAFRAME_TX = s_xl_eth_dataframe_tx

class s_xl_eth_dataframe_tx_event(ctypes.Structure):
    _anonymous_ = ("frameData",)
    _fields_ = [
        #FPGA internal identifier unique to every frame sent
        ("frameIdentifier", ctypes.c_uint),
        #Flags (see XL_ETH_DATAFRAME_FLAGS_)
        ("flags", ctypes.c_uint),
        #Overall data length of <frameData>
        ("dataLen", ctypes.c_ushort),
        #currently reserved field - not used, ignore
        ("reserved", ctypes.c_ushort),
        #transmit duration of the Ethernet frame, in nanoseconds
        ("frameDuration", ctypes.c_uint),
        #currently reserved field - not used, ignore
        ("reserved2", ctypes.c_uint*2),
        #Frame Check Sum
        ("fcs", ctypes.c_uint),
        #Destination MAC address
        ("destMAC", ctypes.c_ubyte*XL_ETH_MACADDR_OCTETS),
        #Source MAC address
        ("sourceMAC", ctypes.c_ubyte*XL_ETH_MACADDR_OCTETS),
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
        #(XL_ETH_STATUS_LINK_*)      Ethernet connection status
        ("link", ctypes.c_uint),
        #(XL_ETH_STATUS_SPEED_*)     Link connection speed
        ("speed", ctypes.c_uint),
        #(XL_ETH_STATUS_DUPLEX_*)    Ethernet duplex mode. 1000Base-T always uses full duplex.
        ("duplex", ctypes.c_uint),
        #(XL_ETH_STATUS_MDI_*)       Currently active MDI-mode
        ("mdiType", ctypes.c_uint),
        #(XL_ETH_STATUS_CONNECTOR_*) Connector (plug) to use (BroadR-REACH or RJ-45)
        ("activeConnector", ctypes.c_uint),
        #(XL_ETH_STATUS_PHY_*)       Currently active physical layer
        ("activePhy", ctypes.c_uint),
        #(XL_ETH_STATUS_CLOCK_*)     When in 1000Base-T or BroadR-mode, currently active mode
        ("clockMode", ctypes.c_uint),
        #(XL_ETH_STATUS_BR_PAIR_*)   When in BroadR-mode, number of used cable pairs
        ("brPairs", ctypes.c_uint),
    ]
T_XL_ETH_CHANNEL_STATUS = s_xl_eth_channel_status

class s_xl_eth_txAck(ctypes.Structure):
    _fields_ = [
        #FPGA internal identifier unique to every frame sent
        ("frameIdentifier", ctypes.c_uint),
        #Frame Check Sum
        ("fcs", ctypes.c_uint),
        #Source MAC address
        ("sourceMAC", ctypes.c_ubyte*XL_ETH_MACADDR_OCTETS),
        #currently reserved field - not used
        ("reserved", ctypes.c_ubyte*2),
    ]
s_xl_eth_txAckSw = s_xl_eth_txAck

class s_xl_eth_txError(ctypes.Structure):
    _fields_ = [
        ("errorType", ctypes.c_uint),
        #FPGA internal identifier unique to every frame sent
        ("frameIdentifier", ctypes.c_uint),
        #Frame Check Sum
        ("fcs", ctypes.c_uint),
        #Source MAC address
        ("sourceMAC", ctypes.c_ubyte*XL_ETH_MACADDR_OCTETS),
        #currently reserved field - not used
        ("reserved", ctypes.c_ubyte*2),
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
        #Type of event lost
        ("eventTypeLost", XLethEventTag),
        #currently reserved field - not used
        ("reserved", ctypes.c_ushort),
        #Reason code why the events were lost (0 means unknown)
        ("reason", ctypes.c_uint),
        ("eventInfo", u_xl_eth_eventInfo),
    ]
T_XL_ETH_LOSTEVENT = s_xl_eth_lostevent

class s_xl_eth_tag_data(ctypes.Union):
    _fields_ = [
        ("rawData", ctypes.c_ubyte*XL_ETH_EVENT_SIZE_MAX),
        #(tag==XL_ETH_EVENT_TAG_FRAMERX) - Frame received from network
        ("frameRxOk", s_xl_eth_dataframe_rx),
        #(tag==XL_ETH_EVENT_TAG_FRAMERX_ERROR) - Erroneous frame received from network
        ("frameRxError", s_xl_eth_dataframe_rxerror),
        #(tag==XL_ETH_EVENT_TAG_FRAMETX_ACK) - ACK for frame sent by application
        ("frameTxAck", s_xl_eth_dataframe_tx_event),
        #(tag==XL_ETH_EVENT_TAG_FRAMETX_ACK_SWITCH) - ACK for frame sent by switch
        ("frameTxAckSw", s_xl_eth_dataframe_tx_event),
        #(tag==XL_ETH_EVENT_TAG_FRAMETX_ERROR_OTHER_APP) - ACK for frame sent by another application
        ("frameTxAckOtherApp", s_xl_eth_dataframe_tx_event),
        #(tag==XL_ETH_EVENT_TAG_FRAMETX_ERROR) - NACK for frame sent by application (frame could not be transmitted)
        ("frameTxError", s_xl_eth_dataframe_txerror),
        #(tag==XL_ETH_EVENT_TAG_FRAMETX_ERROR_SWITCH) - NACK for frame sent by switch. May indicate internal processing failure (e.g. queue full condition)
        ("frameTxErrorSw", s_xl_eth_dataframe_txerror),
        #(tag==XL_ETH_EVENT_TAG_FRAMETX_ERROR_OTHER_APP) - NACK for frame sent by another application
        ("frameTxErrorOtherApp", s_xl_eth_dataframe_txerror),
        ("configResult", s_xl_eth_config_result),
        ("channelStatus", s_xl_eth_channel_status),
        ("syncPulse", s_xl_sync_pulse_ev),
        #(tag==XL_ETH_EVENT_TAG_LOSTEVENT) - Indication that one or more events have been lost
        ("lostEvent", s_xl_eth_lostevent),
    ]

class s_xl_eth_event(ctypes.Structure):
    _anonymous_ = ("tagData",)
    _fields_ = [
        #overall size of the complete event, depending on event type and piggybacked data
        ("size", ctypes.c_uint),
        #type of the event
        ("tag", XLethEventTag),
        ("channelIndex", ctypes.c_ushort),
        ("userHandle", ctypes.c_uint),
        ("flagsChip", ctypes.c_ushort),
        ("reserved", ctypes.c_ushort),
        ("reserved1", XLuint64),
        #timestamp which is synchronized by the driver
        ("timeStampSync", XLuint64),
        ("tagData", s_xl_eth_tag_data),
    ]
T_XL_ETH_EVENT = s_xl_eth_event

class s_xl_net_eth_dataframe_rx(ctypes.Structure):
    _anonymous_ = ("frameData",)
    _fields_ = [
        #Transmit duration of the Ethernet frame, in nanoseconds
        ("frameDuration", ctypes.c_uint),
        #Overall data length of <frameData>
        ("dataLen", ctypes.c_ushort),
        #currently reserved field - not used, ignore
        ("reserved1", ctypes.c_ubyte),
        #currently reserved field - not used, ignore
        ("reserved2", ctypes.c_ubyte),
        #see XL_ETH_NETWORK_RX_ERROR_xxx and XL_ETH_NETWORK_TX_ERROR_xxx
        ("errorFlags", ctypes.c_uint),
        #currently reserved field - not used, ignore
        ("reserved3", ctypes.c_uint),
        #Frame Check Sum
        ("fcs", ctypes.c_uint),
        #Destination MAC address
        ("destMAC", ctypes.c_ubyte*XL_ETH_MACADDR_OCTETS),
        #Source MAC address
        ("sourceMAC", ctypes.c_ubyte*XL_ETH_MACADDR_OCTETS),
        ("frameData", s_xl_eth_framedata),
    ]
T_XL_NET_ETH_DATAFRAME_RX =s_xl_net_eth_dataframe_rx
T_XL_NET_ETH_DATAFRAME_SIMULATION_TX_ACK = T_XL_NET_ETH_DATAFRAME_RX
T_XL_NET_ETH_DATAFRAME_MEASUREMENT_RX = T_XL_NET_ETH_DATAFRAME_RX
T_XL_NET_ETH_DATAFRAME_MEASUREMENT_TX = T_XL_NET_ETH_DATAFRAME_RX

class s_xl_net_eth_dataframe_rx_error(ctypes.Structure):
    _anonymous_ = ("frameData",)
    _fields_ = [
        #Transmit duration of the Ethernet frame, in nanoseconds
        ("frameDuration", ctypes.c_uint),
        #see XL_ETH_NETWORK_RX_ERROR_xxx and XL_ETH_NETWORK_TX_ERROR_xxx
        ("errorFlags", ctypes.c_uint),
        #Overall data length of <frameData>
        ("dataLen", ctypes.c_ushort),
        #currently reserved field - not used, ignore
        ("reserved1", ctypes.c_ubyte),
        #currently reserved field - not used, ignore
        ("reserved2", ctypes.c_ubyte),
        #currently reserved field - not used, ignore
        ("reserved3", ctypes.c_uint*2),
        #Frame Check Sum
        ("fcs", ctypes.c_uint),
        #Destination MAC address
        ("destMAC", ctypes.c_ubyte*XL_ETH_MACADDR_OCTETS),
        #Source MAC address
        ("sourceMAC", ctypes.c_ubyte*XL_ETH_MACADDR_OCTETS),
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
        ("rawData", ctypes.c_ubyte*XL_ETH_EVENT_SIZE_MAX),
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
        #overall size of the complete event
        ("size", ctypes.c_uint),
        #type of the event
        ("tag", XLethEventTag),
        #channel index
        ("channelIndex", ctypes.c_ushort),
        #application specific user handle
        ("userHandle", ctypes.c_uint),
        #flags
        ("flagsChip", ctypes.c_ushort),
        #currently reserved field - not used
        ("reserved", ctypes.c_ushort),
        #currently reserved field - not used
        ("reserved1", XLuint64),
        #synchronized TS by the driver
        ("timeStampSync", XLuint64),
        ("tagData", s_xl_eth_net_tag_data),
    ]
T_XL_NET_ETH_EVENT = s_xl_net_eth_event

class s_xl_eth_config(ctypes.Structure):
    _fields_ = [
        #(XL_ETH_MODE_SPEED_*)       Connection speed setting
        ("speed", ctypes.c_uint),
        #(XL_ETH_MODE_DUPLEX_*)      Duplex mode setting. Not relevant for BroadR-REACH mode, set to "nochange" or "auto".
        ("duplex", ctypes.c_uint),
        #(XL_ETH_MODE_CONNECTOR_*)   Connector to use
        ("connector", ctypes.c_uint),
        #(XL_ETH_MODE_PHY_*)         Physical interface to enable
        ("phy", ctypes.c_uint),
        #(XL_ETH_MODE_CLOCK_*)       Master or slave clock mode setting (1000Base-T/BroadR-REACH mode only).
        ("clockMode", ctypes.c_uint),
        #(XL_ETH_MODE_MDI_*)         Currently active MDI-mode
        ("mdiMode", ctypes.c_uint),
        #(XL_ETH_MODE_BR_PAIR_*)     Number of cable pairs to use (BroadR-REACH mode only).
        ("brPairs", ctypes.c_uint),
    ]
T_XL_ETH_CONFIG = s_xl_eth_config

class s_xl_eth_mac_address(ctypes.Structure):
    _fields_ = [
        ("address", ctypes.c_ubyte*XL_ETH_MACADDR_OCTETS),
    ]
T_XL_ETH_MAC_ADDRESS = s_xl_eth_mac_address

### MOST150 XL API ###

XL_MOST150_RX_EVENT_HEADER_SIZE = 32
XL_MOST150_MAX_EVENT_DATA_SIZE = 2048
MOST150_SYNC_ALLOC_INFO_SIZE = 372
XL_MOST150_CTRL_PAYLOAD_MAX_SIZE = 45
#maximum valid length (s. INIC User Manual)
XL_MOST150_ASYNC_PAYLOAD_MAX_SIZE = 1524
#maximum valid length (s. INIC User Manual)
XL_MOST150_ETHERNET_PAYLOAD_MAX_SIZE = 1506
#maximum length for sending a MDP
XL_MOST150_ASYNC_SEND_PAYLOAD_MAX_SIZE = 1600
#maximum length for sending a MEP
XL_MOST150_ETHERNET_SEND_PAYLOAD_MAX_SIZE = 1600

class XL_MOST150_FLAGS_CHIP(enum.IntEnum):
    #common VN2640 event
    XL_MOST150_VN2640 = 1
    #event was generated by INIC
    XL_MOST150_INIC = 2
    #event was generated by spy
    XL_MOST150_SPY = 4
    #queue overflow occured (some events are lost)
    XL_MOST150_QUEUE_OVERFLOW = 256

class XL_MOST150_SOURCE(enum.IntEnum):
    SPECIAL_NODE = 1
    SYNC_ALLOC_INFO = 4
    CTRL_SPY = 8
    ASYNC_SPY = 16
    ETH_SPY = 32
    SHUTDOWN_FLAG = 64
    SYSTEMLOCK_FLAG = 128
    LIGHTLOCK_SPY = 512
    LIGHTLOCK_INIC = 1024
    ECL_CHANGE = 2048
    LIGHT_STRESS = 4096
    LOCK_STRESS = 8192
    BUSLOAD_CTRL = 16384
    BUSLOAD_ASYNC = 32768
    CTRL_MLB = 65536
    ASYNC_MLB = 131072
    ETH_MLB = 262144
    TXACK_MLB = 524288
    STREAM_UNDERFLOW = 1048576
    STREAM_OVERFLOW = 2097152
    STREAM_RX_DATA = 4194304
    ECL_SEQUENCE = 8388608

class XL_MOST150_DEVICEMODE(enum.IntEnum):
    SLAVE = 0
    MASTER = 1
    STATIC_MASTER = 3
    RETIMED_BYPASS_SLAVE = 4
    RETIMED_BYPASS_MASTER = 5

class XL_MOST150_FREQUENCY(enum.IntEnum):
    FREQUENCY_44100 = 0
    FREQUENCY_48000 = 1
    FREQUENCY_ERROR = 2

class XL_MOST150_SPECIAL_NODE_INFO(enum.IntEnum):
    NA_CHANGED = 1
    GA_CHANGED = 2
    NPR_CHANGED = 4
    MPR_CHANGED = 8
    SBC_CHANGED = 16
    CTRL_RETRY_PARAMS_CHANGED = 96
    ASYNC_RETRY_PARAMS_CHANGED = 384
    MAC_ADDR_CHANGED = 512
    NPR_SPY_CHANGED = 1024
    MPR_SPY_CHANGED = 2048
    SBC_SPY_CHANGED = 4096
    INIC_NISTATE_CHANGED = 8192
    SPECIAL_NODE_MASK_CHANGED = 16383

class XL_MOST150_CTRL_RETRY(enum.IntEnum):
    #Time Unit: 16 MOST Frames
    RETRY_TIME_MIN = 3
    RETRY_TIME_MAX = 31
    SEND_ATTEMPT_MIN = 1
    SEND_ATTEMPT_MAX = 16
    #Time Unit: 1 MOST Frame
    ASYNC_RETRY_TIME_MIN = 0
    ASYNC_RETRY_TIME_MAX = 255
    #For both MDP and MEP
    ASYNC_SEND_ATTEMPT_MIN = 1
    ASYNC_SEND_ATTEMPT_MAX = 16

class XL_MOST150_INIC_NISTATE(enum.IntEnum):
    NET_OFF = 0
    NET_INIT = 1
    NET_RBD = 2
    NET_ON = 3
    NET_RBD_RESULT = 4

class XL_MOST150_TX(enum.IntEnum):
    OK = 1
    FAILED_FORMAT_ERROR = 2
    FAILED_NETWORK_OFF = 4
    FAILED_TIMEOUT = 5
    FAILED_WRONG_TARGET = 8
    OK_ONE_SUCCESS = 9
    FAILED_BAD_CRC = 12
    FAILED_RECEIVER_BUFFER_FULL = 14

class XL_MOST150_VALID(enum.IntEnum):
    DATALENANNOUNCED = 1
    SOURCEADDRESS = 2
    TARGETADDRESS = 4
    PACK = 8
    CACK = 16
    PINDEX = 32
    PRIORITY = 64
    CRC = 128
    CRCCALCULATED = 256
    MESSAGE = 2147483648

class XL_MOST150_SPY_PACK(enum.IntEnum):
    OK = 4
    BUFFER_FULL = 1
    #maybe spy before receiver
    NO_RESPONSE = 0

class XL_MOST150_SPY_CACK(enum.IntEnum):
    OK = 4
    CRC_ERROR = 1
    #maybe spy before receiver
    NO_RESPONSE = 0

#flag indicating a received MDP with length > XL_MOST150_ASYNC_PAYLOAD_MAX_SIZE
XL_MOST150_ASYNC_INVALID_RX_LENGTH    = 0x00008000
#flag indicating a received MEP with length > XL_MOST150_ETHERNET_PAYLOAD_MAX_SIZE
XL_MOST150_ETHERNET_INVALID_RX_LENGTH = 0x80000000

class XL_MOST150_LIGHT(enum.IntEnum):
    OFF = 0
    FORCE_ON = 1
    MODULATED = 2
    ON_UNLOCK = 3
    ON_LOCK = 4
    ON_STABLE_LOCK = 5
    ON_CRITICAL_UNLOCK = 6

class XL_MOST150_ERROR(enum.IntEnum):
    ASYNC_TX_ACK_HANDLE = 1
    ETH_TX_ACK_HANDLE = 2

class XL_MOST150_RX_BUFFER_TYPE(enum.IntEnum):
    CTRL = 1
    ASYNC = 2

class XL_MOST150_RX_BUFFER_MODE(enum.IntEnum):
    NORMAL_MODE = 0
    BLOCK_MODE = 1

class XL_MOST150_CTRL_SYNC_AUDIO(enum.IntEnum):
    DEVICE_LINE_IN = 0
    DEVICE_LINE_OUT = 1
    DEVICE_SPDIF_IN = 2
    DEVICE_SPDIF_OUT = 3
    DEVICE_ALLOC_BANDWIDTH = 4

class XL_MOST150_DEVICE_MODE(enum.IntEnum):
    OFF = 0
    ON = 1
    OFF_BYPASS_CLOSED = 2
    OFF_NOT_IN_NETON = 3
    OFF_NO_MORE_RESOURCES = 4
    OFF_NOT_ENOUGH_FREE_BW = 5
    OFF_DUE_TO_NET_OFF = 6
    OFF_DUE_TO_CFG_NOT_OK = 7
    OFF_COMMUNICATION_ERROR = 8
    OFF_STREAM_CONN_ERROR = 9
    OFF_CL_ALREADY_USED = 10
    CL_NOT_ALLOCATED = 255

#Maximum number of CL that can be allocated for device XL_MOST150_DEVICE_ALLOC_BANDWIDTH
XL_MOST150_ALLOC_BANDWIDTH_NUM_CL_MAX = 10
#special CL for xlMost150CtrlSyncAudio to de-allocate all CLs for device XL_MOST150_DEVICE_ALLOC_BANDWIDTH
XL_MOST150_CL_DEALLOC_ALL = 0x00000FFF

class XL_MOST150_VOLUME(enum.IntEnum):
    MIN = 0
    MAX = 255

class XL_MOST150_SYNC_MUTE_STATUS(enum.IntEnum):
    NO_MUTE = 0
    MUTE = 1

class XL_MOST150_LIGHT_POWER(enum.IntEnum):
    LIGHT_FULL = 100
    LIGHT_3DB = 50

class XL_MOST150_SYSTEMLOCK_FLAG(enum.IntEnum):
    NOT_SET = 0
    SET = 1

class XL_MOST150_SHUTDOWN_FLAG(enum.IntEnum):
    NOT_SET = 0
    SET = 1

class XL_MOST150_ECL_LINE(enum.IntEnum):
    LOW = 0
    HIGH = 1

class XL_MOST150_ECL_LINE_PULL_UP(enum.IntEnum):
    NOT_ACTIVE = 0
    ACTIVE = 1

class XL_MOST150_ECL_SEQ(enum.IntEnum):
    #Maximum number of states that can be configured for a sequence
    NUM_STATES_MAX = 200
    #Value range for duration of ECL sequence states
    #100 us
    DURATION_MIN = 1
    #65535 ms
    DURATION_MAX = 655350

class XL_MOST150_ECL_GLITCH_FILTER(enum.IntEnum):
    #Value range for setting the glitch filter
    #50 us
    MIN = 50
    #50 ms
    MAX = 50000

class XL_MOST150_MODE(enum.IntEnum):
    DEACTIVATED = 0
    ACTIVATED = 1

class XL_MOST150_BUSLOAD_TYPE(enum.IntEnum):
    DATA_PACKET = 0
    ETHERNET_PACKET = 1

class XL_MOST150_BUSLOAD_COUNTER_TYPE(enum.IntEnum):
    TYPE_NONE = 0
    TYPE_1_BYTE = 1
    TYPE_2_BYTE = 2
    TYPE_3_BYTE = 3
    TYPE_4_BYTE = 4

class XL_MOST150_SPDIF_MODE(enum.IntEnum):
    SLAVE = 0
    MASTER = 1

class XL_MOST150_SPDIF_ERR(enum.IntEnum):
    NO_ERROR = 0
    HW_COMMUNICATION = 1

class XL_MOST150_NW_STARTUP(enum.IntEnum):
    NO_ERROR = 0
    NO_ERRORINFO = 4294967295

class XL_MOST150_NW_SHUTDOWN(enum.IntEnum):
    NO_ERROR = 0
    NO_ERRORINFO = 4294967295

class XL_MOST150_STREAM(enum.IntEnum):
    #RX streaming: MOST -> PC
    RX_DATA = 0
    #TX streaming: PC -> MOST
    TX_DATA = 1

XL_MOST150_STREAM_INVALID_HANDLE = 0

class XL_MOST150_STREAM_STATE(enum.IntEnum):
    CLOSED = 1
    OPENED = 2
    STARTED = 3
    STOPPED = 4
    START_PENDING = 5
    STOP_PENDING = 6
    OPEN_PENDING = 7
    CLOSE_PENDING = 8
#TX Streaming: Maximum number of bytes that can be streamed per MOST frame
XL_MOST150_STREAM_TX_BYTES_PER_FRAME_MIN = 1
XL_MOST150_STREAM_TX_BYTES_PER_FRAME_MAX = 152
#RX Streaming: Maximum number of connection labels that can be streamed
XL_MOST150_STREAM_RX_NUM_CL_MAX = 8
#valid connection label range
XL_MOST150_STREAM_CL_MIN = 0x000C
XL_MOST150_STREAM_CL_MAX = 0x017F

class XL_MOST150_STREAM_STATE_ERROR(enum.IntEnum):
    NO_ERROR = 0
    NOT_ENOUGH_BW = 1
    NET_OFF = 2
    CONFIG_NOT_OK = 3
    CL_DISAPPEARED = 4
    INIC_SC_ERROR = 5
    DEVICEMODE_BYPASS = 6
    NISTATE_NOT_NETON = 7
    INIC_BUSY = 8
    CL_MISSING = 9
    NUM_BYTES_MISMATCH = 10
    INIC_COMMUNICATION = 11

class XL_MOST150_STREAM_TX_BUFFER(enum.IntEnum):
    ERROR_NO_ERROR = 0
    ERROR_NOT_ENOUGH_DATA = 1
    TX_FIFO_CLEARED = 2

class XL_MOST150_STREAM_RX_BUFFER(enum.IntEnum):
    ERROR_STOP_BY_APP = 1
    ERROR_MOST_SIGNAL_OFF = 2
    ERROR_UNLOCK = 3
    ERROR_CL_MISSING = 4
    ERROR_ALL_CL_MISSING = 5
    #overflow bit
    ERROR_OVERFLOW = 128

class XL_MOST150_STREAM_LATENCY(enum.IntEnum):
    VERY_LOW = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    VERY_HIGH = 4

class XL_MOST150_BYPASS_STRESS_TIME(enum.IntEnum):
    MIN = 10
    MAX = 65535

class XL_MOST150_BYPASS_STRESS(enum.IntEnum):
    STOPPED = 0
    STARTED = 1
    STOPPED_LIGHT_OFF = 2
    STOPPED_DEVICE_MODE = 3

class XL_MOST150_SSO_RESULT(enum.IntEnum):
    NO_RESULT = 0
    NO_FAULT_SAVED = 1
    SUDDEN_SIGNAL_OFF = 2
    CRITICAL_UNLOCK = 3

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
        #duration of message transmission in [ns]
        ("msgDuration", ctypes.c_uint),
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
        #number of bytes contained in ctrlData[]
        ("ctrlDataLen", ctypes.c_ushort),
        ("reserved2", ctypes.c_ubyte),
        #currently not used
        ("status", ctypes.c_uint),
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
        #duration of data packet transmission in [ns]
        ("pktDuration", ctypes.c_uint),
        ("asyncDataLenAnnounced", ctypes.c_ushort),
        ("targetAddress", ctypes.c_ushort),
        ("pAck", ctypes.c_ubyte),
        ("pIndex", ctypes.c_ubyte),
        ("sourceAddress", ctypes.c_ushort),
        ("crc", ctypes.c_uint),
        ("crcCalculated", ctypes.c_uint),
        ("cAck", ctypes.c_ubyte),
        #number of bytes contained in asyncData[]
        ("asyncDataLen", ctypes.c_ushort),
        ("reserved", ctypes.c_ubyte),
        #currently not used
        ("status", ctypes.c_uint),
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
        #duration of ethernet packet transmission in [ns]
        ("pktDuration", ctypes.c_uint),
        ("ethernetDataLenAnnounced", ctypes.c_ushort),
        ("targetAddress", ctypes.c_ubyte*6),
        ("pAck", ctypes.c_ubyte),
        ("sourceAddress", ctypes.c_ubyte*6),
        ("reserved0", ctypes.c_ubyte),
        ("crc", ctypes.c_uint),
        ("crcCalculated", ctypes.c_uint),
        ("cAck", ctypes.c_ubyte),
        #number of bytes contained in ethernetData[]
        ("ethernetDataLen", ctypes.c_ushort),
        ("reserved1", ctypes.c_ubyte),
        #currently not used
        ("status", ctypes.c_uint),
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
        ("allocTable", s_xl_most150_cl_info*MOST150_SYNC_ALLOC_INFO_SIZE),
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
        ("rawData", ctypes.c_ubyte*XL_MOST150_MAX_EVENT_DATA_SIZE),
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
        #see XL_MOST150_SPECIAL_NODE_MASK_CHANGED
        ("changeMask", ctypes.c_uint),
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
        #Prio: Currently fixed to 0x01 for Control Messages
        ("ctrlPrio", ctypes.c_uint),
        #1..16 attempts, set an invalid value to use the default value set by xlMost150SetCtrlRetryParameters
        ("ctrlSendAttempts", ctypes.c_uint),
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
        #Prio: Currently fixed to 0x00 for MDP /MEP
        ("priority", ctypes.c_uint),
        #1..16 attempts,set an invalid value to use the default value set by xlMost150SetAsyncRetryParameters
        ("asyncSendAttempts", ctypes.c_uint),
        #max. 1600 bytes
        ("length", ctypes.c_uint),
        ("targetAddress", ctypes.c_uint),
        ("asyncData", ctypes.c_ubyte*XL_MOST150_ASYNC_SEND_PAYLOAD_MAX_SIZE),
    ]
XLmost150AsyncTxMsg = s_xl_most150_async_tx_msg

class s_xl_most150_ethernet_tx_msg(ctypes.Structure):
    _fields_ = [
        #Prio: Currently fixed to 0x00 for MDP /MEP
        ("priority", ctypes.c_uint),
        #1..16 attempts, set an invalid value to use the default value set by xlMost150SetAsyncRetryParameters
        ("ethSendAttempts", ctypes.c_uint),
        ("sourceAddress", ctypes.c_ubyte*6),
        ("targetAddress", ctypes.c_ubyte*6),
        #max. 1600 bytes
        ("length", ctypes.c_uint),
        ("ethernetData", ctypes.c_ubyte*XL_MOST150_ETHERNET_SEND_PAYLOAD_MAX_SIZE),
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
        #counter can be only be set in the payload -> position 0 means first payload byte!
        ("counterPosition", ctypes.c_uint),
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
        ("connLabels", ctypes.c_uint*XL_MOST150_STREAM_RX_NUM_CL_MAX),
    ]
XLmost150StreamInfo = s_xl_most150_stream_get_info

### CAN / CAN-FD definitions ###

XL_CAN_MAX_DATA_LEN = 64
XL_CANFD_RX_EVENT_HEADER_SIZE = 32
XL_CANFD_MAX_EVENT_SIZE = 128

CANFD_GET_NUM_DATABYTES = lambda dlc, edl, rtr: (
    0 if rtr else\
    dlc if dlc < 9 else\
    8 if not edl else\
    12 if dlc == 9 else\
    16 if dlc == 10 else\
    20 if dlc == 11 else\
    24 if dlc == 12 else\
    32 if dlc == 13 else\
    48 if dlc == 14 else 64
)

class XL_CAN_TXMSG_FLAG(enum.IntFlag):
    #extended data length
    EDL = 1
    #baud rate switch
    BRS = 2
    #remote transmission request
    RTR = 16
    #high priority message - clears all send buffers - then transmits
    HIGHPRIO = 128
    #generate a wakeup message
    WAKEUP = 512

class XL_CAN_RXMSG_FLAG(enum.IntFlag):
    #extended data length
    EDL = 1
    #baud rate switch
    BRS = 2
    #error state indicator
    ESI = 4
    #remote transmission request
    RTR = 16
    #error frame (only posssible in XL_CAN_EV_TX_REQUEST/XL_CAN_EV_TX_REMOVED)
    EF = 512
    #Arbitration Lost(set if the receiving node tried to transmit a message but lost arbitration process)
    ARB_LOST = 1024
    #high voltage message on single wire CAN
    WAKEUP = 8192
    #1: transceiver error detected
    TE = 16384

class s_xl_can_tx_msg(ctypes.Structure):
    _fields_ = [
        ("canId", ctypes.c_uint),
        ("msgFlags", ctypes.c_uint),
        ("dlc", ctypes.c_ubyte),
        ("reserved", ctypes.c_ubyte*7),
        ("data", ctypes.c_ubyte*XL_CAN_MAX_DATA_LEN),
    ]
XL_CAN_TX_MSG = s_xl_can_tx_msg

class u_xl_can_event_tag_data(ctypes.Union):
    _fields_ = [
        ("canMsg", s_xl_can_tx_msg),
    ]

class s_xl_can_tx_event(ctypes.Structure):
    _anonymous_ = ("tagData",)
    _fields_ = [
        #type of the event
        ("tag", ctypes.c_ushort),
        ("transId", ctypes.c_ushort),
        #internal has to be 0
        ("channelIndex", ctypes.c_ubyte),
        #has to be zero
        ("reserved", ctypes.c_ubyte*3),
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
        ("data", ctypes.c_ubyte*XL_CAN_MAX_DATA_LEN),
    ]
XL_CAN_EV_RX_MSG = s_xl_can_rx_msg

class s_xl_can_tx_request(ctypes.Structure):
    _fields_ = [
        ("canId", ctypes.c_uint),
        ("msgFlags", ctypes.c_uint),
        ("dlc", ctypes.c_ubyte),
        ("reserved1", ctypes.c_ubyte),
        ("reserved", ctypes.c_ushort),
        ("data", ctypes.c_ubyte*XL_CAN_MAX_DATA_LEN),
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

class XL_CAN_ERRC(enum.IntEnum):
    BIT_ERROR = 1
    FORM_ERROR = 2
    STUFF_ERROR = 3
    OTHER_ERROR = 4
    CRC_ERROR = 5
    ACK_ERROR = 6
    NACK_ERROR = 7
    OVLD_ERROR = 8
    EXCPT_ERROR = 9

class s_xl_can_error(ctypes.Structure):
    _fields_ = [
        ("errorCode", ctypes.c_ubyte),
        ("reserved", ctypes.c_ubyte*95),
    ]
XL_CAN_EV_ERROR = s_xl_can_error

XL_CAN_QUEUE_OVERFLOW = 0x100

#0,5 MByte
RX_FIFO_CANFD_QUEUE_SIZE_MAX = 524288
#8 kByte
RX_FIFO_CANFD_QUEUE_SIZE_MIN = 8192

class u_xl_can_msg_tag_data(ctypes.Union):
    _fields_ = [
        ("raw", ctypes.c_ubyte*(XL_CANFD_MAX_EVENT_SIZE - XL_CANFD_RX_EVENT_HEADER_SIZE)),
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

### ARINC429 definitions ###

class XL_A429_MSG_CHANNEL_DIR(enum.IntEnum):
    TX = 1
    RX = 2

class XL_A429_MSG_BITRATE(enum.IntEnum):
    SLOW_MIN = 10500
    SLOW_MAX = 16000
    FAST_MIN = 90000
    FAST_MAX = 110000

XL_A429_MSG_GAP_4BIT = 32

class XL_A429_MSG_BITRATE_RX(enum.IntEnum):
    MIN = 10000
    MAX = 120000

class XL_A429_MSG_AUTO_BAUDRATE(enum.IntEnum):
    DISABLED = 0
    ENABLED = 1

class XL_A429_MSG_FLAG(enum.IntEnum):
    ON_REQUEST = 1
    CYCLIC = 2
    DELETE_CYCLIC = 4

XL_A429_MSG_CYCLE_MAX = 0x3FFFFFFF

class XL_A429_MSG_GAP(enum.IntEnum):
    #get minGap config from set channel params
    DEFAULT = 0
    MAX = 0x000FFFFF

class XL_A429_MSG_PARITY(enum.IntEnum):
    #get parity config from set channel params
    DEFAULT = 0
    #tx: get parity config from transmit data - rx: check disabled
    DISABLED = 1
    ODD = 2
    EVEN = 3

class XL_A429_EV_TX_MSG_CTRL(enum.IntEnum):
    ON_REQUEST = 0
    CYCLIC = 1

class XL_A429_EV_TX_ERROR(enum.IntEnum):
    ACCESS_DENIED = 0
    TRANSMISSION_ERROR = 1

class XL_A429_EV_RX_ERROR(enum.IntEnum):
    GAP_VIOLATION = 0
    PARITY = 1
    BITRATE_LOW = 2
    BITRATE_HIGH = 3
    FRAME_FORMAT = 4
    CODING_RZ = 5
    DUTY_FACTOR = 6
    AVG_BIT_LENGTH = 7

XL_A429_QUEUE_OVERFLOW = 0x100
#0,5 MByte
XL_A429_RX_FIFO_QUEUE_SIZE_MAX = 524288
#8 kByte
XL_A429_RX_FIFO_QUEUE_SIZE_MIN = 8192

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
        #0.00-100.00%
        ("busLoad", ctypes.c_uint),
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
        #overall size of the complete event
        ("size", ctypes.c_uint),
        #type of the event
        ("tag", ctypes.c_ushort),
        ("channelIndex", ctypes.c_ubyte),
        ("reserved", ctypes.c_ubyte),
        #(lower 12 bit available for CAN)
        ("userHandle", ctypes.c_uint),
        #queue overflow (upper 8bit)
        ("flagsChip", ctypes.c_ushort),
        ("reserved0", ctypes.c_ushort),
        #raw timestamp
        ("timeStamp", XLuint64),
        #timestamp which is synchronized by the driver
        ("timeStampSync", XLuint64),
        ("tagData", u_xl_a429_rx_tag_data),
    ]
XLa429RxEvent = s_xl_a429_rx_event

#anonymous structure for driver config interface
class XLIDriverConfig(ctypes.Structure):
    pass
#driver config handle is a pointer to anonymous structure
class _XLdriverConfig(ctypes.Structure):
    pass
XLdrvConfigHandle = ctypes.POINTER(_XLdriverConfig)

XL_INVALID_CONFIG_HANDLE = 0

class s_xl_channel_transceiver(ctypes.Structure):
    _fields_ = [
        #name of the transceiver, NULL terminated UTF-8 encoded string
        ("name", ctypes.c_char_p),
        ("type", ctypes.c_uint),
        #XL_CHANNEL_CONFIG_ERROR_XXX
        ("configError", ctypes.c_uint),
    ]

class s_xl_channel_drv_config_v1(ctypes.Structure):
    _fields_ = [
        #Index of the channel (same hardware) (0,1,...)
        ("hwChannel", ctypes.c_uint),
        #Global channel index (0,1,...) in the channel list, on remote devices this is the index of the local administrated channel
        ("channelIndex", ctypes.c_uint),
        #The index of the device in the device list
        ("deviceIndex", ctypes.c_uint),
        #version of interface with driver
        ("interfaceVersion", ctypes.c_uint),
        #The channel is on bus
        ("isOnBus", ctypes.c_uint),
        #capabilities which are supported (e.g CHANNEL_FLAG_XXX)
        ("channelCapabilities", XLuint64),
        ("channelCapabilities2", XLuint64),
        #what buses are supported
        ("channelBusCapabilities", XLuint64),
        #and which are possible to be activated
        ("channelBusActiveCapabilities", XLuint64),
        #currently selected bus
        ("connectedBusType", XLuint64),
        ("currentlyAvailableTimestamps", ctypes.c_uint),
        ("busParams", s_xl_bus_params),
        ("transceiver", s_xl_channel_transceiver),
    ]
s_xl_channel_drv_config_v1._fields_.append(
    ("remoteChannel", ctypes.POINTER(s_xl_channel_drv_config_v1))
)
XLchannelDrvConfigV1 = s_xl_channel_drv_config_v1
pXLchannelDrvConfigV1 = ctypes.POINTER(s_xl_channel_drv_config_v1)

class s_channel_drv_config_list_v1(ctypes.Structure):
    _fields_ = [
        ("item", ctypes.POINTER(s_xl_channel_drv_config_v1)),
        ("count", ctypes.c_uint),
    ]
XLchannelDrvConfigListV1 = s_channel_drv_config_list_v1
pXLchannelDrvConfigListV1 = ctypes.POINTER(s_channel_drv_config_list_v1)

class s_xl_device_drv_config_v1(ctypes.Structure):
    _fields_ = [
        #NULL terminated UTF-8 encoded string
        ("name", ctypes.c_char_p),
        #HWTYPE_xxxx
        ("hwType", ctypes.c_uint),
        #Index of the hardware (same type) (0,1,...)
        ("hwIndex", ctypes.c_uint),
        ("serialNumber", ctypes.c_uint),
        ("articleNumber", ctypes.c_uint),
        #version of the driver
        ("driverVersion", XLuint64),
        #XL_CONNECTION_INFO_XXX
        ("connectionInfo", ctypes.c_uint),
        #indicates a device of the remote driver config
        ("isRemoteDevice", ctypes.c_uint),
        #device channel list
        ("channelList", s_channel_drv_config_list_v1),
    ]
class s_xl_device_drv_config_remote_list(ctypes.Structure):
    _fields_ = [
        ("item", ctypes.POINTER(s_xl_device_drv_config_v1)),
        ("count", ctypes.c_uint),
    ]
#Insert structure
s_xl_device_drv_config_v1._fields_.insert(
    8, ("remoteDeviceList", s_xl_device_drv_config_remote_list)
)
XLdeviceDrvConfigV1 = s_xl_device_drv_config_v1
pXLdeviceDrvConfigV1 = ctypes.POINTER(s_xl_device_drv_config_v1)

class s_device_drv_config_list_v1(ctypes.Structure):
    _fields_ = [
        ("item", ctypes.POINTER(s_xl_device_drv_config_v1)),
        ("count", ctypes.c_uint),
    ]
XLdeviceDrvConfigListV1 = s_device_drv_config_list_v1
pXLdeviceDrvConfigListV1 = ctypes.POINTER(s_device_drv_config_list_v1)

class s_xl_virtual_port_drv_config_v1(ctypes.Structure):
    _fields_ = [
        #name of the virtual port, NULL terminated UTF-8 encoded string
        ("virtualPortName", ctypes.c_char_p),
        #the index of the network in the network list this vp belongs to
        ("networkIdx", ctypes.c_uint),
        #ID of the switch in the network - switches in different networks may have the same switch ID
        ("switchId", XLswitchId),
    ]
XLvirtualportDrvConfigV1 = s_xl_virtual_port_drv_config_v1
pXLvirtualportDrvConfigV1 = ctypes.POINTER(s_xl_virtual_port_drv_config_v1)

class s_virtual_port_drv_config_list_v1(ctypes.Structure):
    _fields_ = [
        ("item", ctypes.POINTER(s_xl_virtual_port_drv_config_v1)),
        ("count", ctypes.c_uint),
    ]
XLvirtualportDrvConfigListV1 = s_virtual_port_drv_config_list_v1
pXLvirtualportDrvConfigListV1 = ctypes.POINTER(s_virtual_port_drv_config_list_v1)

class s_xl_measurement_point_drv_config_v1(ctypes.Structure):
    _fields_ = [
        #name of the measurement point, NULL terminated UTF-8 encoded string
        ("measurementPointName", ctypes.c_char_p),
        #the index of the network in the network list this mp belongs to
        ("networkIdx", ctypes.c_uint),
        #ID of the switch in the network - switches in different networks may have the same switch ID
        ("switchId", XLswitchId),
        #the hardware channel the MP is connected to
        ("channel", s_xl_channel_drv_config_v1),
    ]
XLmeasurementpointDrvConfigV1 = s_xl_measurement_point_drv_config_v1
pXLmeasurementpointDrvConfigV1 = ctypes.POINTER(s_xl_measurement_point_drv_config_v1)

class s_xl_measurement_point_drv_config_list_v1(ctypes.Structure):
    _fields_ = [
        ("item", ctypes.POINTER(s_xl_measurement_point_drv_config_v1)),
        ("count", ctypes.c_uint),
    ]
XLmeasurementpointDrvConfigListV1 = s_xl_measurement_point_drv_config_list_v1
pXLmeasurementpointDrvConfigListV1 = ctypes.POINTER(s_xl_measurement_point_drv_config_list_v1)

class s_xl_switch_drv_config_v1(ctypes.Structure):
    _fields_ = [
        #name of the switch, NULL terminated UTF-8 encoded string
        ("switchName", ctypes.c_char_p),
        #ID of the switch in the network - switches in different networks may have the same switch ID
        ("switchId", XLswitchId),
        #the index of the network in the network list this switch belongs to
        ("networkIdx", ctypes.c_uint),
        #the device the switch resides on
        ("device", s_xl_device_drv_config_v1),
        #type of the switch "real", TAP or direct connection
        ("switchCapability", ctypes.c_uint),
        #Virtual Port list
        ("vpList", s_virtual_port_drv_config_list_v1),
        #Measurement Point list
        ("mpList", s_xl_measurement_point_drv_config_list_v1),
    ]
XLswitchDrvConfigV1 = s_xl_switch_drv_config_v1
pXLswitchDrvConfigV1 = ctypes.POINTER(s_xl_switch_drv_config_v1)

class s_switch_drv_config_list_v1(ctypes.Structure):
    _fields_ = [
        ("item", ctypes.POINTER(s_xl_switch_drv_config_v1)),
        ("count", ctypes.c_uint),
    ]
XLswitchDrvConfigListV1 = s_switch_drv_config_list_v1
pXLswitchDrvConfigListV1 = ctypes.POINTER(s_switch_drv_config_list_v1)

class e_xl_network_type(enum.IntEnum):
    ETH_NETWORK = 1
XLnetworkType = e_xl_network_type

class s_xl_network_drv_config_v1(ctypes.Structure):
    _fields_ = [
        #name of the network, NULL terminated UTF-8 encoded string
        ("networkName", ctypes.c_char_p),
        #network configuration error XL_NET_CFG_*
        ("statusCode", ctypes.c_uint),
        #NULL terminated UTF-8 encoded string that describes statusCode. NULL if no error string exists.
        ("statusErrorString", ctypes.c_char_p),
        #ETH_NETWORK - e_xl_network_type
        ("networkType", ctypes.c_int),
        ("switchList", s_switch_drv_config_list_v1),
    ]
XLnetworkDrvConfigV1 = s_xl_network_drv_config_v1
pXLnetworkDrvConfigV1 = ctypes.POINTER(s_xl_network_drv_config_v1)

class s_xl_network_drv_config_list_v1(ctypes.Structure):
    _fields_ = [
        ("item", ctypes.POINTER(s_xl_network_drv_config_v1)),
        ("count", ctypes.c_uint),
    ]
XLnetworkDrvConfigListV1 = s_xl_network_drv_config_list_v1
pXLnetworkDrvConfigListV1 = ctypes.POINTER(s_xl_network_drv_config_list_v1)

class s_xl_dll_drv_config_v1(ctypes.Structure):
    _fields_ = [
        #version of the loaded DLL instance
        ("dllVersion", XLuint64),
    ]
XLdllDrvConfigV1 = s_xl_dll_drv_config_v1
pXLdllDrvConfigV1 = ctypes.POINTER(s_xl_dll_drv_config_v1)

class e_xl_driver_config_version(enum.IntEnum):
    IDRIVER_CONFIG_VERSION_1 = 0x8001
XLIdriverConfigVersion = e_xl_driver_config_version


if sys.platform.startswith("win"):
    __func_ptr = ctypes.WINFUNCTYPE
else:
    __func_ptr = ctypes.CFUNCTYPE

TP_FCT_XLAPI_GET_CHANNEL_CONFIG_V1 = __func_ptr(
    XLstatus, XLdrvConfigHandle, pXLchannelDrvConfigListV1
)
TP_FCT_XLAPI_GET_DEVICE_CONFIG_V1 = __func_ptr(
    XLstatus, XLdrvConfigHandle, pXLdeviceDrvConfigListV1
)
TP_FCT_XLAPI_GET_VIRTUAL_PORT_CONFIG_V1 = __func_ptr(
    XLstatus, XLdrvConfigHandle, pXLvirtualportDrvConfigListV1
)
TP_FCT_XLAPI_GET_MEASUREMENT_POINT_CONFIG_V1 = __func_ptr(
    XLstatus, XLdrvConfigHandle, pXLmeasurementpointDrvConfigListV1
)
TP_FCT_XLAPI_GET_SWITCH_CONFIG_V1 = __func_ptr(
    XLstatus, XLdrvConfigHandle, pXLswitchDrvConfigListV1
)
TP_FCT_XLAPI_GET_NETWORK_CONFIG_V1 = __func_ptr(
    XLstatus, XLdrvConfigHandle, pXLnetworkDrvConfigListV1
)
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
XLapiIDriverConfigV1 = s_xlapi_driver_config_v1
pXLapiIDriverConfigV1 = ctypes.POINTER(s_xlapi_driver_config_v1)

### Load the vxlapi.dll (or vxlapi64.dll) ###
if sys.platform.startswith("win"):
    __LIB_NAME = "vxlapi64.dll" if sys.maxsize > 2**32 else "vxlapi.dll"
    __LOADER = ctypes.windll
else:
    raise NotImplementedError(
        "Unforunately the Vector XL Driver Library is only available on Windows."
    )
    __LOADER = ctypes.cdll

try:
    _vector_xlapi_dll_ = __LOADER.LoadLibrary(__LIB_NAME)
except Exception as exc:
    # We search in local folder for the .dll

    __LOCAL_LIB = "\\".join(__file__.split("\\")[0:-1] + [__LIB_NAME])
    print("Could not load vxlapi, trying to load local copy: {0}".format(__LOCAL_LIB))
    _vector_xlapi_dll_ = __LOADER.LoadLibrary(__LOCAL_LIB)

class VectorError(Exception):
    def __init__(self, error_code, error_text, fnc_name):
        super(VectorError, self).__init__(
            f"Error {error_code}: {fnc_name} failed ({error_text})"
        )
        # keep reference to args for pickling

        self._args = error_code, error_text, fnc_name

    def __reduce__(self):
        return type(self), self._args

def check_xl_status(res, fnc, args):
    if res > 0:
        raise VectorError(res, xlGetErrorString(res).decode(), fnc.__name__)
    return res


xlOpenDriver = _vector_xlapi_dll_.xlOpenDriver
xlOpenDriver.restype = XLstatus
xlOpenDriver.argtypes = []
xlOpenDriver.errcheck = check_xl_status

xlCloseDriver = _vector_xlapi_dll_.xlCloseDriver
xlCloseDriver.restype = XLstatus
xlCloseDriver.argtypes = []
xlCloseDriver.errcheck = check_xl_status

xlGetApplConfig = _vector_xlapi_dll_.xlGetApplConfig
xlGetApplConfig.restype = XLstatus
xlGetApplConfig.argtypes = [
    #appName
    ctypes.c_char_p,
    #appChannel
    ctypes.c_uint,
    #pHwType
    ctypes.POINTER(ctypes.c_uint),
    #pHwIndex
    ctypes.POINTER(ctypes.c_uint),
    #pHwChannel
    ctypes.POINTER(ctypes.c_uint),
    #busType
    ctypes.c_uint,
]
xlGetApplConfig.errcheck = check_xl_status

xlSetApplConfig = _vector_xlapi_dll_.xlSetApplConfig
xlSetApplConfig.restype = XLstatus
xlSetApplConfig.argtypes = [
    #appName
    ctypes.c_char_p,
    #appChannel
    ctypes.c_uint,
    #hwType
    ctypes.c_uint,
    #hwIndex
    ctypes.c_uint,
    #hwChannel
    ctypes.c_uint,
    #busType
    ctypes.c_uint,
]
xlSetApplConfig.errcheck = check_xl_status

xlGetDriverConfig = _vector_xlapi_dll_.xlGetDriverConfig
xlGetDriverConfig.restype = XLstatus
xlGetDriverConfig.argtypes = [
    #pDriverConfig
    pXLdriverConfig,
]
xlGetDriverConfig.errcheck = check_xl_status

xlCreateDriverConfig = _vector_xlapi_dll_.xlCreateDriverConfig
xlCreateDriverConfig.restype = XLstatus
xlCreateDriverConfig.argtypes = [
    #version
    ctypes.c_int,
    #pConfigInterface
    ctypes.POINTER(XLIDriverConfig),
]
xlCreateDriverConfig.errcheck = check_xl_status

xlDestroyDriverConfig = _vector_xlapi_dll_.xlDestroyDriverConfig
xlDestroyDriverConfig.restype = XLstatus
xlDestroyDriverConfig.argtypes = [
    #configHandle
    XLdrvConfigHandle,
]
xlDestroyDriverConfig.errcheck = check_xl_status

xlGetChannelIndex = _vector_xlapi_dll_.xlGetChannelIndex
xlGetChannelIndex.restype = ctypes.c_int
xlGetChannelIndex.argtypes = [
    #hwType
    ctypes.c_int,
    #hwIndex
    ctypes.c_int,
    #hwChannel
    ctypes.c_int,
]

xlGetChannelMask = _vector_xlapi_dll_.xlGetChannelMask
xlGetChannelMask.restype = XLaccess
xlGetChannelMask.argtypes = [
    #hwType
    ctypes.c_int,
    #hwIndex
    ctypes.c_int,
    #hwChannel
    ctypes.c_int,
]

xlOpenPort = _vector_xlapi_dll_.xlOpenPort
xlOpenPort.restype = XLstatus
xlOpenPort.argtypes = [
    #pPortHandle
    pXLportHandle,
    #userName
    ctypes.c_char_p,
    #accessMask
    XLaccess,
    #pPermissionMask
    ctypes.POINTER(XLaccess),
    #rxQueueSize
    ctypes.c_uint,
    #xlInterfaceVersion
    ctypes.c_uint,
    #busType
    ctypes.c_uint,
]
xlOpenPort.errcheck = check_xl_status

xlSetTimerRate = _vector_xlapi_dll_.xlSetTimerRate
xlSetTimerRate.restype = XLstatus
xlSetTimerRate.argtypes = [
    #portHandle
    XLportHandle,
    #timerRate
    XLulong,
]
xlSetTimerRate.errcheck = check_xl_status

xlSetTimerRateAndChannel = _vector_xlapi_dll_.xlSetTimerRateAndChannel
xlSetTimerRateAndChannel.restype = XLstatus
xlSetTimerRateAndChannel.argtypes = [
    #portHandle
    XLportHandle,
    #timerChannelMask
    ctypes.POINTER(XLaccess),
    #timerRate
    ctypes.POINTER(XLulong),
]
xlSetTimerRateAndChannel.errcheck = check_xl_status

xlResetClock = _vector_xlapi_dll_.xlResetClock
xlResetClock.restype = XLstatus
xlResetClock.argtypes = [
    #portHandle
    XLportHandle,
]
xlResetClock.errcheck = check_xl_status

xlSetNotification = _vector_xlapi_dll_.xlSetNotification
xlSetNotification.restype = XLstatus
xlSetNotification.argtypes = [
    #portHandle
    XLportHandle,
    #pHandle
    ctypes.POINTER(XLhandle),
    #queueLevel
    ctypes.c_int,
]
xlSetNotification.errcheck = check_xl_status

xlSetTimerBasedNotify = _vector_xlapi_dll_.xlSetTimerBasedNotify
xlSetTimerBasedNotify.restype = XLstatus
xlSetTimerBasedNotify.argtypes = [
    #portHandle
    XLportHandle,
    #pHandle
    ctypes.POINTER(XLhandle),
]
xlSetTimerBasedNotify.errcheck = check_xl_status

xlFlushReceiveQueue = _vector_xlapi_dll_.xlFlushReceiveQueue
xlFlushReceiveQueue.restype = XLstatus
xlFlushReceiveQueue.argtypes = [
    #portHandle
    XLportHandle,
]
xlFlushReceiveQueue.errcheck = check_xl_status

xlGetReceiveQueueLevel = _vector_xlapi_dll_.xlGetReceiveQueueLevel
xlGetReceiveQueueLevel.restype = XLstatus
xlGetReceiveQueueLevel.argtypes = [
    #portHandle
    XLportHandle,
    #level
    ctypes.POINTER(ctypes.c_int),
]
xlGetReceiveQueueLevel.errcheck = check_xl_status

xlActivateChannel = _vector_xlapi_dll_.xlActivateChannel
xlActivateChannel.restype = XLstatus
xlActivateChannel.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #busType
    ctypes.c_uint,
    #flags
    ctypes.c_uint,
]
xlActivateChannel.errcheck = check_xl_status

xlReceive = _vector_xlapi_dll_.xlReceive
xlReceive.restype = XLstatus
xlReceive.argtypes = [
    #portHandle
    XLportHandle,
    #pEventCount
    ctypes.POINTER(ctypes.c_uint),
    #pEvents
    ctypes.POINTER(XLevent),
]
xlReceive.errcheck = check_xl_status

xlGetErrorString = _vector_xlapi_dll_.xlGetErrorString
xlGetErrorString.restype = XLstringType
xlGetErrorString.argtypes = [
    #err
    XLstatus,
]

xlGetEventString = _vector_xlapi_dll_.xlGetEventString
xlGetEventString.restype = XLstringType
xlGetEventString.argtypes = [
    #pEv
    ctypes.POINTER(XLevent),
]

xlCanGetEventString = _vector_xlapi_dll_.xlCanGetEventString
xlCanGetEventString.restype = XLstringType
xlCanGetEventString.argtypes = [
    #pEv
    ctypes.POINTER(XLcanRxEvent),
]


xlOemContact = _vector_xlapi_dll_.xlOemContact
xlOemContact.restype = XLstatus
xlOemContact.argtypes = [
    #portHandle
    XLportHandle,
    #Channel
    XLulong,
    #context1
    XLuint64,
    #context2
    ctypes.POINTER(XLuint64),
]
xlOemContact.errcheck = check_xl_status

xlGetSyncTime = _vector_xlapi_dll_.xlGetSyncTime
xlGetSyncTime.restype = XLstatus
xlGetSyncTime.argtypes = [
    #portHandle
    XLportHandle,
    #pTime
    ctypes.POINTER(XLuint64),
]
xlGetSyncTime.errcheck = check_xl_status

xlGetChannelTime = _vector_xlapi_dll_.xlGetChannelTime
xlGetChannelTime.restype = XLstatus
xlGetChannelTime.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #pChannelTime
    ctypes.POINTER(XLuint64),
]
xlGetChannelTime.errcheck = check_xl_status

xlGenerateSyncPulse = _vector_xlapi_dll_.xlGenerateSyncPulse
xlGenerateSyncPulse.restype = XLstatus
xlGenerateSyncPulse.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
]
xlGenerateSyncPulse.errcheck = check_xl_status

xlPopupHwConfig = _vector_xlapi_dll_.xlPopupHwConfig
xlPopupHwConfig.restype = XLstatus
xlPopupHwConfig.argtypes = [
    #callSign
    ctypes.c_char_p,
    #waitForFinish
    ctypes.c_uint,
]
xlPopupHwConfig.errcheck = check_xl_status

xlDeactivateChannel = _vector_xlapi_dll_.xlDeactivateChannel
xlDeactivateChannel.restype = XLstatus
xlDeactivateChannel.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
]
xlDeactivateChannel.errcheck = check_xl_status

xlClosePort = _vector_xlapi_dll_.xlClosePort
xlClosePort.restype = XLstatus
xlClosePort.argtypes = [
    #portHandle
    XLportHandle,
]
xlClosePort.errcheck = check_xl_status

xlCanFlushTransmitQueue = _vector_xlapi_dll_.xlCanFlushTransmitQueue
xlCanFlushTransmitQueue.restype = XLstatus
xlCanFlushTransmitQueue.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
]
xlCanFlushTransmitQueue.errcheck = check_xl_status

xlCanSetChannelOutput = _vector_xlapi_dll_.xlCanSetChannelOutput
xlCanSetChannelOutput.restype = XLstatus
xlCanSetChannelOutput.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #mode
    ctypes.c_int,
]
xlCanSetChannelOutput.errcheck = check_xl_status

xlCanSetChannelMode = _vector_xlapi_dll_.xlCanSetChannelMode
xlCanSetChannelMode.restype = XLstatus
xlCanSetChannelMode.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #tx
    ctypes.c_int,
    #txrq
    ctypes.c_int,
]
xlCanSetChannelMode.errcheck = check_xl_status

xlCanSetReceiveMode = _vector_xlapi_dll_.xlCanSetReceiveMode
xlCanSetReceiveMode.restype = XLstatus
xlCanSetReceiveMode.argtypes = [
    #Port
    XLportHandle,
    #ErrorFrame
    ctypes.c_ubyte,
    #ChipState
    ctypes.c_ubyte,
]
xlCanSetReceiveMode.errcheck = check_xl_status

xlCanSetChannelTransceiver = _vector_xlapi_dll_.xlCanSetChannelTransceiver
xlCanSetChannelTransceiver.restype = XLstatus
xlCanSetChannelTransceiver.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #type
    ctypes.c_int,
    #lineMode
    ctypes.c_int,
    #resNet
    ctypes.c_int,
]
xlCanSetChannelTransceiver.errcheck = check_xl_status

xlCanSetChannelParams = _vector_xlapi_dll_.xlCanSetChannelParams
xlCanSetChannelParams.restype = XLstatus
xlCanSetChannelParams.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #pChipParams
    ctypes.POINTER(XLchipParams),
]
xlCanSetChannelParams.errcheck = check_xl_status

xlCanSetChannelParamsC200 = _vector_xlapi_dll_.xlCanSetChannelParamsC200
xlCanSetChannelParamsC200.restype = XLstatus
xlCanSetChannelParamsC200.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #btr0
    ctypes.c_ubyte,
    #btr1
    ctypes.c_ubyte,
]
xlCanSetChannelParamsC200.errcheck = check_xl_status

xlCanSetChannelBitrate = _vector_xlapi_dll_.xlCanSetChannelBitrate
xlCanSetChannelBitrate.restype = XLstatus
xlCanSetChannelBitrate.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #bitrate
    XLulong,
]
xlCanSetChannelBitrate.errcheck = check_xl_status

xlCanFdSetConfiguration = _vector_xlapi_dll_.xlCanFdSetConfiguration
xlCanFdSetConfiguration.restype = XLstatus
xlCanFdSetConfiguration.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #pCanFdConf
    ctypes.POINTER(XLcanFdConf),
]
xlCanFdSetConfiguration.errcheck = check_xl_status

xlCanReceive = _vector_xlapi_dll_.xlCanReceive
xlCanReceive.restype = XLstatus
xlCanReceive.argtypes = [
    #portHandle
    XLportHandle,
    #pXlCanRxEvt
    ctypes.POINTER(XLcanRxEvent),
]
xlCanReceive.errcheck = check_xl_status

xlCanTransmitEx = _vector_xlapi_dll_.xlCanTransmitEx
xlCanTransmitEx.restype = XLstatus
xlCanTransmitEx.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #msgCnt
    ctypes.c_uint,
    #pMsgCntSent
    ctypes.POINTER(ctypes.c_uint),
    #pXlCanTxEvt
    ctypes.POINTER(XLcanTxEvent),
]
xlCanTransmitEx.errcheck = check_xl_status

xlCanSetChannelAcceptance = _vector_xlapi_dll_.xlCanSetChannelAcceptance
xlCanSetChannelAcceptance.restype = XLstatus
xlCanSetChannelAcceptance.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #code
    XLulong,
    #mask
    XLulong,
    #idRange
    ctypes.c_uint,
]
xlCanSetChannelAcceptance.errcheck = check_xl_status

xlCanAddAcceptanceRange = _vector_xlapi_dll_.xlCanAddAcceptanceRange
xlCanAddAcceptanceRange.restype = XLstatus
xlCanAddAcceptanceRange.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #first_id
    XLulong,
    #last_id
    XLulong,
]
xlCanAddAcceptanceRange.errcheck = check_xl_status

xlCanRemoveAcceptanceRange = _vector_xlapi_dll_.xlCanRemoveAcceptanceRange
xlCanRemoveAcceptanceRange.restype = XLstatus
xlCanRemoveAcceptanceRange.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #first_id
    XLulong,
    #last_id
    XLulong,
]
xlCanRemoveAcceptanceRange.errcheck = check_xl_status

xlCanResetAcceptance = _vector_xlapi_dll_.xlCanResetAcceptance
xlCanResetAcceptance.restype = XLstatus
xlCanResetAcceptance.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #idRange
    ctypes.c_uint,
]
xlCanResetAcceptance.errcheck = check_xl_status

xlCanRequestChipState = _vector_xlapi_dll_.xlCanRequestChipState
xlCanRequestChipState.restype = XLstatus
xlCanRequestChipState.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
]
xlCanRequestChipState.errcheck = check_xl_status

xlCanTransmit = _vector_xlapi_dll_.xlCanTransmit
xlCanTransmit.restype = XLstatus
xlCanTransmit.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #pEventCount
    ctypes.POINTER(ctypes.c_uint),
    #pEvents
    ctypes.c_void_p,
]
xlCanTransmit.errcheck = check_xl_status

xlSetGlobalTimeSync = _vector_xlapi_dll_.xlSetGlobalTimeSync
xlSetGlobalTimeSync.restype = XLstatus
xlSetGlobalTimeSync.argtypes = [
    #newValue
    XLulong,
    #previousValue
    ctypes.POINTER(XLulong),
]
xlSetGlobalTimeSync.errcheck = check_xl_status

xlCheckLicense = _vector_xlapi_dll_.xlCheckLicense
xlCheckLicense.restype = XLstatus
xlCheckLicense.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #protectionCode
    XLulong,
]
xlCheckLicense.errcheck = check_xl_status

xlGetLicenseInfo = _vector_xlapi_dll_.xlGetLicenseInfo
xlGetLicenseInfo.restype = XLstatus
xlGetLicenseInfo.argtypes = [
    #channelMask
    XLaccess,
    #pLicInfoArray
    ctypes.POINTER(XLlicenseInfo),
    #licInfoArraySize
    ctypes.c_uint,
]
xlGetLicenseInfo.errcheck = check_xl_status

xlLinSetChannelParams = _vector_xlapi_dll_.xlLinSetChannelParams
xlLinSetChannelParams.restype = XLstatus
xlLinSetChannelParams.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #vStatPar
    XLlinStatPar,
]
xlLinSetChannelParams.errcheck = check_xl_status

xlLinSetDLC = _vector_xlapi_dll_.xlLinSetDLC
xlLinSetDLC.restype = XLstatus
xlLinSetDLC.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #dlc[64]
    ctypes.c_ubyte*64,
]
xlLinSetDLC.errcheck = check_xl_status

xlLinSetSlave = _vector_xlapi_dll_.xlLinSetSlave
xlLinSetSlave.restype = XLstatus
xlLinSetSlave.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #linId
    ctypes.c_ubyte,
    #data[8]
    ctypes.c_ubyte*8,
    #dlc
    ctypes.c_ubyte,
    #checksum
    ctypes.c_ushort,
]
xlLinSetSlave.errcheck = check_xl_status

xlLinSendRequest = _vector_xlapi_dll_.xlLinSendRequest
xlLinSendRequest.restype = XLstatus
xlLinSendRequest.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #linId
    ctypes.c_ubyte,
    #flags
    ctypes.c_uint,
]
xlLinSendRequest.errcheck = check_xl_status

xlLinSetSleepMode = _vector_xlapi_dll_.xlLinSetSleepMode
xlLinSetSleepMode.restype = XLstatus
xlLinSetSleepMode.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #flags
    ctypes.c_uint,
    #linId
    ctypes.c_ubyte,
]
xlLinSetSleepMode.errcheck = check_xl_status

xlLinWakeUp = _vector_xlapi_dll_.xlLinWakeUp
xlLinWakeUp.restype = XLstatus
xlLinWakeUp.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
]
xlLinWakeUp.errcheck = check_xl_status

xlLinSetChecksum = _vector_xlapi_dll_.xlLinSetChecksum
xlLinSetChecksum.restype = XLstatus
xlLinSetChecksum.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #checksum[60]
    ctypes.c_ubyte*60,
]
xlLinSetChecksum.errcheck = check_xl_status

xlLinSwitchSlave = _vector_xlapi_dll_.xlLinSwitchSlave
xlLinSwitchSlave.restype = XLstatus
xlLinSwitchSlave.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #linID
    ctypes.c_ubyte,
    #mode
    ctypes.c_ubyte,
]
xlLinSwitchSlave.errcheck = check_xl_status

xlDAIOSetPWMOutput = _vector_xlapi_dll_.xlDAIOSetPWMOutput
xlDAIOSetPWMOutput.restype = XLstatus
xlDAIOSetPWMOutput.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #frequency
    ctypes.c_uint,
    #value
    ctypes.c_uint,
]
xlDAIOSetPWMOutput.errcheck = check_xl_status

xlDAIOSetDigitalOutput = _vector_xlapi_dll_.xlDAIOSetDigitalOutput
xlDAIOSetDigitalOutput.restype = XLstatus
xlDAIOSetDigitalOutput.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #outputMask
    ctypes.c_uint,
    #valuePattern
    ctypes.c_uint,
]
xlDAIOSetDigitalOutput.errcheck = check_xl_status

xlDAIOSetAnalogOutput = _vector_xlapi_dll_.xlDAIOSetAnalogOutput
xlDAIOSetAnalogOutput.restype = XLstatus
xlDAIOSetAnalogOutput.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #analogLine1
    ctypes.c_uint,
    #analogLine2
    ctypes.c_uint,
    #analogLine3
    ctypes.c_uint,
    #analogLine4
    ctypes.c_uint,
]
xlDAIOSetAnalogOutput.errcheck = check_xl_status

xlDAIORequestMeasurement = _vector_xlapi_dll_.xlDAIORequestMeasurement
xlDAIORequestMeasurement.restype = XLstatus
xlDAIORequestMeasurement.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
]
xlDAIORequestMeasurement.errcheck = check_xl_status

xlDAIOSetDigitalParameters = _vector_xlapi_dll_.xlDAIOSetDigitalParameters
xlDAIOSetDigitalParameters.restype = XLstatus
xlDAIOSetDigitalParameters.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #inputMask
    ctypes.c_uint,
    #outputMask
    ctypes.c_uint,
]
xlDAIOSetDigitalParameters.errcheck = check_xl_status

xlDAIOSetAnalogParameters = _vector_xlapi_dll_.xlDAIOSetAnalogParameters
xlDAIOSetAnalogParameters.restype = XLstatus
xlDAIOSetAnalogParameters.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #inputMask
    ctypes.c_uint,
    #outputMask
    ctypes.c_uint,
    #highRangeMask
    ctypes.c_uint,
]
xlDAIOSetAnalogParameters.errcheck = check_xl_status

xlDAIOSetAnalogTrigger = _vector_xlapi_dll_.xlDAIOSetAnalogTrigger
xlDAIOSetAnalogTrigger.restype = XLstatus
xlDAIOSetAnalogTrigger.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #triggerMask
    ctypes.c_uint,
    #triggerLevel
    ctypes.c_uint,
    #triggerEventMode
    ctypes.c_uint,
]
xlDAIOSetAnalogTrigger.errcheck = check_xl_status

xlDAIOSetMeasurementFrequency = _vector_xlapi_dll_.xlDAIOSetMeasurementFrequency
xlDAIOSetMeasurementFrequency.restype = XLstatus
xlDAIOSetMeasurementFrequency.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #measurementInterval
    ctypes.c_uint,
]
xlDAIOSetMeasurementFrequency.errcheck = check_xl_status

xlDAIOSetDigitalTrigger = _vector_xlapi_dll_.xlDAIOSetDigitalTrigger
xlDAIOSetDigitalTrigger.restype = XLstatus
xlDAIOSetDigitalTrigger.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #triggerMask
    ctypes.c_uint,
]
xlDAIOSetDigitalTrigger.errcheck = check_xl_status

xlKlineTransmit = _vector_xlapi_dll_.xlKlineTransmit
xlKlineTransmit.restype = XLstatus
xlKlineTransmit.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #length
    ctypes.c_uint,
    #data
    ctypes.POINTER(ctypes.c_ubyte),
]
xlKlineTransmit.errcheck = check_xl_status

xlKlineSetUartParams = _vector_xlapi_dll_.xlKlineSetUartParams
xlKlineSetUartParams.restype = XLstatus
xlKlineSetUartParams.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #pxlKlineUartParams
    ctypes.POINTER(XLklineUartParameter),
]
xlKlineSetUartParams.errcheck = check_xl_status

xlKlineSwitchHighspeedMode = _vector_xlapi_dll_.xlKlineSwitchHighspeedMode
xlKlineSwitchHighspeedMode.restype = XLstatus
xlKlineSwitchHighspeedMode.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #trxMode
    ctypes.c_uint,
]
xlKlineSwitchHighspeedMode.errcheck = check_xl_status

xlKlineSwitchTesterResistor = _vector_xlapi_dll_.xlKlineSwitchTesterResistor
xlKlineSwitchTesterResistor.restype = XLstatus
xlKlineSwitchTesterResistor.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #testerR
    ctypes.c_uint,
]
xlKlineSwitchTesterResistor.errcheck = check_xl_status

xlKlineSetBaudrate = _vector_xlapi_dll_.xlKlineSetBaudrate
xlKlineSetBaudrate.restype = XLstatus
xlKlineSetBaudrate.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #baudrate
    ctypes.c_uint,
]
xlKlineSetBaudrate.errcheck = check_xl_status

xlKlineFastInitTester = _vector_xlapi_dll_.xlKlineFastInitTester
xlKlineFastInitTester.restype = XLstatus
xlKlineFastInitTester.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #length
    ctypes.c_uint,
    #data
    ctypes.POINTER(ctypes.c_ubyte),
    #pxlKlineInitTester
    ctypes.POINTER(XLklineInitTester),
]
xlKlineFastInitTester.errcheck = check_xl_status

xlKlineInit5BdTester = _vector_xlapi_dll_.xlKlineInit5BdTester
xlKlineInit5BdTester.restype = XLstatus
xlKlineInit5BdTester.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #pxlKline5BdTester
    ctypes.POINTER(XLkline5BdTester),
]
xlKlineInit5BdTester.errcheck = check_xl_status

xlKlineInit5BdEcu = _vector_xlapi_dll_.xlKlineInit5BdEcu
xlKlineInit5BdEcu.restype = XLstatus
xlKlineInit5BdEcu.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #pxlKline5BdEcu
    ctypes.POINTER(XLkline5BdEcu),
]
xlKlineInit5BdEcu.errcheck = check_xl_status

xlKlineSetCommunicationTimingTester = _vector_xlapi_dll_.xlKlineSetCommunicationTimingTester
xlKlineSetCommunicationTimingTester.restype = XLstatus
xlKlineSetCommunicationTimingTester.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #pxlKlineSetComTester
    ctypes.POINTER(XLklineSetComTester),
]
xlKlineSetCommunicationTimingTester.errcheck = check_xl_status

xlKlineSetCommunicationTimingEcu = _vector_xlapi_dll_.xlKlineSetCommunicationTimingEcu
xlKlineSetCommunicationTimingEcu.restype = XLstatus
xlKlineSetCommunicationTimingEcu.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #pxlKlineSetComEcu
    ctypes.POINTER(XLklineSetComEcu),
]
xlKlineSetCommunicationTimingEcu.errcheck = check_xl_status

xlMostReceive = _vector_xlapi_dll_.xlMostReceive
xlMostReceive.restype = XLstatus
xlMostReceive.argtypes = [
    #portHandle
    XLportHandle,
#  XLaccess, #accessMask -> is not in header (possible bug)
    #pEventBuffer
    ctypes.POINTER(XLmostEvent),
]
xlMostReceive.errcheck = check_xl_status

xlMostSwitchEventSources = _vector_xlapi_dll_.xlMostSwitchEventSources
xlMostSwitchEventSources.restype = XLstatus
xlMostSwitchEventSources.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #sourceMask
    ctypes.c_ushort,
]
xlMostSwitchEventSources.errcheck = check_xl_status

xlMostSetAllBypass = _vector_xlapi_dll_.xlMostSetAllBypass
xlMostSetAllBypass.restype = XLstatus
xlMostSetAllBypass.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #bypassMode
    ctypes.c_ubyte,
]
xlMostSetAllBypass.errcheck = check_xl_status

xlMostGetAllBypass = _vector_xlapi_dll_.xlMostGetAllBypass
xlMostGetAllBypass.restype = XLstatus
xlMostGetAllBypass.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
]
xlMostGetAllBypass.errcheck = check_xl_status

xlMostSetTimingMode = _vector_xlapi_dll_.xlMostSetTimingMode
xlMostSetTimingMode.restype = XLstatus
xlMostSetTimingMode.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #timingMode
    ctypes.c_ubyte,
]
xlMostSetTimingMode.errcheck = check_xl_status

xlMostGetTimingMode = _vector_xlapi_dll_.xlMostGetTimingMode
xlMostGetTimingMode.restype = XLstatus
xlMostGetTimingMode.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
]
xlMostGetTimingMode.errcheck = check_xl_status

xlMostSetFrequency = _vector_xlapi_dll_.xlMostSetFrequency
xlMostSetFrequency.restype = XLstatus
xlMostSetFrequency.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #frequency
    ctypes.c_ushort,
]
xlMostSetFrequency.errcheck = check_xl_status

xlMostGetFrequency = _vector_xlapi_dll_.xlMostGetFrequency
xlMostGetFrequency.restype = XLstatus
xlMostGetFrequency.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
]
xlMostGetFrequency.errcheck = check_xl_status

xlMostWriteRegister = _vector_xlapi_dll_.xlMostWriteRegister
xlMostWriteRegister.restype = XLstatus
xlMostWriteRegister.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #adr
    ctypes.c_ushort,
    #numBytes
    ctypes.c_ubyte,
    #data[16]
    ctypes.c_ubyte*16,
]
xlMostWriteRegister.errcheck = check_xl_status

xlMostReadRegister = _vector_xlapi_dll_.xlMostReadRegister
xlMostReadRegister.restype = XLstatus
xlMostReadRegister.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #adr
    ctypes.c_ushort,
    #numBytes
    ctypes.c_ubyte,
]
xlMostReadRegister.errcheck = check_xl_status

xlMostWriteRegisterBit = _vector_xlapi_dll_.xlMostWriteRegisterBit
xlMostWriteRegisterBit.restype = XLstatus
xlMostWriteRegisterBit.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #adr
    ctypes.c_ushort,
    #mask
    ctypes.c_ubyte,
    #value
    ctypes.c_ubyte,
]
xlMostWriteRegisterBit.errcheck = check_xl_status

xlMostCtrlTransmit = _vector_xlapi_dll_.xlMostCtrlTransmit
xlMostCtrlTransmit.restype = XLstatus
xlMostCtrlTransmit.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #pCtrlMsg
    ctypes.POINTER(XLmostCtrlMsg),
]
xlMostCtrlTransmit.errcheck = check_xl_status

xlMostAsyncTransmit = _vector_xlapi_dll_.xlMostAsyncTransmit
xlMostAsyncTransmit.restype = XLstatus
xlMostAsyncTransmit.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #pAsyncMsg
    ctypes.POINTER(XLmostAsyncMsg),
]
xlMostAsyncTransmit.errcheck = check_xl_status

xlMostSyncGetAllocTable = _vector_xlapi_dll_.xlMostSyncGetAllocTable
xlMostSyncGetAllocTable.restype = XLstatus
xlMostSyncGetAllocTable.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
]
xlMostSyncGetAllocTable.errcheck = check_xl_status

xlMostCtrlSyncAudio = _vector_xlapi_dll_.xlMostCtrlSyncAudio
xlMostCtrlSyncAudio.restype = XLstatus
xlMostCtrlSyncAudio.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #channel[4]
    ctypes.c_uint*4,
    #device
    ctypes.c_uint,
    #mode
    ctypes.c_uint,
]
xlMostCtrlSyncAudio.errcheck = check_xl_status

xlMostCtrlSyncAudioEx = _vector_xlapi_dll_.xlMostCtrlSyncAudioEx
xlMostCtrlSyncAudioEx.restype = XLstatus
xlMostCtrlSyncAudioEx.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #channel[16]
    ctypes.c_uint*16,
    #device
    ctypes.c_uint,
    #mode
    ctypes.c_uint,
]
xlMostCtrlSyncAudioEx.errcheck = check_xl_status

xlMostSyncVolume = _vector_xlapi_dll_.xlMostSyncVolume
xlMostSyncVolume.restype = XLstatus
xlMostSyncVolume.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #device
    ctypes.c_uint,
    #volume
    ctypes.c_ubyte,
]
xlMostSyncVolume.errcheck = check_xl_status

xlMostSyncMute = _vector_xlapi_dll_.xlMostSyncMute
xlMostSyncMute.restype = XLstatus
xlMostSyncMute.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #device
    ctypes.c_uint,
    #mute
    ctypes.c_ubyte,
]
xlMostSyncMute.errcheck = check_xl_status

xlMostSyncGetVolumeStatus = _vector_xlapi_dll_.xlMostSyncGetVolumeStatus
xlMostSyncGetVolumeStatus.restype = XLstatus
xlMostSyncGetVolumeStatus.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #device
    ctypes.c_uint,
]
xlMostSyncGetVolumeStatus.errcheck = check_xl_status

xlMostSyncGetMuteStatus = _vector_xlapi_dll_.xlMostSyncGetMuteStatus
xlMostSyncGetMuteStatus.restype = XLstatus
xlMostSyncGetMuteStatus.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #device
    ctypes.c_uint,
]
xlMostSyncGetMuteStatus.errcheck = check_xl_status

xlMostGetRxLight = _vector_xlapi_dll_.xlMostGetRxLight
xlMostGetRxLight.restype = XLstatus
xlMostGetRxLight.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
]
xlMostGetRxLight.errcheck = check_xl_status

xlMostSetTxLight = _vector_xlapi_dll_.xlMostSetTxLight
xlMostSetTxLight.restype = XLstatus
xlMostSetTxLight.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #txLight
    ctypes.c_ubyte,
]
xlMostSetTxLight.errcheck = check_xl_status

xlMostGetTxLight = _vector_xlapi_dll_.xlMostGetTxLight
xlMostGetTxLight.restype = XLstatus
xlMostGetTxLight.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
]
xlMostGetTxLight.errcheck = check_xl_status

xlMostSetLightPower = _vector_xlapi_dll_.xlMostSetLightPower
xlMostSetLightPower.restype = XLstatus
xlMostSetLightPower.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #attenuation
    ctypes.c_ubyte,
]
xlMostSetLightPower.errcheck = check_xl_status

xlMostGetLockStatus = _vector_xlapi_dll_.xlMostGetLockStatus
xlMostGetLockStatus.restype = XLstatus
xlMostGetLockStatus.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
]
xlMostGetLockStatus.errcheck = check_xl_status

xlMostGenerateLightError = _vector_xlapi_dll_.xlMostGenerateLightError
xlMostGenerateLightError.restype = XLstatus
xlMostGenerateLightError.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #lightOffTime
    XLulong,
    #lightOnTime
    XLulong,
    #repeat
    ctypes.c_ushort,
]
xlMostGenerateLightError.errcheck = check_xl_status

xlMostGenerateLockError = _vector_xlapi_dll_.xlMostGenerateLockError
xlMostGenerateLockError.restype = XLstatus
xlMostGenerateLockError.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #unmodTime
    XLulong,
    #modTime
    XLulong,
    #repeat
    ctypes.c_ushort,
]
xlMostGenerateLockError.errcheck = check_xl_status

xlMostCtrlRxBuffer = _vector_xlapi_dll_.xlMostCtrlRxBuffer
xlMostCtrlRxBuffer.restype = XLstatus
xlMostCtrlRxBuffer.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #bufferMode
    ctypes.c_ushort,
]
xlMostCtrlRxBuffer.errcheck = check_xl_status

xlMostTwinklePowerLed = _vector_xlapi_dll_.xlMostTwinklePowerLed
xlMostTwinklePowerLed.restype = XLstatus
xlMostTwinklePowerLed.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
]
xlMostTwinklePowerLed.errcheck = check_xl_status

xlMostCtrlConfigureBusload = _vector_xlapi_dll_.xlMostCtrlConfigureBusload
xlMostCtrlConfigureBusload.restype = XLstatus
xlMostCtrlConfigureBusload.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #pCtrlBusloadConfiguration
    ctypes.POINTER(XLmostCtrlBusloadConfiguration),
]
xlMostCtrlConfigureBusload.errcheck = check_xl_status

xlMostCtrlGenerateBusload = _vector_xlapi_dll_.xlMostCtrlGenerateBusload
xlMostCtrlGenerateBusload.restype = XLstatus
xlMostCtrlGenerateBusload.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #numberCtrlFrames
    XLulong,
]
xlMostCtrlGenerateBusload.errcheck = check_xl_status

xlMostAsyncConfigureBusload = _vector_xlapi_dll_.xlMostAsyncConfigureBusload
xlMostAsyncConfigureBusload.restype = XLstatus
xlMostAsyncConfigureBusload.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #pAsyncBusloadConfiguration
    ctypes.POINTER(XLmostAsyncBusloadConfiguration),
]
xlMostAsyncConfigureBusload.errcheck = check_xl_status

xlMostAsyncGenerateBusload = _vector_xlapi_dll_.xlMostAsyncGenerateBusload
xlMostAsyncGenerateBusload.restype = XLstatus
xlMostAsyncGenerateBusload.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #numberAsyncFrames
    XLulong,
]
xlMostAsyncGenerateBusload.errcheck = check_xl_status

xlMostStreamOpen = _vector_xlapi_dll_.xlMostStreamOpen
xlMostStreamOpen.restype = XLstatus
xlMostStreamOpen.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #pStreamOpen
    ctypes.POINTER(XLmostStreamOpen),
]
xlMostStreamOpen.errcheck = check_xl_status

xlMostStreamClose = _vector_xlapi_dll_.xlMostStreamClose
xlMostStreamClose.restype = XLstatus
xlMostStreamClose.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #streamHandle
    ctypes.c_uint,
]
xlMostStreamClose.errcheck = check_xl_status

xlMostStreamStart = _vector_xlapi_dll_.xlMostStreamStart
xlMostStreamStart.restype = XLstatus
xlMostStreamStart.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #streamHandle
    ctypes.c_uint,
    #syncChannels[60]
    ctypes.c_ubyte*60,
]
xlMostStreamStart.errcheck = check_xl_status

xlMostStreamStop = _vector_xlapi_dll_.xlMostStreamStop
xlMostStreamStop.restype = XLstatus
xlMostStreamStop.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #streamHandle
    ctypes.c_uint,
]
xlMostStreamStop.errcheck = check_xl_status

xlMostStreamBufferAllocate = _vector_xlapi_dll_.xlMostStreamBufferAllocate
xlMostStreamBufferAllocate.restype = XLstatus
xlMostStreamBufferAllocate.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #streamHandle
    ctypes.c_uint,
    #ppBuffer
    ctypes.POINTER(ctypes.POINTER(ctypes.c_ubyte)),
    #pBufferSize
    ctypes.POINTER(ctypes.c_uint),
]
xlMostStreamBufferAllocate.errcheck = check_xl_status

xlMostStreamBufferDeallocateAll = _vector_xlapi_dll_.xlMostStreamBufferDeallocateAll
xlMostStreamBufferDeallocateAll.restype = XLstatus
xlMostStreamBufferDeallocateAll.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #streamHandle
    ctypes.c_uint,
]
xlMostStreamBufferDeallocateAll.errcheck = check_xl_status

xlMostStreamBufferSetNext = _vector_xlapi_dll_.xlMostStreamBufferSetNext
xlMostStreamBufferSetNext.restype = XLstatus
xlMostStreamBufferSetNext.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #streamHandle
    ctypes.c_uint,
    #pBuffer
    ctypes.POINTER(ctypes.c_ubyte),
    #filledBytes
    ctypes.c_uint,
]
xlMostStreamBufferSetNext.errcheck = check_xl_status

xlMostStreamGetInfo = _vector_xlapi_dll_.xlMostStreamGetInfo
xlMostStreamGetInfo.restype = XLstatus
xlMostStreamGetInfo.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #pStreamInfo
    ctypes.POINTER(XLmostStreamInfo),
]
xlMostStreamGetInfo.errcheck = check_xl_status

xlMostStreamBufferClearAll = _vector_xlapi_dll_.xlMostStreamBufferClearAll
xlMostStreamBufferClearAll.restype = XLstatus
xlMostStreamBufferClearAll.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #streamHandle
    ctypes.c_uint,
]
xlMostStreamBufferClearAll.errcheck = check_xl_status

xlFrSetConfiguration = _vector_xlapi_dll_.xlFrSetConfiguration
xlFrSetConfiguration.restype = XLstatus
xlFrSetConfiguration.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #pxlClusterConfig
    ctypes.POINTER(XLfrClusterConfig),
]
xlFrSetConfiguration.errcheck = check_xl_status

xlFrGetChannelConfiguration = _vector_xlapi_dll_.xlFrGetChannelConfiguration
xlFrGetChannelConfiguration.restype = XLstatus
xlFrGetChannelConfiguration.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #pxlFrChannelConfig
    ctypes.POINTER(XLfrChannelConfig),
]
xlFrGetChannelConfiguration.errcheck = check_xl_status

xlFrSetMode = _vector_xlapi_dll_.xlFrSetMode
xlFrSetMode.restype = XLstatus
xlFrSetMode.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #pxlFrMode
    ctypes.POINTER(XLfrMode),
]
xlFrSetMode.errcheck = check_xl_status

xlFrInitStartupAndSync = _vector_xlapi_dll_.xlFrInitStartupAndSync
xlFrInitStartupAndSync.restype = XLstatus
xlFrInitStartupAndSync.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #pEventBuffer
    ctypes.POINTER(XLfrEvent),
]
xlFrInitStartupAndSync.errcheck = check_xl_status

xlFrSetupSymbolWindow = _vector_xlapi_dll_.xlFrSetupSymbolWindow
xlFrSetupSymbolWindow.restype = XLstatus
xlFrSetupSymbolWindow.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #frChannel
    ctypes.c_uint,
    #symbolWindowMask
    ctypes.c_uint,
]
xlFrSetupSymbolWindow.errcheck = check_xl_status

xlFrReceive = _vector_xlapi_dll_.xlFrReceive
xlFrReceive.restype = XLstatus
xlFrReceive.argtypes = [
    #portHandle
    XLportHandle,
    #pEventBuffer
    ctypes.POINTER(XLfrEvent),
]
xlFrReceive.errcheck = check_xl_status

xlFrTransmit = _vector_xlapi_dll_.xlFrTransmit
xlFrTransmit.restype = XLstatus
xlFrTransmit.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #pEventBuffer
    ctypes.POINTER(XLfrEvent),
]
xlFrTransmit.errcheck = check_xl_status

xlFrSetTransceiverMode = _vector_xlapi_dll_.xlFrSetTransceiverMode
xlFrSetTransceiverMode.restype = XLstatus
xlFrSetTransceiverMode.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #frChannel
    ctypes.c_uint,
    #mode
    ctypes.c_uint,
]
xlFrSetTransceiverMode.errcheck = check_xl_status

xlFrSendSymbolWindow = _vector_xlapi_dll_.xlFrSendSymbolWindow
xlFrSendSymbolWindow.restype = XLstatus
xlFrSendSymbolWindow.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #symbolWindow
    ctypes.c_uint,
]
xlFrSendSymbolWindow.errcheck = check_xl_status

xlFrActivateSpy = _vector_xlapi_dll_.xlFrActivateSpy
xlFrActivateSpy.restype = XLstatus
xlFrActivateSpy.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #mode
    ctypes.c_uint,
]
xlFrActivateSpy.errcheck = check_xl_status

xlFrSetAcceptanceFilter = _vector_xlapi_dll_.xlFrSetAcceptanceFilter
xlFrSetAcceptanceFilter.restype = XLstatus
xlFrSetAcceptanceFilter.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #pAcceptanceFilter
    ctypes.POINTER(XLfrAcceptanceFilter),
]
xlFrSetAcceptanceFilter.errcheck = check_xl_status

xlGetRemoteDriverConfig = _vector_xlapi_dll_.xlGetRemoteDriverConfig
xlGetRemoteDriverConfig.restype = XLstatus
xlGetRemoteDriverConfig.argtypes = [
    #pDriverConfig
    ctypes.POINTER(XLdriverConfig),
]
xlGetRemoteDriverConfig.errcheck = check_xl_status

xlGetRemoteDeviceInfo = _vector_xlapi_dll_.xlGetRemoteDeviceInfo
xlGetRemoteDeviceInfo.restype = XLstatus
xlGetRemoteDeviceInfo.argtypes = [
    #deviceList
    ctypes.POINTER(ctypes.POINTER(XLremoteDeviceInfo)),
    #nbrOfRemoteDevices
    ctypes.POINTER(ctypes.c_uint),
    #netSearch
    ctypes.c_uint,
]
xlGetRemoteDeviceInfo.errcheck = check_xl_status

xlReleaseRemoteDeviceInfo = _vector_xlapi_dll_.xlReleaseRemoteDeviceInfo
xlReleaseRemoteDeviceInfo.restype = XLstatus
xlReleaseRemoteDeviceInfo.argtypes = [
    #deviceList
    ctypes.POINTER(ctypes.POINTER(XLremoteDeviceInfo)),
]
xlReleaseRemoteDeviceInfo.errcheck = check_xl_status

xlAddRemoteDevice = _vector_xlapi_dll_.xlAddRemoteDevice
xlAddRemoteDevice.restype = XLstatus
xlAddRemoteDevice.argtypes = [
    #remoteHandle
    XLremoteHandle,
    #deviceMask
    XLdeviceAccess,
    #flags
    ctypes.c_uint,
]
xlAddRemoteDevice.errcheck = check_xl_status

xlRemoveRemoteDevice = _vector_xlapi_dll_.xlRemoveRemoteDevice
xlRemoveRemoteDevice.restype = XLstatus
xlRemoveRemoteDevice.argtypes = [
    #remoteHandle
    XLremoteHandle,
    #deviceMask
    XLdeviceAccess,
    #flags
    ctypes.c_uint,
]
xlRemoveRemoteDevice.errcheck = check_xl_status

xlUpdateRemoteDeviceInfo = _vector_xlapi_dll_.xlUpdateRemoteDeviceInfo
xlUpdateRemoteDeviceInfo.restype = XLstatus
xlUpdateRemoteDeviceInfo.argtypes = [
    #deviceList
    ctypes.POINTER(XLremoteDeviceInfo),
    #nbrOfRemoteDevices
    ctypes.c_uint,
]
xlUpdateRemoteDeviceInfo.errcheck = check_xl_status

xlGetRemoteHwInfo = _vector_xlapi_dll_.xlGetRemoteHwInfo
xlGetRemoteHwInfo.restype = XLstatus
xlGetRemoteHwInfo.argtypes = [
    #remoteHandle
    XLremoteHandle,
    #hwType
    ctypes.POINTER(ctypes.c_int),
    #hwIndex
    ctypes.POINTER(ctypes.c_int),
    #isPresent
    ctypes.POINTER(ctypes.c_int),
]
xlGetRemoteHwInfo.errcheck = check_xl_status

xlRegisterRemoteDevice = _vector_xlapi_dll_.xlRegisterRemoteDevice
xlRegisterRemoteDevice.restype = XLstatus
xlRegisterRemoteDevice.argtypes = [
    #hwType
    ctypes.c_int,
    #ipAddress
    ctypes.POINTER(XLipAddress),
    #flags
    ctypes.c_uint,
]
xlRegisterRemoteDevice.errcheck = check_xl_status

xlIoSetTriggerMode = _vector_xlapi_dll_.xlIoSetTriggerMode
xlIoSetTriggerMode.restype = XLstatus
xlIoSetTriggerMode.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #pxlDaioTriggerMode
    ctypes.POINTER(XLdaioTriggerMode),
]
xlIoSetTriggerMode.errcheck = check_xl_status

xlIoSetDigitalOutput = _vector_xlapi_dll_.xlIoSetDigitalOutput
xlIoSetDigitalOutput.restype = XLstatus
xlIoSetDigitalOutput.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #pxlDaioDigitalParams
    ctypes.POINTER(XLdaioDigitalParams),
]
xlIoSetDigitalOutput.errcheck = check_xl_status

xlIoConfigurePorts = _vector_xlapi_dll_.xlIoConfigurePorts
xlIoConfigurePorts.restype = XLstatus
xlIoConfigurePorts.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #pxlDaioSetPort
    ctypes.POINTER(XLdaioSetPort),
]
xlIoConfigurePorts.errcheck = check_xl_status

xlIoSetDigInThreshold = _vector_xlapi_dll_.xlIoSetDigInThreshold
xlIoSetDigInThreshold.restype = XLstatus
xlIoSetDigInThreshold.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #level
    ctypes.c_uint,
]
xlIoSetDigInThreshold.errcheck = check_xl_status

xlIoSetDigOutLevel = _vector_xlapi_dll_.xlIoSetDigOutLevel
xlIoSetDigOutLevel.restype = XLstatus
xlIoSetDigOutLevel.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #level
    ctypes.c_uint,
]
xlIoSetDigOutLevel.errcheck = check_xl_status

xlIoSetAnalogOutput = _vector_xlapi_dll_.xlIoSetAnalogOutput
xlIoSetAnalogOutput.restype = XLstatus
xlIoSetAnalogOutput.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #pxlDaioAnalogParams
    ctypes.POINTER(XLdaioAnalogParams),
]
xlIoSetAnalogOutput.errcheck = check_xl_status

xlIoStartSampling = _vector_xlapi_dll_.xlIoStartSampling
xlIoStartSampling.restype = XLstatus
xlIoStartSampling.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #portTypeMask
    ctypes.c_uint,
]
xlIoStartSampling.errcheck = check_xl_status

xlMost150Receive = _vector_xlapi_dll_.xlMost150Receive
xlMost150Receive.restype = XLstatus
xlMost150Receive.argtypes = [
    #portHandle
    XLportHandle,
    #pEventBuffer
    ctypes.POINTER(XLmost150event),
]
xlMost150Receive.errcheck = check_xl_status

xlMost150TwinklePowerLed = _vector_xlapi_dll_.xlMost150TwinklePowerLed
xlMost150TwinklePowerLed.restype = XLstatus
xlMost150TwinklePowerLed.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
]
xlMost150TwinklePowerLed.errcheck = check_xl_status

xlMost150SwitchEventSources = _vector_xlapi_dll_.xlMost150SwitchEventSources
xlMost150SwitchEventSources.restype = XLstatus
xlMost150SwitchEventSources.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #sourceMask
    ctypes.c_uint,
]
xlMost150SwitchEventSources.errcheck = check_xl_status

xlMost150SetDeviceMode = _vector_xlapi_dll_.xlMost150SetDeviceMode
xlMost150SetDeviceMode.restype = XLstatus
xlMost150SetDeviceMode.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #deviceMode
    ctypes.c_uint,
]
xlMost150SetDeviceMode.errcheck = check_xl_status

xlMost150GetDeviceMode = _vector_xlapi_dll_.xlMost150GetDeviceMode
xlMost150GetDeviceMode.restype = XLstatus
xlMost150GetDeviceMode.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
]
xlMost150GetDeviceMode.errcheck = check_xl_status

xlMost150SetSPDIFMode = _vector_xlapi_dll_.xlMost150SetSPDIFMode
xlMost150SetSPDIFMode.restype = XLstatus
xlMost150SetSPDIFMode.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #spdifMode
    ctypes.c_uint,
]
xlMost150SetSPDIFMode.errcheck = check_xl_status

xlMost150GetSPDIFMode = _vector_xlapi_dll_.xlMost150GetSPDIFMode
xlMost150GetSPDIFMode.restype = XLstatus
xlMost150GetSPDIFMode.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
]
xlMost150GetSPDIFMode.errcheck = check_xl_status

xlMost150SetSpecialNodeInfo = _vector_xlapi_dll_.xlMost150SetSpecialNodeInfo
xlMost150SetSpecialNodeInfo.restype = XLstatus
xlMost150SetSpecialNodeInfo.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #pSpecialNodeInfo
    ctypes.POINTER(XLmost150SetSpecialNodeInfo),
]
xlMost150SetSpecialNodeInfo.errcheck = check_xl_status

xlMost150GetSpecialNodeInfo = _vector_xlapi_dll_.xlMost150GetSpecialNodeInfo
xlMost150GetSpecialNodeInfo.restype = XLstatus
xlMost150GetSpecialNodeInfo.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #requestMask
    ctypes.c_uint,
]
xlMost150GetSpecialNodeInfo.errcheck = check_xl_status

xlMost150SetFrequency = _vector_xlapi_dll_.xlMost150SetFrequency
xlMost150SetFrequency.restype = XLstatus
xlMost150SetFrequency.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #frequency
    ctypes.c_uint,
]
xlMost150SetFrequency.errcheck = check_xl_status

xlMost150GetFrequency = _vector_xlapi_dll_.xlMost150GetFrequency
xlMost150GetFrequency.restype = XLstatus
xlMost150GetFrequency.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
]
xlMost150GetFrequency.errcheck = check_xl_status

xlMost150CtrlTransmit = _vector_xlapi_dll_.xlMost150CtrlTransmit
xlMost150CtrlTransmit.restype = XLstatus
xlMost150CtrlTransmit.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #pCtrlTxMsg
    ctypes.POINTER(XLmost150CtrlTxMsg),
]
xlMost150CtrlTransmit.errcheck = check_xl_status

xlMost150AsyncTransmit = _vector_xlapi_dll_.xlMost150AsyncTransmit
xlMost150AsyncTransmit.restype = XLstatus
xlMost150AsyncTransmit.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #pAsyncTxMsg
    ctypes.POINTER(XLmost150AsyncTxMsg),
]
xlMost150AsyncTransmit.errcheck = check_xl_status

xlMost150EthernetTransmit = _vector_xlapi_dll_.xlMost150EthernetTransmit
xlMost150EthernetTransmit.restype = XLstatus
xlMost150EthernetTransmit.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #pEthernetTxMsg
    ctypes.POINTER(XLmost150EthernetTxMsg),
]
xlMost150EthernetTransmit.errcheck = check_xl_status

xlMost150GetSystemLockFlag = _vector_xlapi_dll_.xlMost150GetSystemLockFlag
xlMost150GetSystemLockFlag.restype = XLstatus
xlMost150GetSystemLockFlag.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
]
xlMost150GetSystemLockFlag.errcheck = check_xl_status

xlMost150GetShutdownFlag = _vector_xlapi_dll_.xlMost150GetShutdownFlag
xlMost150GetShutdownFlag.restype = XLstatus
xlMost150GetShutdownFlag.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
]
xlMost150GetShutdownFlag.errcheck = check_xl_status

xlMost150Shutdown = _vector_xlapi_dll_.xlMost150Shutdown
xlMost150Shutdown.restype = XLstatus
xlMost150Shutdown.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
]
xlMost150Shutdown.errcheck = check_xl_status

xlMost150Startup = _vector_xlapi_dll_.xlMost150Startup
xlMost150Startup.restype = XLstatus
xlMost150Startup.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
]
xlMost150Startup.errcheck = check_xl_status

xlMost150SyncGetAllocTable = _vector_xlapi_dll_.xlMost150SyncGetAllocTable
xlMost150SyncGetAllocTable.restype = XLstatus
xlMost150SyncGetAllocTable.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
]
xlMost150SyncGetAllocTable.errcheck = check_xl_status

xlMost150CtrlSyncAudio = _vector_xlapi_dll_.xlMost150CtrlSyncAudio
xlMost150CtrlSyncAudio.restype = XLstatus
xlMost150CtrlSyncAudio.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #pSyncAudioParameter
    ctypes.POINTER(XLmost150SyncAudioParameter),
]
xlMost150CtrlSyncAudio.errcheck = check_xl_status

xlMost150SyncSetVolume = _vector_xlapi_dll_.xlMost150SyncSetVolume
xlMost150SyncSetVolume.restype = XLstatus
xlMost150SyncSetVolume.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #device
    ctypes.c_uint,
    #volume
    ctypes.c_uint,
]
xlMost150SyncSetVolume.errcheck = check_xl_status

xlMost150SyncGetVolume = _vector_xlapi_dll_.xlMost150SyncGetVolume
xlMost150SyncGetVolume.restype = XLstatus
xlMost150SyncGetVolume.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #device
    ctypes.c_uint,
]
xlMost150SyncGetVolume.errcheck = check_xl_status

xlMost150SyncSetMute = _vector_xlapi_dll_.xlMost150SyncSetMute
xlMost150SyncSetMute.restype = XLstatus
xlMost150SyncSetMute.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #device
    ctypes.c_uint,
    #mute
    ctypes.c_uint,
]
xlMost150SyncSetMute.errcheck = check_xl_status

xlMost150SyncGetMute = _vector_xlapi_dll_.xlMost150SyncGetMute
xlMost150SyncGetMute.restype = XLstatus
xlMost150SyncGetMute.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #device
    ctypes.c_uint,
]
xlMost150SyncGetMute.errcheck = check_xl_status

xlMost150GetRxLightLockStatus = _vector_xlapi_dll_.xlMost150GetRxLightLockStatus
xlMost150GetRxLightLockStatus.restype = XLstatus
xlMost150GetRxLightLockStatus.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #fromSpy
    ctypes.c_uint,
]
xlMost150GetRxLightLockStatus.errcheck = check_xl_status

xlMost150SetTxLight = _vector_xlapi_dll_.xlMost150SetTxLight
xlMost150SetTxLight.restype = XLstatus
xlMost150SetTxLight.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #txLight
    ctypes.c_uint,
]
xlMost150SetTxLight.errcheck = check_xl_status

xlMost150GetTxLight = _vector_xlapi_dll_.xlMost150GetTxLight
xlMost150GetTxLight.restype = XLstatus
xlMost150GetTxLight.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
]
xlMost150GetTxLight.errcheck = check_xl_status

xlMost150SetTxLightPower = _vector_xlapi_dll_.xlMost150SetTxLightPower
xlMost150SetTxLightPower.restype = XLstatus
xlMost150SetTxLightPower.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #attenuation
    ctypes.c_uint,
]
xlMost150SetTxLightPower.errcheck = check_xl_status

xlMost150GenerateLightError = _vector_xlapi_dll_.xlMost150GenerateLightError
xlMost150GenerateLightError.restype = XLstatus
xlMost150GenerateLightError.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #lightOffTime
    ctypes.c_uint,
    #lightOnTime
    ctypes.c_uint,
    #repeat
    ctypes.c_uint,
]
xlMost150GenerateLightError.errcheck = check_xl_status

xlMost150GenerateLockError = _vector_xlapi_dll_.xlMost150GenerateLockError
xlMost150GenerateLockError.restype = XLstatus
xlMost150GenerateLockError.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #unlockTime
    ctypes.c_uint,
    #lockTime
    ctypes.c_uint,
    #repeat
    ctypes.c_uint,
]
xlMost150GenerateLockError.errcheck = check_xl_status

xlMost150ConfigureRxBuffer = _vector_xlapi_dll_.xlMost150ConfigureRxBuffer
xlMost150ConfigureRxBuffer.restype = XLstatus
xlMost150ConfigureRxBuffer.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #bufferType
    ctypes.c_uint,
    #bufferMode
    ctypes.c_uint,
]
xlMost150ConfigureRxBuffer.errcheck = check_xl_status

xlMost150CtrlConfigureBusload = _vector_xlapi_dll_.xlMost150CtrlConfigureBusload
xlMost150CtrlConfigureBusload.restype = XLstatus
xlMost150CtrlConfigureBusload.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #pCtrlBusLoad
    ctypes.POINTER(XLmost150CtrlBusloadConfig),
]
xlMost150CtrlConfigureBusload.errcheck = check_xl_status

xlMost150CtrlGenerateBusload = _vector_xlapi_dll_.xlMost150CtrlGenerateBusload
xlMost150CtrlGenerateBusload.restype = XLstatus
xlMost150CtrlGenerateBusload.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #numberCtrlFrames
    XLulong,
]
xlMost150CtrlGenerateBusload.errcheck = check_xl_status

xlMost150AsyncConfigureBusload = _vector_xlapi_dll_.xlMost150AsyncConfigureBusload
xlMost150AsyncConfigureBusload.restype = XLstatus
xlMost150AsyncConfigureBusload.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #pAsyncBusLoad
    ctypes.POINTER(XLmost150AsyncBusloadConfig),
]
xlMost150AsyncConfigureBusload.errcheck = check_xl_status

xlMost150AsyncGenerateBusload = _vector_xlapi_dll_.xlMost150AsyncGenerateBusload
xlMost150AsyncGenerateBusload.restype = XLstatus
xlMost150AsyncGenerateBusload.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #numberAsyncPackets
    XLulong,
]
xlMost150AsyncGenerateBusload.errcheck = check_xl_status

xlMost150SetECLLine = _vector_xlapi_dll_.xlMost150SetECLLine
xlMost150SetECLLine.restype = XLstatus
xlMost150SetECLLine.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #eclLineState
    ctypes.c_uint,
]
xlMost150SetECLLine.errcheck = check_xl_status

xlMost150SetECLTermination = _vector_xlapi_dll_.xlMost150SetECLTermination
xlMost150SetECLTermination.restype = XLstatus
xlMost150SetECLTermination.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #eclLineTermination
    ctypes.c_uint,
]
xlMost150SetECLTermination.errcheck = check_xl_status

xlMost150GetECLInfo = _vector_xlapi_dll_.xlMost150GetECLInfo
xlMost150GetECLInfo.restype = XLstatus
xlMost150GetECLInfo.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
]
xlMost150GetECLInfo.errcheck = check_xl_status

xlMost150StreamOpen = _vector_xlapi_dll_.xlMost150StreamOpen
xlMost150StreamOpen.restype = XLstatus
xlMost150StreamOpen.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #pStreamOpen
    ctypes.POINTER(XLmost150StreamOpen),
]
xlMost150StreamOpen.errcheck = check_xl_status

xlMost150StreamClose = _vector_xlapi_dll_.xlMost150StreamClose
xlMost150StreamClose.restype = XLstatus
xlMost150StreamClose.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #streamHandle
    ctypes.c_uint,
]
xlMost150StreamClose.errcheck = check_xl_status

xlMost150StreamStart = _vector_xlapi_dll_.xlMost150StreamStart
xlMost150StreamStart.restype = XLstatus
xlMost150StreamStart.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #streamHandle
    ctypes.c_uint,
    #numConnLabels
    ctypes.c_uint,
    #pConnLabels
    ctypes.POINTER(ctypes.c_uint),
]
xlMost150StreamStart.errcheck = check_xl_status

xlMost150StreamStop = _vector_xlapi_dll_.xlMost150StreamStop
xlMost150StreamStop.restype = XLstatus
xlMost150StreamStop.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #streamHandle
    ctypes.c_uint,
]
xlMost150StreamStop.errcheck = check_xl_status

xlMost150StreamTransmitData = _vector_xlapi_dll_.xlMost150StreamTransmitData
xlMost150StreamTransmitData.restype = XLstatus
xlMost150StreamTransmitData.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #streamHandle
    ctypes.c_uint,
    #pBuffer
    ctypes.POINTER(ctypes.c_ubyte),
    #pNumberOfBytes
    ctypes.POINTER(ctypes.c_uint),
]
xlMost150StreamTransmitData.errcheck = check_xl_status

xlMost150StreamClearTxFifo = _vector_xlapi_dll_.xlMost150StreamClearTxFifo
xlMost150StreamClearTxFifo.restype = XLstatus
xlMost150StreamClearTxFifo.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #streamHandle
    ctypes.c_uint,
]
xlMost150StreamClearTxFifo.errcheck = check_xl_status

xlMost150StreamGetInfo = _vector_xlapi_dll_.xlMost150StreamGetInfo
xlMost150StreamGetInfo.restype = XLstatus
xlMost150StreamGetInfo.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #pStreamInfo
    ctypes.POINTER(XLmost150StreamInfo),
]
xlMost150StreamGetInfo.errcheck = check_xl_status

xlMost150StreamInitRxFifo = _vector_xlapi_dll_.xlMost150StreamInitRxFifo
xlMost150StreamInitRxFifo.restype = XLstatus
xlMost150StreamInitRxFifo.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
]
xlMost150StreamInitRxFifo.errcheck = check_xl_status

xlMost150StreamReceiveData = _vector_xlapi_dll_.xlMost150StreamReceiveData
xlMost150StreamReceiveData.restype = XLstatus
xlMost150StreamReceiveData.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #pBuffer
    ctypes.POINTER(ctypes.c_ubyte),
    #pBufferSize
    ctypes.POINTER(ctypes.c_uint),
]
xlMost150StreamReceiveData.errcheck = check_xl_status

xlMost150GenerateBypassStress = _vector_xlapi_dll_.xlMost150GenerateBypassStress
xlMost150GenerateBypassStress.restype = XLstatus
xlMost150GenerateBypassStress.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #bypassCloseTime
    ctypes.c_uint,
    #bypassOpenTime
    ctypes.c_uint,
    #repeat
    ctypes.c_uint,
]
xlMost150GenerateBypassStress.errcheck = check_xl_status

xlMost150EclConfigureSeq = _vector_xlapi_dll_.xlMost150EclConfigureSeq
xlMost150EclConfigureSeq.restype = XLstatus
xlMost150EclConfigureSeq.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #numStates
    ctypes.c_uint,
    #pEclStates
    ctypes.POINTER(ctypes.c_uint),
    #pEclStatesDuration
    ctypes.POINTER(ctypes.c_uint),
]
xlMost150EclConfigureSeq.errcheck = check_xl_status

xlMost150EclGenerateSeq = _vector_xlapi_dll_.xlMost150EclGenerateSeq
xlMost150EclGenerateSeq.restype = XLstatus
xlMost150EclGenerateSeq.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #start
    ctypes.c_uint,
]
xlMost150EclGenerateSeq.errcheck = check_xl_status

xlMost150SetECLGlitchFilter = _vector_xlapi_dll_.xlMost150SetECLGlitchFilter
xlMost150SetECLGlitchFilter.restype = XLstatus
xlMost150SetECLGlitchFilter.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #duration
    ctypes.c_uint,
]
xlMost150SetECLGlitchFilter.errcheck = check_xl_status

xlMost150SetSSOResult = _vector_xlapi_dll_.xlMost150SetSSOResult
xlMost150SetSSOResult.restype = XLstatus
xlMost150SetSSOResult.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #ssoCUStatus
    ctypes.c_uint,
]
xlMost150SetSSOResult.errcheck = check_xl_status

xlMost150GetSSOResult = _vector_xlapi_dll_.xlMost150GetSSOResult
xlMost150GetSSOResult.restype = XLstatus
xlMost150GetSSOResult.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
]
xlMost150GetSSOResult.errcheck = check_xl_status

xlEthSetConfig = _vector_xlapi_dll_.xlEthSetConfig
xlEthSetConfig.restype = XLstatus
xlEthSetConfig.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #config
    ctypes.POINTER(T_XL_ETH_CONFIG),
]
xlEthSetConfig.errcheck = check_xl_status

xlEthGetConfig = _vector_xlapi_dll_.xlEthGetConfig
xlEthGetConfig.restype = XLstatus
xlEthGetConfig.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #config
    ctypes.POINTER(T_XL_ETH_CONFIG),
]
xlEthGetConfig.errcheck = check_xl_status

xlEthReceive = _vector_xlapi_dll_.xlEthReceive
xlEthReceive.restype = XLstatus
xlEthReceive.argtypes = [
    #portHandle
    XLportHandle,
    #ethEventBuffer
    ctypes.POINTER(T_XL_ETH_EVENT),
]
xlEthReceive.errcheck = check_xl_status

xlEthSetBypass = _vector_xlapi_dll_.xlEthSetBypass
xlEthSetBypass.restype = XLstatus
xlEthSetBypass.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #mode
    ctypes.c_uint,
]
xlEthSetBypass.errcheck = check_xl_status

xlEthTwinkleStatusLed = _vector_xlapi_dll_.xlEthTwinkleStatusLed
xlEthTwinkleStatusLed.restype = XLstatus
xlEthTwinkleStatusLed.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
]
xlEthTwinkleStatusLed.errcheck = check_xl_status

xlEthTransmit = _vector_xlapi_dll_.xlEthTransmit
xlEthTransmit.restype = XLstatus
xlEthTransmit.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #userHandle
    XLuserHandle,
    #data
    ctypes.POINTER(T_XL_ETH_DATAFRAME_TX),
]
xlEthTransmit.errcheck = check_xl_status

xlNetEthOpenNetwork = _vector_xlapi_dll_.xlNetEthOpenNetwork
xlNetEthOpenNetwork.restype = XLstatus
xlNetEthOpenNetwork.argtypes = [
    #pNetworkName
    ctypes.c_char_p,
    #pNetworkHandle
    ctypes.POINTER(XLnetworkHandle),
    #pAppName
    ctypes.c_char_p,
    #accessType
    ctypes.c_uint,
    #queueSize
    ctypes.c_uint,
]
xlNetEthOpenNetwork.errcheck = check_xl_status

xlNetCloseNetwork = _vector_xlapi_dll_.xlNetCloseNetwork
xlNetCloseNetwork.restype = XLstatus
xlNetCloseNetwork.argtypes = [
    #networkHandle
    XLnetworkHandle,
]
xlNetCloseNetwork.errcheck = check_xl_status

xlNetOpenVirtualPort = _vector_xlapi_dll_.xlNetOpenVirtualPort
xlNetOpenVirtualPort.restype = XLstatus
xlNetOpenVirtualPort.argtypes = [
    #networkHandle
    XLnetworkHandle,
    #pVPortName
    ctypes.c_char_p,
    #pEthPortHandle
    ctypes.POINTER(XLethPortHandle),
    #rxHandle
    XLrxHandle,
]
xlNetOpenVirtualPort.errcheck = check_xl_status

xlNetAddVirtualPort = _vector_xlapi_dll_.xlNetAddVirtualPort
xlNetAddVirtualPort.restype = XLstatus
xlNetAddVirtualPort.argtypes = [
    #networkHandle
    XLnetworkHandle,
    #pSwitchName
    ctypes.c_char_p,
    #pVPortName
    ctypes.c_char_p,
    #pEthPortHandle
    ctypes.POINTER(XLethPortHandle),
    #rxHandle
    XLrxHandle,
]
xlNetAddVirtualPort.errcheck = check_xl_status

xlNetConnectMeasurementPoint = _vector_xlapi_dll_.xlNetConnectMeasurementPoint
xlNetConnectMeasurementPoint.restype = XLstatus
xlNetConnectMeasurementPoint.argtypes = [
    #networkHandle
    XLnetworkHandle,
    #pPortName
    ctypes.c_char_p,
    #pEthPortHandle
    ctypes.POINTER(XLethPortHandle),
    #rxHandle
    XLrxHandle,
]
xlNetConnectMeasurementPoint.errcheck = check_xl_status

xlNetActivateNetwork = _vector_xlapi_dll_.xlNetActivateNetwork
xlNetActivateNetwork.restype = XLstatus
xlNetActivateNetwork.argtypes = [
    #networkHandle
    XLnetworkHandle,
]
xlNetActivateNetwork.errcheck = check_xl_status

xlNetDeactivateNetwork = _vector_xlapi_dll_.xlNetDeactivateNetwork
xlNetDeactivateNetwork.restype = XLstatus
xlNetDeactivateNetwork.argtypes = [
    #networkHandle
    XLnetworkHandle,
]
xlNetDeactivateNetwork.errcheck = check_xl_status

xlNetEthSend = _vector_xlapi_dll_.xlNetEthSend
xlNetEthSend.restype = XLstatus
xlNetEthSend.argtypes = [
    #networkHandle
    XLnetworkHandle,
    #ethPortHandle
    XLethPortHandle,
    #userHandle
    XLuserHandle,
    #pEthTxFrame
    ctypes.POINTER(T_XL_NET_ETH_DATAFRAME_TX),
]
xlNetEthSend.errcheck = check_xl_status

xlNetEthReceive = _vector_xlapi_dll_.xlNetEthReceive
xlNetEthReceive.restype = XLstatus
xlNetEthReceive.argtypes = [
    #networkHandle
    XLnetworkHandle,
    #pEventBuffer
    ctypes.POINTER(T_XL_NET_ETH_EVENT),
    #pRxHandleCount
    ctypes.POINTER(ctypes.c_uint),
    #pRxHandle
    ctypes.POINTER(XLrxHandle),
]
xlNetEthReceive.errcheck = check_xl_status

xlNetEthRequestChannelStatus = _vector_xlapi_dll_.xlNetEthRequestChannelStatus
xlNetEthRequestChannelStatus.restype = XLstatus
xlNetEthRequestChannelStatus.argtypes = [
    #networkHandle
    XLnetworkHandle,
]
xlNetEthRequestChannelStatus.errcheck = check_xl_status

xlNetSetNotification = _vector_xlapi_dll_.xlNetSetNotification
xlNetSetNotification.restype = XLstatus
xlNetSetNotification.argtypes = [
    #networkHandle
    XLnetworkHandle,
    #pHandle
    ctypes.POINTER(XLhandle),
    #queueLevel
    ctypes.c_int,
]
xlNetSetNotification.errcheck = check_xl_status

xlNetRequestMACAddress = _vector_xlapi_dll_.xlNetRequestMACAddress
xlNetRequestMACAddress.restype = XLstatus
xlNetRequestMACAddress.argtypes = [
    #networkHandle
    XLnetworkHandle,
    #pMACAddress
    ctypes.POINTER(T_XL_ETH_MAC_ADDRESS),
]
xlNetRequestMACAddress.errcheck = check_xl_status

xlNetReleaseMACAddress = _vector_xlapi_dll_.xlNetReleaseMACAddress
xlNetReleaseMACAddress.restype = XLstatus
xlNetReleaseMACAddress.argtypes = [
    #networkHandle
    XLnetworkHandle,
    #pMACAddress
    ctypes.POINTER(T_XL_ETH_MAC_ADDRESS),
]
xlNetReleaseMACAddress.errcheck = check_xl_status

xlNetFlushReceiveQueue = _vector_xlapi_dll_.xlNetFlushReceiveQueue
xlNetFlushReceiveQueue.restype = XLstatus
xlNetFlushReceiveQueue.argtypes = [
    #networkHandle
    XLnetworkHandle,
]
xlNetFlushReceiveQueue.errcheck = check_xl_status

xlA429Receive = _vector_xlapi_dll_.xlA429Receive
xlA429Receive.restype = XLstatus
xlA429Receive.argtypes = [
    #portHandle
    XLportHandle,
    #pXlA429RxEvt
    ctypes.POINTER(XLa429RxEvent),
]
xlA429Receive.errcheck = check_xl_status

xlA429SetChannelParams = _vector_xlapi_dll_.xlA429SetChannelParams
xlA429SetChannelParams.restype = XLstatus
xlA429SetChannelParams.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #pXlA429Params
    ctypes.POINTER(XL_A429_PARAMS),
]
xlA429SetChannelParams.errcheck = check_xl_status

xlA429Transmit = _vector_xlapi_dll_.xlA429Transmit
xlA429Transmit.restype = XLstatus
xlA429Transmit.argtypes = [
    #portHandle
    XLportHandle,
    #accessMask
    XLaccess,
    #msgCnt
    ctypes.c_uint,
    #pMsgCntSent
    ctypes.POINTER(ctypes.c_uint),
    #pXlA429MsgTx
    ctypes.POINTER(XL_A429_MSG_TX),
]
xlA429Transmit.errcheck = check_xl_status

xlGetKeymanBoxes = _vector_xlapi_dll_.xlGetKeymanBoxes
xlGetKeymanBoxes.restype = XLstatus
xlGetKeymanBoxes.argtypes = [
    #boxCount
    ctypes.POINTER(ctypes.c_uint),
]
xlGetKeymanBoxes.errcheck = check_xl_status

xlGetKeymanInfo = _vector_xlapi_dll_.xlGetKeymanInfo
xlGetKeymanInfo.restype = XLstatus
xlGetKeymanInfo.argtypes = [
    #boxIndex
    ctypes.c_uint,
    #boxMask
    ctypes.POINTER(ctypes.c_uint),
    #boxSerial
    ctypes.POINTER(ctypes.c_uint),
    #licInfo
    ctypes.POINTER(XLuint64),
]
xlGetKeymanInfo.errcheck = check_xl_status
