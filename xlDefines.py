##############################################################################
#                                                                            #
# Module: xlDefines                                                          #
# Author: Maximilian Prindl                                                  #
#                                                                            #
# Part of a python ctypes wrapper lib for the Vector XL Driver Library.      #
# Contains most of the #define instructions of the 'vxlapi.h'.               #
# They are classed as enums so e.g. the original # define XL_BUS_TYPE_CAN    #
# can be acessed through XL_BUS_TYPE.CAN.                                    #
#                                                                            #
##############################################################################

from enum import Enum, IntEnum, IntFlag

class XL_BUS_TYPE(IntEnum):
  NONE     =    0
  CAN      =    1
  LIN      =    2
  FLEXRAY  =    4
  AFDX     =    8 #former BUS_TYPE_BEAN
  MOST     =   16
  DAIO     =   64 #IO cab/piggy
  J1708    =  256
  KLINE    = 2048
  ETHERNET = 4096
  A429     = 8192

class XL_TRANSCEIVER_TYPE(IntEnum):
  #Can Cab
  NONE = 0
  CAN_251 = 1
  CAN_252 = 2
  CAN_DNOPTO = 3
  CAN_SWC_PROTO = 5 #Prototype. Driver may latch-up.
  CAN_SWC = 6
  CAN_EVA = 7
  CAN_FIBER = 8
  CAN_1054_OPTO = 11 #1054 with optical isolation
  CAN_SWC_OPTO = 12 #SWC with optical isolation
  CAN_B10011S = 13 #B10011S truck-and-trailer
  CAN_1050 = 14 #1050
  CAN_1050_OPTO = 15 #1050 with optical isolation
  CAN_1041 = 16 #1041
  CAN_1041_OPTO = 17 #1041 with optical isolation
  CAN_VIRTUAL = 22 #Virtual CAN Transceiver for Virtual CAN Bus Driver
  LIN_6258_OPTO = 23 #Vector LINcab 6258opto with transceiver Infineon TLE6258
  LIN_6259_OPTO = 25 #Vector LINcab 6259opto with transceiver Infineon TLE6259
  DAIO_8444_OPTO = 29 #Vector IOcab 8444  (8 dig.Inp.; 4 dig.Outp.; 4 ana.Inp.; 4 ana.Outp.)
  CAN_1041A_OPTO = 33 #1041A with optical isolation
  LIN_6259_MAG = 35 #LIN transceiver 6259, with transceiver Infineon TLE6259, magnetically isolated, stress functionality
  LIN_7259_MAG = 37 #LIN transceiver 7259, with transceiver Infineon TLE7259, magnetically isolated, stress functionality
  LIN_7269_MAG = 39 #LIN transceiver 7269, with transceiver Infineon TLE7269, magnetically isolated, stress functionality
  CAN_1054_MAG = 51 #TJA1054, magnetically isolated, with selectable termination resistor (via 4th IO line) 
  CAN_251_MAG = 53 #82C250/251 or equivalent, magnetically isolated
  CAN_1050_MAG = 55 #TJA1050, magnetically isolated
  CAN_1040_MAG = 57 #TJA1040, magnetically isolated
  CAN_1041A_MAG = 59 #TJA1041A, magnetically isolated
  TWIN_CAN_1041A_MAG = 128 #TWINcab with two TJA1041, magnetically isolated
  TWIN_LIN_7269_MAG = 129 #TWINcab with two 7259, Infineon TLE7259, magnetically isolated, stress functionality
  TWIN_CAN_1041AV2_MAG = 130 #TWINcab with two TJA1041, magnetically isolated
  TWIN_CAN_1054_1041A_MAG = 131 #TWINcab with TJA1054A and TJA1041A with magnetic isolation
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
  PB_LIN_6258_OPTO = 297 #LIN piggy back with transceiver Infineon TLE6258
  PB_LIN_6259_OPTO = 299 #LIN piggy back with transceiver Infineon TLE6259
  PB_LIN_6259_MAG = 301 #LIN piggy back with transceiver Infineon TLE6259, magnetically isolated, stress functionality
  PB_CAN_1041A_OPTO = 303 #CAN transceiver 1041A
  PB_LIN_7259_MAG = 305 #LIN piggy back with transceiver Infineon TLE7259, magnetically isolated, stress functionality
  PB_LIN_7269_MAG = 307 #LIN piggy back with transceiver Infineon TLE7269, magnetically isolated, stress functionality
  PB_CAN_251_MAG = 309 #82C250/251 or compatible, magnetically isolated
  PB_CAN_1050_MAG = 310 #TJA 1050, magnetically isolated
  PB_CAN_1040_MAG = 311 #TJA 1040, magnetically isolated
  PB_CAN_1041A_MAG = 312 #TJA 1041A, magnetically isolated
  PB_DAIO_8444_OPTO = 313 #optically isolated IO piggy
  PB_CAN_1054_MAG = 315 #TJA1054, magnetically isolated, with selectable termination resistor (via 4th IO line) 
  CAN_1051_CAP_FIX = 316 #TJA1051 - fixed transceiver on e.g. 16xx/8970
  DAIO_1021_FIX = 317 #Onboard IO of VN1630/VN1640
  LIN_7269_CAP_FIX = 318 #TLE7269 - fixed transceiver on VN1611
  PB_CAN_1051_CAP = 319 #TJA 1051, capacitive isolated
  PB_CAN_SWC_7356_CAP = 320 #Single Wire NCV7356, capacitive isolated
  PB_CAN_1055_CAP = 321 #TJA1055, capacitive isolated, with selectable termination resistor (via 4th IO line)
  PB_CAN_1057_CAP = 322 #TJA 1057, capacitive isolated
  A429_HOLT8596_FIX = 323 #Onboard HOLT 8596 TX transceiver on VN0601
  A429_HOLT8455_FIX = 324 #Onboard HOLT 8455 RX transceiver on VN0601
  PB_CAN_1051HG_CAP = 325 #TJA 1051HG, capacitive isolated
  CAN_1057_FIX = 326 #TJA 1057 - fixed transceiver on e.g. VN1530, VN4610
  LIN_7269_FIX = 327 #TLE7269 - fixed transceiver on VN1531
  PB_CAN_1462BT = 329
  #FlexRay PiggyBacks
  PB_FR_1080 = 513 #TJA 1080
  PB_FR_1080_MAG = 514 #TJA 1080 magnetically isolated piggy
  PB_FR_1080A_MAG = 515 #TJA 1080A magnetically isolated piggy
  PB_FR_1082_CAP = 516 #TJA 1082 capacitive isolated piggy
  PB_FRC_1082_CAP = 517 #TJA 1082 capacitive isolated piggy with CANpiggy form factor
  FR_1082_CAP_FIX = 518 #TJA 1082 capacitive isolated piggy fixed transceiver - e.g. 7610
  MOST150_ONBOARD = 544 #Onboard MOST150 transceiver of VN2640
  #Ethernet Phys
  ETH_BCM54810_FIX = 560 #Onboard Broadcom Ethernet PHY on VN5610 and VX0312
  ETH_AR8031_FIX = 561 #Onboard Atheros Ethernet PHY
  ETH_BCM89810_FIX = 562 #Onboard Broadcom Ethernet PHY
  ETH_TJA1100_FIX = 563 #Onboard NXP Ethernet PHY
  ETH_BCM54810_89811_FIX = 564 #Onboard Broadcom Ethernet PHYs (e.g. VN5610A - BCM54810: RJ45, BCM89811: DSUB)
  ETH_DP83XG710Q1_FIX = 565 #Onboard TI 1000BASE-T1 Eth PHY
  ETH_BCM54811S_FIX = 566 #Onboard Broadcom Ethernet PHY on VN7640 and VH6501
  ETH_RTL9000AA_FIX = 567 #Onboard Realtek Eth PHY
  ETH_BCM89811_FIX = 568 #Onboard Broadcom Ethernet PHY
  ETH_BCM54210_FIX = 569 #Onboard Broadcom BCM54210
  ETH_88Q2112_FIX = 570 #Onboard Marvell 88Q2112
  ETH_BCM84891_FIX = 571 #Onboard Broadcom BCM84891
  #IOpiggy 8642
  PB_DAIO_8642 = 640 #Iopiggy for VN8900
  DAIO_AL_ONLY = 655 #virtual piggy type for activation line only (e.g. VN8810ini)
  DAIO_1021_FIX_WITH_AL = 656 #On board IO with Activation Line (e.g. VN5640) 
  DAIO_AL_WU = 657 #virtual piggy type for activation line and WakeUp Line only (e.g. VN5610A/VN5620)
  DAIO_1021_FIX_WITH_5V = 658 #On board IO with 2nd output (e.g. 5V CMOS @ VN4610) 
  #Eth modules
  ETH_MOD_BR_BCM89810 = 768 #BroadR-Reach Module with 2x Broadcom BCM89810
  ETH_MOD_IEEE_RGMII_AR8031 = 769 #IEEE802.3 RGMII Module with 2x Atheros AR8031
  ETH_MOD_IEEE_SGMII_AR8031 = 770 #IEEE802.3 SGMII Module with 2x Atheros AR8031
  ETH_MOD_BR_TJA1100 = 771 #BroadR-Reach Module with 2x NXP TJA1100
  ETH_MOD_BR_RTL9000AA = 772 #BroadR-Reach Module with 2x Realtek RTL9000-AA
  ETH_MOD_BR_SGMII_DP83XG710Q1 = 773 #1Gbit (1000BASE-T1) SGMII Module with 2x TI DP83GX710-Q1
  ETH_MOD_BR_88Q2112 = 774 #BroadR-Reach Module with 2x Marvell 88Q2112
  ETH_MOD_BR_BCM89811 = 775 #BroadR-Reach Module with 2x Broadcom BCM89811
  ETH_MOD_BR_TJA1101 = 776 #100BASE-T1 Module with 2x NXP TJA1101
  #AE modules
  AE_MOD_BR_BCM89883 = 1025 #100/1000BASE-T1 Module with 4x Broadcom BCM89883
  #VT Ethernet piggy
  PB_ETH_100BASET1_TJA1101 = 8066 #100BASE-T1 piggy with 6x NXP TJA1101
  PB_ETH_1000BASET1_88Q2112 = 8067 #1000BASE-T1 piggy with 6x Marvell 88Q2112

class XL_TRANSCEIVER_LINEMODE(IntEnum):
  NA = 0
  TWO_LINE = 1
  CAN_H = 2
  CAN_L = 3
  SWC_SLEEP = 4 #SWC Sleep Mode
  SWC_NORMAL = 5 #SWC Normal Mode
  SWC_FAST = 6 #SWC High-Speed Mode
  SWC_WAKEUP = 7 #SWC Wakeup Mode
  SLEEP = 8
  NORMAL = 9
  STDBY = 10 #Standby for those who support it
  TT_CAN_H = 11 #truck & trailer: operating mode single wire using CAN high
  TT_CAN_L = 12 #truck & trailer: operating mode single wire using CAN low
  EVA_00 = 13 #CANcab Eva
  EVA_01 = 14 #CANcab Eva
  EVA_10 = 15 #CANcab Eva
  EVA_11 = 16 #CANcab Eva

class XL_TRANSCEIVER_STATUS(IntFlag):
  PRESENT = 1
  POWER_GOOD = 16
  EXT_POWER_GOOD = 32
  NOT_SUPPORTED = 64

class XL_DRIVER_STATUS(IntEnum):
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
  ERR_PDU_OUT_OF_MEMORY = 260 #Too many PDUs configured or too less system memory free
  ERR_FR_CLUSTERCONFIG_MISSING = 261 #No cluster configuration has been sent to the driver but is needed for the command which failed
  ERR_PDU_OFFSET_REPET_INVALID = 262 #Invalid offset and/or repetition value specified
  ERR_PDU_PAYLOAD_SIZE_INVALID = 263 #Specified PDU payload size is invalid (e.g. size is too large) Frame-API: size is different than static payload length configured in cluster config
  ERR_FR_NBR_FRAMES_OVERFLOW = 265 #Too many frames specified in parameter
  ERR_FR_SLOT_ID_INVALID = 267 #Specified slot-ID exceeds biggest possible ID specified by the cluster configuration
  ERR_FR_SLOT_ALREADY_OCCUPIED_BY_ERAY = 268 #Specified slot cannot be used by Coldstart-Controller because it's already in use by the eRay
  ERR_FR_SLOT_ALREADY_OCCUPIED_BY_COLDC = 269 #Specified slot cannot be used by eRay because it's already in use by the Coldstart-Controller
  ERR_FR_SLOT_OCCUPIED_BY_OTHER_APP = 270 #Specified slot cannot be used because it's already in use by another application
  ERR_FR_SLOT_IN_WRONG_SEGMENT = 271 #Specified slot is not in correct segment. E.g.: A dynamic slot was specified for startup&sync
  ERR_FR_FRAME_CYCLE_MULTIPLEX_ERROR = 272 #The given frame-multiplexing rule (specified by offset and repetition) cannot be done because some of the slots are already in use
  ERR_PDU_NO_UNMAP_OF_SYNCFRAME = 278 #Unmapping of eRay startup/sync frames is not allowed
  ERR_SYNC_FRAME_MODE = 291 #Wrong txMode in sync frame
  ERR_INVALID_DLC = 513 #DLC with invalid value
  ERR_INVALID_CANID = 514 #CAN Id has invalid bits set
  ERR_INVALID_FDFLAG_MODE20 = 515 #flag set that must not be set when configured for CAN20 (e.g. EDL)
  ERR_EDL_RTR = 516 #RTR must not be set in combination with EDL
  ERR_EDL_NOT_SET = 517 #EDL is not set but BRS and/or ESICTRL is
  ERR_UNKNOWN_FLAG = 518 #unknown bit in flags field is set
  ERR_ETH_PHY_ACTIVATION_FAILED = 4352
  ERR_ETH_PHY_CONFIG_ABORTED = 4355
  ERR_ETH_RESET_FAILED = 4356
  ERR_ETH_SET_CONFIG_DELAYED = 4357 #Requested config was stored but could not be immediately activated
  ERR_ETH_UNSUPPORTED_FEATURE = 4358 #Requested feature/function not supported by device
  ERR_ETH_MAC_ACTIVATION_FAILED = 4359
  ERR_NET_ETH_SWITCH_IS_ONLINE = 4364 #Switch has already been activated

class XL_EVENT_TYPE(IntEnum):
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
  RECEIVE_DAIO_DATA = 32 #D/A IO data message
  RECEIVE_DAIO_PIGGY = 34 #D/A IO Piggy data message
  KLINE_MSG = 36

class XL_EVENT_TAGS(IntEnum):
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
  RECEIVE_DAIO_DATA = 0x20 #D/A IO data message
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
  ETH_EVENT_TAG_FRAMERX = 1280 #Event data type T_XL_ETH_DATAFRAME_RX
  ETH_EVENT_TAG_FRAMERX_ERROR = 1281 #Event data type T_XL_ETH_DATAFRAME_RX_ERROR
  ETH_EVENT_TAG_FRAMETX_ERROR = 1286 #Event data type T_XL_ETH_DATAFRAME_TX_ERROR
  ETH_EVENT_TAG_FRAMETX_ERROR_SWITCH = 1287 #Event data type T_XL_ETH_DATAFRAME_TX_ERR_SW
  ETH_EVENT_TAG_FRAMETX_ACK = 1296 #Event data type T_XL_ETH_DATAFRAME_TXACK
  ETH_EVENT_TAG_FRAMETX_ACK_SWITCH = 1297 #Event data type T_XL_ETH_DATAFRAME_TXACK_SW
  ETH_EVENT_TAG_FRAMETX_ACK_OTHER_APP = 1299 #Event data type T_XL_ETH_DATAFRAME_TXACK_OTHERAPP
  ETH_EVENT_TAG_FRAMETX_ERROR_OTHER_APP = 1300 #Event data type T_XL_ETH_DATAFRAME_TX_ERR_OTHERAPP
  ETH_EVENT_TAG_CHANNEL_STATUS = 1312 #Event data type T_XL_ETH_CHANNEL_STATUS
  ETH_EVENT_TAG_CONFIGRESULT = 1328 #Event data type T_XL_ETH_CONFIG_RESULT
  ETH_EVENT_TAG_FRAMERX_SIMULATION = 1360 #Event data type T_XL_ETH_DATAFRAME_RX_SIMULATION  (with payload)
  ETH_EVENT_TAG_FRAMERX_ERROR_SIMULATION = 1361 #Event data type T_XL_ETH_DATAFRAME_RX_ERROR_SIMULATION (with payload)
  ETH_EVENT_TAG_FRAMETX_ACK_SIMULATION = 1362 #Event data type T_XL_ETH_DATAFRAME_TX_SIMULATION (with payload)
  ETH_EVENT_TAG_FRAMETX_ERROR_SIMULATION = 1363 #Event data type T_XL_ETH_DATAFRAME_TX_ERROR_SIMULATION (with payload)
  ETH_EVENT_TAG_FRAMERX_MEASUREMENT = 1376 #Event data type T_XL_ETH_DATAFRAME_RX_MEASUREMENT  (with payload)
  ETH_EVENT_TAG_FRAMERX_ERROR_MEASUREMENT = 1377 #Event data type T_XL_ETH_DATAFRAME_RX_ERROR_MEASUREMENT (with payload)
  ETH_EVENT_TAG_FRAMETX_MEASUREMENT = 1378 #Event data type T_XL_ETH_DATAFRAME_TX_MEASUREMENT (with payload)
  ETH_EVENT_TAG_FRAMETX_ERROR_MEASUREMENT = 1379 #Event data type T_XL_ETH_DATAFRAME_TX_ERROR_MEASUREMENT (with payload)
  ETH_EVENT_TAG_LOSTEVENT = 1534 #Indication that one or more intended events could not be generated. Event data type T_XL_ETH_LOSTEVENT
  ETH_EVENT_TAG_ERROR = 1535 #Generic error
  #ARINC429 event tags
  A429_EV_TAG_TX_OK = 1536
  A429_EV_TAG_TX_ERR = 1537
  A429_EV_TAG_RX_OK = 1544
  A429_EV_TAG_RX_ERR = 1545
  A429_EV_TAG_BUS_STATISTIC = 1551

class XL_NOTIFY_REASON(IntEnum):
  CHANNEL_ACTIVATION = 1
  CHANNEL_DEACTIVATION = 2
  PORT_CLOSED = 3

class XL_SYNC_PULSE(IntEnum):
  EXTERNAL = 0
  OUR = 1
  OUR_SHARED = 2

class XL_HWTYPE(IntEnum):
  NONE = 0
  VIRTUAL = 1
  CANCARDX = 2
  CANAC2PCI = 6
  CANCARDY = 12
  CANCARDXL = 15
  CANCASEXL = 21
  CANCASEXL_LOG_OBSOLETE = 23
  CANBOARDXL = 25 #CANboardXL, CANboardXL PCIe
  CANBOARDXL_PXI = 27 #CANboardXL pxi
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

class XL_CHANNEL_SELECTOR(IntEnum):
  INVALID_CHANNEL_INDEX = 4294967295 #0xFFFFFFFF
  INVALID_DEVICE_INDEX = 4294967295 #0xFFFFFFFF

class XL_LIN(IntEnum):
  MASTER = 1 #channel is a LIN master
  SLAVE = 2 #channel is a LIN slave
  VERSION_1_3 = 1 #LIN version 1.3
  VERSION_2_0 = 2 #LIN version 2.0
  VERSION_2_1 = 3 #LIN version 2.1
  CALC_CHECKSUM = 256 #flag for automatic 'classic' checksum calculation
  CALC_CHECKSUM_ENHANCED = 512 #flag for automatic 'enhanced' checksum calculation
  SET_SILENT = 1 #set hardware into sleep mode
  SET_WAKEUPID = 3 #set hardware into sleep mode and send a request at wake-up
  CHECKSUM_CLASSIC = 0 #Use classic CRC 
  CHECKSUM_ENHANCED = 1 #Use enhanced CRC
  CHECKSUM_UNDEFINED = 255 #Set the checksum calculation to undefined.
  STAYALIVE = 0 #flag if nothing changes
  SET_SLEEPMODE = 1 #flag if the hardware is set into the sleep mode
  COMESFROM_SLEEPMODE = 2 #flag if the hardware comes from the sleep mode
  WAKUP_INTERNAL = 1 #flag to signal a internal WAKEUP (event)
  UNDEFINED_DLC = 255 #set the DLC to undefined
  SLAVE_ON = 255 #switch on the LIN slave
  SLAVE_OFF = 0 #switch off the LIN slave

MAX_MSG_LEN = 8

class XL_INTERFACE_VERSION(IntEnum):
  V2 = 2
  V3 = 3
  V4 = 4
#Current Version
XL_CURRENT_INTERFACE_VERSION = XL_INTERFACE_VERSION.V3

XL_CAN_EXT_MSG_ID = 2147483648

class XL_CAN_MSG_FLAG(IntFlag):
  ERROR_FRAME = 1
  OVERRUN = 2 #Overrun in Driver or CAN Controller, previous msgs have been lost.
  NERR = 4 #Line Error on Lowspeed
  WAKEUP = 8 # #High Voltage Message on Single Wire CAN
  REMOTE_FRAME = 16
  RESERVED_1 = 32
  TX_COMPLETED = 64 #Message Transmitted
  TX_REQUEST = 128 #Transmit Message stored into Controller
  SRR_BIT_DOM = 512 #SRR bit in CAN message is dominant

XL_EVENT_FLAG_OVERRUN = 1 #Used in XLevent.flags

class XL_LIN_MSGFLAG(IntFlag):
  TX = XL_CAN_MSG_FLAG.TX_COMPLETED #LIN TX flag
  CRCERROR = 129 #Wrong LIN CRC

class XL_DAIO_DATA(IntEnum):
  GET = 32768
  VALUE_DIGITAL = 1
  VALUE_ANALOG = 2
  PWM = 16

class XL_DAIO_MODE(IntEnum):
  PULSE = 32 #generates pulse in values of PWM

class XL_CHIPSTAT(IntEnum):
  BUSOFF = 1
  ERROR_PASSIVE = 2
  ERROR_WARNING = 4
  ERROR_ACTIVE = 8

class XL_TRANSCEIVER_EVENT(IntEnum):
  NONE = 0
  INSERTED = 1 #cable was inserted
  REMOVED = 2 #cable was removed
  STATE_CHANGE = 3 #transceiver state changed

class XL_OUTPUT_MODE(IntEnum):
  SILENT = 0 #switch CAN trx into default silent mode
  XL_OUTPUT_MODE_NORMAL = 1 #switch CAN trx into normal mode
  XL_OUTPUT_MODE_TX_OFF = 2 #switch CAN trx into silent mode with tx pin off
  XL_OUTPUT_MODE_SJA_1000_SILENT = 3 #switch CAN trx into SJA1000 silent mode

class XL_TRANSCEIVER_MODE(IntEnum):
  EVENT_ERROR = 1
  EVENT_CHANGED = 2
#message name to acquire a unique message id from windows
DriverNotifyMessageName = "VectorCanDriverChangeNotifyMessage"

#build a channels mask from the channels index
XL_CHANNEL_MASK = lambda x: 1 << x

XL_MAX_APPNAME = 32

#defines for xlGetDriverConfig structures
XL_MAX_LENGTH = 31
XL_CONFIG_MAX_CHANNELS = 64
XL_MAX_NAME_LENGTH = 48

#defines for xlSet/GetApplConfig
XL_APPLCONFIG_MAX_CHANNELS = 256
class XL_ACTIVATE(IntEnum):
  NONE = 0
  RESET_CLOCK = 8 #using this flag with time synchronisation protocols supported by Vector Timesync Service is not recommended

class XL_BUS_COMPATIBLE(IntFlag):
  CAN      = XL_BUS_TYPE.CAN      #   1
  LIN      = XL_BUS_TYPE.LIN      #   2
  FLEXRAY  = XL_BUS_TYPE.FLEXRAY  #   4
  MOST     = XL_BUS_TYPE.MOST     #  16
  DAIO     = XL_BUS_TYPE.DAIO     #  64 #io cab/piggy
  J1708    = XL_BUS_TYPE.J1708    # 256
  KLINE    = XL_BUS_TYPE.KLINE    #2048
  ETHERNET = XL_BUS_TYPE.ETHERNET #4096
  A429     = XL_BUS_TYPE.A429     #8192

class XL_BUS_ACTIVE_CAP(IntFlag):
  CAN      = XL_BUS_COMPATIBLE.CAN      << 16 #    65536
  LIN      = XL_BUS_COMPATIBLE.LIN      << 16 #   131072
  FLEXRAY  = XL_BUS_COMPATIBLE.FLEXRAY  << 16 #   262144
  MOST     = XL_BUS_COMPATIBLE.MOST     << 16 #  1048576
  DAIO     = XL_BUS_COMPATIBLE.DAIO     << 16 #  4194304
  J1708    = XL_BUS_COMPATIBLE.J1708    << 16 # 16777216
  KLINE    = XL_BUS_COMPATIBLE.KLINE    << 16 #134217728
  ETHERNET = XL_BUS_COMPATIBLE.ETHERNET << 16 #268435456
  A429     = XL_BUS_COMPATIBLE.A429     << 16 #536870912

class XL_BUS_NAME(Enum):
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

class XL_ACCEPTANCE_FILTER(IntEnum):
  CAN_STD = 1 #flag for standard ID's
  CAN_EXT = 2 #flag for extended ID's

CANFD_CONFOPT_NO_ISO = 8 #configuration option CANFD-BOSCH

class XL_BUS_PARAMS_MOST_SPEED(IntEnum):
  GRADE_25 = 1
  GRADE_150 = 2

class XL_BUS_PARAMS_CANOPMODE(IntEnum):
  CAN20 = 1 #channel operates in CAN20
  CANFD = 2 #channel operates in CANFD
  CANFD_NO_ISO = 8 #channel operates in CANFD_NO_ISO

XL_INVALID_PORTHANDLE = -1

class XL_CONNECTION_INFO(IntEnum):
  FAMILY_MASK = 4278190080
  DETAIL_MASK = 16777215
  FAMILY_USB = 0 << 24 #USB devices
  FAMILY_NETWORK = 1 << 24 #Ethernet and WiFi devices
  FAMILY_PCIE = 2 << 24 #PCI-Express devices
  USB_UNKNOWN = 0
  USB_FULLSPEED = 1
  USB_HIGHSPEED = 2
  USB_SUPERSPEED = 3

class XL_FPGA_CORE_TYPE(IntEnum):
  NONE = 0
  CAN = 1
  LIN = 2
  LIN_RX = 3
XL_SPECIAL_DEVICE_STAT_FPGA_UPDATE_DONE = 1 #automatic driver FPGA flashing done

class XL_DAIO_DIGITAL(IntEnum):
  ENABLED = 1 #digital port is enabled
  INPUT = 2 #digital port is input, otherwise it is an output
  TRIGGER = 4 #digital port is trigger

class XL_DAIO_ANALOG(IntEnum):
  ENABLED = 1 #analog port is enabled
  INPUT = 2 #analog port is input, otherwise it is an output
  TRIGGER = 4 #analog port is trigger
  RANGE_32V = 8 #analog port is in range 0..32,768V, otherwise 0..8,192V

class XL_DAIO_TRIGGER_MODE(IntEnum):
  NONE = 0 #no trigger configured
  DIGITAL = 1 #trigger on preconfigured digital lines
  ANALOG_ASCENDING = 2 #trigger on input 3 ascending
  ANALOG_DESCENDING = 4 #trigger on input 3 descending
  ANALOG = ANALOG_ASCENDING|ANALOG_DESCENDING #trigger on input
XL_DAIO_TRIGGER_LEVEL_NONE = 0 #no trigger level is defined
XL_DAIO_POLLING_NONE = 0 #periodic measurement is disabled

class XL_SET_TIMESYNC(IntEnum):
  NO_CHANGE = 0
  ON = 1
  OFF = 2

MOST_ALLOC_TABLE_SIZE = 64 #size of channel alloctaion table + 4Bytes (MPR, MDR; ?, ?)
XL_IPv4 = 4
XL_IPv6 = 6
XL_MAX_REMOTE_DEVICE_INFO = 16
XL_ALL_REMOTE_DEVICES = 4294967295
XL_MAX_REMOTE_ALIAS_SIZE = 64

class  XL_REMOTE(IntEnum):
  OFFLINE = 1
  ONLINE = 2
  BUSY = 3
  CONNECION_REFUSED = 4

class  XL_REMOTE_ADD(IntEnum):
  PERMANENT = 0
  TEMPORARY = 1

class  XL_REMOTE_REGISTER(IntEnum):
  NONE = 0
  CONNECT = 1
  TEMP_CONNECT = 2

class  XL_REMOTE_DISCONNECT(IntEnum):
  NONE = 0
  REMOVE_ENTRY = 1

class  XL_REMOTE_DEVICE(IntEnum):
  AVAILABLE = 1 #the device is present
  CONFIGURED = 2 #the device has a configuration entry in registry
  CONNECTED = 4 #the device is connected to this client
  ENABLED = 8 #the driver should open a connection to this client
  BUSY = 16 #the device is used by another client
  TEMP_CONFIGURED = 32 #the device is temporary configured, it has not entry in registry
  STATUS_MASK = 63
  NO_NET_SEARCH = 0
  NET_SEARCH = 1

class  XL_REMOTE_DEVICE_TYPE(IntEnum):
  UNKNOWN = 0
  VN8900 = 1
  STANDARD_PC = 2
  VX = 3 #VX hardware
  VN8800 = 4
  VN = 5 #VN network interfaces
  VT = 6 #VT hardware

XL_CHANNEL_FLAG_EX_MASK = lambda n: 1 << n
#Flags for channelCapabilities
class  XL_CHANNEL_FLAG(IntFlag):
  TIME_SYNC_RUNNING = 1
  NO_HWSYNC_SUPPORT = 1024 #Device is not capable of hardware-based time synchronization via Sync-line 
  SPDIF_CAPABLE = 16384 #used to distinguish between VN2600 (w/o SPDIF) and VN2610 (with S/PDIF)
  CANFD_BOSCH_SUPPORT = 536870912
  CMACTLICENSE_SUPPORT = 1073741824
  CANFD_ISO_SUPPORT = 2147483648
  EX1_TIME_SYNC_RUNNING = XL_CHANNEL_FLAG_EX_MASK(0)
  EX1_HWSYNC_SUPPORT = XL_CHANNEL_FLAG_EX_MASK(4)
  EX1_CANFD_ISO_SUPPORT = XL_CHANNEL_FLAG_EX_MASK(10)
  EX1_SPDIF_CAPABLE = XL_CHANNEL_FLAG_EX_MASK(20)
  EX1_CANFD_BOSCH_SUPPORT = XL_CHANNEL_FLAG_EX_MASK(35)
  #Ethernet device operates in network-based instead of channel-based mode
  EX1_NET_ETH_SUPPORT = XL_CHANNEL_FLAG_EX_MASK(36)

class XL_MOST_SOURCE(IntEnum):
  """Defines for xlMostSwitchEventSources"""
  ASYNC_SPY = 32768
  ASYNC_RX = 4096
  ASYNC_TX = 2048
  CTRL_OS8104A = 1024
  CTRL_SPY = 256
  ALLOC_TABLE = 128
  SYNC_RC_OVER = 64
  SYNC_TX_UNDER = 32
  SYNCLINE = 16
  ASYNC_RX_FIFO_OVER = 8

class XL_MOST_ERROR(IntEnum):
  OS8104_TX_LOCK_ERROR = 1
  OS8104_SPDIF_LOCK_ERROR = 2
  OS8104_ASYNC_BUFFER_FULL = 3
  OS8104_ASYNC_CRC_ERROR = 4
  ASYNC_TX_UNDERRUN = 5
  CTRL_TX_UNDERRUN = 6
  MCU_TS_CMD_QUEUE_UNDERRUN = 7
  MCU_TS_CMD_QUEUE_OVERRUN = 8
  CMD_TX_UNDERRUN = 9
  SYNCPULSE_ERROR = 10
  OS8104_CODING_ERROR = 11
  ERROR_UNKNOWN_COMMAND = 12
  ASYNC_RX_OVERFLOW_ERROR = 13
  FPGA_TS_FIFO_OVERFLOW = 14
  SPY_OVERFLOW_ERROR = 15
  CTRL_TYPE_QUEUE_OVERFLOW = 16
  ASYNC_TYPE_QUEUE_OVERFLOW = 17
  CTRL_UNKNOWN_TYPE = 18
  CTRL_QUEUE_UNDERRUN = 19
  ASYNC_UNKNOWN_TYPE = 20
  ASYNC_QUEUE_UNDERRUN = 21

XL_MOST_DEMANDED_START = 1 #data for demanded timstamps
XL_MOST_RX_DATA_SIZE = 1028
XL_MOST_TS_DATA_SIZE = 12
XL_MOST_RX_ELEMENT_HEADER_SIZE = 32
XL_MOST_CTRL_RX_SPY_SIZE = 36
XL_MOST_CTRL_RX_OS8104_SIZE = 28
XL_MOST_SPECIAL_REGISTER_CHANGE_SIZE = 20
XL_MOST_ERROR_EV_SIZE_4 = 4
XL_MOST_ERROR_EV_SIZE = 16

class XL_MOST_DEVICE(IntEnum):
  """defines for the audio devices"""
  CASE_LINE_IN = 0
  CASE_LINE_OUT = 1
  SPDIF_IN = 7
  SPDIF_OUT = 8
  SPDIF_IN_OUT_SYNC = 11

class XL_MOST_SPDIF(IntEnum):
  """defines for xlMostCtrlSyncAudioEx, mode"""
  LOCK_OFF = 0
  LOCK_ON = 1

class XL_MOST_SYNC_MUTES_STATUS(IntEnum):
  """defines for the XL_MOST_SYNC_MUTES_STATUS event"""
  NO_MUTE = 0
  MUTE = 1

class XL_MOST_EVENT_SOURCE(IntEnum):
  """defines for the event sources in XLmostEvent"""
  XL_MOST_VN2600 = 1
  XL_MOST_OS8104A = 2
  XL_MOST_OS8104B = 4
  XL_MOST_SPY = 8

class XL_MOST_MODE(IntEnum):
  """defines for xlMostSetAllBypass and XL_MOST_ALLBYPASS"""
  DEACTIVATE = 0
  ACTIVATE = 1
  FORCE_DEACTIVATE = 2

XL_MOST_RX_BUFFER_CLEAR_ONCE = 2

class XL_MOST_TIMING(IntEnum):
  """defines for xlMostSetTimingMode and the XL_MOST_TIMINGMODE(_SPDIF)_EV event."""
  SLAVE = 0
  MASTER = 1
  SLAVE_SPDIF_MASTER = 2
  SLAVE_SPDIF_SLAVE = 3
  MASTER_SPDIF_MASTER = 4
  MASTER_SPDIF_SLAVE = 5
  MASTER_FROM_SPDIF_SLAVE = 6

class XL_MOST_FREQUENCY(IntEnum):
  """defines for xlMostSetFrequency and the XL_MOST_FREQUENCY_EV event."""
  FREQUENCY_44100 = 0
  FREQUENCY_48000 = 1
  FREQUENCY_ERROR = 2

class XL_MOST_LIGHT(IntEnum):
  """defines for xlMostSetTxLight"""
  OFF = 0
  FORCE_ON = 1 #unmodulated on
  MODULATED = 2 #modulated light
  #xlMostSetTxLightPower
  FULL = 100
  LIGHT_3DB = 50

class XL_MOST_LOCKSTATUS(IntEnum):
  """defines for the XL_MOST_LOCKSTATUS event"""
  UNLOCK = 5
  LOCK = 6
  STATE_UNKNOWN = 9

class XL_MOST_CTRL_RX_OS8104(IntEnum):
  """defines for the XL_MOST_CTRL_RX_OS8104 event (tx event)"""
  TX_WHILE_UNLOCKED = 2147483648
  TX_TIMEOUT = 1073741824
  DIRECTION_RX = 0
  DIRECTION_TX = 1
  NO_QUEUE_OVERFLOW = 0 #No rx-queue overflow occured
  QUEUE_OVERFLOW = 32768 #Overflow of rx-queue in firmware when trying to add a rx-event
  COMMAND_FAILED = 16384
  INTERNAL_OVERFLOW = 8192 #Overflow of command-timestamp-queue in firmware
  MEASUREMENT_NOT_ACTIVE = 4096
  QUEUE_OVERFLOW_ASYNC = 2048 #Overflow of async rx-queue in firmware when trying to add a packet
  QUEUE_OVERFLOW_CTRL = 1024 #Overflow of rx-queue in firmware when trying to add a message
  NOT_SUPPORTED = 512
  QUEUE_OVERFLOW_DRV = 256 #Overflow occured when trying to add an event to application rx-queue
  NA_CHANGED = 1 #node address changed
  GA_CHANGED = 2 #group address changed
  APA_CHANGED = 4 #alternative packet address changed
  NPR_CHANGED = 8 #node position register changed
  MPR_CHANGED = 16 #max position register changed
  NDR_CHANGED = 32 #node delay register changed
  MDR_CHANGED = 64 #max delay register changed
  SBC_CHANGED = 128
  XTIM_CHANGED = 256
  XRTY_CHANGED = 512

class XL_MOST_REGISTER(IntEnum):
  """defines for the MOST register (xlMostWriteRegister)"""
  bGA = 137 #Group Address
  bNAH = 138 #Node Address High
  bNAL = 139 #Node Address Low
  bSDC2 = 140 #Source Data Control 2
  bSDC3 = 141 #Source Data Control 3
  bCM2 = 142 #Clock Manager 2
  bNDR = 143 #Node Delay
  bMPR = 144 #Maximum Position
  bMDR = 145 #Maximum Delay
  bCM4 = 147 #Clock Manager 4
  bSBC = 150 #Synchronous Bandwidth Control
  bXSR2 = 151 #Transceiver Status 2
  bRTYP = 160 #Receive Message Type
  bRSAH = 161 #Source Address High
  bRSAL = 162 #Source Address Low
  bRCD0 = 163 #Receive Control Data 0 --> bRCD16 = bRCD0+16
  bXTIM = 190 #Transmit Retry Time
  bXRTY = 191 #Transmit Retries
  bXPRI = 192 #Transmit Priority
  bXTYP = 193 #Transmit Message Type
  bXTAH = 194 #Target Address High
  bXTAL = 195 #Target Address Low
  bXCD0 = 196 #Transmit Control Data 0 --> bXCD16 = bXCD0+16
  bXTS = 213 #Transmit Transfer Status
  bPCTC = 226 #Packet Control
  bPCTS = 227 #Packet Status

class XL_MOST_SPY_RX_STATUS(IntEnum):
  NO_LIGHT = 1
  NO_LOCK = 2
  BIPHASE_ERROR = 4
  MESSAGE_LENGTH_ERROR = 8
  PARITY_ERROR = 16
  FRAME_LENGTH_ERROR = 32
  PREAMBLE_TYPE_ERROR = 64
  CRC_ERROR = 128

class XL_MOST_ASYNC(IntEnum):
  """defines for status of async frames"""
  NO_ERROR = 0
  SBC_ERROR = 12
  NEXT_STARTS_TO_EARLY = 13
  TO_LONG = 14
  UNLOCK = 15 #unlock occured within receiption of packet

class XL_MOST_SYNC_PULSE(IntEnum):
  """defines for XL_MOST_SYNC_PULSE_EV member trigger_source"""
  EXTERNAL = 0
  OUR = 1

class XL_MOST_CTRL_TYPE(IntEnum):
  """ctrlType value within the XL_CTRL_SPY event"""
  NORMAL = 0
  REMOTE_READ = 1
  REMOTE_WRITE = 2
  RESOURCE_ALLOCATE = 3
  RESOURCE_DEALLOCATE = 4
  GET_SOURCE = 5

class XL_MOST_BUSLOAD_COUNTER(IntEnum):
  """counterType for the xlMost****GenerateBusload function"""
  TYPE_NONE = 0
  TYPE_1_BYTE = 1
  TYPE_2_BYTE = 2
  TYPE_3_BYTE = 3
  TYPE_4_BYTE = 4

class XL_MOST_STATESEL(IntFlag):
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

class XL_MOST_STREAM(IntEnum):
  RX_DATA = 0 #RX streaming: MOST -> PC
  TX_DATA = 1 #TX streaming: PC -> MOST
  ADD_FRAME_HEADER = 1 #only for RX: additionally the orig. TS + status information are reported

class XL_MOST_STREAM_STATE(IntEnum):
  CLOSED = 1
  OPENED = 2
  STARTED = 3
  STOPPED = 4
  START_PENDING = 5 #waiting for result from hw
  STOP_PENDING = 6 #waiting for result from hw
  UNKNOWN = 255

class XL_MOST_STREAM_MODE(IntEnum):
  ACTIVATE = 0
  DEACTIVATE = 1

XL_MOST_STREAM_INVALID_HANDLE = 0

class XL_MOST_STREAM_LATENCY(IntEnum):
  VERY_LOW = 0
  LOW = 1
  MEDIUM = 2
  HIGH = 3
  VERY_HIGH = 4

class XL_MOST_STREAM_ERR(IntEnum):
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

XL_MOST_EVENT_HEADER_SIZE = 32
XL_MOST_EVENT_MAX_DATA_SIZE = 1024
XL_MOST_EVENT_MAX_SIZE = 1056

### FlexRay XL API ###

XL_FR_MAX_DATA_LENGTH = 254

class XL_FR_CHANNEL_CFG_STATUS(IntFlag):
  INIT_APP_PRESENT = 1
  CHANNEL_ACTIVATED = 2
  VALID_CLUSTER_CFG = 4
  VALID_CFG_MODE = 8

class XL_FR_CHANNEL_CFG_MODE(IntEnum):
  SYNCHRONOUS = 1
  COMBINED = 2
  ASYNCHRONOUS = 3

class XL_FR_MODE(IntEnum):
  NORMAL = 0 #setup the VN3000 (eRay) normal operation mode. (default mode)
  COLD_NORMAL = 4 #setup the VN3000 (Fujitsu) normal operation mode. (default mode)

class XL_FR_MODE_STARTUP(IntEnum):
  NONE = 0 #for normal use
  WAKEUP = 1 #for wakeup
  COLDSTART_LEADING = 2 #Coldstart path initiating the schedule synchronization
  COLDSTART_FOLLOWING = 3 #Coldstart path joining other coldstart nodes
  WAKEUP_AND_COLDSTART_LEADING = 4 #Send Wakeup and Coldstart path initiating the schedule synchronization
  WAKEUP_AND_COLDSTART_FOLLOWING = 5 #Send Wakeup and Coldstart path joining other coldstart nodes

class XL_FR_SYMBOL(IntEnum):
  MTS = 1 #defines a MTS (Media Access Test Symbol)
  CAS = 2 #defines a CAS (Collision Avoidance Symbol)

class XL_FR_TRANSCEIVER_MODE(IntEnum):
  SLEEP = 1
  NORMAL = 2
  RECEIVE_ONLY = 3
  STANDBY = 4

class XL_FR_SYNC_PULSE(IntEnum):
  EXTERNAL = XL_SYNC_PULSE.EXTERNAL
  OUR = XL_SYNC_PULSE.OUR
  OUR_SHARED = XL_SYNC_PULSE.OUR_SHARED

XL_FR_SPY_MODE_ASYNCHRONOUS = 1

class XL_FR_FILTER_STATUS(IntEnum):
  PASS = 0 #maching frame passes the filter
  BLOCK = 1 #maching frame is blocked

class XL_FR_FILTER_TYPE(IntEnum):
  DATA = 1 #specifies a data frame
  NF = 2 #specifies a null frame in an used cycle
  FILLUP_NF = 4 #specifies a null frame in an unused cycle

class XL_FR_FILTER_CHANNEL(IntEnum):
  A = 1 #specifies FlexRay channel A for the PC
  B = 2 #specifies FlexRay channel B for the PC

class XL_FR_FLAGS_CHIP(IntFlag):
  CHANNEL_A = 1
  CHANNEL_B = 2
  CHANNEL_AB = CHANNEL_A|CHANNEL_B # 3
  CC_COLD_A = 4 #second CC channel A to initiate the coldstart
  CC_COLD_B = 8 #second CC channel B to initiate the coldstart
  CC_COLD_AB = CC_COLD_A|CC_COLD_B # 12
  SPY_CHANNEL_A = 16 #Spy mode flags
  SPY_CHANNEL_B = 32 #Spy mode flags

XL_FR_QUEUE_OVERFLOW = 256 #driver queue overflow

class XL_FR_FRAMEFLAG(IntEnum):
  STARTUP = 1 #indicates a startup frame
  SYNC = 2 #indicates a sync frame
  NULLFRAME = 4 #indicates a null frame
  PAYLOAD_PREAMBLE = 8 #indicates a present payload preamble bit
  FR_RESERVED = 16 #reserved by Flexray protocol
  REQ_TXACK = 32 #used for Tx events only
  TXACK_SS = REQ_TXACK #indicates TxAck of SingleShot; used for TxAck events only
  RX_UNEXPECTED = REQ_TXACK #indicates unexpected Rx frame; used for Rx events only
  NEW_DATA_TX = 64 #flag used with TxAcks to indicate first TxAck after data update
  DATA_UPDATE_LOST = 128 #flag used with TxAcks indicating that data update has been lost
  SYNTAX_ERROR = 512
  CONTENT_ERROR = 1024
  SLOT_BOUNDARY_VIOLATION = 2048
  TX_CONFLICT = 4096
  EMPTY_SLOT = 8192
  FRAME_TRANSMITTED = 32768 #Only used with TxAcks: Frame has been transmitted. If not set after transmission, an error has occurred.

class XL_FR_SPY_FRAMEFLAG_ERROR(IntEnum):
  FRAMING_ERROR = 1
  HEADER_CRC_ERROR = 2
  FRAME_CRC_ERROR = 4
  BUS_ERROR = 8

class XL_FR_SPY_FRAMEFLAG_FRAME_CRC(IntEnum):
  NEW_LAYOUT = 2147483648

class XL_FR_SPY_FRAMEFLAG_FRAME_FLAGS(IntEnum):
  STATIC_FRAME = 1

class XL_FR_TX_MODE(IntEnum):
  CYCLIC = 1 #'normal' cyclic mode
  SINGLE_SHOT = 2 #sends only a single shot
  NONE = 255 #switch off TX

class XL_FR_PAYLOAD_INCREMENT(IntEnum):
  INCREMENT_8BIT = 8
  INCREMENT_16BIT = 16
  INCREMENT_32BIT = 32
  INCREMENT_NONE = 0

class XL_FR_STATUS(IntEnum):
  DEFAULT_CONFIG = 0 #indicates the actual state of the POC in operation control
  READY = 1
  NORMAL_ACTIVE = 2
  NORMAL_PASSIVE = 3
  HALT = 4
  MONITOR_MODE = 5
  CONFIG = 15
  WAKEUP_STANDBY = 16 #indicates the actual state of the POC in the wakeup path
  WAKEUP_LISTEN = 17
  WAKEUP_SEND = 18
  WAKEUP_DETECT = 19
  STARTUP_PREPARE = 32 #indicates the actual state of the POC in the startup path
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

class XL_FR_ERROR_POC(IntEnum):
  ACTIVE = 0 #Indicates the actual error mode of the POC: active (green)
  PASSIVE = 1 #Indicates the actual error mode of the POC: passive (yellow)
  COMM_HALT = 2 #Indicates the actual error mode of the POC: comm-halt (red)

class XL_FR_ERROR_NIT(IntEnum):
  SENA = 256 #Syntax Error during NIT Channel A
  SBNA = 512 #Slot Boundary Violation during NIT Channel A
  SENB = 1024 #Syntax Error during NIT Channel B
  SBNB = 2048 #Slot Boundary Violation during NIT Channel B

class XL_FR_ERROR_CLOCK(IntEnum):
  MISSING_OFFSET_CORRECTION = 1 #Set if no sync frames were received. -> no offset correction possible.
  MAX_OFFSET_CORRECTION_REACHED = 2 #Set if max. offset correction limit is reached.
  MISSING_RATE_CORRECTION = 4 #Set if no even/odd sync frames were received -> no rate correction possible.
  MAX_RATE_CORRECTION_REACHED = 8 #Set if max. rate correction limit is reached.

class XL_FR_ERROR_CC(IntEnum):
  PERR = 64 #Parity Error, data from MHDS (internal ERay error)
  IIBA = 512 #Illegal Input Buffer Access (internal ERay error)
  IOBA = 1024 #Illegal Output Buffer Access (internal ERay error)
  MHF = 2048 #Message Handler Constraints Flag data from MHDF (internal ERay error)
  EDA = 65536 #Error Detection on channel A, data from ACS
  LTVA = 131072 #Latest Transmit Violation on channel A
  TABA = 262144 #Transmit Across Boundary on Channel A
  EDB = 16777216 #Error Detection on channel B, data from ACS
  LTVB = 33554432 #Latest Transmit Violation on channel B
  TABB = 67108864 #Transmit Across Boundary on Channel B

class XL_FR_WAKEUP(IntEnum):
  UNDEFINED = 0 #No wakeup attempt since CONFIG state was left. (e.g. when a wakeup pattern A|B is received)
  RECEIVED_HEADER = 1 #Frame header without coding violation received.
  RECEIVED_WUP = 2 #Wakeup pattern on the configured wakeup channel received.
  COLLISION_HEADER = 3 #Detected collision during wakeup pattern transmission received.
  COLLISION_WUP = 4 #Collision during wakeup pattern transmission received.
  COLLISION_UNKNOWN = 5 #Set when the CC stops wakeup.
  TRANSMITTED = 6 #Completed the transmission of the wakeup pattern.
  EXTERNAL_WAKEUP = 7 #wakeup comes from external
  WUP_RECEIVED_WITHOUT_WUS_TX = 16 #wakeupt pattern received from flexray bus
  RESERVED = 255 #

class XL_FR_SYMBOL_STATUS(IntEnum):
  SESA = 1 #Syntax Error in Symbol Window Channel A
  SBSA = 2 #Slot Boundary Violation in Symbol Window Channel A
  TCSA = 4 #Transmission Conflict in Symbol Window Channel A
  SESB = 8 #Syntax Error in Symbol Window Channel B
  SBSB = 16 #Slot Boundary Violation in Symbol Window Channel B
  TCSB = 32 #Transmission Conflict in Symbol Window Channel B
  MTSA = 64 #MTS received in Symbol Window Channel A
  MTSB = 128 #MTS received in Symbol Window Channel B

XL_FR_RX_EVENT_HEADER_SIZE = 32
XL_FR_MAX_EVENT_SIZE = 512

### IO XL API ###

class XL_DAIO_PORT_TYPE_MASK(IntEnum):
  DIGITAL = 1
  ANALOG = 2

class XL_DAIO_TRIGGER_MODE(IntEnum):
  CYCLIC = 1
  PORT = 2

class XL_DAIO_TRIGGER_TYPE(IntEnum):
  RISING = 1
  FALLING = 2
  BOTH = 3

class XL_DAIO_PORT_DIGITAL(IntEnum):
  IN = 0
  PUSHPULL = 1
  OPENDRAIN = 2
  SWITCH = 5 #(only for digital pin 4..7)
  IN_OUT = 6 #(only for WakeUp line)

class XL_DAIO_PORT_ANALOG(IntEnum):
  IN = 0
  OUT = 1
  DIFF = 2
  OFF = 3

class XL_DAIO_DO_LEVEL(IntEnum):
  LEVEL_0V = 0
  LEVEL_5V = 5
  LEVEL_12V = 12

class XL_DAIO_PORT_MASK_DIGITAL(IntEnum):
  D0 = 1
  D1 = 2
  D2 = 4
  D3 = 8
  D4 = 16
  D5 = 32
  D6 = 64
  D7 = 128

class XL_DAIO_PORT_MASK_ANALOG(IntEnum):
  A0 = 1
  A1 = 2
  A2 = 4
  A3 = 8

class XL_DAIO_EVT_ID(IntEnum):
  XL_DAIO_EVT_ID_DIGITAL = XL_DAIO_PORT_TYPE_MASK.DIGITAL #1
  XL_DAIO_EVT_ID_ANALOG  = XL_DAIO_PORT_TYPE_MASK.ANALOG  #2

### K-Line XL API ###

class XL_KLINE_EVT(IntEnum):
  """K-Line event tags"""
  RX_DATA = 1
  TX_DATA = 2
  TESTER_5BD = 3
  ECU_5BD = 5
  TESTER_FI_WU_PATTERN = 7
  ECU_FI_WU_PATTERN = 8
  ERROR = 9
  CONFIRMATION = 10

class XL_KLINE_UART_PARITY(IntEnum):
  """defines for xlKlineSetUartParams"""
  NONE = 0
  EVEN = 1
  ODD = 2
  MARK = 3
  SPACE = 4

class XL_KLINE_TRXMODE(IntEnum):
  """defines for xlKlineSwitchHighspeedMode"""
  NORMAL = 0
  HIGHSPEED = 1

class XL_KLINE_TESTERRESISTOR(IntEnum):
  """defines for xlKlineSwitchTesterResistor"""
  OFF = 0
  ON = 1

XL_KLINE_UNCONFIGURE_ECU = 0
XL_KLINE_CONFIGURE_ECU = 1

class XL_KLINE_EVT_TAG_5BD(IntEnum):
  """event defines 5bdTag"""
  ADDR = 1
  BAUDRATE = 2
  KB1 = 3
  KB2 = 4
  KB2NOT = 5
  ADDRNOT = 6

class XL_KLINE_BYTE_ERROR_MASK(IntEnum):
  """defines for the tx/rx byte error mask"""
  FRAMING_ERROR_MASK = 1
  PARITY_ERROR_MASK = 2

class XL_KLINE_EVT_TAG(IntEnum):
  """defines for confirmation event"""
  SET_COMM_PARAM_TESTER = 1
  COMM_PARAM_ECU = 2
  SWITCH_HIGHSPEED = 3

class XL_KLINE_FLAG(IntEnum):
  """"""
  TAKE_KB2NOT = 2147483648
  TAKE_ADDRNOT = 2147483648

class XL_KLINE_ERROR_TYPE(IntEnum):
  """defines for T_KLINE_ERROR - errorType"""
  TYPE_RXTX_ERROR = 1
  TYPE_5BD_TESTER = 2
  TYPE_5BD_ECU = 3
  TYPE_IBS = 4
  TYPE_FI = 5

class XL_KLINE_ERR_RXTX(IntEnum):
  """defines for XL_KLINE_ERROR_TYPE_RXTX_ERROR / XL_KLINE_ERROR_TYPE_FI"""
  UA = 4 #unexpected activity
  MA = 2 #missing activity
  ISB = 1 #invalid sync byte

class XL_KLINE_ERR_TESTER(IntEnum):
  """defines for XL_KLINE_ERROR_TYPE_5BD_TESTER"""
  W1MIN = 1
  W1MAX = 2
  W2MIN = 3
  W2MAX = 4
  W3MIN = 5
  W3MAX = 6
  W4MIN = 7
  W4MAX = 8

class XL_KLINE_ERR_ECU(IntEnum):
  """defines for XL_KLINE_ERROR_TYPE_5BD_ECU"""
  W4MIN = 1
  W4MAX = 2

class XL_KLINE_ERR_IBS(IntEnum):
  """defines for XL_KLINE_ERROR_TYPE_IBS"""
  P1 = 1
  P4 = 2

### Ethernet API ###

XL_ETH_EVENT_SIZE_HEADER = 32
XL_ETH_EVENT_SIZE_MAX = 2048
XL_ETH_RX_FIFO_QUEUE_SIZE_MAX = 67108864 #Maximum size of ethernet receive queue: 64 MByte
XL_ETH_RX_FIFO_QUEUE_SIZE_MIN = 65536 #Minimum size of ethernet receive queue: 64 KByte
XL_ETH_PAYLOAD_SIZE_MAX = 1500 #maximum payload length for sending an ethernet packet
XL_ETH_PAYLOAD_SIZE_MIN = 46 #minimum payload length for sending an ethernet packet (42 octets with VLAN tag present)
XL_ETH_RAW_FRAME_SIZE_MAX = 1600 #maximum buffer size for storing a "raw" Ethernet frame (including VLAN tags, if present)
XL_ETH_RAW_FRAME_SIZE_MIN = 24 #minimum buffer size for storing a "raw" Ethernet frame (including VLAN tags, if present)
XL_ETH_MACADDR_OCTETS = 6
XL_ETH_ETHERTYPE_OCTETS = 2
XL_ETH_VLANTAG_OCTETS = 4

class XL_ETH_CHANNEL_CAP(IntEnum):
  IEEE100T1 = 1 #Channel supports IEEE 802.3pw (100BASE-T1) - Automotive Ethernet over single twisted pair
  IEEE100TX = 2 #Channel supports IEEE 802.3u (100-BASE-TX) and 802.3i (10BASE-T) - Ethernet and Fast Ethernet
  IEEE1000T = 4 #Channel supports IEEE 802.3ab (1000BASE-T) - Gigabit Ethernet
  IEEE1000T1 = 8 #Channel supports IEEE 802.3bp (1000BASE-T1) - Automotive Ethernet over single twisted pair

class XL_NET_ETH_SWITCH_CAP(IntEnum):
  REALSWITCH = 0 #Switch type is "normal" switch (learning is on)
  DIRECTCONN = 1 #Switch type is direct connection
  TAP_LINK = 2 #Switch type is TAP

class XL_ETH_FLAGS_CHIP(IntEnum):
  CONNECTOR_RJ45 = 1
  CONNECTOR_DSUB = 2
  PHY_IEEE = 4
  PHY_BROADR = 8
  FRAME_BYPASSED = 16 #For Rx and RxError events
  QUEUE_OVERFLOW = 256
  BYPASS_QUEUE_OVERFLOW = 32768 #MAC bypass queue full condition occurred, one or more packets dropped

class XL_ETH_MODE_SPEED(IntEnum):
  AUTO_100 = 2 #Set connection speed set to 100 Mbps via auto-negotiation
  AUTO_1000 = 4 #Set connection speed to 1000 Mbps via auto-negotiation
  AUTO_100_1000 = 5 #Set connection speed automatically to either 100 or 1000 Mbps
  FIXED_100 = 8 #Set connection speed to 100 Mbps. Auto-negotiation disabled.
  FIXED_1000 = 9 #Set connection speed to 1 Gbps. Auto-negotiation disabled.

class XL_ETH_MODE_DUPLEX(IntEnum):
  DONT_CARE = 0 #Used for BroadR-Reach since only full duplex mode possible.
  AUTO = 1 #Duplex mode set via auto-negotiation. Requires connection speed set to an "auto" value. Only for IEEE 802.3
  FULL = 3 #Full duplex mode. Only for IEEE 802.3

class XL_ETH_MODE_CONNECTOR(IntEnum):
  DONT_CARE = 0 #Apart from VN5610(A), always only one connector available anyway
  RJ45 = 1 #Using RJ-45 connector
  DSUB = 2 #Using D-Sub connector

class XL_ETH_MODE_PHY(IntEnum):
  DONT_CARE = 0 #Set whatever PHY layer is available
  IEEE_802_3 = 1 #Set IEEE 802.3
  BROADR_REACH = 2 #Set BroadR-Reach

class XL_ETH_MODE_CLOCK(IntEnum):
  DONT_CARE = 0 #Used for IEEE 802.3 100 and 10 MBit
  AUTO = 1 #Clock mode set automatically via auto-negotiation. Only for 1000Base-T if speed mode is one of the "auto" modes
  MASTER = 2 #Clock mode is master. Only for 1000Base-T or BroadR-Reach
  SLAVE = 3 #Clock mode is slave. Only for 1000Base-T or BroadR-Reach

class XL_ETH_MODE_MDI(IntEnum):
  AUTO = 1 #Perform MDI auto detection
  STRAIGHT = 2 #Direct MDI (connected to switch)
  CROSSOVER = 3 #Crossover MDI (connected to endpoint)

class XL_ETH_MODE_BR_PAIR(IntEnum):
  DONT_CARE = 0 #Used for IEEE 802.3
  BR_1PAIR = 1 #BR 1-pair connection. Only for BroadR-Reach

class XL_ETH_STATUS_LINK(IntEnum):
  UNKNOWN = 0 #The link state could not be determined (e.g. lost connection to board)
  DOWN = 1 #Link is down (no cable attached, no configuration set, configuration does not match)
  UP = 2 #Link is up
  ERROR = 4 #Link is in error state (e.g. auto-negotiation failed)

class XL_ETH_STATUS_SPEED(IntEnum):
  UNKNOWN = 0 #Connection speed could not be determined (e.g. during auto-negotiation or if link down)
  SPEED_10 = 1 #Link speed is 10 Mbps
  SPEED_100 = 2 #Link speed is 100 Mbps
  SPEED_1000 = 3 #Link speed is 1000 Mbps
  SPEED_2500 = 4 #Link speed is 2500 Mbps
  SPEED_5000 = 5 #Link speed is 5000 Mbps
  SPEED_10000 = 6 #Link speed is 10000 Mbps

class XL_ETH_STATUS_DUPLEX(IntEnum):
  UNKNOWN = 0 #Duplex mode could not be determined (e.g. during auto-negotiation or if link down)
  FULL = 2 #Full duplex mode

class XL_ETH_STATUS_MDI(IntEnum):
  UNKNOWN = 0 #MDI mode could not be determined  (e.g. during auto-negotiation or if link down)
  STRAIGHT = 1 #Direct MDI
  CROSSOVER = 2 #Crossover MDI

class XL_ETH_STATUS_CONNECTOR(IntEnum):
  DEFAULT = 0 #Using the only available connector on channel
  RJ45 = 1 #Using RJ-45 connector
  DSUB = 2 #Using D-Sub connector

class XL_ETH_STATUS_PHY(IntEnum):
  UNKNOWN = 0 #PHY is currently unknown (e.g. if link is down)
  IEEE_802_3 = 1 #PHY is IEEE 802.3
  BROADR_REACH = 2 #PHY is BroadR-Reach
  PHY_100BASE_T1 = 2 #PHY is IEEE  100BASE-T1 (802.3bw) - intentionally same value as BroadR-Reach 100Bit
  PHY_1000BASE_T1 = 4 #PHY is IEEE 1000BASE-T1 (802.3bp)

class XL_ETH_STATUS_CLOCK(IntEnum):
  DONT_CARE = 0 #Clock mode not relevant. Only for IEEE 802.3 100/10 MBit
  MASTER = 1 #Clock mode is master. Only for 1000Base-T or BroadR-Reach
  SLAVE = 2 #Clock mode is slave. Only for 1000Base-T or BroadR-Reach

class XL_ETH_STATUS_BR_PAIR(IntEnum):
  DONT_CARE = 0 #No BR pair available. Only for IEEE 802.3 1000/100/10 MBit
  BR_1PAIR = 1 #BR 1-pair connection. Only for BroadR-Reach

class XL_ETH_RX_ERROR(IntEnum):
  INVALID_LENGTH = 1 #Invalid length error. Set when the receive frame has an invalid length as defined by IEEE802.3
  INVALID_CRC = 2 #CRC error. Set when frame is received with CRC-32 error but valid length
  PHY_ERROR = 4 #Corrupted receive frame caused by a PHY error

XL_ETH_DATAFRAME_FLAGS_USE_SOURCE_MAC = 1 #Use the given source MAC address (not set by hardware)

class XL_ETH_BYPASS(IntEnum):
  INACTIVE = 0 #Bypass inactive (default state)
  PHY = 1 #Bypass active via PHY loop
  MACCORE = 2 #Bypass active via L2 switch (using MAC cores)

class XL_ETH_TX_ERROR(IntEnum):
  BYPASS_ENABLED = 1 #Bypass activated
  NO_LINK = 2 #No Link
  PHY_NOT_CONFIGURED = 3 #PHY not yet configured
  INVALID_LENGTH = 7 #Frame with invalid length transmitted

class XL_ETH_NETWORK_TX_ERROR(IntEnum):
  NO_LINK = 1 #No Link
  PHY_NOT_CONFIGURED = 2 #PHY not yet configured
  PHY_BRIDGE_ENABLED = 4 #PHY Bypass activated
  CONVERTER_RESET = 8 #RGMII Converter in reset
  INVALID_LENGTH = 16 #Invalid length error. Set when the frame has an invalid length as defined by IEEE802.3
  INVALID_CRC = 32 #CRC error. Set when frame is transmitted with CRC-32 error but valid length
  MACADDR_ERROR = 64 #Invalid src or dest MAC address

class XL_ETH_NETWORK_RX_ERROR(IntEnum):
  INVALID_LENGTH = 1 #Invalid length error. Set when the receive frame has an invalid length as defined by IEEE802.3
  INVALID_CRC = 2 #CRC error. Set when frame is received with CRC-32 error but valid length
  PHY_ERROR = 4 #Corrupted receive frame caused by a PHY error
  MACADDR_ERROR = 8 #Invalid src or dest MAC address

XL_NET_MAX_NAME_LENGTH = 32 #

class XL_ACCESS_TYPE(IntEnum):
  UNRELIABLE = 0 #Only for Ethernet uplink, means UDP transfers. (Not supported yet)
  RELIABLE = 1 #Always for USB uplink or TCP for Ethernet host uplink

XL_INVALID_NETWORKID = -1
XL_INVALID_SWITCHID = -1
XL_INVALID_NETWORKHANDLE = -1
XL_INVALID_ETHPORTHANDLE = -1
XL_INVALID_RXHANDLE = -1

XL_NET_CFG_STAT_OK = 0
XL_NET_CFG_DUPLICATE_SEGMENT_NAME = 1
XL_NET_CFG_DUPLICATE_VP_NAME = 2
XL_NET_CFG_DUPLICATE_MP_NAME = 3

### MOST150 XL API ###

XL_MOST150_RX_EVENT_HEADER_SIZE = 32
XL_MOST150_MAX_EVENT_DATA_SIZE = 2048
MOST150_SYNC_ALLOC_INFO_SIZE = 372
XL_MOST150_CTRL_PAYLOAD_MAX_SIZE = 45
XL_MOST150_ASYNC_PAYLOAD_MAX_SIZE = 1524 #maximum valid length (s. INIC User Manual)
XL_MOST150_ETHERNET_PAYLOAD_MAX_SIZE = 1506 #maximum valid length (s. INIC User Manual)
XL_MOST150_ASYNC_SEND_PAYLOAD_MAX_SIZE = 1600 #maximum length for sending a MDP
XL_MOST150_ETHERNET_SEND_PAYLOAD_MAX_SIZE = 1600 #maximum length for sending a MEP

class XL_MOST150_FLAGS_CHIP(IntEnum):
  XL_MOST150_VN2640 = 1 #common VN2640 event
  XL_MOST150_INIC = 2 #event was generated by INIC
  XL_MOST150_SPY = 4 #event was generated by spy
  XL_MOST150_QUEUE_OVERFLOW = 256 #queue overflow occured (some events are lost)

class XL_MOST150_SOURCE(IntEnum):
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

class XL_MOST150_DEVICEMODE(IntEnum):
  SLAVE = 0
  MASTER = 1
  STATIC_MASTER = 3
  RETIMED_BYPASS_SLAVE = 4
  RETIMED_BYPASS_MASTER = 5

class XL_MOST150_FREQUENCY(IntEnum):
  FREQUENCY_44100 = 0
  FREQUENCY_48000 = 1
  FREQUENCY_ERROR = 2

class XL_MOST150_SPECIAL_NODE_INFO(IntEnum):
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

class XL_MOST150_CTRL_RETRY(IntEnum):
  RETRY_TIME_MIN = 3 #Time Unit: 16 MOST Frames
  RETRY_TIME_MAX = 31
  SEND_ATTEMPT_MIN = 1
  SEND_ATTEMPT_MAX = 16
  ASYNC_RETRY_TIME_MIN = 0 #Time Unit: 1 MOST Frame
  ASYNC_RETRY_TIME_MAX = 255
  ASYNC_SEND_ATTEMPT_MIN = 1 #For both MDP and MEP
  ASYNC_SEND_ATTEMPT_MAX = 16

class XL_MOST150_INIC_NISTATE(IntEnum):
  NET_OFF = 0
  NET_INIT = 1
  NET_RBD = 2
  NET_ON = 3
  NET_RBD_RESULT = 4

class XL_MOST150_TX(IntEnum):
  OK = 1
  FAILED_FORMAT_ERROR = 2
  FAILED_NETWORK_OFF = 4
  FAILED_TIMEOUT = 5
  FAILED_WRONG_TARGET = 8
  OK_ONE_SUCCESS = 9
  FAILED_BAD_CRC = 12
  FAILED_RECEIVER_BUFFER_FULL = 14

class XL_MOST150_VALID(IntEnum):
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

class XL_MOST150_SPY_PACK(IntEnum):
  OK = 4
  BUFFER_FULL = 1
  NO_RESPONSE = 0 #maybe spy before receiver

class XL_MOST150_SPY_CACK(IntEnum):
  OK = 4
  CRC_ERROR = 1
  NO_RESPONSE = 0 #maybe spy before receiver

XL_MOST150_ASYNC_INVALID_RX_LENGTH = 32768 #flag indicating a received MDP with length > XL_MOST150_ASYNC_PAYLOAD_MAX_SIZE
XL_MOST150_ETHERNET_INVALID_RX_LENGTH = 2147483648 #flag indicating a received MEP with length > XL_MOST150_ETHERNET_PAYLOAD_MAX_SIZE

class XL_MOST150_LIGHT(IntEnum):
  OFF = 0
  FORCE_ON = 1
  MODULATED = 2
  ON_UNLOCK = 3
  ON_LOCK = 4
  ON_STABLE_LOCK = 5
  ON_CRITICAL_UNLOCK = 6

class XL_MOST150_ERROR(IntEnum):
  ASYNC_TX_ACK_HANDLE = 1
  ETH_TX_ACK_HANDLE = 2

class XL_MOST150_RX_BUFFER_TYPE(IntEnum):
  CTRL = 1
  ASYNC = 2

class XL_MOST150_RX_BUFFER_MODE(IntEnum):
  NORMAL_MODE = 0
  BLOCK_MODE = 1

class XL_MOST150_CTRL_SYNC_AUDIO(IntEnum):
  DEVICE_LINE_IN = 0
  DEVICE_LINE_OUT = 1
  DEVICE_SPDIF_IN = 2
  DEVICE_SPDIF_OUT = 3
  DEVICE_ALLOC_BANDWIDTH = 4

class XL_MOST150_DEVICE_MODE(IntEnum):
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


XL_MOST150_ALLOC_BANDWIDTH_NUM_CL_MAX = 10
XL_MOST150_CL_DEALLOC_ALL = 4095

class XL_MOST150_VOLUME(IntEnum):
  MIN = 0
  MAX = 255

class XL_MOST150_SYNC_MUTE_STATUS(IntEnum):
  NO_MUTE = 0
  MUTE = 1

class XL_MOST150_LIGHT_POWER(IntEnum):
  LIGHT_FULL = 100
  LIGHT_3DB = 50

class XL_MOST150_SYSTEMLOCK_FLAG(IntEnum):
  NOT_SET = 0
  SET = 1

class XL_MOST150_SHUTDOWN_FLAG(IntEnum):
  NOT_SET = 0
  SET = 1

class XL_MOST150_ECL_LINE(IntEnum):
  LOW = 0
  HIGH = 1

class XL_MOST150_ECL_LINE_PULL_UP(IntEnum):
  NOT_ACTIVE = 0
  ACTIVE = 1

class XL_MOST150_ECL_SEQ(IntEnum):
  NUM_STATES_MAX = 200 #Maximum number of states that can be configured for a sequence
  #Value range for duration of ECL sequence states
  DURATION_MIN = 1 #100 us
  DURATION_MAX = 655350 #65535 ms

class XL_MOST150_ECL_GLITCH_FILTER(IntEnum):
  #Value range for setting the glitch filter
  MIN = 50 #50 us
  MAX = 50000 #50 ms

class XL_MOST150_MODE(IntEnum):
  DEACTIVATED = 0
  ACTIVATED = 1

class XL_MOST150_BUSLOAD_TYPE(IntEnum):
  DATA_PACKET = 0
  ETHERNET_PACKET = 1

class XL_MOST150_BUSLOAD_COUNTER_TYPE(IntEnum):
  TYPE_NONE = 0
  TYPE_1_BYTE = 1
  TYPE_2_BYTE = 2
  TYPE_3_BYTE = 3
  TYPE_4_BYTE = 4

class XL_MOST150_SPDIF_MODE(IntEnum):
  SLAVE = 0
  MASTER = 1

class XL_MOST150_SPDIF_ERR(IntEnum):
  NO_ERROR = 0
  HW_COMMUNICATION = 1

class XL_MOST150_NW_STARTUP(IntEnum):
  NO_ERROR = 0
  NO_ERRORINFO = 4294967295

class XL_MOST150_NW_SHUTDOWN(IntEnum):
  NO_ERROR = 0
  NO_ERRORINFO = 4294967295

class XL_MOST150_STREAM(IntEnum):
  RX_DATA = 0 #RX streaming: MOST -> PC
  TX_DATA = 1 #TX streaming: PC -> MOST

XL_MOST150_STREAM_INVALID_HANDLE = 0

class XL_MOST150_STREAM_STATE(IntEnum):
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
XL_MOST150_STREAM_CL_MIN = 12
XL_MOST150_STREAM_CL_MAX = 383

class XL_MOST150_STREAM_STATE_ERROR(IntEnum):
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

class XL_MOST150_STREAM_TX_BUFFER(IntEnum):
  ERROR_NO_ERROR = 0
  ERROR_NOT_ENOUGH_DATA = 1
  TX_FIFO_CLEARED = 2

class XL_MOST150_STREAM_RX_BUFFER(IntEnum):
  ERROR_STOP_BY_APP = 1
  ERROR_MOST_SIGNAL_OFF = 2
  ERROR_UNLOCK = 3
  ERROR_CL_MISSING = 4
  ERROR_ALL_CL_MISSING = 5
  ERROR_OVERFLOW = 128 #overflow bit

class XL_MOST150_STREAM_LATENCY(IntEnum):
  VERY_LOW = 0
  LOW = 1
  MEDIUM = 2
  HIGH = 3
  VERY_HIGH = 4

class XL_MOST150_BYPASS_STRESS_TIME(IntEnum):
  MIN = 10
  MAX = 65535

class XL_MOST150_BYPASS_STRESS(IntEnum):
  STOPPED = 0
  STARTED = 1
  STOPPED_LIGHT_OFF = 2
  STOPPED_DEVICE_MODE = 3

class XL_MOST150_SSO_RESULT_(IntEnum):
  NO_RESULT = 0
  NO_FAULT_SAVED = 1
  SUDDEN_SIGNAL_OFF = 2
  CRITICAL_UNLOCK = 3

### CAN / CAN-FD definitions ###

XL_CAN_MAX_DATA_LEN = 64
XL_CANFD_RX_EVENT_HEADER_SIZE = 32
XL_CANFD_MAX_EVENT_SIZE = 128

CANFD_GET_NUM_DATABYTES = lambda dlc, edl, rtr:\
  (0 if rtr else\
  dlc if dlc < 9 else\
  8 if not edl else\
  12 if dlc == 9 else\
  16 if dlc == 10 else\
  20 if dlc ==11 else\
  24 if dlc ==12 else\
  32 if dlc ==13 else\
  48 if dlc ==14 else 64)

class XL_CAN_TXMSG_FLAG(IntFlag):
  EDL = 1 #extended data length
  BRS = 2 #baud rate switch
  RTR = 16 #remote transmission request
  HIGHPRIO = 128 #high priority message - clears all send buffers - then transmits
  WAKEUP = 512 #generate a wakeup message

class XL_CAN_RXMSG_FLAG(IntFlag):
  EDL = 1 #extended data length
  BRS = 2 #baud rate switch
  ESI = 4 #error state indicator
  RTR = 16 #remote transmission request
  EF = 512 #error frame (only posssible in XL_CAN_EV_TX_REQUEST/XL_CAN_EV_TX_REMOVED)
  ARB_LOST = 1024 #Arbitration Lost(set if the receiving node tried to transmit a message but lost arbitration process)
  WAKEUP = 8192 #high voltage message on single wire CAN
  TE = 16384 #1: transceiver error detected

class XL_CAN_ERRC(IntEnum):
  BIT_ERROR = 1
  FORM_ERROR = 2
  STUFF_ERROR = 3
  OTHER_ERROR = 4
  CRC_ERROR = 5
  ACK_ERROR = 6
  NACK_ERROR = 7
  OVLD_ERROR = 8
  EXCPT_ERROR = 9

XL_CAN_QUEUE_OVERFLOW = 256
RX_FIFO_CANFD_QUEUE_SIZE_MAX = 524288
RX_FIFO_CANFD_QUEUE_SIZE_MIN = 8192

### ARINC429 definitions ###

class XL_A429_MSG_CHANNEL_DIR(IntEnum):
  TX = 1
  RX = 2

class XL_A429_MSG_BITRATE(IntEnum):
  SLOW_MIN = 10500
  SLOW_MAX = 16000
  FAST_MIN = 90000
  FAST_MAX = 110000

XL_A429_MSG_GAP_4BIT = 32

class XL_A429_MSG_BITRATE_RX(IntEnum):
  MIN = 10000
  MAX = 120000

class XL_A429_MSG_AUTO_BAUDRATE(IntEnum):
  DISABLED = 0
  ENABLED = 1

class XL_A429_MSG_FLAG(IntEnum):
  ON_REQUEST = 1
  CYCLIC = 2
  DELETE_CYCLIC = 4

XL_A429_MSG_CYCLE_MAX = 1073741823

class XL_A429_MSG_GAP(IntEnum):
  DEFAULT = 0 #get minGap config from set channel params
  MAX = 1048575

class XL_A429_MSG_PARITY(IntEnum):
  DEFAULT = 0 #get parity config from set channel params
  DISABLED = 1 #tx: get parity config from transmit data - rx: check disabled
  ODD = 2
  EVEN = 3

class XL_A429_EV_TX_MSG_CTRL(IntEnum):
  ON_REQUEST = 0
  CYCLIC = 1

class XL_A429_EV_TX_ERROR(IntEnum):
  ACCESS_DENIED = 0
  TRANSMISSION_ERROR = 1

class XL_A429_EV_RX_ERROR(IntEnum):
  GAP_VIOLATION = 0
  PARITY = 1
  BITRATE_LOW = 2
  BITRATE_HIGH = 3
  FRAME_FORMAT = 4
  CODING_RZ = 5
  DUTY_FACTOR = 6
  AVG_BIT_LENGTH = 7

XL_A429_QUEUE_OVERFLOW = 256
XL_A429_RX_FIFO_QUEUE_SIZE_MAX = 524288 #0,5 MByte
XL_A429_RX_FIFO_QUEUE_SIZE_MIN = 8192 #8 kByte
XL_INVALID_CONFIG_HANDLE = 0
