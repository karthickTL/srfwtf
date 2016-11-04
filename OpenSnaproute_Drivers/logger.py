import robot.api.logger
from robot.output import Message
from robot.output.logger import LOGGER
import threading
from robot.version import get_version
ROBOT_VERSION = get_version()
if ROBOT_VERSION == '2.8.4':
    from robot.running.timeouts import timeoutthread
import sys
#from dataStructure import nestedDict
#import const
import os

if ROBOT_VERSION == '2.8.4':
    LOGGING_THREADS = ('MainThread', timeoutthread.TIMEOUT_THREAD_NAME)
else:
    LOGGING_THREADS = ('MainThread')

#threadDict = nestedDict()
logThreadLock = threading.Lock()
if 'LOG_LEVEL' in os.environ:
    debugLogLevel = int(os.environ['LOG_LEVEL'])
else:
    debugLogLevel = 0

def info(msg, html=True, also_console=True,timestamp=None):
    currentThread = threading.currentThread()
    if currentThread.getName() in LOGGING_THREADS:
        logMsg = Message(msg, 'INFO', html, timestamp=timestamp)
        LOGGER.log_message(logMsg)
        if also_console:
            sys.__stdout__.write('\n\x1b[5;36mINFO          : %s\x1b[0m' %(msg))
    else:
        if also_console:
             sys.__stdout__.write("\n%s" %(msg))
        logMsg = Message(msg,'INFO',html,timestamp=timestamp)
        if currentThread in threadDict:
            threadDict[currentThread]['msgList'].append(logMsg)
        else:
            threadDict[currentThread]['msgList'] = []
            threadDict[currentThread]['msgList'].append(logMsg)

def case(msg,step='', html=True, also_console=True, timestamp=None):
    strLen = len(msg)
    fontTag = '<font color=\"blue\"><strong> TEST-CASE: </strong>'
    fontEndTag = '</font>'
    info("%s %s %s" %(fontTag, msg, fontEndTag), html, also_console=False,timestamp=timestamp)
    if also_console and step=='':
        sys.__stdout__.write("\n\n\n\n\n\x1b[1;33mCASE          : %s\x1b[0m" %(msg))
    elif also_console and step!='':
        sys.__stdout__.write("\n\n\n\n\n\x1b[1;33mTEST-CASE %s: %s\x1b[0m" %(step,msg))

'''
def details(msg,step='', html=True, also_console=False, timestamp=None):
    strLen = len(msg)
    fontTag = '<font color=\"black\"><strong> DETAILS: </strong>'
    fontEndTag = '</font>'
    info("%s %s %s" %(fontTag, msg, fontEndTag), html, also_console=False,timestamp=timestamp)
    if also_console and step=='':
        sys.__stdout__.write("\n\x1b[1;30mDETAILS       : %s\x1b[0m" %(msg))
    elif also_console and step!='':
        sys.__stdout__.write("\n\x1b[1;30mSTEP-DETAILS %s: %s\x1b[0m" %(step,msg))'''

def details(msg, html=True, also_console=True,timestamp=None):
    currentThread = threading.currentThread()
    if currentThread.getName() in LOGGING_THREADS:
        logMsg = Message(msg, 'INFO', html, timestamp=timestamp)
        LOGGER.log_message(logMsg)
        if also_console:
            sys.__stdout__.write('\n\x1b[5;36mINFO          : %s\x1b[0m' %(msg))
    else:
        if also_console:
             sys.__stdout__.write("\n%s" %(msg))
        logMsg = Message(msg,'INFO',html,timestamp=timestamp)
        if currentThread in threadDict:
            threadDict[currentThread]['msgList'].append(logMsg)
        else:
            threadDict[currentThread]['msgList'] = []
            threadDict[currentThread]['msgList'].append(logMsg)




def alert(msg,step='', html=True, also_console=True, timestamp=None):
    strLen = len(msg)
    fontTag = '<font color=\"black\"><strong> DETAILS: </strong>'
    fontEndTag = '</font>'
    info("%s %s %s" %(fontTag, msg, fontEndTag), html, also_console=False,timestamp=timestamp)
    if also_console and step=='':
        sys.__stdout__.write("\n\x1b[1;30mALERT_MESSAGE : %s\x1b[0m" %(msg))
    elif also_console and step!='':
        sys.__stdout__.write("\n\x1b[1;30mSTEP-DETAILS %s: %s\x1b[0m" %(step,msg))




def step(msg,step='', html=True, also_console=True, timestamp=None):
    strLen = len(msg)
    fontTag = '<font color=\"blue\"><strong> CHECKPOINT: </strong>'
    fontEndTag = '</font>'
    info("%s %s %s" %(fontTag, msg, fontEndTag), html, also_console=False,timestamp=timestamp)
    if also_console and step=='':
        sys.__stdout__.write("\n\n\x1b[1;34mCHECKPOINT    : %s\x1b[0m" %(msg))
    elif also_console and step!='':
        sys.__stdout__.write("\n\x1b[1;34mCHECKPOINT %s: %s\x1b[0m" %(step,msg))

def error(msg, html=True, also_console=False,timestamp=None):
    fontTag = '<font color=\"red\"><b> ERROR: '
    fontEndTag = '</b></font>'
    info("%s %s %s" %(fontTag, msg, fontEndTag), html, also_console=False,timestamp=timestamp)
    if also_console:
        sys.__stdout__.write('\n\x1b[31mERROR: %s\x1b[0m' %(msg))

def warn(msg, html=True, also_console=True,timestamp=None):
    fontTag = '<font color=\"yellow\"><b> WARNING: '
    fontEndTag = '</b></font>'
    info("%s %s %s" %(fontTag, msg, fontEndTag), html, also_console=False,timestamp=timestamp)
    if also_console:
        sys.__stdout__.write('\n\x1b[35mWARNING: %s\x1b[0m' %(msg))

def fail(msg, html=True, also_console=True,timestamp=None):
    fontTag = '<font color=\"red\"><b> FAIL: '
    fontEndTag = '</b></font>'
    failmsg = "%s %s %s" %(fontTag, msg, fontEndTag)
    currentThread = threading.currentThread()
    sys.__stdout__.write('\n\x1b[38;5;1mFAIL: %s\x1b[0m' %(msg))
    if currentThread.getName() in LOGGING_THREADS:
        logMsg = Message(failmsg, 'FAIL', html, timestamp=timestamp)
        LOGGER.log_message(logMsg)
        if also_console:
            sys.__stdout__.write('\n %s' %(msg))
    else:
        if also_console:
             sys.__stdout__.write("\n%s" %(msg))
        logMsg = Message(msg,'FAIL',html,timestamp=timestamp)
        if currentThread in threadDict:
            threadDict[currentThread]['msgList'].append(logMsg)
        else:
            threadDict[currentThread]['msgList'] = []
            threadDict[currentThread]['msgList'].append(logMsg)

def success(msg, html=True, also_console=True,timestamp=None):
    fontTag = '<font color=\"green\"><b> PASS:'
    fontEndTag = '</b></font>'
    info("%s %s %s" %(fontTag, msg, fontEndTag), html, also_console=False,timestamp=timestamp)
    if also_console:
        sys.__stdout__.write('\n\x1b[32mPASS RESULT   : %s\x1b[0m' %(msg))

def failure(msg, html=True, also_console=True,timestamp=None):
    fontTag = '<font color=\"red\"><b> FAIL:'
    fontEndTag = '</b></font>'
    info("%s %s %s" %(fontTag, msg, fontEndTag), html, also_console=False,timestamp=timestamp)
    if also_console:
        sys.__stdout__.write('\n\x1b[38;5;1mFAIL: %s\x1b[0m' %(msg))

def debug(msg, html=True, timestamp=None, level=0):
    currentThread = threading.currentThread()
    if currentThread.getName() in LOGGING_THREADS:
        if level <= debugLogLevel:
            logMsg = Message(msg, 'DEBUG', html, timestamp=timestamp)
            LOGGER.log_message(logMsg)
    else:
        if level <= debugLogLevel:
            logMsg = Message(msg,'DEBUG',html,timestamp=timestamp)
            if currentThread in threadDict:
                threadDict[currentThread]['msgList'].append(logMsg)
            else:
                threadDict[currentThread]['msgList'] = []
                threadDict[currentThread]['msgList'].append(logMsg)


def flushThreadLog(threadList):
    #global threadDict
    #global logThreadLock
    currentThread = threading.currentThread()
    for thread in threadList:
        if thread == currentThread:
            continue
        elif currentThread.getName() not in LOGGING_THREADS:
            for msg in threadDict[thread]['msgList']:
                logThreadLock.acquire()
                debug('flushThreadLog - lock acquired by thread %s' %thread.threadId, level=const.LEVEL4)
                try:
                    threadDict[currentThread]['msgList'].append(msg)
                except:
                    sys.__stdout__.write(sys.exc_info())
                    logThreadLock.release()
                    debug('flushThreadLog - lock released by thread %s' %thread.threadId, level=const.LEVEL4)
                logThreadLock.release()
                debug('flushThreadLog - lock released by thread %s' %thread.threadId, level=const.LEVEL4)
            threadDict.pop(thread, None)
        else:
            for msg in threadDict[thread]['msgList']:
                LOGGER.log_message(msg)
            threadDict.pop(thread, None)

def testcase_log(f10TcInfo, tcid=None, result='PASS'):
    if tcid is None:
        msgList = f10TcInfo['msgList']
        timestampList = f10TcInfo['timestamps']
        if f10TcInfo['result']:
            result = f10TcInfo['result']
    else:
        msgList = f10TcInfo[tcid]['msgList']
        timestampList = f10TcInfo[tcid]['timestamps']
        if f10TcInfo[tcid]['result']:
            result = f10TcInfo[tcid]['result']
    for msg,timestamp in zip(msgList, timestampList) :
        info(msg,timestamp=timestamp,also_console=False)
    if result == 'FAIL' or result == 'TERMINATED':
        assert False, "Test failed"


def setup_log(setupLog):
    msgList = setupLog["msgList"]
    timestampList = setupLog["timestamps"]
    for msg, timestamp in zip(msgList, timestampList):
        info(msg, timestamp=timestamp, also_console=False)

def cleanup_log(cleanupLog):
    msgList = cleanupLog["msgList"]
    timestampList = cleanupLog["timestamps"]
    for msg, timestamp in zip(msgList, timestampList):
        info(msg, timestamp=timestamp, also_console=False)
