#!/usr/bin/python
"""
flexprint.py
"""
import json
import urllib2
from flexswitchV2 import FlexSwitch
from tablePrint import *

HEADERS = {'Accept' : 'application/json', 'Content-Type' : 'application/json'}
class FlexSwitchShow(object):
    httpSuccessCodes = [200, 201, 202, 204]
    def __init__(self, ip, port):
        self.switch = FlexSwitch(ip, port)

    def table_print_object(self, obj_name, header, values_list):
        """
        Prints the data in a table format
        obj_name - Object which is being printed
        keys - This will be the attributes of the obj and column names
        valueList - List of tuples containing the data to be put into
                    the rows_list.  Each attribute must be in string format
        """
        def terminal_size():
            import fcntl, termios, struct
            h, w, hp, wp = struct.unpack('HHHH',
                                         fcntl.ioctl(0, termios.TIOCGWINSZ,
                                                     struct.pack('HHHH', 0, 0, 0, 0)))
            return h, w

        labels_value = header
        rows_list = values_list

        height, width_value = terminal_size()
        if labels_value:
            width_value = (width_value / len(labels_value)) + 5
            var1 = indent([labels_value]+rows_list, has_header=True, separate_rows=True,
                          prefix=' ', postfix=' ', header_char= '-', delimit='    ',
                          wrapfunc=lambda x: wrap_onspace_strict(x, width_value))

            return var1
        elif rows_list:
            width_value = (width_value / len(rows_list[0])) + 5
            var1 = indent(rows_list, has_header=False, separate_rows=True,
                          prefix=' ', postfix=' ', header_char= '-', delimit='    ',
                          wrapfunc=lambda x: wrap_onspace_strict(x, width_value))
            return var1
        else:
            print('No Data To Display for %s' % obj_name)
            return 0

    def print_lldp_intf_states(self, add_header=True, brief=None):
        header = []
        rows_list = []
        if add_header:
            header.append('IntfRef')
            header.append('IfIndex')
            header.append('SendFrames')
            header.append('ReceivedFrames')
            header.append('Enable')
            header.append('LocalPort')
            header.append('PeerMac')
            header.append('PeerPort')
            header.append('PeerHostName')
            header.append('HoldTime')
            header.append('SystemDescription')
            header.append('SystemCapabilities')
            header.append('EnabledCapabilities')

        objs = self.switch.get_all_lldp_intf_states()
        for obj in objs:
            o = obj['Object']
            values_list = []
            values_list.append('%s' % o['IntfRef'])
            values_list.append('%s' % o['IfIndex'])
            values_list.append('%s' % o['SendFrames'])
            values_list.append('%s' % o['ReceivedFrames'])
            values_list.append('%s' % o['Enable'])
            values_list.append('%s' % o['LocalPort'])
            values_list.append('%s' % o['PeerMac'])
            values_list.append('%s' % o['PeerPort'])
            values_list.append('%s' % o['PeerHostName'])
            values_list.append('%s' % o['HoldTime'])
            values_list.append('%s' % o['SystemDescription'])
            values_list.append('%s' % o['SystemCapabilities'])
            values_list.append('%s' % o['EnabledCapabilities'])
            rows_list.append(values_list)
        var1 = self.table_print_object('LLDPIntfState', header, rows_list)
        return var1


    def print_combined_vlan_states(self, add_header=True, brief=None):
        header = []
        rows_list = []
        if add_header:
            header.append('VlanId')
            header.append('VlanName')
            header.append('OperState')
            header.append('IfIndex')
            #header.append('SysInternalDescription')
            header.append('IntfList')
            header.append('UntagIntfList')
            #header.append('AdminState')

        objs = self.switch.get_all_vlan_states()
        for obj in objs:
            o = obj['Object']
            values_list = []
            values_list.append('%s' % o['VlanId'])
            values_list.append('%s' % o['VlanName'])
            values_list.append('%s' % o['OperState'])
            values_list.append('%s' % o['IfIndex'])
            #values_list.append('%s' % o['SysInternalDescription'])
            r = self.switch.get_vlan(o['VlanId'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
                values_list.append('%s' % o['IntfList'])
                values_list.append('%s' % o['UntagIntfList'])
                #values_list.append('%s' % o['AdminState'])
            rows_list.append(values_list)
        var = self.table_print_object('VlanState', header, rows_list)
        return var
