import traceback
import sys
'''
def getTraceback(tbObj):
    tb = 'Traceback (most recent call last):\n'
    tbList = traceback.extract_tb(tbObj)
    for file, line, func, caller in iter(tbList):
        tb += 'File %s, line %s, in %s\n %s\n' %(file, line, func, caller)
    sys.__stdout__.write(tb)
    return tb
'''

class wrongPassword(Exception):
    pass

class patternNotReceived(Exception):
    pass

class deviceNotFound(Exception):
    pass

class linkNotFound(Exception):
    pass

class configFailed(Exception):
    pass

class reloadFailed(Exception):
    pass

class threadFailed(Exception):
    pass

class deviceNotInDb(Exception):
    pass

class noDeviceObjAvailable(Exception):
    pass

class noSuchClass(Exception):
    pass

class devObjExists(Exception):
    pass

class FailOverFailed(Exception):
    pass

class trafficGenError(Exception):
    pass

class testFailed(Exception):
    pass

class topologyUnavailable(Exception):
    pass

class UnableToLoadTheImage(Exception):
    pass

class AttributeNotFound(Exception):
    pass

class PromptNotFound(Exception) :
    pass

class noCleanProcedure(Exception) :
    pass

class powerCycleFailed(Exception) :
    pass
