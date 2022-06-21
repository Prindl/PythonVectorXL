##############################################################################
#                                                                            #
# Module: xlFunctions                                                        #
# Author: Maximilian Prindl                                                  #
#                                                                            #
# Part of a python ctypes wrapper lib for the Vector XL Driver Library.      #
# Contains all of the function definitions of the 'vxlapi.h' and loads       #
# the DLL.                                                                   #
#                                                                            #
##############################################################################
import sys
import ctypes

import xlClasses

if sys.platform.startswith('win'):
    __LIB_NAME =  "vxlapi64.dll" if sys.maxsize > 2**32 else "vxlapi.dll"
    __LOADER = ctypes.windll
else:
    raise NotImplementedError("Unforunately the Vector XL Driver Library is only available on Windows.")
    __LOADER = ctypes.cdll

try:
    _vector_xlapi_dll_ = __LOADER.LoadLibrary(__LIB_NAME)
except Exception as exc:
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
xlOpenDriver.restype = xlClasses.XLstatus
xlOpenDriver.argtypes = []
xlOpenDriver.errcheck = check_xl_status

xlCloseDriver = _vector_xlapi_dll_.xlCloseDriver
xlCloseDriver.restype = xlClasses.XLstatus
xlCloseDriver.argtypes = []
xlCloseDriver.errcheck = check_xl_status

xlGetApplConfig = _vector_xlapi_dll_.xlGetApplConfig
xlGetApplConfig.restype = xlClasses.XLstatus
xlGetApplConfig.argtypes = [
  ctypes.c_char_p, #appName
  ctypes.c_uint, #appChannel
  ctypes.POINTER(ctypes.c_uint), #pHwType
  ctypes.POINTER(ctypes.c_uint), #pHwIndex
  ctypes.POINTER(ctypes.c_uint), #pHwChannel
  ctypes.c_uint, #busType
]
xlGetApplConfig.errcheck = check_xl_status

xlSetApplConfig = _vector_xlapi_dll_.xlSetApplConfig
xlSetApplConfig.restype = xlClasses.XLstatus
xlSetApplConfig.argtypes = [
  ctypes.c_char_p, #appName
  ctypes.c_uint, #appChannel
  ctypes.c_uint, #hwType
  ctypes.c_uint, #hwIndex
  ctypes.c_uint, #hwChannel
  ctypes.c_uint, #busType
]
xlSetApplConfig.errcheck = check_xl_status

xlGetDriverConfig = _vector_xlapi_dll_.xlGetDriverConfig
xlGetDriverConfig.restype = xlClasses.XLstatus
xlGetDriverConfig.argtypes = [
  xlClasses.pXLdriverConfig, #pDriverConfig
]
xlGetDriverConfig.errcheck = check_xl_status

xlCreateDriverConfig = _vector_xlapi_dll_.xlCreateDriverConfig
xlCreateDriverConfig.restype = xlClasses.XLstatus
xlCreateDriverConfig.argtypes = [
  ctypes.c_int, #version
  ctypes.POINTER(xlClasses.XLIDriverConfig), #pConfigInterface
]
xlCreateDriverConfig.errcheck = check_xl_status

xlDestroyDriverConfig = _vector_xlapi_dll_.xlDestroyDriverConfig
xlDestroyDriverConfig.restype = xlClasses.XLstatus
xlDestroyDriverConfig.argtypes = [
  xlClasses.XLdrvConfigHandle, #configHandle
]
xlDestroyDriverConfig.errcheck = check_xl_status

xlGetChannelIndex = _vector_xlapi_dll_.xlGetChannelIndex
xlGetChannelIndex.restype = ctypes.c_int
xlGetChannelIndex.argtypes = [
  ctypes.c_int, #hwType
  ctypes.c_int, #hwIndex
  ctypes.c_int, #hwChannel
]

xlGetChannelMask = _vector_xlapi_dll_.xlGetChannelMask
xlGetChannelMask.restype = xlClasses.XLaccess
xlGetChannelMask.argtypes = [
  ctypes.c_int, #hwType
  ctypes.c_int, #hwIndex
  ctypes.c_int, #hwChannel
]

xlOpenPort = _vector_xlapi_dll_.xlOpenPort
xlOpenPort.restype = xlClasses.XLstatus
xlOpenPort.argtypes = [
  xlClasses.pXLportHandle, #pPortHandle
  ctypes.c_char_p, #userName
  xlClasses.XLaccess, #accessMask
  ctypes.POINTER(xlClasses.XLaccess), #pPermissionMask
  ctypes.c_uint, #rxQueueSize
  ctypes.c_uint, #xlInterfaceVersion
  ctypes.c_uint, #busType
]
xlOpenPort.errcheck = check_xl_status

xlSetTimerRate = _vector_xlapi_dll_.xlSetTimerRate
xlSetTimerRate.restype = xlClasses.XLstatus
xlSetTimerRate.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLulong, #timerRate
]
xlSetTimerRate.errcheck = check_xl_status

xlSetTimerRateAndChannel = _vector_xlapi_dll_.xlSetTimerRateAndChannel
xlSetTimerRateAndChannel.restype = xlClasses.XLstatus
xlSetTimerRateAndChannel.argtypes = [
  xlClasses.XLportHandle, #portHandle
  ctypes.POINTER(xlClasses.XLaccess), #timerChannelMask
  ctypes.POINTER(xlClasses.XLulong), #timerRate
]
xlSetTimerRateAndChannel.errcheck = check_xl_status

xlResetClock = _vector_xlapi_dll_.xlResetClock
xlResetClock.restype = xlClasses.XLstatus
xlResetClock.argtypes = [
  xlClasses.XLportHandle, #portHandle
]
xlResetClock.errcheck = check_xl_status

xlSetNotification = _vector_xlapi_dll_.xlSetNotification
xlSetNotification.restype = xlClasses.XLstatus
xlSetNotification.argtypes = [
  xlClasses.XLportHandle, #portHandle
  ctypes.POINTER(xlClasses.XLhandle), #pHandle
  ctypes.c_int, #queueLevel
]
xlSetNotification.errcheck = check_xl_status

xlSetTimerBasedNotify = _vector_xlapi_dll_.xlSetTimerBasedNotify
xlSetTimerBasedNotify.restype = xlClasses.XLstatus
xlSetTimerBasedNotify.argtypes = [
  xlClasses.XLportHandle, #portHandle
  ctypes.POINTER(xlClasses.XLhandle), #pHandle
]
xlSetTimerBasedNotify.errcheck = check_xl_status

xlFlushReceiveQueue = _vector_xlapi_dll_.xlFlushReceiveQueue
xlFlushReceiveQueue.restype = xlClasses.XLstatus
xlFlushReceiveQueue.argtypes = [
  xlClasses.XLportHandle, #portHandle
]
xlFlushReceiveQueue.errcheck = check_xl_status

xlGetReceiveQueueLevel = _vector_xlapi_dll_.xlGetReceiveQueueLevel
xlGetReceiveQueueLevel.restype = xlClasses.XLstatus
xlGetReceiveQueueLevel.argtypes = [
  xlClasses.XLportHandle, #portHandle
  ctypes.POINTER(ctypes.c_int), #level
]
xlGetReceiveQueueLevel.errcheck = check_xl_status

xlActivateChannel = _vector_xlapi_dll_.xlActivateChannel
xlActivateChannel.restype = xlClasses.XLstatus
xlActivateChannel.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  ctypes.c_uint, #busType
  ctypes.c_uint, #flags
]
xlActivateChannel.errcheck = check_xl_status

xlReceive = _vector_xlapi_dll_.xlReceive
xlReceive.restype = xlClasses.XLstatus
xlReceive.argtypes = [
  xlClasses.XLportHandle, #portHandle
  ctypes.POINTER(ctypes.c_uint), #pEventCount
  ctypes.POINTER(xlClasses.XLevent), #pEvents
]
xlReceive.errcheck = check_xl_status

xlGetErrorString = _vector_xlapi_dll_.xlGetErrorString
xlGetErrorString.restype = xlClasses.XLstringType
xlGetErrorString.argtypes = [
  xlClasses.XLstatus, #err
]

xlGetEventString = _vector_xlapi_dll_.xlGetEventString
xlGetEventString.restype = xlClasses.XLstringType
xlGetEventString.argtypes = [
  ctypes.POINTER(xlClasses.XLevent), #pEv
]

xlCanGetEventString = _vector_xlapi_dll_.xlCanGetEventString
xlCanGetEventString.restype = xlClasses.XLstringType
xlCanGetEventString.argtypes = [
  ctypes.POINTER(xlClasses.XLcanRxEvent), #pEv
]


xlOemContact = _vector_xlapi_dll_.xlOemContact
xlOemContact.restype = xlClasses.XLstatus
xlOemContact.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLulong, #Channel
  xlClasses.XLuint64, #context1
  ctypes.POINTER(xlClasses.XLuint64), #context2
]
xlOemContact.errcheck = check_xl_status

xlGetSyncTime = _vector_xlapi_dll_.xlGetSyncTime
xlGetSyncTime.restype = xlClasses.XLstatus
xlGetSyncTime.argtypes = [
  xlClasses.XLportHandle, #portHandle
  ctypes.POINTER(xlClasses.XLuint64), #pTime
]
xlGetSyncTime.errcheck = check_xl_status

xlGetChannelTime = _vector_xlapi_dll_.xlGetChannelTime
xlGetChannelTime.restype = xlClasses.XLstatus
xlGetChannelTime.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  ctypes.POINTER(xlClasses.XLuint64), #pChannelTime
]
xlGetChannelTime.errcheck = check_xl_status

xlGenerateSyncPulse = _vector_xlapi_dll_.xlGenerateSyncPulse
xlGenerateSyncPulse.restype = xlClasses.XLstatus
xlGenerateSyncPulse.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
]
xlGenerateSyncPulse.errcheck = check_xl_status

xlPopupHwConfig = _vector_xlapi_dll_.xlPopupHwConfig
xlPopupHwConfig.restype = xlClasses.XLstatus
xlPopupHwConfig.argtypes = [
  ctypes.c_char_p, #callSign
  ctypes.c_uint, #waitForFinish
]
xlPopupHwConfig.errcheck = check_xl_status

xlDeactivateChannel = _vector_xlapi_dll_.xlDeactivateChannel
xlDeactivateChannel.restype = xlClasses.XLstatus
xlDeactivateChannel.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
]
xlDeactivateChannel.errcheck = check_xl_status

xlClosePort = _vector_xlapi_dll_.xlClosePort
xlClosePort.restype = xlClasses.XLstatus
xlClosePort.argtypes = [
  xlClasses.XLportHandle, #portHandle
]
xlClosePort.errcheck = check_xl_status

xlCanFlushTransmitQueue = _vector_xlapi_dll_.xlCanFlushTransmitQueue
xlCanFlushTransmitQueue.restype = xlClasses.XLstatus
xlCanFlushTransmitQueue.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
]
xlCanFlushTransmitQueue.errcheck = check_xl_status

xlCanSetChannelOutput = _vector_xlapi_dll_.xlCanSetChannelOutput
xlCanSetChannelOutput.restype = xlClasses.XLstatus
xlCanSetChannelOutput.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  ctypes.c_int, #mode
]
xlCanSetChannelOutput.errcheck = check_xl_status

xlCanSetChannelMode = _vector_xlapi_dll_.xlCanSetChannelMode
xlCanSetChannelMode.restype = xlClasses.XLstatus
xlCanSetChannelMode.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  ctypes.c_int, #tx
  ctypes.c_int, #txrq
]
xlCanSetChannelMode.errcheck = check_xl_status

xlCanSetReceiveMode = _vector_xlapi_dll_.xlCanSetReceiveMode
xlCanSetReceiveMode.restype = xlClasses.XLstatus
xlCanSetReceiveMode.argtypes = [
  xlClasses.XLportHandle, #Port
  ctypes.c_ubyte, #ErrorFrame
  ctypes.c_ubyte, #ChipState
]
xlCanSetReceiveMode.errcheck = check_xl_status

xlCanSetChannelTransceiver = _vector_xlapi_dll_.xlCanSetChannelTransceiver
xlCanSetChannelTransceiver.restype = xlClasses.XLstatus
xlCanSetChannelTransceiver.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  ctypes.c_int, #type
  ctypes.c_int, #lineMode
  ctypes.c_int, #resNet
]
xlCanSetChannelTransceiver.errcheck = check_xl_status

xlCanSetChannelParams = _vector_xlapi_dll_.xlCanSetChannelParams
xlCanSetChannelParams.restype = xlClasses.XLstatus
xlCanSetChannelParams.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  ctypes.POINTER(xlClasses.XLchipParams), #pChipParams
]
xlCanSetChannelParams.errcheck = check_xl_status

xlCanSetChannelParamsC200 = _vector_xlapi_dll_.xlCanSetChannelParamsC200
xlCanSetChannelParamsC200.restype = xlClasses.XLstatus
xlCanSetChannelParamsC200.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  ctypes.c_ubyte, #btr0
  ctypes.c_ubyte, #btr1
]
xlCanSetChannelParamsC200.errcheck = check_xl_status

xlCanSetChannelBitrate = _vector_xlapi_dll_.xlCanSetChannelBitrate
xlCanSetChannelBitrate.restype = xlClasses.XLstatus
xlCanSetChannelBitrate.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLulong, #bitrate
]
xlCanSetChannelBitrate.errcheck = check_xl_status

xlCanFdSetConfiguration = _vector_xlapi_dll_.xlCanFdSetConfiguration
xlCanFdSetConfiguration.restype = xlClasses.XLstatus
xlCanFdSetConfiguration.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  ctypes.POINTER(xlClasses.XLcanFdConf), #pCanFdConf
]
xlCanFdSetConfiguration.errcheck = check_xl_status

xlCanReceive = _vector_xlapi_dll_.xlCanReceive
xlCanReceive.restype = xlClasses.XLstatus
xlCanReceive.argtypes = [
  xlClasses.XLportHandle, #portHandle
  ctypes.POINTER(xlClasses.XLcanRxEvent), #pXlCanRxEvt
]
xlCanReceive.errcheck = check_xl_status

xlCanTransmitEx = _vector_xlapi_dll_.xlCanTransmitEx
xlCanTransmitEx.restype = xlClasses.XLstatus
xlCanTransmitEx.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  ctypes.c_uint, #msgCnt
  ctypes.POINTER(ctypes.c_uint), #pMsgCntSent
  ctypes.POINTER(xlClasses.XLcanTxEvent), #pXlCanTxEvt
]
xlCanTransmitEx.errcheck = check_xl_status

xlCanSetChannelAcceptance = _vector_xlapi_dll_.xlCanSetChannelAcceptance
xlCanSetChannelAcceptance.restype = xlClasses.XLstatus
xlCanSetChannelAcceptance.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLulong, #code
  xlClasses.XLulong, #mask
  ctypes.c_uint, #idRange
]
xlCanSetChannelAcceptance.errcheck = check_xl_status

xlCanAddAcceptanceRange = _vector_xlapi_dll_.xlCanAddAcceptanceRange
xlCanAddAcceptanceRange.restype = xlClasses.XLstatus
xlCanAddAcceptanceRange.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLulong, #first_id
  xlClasses.XLulong, #last_id
]
xlCanAddAcceptanceRange.errcheck = check_xl_status

xlCanRemoveAcceptanceRange = _vector_xlapi_dll_.xlCanRemoveAcceptanceRange
xlCanRemoveAcceptanceRange.restype = xlClasses.XLstatus
xlCanRemoveAcceptanceRange.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLulong, #first_id
  xlClasses.XLulong, #last_id
]
xlCanRemoveAcceptanceRange.errcheck = check_xl_status

xlCanResetAcceptance = _vector_xlapi_dll_.xlCanResetAcceptance
xlCanResetAcceptance.restype = xlClasses.XLstatus
xlCanResetAcceptance.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  ctypes.c_uint, #idRange
]
xlCanResetAcceptance.errcheck = check_xl_status

xlCanRequestChipState = _vector_xlapi_dll_.xlCanRequestChipState
xlCanRequestChipState.restype = xlClasses.XLstatus
xlCanRequestChipState.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
]
xlCanRequestChipState.errcheck = check_xl_status

xlCanTransmit = _vector_xlapi_dll_.xlCanTransmit
xlCanTransmit.restype = xlClasses.XLstatus
xlCanTransmit.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  ctypes.POINTER(ctypes.c_uint), #pEventCount
  ctypes.c_void_p, #pEvents
]
xlCanTransmit.errcheck = check_xl_status

xlSetGlobalTimeSync = _vector_xlapi_dll_.xlSetGlobalTimeSync
xlSetGlobalTimeSync.restype = xlClasses.XLstatus
xlSetGlobalTimeSync.argtypes = [
  xlClasses.XLulong, #newValue
  ctypes.POINTER(xlClasses.XLulong), #previousValue
]
xlSetGlobalTimeSync.errcheck = check_xl_status

xlCheckLicense = _vector_xlapi_dll_.xlCheckLicense
xlCheckLicense.restype = xlClasses.XLstatus
xlCheckLicense.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLulong, #protectionCode
]
xlCheckLicense.errcheck = check_xl_status

xlGetLicenseInfo = _vector_xlapi_dll_.xlGetLicenseInfo
xlGetLicenseInfo.restype = xlClasses.XLstatus
xlGetLicenseInfo.argtypes = [
  xlClasses.XLaccess, #channelMask
  ctypes.POINTER(xlClasses.XLlicenseInfo), #pLicInfoArray
  ctypes.c_uint, #licInfoArraySize
]
xlGetLicenseInfo.errcheck = check_xl_status

xlLinSetChannelParams = _vector_xlapi_dll_.xlLinSetChannelParams
xlLinSetChannelParams.restype = xlClasses.XLstatus
xlLinSetChannelParams.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLlinStatPar, #vStatPar
]
xlLinSetChannelParams.errcheck = check_xl_status

xlLinSetDLC = _vector_xlapi_dll_.xlLinSetDLC
xlLinSetDLC.restype = xlClasses.XLstatus
xlLinSetDLC.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  ctypes.c_ubyte*64, #dlc[64]
]
xlLinSetDLC.errcheck = check_xl_status

xlLinSetSlave = _vector_xlapi_dll_.xlLinSetSlave
xlLinSetSlave.restype = xlClasses.XLstatus
xlLinSetSlave.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  ctypes.c_ubyte, #linId
  ctypes.c_ubyte*8, #data[8]
  ctypes.c_ubyte, #dlc
  ctypes.c_ushort, #checksum
]
xlLinSetSlave.errcheck = check_xl_status

xlLinSendRequest = _vector_xlapi_dll_.xlLinSendRequest
xlLinSendRequest.restype = xlClasses.XLstatus
xlLinSendRequest.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  ctypes.c_ubyte, #linId
  ctypes.c_uint, #flags
]
xlLinSendRequest.errcheck = check_xl_status

xlLinSetSleepMode = _vector_xlapi_dll_.xlLinSetSleepMode
xlLinSetSleepMode.restype = xlClasses.XLstatus
xlLinSetSleepMode.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  ctypes.c_uint, #flags
  ctypes.c_ubyte, #linId
]
xlLinSetSleepMode.errcheck = check_xl_status

xlLinWakeUp = _vector_xlapi_dll_.xlLinWakeUp
xlLinWakeUp.restype = xlClasses.XLstatus
xlLinWakeUp.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
]
xlLinWakeUp.errcheck = check_xl_status

xlLinSetChecksum = _vector_xlapi_dll_.xlLinSetChecksum
xlLinSetChecksum.restype = xlClasses.XLstatus
xlLinSetChecksum.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  ctypes.c_ubyte*60, #checksum[60]
]
xlLinSetChecksum.errcheck = check_xl_status

xlLinSwitchSlave = _vector_xlapi_dll_.xlLinSwitchSlave
xlLinSwitchSlave.restype = xlClasses.XLstatus
xlLinSwitchSlave.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  ctypes.c_ubyte, #linID
  ctypes.c_ubyte, #mode
]
xlLinSwitchSlave.errcheck = check_xl_status

xlDAIOSetPWMOutput = _vector_xlapi_dll_.xlDAIOSetPWMOutput
xlDAIOSetPWMOutput.restype = xlClasses.XLstatus
xlDAIOSetPWMOutput.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  ctypes.c_uint, #frequency
  ctypes.c_uint, #value
]
xlDAIOSetPWMOutput.errcheck = check_xl_status

xlDAIOSetDigitalOutput = _vector_xlapi_dll_.xlDAIOSetDigitalOutput
xlDAIOSetDigitalOutput.restype = xlClasses.XLstatus
xlDAIOSetDigitalOutput.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  ctypes.c_uint, #outputMask
  ctypes.c_uint, #valuePattern
]
xlDAIOSetDigitalOutput.errcheck = check_xl_status

xlDAIOSetAnalogOutput = _vector_xlapi_dll_.xlDAIOSetAnalogOutput
xlDAIOSetAnalogOutput.restype = xlClasses.XLstatus
xlDAIOSetAnalogOutput.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  ctypes.c_uint, #analogLine1
  ctypes.c_uint, #analogLine2
  ctypes.c_uint, #analogLine3
  ctypes.c_uint, #analogLine4
]
xlDAIOSetAnalogOutput.errcheck = check_xl_status

xlDAIORequestMeasurement = _vector_xlapi_dll_.xlDAIORequestMeasurement
xlDAIORequestMeasurement.restype = xlClasses.XLstatus
xlDAIORequestMeasurement.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
]
xlDAIORequestMeasurement.errcheck = check_xl_status

xlDAIOSetDigitalParameters = _vector_xlapi_dll_.xlDAIOSetDigitalParameters
xlDAIOSetDigitalParameters.restype = xlClasses.XLstatus
xlDAIOSetDigitalParameters.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  ctypes.c_uint, #inputMask
  ctypes.c_uint, #outputMask
]
xlDAIOSetDigitalParameters.errcheck = check_xl_status

xlDAIOSetAnalogParameters = _vector_xlapi_dll_.xlDAIOSetAnalogParameters
xlDAIOSetAnalogParameters.restype = xlClasses.XLstatus
xlDAIOSetAnalogParameters.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  ctypes.c_uint, #inputMask
  ctypes.c_uint, #outputMask
  ctypes.c_uint, #highRangeMask
]
xlDAIOSetAnalogParameters.errcheck = check_xl_status

xlDAIOSetAnalogTrigger = _vector_xlapi_dll_.xlDAIOSetAnalogTrigger
xlDAIOSetAnalogTrigger.restype = xlClasses.XLstatus
xlDAIOSetAnalogTrigger.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  ctypes.c_uint, #triggerMask
  ctypes.c_uint, #triggerLevel
  ctypes.c_uint, #triggerEventMode
]
xlDAIOSetAnalogTrigger.errcheck = check_xl_status

xlDAIOSetMeasurementFrequency = _vector_xlapi_dll_.xlDAIOSetMeasurementFrequency
xlDAIOSetMeasurementFrequency.restype = xlClasses.XLstatus
xlDAIOSetMeasurementFrequency.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  ctypes.c_uint, #measurementInterval
]
xlDAIOSetMeasurementFrequency.errcheck = check_xl_status

xlDAIOSetDigitalTrigger = _vector_xlapi_dll_.xlDAIOSetDigitalTrigger
xlDAIOSetDigitalTrigger.restype = xlClasses.XLstatus
xlDAIOSetDigitalTrigger.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  ctypes.c_uint, #triggerMask
]
xlDAIOSetDigitalTrigger.errcheck = check_xl_status

xlKlineTransmit = _vector_xlapi_dll_.xlKlineTransmit
xlKlineTransmit.restype = xlClasses.XLstatus
xlKlineTransmit.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  ctypes.c_uint, #length
  ctypes.POINTER(ctypes.c_ubyte), #data
]
xlKlineTransmit.errcheck = check_xl_status

xlKlineSetUartParams = _vector_xlapi_dll_.xlKlineSetUartParams
xlKlineSetUartParams.restype = xlClasses.XLstatus
xlKlineSetUartParams.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  ctypes.POINTER(xlClasses.XLklineUartParameter), #pxlKlineUartParams
]
xlKlineSetUartParams.errcheck = check_xl_status

xlKlineSwitchHighspeedMode = _vector_xlapi_dll_.xlKlineSwitchHighspeedMode
xlKlineSwitchHighspeedMode.restype = xlClasses.XLstatus
xlKlineSwitchHighspeedMode.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  ctypes.c_uint, #trxMode
]
xlKlineSwitchHighspeedMode.errcheck = check_xl_status

xlKlineSwitchTesterResistor = _vector_xlapi_dll_.xlKlineSwitchTesterResistor
xlKlineSwitchTesterResistor.restype = xlClasses.XLstatus
xlKlineSwitchTesterResistor.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  ctypes.c_uint, #testerR
]
xlKlineSwitchTesterResistor.errcheck = check_xl_status

xlKlineSetBaudrate = _vector_xlapi_dll_.xlKlineSetBaudrate
xlKlineSetBaudrate.restype = xlClasses.XLstatus
xlKlineSetBaudrate.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  ctypes.c_uint, #baudrate
]
xlKlineSetBaudrate.errcheck = check_xl_status

xlKlineFastInitTester = _vector_xlapi_dll_.xlKlineFastInitTester
xlKlineFastInitTester.restype = xlClasses.XLstatus
xlKlineFastInitTester.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  ctypes.c_uint, #length
  ctypes.POINTER(ctypes.c_ubyte), #data
  ctypes.POINTER(xlClasses.XLklineInitTester), #pxlKlineInitTester
]
xlKlineFastInitTester.errcheck = check_xl_status

xlKlineInit5BdTester = _vector_xlapi_dll_.xlKlineInit5BdTester
xlKlineInit5BdTester.restype = xlClasses.XLstatus
xlKlineInit5BdTester.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  ctypes.POINTER(xlClasses.XLkline5BdTester), #pxlKline5BdTester
]
xlKlineInit5BdTester.errcheck = check_xl_status

xlKlineInit5BdEcu = _vector_xlapi_dll_.xlKlineInit5BdEcu
xlKlineInit5BdEcu.restype = xlClasses.XLstatus
xlKlineInit5BdEcu.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  ctypes.POINTER(xlClasses.XLkline5BdEcu), #pxlKline5BdEcu
]
xlKlineInit5BdEcu.errcheck = check_xl_status

xlKlineSetCommunicationTimingTester = _vector_xlapi_dll_.xlKlineSetCommunicationTimingTester
xlKlineSetCommunicationTimingTester.restype = xlClasses.XLstatus
xlKlineSetCommunicationTimingTester.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  ctypes.POINTER(xlClasses.XLklineSetComTester), #pxlKlineSetComTester
]
xlKlineSetCommunicationTimingTester.errcheck = check_xl_status

xlKlineSetCommunicationTimingEcu = _vector_xlapi_dll_.xlKlineSetCommunicationTimingEcu
xlKlineSetCommunicationTimingEcu.restype = xlClasses.XLstatus
xlKlineSetCommunicationTimingEcu.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  ctypes.POINTER(xlClasses.XLklineSetComEcu), #pxlKlineSetComEcu
]
xlKlineSetCommunicationTimingEcu.errcheck = check_xl_status

xlMostReceive = _vector_xlapi_dll_.xlMostReceive
xlMostReceive.restype = xlClasses.XLstatus
xlMostReceive.argtypes = [
  xlClasses.XLportHandle, #portHandle
#  xlClasses.XLaccess, #accessMask -> is not in header (possible bug)
  ctypes.POINTER(xlClasses.XLmostEvent), #pEventBuffer
]
xlMostReceive.errcheck = check_xl_status

xlMostSwitchEventSources = _vector_xlapi_dll_.xlMostSwitchEventSources
xlMostSwitchEventSources.restype = xlClasses.XLstatus
xlMostSwitchEventSources.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.c_ushort, #sourceMask
]
xlMostSwitchEventSources.errcheck = check_xl_status

xlMostSetAllBypass = _vector_xlapi_dll_.xlMostSetAllBypass
xlMostSetAllBypass.restype = xlClasses.XLstatus
xlMostSetAllBypass.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.c_ubyte, #bypassMode
]
xlMostSetAllBypass.errcheck = check_xl_status

xlMostGetAllBypass = _vector_xlapi_dll_.xlMostGetAllBypass
xlMostGetAllBypass.restype = xlClasses.XLstatus
xlMostGetAllBypass.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
]
xlMostGetAllBypass.errcheck = check_xl_status

xlMostSetTimingMode = _vector_xlapi_dll_.xlMostSetTimingMode
xlMostSetTimingMode.restype = xlClasses.XLstatus
xlMostSetTimingMode.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.c_ubyte, #timingMode
]
xlMostSetTimingMode.errcheck = check_xl_status

xlMostGetTimingMode = _vector_xlapi_dll_.xlMostGetTimingMode
xlMostGetTimingMode.restype = xlClasses.XLstatus
xlMostGetTimingMode.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
]
xlMostGetTimingMode.errcheck = check_xl_status

xlMostSetFrequency = _vector_xlapi_dll_.xlMostSetFrequency
xlMostSetFrequency.restype = xlClasses.XLstatus
xlMostSetFrequency.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.c_ushort, #frequency
]
xlMostSetFrequency.errcheck = check_xl_status

xlMostGetFrequency = _vector_xlapi_dll_.xlMostGetFrequency
xlMostGetFrequency.restype = xlClasses.XLstatus
xlMostGetFrequency.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
]
xlMostGetFrequency.errcheck = check_xl_status

xlMostWriteRegister = _vector_xlapi_dll_.xlMostWriteRegister
xlMostWriteRegister.restype = xlClasses.XLstatus
xlMostWriteRegister.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.c_ushort, #adr
  ctypes.c_ubyte, #numBytes
  ctypes.c_ubyte*16, #data[16]
]
xlMostWriteRegister.errcheck = check_xl_status

xlMostReadRegister = _vector_xlapi_dll_.xlMostReadRegister
xlMostReadRegister.restype = xlClasses.XLstatus
xlMostReadRegister.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.c_ushort, #adr
  ctypes.c_ubyte, #numBytes
]
xlMostReadRegister.errcheck = check_xl_status

xlMostWriteRegisterBit = _vector_xlapi_dll_.xlMostWriteRegisterBit
xlMostWriteRegisterBit.restype = xlClasses.XLstatus
xlMostWriteRegisterBit.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.c_ushort, #adr
  ctypes.c_ubyte, #mask
  ctypes.c_ubyte, #value
]
xlMostWriteRegisterBit.errcheck = check_xl_status

xlMostCtrlTransmit = _vector_xlapi_dll_.xlMostCtrlTransmit
xlMostCtrlTransmit.restype = xlClasses.XLstatus
xlMostCtrlTransmit.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.POINTER(xlClasses.XLmostCtrlMsg), #pCtrlMsg
]
xlMostCtrlTransmit.errcheck = check_xl_status

xlMostAsyncTransmit = _vector_xlapi_dll_.xlMostAsyncTransmit
xlMostAsyncTransmit.restype = xlClasses.XLstatus
xlMostAsyncTransmit.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.POINTER(xlClasses.XLmostAsyncMsg), #pAsyncMsg
]
xlMostAsyncTransmit.errcheck = check_xl_status

xlMostSyncGetAllocTable = _vector_xlapi_dll_.xlMostSyncGetAllocTable
xlMostSyncGetAllocTable.restype = xlClasses.XLstatus
xlMostSyncGetAllocTable.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
]
xlMostSyncGetAllocTable.errcheck = check_xl_status

xlMostCtrlSyncAudio = _vector_xlapi_dll_.xlMostCtrlSyncAudio
xlMostCtrlSyncAudio.restype = xlClasses.XLstatus
xlMostCtrlSyncAudio.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.c_uint*4, #channel[4]
  ctypes.c_uint, #device
  ctypes.c_uint, #mode
]
xlMostCtrlSyncAudio.errcheck = check_xl_status

xlMostCtrlSyncAudioEx = _vector_xlapi_dll_.xlMostCtrlSyncAudioEx
xlMostCtrlSyncAudioEx.restype = xlClasses.XLstatus
xlMostCtrlSyncAudioEx.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.c_uint*16, #channel[16]
  ctypes.c_uint, #device
  ctypes.c_uint, #mode
]
xlMostCtrlSyncAudioEx.errcheck = check_xl_status

xlMostSyncVolume = _vector_xlapi_dll_.xlMostSyncVolume
xlMostSyncVolume.restype = xlClasses.XLstatus
xlMostSyncVolume.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.c_uint, #device
  ctypes.c_ubyte, #volume
]
xlMostSyncVolume.errcheck = check_xl_status

xlMostSyncMute = _vector_xlapi_dll_.xlMostSyncMute
xlMostSyncMute.restype = xlClasses.XLstatus
xlMostSyncMute.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.c_uint, #device
  ctypes.c_ubyte, #mute
]
xlMostSyncMute.errcheck = check_xl_status

xlMostSyncGetVolumeStatus = _vector_xlapi_dll_.xlMostSyncGetVolumeStatus
xlMostSyncGetVolumeStatus.restype = xlClasses.XLstatus
xlMostSyncGetVolumeStatus.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.c_uint, #device
]
xlMostSyncGetVolumeStatus.errcheck = check_xl_status

xlMostSyncGetMuteStatus = _vector_xlapi_dll_.xlMostSyncGetMuteStatus
xlMostSyncGetMuteStatus.restype = xlClasses.XLstatus
xlMostSyncGetMuteStatus.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.c_uint, #device
]
xlMostSyncGetMuteStatus.errcheck = check_xl_status

xlMostGetRxLight = _vector_xlapi_dll_.xlMostGetRxLight
xlMostGetRxLight.restype = xlClasses.XLstatus
xlMostGetRxLight.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
]
xlMostGetRxLight.errcheck = check_xl_status

xlMostSetTxLight = _vector_xlapi_dll_.xlMostSetTxLight
xlMostSetTxLight.restype = xlClasses.XLstatus
xlMostSetTxLight.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.c_ubyte, #txLight
]
xlMostSetTxLight.errcheck = check_xl_status

xlMostGetTxLight = _vector_xlapi_dll_.xlMostGetTxLight
xlMostGetTxLight.restype = xlClasses.XLstatus
xlMostGetTxLight.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
]
xlMostGetTxLight.errcheck = check_xl_status

xlMostSetLightPower = _vector_xlapi_dll_.xlMostSetLightPower
xlMostSetLightPower.restype = xlClasses.XLstatus
xlMostSetLightPower.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.c_ubyte, #attenuation
]
xlMostSetLightPower.errcheck = check_xl_status

xlMostGetLockStatus = _vector_xlapi_dll_.xlMostGetLockStatus
xlMostGetLockStatus.restype = xlClasses.XLstatus
xlMostGetLockStatus.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
]
xlMostGetLockStatus.errcheck = check_xl_status

xlMostGenerateLightError = _vector_xlapi_dll_.xlMostGenerateLightError
xlMostGenerateLightError.restype = xlClasses.XLstatus
xlMostGenerateLightError.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  xlClasses.XLulong, #lightOffTime
  xlClasses.XLulong, #lightOnTime
  ctypes.c_ushort, #repeat
]
xlMostGenerateLightError.errcheck = check_xl_status

xlMostGenerateLockError = _vector_xlapi_dll_.xlMostGenerateLockError
xlMostGenerateLockError.restype = xlClasses.XLstatus
xlMostGenerateLockError.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  xlClasses.XLulong, #unmodTime
  xlClasses.XLulong, #modTime
  ctypes.c_ushort, #repeat
]
xlMostGenerateLockError.errcheck = check_xl_status

xlMostCtrlRxBuffer = _vector_xlapi_dll_.xlMostCtrlRxBuffer
xlMostCtrlRxBuffer.restype = xlClasses.XLstatus
xlMostCtrlRxBuffer.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.c_ushort, #bufferMode
]
xlMostCtrlRxBuffer.errcheck = check_xl_status

xlMostTwinklePowerLed = _vector_xlapi_dll_.xlMostTwinklePowerLed
xlMostTwinklePowerLed.restype = xlClasses.XLstatus
xlMostTwinklePowerLed.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
]
xlMostTwinklePowerLed.errcheck = check_xl_status

xlMostCtrlConfigureBusload = _vector_xlapi_dll_.xlMostCtrlConfigureBusload
xlMostCtrlConfigureBusload.restype = xlClasses.XLstatus
xlMostCtrlConfigureBusload.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.POINTER(xlClasses.XLmostCtrlBusloadConfiguration), #pCtrlBusloadConfiguration
]
xlMostCtrlConfigureBusload.errcheck = check_xl_status

xlMostCtrlGenerateBusload = _vector_xlapi_dll_.xlMostCtrlGenerateBusload
xlMostCtrlGenerateBusload.restype = xlClasses.XLstatus
xlMostCtrlGenerateBusload.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  xlClasses.XLulong, #numberCtrlFrames
]
xlMostCtrlGenerateBusload.errcheck = check_xl_status

xlMostAsyncConfigureBusload = _vector_xlapi_dll_.xlMostAsyncConfigureBusload
xlMostAsyncConfigureBusload.restype = xlClasses.XLstatus
xlMostAsyncConfigureBusload.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.POINTER(xlClasses.XLmostAsyncBusloadConfiguration), #pAsyncBusloadConfiguration
]
xlMostAsyncConfigureBusload.errcheck = check_xl_status

xlMostAsyncGenerateBusload = _vector_xlapi_dll_.xlMostAsyncGenerateBusload
xlMostAsyncGenerateBusload.restype = xlClasses.XLstatus
xlMostAsyncGenerateBusload.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  xlClasses.XLulong, #numberAsyncFrames
]
xlMostAsyncGenerateBusload.errcheck = check_xl_status

xlMostStreamOpen = _vector_xlapi_dll_.xlMostStreamOpen
xlMostStreamOpen.restype = xlClasses.XLstatus
xlMostStreamOpen.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.POINTER(xlClasses.XLmostStreamOpen), #pStreamOpen
]
xlMostStreamOpen.errcheck = check_xl_status

xlMostStreamClose = _vector_xlapi_dll_.xlMostStreamClose
xlMostStreamClose.restype = xlClasses.XLstatus
xlMostStreamClose.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.c_uint, #streamHandle
]
xlMostStreamClose.errcheck = check_xl_status

xlMostStreamStart = _vector_xlapi_dll_.xlMostStreamStart
xlMostStreamStart.restype = xlClasses.XLstatus
xlMostStreamStart.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.c_uint, #streamHandle
  ctypes.c_ubyte*60, #syncChannels[60]
]
xlMostStreamStart.errcheck = check_xl_status

xlMostStreamStop = _vector_xlapi_dll_.xlMostStreamStop
xlMostStreamStop.restype = xlClasses.XLstatus
xlMostStreamStop.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.c_uint, #streamHandle
]
xlMostStreamStop.errcheck = check_xl_status

xlMostStreamBufferAllocate = _vector_xlapi_dll_.xlMostStreamBufferAllocate
xlMostStreamBufferAllocate.restype = xlClasses.XLstatus
xlMostStreamBufferAllocate.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.c_uint, #streamHandle
  ctypes.POINTER(ctypes.POINTER(ctypes.c_ubyte)), #ppBuffer
  ctypes.POINTER(ctypes.c_uint), #pBufferSize
]
xlMostStreamBufferAllocate.errcheck = check_xl_status

xlMostStreamBufferDeallocateAll = _vector_xlapi_dll_.xlMostStreamBufferDeallocateAll
xlMostStreamBufferDeallocateAll.restype = xlClasses.XLstatus
xlMostStreamBufferDeallocateAll.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.c_uint, #streamHandle
]
xlMostStreamBufferDeallocateAll.errcheck = check_xl_status

xlMostStreamBufferSetNext = _vector_xlapi_dll_.xlMostStreamBufferSetNext
xlMostStreamBufferSetNext.restype = xlClasses.XLstatus
xlMostStreamBufferSetNext.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.c_uint, #streamHandle
  ctypes.POINTER(ctypes.c_ubyte), #pBuffer
  ctypes.c_uint, #filledBytes
]
xlMostStreamBufferSetNext.errcheck = check_xl_status

xlMostStreamGetInfo = _vector_xlapi_dll_.xlMostStreamGetInfo
xlMostStreamGetInfo.restype = xlClasses.XLstatus
xlMostStreamGetInfo.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.POINTER(xlClasses.XLmostStreamInfo), #pStreamInfo
]
xlMostStreamGetInfo.errcheck = check_xl_status

xlMostStreamBufferClearAll = _vector_xlapi_dll_.xlMostStreamBufferClearAll
xlMostStreamBufferClearAll.restype = xlClasses.XLstatus
xlMostStreamBufferClearAll.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.c_uint, #streamHandle
]
xlMostStreamBufferClearAll.errcheck = check_xl_status

xlFrSetConfiguration = _vector_xlapi_dll_.xlFrSetConfiguration
xlFrSetConfiguration.restype = xlClasses.XLstatus
xlFrSetConfiguration.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  ctypes.POINTER(xlClasses.XLfrClusterConfig), #pxlClusterConfig
]
xlFrSetConfiguration.errcheck = check_xl_status

xlFrGetChannelConfiguration = _vector_xlapi_dll_.xlFrGetChannelConfiguration
xlFrGetChannelConfiguration.restype = xlClasses.XLstatus
xlFrGetChannelConfiguration.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  ctypes.POINTER(xlClasses.XLfrChannelConfig), #pxlFrChannelConfig
]
xlFrGetChannelConfiguration.errcheck = check_xl_status

xlFrSetMode = _vector_xlapi_dll_.xlFrSetMode
xlFrSetMode.restype = xlClasses.XLstatus
xlFrSetMode.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  ctypes.POINTER(xlClasses.XLfrMode), #pxlFrMode
]
xlFrSetMode.errcheck = check_xl_status

xlFrInitStartupAndSync = _vector_xlapi_dll_.xlFrInitStartupAndSync
xlFrInitStartupAndSync.restype = xlClasses.XLstatus
xlFrInitStartupAndSync.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  ctypes.POINTER(xlClasses.XLfrEvent), #pEventBuffer
]
xlFrInitStartupAndSync.errcheck = check_xl_status

xlFrSetupSymbolWindow = _vector_xlapi_dll_.xlFrSetupSymbolWindow
xlFrSetupSymbolWindow.restype = xlClasses.XLstatus
xlFrSetupSymbolWindow.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  ctypes.c_uint, #frChannel
  ctypes.c_uint, #symbolWindowMask
]
xlFrSetupSymbolWindow.errcheck = check_xl_status

xlFrReceive = _vector_xlapi_dll_.xlFrReceive
xlFrReceive.restype = xlClasses.XLstatus
xlFrReceive.argtypes = [
  xlClasses.XLportHandle, #portHandle
  ctypes.POINTER(xlClasses.XLfrEvent), #pEventBuffer
]
xlFrReceive.errcheck = check_xl_status

xlFrTransmit = _vector_xlapi_dll_.xlFrTransmit
xlFrTransmit.restype = xlClasses.XLstatus
xlFrTransmit.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  ctypes.POINTER(xlClasses.XLfrEvent), #pEventBuffer
]
xlFrTransmit.errcheck = check_xl_status

xlFrSetTransceiverMode = _vector_xlapi_dll_.xlFrSetTransceiverMode
xlFrSetTransceiverMode.restype = xlClasses.XLstatus
xlFrSetTransceiverMode.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  ctypes.c_uint, #frChannel
  ctypes.c_uint, #mode
]
xlFrSetTransceiverMode.errcheck = check_xl_status

xlFrSendSymbolWindow = _vector_xlapi_dll_.xlFrSendSymbolWindow
xlFrSendSymbolWindow.restype = xlClasses.XLstatus
xlFrSendSymbolWindow.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  ctypes.c_uint, #symbolWindow
]
xlFrSendSymbolWindow.errcheck = check_xl_status

xlFrActivateSpy = _vector_xlapi_dll_.xlFrActivateSpy
xlFrActivateSpy.restype = xlClasses.XLstatus
xlFrActivateSpy.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  ctypes.c_uint, #mode
]
xlFrActivateSpy.errcheck = check_xl_status

xlFrSetAcceptanceFilter = _vector_xlapi_dll_.xlFrSetAcceptanceFilter
xlFrSetAcceptanceFilter.restype = xlClasses.XLstatus
xlFrSetAcceptanceFilter.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  ctypes.POINTER(xlClasses.XLfrAcceptanceFilter), #pAcceptanceFilter
]
xlFrSetAcceptanceFilter.errcheck = check_xl_status

xlGetRemoteDriverConfig = _vector_xlapi_dll_.xlGetRemoteDriverConfig
xlGetRemoteDriverConfig.restype = xlClasses.XLstatus
xlGetRemoteDriverConfig.argtypes = [
  ctypes.POINTER(xlClasses.XLdriverConfig), #pDriverConfig
]
xlGetRemoteDriverConfig.errcheck = check_xl_status

xlGetRemoteDeviceInfo = _vector_xlapi_dll_.xlGetRemoteDeviceInfo
xlGetRemoteDeviceInfo.restype = xlClasses.XLstatus
xlGetRemoteDeviceInfo.argtypes = [
  ctypes.POINTER(ctypes.POINTER(xlClasses.XLremoteDeviceInfo)), #deviceList
  ctypes.POINTER(ctypes.c_uint), #nbrOfRemoteDevices
  ctypes.c_uint, #netSearch
]
xlGetRemoteDeviceInfo.errcheck = check_xl_status

xlReleaseRemoteDeviceInfo = _vector_xlapi_dll_.xlReleaseRemoteDeviceInfo
xlReleaseRemoteDeviceInfo.restype = xlClasses.XLstatus
xlReleaseRemoteDeviceInfo.argtypes = [
  ctypes.POINTER(ctypes.POINTER(xlClasses.XLremoteDeviceInfo)), #deviceList
]
xlReleaseRemoteDeviceInfo.errcheck = check_xl_status

xlAddRemoteDevice = _vector_xlapi_dll_.xlAddRemoteDevice
xlAddRemoteDevice.restype = xlClasses.XLstatus
xlAddRemoteDevice.argtypes = [
  xlClasses.XLremoteHandle, #remoteHandle
  xlClasses.XLdeviceAccess, #deviceMask
  ctypes.c_uint, #flags
]
xlAddRemoteDevice.errcheck = check_xl_status

xlRemoveRemoteDevice = _vector_xlapi_dll_.xlRemoveRemoteDevice
xlRemoveRemoteDevice.restype = xlClasses.XLstatus
xlRemoveRemoteDevice.argtypes = [
  xlClasses.XLremoteHandle, #remoteHandle
  xlClasses.XLdeviceAccess, #deviceMask
  ctypes.c_uint, #flags
]
xlRemoveRemoteDevice.errcheck = check_xl_status

xlUpdateRemoteDeviceInfo = _vector_xlapi_dll_.xlUpdateRemoteDeviceInfo
xlUpdateRemoteDeviceInfo.restype = xlClasses.XLstatus
xlUpdateRemoteDeviceInfo.argtypes = [
  ctypes.POINTER(xlClasses.XLremoteDeviceInfo), #deviceList
  ctypes.c_uint, #nbrOfRemoteDevices
]
xlUpdateRemoteDeviceInfo.errcheck = check_xl_status

xlGetRemoteHwInfo = _vector_xlapi_dll_.xlGetRemoteHwInfo
xlGetRemoteHwInfo.restype = xlClasses.XLstatus
xlGetRemoteHwInfo.argtypes = [
  xlClasses.XLremoteHandle, #remoteHandle
  ctypes.POINTER(ctypes.c_int), #hwType
  ctypes.POINTER(ctypes.c_int), #hwIndex
  ctypes.POINTER(ctypes.c_int), #isPresent
]
xlGetRemoteHwInfo.errcheck = check_xl_status

xlRegisterRemoteDevice = _vector_xlapi_dll_.xlRegisterRemoteDevice
xlRegisterRemoteDevice.restype = xlClasses.XLstatus
xlRegisterRemoteDevice.argtypes = [
  ctypes.c_int, #hwType
  ctypes.POINTER(xlClasses.XLipAddress), #ipAddress
  ctypes.c_uint, #flags
]
xlRegisterRemoteDevice.errcheck = check_xl_status

xlIoSetTriggerMode = _vector_xlapi_dll_.xlIoSetTriggerMode
xlIoSetTriggerMode.restype = xlClasses.XLstatus
xlIoSetTriggerMode.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  ctypes.POINTER(xlClasses.XLdaioTriggerMode), #pxlDaioTriggerMode
]
xlIoSetTriggerMode.errcheck = check_xl_status

xlIoSetDigitalOutput = _vector_xlapi_dll_.xlIoSetDigitalOutput
xlIoSetDigitalOutput.restype = xlClasses.XLstatus
xlIoSetDigitalOutput.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  ctypes.POINTER(xlClasses.XLdaioDigitalParams), #pxlDaioDigitalParams
]
xlIoSetDigitalOutput.errcheck = check_xl_status

xlIoConfigurePorts = _vector_xlapi_dll_.xlIoConfigurePorts
xlIoConfigurePorts.restype = xlClasses.XLstatus
xlIoConfigurePorts.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  ctypes.POINTER(xlClasses.XLdaioSetPort), #pxlDaioSetPort
]
xlIoConfigurePorts.errcheck = check_xl_status

xlIoSetDigInThreshold = _vector_xlapi_dll_.xlIoSetDigInThreshold
xlIoSetDigInThreshold.restype = xlClasses.XLstatus
xlIoSetDigInThreshold.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  ctypes.c_uint, #level
]
xlIoSetDigInThreshold.errcheck = check_xl_status

xlIoSetDigOutLevel = _vector_xlapi_dll_.xlIoSetDigOutLevel
xlIoSetDigOutLevel.restype = xlClasses.XLstatus
xlIoSetDigOutLevel.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  ctypes.c_uint, #level
]
xlIoSetDigOutLevel.errcheck = check_xl_status

xlIoSetAnalogOutput = _vector_xlapi_dll_.xlIoSetAnalogOutput
xlIoSetAnalogOutput.restype = xlClasses.XLstatus
xlIoSetAnalogOutput.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  ctypes.POINTER(xlClasses.XLdaioAnalogParams), #pxlDaioAnalogParams
]
xlIoSetAnalogOutput.errcheck = check_xl_status

xlIoStartSampling = _vector_xlapi_dll_.xlIoStartSampling
xlIoStartSampling.restype = xlClasses.XLstatus
xlIoStartSampling.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  ctypes.c_uint, #portTypeMask
]
xlIoStartSampling.errcheck = check_xl_status

xlMost150Receive = _vector_xlapi_dll_.xlMost150Receive
xlMost150Receive.restype = xlClasses.XLstatus
xlMost150Receive.argtypes = [
  xlClasses.XLportHandle, #portHandle
  ctypes.POINTER(xlClasses.XLmost150event), #pEventBuffer
]
xlMost150Receive.errcheck = check_xl_status

xlMost150TwinklePowerLed = _vector_xlapi_dll_.xlMost150TwinklePowerLed
xlMost150TwinklePowerLed.restype = xlClasses.XLstatus
xlMost150TwinklePowerLed.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
]
xlMost150TwinklePowerLed.errcheck = check_xl_status

xlMost150SwitchEventSources = _vector_xlapi_dll_.xlMost150SwitchEventSources
xlMost150SwitchEventSources.restype = xlClasses.XLstatus
xlMost150SwitchEventSources.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.c_uint, #sourceMask
]
xlMost150SwitchEventSources.errcheck = check_xl_status

xlMost150SetDeviceMode = _vector_xlapi_dll_.xlMost150SetDeviceMode
xlMost150SetDeviceMode.restype = xlClasses.XLstatus
xlMost150SetDeviceMode.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.c_uint, #deviceMode
]
xlMost150SetDeviceMode.errcheck = check_xl_status

xlMost150GetDeviceMode = _vector_xlapi_dll_.xlMost150GetDeviceMode
xlMost150GetDeviceMode.restype = xlClasses.XLstatus
xlMost150GetDeviceMode.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
]
xlMost150GetDeviceMode.errcheck = check_xl_status

xlMost150SetSPDIFMode = _vector_xlapi_dll_.xlMost150SetSPDIFMode
xlMost150SetSPDIFMode.restype = xlClasses.XLstatus
xlMost150SetSPDIFMode.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.c_uint, #spdifMode
]
xlMost150SetSPDIFMode.errcheck = check_xl_status

xlMost150GetSPDIFMode = _vector_xlapi_dll_.xlMost150GetSPDIFMode
xlMost150GetSPDIFMode.restype = xlClasses.XLstatus
xlMost150GetSPDIFMode.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
]
xlMost150GetSPDIFMode.errcheck = check_xl_status

xlMost150SetSpecialNodeInfo = _vector_xlapi_dll_.xlMost150SetSpecialNodeInfo
xlMost150SetSpecialNodeInfo.restype = xlClasses.XLstatus
xlMost150SetSpecialNodeInfo.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.POINTER(xlClasses.XLmost150SetSpecialNodeInfo), #pSpecialNodeInfo
]
xlMost150SetSpecialNodeInfo.errcheck = check_xl_status

xlMost150GetSpecialNodeInfo = _vector_xlapi_dll_.xlMost150GetSpecialNodeInfo
xlMost150GetSpecialNodeInfo.restype = xlClasses.XLstatus
xlMost150GetSpecialNodeInfo.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.c_uint, #requestMask
]
xlMost150GetSpecialNodeInfo.errcheck = check_xl_status

xlMost150SetFrequency = _vector_xlapi_dll_.xlMost150SetFrequency
xlMost150SetFrequency.restype = xlClasses.XLstatus
xlMost150SetFrequency.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.c_uint, #frequency
]
xlMost150SetFrequency.errcheck = check_xl_status

xlMost150GetFrequency = _vector_xlapi_dll_.xlMost150GetFrequency
xlMost150GetFrequency.restype = xlClasses.XLstatus
xlMost150GetFrequency.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
]
xlMost150GetFrequency.errcheck = check_xl_status

xlMost150CtrlTransmit = _vector_xlapi_dll_.xlMost150CtrlTransmit
xlMost150CtrlTransmit.restype = xlClasses.XLstatus
xlMost150CtrlTransmit.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.POINTER(xlClasses.XLmost150CtrlTxMsg), #pCtrlTxMsg
]
xlMost150CtrlTransmit.errcheck = check_xl_status

xlMost150AsyncTransmit = _vector_xlapi_dll_.xlMost150AsyncTransmit
xlMost150AsyncTransmit.restype = xlClasses.XLstatus
xlMost150AsyncTransmit.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.POINTER(xlClasses.XLmost150AsyncTxMsg), #pAsyncTxMsg
]
xlMost150AsyncTransmit.errcheck = check_xl_status

xlMost150EthernetTransmit = _vector_xlapi_dll_.xlMost150EthernetTransmit
xlMost150EthernetTransmit.restype = xlClasses.XLstatus
xlMost150EthernetTransmit.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.POINTER(xlClasses.XLmost150EthernetTxMsg), #pEthernetTxMsg
]
xlMost150EthernetTransmit.errcheck = check_xl_status

xlMost150GetSystemLockFlag = _vector_xlapi_dll_.xlMost150GetSystemLockFlag
xlMost150GetSystemLockFlag.restype = xlClasses.XLstatus
xlMost150GetSystemLockFlag.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
]
xlMost150GetSystemLockFlag.errcheck = check_xl_status

xlMost150GetShutdownFlag = _vector_xlapi_dll_.xlMost150GetShutdownFlag
xlMost150GetShutdownFlag.restype = xlClasses.XLstatus
xlMost150GetShutdownFlag.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
]
xlMost150GetShutdownFlag.errcheck = check_xl_status

xlMost150Shutdown = _vector_xlapi_dll_.xlMost150Shutdown
xlMost150Shutdown.restype = xlClasses.XLstatus
xlMost150Shutdown.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
]
xlMost150Shutdown.errcheck = check_xl_status

xlMost150Startup = _vector_xlapi_dll_.xlMost150Startup
xlMost150Startup.restype = xlClasses.XLstatus
xlMost150Startup.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
]
xlMost150Startup.errcheck = check_xl_status

xlMost150SyncGetAllocTable = _vector_xlapi_dll_.xlMost150SyncGetAllocTable
xlMost150SyncGetAllocTable.restype = xlClasses.XLstatus
xlMost150SyncGetAllocTable.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
]
xlMost150SyncGetAllocTable.errcheck = check_xl_status

xlMost150CtrlSyncAudio = _vector_xlapi_dll_.xlMost150CtrlSyncAudio
xlMost150CtrlSyncAudio.restype = xlClasses.XLstatus
xlMost150CtrlSyncAudio.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.POINTER(xlClasses.XLmost150SyncAudioParameter), #pSyncAudioParameter
]
xlMost150CtrlSyncAudio.errcheck = check_xl_status

xlMost150SyncSetVolume = _vector_xlapi_dll_.xlMost150SyncSetVolume
xlMost150SyncSetVolume.restype = xlClasses.XLstatus
xlMost150SyncSetVolume.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.c_uint, #device
  ctypes.c_uint, #volume
]
xlMost150SyncSetVolume.errcheck = check_xl_status

xlMost150SyncGetVolume = _vector_xlapi_dll_.xlMost150SyncGetVolume
xlMost150SyncGetVolume.restype = xlClasses.XLstatus
xlMost150SyncGetVolume.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.c_uint, #device
]
xlMost150SyncGetVolume.errcheck = check_xl_status

xlMost150SyncSetMute = _vector_xlapi_dll_.xlMost150SyncSetMute
xlMost150SyncSetMute.restype = xlClasses.XLstatus
xlMost150SyncSetMute.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.c_uint, #device
  ctypes.c_uint, #mute
]
xlMost150SyncSetMute.errcheck = check_xl_status

xlMost150SyncGetMute = _vector_xlapi_dll_.xlMost150SyncGetMute
xlMost150SyncGetMute.restype = xlClasses.XLstatus
xlMost150SyncGetMute.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.c_uint, #device
]
xlMost150SyncGetMute.errcheck = check_xl_status

xlMost150GetRxLightLockStatus = _vector_xlapi_dll_.xlMost150GetRxLightLockStatus
xlMost150GetRxLightLockStatus.restype = xlClasses.XLstatus
xlMost150GetRxLightLockStatus.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.c_uint, #fromSpy
]
xlMost150GetRxLightLockStatus.errcheck = check_xl_status

xlMost150SetTxLight = _vector_xlapi_dll_.xlMost150SetTxLight
xlMost150SetTxLight.restype = xlClasses.XLstatus
xlMost150SetTxLight.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.c_uint, #txLight
]
xlMost150SetTxLight.errcheck = check_xl_status

xlMost150GetTxLight = _vector_xlapi_dll_.xlMost150GetTxLight
xlMost150GetTxLight.restype = xlClasses.XLstatus
xlMost150GetTxLight.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
]
xlMost150GetTxLight.errcheck = check_xl_status

xlMost150SetTxLightPower = _vector_xlapi_dll_.xlMost150SetTxLightPower
xlMost150SetTxLightPower.restype = xlClasses.XLstatus
xlMost150SetTxLightPower.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.c_uint, #attenuation
]
xlMost150SetTxLightPower.errcheck = check_xl_status

xlMost150GenerateLightError = _vector_xlapi_dll_.xlMost150GenerateLightError
xlMost150GenerateLightError.restype = xlClasses.XLstatus
xlMost150GenerateLightError.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.c_uint, #lightOffTime
  ctypes.c_uint, #lightOnTime
  ctypes.c_uint, #repeat
]
xlMost150GenerateLightError.errcheck = check_xl_status

xlMost150GenerateLockError = _vector_xlapi_dll_.xlMost150GenerateLockError
xlMost150GenerateLockError.restype = xlClasses.XLstatus
xlMost150GenerateLockError.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.c_uint, #unlockTime
  ctypes.c_uint, #lockTime
  ctypes.c_uint, #repeat
]
xlMost150GenerateLockError.errcheck = check_xl_status

xlMost150ConfigureRxBuffer = _vector_xlapi_dll_.xlMost150ConfigureRxBuffer
xlMost150ConfigureRxBuffer.restype = xlClasses.XLstatus
xlMost150ConfigureRxBuffer.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.c_uint, #bufferType
  ctypes.c_uint, #bufferMode
]
xlMost150ConfigureRxBuffer.errcheck = check_xl_status

xlMost150CtrlConfigureBusload = _vector_xlapi_dll_.xlMost150CtrlConfigureBusload
xlMost150CtrlConfigureBusload.restype = xlClasses.XLstatus
xlMost150CtrlConfigureBusload.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.POINTER(xlClasses.XLmost150CtrlBusloadConfig), #pCtrlBusLoad
]
xlMost150CtrlConfigureBusload.errcheck = check_xl_status

xlMost150CtrlGenerateBusload = _vector_xlapi_dll_.xlMost150CtrlGenerateBusload
xlMost150CtrlGenerateBusload.restype = xlClasses.XLstatus
xlMost150CtrlGenerateBusload.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  xlClasses.XLulong, #numberCtrlFrames
]
xlMost150CtrlGenerateBusload.errcheck = check_xl_status

xlMost150AsyncConfigureBusload = _vector_xlapi_dll_.xlMost150AsyncConfigureBusload
xlMost150AsyncConfigureBusload.restype = xlClasses.XLstatus
xlMost150AsyncConfigureBusload.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.POINTER(xlClasses.XLmost150AsyncBusloadConfig), #pAsyncBusLoad
]
xlMost150AsyncConfigureBusload.errcheck = check_xl_status

xlMost150AsyncGenerateBusload = _vector_xlapi_dll_.xlMost150AsyncGenerateBusload
xlMost150AsyncGenerateBusload.restype = xlClasses.XLstatus
xlMost150AsyncGenerateBusload.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  xlClasses.XLulong, #numberAsyncPackets
]
xlMost150AsyncGenerateBusload.errcheck = check_xl_status

xlMost150SetECLLine = _vector_xlapi_dll_.xlMost150SetECLLine
xlMost150SetECLLine.restype = xlClasses.XLstatus
xlMost150SetECLLine.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.c_uint, #eclLineState
]
xlMost150SetECLLine.errcheck = check_xl_status

xlMost150SetECLTermination = _vector_xlapi_dll_.xlMost150SetECLTermination
xlMost150SetECLTermination.restype = xlClasses.XLstatus
xlMost150SetECLTermination.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.c_uint, #eclLineTermination
]
xlMost150SetECLTermination.errcheck = check_xl_status

xlMost150GetECLInfo = _vector_xlapi_dll_.xlMost150GetECLInfo
xlMost150GetECLInfo.restype = xlClasses.XLstatus
xlMost150GetECLInfo.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
]
xlMost150GetECLInfo.errcheck = check_xl_status

xlMost150StreamOpen = _vector_xlapi_dll_.xlMost150StreamOpen
xlMost150StreamOpen.restype = xlClasses.XLstatus
xlMost150StreamOpen.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.POINTER(xlClasses.XLmost150StreamOpen), #pStreamOpen
]
xlMost150StreamOpen.errcheck = check_xl_status

xlMost150StreamClose = _vector_xlapi_dll_.xlMost150StreamClose
xlMost150StreamClose.restype = xlClasses.XLstatus
xlMost150StreamClose.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.c_uint, #streamHandle
]
xlMost150StreamClose.errcheck = check_xl_status

xlMost150StreamStart = _vector_xlapi_dll_.xlMost150StreamStart
xlMost150StreamStart.restype = xlClasses.XLstatus
xlMost150StreamStart.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.c_uint, #streamHandle
  ctypes.c_uint, #numConnLabels
  ctypes.POINTER(ctypes.c_uint), #pConnLabels
]
xlMost150StreamStart.errcheck = check_xl_status

xlMost150StreamStop = _vector_xlapi_dll_.xlMost150StreamStop
xlMost150StreamStop.restype = xlClasses.XLstatus
xlMost150StreamStop.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.c_uint, #streamHandle
]
xlMost150StreamStop.errcheck = check_xl_status

xlMost150StreamTransmitData = _vector_xlapi_dll_.xlMost150StreamTransmitData
xlMost150StreamTransmitData.restype = xlClasses.XLstatus
xlMost150StreamTransmitData.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.c_uint, #streamHandle
  ctypes.POINTER(ctypes.c_ubyte), #pBuffer
  ctypes.POINTER(ctypes.c_uint), #pNumberOfBytes
]
xlMost150StreamTransmitData.errcheck = check_xl_status

xlMost150StreamClearTxFifo = _vector_xlapi_dll_.xlMost150StreamClearTxFifo
xlMost150StreamClearTxFifo.restype = xlClasses.XLstatus
xlMost150StreamClearTxFifo.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.c_uint, #streamHandle
]
xlMost150StreamClearTxFifo.errcheck = check_xl_status

xlMost150StreamGetInfo = _vector_xlapi_dll_.xlMost150StreamGetInfo
xlMost150StreamGetInfo.restype = xlClasses.XLstatus
xlMost150StreamGetInfo.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.POINTER(xlClasses.XLmost150StreamInfo), #pStreamInfo
]
xlMost150StreamGetInfo.errcheck = check_xl_status

xlMost150StreamInitRxFifo = _vector_xlapi_dll_.xlMost150StreamInitRxFifo
xlMost150StreamInitRxFifo.restype = xlClasses.XLstatus
xlMost150StreamInitRxFifo.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
]
xlMost150StreamInitRxFifo.errcheck = check_xl_status

xlMost150StreamReceiveData = _vector_xlapi_dll_.xlMost150StreamReceiveData
xlMost150StreamReceiveData.restype = xlClasses.XLstatus
xlMost150StreamReceiveData.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  ctypes.POINTER(ctypes.c_ubyte), #pBuffer
  ctypes.POINTER(ctypes.c_uint), #pBufferSize
]
xlMost150StreamReceiveData.errcheck = check_xl_status

xlMost150GenerateBypassStress = _vector_xlapi_dll_.xlMost150GenerateBypassStress
xlMost150GenerateBypassStress.restype = xlClasses.XLstatus
xlMost150GenerateBypassStress.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.c_uint, #bypassCloseTime
  ctypes.c_uint, #bypassOpenTime
  ctypes.c_uint, #repeat
]
xlMost150GenerateBypassStress.errcheck = check_xl_status

xlMost150EclConfigureSeq = _vector_xlapi_dll_.xlMost150EclConfigureSeq
xlMost150EclConfigureSeq.restype = xlClasses.XLstatus
xlMost150EclConfigureSeq.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.c_uint, #numStates
  ctypes.POINTER(ctypes.c_uint), #pEclStates
  ctypes.POINTER(ctypes.c_uint), #pEclStatesDuration
]
xlMost150EclConfigureSeq.errcheck = check_xl_status

xlMost150EclGenerateSeq = _vector_xlapi_dll_.xlMost150EclGenerateSeq
xlMost150EclGenerateSeq.restype = xlClasses.XLstatus
xlMost150EclGenerateSeq.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.c_uint, #start
]
xlMost150EclGenerateSeq.errcheck = check_xl_status

xlMost150SetECLGlitchFilter = _vector_xlapi_dll_.xlMost150SetECLGlitchFilter
xlMost150SetECLGlitchFilter.restype = xlClasses.XLstatus
xlMost150SetECLGlitchFilter.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.c_uint, #duration
]
xlMost150SetECLGlitchFilter.errcheck = check_xl_status

xlMost150SetSSOResult = _vector_xlapi_dll_.xlMost150SetSSOResult
xlMost150SetSSOResult.restype = xlClasses.XLstatus
xlMost150SetSSOResult.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.c_uint, #ssoCUStatus
]
xlMost150SetSSOResult.errcheck = check_xl_status

xlMost150GetSSOResult = _vector_xlapi_dll_.xlMost150GetSSOResult
xlMost150GetSSOResult.restype = xlClasses.XLstatus
xlMost150GetSSOResult.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
]
xlMost150GetSSOResult.errcheck = check_xl_status

xlEthSetConfig = _vector_xlapi_dll_.xlEthSetConfig
xlEthSetConfig.restype = xlClasses.XLstatus
xlEthSetConfig.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.POINTER(xlClasses.T_XL_ETH_CONFIG), #config
]
xlEthSetConfig.errcheck = check_xl_status

xlEthGetConfig = _vector_xlapi_dll_.xlEthGetConfig
xlEthGetConfig.restype = xlClasses.XLstatus
xlEthGetConfig.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.POINTER(xlClasses.T_XL_ETH_CONFIG), #config
]
xlEthGetConfig.errcheck = check_xl_status

xlEthReceive = _vector_xlapi_dll_.xlEthReceive
xlEthReceive.restype = xlClasses.XLstatus
xlEthReceive.argtypes = [
  xlClasses.XLportHandle, #portHandle
  ctypes.POINTER(xlClasses.T_XL_ETH_EVENT), #ethEventBuffer
]
xlEthReceive.errcheck = check_xl_status

xlEthSetBypass = _vector_xlapi_dll_.xlEthSetBypass
xlEthSetBypass.restype = xlClasses.XLstatus
xlEthSetBypass.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.c_uint, #mode
]
xlEthSetBypass.errcheck = check_xl_status

xlEthTwinkleStatusLed = _vector_xlapi_dll_.xlEthTwinkleStatusLed
xlEthTwinkleStatusLed.restype = xlClasses.XLstatus
xlEthTwinkleStatusLed.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
]
xlEthTwinkleStatusLed.errcheck = check_xl_status

xlEthTransmit = _vector_xlapi_dll_.xlEthTransmit
xlEthTransmit.restype = xlClasses.XLstatus
xlEthTransmit.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  xlClasses.XLuserHandle, #userHandle
  ctypes.POINTER(xlClasses.T_XL_ETH_DATAFRAME_TX), #data
]
xlEthTransmit.errcheck = check_xl_status

xlNetEthOpenNetwork = _vector_xlapi_dll_.xlNetEthOpenNetwork
xlNetEthOpenNetwork.restype = xlClasses.XLstatus
xlNetEthOpenNetwork.argtypes = [
  ctypes.c_char_p, #pNetworkName
  ctypes.POINTER(xlClasses.XLnetworkHandle), #pNetworkHandle
  ctypes.c_char_p, #pAppName
  ctypes.c_uint, #accessType
  ctypes.c_uint, #queueSize
]
xlNetEthOpenNetwork.errcheck = check_xl_status

xlNetCloseNetwork = _vector_xlapi_dll_.xlNetCloseNetwork
xlNetCloseNetwork.restype = xlClasses.XLstatus
xlNetCloseNetwork.argtypes = [
  xlClasses.XLnetworkHandle, #networkHandle
]
xlNetCloseNetwork.errcheck = check_xl_status

xlNetOpenVirtualPort = _vector_xlapi_dll_.xlNetOpenVirtualPort
xlNetOpenVirtualPort.restype = xlClasses.XLstatus
xlNetOpenVirtualPort.argtypes = [
  xlClasses.XLnetworkHandle, #networkHandle
  ctypes.c_char_p, #pVPortName
  ctypes.POINTER(xlClasses.XLethPortHandle), #pEthPortHandle
  xlClasses.XLrxHandle, #rxHandle
]
xlNetOpenVirtualPort.errcheck = check_xl_status

xlNetAddVirtualPort = _vector_xlapi_dll_.xlNetAddVirtualPort
xlNetAddVirtualPort.restype = xlClasses.XLstatus
xlNetAddVirtualPort.argtypes = [
  xlClasses.XLnetworkHandle, #networkHandle
  ctypes.c_char_p, #pSwitchName
  ctypes.c_char_p, #pVPortName
  ctypes.POINTER(xlClasses.XLethPortHandle), #pEthPortHandle
  xlClasses.XLrxHandle, #rxHandle
]
xlNetAddVirtualPort.errcheck = check_xl_status

xlNetConnectMeasurementPoint = _vector_xlapi_dll_.xlNetConnectMeasurementPoint
xlNetConnectMeasurementPoint.restype = xlClasses.XLstatus
xlNetConnectMeasurementPoint.argtypes = [
  xlClasses.XLnetworkHandle, #networkHandle
  ctypes.c_char_p, #pPortName
  ctypes.POINTER(xlClasses.XLethPortHandle), #pEthPortHandle
  xlClasses.XLrxHandle, #rxHandle
]
xlNetConnectMeasurementPoint.errcheck = check_xl_status

xlNetActivateNetwork = _vector_xlapi_dll_.xlNetActivateNetwork
xlNetActivateNetwork.restype = xlClasses.XLstatus
xlNetActivateNetwork.argtypes = [
  xlClasses.XLnetworkHandle, #networkHandle
]
xlNetActivateNetwork.errcheck = check_xl_status

xlNetDeactivateNetwork = _vector_xlapi_dll_.xlNetDeactivateNetwork
xlNetDeactivateNetwork.restype = xlClasses.XLstatus
xlNetDeactivateNetwork.argtypes = [
  xlClasses.XLnetworkHandle, #networkHandle
]
xlNetDeactivateNetwork.errcheck = check_xl_status

xlNetEthSend = _vector_xlapi_dll_.xlNetEthSend
xlNetEthSend.restype = xlClasses.XLstatus
xlNetEthSend.argtypes = [
  xlClasses.XLnetworkHandle, #networkHandle
  xlClasses.XLethPortHandle, #ethPortHandle
  xlClasses.XLuserHandle, #userHandle
  ctypes.POINTER(xlClasses.T_XL_NET_ETH_DATAFRAME_TX), #pEthTxFrame
]
xlNetEthSend.errcheck = check_xl_status

xlNetEthReceive = _vector_xlapi_dll_.xlNetEthReceive
xlNetEthReceive.restype = xlClasses.XLstatus
xlNetEthReceive.argtypes = [
  xlClasses.XLnetworkHandle, #networkHandle
  ctypes.POINTER(xlClasses.T_XL_NET_ETH_EVENT), #pEventBuffer
  ctypes.POINTER(ctypes.c_uint), #pRxHandleCount
  ctypes.POINTER(xlClasses.XLrxHandle), #pRxHandle
]
xlNetEthReceive.errcheck = check_xl_status

xlNetEthRequestChannelStatus = _vector_xlapi_dll_.xlNetEthRequestChannelStatus
xlNetEthRequestChannelStatus.restype = xlClasses.XLstatus
xlNetEthRequestChannelStatus.argtypes = [
  xlClasses.XLnetworkHandle, #networkHandle
]
xlNetEthRequestChannelStatus.errcheck = check_xl_status

xlNetSetNotification = _vector_xlapi_dll_.xlNetSetNotification
xlNetSetNotification.restype = xlClasses.XLstatus
xlNetSetNotification.argtypes = [
  xlClasses.XLnetworkHandle, #networkHandle
  ctypes.POINTER(xlClasses.XLhandle), #pHandle
  ctypes.c_int, #queueLevel
]
xlNetSetNotification.errcheck = check_xl_status

xlNetRequestMACAddress = _vector_xlapi_dll_.xlNetRequestMACAddress
xlNetRequestMACAddress.restype = xlClasses.XLstatus
xlNetRequestMACAddress.argtypes = [
  xlClasses.XLnetworkHandle, #networkHandle
  ctypes.POINTER(xlClasses.T_XL_ETH_MAC_ADDRESS), #pMACAddress
]
xlNetRequestMACAddress.errcheck = check_xl_status

xlNetReleaseMACAddress = _vector_xlapi_dll_.xlNetReleaseMACAddress
xlNetReleaseMACAddress.restype = xlClasses.XLstatus
xlNetReleaseMACAddress.argtypes = [
  xlClasses.XLnetworkHandle, #networkHandle
  ctypes.POINTER(xlClasses.T_XL_ETH_MAC_ADDRESS), #pMACAddress
]
xlNetReleaseMACAddress.errcheck = check_xl_status

xlNetFlushReceiveQueue = _vector_xlapi_dll_.xlNetFlushReceiveQueue
xlNetFlushReceiveQueue.restype = xlClasses.XLstatus
xlNetFlushReceiveQueue.argtypes = [
  xlClasses.XLnetworkHandle, #networkHandle
]
xlNetFlushReceiveQueue.errcheck = check_xl_status

xlA429Receive = _vector_xlapi_dll_.xlA429Receive
xlA429Receive.restype = xlClasses.XLstatus
xlA429Receive.argtypes = [
  xlClasses.XLportHandle, #portHandle
  ctypes.POINTER(xlClasses.XLa429RxEvent), #pXlA429RxEvt
]
xlA429Receive.errcheck = check_xl_status

xlA429SetChannelParams = _vector_xlapi_dll_.xlA429SetChannelParams
xlA429SetChannelParams.restype = xlClasses.XLstatus
xlA429SetChannelParams.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  ctypes.POINTER(xlClasses.XL_A429_PARAMS), #pXlA429Params
]
xlA429SetChannelParams.errcheck = check_xl_status

xlA429Transmit = _vector_xlapi_dll_.xlA429Transmit
xlA429Transmit.restype = xlClasses.XLstatus
xlA429Transmit.argtypes = [
  xlClasses.XLportHandle, #portHandle
  xlClasses.XLaccess, #accessMask
  ctypes.c_uint, #msgCnt
  ctypes.POINTER(ctypes.c_uint), #pMsgCntSent
  ctypes.POINTER(xlClasses.XL_A429_MSG_TX), #pXlA429MsgTx
]
xlA429Transmit.errcheck = check_xl_status

xlGetKeymanBoxes = _vector_xlapi_dll_.xlGetKeymanBoxes
xlGetKeymanBoxes.restype = xlClasses.XLstatus
xlGetKeymanBoxes.argtypes = [
  ctypes.POINTER(ctypes.c_uint), #boxCount
]
xlGetKeymanBoxes.errcheck = check_xl_status

xlGetKeymanInfo = _vector_xlapi_dll_.xlGetKeymanInfo
xlGetKeymanInfo.restype = xlClasses.XLstatus
xlGetKeymanInfo.argtypes = [
  ctypes.c_uint, #boxIndex
  ctypes.POINTER(ctypes.c_uint), #boxMask
  ctypes.POINTER(ctypes.c_uint), #boxSerial
  ctypes.POINTER(xlClasses.XLuint64), #licInfo
]
xlGetKeymanInfo.errcheck = check_xl_status

