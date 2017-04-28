import threading
import robot.api.logger
from robot.output import Message
from robot.output.logger import LOGGER
from robot.version import get_version


ROBOT_VERSION = get_version()
if ROBOT_VERSION == '2.8.4':
    from robot.running.timeouts import timeoutthread
import sys
# from dataStructure import nestedDict
# import const
import os

if ROBOT_VERSION == '2.8.4':
    LOGGING_THREADS = ('MainThread', timeoutthread.TIMEOUT_THREAD_NAME)
else:
    LOGGING_THREADS = 'MainThread'

# threadDict = nestedDict()
LOG_THREAD_LOCK = threading.Lock()
if 'LOG_LEVEL' in os.environ:
    DEBUG_LOG_LEVEL = int(os.environ['LOG_LEVEL'])
else:
    DEBUG_LOG_LEVEL = 0


def info(msg, html=True, also_console=True, timestamp=None):
    current_thread = threading.currentThread()
    log_msg = ''
    if current_thread.getName() in LOGGING_THREADS:
        log_msg = Message(msg, 'INFO', html, timestamp=timestamp)
        LOGGER.log_message(log_msg)
        if also_console:
            sys.__stdout__.write('\n\x1b[5;36mINFO          : %s\x1b[0m' % msg)
    else:
        if also_console:
            sys.__stdout__.write("\n%s" % msg)
            log_msg = Message(msg, 'INFO', html, timestamp=timestamp)
        if current_thread in threadDict:
            threadDict[current_thread]['msg_list'].append(log_msg)
        else:
            threadDict[current_thread]['msg_list'] = []
            threadDict[current_thread]['msg_list'].append(log_msg)


def case(msg, step_value='', html=True, also_console=True, timestamp=None):
    str_len = len(msg)
    font_tag = '<font color=\"blue\"><strong> TEST-CASE: </strong>'
    font_end_tag = '</font>'
    info("%s %s %s" % (font_tag, msg, font_end_tag), html, also_console=False, timestamp=timestamp)
    if also_console and step_value == '':
        sys.__stdout__.write("\n\n\n\n\n\x1b[1;33mCASE          : %s\x1b[0m" % msg)
    elif also_console and step_value != '':
        sys.__stdout__.write("\n\n\n\n\n\x1b[1;33mTEST-CASE %s: %s\x1b[0m" % (step_value, msg))


def details(msg, html=True, also_console=True, timestamp=None):
    current_thread = threading.currentThread()
    if current_thread.getName() in LOGGING_THREADS:
        log_msg = Message(msg, 'INFO', html, timestamp=timestamp)
        LOGGER.log_message(log_msg)
        if also_console:
            sys.__stdout__.write('\n\x1b[5;36mINFO          : %s\x1b[0m' % msg)
    else:
        if also_console:
            sys.__stdout__.write("\n%s" % msg)
        log_msg = Message(msg, 'INFO', html, timestamp=timestamp)
        if current_thread in threadDict:
            threadDict[current_thread]['msg_list'].append(log_msg)
        else:
            threadDict[current_thread]['msg_list'] = []
            threadDict[current_thread]['msg_list'].append(log_msg)


def alert(msg, step_value='', html=True, also_console=True, timestamp=None):
    str_len = len(msg)
    font_tag = '<font color=\"black\"><strong> DETAILS: </strong>'
    font_end_tag = '</font>'
    info("%s %s %s" % (font_tag, msg, font_end_tag), html, also_console=False, timestamp=timestamp)
    if also_console and step_value == '':
        sys.__stdout__.write("\n\x1b[1;30mALERT_MESSAGE : %s\x1b[0m" % msg)
    elif also_console and step_value != '':
        sys.__stdout__.write("\n\x1b[1;30mstep_value-DETAILS %s: %s\x1b[0m" % (step_value, msg))


def step(msg, step_value='', html=True, also_console=True, timestamp=None):
    str_len = len(msg)
    font_tag = '<font color=\"blue\"><strong> CHECKPOINT: </strong>'
    font_end_tag = '</font>'
    info("%s %s %s" % (font_tag, msg, font_end_tag), html, also_console=False, timestamp=timestamp)
    if also_console and step_value == '':
        sys.__stdout__.write("\n\n\x1b[1;34mCHECKPOINT    : %s\x1b[0m" % msg)
    elif also_console and step_value != '':
        sys.__stdout__.write("\n\x1b[1;34mCHECKPOINT %s: %s\x1b[0m" % (step_value, msg))


def error(msg, html=True, also_console=False, timestamp=None):
    font_tag = '<font color=\"red\"><b> ERROR: '
    font_end_tag = '</b></font>'
    info("%s %s %s" % (font_tag, msg, font_end_tag), html, also_console=False, timestamp=timestamp)
    if also_console:
        sys.__stdout__.write('\n\x1b[31mERROR: %s\x1b[0m' % msg)


def warn(msg, html=True, also_console=True, timestamp=None):
    font_tag = '<font color=\"yellow\"><b> WARNING: '
    font_end_tag = '</b></font>'
    info("%s %s %s" % (font_tag, msg, font_end_tag), html, also_console=False, timestamp=timestamp)
    if also_console:
        sys.__stdout__.write('\n\x1b[35mWARNING: %s\x1b[0m' % msg)


def fail(msg, html=True, also_console=True, timestamp=None):
    font_tag = '<font color=\"red\"><b> FAIL: '
    font_end_tag = '</b></font>'
    failmsg = "%s %s %s" % (font_tag, msg, font_end_tag)
    current_thread = threading.currentThread()
    sys.__stdout__.write('\n\x1b[38;5;1mFAIL: %s\x1b[0m' % msg)
    if current_thread.getName() in LOGGING_THREADS:
        log_msg = Message(failmsg, 'FAIL', html, timestamp=timestamp)
        LOGGER.log_message(log_msg)
        if also_console:
            sys.__stdout__.write('\n %s' % msg)
    else:
        if also_console:
            sys.__stdout__.write("\n%s" % msg)
        log_msg = Message(msg, 'FAIL', html, timestamp=timestamp)
        if current_thread in threadDict:
            threadDict[current_thread]['msg_list'].append(log_msg)
        else:
            threadDict[current_thread]['msg_list'] = []
            threadDict[current_thread]['msg_list'].append(log_msg)


def success(msg, html=True, also_console=True, timestamp=None):
    font_tag = '<font color=\"green\"><b> PASS:'
    font_end_tag = '</b></font>'
    info("%s %s %s" % (font_tag, msg, font_end_tag), html, also_console=False, timestamp=timestamp)
    if also_console:
        sys.__stdout__.write('\n\x1b[32mPASS RESULT   : %s\x1b[0m' % msg)


def failure(msg, html=True, also_console=True, timestamp=None):
    font_tag = '<font color=\"red\"><b> FAIL:'
    font_end_tag = '</b></font>'
    info("%s %s %s" % (font_tag, msg, font_end_tag), html, also_console=False, timestamp=timestamp)
    if also_console:
        sys.__stdout__.write('\n\x1b[38;5;1mFAIL: %s\x1b[0m' % msg)


def debug(msg, html=True, timestamp=None, level=0):
    current_thread = threading.currentThread()
    if current_thread.getName() in LOGGING_THREADS:
        if level <= DEBUG_LOG_LEVEL:
            log_msg = Message(msg, 'DEBUG', html, timestamp=timestamp)
            LOGGER.log_message(log_msg)
    else:
        if level <= DEBUG_LOG_LEVEL:
            log_msg = Message(msg, 'DEBUG', html, timestamp=timestamp)
            if current_thread in threadDict:
                threadDict[current_thread]['msg_list'].append(log_msg)
            else:
                threadDict[current_thread]['msg_list'] = []
                threadDict[current_thread]['msg_list'].append(log_msg)


def flush_thread_log(thread_list):
    current_thread = threading.currentThread()
    for thread in thread_list:
        if thread == current_thread:
            continue
        elif current_thread.getName() not in LOGGING_THREADS:
            for msg in threadDict[thread]['msg_list']:
                LOG_THREAD_LOCK.acquire()
                debug('flushThreadLog - lock acquired by thread %s' % thread.threadId, level=const.LEVEL4)
                try:
                    threadDict[current_thread]['msg_list'].append(msg)
                except Exception:
                    sys.__stdout__.write(sys.exc_info())
                    LOG_THREAD_LOCK.release()
                    debug('flushThreadLog - lock released by thread %s' % thread.threadId, level=const.LEVEL4)
                LOG_THREAD_LOCK.release()
                debug('flushThreadLog - lock released by thread %s' % thread.threadId, level=const.LEVEL4)
            threadDict.pop(thread, None)
        else:
            for msg in threadDict[thread]['msg_list']:
                LOGGER.log_message(msg)
            threadDict.pop(thread, None)


def testcase_log(f10_tc_info, tcid=None, result='PASS'):
    if tcid is None:
        msg_list = f10_tc_info['msg_list']
        timestamp_list = f10_tc_info['timestamps']
        if f10_tc_info['result']:
            result = f10_tc_info['result']
    else:
        msg_list = f10_tc_info[tcid]['msg_list']
        timestamp_list = f10_tc_info[tcid]['timestamps']
        if f10_tc_info[tcid]['result']:
            result = f10_tc_info[tcid]['result']
    for msg, timestamp in zip(msg_list, timestamp_list):
        info(msg, timestamp=timestamp, also_console=False)
    if result == 'FAIL' or result == 'TERMINATED':
        assert False, "Test failed"


def setup_log(setuplog):
    msg_list = setuplog["msg_list"]
    timestamp_list = setuplog["timestamps"]
    for msg, timestamp in zip(msg_list, timestamp_list):
        info(msg, timestamp=timestamp, also_console=False)


def cleanup_log(cleanuplog):
    msg_list = cleanuplog["msg_list"]
    timestamp_list = cleanuplog["timestamps"]
    for msg, timestamp in zip(msg_list, timestamp_list):
        info(msg, timestamp=timestamp, also_console=False)
