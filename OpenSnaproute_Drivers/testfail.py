"""
testfail is the basic driver which will handle all the Exceptions raised.
"""
import traceback
import sys
"""
def getTraceback(tbObj):
    tb = 'Traceback (most recent call last):\n'
    tbList = traceback.extract_tb(tbObj)
    for file, line, func, caller in iter(tbList):
        tb += 'File %s, line %s, in %s\n %s\n' %(file, line, func, caller)
    sys.__stdout__.write(tb)
    return tb
"""

class WrongPassword(Exception):
    pass

class PatternNotReceived(Exception):
    pass

class DeviceNotFound(Exception):
    pass

class LinkNotFound(Exception):
    pass

class ConfigFailed(Exception):
    pass

class ReloadFailed(Exception):
    pass

class ThreadFailed(Exception):
    pass

class DeviceNotInDb(Exception):
    pass

class NoDeviceObjAvailable(Exception):
    pass

class NoSuchClass(Exception):
    pass

class DevObjExists(Exception):
    pass

class FailOverFailed(Exception):
    pass

class TrafficGenError(Exception):
    pass

class TestFailed(Exception):
    pass

class TopologyUnavailable(Exception):
    pass

class UnableToLoadTheImage(Exception):
    pass

class AttributeNotFound(Exception):
    pass

class PromptNotFound(Exception):
    pass

class NoCleanProcedure(Exception):
    pass

class PowerCycleFailed(Exception):
    pass
