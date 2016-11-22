#!/usr/bin/python                                                                                                       
import requests
import json
import urllib2
from flexswitchV2 import FlexSwitch
from tablePrint import *

headers = {'Accept' : 'application/json', 'Content-Type' : 'application/json'}
class FlexSwitchShow( object):
    httpSuccessCodes = [200, 201, 202, 204]
    def  __init__ (self, ip, port):
        self.swtch = FlexSwitch(ip, port)

    def tblPrintObject(self, objName, headers, valuesList):
        '''
        Prints the data in a table format
        objName - Object which is being printed
        keys - This will be the attributes of the obj and column names
        valueList - List of tuples containing the data to be put into
                    the rows.  Each attribute must be in string format
        '''
        def terminal_size():
            import fcntl, termios, struct
            h, w, hp, wp = struct.unpack('HHHH',
                fcntl.ioctl(0, termios.TIOCGWINSZ,
                struct.pack('HHHH', 0, 0, 0, 0)))
            return h, w

        labels = headers
        rows=valuesList

        height, width = terminal_size()
        if labels:
            width = (width / len(labels)) + 5
            var1=indent([labels]+rows, hasHeader=True, separateRows=True,
                     prefix=' ', postfix=' ', headerChar= '-', delim='    ',
                 wrapfunc=lambda x: wrap_onspace_strict(x,width))

            return var1
        elif rows:
            width = (width / len(rows[0])) + 5
            var1=indent(rows, hasHeader=False, separateRows=True,
                     prefix=' ', postfix=' ', headerChar= '-', delim='    ',
                 wrapfunc=lambda x: wrap_onspace_strict(x,width))
            return var1
        else:
            print 'No Data To Display for %s' %(objName)
            return 0

    def printArpEntryStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IpAddr')
            header.append('MacAddr')
            header.append('Vlan')
            header.append('Intf')
            header.append('ExpiryTimeLeft')

        objs = self.swtch.getAllArpEntryStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IpAddr'])
            values.append('%s' % o['MacAddr'])
            values.append('%s' % o['Vlan'])
            values.append('%s' % o['Intf'])
            values.append('%s' % o['ExpiryTimeLeft'])
            rows.append(values)
        self.tblPrintObject('ArpEntryState', header, rows)


    def printArpEntryState(self, IpAddr, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IpAddr')
            header.append('MacAddr')
            header.append('Vlan')
            header.append('Intf')
            header.append('ExpiryTimeLeft')

        rawobj = self.swtch.getArpEntryState(
                                             IpAddr)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['IpAddr'])
            values.append('%s' % o['MacAddr'])
            values.append('%s' % o['Vlan'])
            values.append('%s' % o['Intf'])
            values.append('%s' % o['ExpiryTimeLeft'])
            rows.append(values)
            self.tblPrintObject('ArpEntryState', header, rows)

        else:
            print rawobj.content

    def printPlatformMgmtDeviceStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('DeviceName')
            header.append('Uptime')
            header.append('Description')
            header.append('ResetReason')
            header.append('MemoryUsage')
            header.append('Version')
            header.append('CPUUsage')

        objs = self.swtch.getAllPlatformMgmtDeviceStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['DeviceName'])
            values.append('%s' % o['Uptime'])
            values.append('%s' % o['Description'])
            values.append('%s' % o['ResetReason'])
            values.append('%s' % o['MemoryUsage'])
            values.append('%s' % o['Version'])
            values.append('%s' % o['CPUUsage'])
            rows.append(values)
        self.tblPrintObject('PlatformMgmtDeviceState', header, rows)


    def printPlatformMgmtDeviceState(self, DeviceName, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('DeviceName')
            header.append('Uptime')
            header.append('Description')
            header.append('ResetReason')
            header.append('MemoryUsage')
            header.append('Version')
            header.append('CPUUsage')

        rawobj = self.swtch.getPlatformMgmtDeviceState(
                                                       DeviceName)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['DeviceName'])
            values.append('%s' % o['Uptime'])
            values.append('%s' % o['Description'])
            values.append('%s' % o['ResetReason'])
            values.append('%s' % o['MemoryUsage'])
            values.append('%s' % o['Version'])
            values.append('%s' % o['CPUUsage'])
            rows.append(values)
            self.tblPrintObject('PlatformMgmtDeviceState', header, rows)

        else:
            print rawobj.content

    def printOspfIPv4RouteStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('DestId')
            header.append('DestType')
            header.append('AddrMask')
            header.append('OptCapabilities')
            header.append('AreaId')
            header.append('PathType')
            header.append('Cost')
            header.append('Type2Cost')
            header.append('NumOfPaths')
            header.append('NextHops')
            header.append('LSOrigin')

        objs = self.swtch.getAllOspfIPv4RouteStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['DestId'])
            values.append('%s' % o['DestType'])
            values.append('%s' % o['AddrMask'])
            values.append('%s' % o['OptCapabilities'])
            values.append('%s' % o['AreaId'])
            values.append('%s' % o['PathType'])
            values.append('%s' % o['Cost'])
            values.append('%s' % o['Type2Cost'])
            values.append('%s' % o['NumOfPaths'])
            values.append('%s' % o['NextHops'])
            values.append('%s' % o['LSOrigin'])
            rows.append(values)
        self.tblPrintObject('OspfIPv4RouteState', header, rows)


    def printOspfIPv4RouteState(self, DestId,DestType,AddrMask, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('DestId')
            header.append('DestType')
            header.append('AddrMask')
            header.append('OptCapabilities')
            header.append('AreaId')
            header.append('PathType')
            header.append('Cost')
            header.append('Type2Cost')
            header.append('NumOfPaths')
            header.append('NextHops')
            header.append('LSOrigin')

        rawobj = self.swtch.getOspfIPv4RouteState(
                                                  DestId,
                                                  DestType,
                                                  AddrMask)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['DestId'])
            values.append('%s' % o['DestType'])
            values.append('%s' % o['AddrMask'])
            values.append('%s' % o['OptCapabilities'])
            values.append('%s' % o['AreaId'])
            values.append('%s' % o['PathType'])
            values.append('%s' % o['Cost'])
            values.append('%s' % o['Type2Cost'])
            values.append('%s' % o['NumOfPaths'])
            values.append('%s' % o['NextHops'])
            values.append('%s' % o['LSOrigin'])
            rows.append(values)
            self.tblPrintObject('OspfIPv4RouteState', header, rows)

        else:
            print rawobj.content

    def printTemperatureSensors(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('HigherAlarmThreshold')
            header.append('HigherWarningThreshold')
            header.append('LowerWarningThreshold')
            header.append('LowerAlarmThreshold')
            header.append('PMClassCAdminState')
            header.append('PMClassAAdminState')
            header.append('AdminState')
            header.append('PMClassBAdminState')

        objs = self.swtch.getAllTemperatureSensors()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['HigherAlarmThreshold'])
            values.append('%s' % o['HigherWarningThreshold'])
            values.append('%s' % o['LowerWarningThreshold'])
            values.append('%s' % o['LowerAlarmThreshold'])
            values.append('%s' % o['PMClassCAdminState'])
            values.append('%s' % o['PMClassAAdminState'])
            values.append('%s' % o['AdminState'])
            values.append('%s' % o['PMClassBAdminState'])
            rows.append(values)
        self.tblPrintObject('TemperatureSensor', header, rows)


    def printNdpEntryHwStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IpAddr')
            header.append('MacAddr')
            header.append('Vlan')
            header.append('Port')

        objs = self.swtch.getAllNdpEntryHwStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IpAddr'])
            values.append('%s' % o['MacAddr'])
            values.append('%s' % o['Vlan'])
            values.append('%s' % o['Port'])
            rows.append(values)
        self.tblPrintObject('NdpEntryHwState', header, rows)


    def printNdpEntryHwState(self, IpAddr, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IpAddr')
            header.append('MacAddr')
            header.append('Vlan')
            header.append('Port')

        rawobj = self.swtch.getNdpEntryHwState(
                                               IpAddr)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['IpAddr'])
            values.append('%s' % o['MacAddr'])
            values.append('%s' % o['Vlan'])
            values.append('%s' % o['Port'])
            rows.append(values)
            self.tblPrintObject('NdpEntryHwState', header, rows)

        else:
            print rawobj.content

    def printPolicyStmts(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('Conditions')
            header.append('Action')
            header.append('MatchConditions')

        objs = self.swtch.getAllPolicyStmts()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['Conditions'])
            values.append('%s' % o['Action'])
            values.append('%s' % o['MatchConditions'])
            rows.append(values)
        var =self.tblPrintObject('PolicyStmt', header, rows)
        return var

    def printQsfpChannels(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('ChannelNum')
            header.append('QsfpId')
            header.append('HigherAlarmRXPower')
            header.append('HigherAlarmTXPower')
            header.append('HigherAlarmTXBias')
            header.append('HigherWarningRXPower')
            header.append('HigherWarningTXPower')
            header.append('HigherWarningTXBias')
            header.append('LowerAlarmRXPower')
            header.append('LowerAlarmTXPower')
            header.append('LowerAlarmTXBias')
            header.append('LowerWarningRXPower')
            header.append('LowerWarningTXPower')
            header.append('LowerWarningTXBias')
            header.append('PMClassBAdminState')
            header.append('PMClassCAdminState')
            header.append('PMClassAAdminState')
            header.append('AdminState')

        objs = self.swtch.getAllQsfpChannels()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['ChannelNum'])
            values.append('%s' % o['QsfpId'])
            values.append('%s' % o['HigherAlarmRXPower'])
            values.append('%s' % o['HigherAlarmTXPower'])
            values.append('%s' % o['HigherAlarmTXBias'])
            values.append('%s' % o['HigherWarningRXPower'])
            values.append('%s' % o['HigherWarningTXPower'])
            values.append('%s' % o['HigherWarningTXBias'])
            values.append('%s' % o['LowerAlarmRXPower'])
            values.append('%s' % o['LowerAlarmTXPower'])
            values.append('%s' % o['LowerAlarmTXBias'])
            values.append('%s' % o['LowerWarningRXPower'])
            values.append('%s' % o['LowerWarningTXPower'])
            values.append('%s' % o['LowerWarningTXBias'])
            values.append('%s' % o['PMClassBAdminState'])
            values.append('%s' % o['PMClassCAdminState'])
            values.append('%s' % o['PMClassAAdminState'])
            values.append('%s' % o['AdminState'])
            rows.append(values)
        self.tblPrintObject('QsfpChannel', header, rows)


    def printPowerConverterSensors(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('HigherAlarmThreshold')
            header.append('HigherWarningThreshold')
            header.append('LowerWarningThreshold')
            header.append('LowerAlarmThreshold')
            header.append('PMClassCAdminState')
            header.append('PMClassAAdminState')
            header.append('AdminState')
            header.append('PMClassBAdminState')

        objs = self.swtch.getAllPowerConverterSensors()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['HigherAlarmThreshold'])
            values.append('%s' % o['HigherWarningThreshold'])
            values.append('%s' % o['LowerWarningThreshold'])
            values.append('%s' % o['LowerAlarmThreshold'])
            values.append('%s' % o['PMClassCAdminState'])
            values.append('%s' % o['PMClassAAdminState'])
            values.append('%s' % o['AdminState'])
            values.append('%s' % o['PMClassBAdminState'])
            rows.append(values)
        self.tblPrintObject('PowerConverterSensor', header, rows)


    def printVlans(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('VlanId')
            header.append('IntfList')
            header.append('UntagIntfList')
            header.append('AdminState')

        objs = self.swtch.getAllVlans()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['VlanId'])
            values.append('%s' % o['IntfList'])
            values.append('%s' % o['UntagIntfList'])
            values.append('%s' % o['AdminState'])
            rows.append(values)
        self.tblPrintObject('Vlan', header, rows)


    def printDWDMModuleNwIntfs(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('NwIntfId')
            header.append('ModuleId')
            header.append('ClntIntfIdToTributary0Map')
            header.append('ClntIntfIdToTributary1Map')
            header.append('EnableRxPRBSChecker')
            header.append('TxPulseShapeFltrRollOff')
            header.append('TxPower')
            header.append('RxPRBSInvertPattern')
            header.append('TxPowerRampdBmPerSec')
            header.append('EnableTxPRBS')
            header.append('TxPRBSInvertPattern')
            header.append('AdminState')
            header.append('ChannelNumber')
            header.append('FECMode')
            header.append('ModulationFmt')
            header.append('TxPulseShapeFltrType')
            header.append('RxPRBSPattern')
            header.append('TxPRBSPattern')
            header.append('DiffEncoding')

        objs = self.swtch.getAllDWDMModuleNwIntfs()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['NwIntfId'])
            values.append('%s' % o['ModuleId'])
            values.append('%s' % o['ClntIntfIdToTributary0Map'])
            values.append('%s' % o['ClntIntfIdToTributary1Map'])
            values.append('%s' % o['EnableRxPRBSChecker'])
            values.append('%s' % o['TxPulseShapeFltrRollOff'])
            values.append('%s' % o['TxPower'])
            values.append('%s' % o['RxPRBSInvertPattern'])
            values.append('%s' % o['TxPowerRampdBmPerSec'])
            values.append('%s' % o['EnableTxPRBS'])
            values.append('%s' % o['TxPRBSInvertPattern'])
            values.append('%s' % o['AdminState'])
            values.append('%s' % o['ChannelNumber'])
            values.append('%s' % o['FECMode'])
            values.append('%s' % o['ModulationFmt'])
            values.append('%s' % o['TxPulseShapeFltrType'])
            values.append('%s' % o['RxPRBSPattern'])
            values.append('%s' % o['TxPRBSPattern'])
            values.append('%s' % o['DiffEncoding'])
            rows.append(values)
        self.tblPrintObject('DWDMModuleNwIntf', header, rows)


    def printComponentLoggings(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Module')
            header.append('Level')

        objs = self.swtch.getAllComponentLoggings()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Module'])
            values.append('%s' % o['Level'])
            rows.append(values)
        self.tblPrintObject('ComponentLogging', header, rows)


    def printFans(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('FanId')
            header.append('AdminState')
            header.append('AdminSpeed')

        objs = self.swtch.getAllFans()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['FanId'])
            values.append('%s' % o['AdminState'])
            values.append('%s' % o['AdminSpeed'])
            rows.append(values)
        self.tblPrintObject('Fan', header, rows)


    def printSubIPv6Intfs(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('IpAddr')
            header.append('Type')
            header.append('MacAddr')
            header.append('Enable')

        objs = self.swtch.getAllSubIPv6Intfs()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['IpAddr'])
            values.append('%s' % o['Type'])
            values.append('%s' % o['MacAddr'])
            values.append('%s' % o['Enable'])
            rows.append(values)
        self.tblPrintObject('SubIPv6Intf', header, rows)


    def printIPv6RouteStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('DestinationNw')
            header.append('Protocol')
            header.append('IsNetworkReachable')
            header.append('RouteCreatedTime')
            header.append('RouteUpdatedTime')
            header.append('NextHopList')
            header.append('PolicyList')
            header.append('NextBestRoute')

        objs = self.swtch.getAllIPv6RouteStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['DestinationNw'])
            values.append('%s' % o['Protocol'])
            values.append('%s' % o['IsNetworkReachable'])
            values.append('%s' % o['RouteCreatedTime'])
            values.append('%s' % o['RouteUpdatedTime'])
            values.append('%s' % o['NextHopList'])
            values.append('%s' % o['PolicyList'])
            values.append('%s' % o['NextBestRoute'])
            rows.append(values)
        self.tblPrintObject('IPv6RouteState', header, rows)


    def printIPv6RouteState(self, DestinationNw, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('DestinationNw')
            header.append('Protocol')
            header.append('IsNetworkReachable')
            header.append('RouteCreatedTime')
            header.append('RouteUpdatedTime')
            header.append('NextHopList')
            header.append('PolicyList')
            header.append('NextBestRoute')

        rawobj = self.swtch.getIPv6RouteState(
                                              DestinationNw)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['DestinationNw'])
            values.append('%s' % o['Protocol'])
            values.append('%s' % o['IsNetworkReachable'])
            values.append('%s' % o['RouteCreatedTime'])
            values.append('%s' % o['RouteUpdatedTime'])
            values.append('%s' % o['NextHopList'])
            values.append('%s' % o['PolicyList'])
            values.append('%s' % o['NextBestRoute'])
            rows.append(values)
            self.tblPrintObject('IPv6RouteState', header, rows)

        else:
            print rawobj.content

    def printCombinedIPv6RouteStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('DestinationNw')
            header.append('Protocol')
            header.append('IsNetworkReachable')
            header.append('RouteCreatedTime')
            header.append('RouteUpdatedTime')
            header.append('NextHopList')
            header.append('PolicyList')
            header.append('NextBestRoute')
            header.append('NetworkMask')
            header.append('NextHop')
            header.append('NullRoute')
            header.append('Cost')

        objs = self.swtch.getAllIPv6RouteStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['DestinationNw'])
            values.append('%s' % o['Protocol'])
            values.append('%s' % o['IsNetworkReachable'])
            values.append('%s' % o['RouteCreatedTime'])
            values.append('%s' % o['RouteUpdatedTime'])
            values.append('%s' % o['NextHopList'])
            values.append('%s' % o['PolicyList'])
            values.append('%s' % o['NextBestRoute'])
            r = self.swtch.getIPv6Route(o['DestinationNw'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
                values.append('%s' % o['NetworkMask'])
                values.append('%s' % o['NextHop'])
                values.append('%s' % o['NullRoute'])
                values.append('%s' % o['Cost'])
            rows.append(values)
        self.tblPrintObject('IPv6RouteState', header, rows)


    def printPolicyPrefixSetStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('PrefixList')
            header.append('PolicyConditionList')

        objs = self.swtch.getAllPolicyPrefixSetStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['PrefixList'])
            values.append('%s' % o['PolicyConditionList'])
            rows.append(values)
        self.tblPrintObject('PolicyPrefixSetState', header, rows)


    def printPolicyPrefixSetState(self, Name, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('PrefixList')
            header.append('PolicyConditionList')

        rawobj = self.swtch.getPolicyPrefixSetState(
                                                    Name)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['PrefixList'])
            values.append('%s' % o['PolicyConditionList'])
            rows.append(values)
            self.tblPrintObject('PolicyPrefixSetState', header, rows)

        else:
            print rawobj.content

    def printCombinedPolicyPrefixSetStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('PrefixList')
            header.append('PolicyConditionList')

        objs = self.swtch.getAllPolicyPrefixSetStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['PrefixList'])
            values.append('%s' % o['PolicyConditionList'])
            r = self.swtch.getPolicyPrefixSet(o['Name'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
            rows.append(values)
        self.tblPrintObject('PolicyPrefixSetState', header, rows)


    def printPsus(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('PsuId')
            header.append('AdminState')

        objs = self.swtch.getAllPsus()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['PsuId'])
            values.append('%s' % o['AdminState'])
            rows.append(values)
        self.tblPrintObject('Psu', header, rows)


    def printBGPv4NeighborStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('NeighborAddress')
            header.append('Description')
            header.append('Disabled')
            header.append('PeerGroup')
            header.append('PeerType')
            header.append('SessionState')
            header.append('PeerAS')
            header.append('LocalAS')
            header.append('UpdateSource')
            header.append('AuthPassword')
            header.append('RouteReflectorClusterId')
            header.append('RouteReflectorClient')
            header.append('MultiHopEnable')
            header.append('MultiHopTTL')
            header.append('ConnectRetryTime')
            header.append('HoldTime')
            header.append('KeepaliveTime')
            header.append('AddPathsRx')
            header.append('AddPathsMaxTx')
            header.append('BfdNeighborState')
            header.append('MaxPrefixes')
            header.append('MaxPrefixesThresholdPct')
            header.append('MaxPrefixesDisconnect')
            header.append('MaxPrefixesRestartTimer')
            header.append('TotalPrefixes')
            header.append('AdjRIBInFilter')
            header.append('AdjRIBOutFilter')
            header.append('Messages')
            header.append('Queues')
            header.append('SessionStateDuration')

        objs = self.swtch.getAllBGPv4NeighborStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['NeighborAddress'])
            values.append('%s' % o['Description'])
            values.append('%s' % o['Disabled'])
            values.append('%s' % o['PeerGroup'])
            values.append('%s' % o['PeerType'])
            values.append('%s' % o['SessionState'])
            values.append('%s' % o['PeerAS'])
            values.append('%s' % o['LocalAS'])
            values.append('%s' % o['UpdateSource'])
            values.append('%s' % o['AuthPassword'])
            values.append('%s' % o['RouteReflectorClusterId'])
            values.append('%s' % o['RouteReflectorClient'])
            values.append('%s' % o['MultiHopEnable'])
            values.append('%s' % o['MultiHopTTL'])
            values.append('%s' % o['ConnectRetryTime'])
            values.append('%s' % o['HoldTime'])
            values.append('%s' % o['KeepaliveTime'])
            values.append('%s' % o['AddPathsRx'])
            values.append('%s' % o['AddPathsMaxTx'])
            values.append('%s' % o['BfdNeighborState'])
            values.append('%s' % o['MaxPrefixes'])
            values.append('%s' % o['MaxPrefixesThresholdPct'])
            values.append('%s' % o['MaxPrefixesDisconnect'])
            values.append('%s' % o['MaxPrefixesRestartTimer'])
            values.append('%s' % o['TotalPrefixes'])
            values.append('%s' % o['AdjRIBInFilter'])
            values.append('%s' % o['AdjRIBOutFilter'])
            values.append('%s' % o['Messages'])
            values.append('%s' % o['Queues'])
            values.append('%s' % o['SessionStateDuration'])
            rows.append(values)
        self.tblPrintObject('BGPv4NeighborState', header, rows)


    def printBGPv4NeighborState(self, IntfRef,NeighborAddress, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('NeighborAddress')
            header.append('Description')
            header.append('Disabled')
            header.append('PeerGroup')
            header.append('PeerType')
            header.append('SessionState')
            header.append('PeerAS')
            header.append('LocalAS')
            header.append('UpdateSource')
            header.append('AuthPassword')
            header.append('RouteReflectorClusterId')
            header.append('RouteReflectorClient')
            header.append('MultiHopEnable')
            header.append('MultiHopTTL')
            header.append('ConnectRetryTime')
            header.append('HoldTime')
            header.append('KeepaliveTime')
            header.append('AddPathsRx')
            header.append('AddPathsMaxTx')
            header.append('BfdNeighborState')
            header.append('MaxPrefixes')
            header.append('MaxPrefixesThresholdPct')
            header.append('MaxPrefixesDisconnect')
            header.append('MaxPrefixesRestartTimer')
            header.append('TotalPrefixes')
            header.append('AdjRIBInFilter')
            header.append('AdjRIBOutFilter')
            header.append('Messages')
            header.append('Queues')
            header.append('SessionStateDuration')

        rawobj = self.swtch.getBGPv4NeighborState(
                                                  IntfRef,
                                                  NeighborAddress)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['NeighborAddress'])
            values.append('%s' % o['Description'])
            values.append('%s' % o['Disabled'])
            values.append('%s' % o['PeerGroup'])
            values.append('%s' % o['PeerType'])
            values.append('%s' % o['SessionState'])
            values.append('%s' % o['PeerAS'])
            values.append('%s' % o['LocalAS'])
            values.append('%s' % o['UpdateSource'])
            values.append('%s' % o['AuthPassword'])
            values.append('%s' % o['RouteReflectorClusterId'])
            values.append('%s' % o['RouteReflectorClient'])
            values.append('%s' % o['MultiHopEnable'])
            values.append('%s' % o['MultiHopTTL'])
            values.append('%s' % o['ConnectRetryTime'])
            values.append('%s' % o['HoldTime'])
            values.append('%s' % o['KeepaliveTime'])
            values.append('%s' % o['AddPathsRx'])
            values.append('%s' % o['AddPathsMaxTx'])
            values.append('%s' % o['BfdNeighborState'])
            values.append('%s' % o['MaxPrefixes'])
            values.append('%s' % o['MaxPrefixesThresholdPct'])
            values.append('%s' % o['MaxPrefixesDisconnect'])
            values.append('%s' % o['MaxPrefixesRestartTimer'])
            values.append('%s' % o['TotalPrefixes'])
            values.append('%s' % o['AdjRIBInFilter'])
            values.append('%s' % o['AdjRIBOutFilter'])
            values.append('%s' % o['Messages'])
            values.append('%s' % o['Queues'])
            values.append('%s' % o['SessionStateDuration'])
            rows.append(values)
            self.tblPrintObject('BGPv4NeighborState', header, rows)

        else:
            print rawobj.content

    def printCombinedBGPv4NeighborStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('NeighborAddress')
            header.append('Description')
            header.append('Disabled')
            header.append('PeerGroup')
            header.append('PeerType')
            header.append('SessionState')
            header.append('PeerAS')
            header.append('LocalAS')
            header.append('UpdateSource')
            header.append('AuthPassword')
            header.append('RouteReflectorClusterId')
            header.append('RouteReflectorClient')
            header.append('MultiHopEnable')
            header.append('MultiHopTTL')
            header.append('ConnectRetryTime')
            header.append('HoldTime')
            header.append('KeepaliveTime')
            header.append('AddPathsRx')
            header.append('AddPathsMaxTx')
            header.append('BfdNeighborState')
            header.append('MaxPrefixes')
            header.append('MaxPrefixesThresholdPct')
            header.append('MaxPrefixesDisconnect')
            header.append('MaxPrefixesRestartTimer')
            header.append('TotalPrefixes')
            header.append('AdjRIBInFilter')
            header.append('AdjRIBOutFilter')
            header.append('Messages')
            header.append('Queues')
            header.append('SessionStateDuration')
            header.append('BfdEnable')
            header.append('BfdSessionParam')

        objs = self.swtch.getAllBGPv4NeighborStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['NeighborAddress'])
            values.append('%s' % o['Description'])
            values.append('%s' % o['Disabled'])
            values.append('%s' % o['PeerGroup'])
            values.append('%s' % o['PeerType'])
            values.append('%s' % o['SessionState'])
            values.append('%s' % o['PeerAS'])
            values.append('%s' % o['LocalAS'])
            values.append('%s' % o['UpdateSource'])
            values.append('%s' % o['AuthPassword'])
            values.append('%s' % o['RouteReflectorClusterId'])
            values.append('%s' % o['RouteReflectorClient'])
            values.append('%s' % o['MultiHopEnable'])
            values.append('%s' % o['MultiHopTTL'])
            values.append('%s' % o['ConnectRetryTime'])
            values.append('%s' % o['HoldTime'])
            values.append('%s' % o['KeepaliveTime'])
            values.append('%s' % o['AddPathsRx'])
            values.append('%s' % o['AddPathsMaxTx'])
            values.append('%s' % o['BfdNeighborState'])
            values.append('%s' % o['MaxPrefixes'])
            values.append('%s' % o['MaxPrefixesThresholdPct'])
            values.append('%s' % o['MaxPrefixesDisconnect'])
            values.append('%s' % o['MaxPrefixesRestartTimer'])
            values.append('%s' % o['TotalPrefixes'])
            values.append('%s' % o['AdjRIBInFilter'])
            values.append('%s' % o['AdjRIBOutFilter'])
            values.append('%s' % o['Messages'])
            values.append('%s' % o['Queues'])
            values.append('%s' % o['SessionStateDuration'])
            r = self.swtch.getBGPv4Neighbor(o['IntfRef'], o['NeighborAddress'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
                values.append('%s' % o['BfdEnable'])
                values.append('%s' % o['BfdSessionParam'])
            rows.append(values)
        self.tblPrintObject('BGPv4NeighborState', header, rows)


    def printXponderGlobals(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('XponderId')
            header.append('XponderDescription')
            header.append('XponderMode')

        objs = self.swtch.getAllXponderGlobals()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['XponderId'])
            values.append('%s' % o['XponderDescription'])
            values.append('%s' % o['XponderMode'])
            rows.append(values)
        self.tblPrintObject('XponderGlobal', header, rows)


    def printOspfAreaEntrys(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('AreaId')
            header.append('AuthType')
            header.append('ImportAsExtern')
            header.append('AreaSummary')
            header.append('AreaNssaTranslatorRole')
            header.append('StubDefaultCost')

        objs = self.swtch.getAllOspfAreaEntrys()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['AreaId'])
            values.append('%s' % o['AuthType'])
            values.append('%s' % o['ImportAsExtern'])
            values.append('%s' % o['AreaSummary'])
            values.append('%s' % o['AreaNssaTranslatorRole'])
            values.append('%s' % o['StubDefaultCost'])
            rows.append(values)
        self.tblPrintObject('OspfAreaEntry', header, rows)


    def printVxlanVtepInstances(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Intf')
            header.append('IntfRef')
            header.append('Vni')
            header.append('DstIp')
            header.append('VlanId')
            header.append('TOS')
            header.append('Mtu')
            header.append('InnerVlanHandlingMode')
            header.append('TTL')
            header.append('SrcIp')
            header.append('DstUDP')

        objs = self.swtch.getAllVxlanVtepInstances()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Intf'])
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['Vni'])
            values.append('%s' % o['DstIp'])
            values.append('%s' % o['VlanId'])
            values.append('%s' % o['TOS'])
            values.append('%s' % o['Mtu'])
            values.append('%s' % o['InnerVlanHandlingMode'])
            values.append('%s' % o['TTL'])
            values.append('%s' % o['SrcIp'])
            values.append('%s' % o['DstUDP'])
            rows.append(values)
        self.tblPrintObject('VxlanVtepInstance', header, rows)


    def printLaPortChannelStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('IfIndex')
            header.append('LagType')
            header.append('MinLinks')
            header.append('SystemIdMac')
            header.append('SystemPriority')
            header.append('AdminState')
            header.append('OperState')
            header.append('IntfRefList')
            header.append('IntfRefListUpInBundle')
            header.append('Interval')
            header.append('LagHash')
            header.append('LacpMode')

        objs = self.swtch.getAllLaPortChannelStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['LagType'])
            values.append('%s' % o['MinLinks'])
            values.append('%s' % o['SystemIdMac'])
            values.append('%s' % o['SystemPriority'])
            values.append('%s' % o['AdminState'])
            values.append('%s' % o['OperState'])
            values.append('%s' % o['IntfRefList'])
            values.append('%s' % o['IntfRefListUpInBundle'])
            values.append('%s' % o['Interval'])
            values.append('%s' % o['LagHash'])
            values.append('%s' % o['LacpMode'])
            rows.append(values)
        self.tblPrintObject('LaPortChannelState', header, rows)


    def printLaPortChannelState(self, IntfRef, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('IfIndex')
            header.append('LagType')
            header.append('MinLinks')
            header.append('SystemIdMac')
            header.append('SystemPriority')
            header.append('AdminState')
            header.append('OperState')
            header.append('IntfRefList')
            header.append('IntfRefListUpInBundle')
            header.append('Interval')
            header.append('LagHash')
            header.append('LacpMode')

        rawobj = self.swtch.getLaPortChannelState(
                                                  IntfRef)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['LagType'])
            values.append('%s' % o['MinLinks'])
            values.append('%s' % o['SystemIdMac'])
            values.append('%s' % o['SystemPriority'])
            values.append('%s' % o['AdminState'])
            values.append('%s' % o['OperState'])
            values.append('%s' % o['IntfRefList'])
            values.append('%s' % o['IntfRefListUpInBundle'])
            values.append('%s' % o['Interval'])
            values.append('%s' % o['LagHash'])
            values.append('%s' % o['LacpMode'])
            rows.append(values)
            self.tblPrintObject('LaPortChannelState', header, rows)

        else:
            print rawobj.content

    def printCombinedLaPortChannelStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('IfIndex')
            header.append('LagType')
            header.append('MinLinks')
            header.append('SystemIdMac')
            header.append('SystemPriority')
            header.append('AdminState')
            header.append('OperState')
            header.append('IntfRefList')
            header.append('IntfRefListUpInBundle')
            header.append('Interval')
            header.append('LagHash')
            header.append('LacpMode')

        objs = self.swtch.getAllLaPortChannelStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['LagType'])
            values.append('%s' % o['MinLinks'])
            values.append('%s' % o['SystemIdMac'])
            values.append('%s' % o['SystemPriority'])
            values.append('%s' % o['AdminState'])
            values.append('%s' % o['OperState'])
            values.append('%s' % o['IntfRefList'])
            values.append('%s' % o['IntfRefListUpInBundle'])
            values.append('%s' % o['Interval'])
            values.append('%s' % o['LagHash'])
            values.append('%s' % o['LacpMode'])
            r = self.swtch.getLaPortChannel(o['IntfRef'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
            rows.append(values)
        self.tblPrintObject('LaPortChannelState', header, rows)


    def printDhcpGlobalConfigs(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('DhcpConfigKey')
            header.append('Enable')
            header.append('DefaultLeaseTime')
            header.append('MaxLeaseTime')

        objs = self.swtch.getAllDhcpGlobalConfigs()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['DhcpConfigKey'])
            values.append('%s' % o['Enable'])
            values.append('%s' % o['DefaultLeaseTime'])
            values.append('%s' % o['MaxLeaseTime'])
            rows.append(values)
        self.tblPrintObject('DhcpGlobalConfig', header, rows)


    def printDhcpRelayIntfs(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IfIndex')
            header.append('Enable')
            header.append('ServerIp')

        objs = self.swtch.getAllDhcpRelayIntfs()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['Enable'])
            values.append('%s' % o['ServerIp'])
            rows.append(values)
        self.tblPrintObject('DhcpRelayIntf', header, rows)


    def printDistributedRelayStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('DrniName')
            header.append('Description')
            header.append('PortalAddress')
            header.append('PortalPriority')
            header.append('ThreePortalSystem')
            header.append('PortalSystemNumber')
            header.append('IntfRefList')
            header.append('IntfRef')
            header.append('ConvAdminGateway')
            header.append('NeighborAdminConvGatewayListDigest')
            header.append('NeighborAdminConvPortListDigest')
            header.append('GatewayAlgorithm')
            header.append('NeighborGatewayAlgorithm')
            header.append('NeighborPortAlgorithm')
            header.append('NeighborAdminDRCPState')
            header.append('EncapMethod')
            header.append('IPLEncapMap')
            header.append('NetEncapMap')
            header.append('DRGatewayConversationPasses')
            header.append('PSI')
            header.append('PortConversationControl')
            header.append('IntraPortalPortProtocolDA')

        objs = self.swtch.getAllDistributedRelayStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['DrniName'])
            values.append('%s' % o['Description'])
            values.append('%s' % o['PortalAddress'])
            values.append('%s' % o['PortalPriority'])
            values.append('%s' % o['ThreePortalSystem'])
            values.append('%s' % o['PortalSystemNumber'])
            values.append('%s' % o['IntfRefList'])
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['ConvAdminGateway'])
            values.append('%s' % o['NeighborAdminConvGatewayListDigest'])
            values.append('%s' % o['NeighborAdminConvPortListDigest'])
            values.append('%s' % o['GatewayAlgorithm'])
            values.append('%s' % o['NeighborGatewayAlgorithm'])
            values.append('%s' % o['NeighborPortAlgorithm'])
            values.append('%s' % o['NeighborAdminDRCPState'])
            values.append('%s' % o['EncapMethod'])
            values.append('%s' % o['IPLEncapMap'])
            values.append('%s' % o['NetEncapMap'])
            values.append('%s' % o['DRGatewayConversationPasses'])
            values.append('%s' % o['PSI'])
            values.append('%s' % o['PortConversationControl'])
            values.append('%s' % o['IntraPortalPortProtocolDA'])
            rows.append(values)
        self.tblPrintObject('DistributedRelayState', header, rows)


    def printDistributedRelayState(self, DrniName, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('DrniName')
            header.append('Description')
            header.append('PortalAddress')
            header.append('PortalPriority')
            header.append('ThreePortalSystem')
            header.append('PortalSystemNumber')
            header.append('IntfRefList')
            header.append('IntfRef')
            header.append('ConvAdminGateway')
            header.append('NeighborAdminConvGatewayListDigest')
            header.append('NeighborAdminConvPortListDigest')
            header.append('GatewayAlgorithm')
            header.append('NeighborGatewayAlgorithm')
            header.append('NeighborPortAlgorithm')
            header.append('NeighborAdminDRCPState')
            header.append('EncapMethod')
            header.append('IPLEncapMap')
            header.append('NetEncapMap')
            header.append('DRGatewayConversationPasses')
            header.append('PSI')
            header.append('PortConversationControl')
            header.append('IntraPortalPortProtocolDA')

        rawobj = self.swtch.getDistributedRelayState(
                                                     DrniName)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['DrniName'])
            values.append('%s' % o['Description'])
            values.append('%s' % o['PortalAddress'])
            values.append('%s' % o['PortalPriority'])
            values.append('%s' % o['ThreePortalSystem'])
            values.append('%s' % o['PortalSystemNumber'])
            values.append('%s' % o['IntfRefList'])
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['ConvAdminGateway'])
            values.append('%s' % o['NeighborAdminConvGatewayListDigest'])
            values.append('%s' % o['NeighborAdminConvPortListDigest'])
            values.append('%s' % o['GatewayAlgorithm'])
            values.append('%s' % o['NeighborGatewayAlgorithm'])
            values.append('%s' % o['NeighborPortAlgorithm'])
            values.append('%s' % o['NeighborAdminDRCPState'])
            values.append('%s' % o['EncapMethod'])
            values.append('%s' % o['IPLEncapMap'])
            values.append('%s' % o['NetEncapMap'])
            values.append('%s' % o['DRGatewayConversationPasses'])
            values.append('%s' % o['PSI'])
            values.append('%s' % o['PortConversationControl'])
            values.append('%s' % o['IntraPortalPortProtocolDA'])
            rows.append(values)
            self.tblPrintObject('DistributedRelayState', header, rows)

        else:
            print rawobj.content

    def printCombinedDistributedRelayStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('DrniName')
            header.append('Description')
            header.append('PortalAddress')
            header.append('PortalPriority')
            header.append('ThreePortalSystem')
            header.append('PortalSystemNumber')
            header.append('IntfRefList')
            header.append('IntfRef')
            header.append('ConvAdminGateway')
            header.append('NeighborAdminConvGatewayListDigest')
            header.append('NeighborAdminConvPortListDigest')
            header.append('GatewayAlgorithm')
            header.append('NeighborGatewayAlgorithm')
            header.append('NeighborPortAlgorithm')
            header.append('NeighborAdminDRCPState')
            header.append('EncapMethod')
            header.append('IPLEncapMap')
            header.append('NetEncapMap')
            header.append('DRGatewayConversationPasses')
            header.append('PSI')
            header.append('PortConversationControl')
            header.append('IntraPortalPortProtocolDA')
            header.append('IntfReflist')

        objs = self.swtch.getAllDistributedRelayStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['DrniName'])
            values.append('%s' % o['Description'])
            values.append('%s' % o['PortalAddress'])
            values.append('%s' % o['PortalPriority'])
            values.append('%s' % o['ThreePortalSystem'])
            values.append('%s' % o['PortalSystemNumber'])
            values.append('%s' % o['IntfRefList'])
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['ConvAdminGateway'])
            values.append('%s' % o['NeighborAdminConvGatewayListDigest'])
            values.append('%s' % o['NeighborAdminConvPortListDigest'])
            values.append('%s' % o['GatewayAlgorithm'])
            values.append('%s' % o['NeighborGatewayAlgorithm'])
            values.append('%s' % o['NeighborPortAlgorithm'])
            values.append('%s' % o['NeighborAdminDRCPState'])
            values.append('%s' % o['EncapMethod'])
            values.append('%s' % o['IPLEncapMap'])
            values.append('%s' % o['NetEncapMap'])
            values.append('%s' % o['DRGatewayConversationPasses'])
            values.append('%s' % o['PSI'])
            values.append('%s' % o['PortConversationControl'])
            values.append('%s' % o['IntraPortalPortProtocolDA'])
            r = self.swtch.getDistributedRelay(o['DrniName'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
                values.append('%s' % o['IntfReflist'])
            rows.append(values)
        self.tblPrintObject('DistributedRelayState', header, rows)


    def printAclRules(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('RuleName')
            header.append('SourceMac')
            header.append('DestMac')
            header.append('SourceIp')
            header.append('DestIp')
            header.append('SourceMask')
            header.append('DestMask')
            header.append('Proto')
            header.append('SrcPort')
            header.append('L4DstPort')
            header.append('L4MinPort')
            header.append('L4SrcPort')
            header.append('Action')
            header.append('L4MaxPort')
            header.append('DstPort')
            header.append('L4PortMatch')

        objs = self.swtch.getAllAclRules()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['RuleName'])
            values.append('%s' % o['SourceMac'])
            values.append('%s' % o['DestMac'])
            values.append('%s' % o['SourceIp'])
            values.append('%s' % o['DestIp'])
            values.append('%s' % o['SourceMask'])
            values.append('%s' % o['DestMask'])
            values.append('%s' % o['Proto'])
            values.append('%s' % o['SrcPort'])
            values.append('%s' % o['L4DstPort'])
            values.append('%s' % o['L4MinPort'])
            values.append('%s' % o['L4SrcPort'])
            values.append('%s' % o['Action'])
            values.append('%s' % o['L4MaxPort'])
            values.append('%s' % o['DstPort'])
            values.append('%s' % o['L4PortMatch'])
            rows.append(values)
        self.tblPrintObject('AclRule', header, rows)


    def printBGPv4Neighbors(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('NeighborAddress')
            header.append('Description')
            header.append('PeerGroup')
            header.append('PeerAS')
            header.append('LocalAS')
            header.append('UpdateSource')
            header.append('AuthPassword')
            header.append('AdjRIBInFilter')
            header.append('AdjRIBOutFilter')
            header.append('BfdEnable')
            header.append('MultiHopTTL')
            header.append('KeepaliveTime')
            header.append('AddPathsRx')
            header.append('RouteReflectorClient')
            header.append('MaxPrefixesRestartTimer')
            header.append('MultiHopEnable')
            header.append('RouteReflectorClusterId')
            header.append('MaxPrefixesDisconnect')
            header.append('AddPathsMaxTx')
            header.append('MaxPrefixes')
            header.append('MaxPrefixesThresholdPct')
            header.append('BfdSessionParam')
            header.append('Disabled')
            header.append('HoldTime')
            header.append('ConnectRetryTime')

        objs = self.swtch.getAllBGPv4Neighbors()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['NeighborAddress'])
            values.append('%s' % o['Description'])
            values.append('%s' % o['PeerGroup'])
            values.append('%s' % o['PeerAS'])
            values.append('%s' % o['LocalAS'])
            values.append('%s' % o['UpdateSource'])
            values.append('%s' % o['AuthPassword'])
            values.append('%s' % o['AdjRIBInFilter'])
            values.append('%s' % o['AdjRIBOutFilter'])
            values.append('%s' % o['BfdEnable'])
            values.append('%s' % o['MultiHopTTL'])
            values.append('%s' % o['KeepaliveTime'])
            values.append('%s' % o['AddPathsRx'])
            values.append('%s' % o['RouteReflectorClient'])
            values.append('%s' % o['MaxPrefixesRestartTimer'])
            values.append('%s' % o['MultiHopEnable'])
            values.append('%s' % o['RouteReflectorClusterId'])
            values.append('%s' % o['MaxPrefixesDisconnect'])
            values.append('%s' % o['AddPathsMaxTx'])
            values.append('%s' % o['MaxPrefixes'])
            values.append('%s' % o['MaxPrefixesThresholdPct'])
            values.append('%s' % o['BfdSessionParam'])
            values.append('%s' % o['Disabled'])
            values.append('%s' % o['HoldTime'])
            values.append('%s' % o['ConnectRetryTime'])
            rows.append(values)
        self.tblPrintObject('BGPv4Neighbor', header, rows)


    def printOspfIfMetricEntrys(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IfMetricAddressLessIf')
            header.append('IfMetricTOS')
            header.append('IfMetricIpAddress')
            header.append('IfMetricValue')

        objs = self.swtch.getAllOspfIfMetricEntrys()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IfMetricAddressLessIf'])
            values.append('%s' % o['IfMetricTOS'])
            values.append('%s' % o['IfMetricIpAddress'])
            values.append('%s' % o['IfMetricValue'])
            rows.append(values)
        self.tblPrintObject('OspfIfMetricEntry', header, rows)


    def printStpPortStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('Vlan')
            header.append('Priority')
            header.append('PathCost')
            header.append('PathCost32')
            header.append('State')
            header.append('DesignatedRoot')
            header.append('DesignatedCost')
            header.append('DesignatedBridge')
            header.append('DesignatedPort')
            header.append('ForwardTransitions')
            header.append('AdminEdgePort')
            header.append('AdminPathCost')
            header.append('OperEdgePort')
            header.append('OperPointToPoint')
            header.append('MaxAge')
            header.append('HelloTime')
            header.append('ForwardDelay')
            header.append('BridgeAssurance')
            header.append('BridgeAssuranceInconsistant')
            header.append('BpduGuard')
            header.append('BpduGuardDetected')
            header.append('StpInPkts')
            header.append('StpOutPkts')
            header.append('RstpInPkts')
            header.append('RstpOutPkts')
            header.append('TcInPkts')
            header.append('TcOutPkts')
            header.append('TcAckInPkts')
            header.append('TcAckOutPkts')
            header.append('PvstInPkts')
            header.append('PvstOutPkts')
            header.append('BpduInPkts')
            header.append('BpduOutPkts')
            header.append('PimPrevState')
            header.append('PimCurrState')
            header.append('PrtmPrevState')
            header.append('PrtmCurrState')
            header.append('PrxmPrevState')
            header.append('PrxmCurrState')
            header.append('PstmPrevState')
            header.append('PstmCurrState')
            header.append('TcmPrevState')
            header.append('TcmCurrState')
            header.append('PpmPrevState')
            header.append('PpmCurrState')
            header.append('PtxmPrevState')
            header.append('PtxmCurrState')
            header.append('PtimPrevState')
            header.append('PtimCurrState')
            header.append('BdmPrevState')
            header.append('BdmCurrState')
            header.append('EdgeDelayWhile')
            header.append('FdWhile')
            header.append('HelloWhen')
            header.append('MdelayWhile')
            header.append('RbWhile')
            header.append('RcvdInfoWhile')
            header.append('RrWhile')
            header.append('TcWhile')
            header.append('BaWhile')
            header.append('Enable')
            header.append('BpduGuardInterval')

        objs = self.swtch.getAllStpPortStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['Vlan'])
            values.append('%s' % o['Priority'])
            values.append('%s' % o['PathCost'])
            values.append('%s' % o['PathCost32'])
            values.append('%s' % o['State'])
            values.append('%s' % o['DesignatedRoot'])
            values.append('%s' % o['DesignatedCost'])
            values.append('%s' % o['DesignatedBridge'])
            values.append('%s' % o['DesignatedPort'])
            values.append('%s' % o['ForwardTransitions'])
            values.append('%s' % o['AdminEdgePort'])
            values.append('%s' % o['AdminPathCost'])
            values.append('%s' % o['OperEdgePort'])
            values.append('%s' % o['OperPointToPoint'])
            values.append('%s' % o['MaxAge'])
            values.append('%s' % o['HelloTime'])
            values.append('%s' % o['ForwardDelay'])
            values.append('%s' % o['BridgeAssurance'])
            values.append('%s' % o['BridgeAssuranceInconsistant'])
            values.append('%s' % o['BpduGuard'])
            values.append('%s' % o['BpduGuardDetected'])
            values.append('%s' % o['StpInPkts'])
            values.append('%s' % o['StpOutPkts'])
            values.append('%s' % o['RstpInPkts'])
            values.append('%s' % o['RstpOutPkts'])
            values.append('%s' % o['TcInPkts'])
            values.append('%s' % o['TcOutPkts'])
            values.append('%s' % o['TcAckInPkts'])
            values.append('%s' % o['TcAckOutPkts'])
            values.append('%s' % o['PvstInPkts'])
            values.append('%s' % o['PvstOutPkts'])
            values.append('%s' % o['BpduInPkts'])
            values.append('%s' % o['BpduOutPkts'])
            values.append('%s' % o['PimPrevState'])
            values.append('%s' % o['PimCurrState'])
            values.append('%s' % o['PrtmPrevState'])
            values.append('%s' % o['PrtmCurrState'])
            values.append('%s' % o['PrxmPrevState'])
            values.append('%s' % o['PrxmCurrState'])
            values.append('%s' % o['PstmPrevState'])
            values.append('%s' % o['PstmCurrState'])
            values.append('%s' % o['TcmPrevState'])
            values.append('%s' % o['TcmCurrState'])
            values.append('%s' % o['PpmPrevState'])
            values.append('%s' % o['PpmCurrState'])
            values.append('%s' % o['PtxmPrevState'])
            values.append('%s' % o['PtxmCurrState'])
            values.append('%s' % o['PtimPrevState'])
            values.append('%s' % o['PtimCurrState'])
            values.append('%s' % o['BdmPrevState'])
            values.append('%s' % o['BdmCurrState'])
            values.append('%s' % o['EdgeDelayWhile'])
            values.append('%s' % o['FdWhile'])
            values.append('%s' % o['HelloWhen'])
            values.append('%s' % o['MdelayWhile'])
            values.append('%s' % o['RbWhile'])
            values.append('%s' % o['RcvdInfoWhile'])
            values.append('%s' % o['RrWhile'])
            values.append('%s' % o['TcWhile'])
            values.append('%s' % o['BaWhile'])
            values.append('%s' % o['Enable'])
            values.append('%s' % o['BpduGuardInterval'])
            rows.append(values)
        self.tblPrintObject('StpPortState', header, rows)


    def printStpPortState(self, IntfRef,Vlan, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('Vlan')
            header.append('Priority')
            header.append('PathCost')
            header.append('PathCost32')
            header.append('State')
            header.append('DesignatedRoot')
            header.append('DesignatedCost')
            header.append('DesignatedBridge')
            header.append('DesignatedPort')
            header.append('ForwardTransitions')
            header.append('AdminEdgePort')
            header.append('AdminPathCost')
            header.append('OperEdgePort')
            header.append('OperPointToPoint')
            header.append('MaxAge')
            header.append('HelloTime')
            header.append('ForwardDelay')
            header.append('BridgeAssurance')
            header.append('BridgeAssuranceInconsistant')
            header.append('BpduGuard')
            header.append('BpduGuardDetected')
            header.append('StpInPkts')
            header.append('StpOutPkts')
            header.append('RstpInPkts')
            header.append('RstpOutPkts')
            header.append('TcInPkts')
            header.append('TcOutPkts')
            header.append('TcAckInPkts')
            header.append('TcAckOutPkts')
            header.append('PvstInPkts')
            header.append('PvstOutPkts')
            header.append('BpduInPkts')
            header.append('BpduOutPkts')
            header.append('PimPrevState')
            header.append('PimCurrState')
            header.append('PrtmPrevState')
            header.append('PrtmCurrState')
            header.append('PrxmPrevState')
            header.append('PrxmCurrState')
            header.append('PstmPrevState')
            header.append('PstmCurrState')
            header.append('TcmPrevState')
            header.append('TcmCurrState')
            header.append('PpmPrevState')
            header.append('PpmCurrState')
            header.append('PtxmPrevState')
            header.append('PtxmCurrState')
            header.append('PtimPrevState')
            header.append('PtimCurrState')
            header.append('BdmPrevState')
            header.append('BdmCurrState')
            header.append('EdgeDelayWhile')
            header.append('FdWhile')
            header.append('HelloWhen')
            header.append('MdelayWhile')
            header.append('RbWhile')
            header.append('RcvdInfoWhile')
            header.append('RrWhile')
            header.append('TcWhile')
            header.append('BaWhile')
            header.append('Enable')
            header.append('BpduGuardInterval')

        rawobj = self.swtch.getStpPortState(
                                            IntfRef,
                                            Vlan)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['Vlan'])
            values.append('%s' % o['Priority'])
            values.append('%s' % o['PathCost'])
            values.append('%s' % o['PathCost32'])
            values.append('%s' % o['State'])
            values.append('%s' % o['DesignatedRoot'])
            values.append('%s' % o['DesignatedCost'])
            values.append('%s' % o['DesignatedBridge'])
            values.append('%s' % o['DesignatedPort'])
            values.append('%s' % o['ForwardTransitions'])
            values.append('%s' % o['AdminEdgePort'])
            values.append('%s' % o['AdminPathCost'])
            values.append('%s' % o['OperEdgePort'])
            values.append('%s' % o['OperPointToPoint'])
            values.append('%s' % o['MaxAge'])
            values.append('%s' % o['HelloTime'])
            values.append('%s' % o['ForwardDelay'])
            values.append('%s' % o['BridgeAssurance'])
            values.append('%s' % o['BridgeAssuranceInconsistant'])
            values.append('%s' % o['BpduGuard'])
            values.append('%s' % o['BpduGuardDetected'])
            values.append('%s' % o['StpInPkts'])
            values.append('%s' % o['StpOutPkts'])
            values.append('%s' % o['RstpInPkts'])
            values.append('%s' % o['RstpOutPkts'])
            values.append('%s' % o['TcInPkts'])
            values.append('%s' % o['TcOutPkts'])
            values.append('%s' % o['TcAckInPkts'])
            values.append('%s' % o['TcAckOutPkts'])
            values.append('%s' % o['PvstInPkts'])
            values.append('%s' % o['PvstOutPkts'])
            values.append('%s' % o['BpduInPkts'])
            values.append('%s' % o['BpduOutPkts'])
            values.append('%s' % o['PimPrevState'])
            values.append('%s' % o['PimCurrState'])
            values.append('%s' % o['PrtmPrevState'])
            values.append('%s' % o['PrtmCurrState'])
            values.append('%s' % o['PrxmPrevState'])
            values.append('%s' % o['PrxmCurrState'])
            values.append('%s' % o['PstmPrevState'])
            values.append('%s' % o['PstmCurrState'])
            values.append('%s' % o['TcmPrevState'])
            values.append('%s' % o['TcmCurrState'])
            values.append('%s' % o['PpmPrevState'])
            values.append('%s' % o['PpmCurrState'])
            values.append('%s' % o['PtxmPrevState'])
            values.append('%s' % o['PtxmCurrState'])
            values.append('%s' % o['PtimPrevState'])
            values.append('%s' % o['PtimCurrState'])
            values.append('%s' % o['BdmPrevState'])
            values.append('%s' % o['BdmCurrState'])
            values.append('%s' % o['EdgeDelayWhile'])
            values.append('%s' % o['FdWhile'])
            values.append('%s' % o['HelloWhen'])
            values.append('%s' % o['MdelayWhile'])
            values.append('%s' % o['RbWhile'])
            values.append('%s' % o['RcvdInfoWhile'])
            values.append('%s' % o['RrWhile'])
            values.append('%s' % o['TcWhile'])
            values.append('%s' % o['BaWhile'])
            values.append('%s' % o['Enable'])
            values.append('%s' % o['BpduGuardInterval'])
            rows.append(values)
            self.tblPrintObject('StpPortState', header, rows)

        else:
            print rawobj.content

    def printCombinedStpPortStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('Vlan')
            header.append('Priority')
            header.append('PathCost')
            header.append('PathCost32')
            header.append('State')
            header.append('DesignatedRoot')
            header.append('DesignatedCost')
            header.append('DesignatedBridge')
            header.append('DesignatedPort')
            header.append('ForwardTransitions')
            header.append('AdminEdgePort')
            header.append('AdminPathCost')
            header.append('OperEdgePort')
            header.append('OperPointToPoint')
            header.append('MaxAge')
            header.append('HelloTime')
            header.append('ForwardDelay')
            header.append('BridgeAssurance')
            header.append('BridgeAssuranceInconsistant')
            header.append('BpduGuard')
            header.append('BpduGuardDetected')
            header.append('StpInPkts')
            header.append('StpOutPkts')
            header.append('RstpInPkts')
            header.append('RstpOutPkts')
            header.append('TcInPkts')
            header.append('TcOutPkts')
            header.append('TcAckInPkts')
            header.append('TcAckOutPkts')
            header.append('PvstInPkts')
            header.append('PvstOutPkts')
            header.append('BpduInPkts')
            header.append('BpduOutPkts')
            header.append('PimPrevState')
            header.append('PimCurrState')
            header.append('PrtmPrevState')
            header.append('PrtmCurrState')
            header.append('PrxmPrevState')
            header.append('PrxmCurrState')
            header.append('PstmPrevState')
            header.append('PstmCurrState')
            header.append('TcmPrevState')
            header.append('TcmCurrState')
            header.append('PpmPrevState')
            header.append('PpmCurrState')
            header.append('PtxmPrevState')
            header.append('PtxmCurrState')
            header.append('PtimPrevState')
            header.append('PtimCurrState')
            header.append('BdmPrevState')
            header.append('BdmCurrState')
            header.append('EdgeDelayWhile')
            header.append('FdWhile')
            header.append('HelloWhen')
            header.append('MdelayWhile')
            header.append('RbWhile')
            header.append('RcvdInfoWhile')
            header.append('RrWhile')
            header.append('TcWhile')
            header.append('BaWhile')
            header.append('Enable')
            header.append('BpduGuardInterval')
            header.append('ProtocolMigration')
            header.append('AdminState')
            header.append('AdminPointToPoint')

        objs = self.swtch.getAllStpPortStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['Vlan'])
            values.append('%s' % o['Priority'])
            values.append('%s' % o['PathCost'])
            values.append('%s' % o['PathCost32'])
            values.append('%s' % o['State'])
            values.append('%s' % o['DesignatedRoot'])
            values.append('%s' % o['DesignatedCost'])
            values.append('%s' % o['DesignatedBridge'])
            values.append('%s' % o['DesignatedPort'])
            values.append('%s' % o['ForwardTransitions'])
            values.append('%s' % o['AdminEdgePort'])
            values.append('%s' % o['AdminPathCost'])
            values.append('%s' % o['OperEdgePort'])
            values.append('%s' % o['OperPointToPoint'])
            values.append('%s' % o['MaxAge'])
            values.append('%s' % o['HelloTime'])
            values.append('%s' % o['ForwardDelay'])
            values.append('%s' % o['BridgeAssurance'])
            values.append('%s' % o['BridgeAssuranceInconsistant'])
            values.append('%s' % o['BpduGuard'])
            values.append('%s' % o['BpduGuardDetected'])
            values.append('%s' % o['StpInPkts'])
            values.append('%s' % o['StpOutPkts'])
            values.append('%s' % o['RstpInPkts'])
            values.append('%s' % o['RstpOutPkts'])
            values.append('%s' % o['TcInPkts'])
            values.append('%s' % o['TcOutPkts'])
            values.append('%s' % o['TcAckInPkts'])
            values.append('%s' % o['TcAckOutPkts'])
            values.append('%s' % o['PvstInPkts'])
            values.append('%s' % o['PvstOutPkts'])
            values.append('%s' % o['BpduInPkts'])
            values.append('%s' % o['BpduOutPkts'])
            values.append('%s' % o['PimPrevState'])
            values.append('%s' % o['PimCurrState'])
            values.append('%s' % o['PrtmPrevState'])
            values.append('%s' % o['PrtmCurrState'])
            values.append('%s' % o['PrxmPrevState'])
            values.append('%s' % o['PrxmCurrState'])
            values.append('%s' % o['PstmPrevState'])
            values.append('%s' % o['PstmCurrState'])
            values.append('%s' % o['TcmPrevState'])
            values.append('%s' % o['TcmCurrState'])
            values.append('%s' % o['PpmPrevState'])
            values.append('%s' % o['PpmCurrState'])
            values.append('%s' % o['PtxmPrevState'])
            values.append('%s' % o['PtxmCurrState'])
            values.append('%s' % o['PtimPrevState'])
            values.append('%s' % o['PtimCurrState'])
            values.append('%s' % o['BdmPrevState'])
            values.append('%s' % o['BdmCurrState'])
            values.append('%s' % o['EdgeDelayWhile'])
            values.append('%s' % o['FdWhile'])
            values.append('%s' % o['HelloWhen'])
            values.append('%s' % o['MdelayWhile'])
            values.append('%s' % o['RbWhile'])
            values.append('%s' % o['RcvdInfoWhile'])
            values.append('%s' % o['RrWhile'])
            values.append('%s' % o['TcWhile'])
            values.append('%s' % o['BaWhile'])
            values.append('%s' % o['Enable'])
            values.append('%s' % o['BpduGuardInterval'])
            r = self.swtch.getStpPort(o['IntfRef'], o['Vlan'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
                values.append('%s' % o['ProtocolMigration'])
                values.append('%s' % o['AdminState'])
                values.append('%s' % o['AdminPointToPoint'])
            rows.append(values)
        self.tblPrintObject('StpPortState', header, rows)


    def printCoppStatStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Protocol')
            header.append('PeakRate')
            header.append('BurstRate')
            header.append('GreenPackets')
            header.append('RedPackets')

        objs = self.swtch.getAllCoppStatStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Protocol'])
            values.append('%s' % o['PeakRate'])
            values.append('%s' % o['BurstRate'])
            values.append('%s' % o['GreenPackets'])
            values.append('%s' % o['RedPackets'])
            rows.append(values)
        self.tblPrintObject('CoppStatState', header, rows)


    def printCoppStatState(self, Protocol, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Protocol')
            header.append('PeakRate')
            header.append('BurstRate')
            header.append('GreenPackets')
            header.append('RedPackets')

        rawobj = self.swtch.getCoppStatState(
                                             Protocol)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['Protocol'])
            values.append('%s' % o['PeakRate'])
            values.append('%s' % o['BurstRate'])
            values.append('%s' % o['GreenPackets'])
            values.append('%s' % o['RedPackets'])
            rows.append(values)
            self.tblPrintObject('CoppStatState', header, rows)

        else:
            print rawobj.content

    def printFMgrGlobals(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Vrf')
            header.append('Enable')

        objs = self.swtch.getAllFMgrGlobals()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Vrf'])
            values.append('%s' % o['Enable'])
            rows.append(values)
        self.tblPrintObject('FMgrGlobal', header, rows)


    def printNotifierEnables(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Vrf')
            header.append('AlarmEnable')
            header.append('FaultEnable')
            header.append('EventEnable')

        objs = self.swtch.getAllNotifierEnables()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Vrf'])
            values.append('%s' % o['AlarmEnable'])
            values.append('%s' % o['FaultEnable'])
            values.append('%s' % o['EventEnable'])
            rows.append(values)
        self.tblPrintObject('NotifierEnable', header, rows)


    def printLaPortChannels(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('IntfRefList')
            header.append('MinLinks')
            header.append('SystemPriority')
            header.append('Interval')
            header.append('LagHash')
            header.append('AdminState')
            header.append('SystemIdMac')
            header.append('LagType')
            header.append('LacpMode')

        objs = self.swtch.getAllLaPortChannels()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['IntfRefList'])
            values.append('%s' % o['MinLinks'])
            values.append('%s' % o['SystemPriority'])
            values.append('%s' % o['Interval'])
            values.append('%s' % o['LagHash'])
            values.append('%s' % o['AdminState'])
            values.append('%s' % o['SystemIdMac'])
            values.append('%s' % o['LagType'])
            values.append('%s' % o['LacpMode'])
            rows.append(values)
        self.tblPrintObject('LaPortChannel', header, rows)


    def printBGPPolicyConditionStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('ConditionInfo')
            header.append('PolicyStmtList')

        objs = self.swtch.getAllBGPPolicyConditionStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['ConditionInfo'])
            values.append('%s' % o['PolicyStmtList'])
            rows.append(values)
        self.tblPrintObject('BGPPolicyConditionState', header, rows)


    def printBGPPolicyConditionState(self, Name, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('ConditionInfo')
            header.append('PolicyStmtList')

        rawobj = self.swtch.getBGPPolicyConditionState(
                                                       Name)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['ConditionInfo'])
            values.append('%s' % o['PolicyStmtList'])
            rows.append(values)
            self.tblPrintObject('BGPPolicyConditionState', header, rows)

        else:
            print rawobj.content

    def printCombinedBGPPolicyConditionStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('ConditionInfo')
            header.append('PolicyStmtList')
            header.append('ConditionType')
            header.append('IpPrefix')
            header.append('MaskLengthRange')

        objs = self.swtch.getAllBGPPolicyConditionStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['ConditionInfo'])
            values.append('%s' % o['PolicyStmtList'])
            r = self.swtch.getBGPPolicyCondition(o['Name'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
                values.append('%s' % o['ConditionType'])
                values.append('%s' % o['IpPrefix'])
                values.append('%s' % o['MaskLengthRange'])
            rows.append(values)
        self.tblPrintObject('BGPPolicyConditionState', header, rows)


    def printApiInfoStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Url')
            header.append('Info')

        objs = self.swtch.getAllApiInfoStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Url'])
            values.append('%s' % o['Info'])
            rows.append(values)
        self.tblPrintObject('ApiInfoState', header, rows)


    def printApiInfoState(self, Url, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Url')
            header.append('Info')

        rawobj = self.swtch.getApiInfoState(
                                            Url)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['Url'])
            values.append('%s' % o['Info'])
            rows.append(values)
            self.tblPrintObject('ApiInfoState', header, rows)

        else:
            print rawobj.content

    def printFanSensorStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('CurrentSpeed')

        objs = self.swtch.getAllFanSensorStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['CurrentSpeed'])
            rows.append(values)
        self.tblPrintObject('FanSensorState', header, rows)


    def printFanSensorState(self, Name, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('CurrentSpeed')

        rawobj = self.swtch.getFanSensorState(
                                              Name)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['CurrentSpeed'])
            rows.append(values)
            self.tblPrintObject('FanSensorState', header, rows)

        else:
            print rawobj.content

    def printCombinedFanSensorStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('CurrentSpeed')
            header.append('HigherAlarmThreshold')
            header.append('HigherWarningThreshold')
            header.append('LowerWarningThreshold')
            header.append('LowerAlarmThreshold')
            header.append('PMClassCAdminState')
            header.append('PMClassAAdminState')
            header.append('AdminState')
            header.append('PMClassBAdminState')

        objs = self.swtch.getAllFanSensorStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['CurrentSpeed'])
            r = self.swtch.getFanSensor(o['Name'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
                values.append('%s' % o['HigherAlarmThreshold'])
                values.append('%s' % o['HigherWarningThreshold'])
                values.append('%s' % o['LowerWarningThreshold'])
                values.append('%s' % o['LowerAlarmThreshold'])
                values.append('%s' % o['PMClassCAdminState'])
                values.append('%s' % o['PMClassAAdminState'])
                values.append('%s' % o['AdminState'])
                values.append('%s' % o['PMClassBAdminState'])
            rows.append(values)
        self.tblPrintObject('FanSensorState', header, rows)


    def printBfdSessionParams(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('RequiredMinRxInterval')
            header.append('AuthData')
            header.append('DemandEnabled')
            header.append('AuthKeyId')
            header.append('AuthType')
            header.append('DesiredMinTxInterval')
            header.append('AuthenticationEnabled')
            header.append('RequiredMinEchoRxInterval')
            header.append('LocalMultiplier')

        objs = self.swtch.getAllBfdSessionParams()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['RequiredMinRxInterval'])
            values.append('%s' % o['AuthData'])
            values.append('%s' % o['DemandEnabled'])
            values.append('%s' % o['AuthKeyId'])
            values.append('%s' % o['AuthType'])
            values.append('%s' % o['DesiredMinTxInterval'])
            values.append('%s' % o['AuthenticationEnabled'])
            values.append('%s' % o['RequiredMinEchoRxInterval'])
            values.append('%s' % o['LocalMultiplier'])
            rows.append(values)
        self.tblPrintObject('BfdSessionParam', header, rows)


    def printConfigLogStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('SeqNum')
            header.append('API')
            header.append('Time')
            header.append('Operation')
            header.append('Data')
            header.append('Result')
            header.append('UserAddr')
            header.append('UserName')

        objs = self.swtch.getAllConfigLogStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['SeqNum'])
            values.append('%s' % o['API'])
            values.append('%s' % o['Time'])
            values.append('%s' % o['Operation'])
            values.append('%s' % o['Data'])
            values.append('%s' % o['Result'])
            values.append('%s' % o['UserAddr'])
            values.append('%s' % o['UserName'])
            rows.append(values)
        self.tblPrintObject('ConfigLogState', header, rows)


    def printConfigLogState(self, SeqNum,API,Time, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('SeqNum')
            header.append('API')
            header.append('Time')
            header.append('Operation')
            header.append('Data')
            header.append('Result')
            header.append('UserAddr')
            header.append('UserName')

        rawobj = self.swtch.getConfigLogState(
                                              SeqNum,
                                              API,
                                              Time)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['SeqNum'])
            values.append('%s' % o['API'])
            values.append('%s' % o['Time'])
            values.append('%s' % o['Operation'])
            values.append('%s' % o['Data'])
            values.append('%s' % o['Result'])
            values.append('%s' % o['UserAddr'])
            values.append('%s' % o['UserName'])
            rows.append(values)
            self.tblPrintObject('ConfigLogState', header, rows)

        else:
            print rawobj.content

    def printBGPPolicyStmtStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('MatchConditions')
            header.append('Conditions')
            header.append('Actions')

        objs = self.swtch.getAllBGPPolicyStmtStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['MatchConditions'])
            values.append('%s' % o['Conditions'])
            values.append('%s' % o['Actions'])
            rows.append(values)
        self.tblPrintObject('BGPPolicyStmtState', header, rows)


    def printBGPPolicyStmtState(self, Name, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('MatchConditions')
            header.append('Conditions')
            header.append('Actions')

        rawobj = self.swtch.getBGPPolicyStmtState(
                                                  Name)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['MatchConditions'])
            values.append('%s' % o['Conditions'])
            values.append('%s' % o['Actions'])
            rows.append(values)
            self.tblPrintObject('BGPPolicyStmtState', header, rows)

        else:
            print rawobj.content

    def printCombinedBGPPolicyStmtStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('MatchConditions')
            header.append('Conditions')
            header.append('Actions')

        objs = self.swtch.getAllBGPPolicyStmtStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['MatchConditions'])
            values.append('%s' % o['Conditions'])
            values.append('%s' % o['Actions'])
            r = self.swtch.getBGPPolicyStmt(o['Name'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
            rows.append(values)
        self.tblPrintObject('BGPPolicyStmtState', header, rows)


    def printDWDMModuleStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('ModuleId')
            header.append('ModuleState')
            header.append('ModuleVoltage')
            header.append('ModuleTemp')
            header.append('Populated')
            header.append('VendorName')
            header.append('VendorPartNum')
            header.append('VendorSerialNum')
            header.append('VendorDateCode')
            header.append('ModuleHWVersion')
            header.append('ModuleActiveFWVersion')
            header.append('ModuleStandByFWVersion')
            header.append('ModuleActiveFWStatus')
            header.append('ModuleStandByFWStatus')

        objs = self.swtch.getAllDWDMModuleStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['ModuleId'])
            values.append('%s' % o['ModuleState'])
            values.append('%s' % o['ModuleVoltage'])
            values.append('%s' % o['ModuleTemp'])
            values.append('%s' % o['Populated'])
            values.append('%s' % o['VendorName'])
            values.append('%s' % o['VendorPartNum'])
            values.append('%s' % o['VendorSerialNum'])
            values.append('%s' % o['VendorDateCode'])
            values.append('%s' % o['ModuleHWVersion'])
            values.append('%s' % o['ModuleActiveFWVersion'])
            values.append('%s' % o['ModuleStandByFWVersion'])
            values.append('%s' % o['ModuleActiveFWStatus'])
            values.append('%s' % o['ModuleStandByFWStatus'])
            rows.append(values)
        self.tblPrintObject('DWDMModuleState', header, rows)


    def printDWDMModuleState(self, ModuleId, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('ModuleId')
            header.append('ModuleState')
            header.append('ModuleVoltage')
            header.append('ModuleTemp')
            header.append('Populated')
            header.append('VendorName')
            header.append('VendorPartNum')
            header.append('VendorSerialNum')
            header.append('VendorDateCode')
            header.append('ModuleHWVersion')
            header.append('ModuleActiveFWVersion')
            header.append('ModuleStandByFWVersion')
            header.append('ModuleActiveFWStatus')
            header.append('ModuleStandByFWStatus')

        rawobj = self.swtch.getDWDMModuleState(
                                               ModuleId)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['ModuleId'])
            values.append('%s' % o['ModuleState'])
            values.append('%s' % o['ModuleVoltage'])
            values.append('%s' % o['ModuleTemp'])
            values.append('%s' % o['Populated'])
            values.append('%s' % o['VendorName'])
            values.append('%s' % o['VendorPartNum'])
            values.append('%s' % o['VendorSerialNum'])
            values.append('%s' % o['VendorDateCode'])
            values.append('%s' % o['ModuleHWVersion'])
            values.append('%s' % o['ModuleActiveFWVersion'])
            values.append('%s' % o['ModuleStandByFWVersion'])
            values.append('%s' % o['ModuleActiveFWStatus'])
            values.append('%s' % o['ModuleStandByFWStatus'])
            rows.append(values)
            self.tblPrintObject('DWDMModuleState', header, rows)

        else:
            print rawobj.content

    def printCombinedDWDMModuleStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('ModuleId')
            header.append('ModuleState')
            header.append('ModuleVoltage')
            header.append('ModuleTemp')
            header.append('Populated')
            header.append('VendorName')
            header.append('VendorPartNum')
            header.append('VendorSerialNum')
            header.append('VendorDateCode')
            header.append('ModuleHWVersion')
            header.append('ModuleActiveFWVersion')
            header.append('ModuleStandByFWVersion')
            header.append('ModuleActiveFWStatus')
            header.append('ModuleStandByFWStatus')
            header.append('EnableExtPMTickSrc')
            header.append('PMInterval')
            header.append('AdminState')
            header.append('IndependentLaneMode')

        objs = self.swtch.getAllDWDMModuleStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['ModuleId'])
            values.append('%s' % o['ModuleState'])
            values.append('%s' % o['ModuleVoltage'])
            values.append('%s' % o['ModuleTemp'])
            values.append('%s' % o['Populated'])
            values.append('%s' % o['VendorName'])
            values.append('%s' % o['VendorPartNum'])
            values.append('%s' % o['VendorSerialNum'])
            values.append('%s' % o['VendorDateCode'])
            values.append('%s' % o['ModuleHWVersion'])
            values.append('%s' % o['ModuleActiveFWVersion'])
            values.append('%s' % o['ModuleStandByFWVersion'])
            values.append('%s' % o['ModuleActiveFWStatus'])
            values.append('%s' % o['ModuleStandByFWStatus'])
            r = self.swtch.getDWDMModule(o['ModuleId'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
                values.append('%s' % o['EnableExtPMTickSrc'])
                values.append('%s' % o['PMInterval'])
                values.append('%s' % o['AdminState'])
                values.append('%s' % o['IndependentLaneMode'])
            rows.append(values)
        self.tblPrintObject('DWDMModuleState', header, rows)


    def printDhcpRelayIntfStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IfIndex')
            header.append('TotalDrops')
            header.append('TotalDhcpClientRx')
            header.append('TotalDhcpClientTx')
            header.append('TotalDhcpServerRx')
            header.append('TotalDhcpServerTx')

        objs = self.swtch.getAllDhcpRelayIntfStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['TotalDrops'])
            values.append('%s' % o['TotalDhcpClientRx'])
            values.append('%s' % o['TotalDhcpClientTx'])
            values.append('%s' % o['TotalDhcpServerRx'])
            values.append('%s' % o['TotalDhcpServerTx'])
            rows.append(values)
        self.tblPrintObject('DhcpRelayIntfState', header, rows)


    def printDhcpRelayIntfState(self, IfIndex, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IfIndex')
            header.append('TotalDrops')
            header.append('TotalDhcpClientRx')
            header.append('TotalDhcpClientTx')
            header.append('TotalDhcpServerRx')
            header.append('TotalDhcpServerTx')

        rawobj = self.swtch.getDhcpRelayIntfState(
                                                  IfIndex)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['TotalDrops'])
            values.append('%s' % o['TotalDhcpClientRx'])
            values.append('%s' % o['TotalDhcpClientTx'])
            values.append('%s' % o['TotalDhcpServerRx'])
            values.append('%s' % o['TotalDhcpServerTx'])
            rows.append(values)
            self.tblPrintObject('DhcpRelayIntfState', header, rows)

        else:
            print rawobj.content

    def printCombinedDhcpRelayIntfStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IfIndex')
            header.append('TotalDrops')
            header.append('TotalDhcpClientRx')
            header.append('TotalDhcpClientTx')
            header.append('TotalDhcpServerRx')
            header.append('TotalDhcpServerTx')
            header.append('Enable')
            header.append('ServerIp')

        objs = self.swtch.getAllDhcpRelayIntfStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['TotalDrops'])
            values.append('%s' % o['TotalDhcpClientRx'])
            values.append('%s' % o['TotalDhcpClientTx'])
            values.append('%s' % o['TotalDhcpServerRx'])
            values.append('%s' % o['TotalDhcpServerTx'])
            r = self.swtch.getDhcpRelayIntf(o['IfIndex'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
                values.append('%s' % o['Enable'])
                values.append('%s' % o['ServerIp'])
            rows.append(values)
        self.tblPrintObject('DhcpRelayIntfState', header, rows)


    def printLaPortChannelIntfRefListStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('LagIntfRef')
            header.append('OperState')
            header.append('IfIndex')
            header.append('Activity')
            header.append('Timeout')
            header.append('Synchronization')
            header.append('Aggregatable')
            header.append('Collecting')
            header.append('Distributing')
            header.append('Defaulted')
            header.append('SystemId')
            header.append('OperKey')
            header.append('DrniName')
            header.append('DrniSynced')
            header.append('PartnerId')
            header.append('PartnerKey')
            header.append('DebugId')
            header.append('RxMachine')
            header.append('RxTime')
            header.append('MuxMachine')
            header.append('MuxReason')
            header.append('ActorChurnMachine')
            header.append('PartnerChurnMachine')
            header.append('ActorChurnCount')
            header.append('PartnerChurnCount')
            header.append('ActorSyncTransitionCount')
            header.append('PartnerSyncTransitionCount')
            header.append('ActorChangeCount')
            header.append('PartnerChangeCount')
            header.append('ActorCdsChurnMachine')
            header.append('PartnerCdsChurnMachine')
            header.append('ActorCdsChurnCount')
            header.append('PartnerCdsChurnCount')
            header.append('LacpInPkts')
            header.append('LacpOutPkts')
            header.append('LacpRxErrors')
            header.append('LacpTxErrors')
            header.append('LacpUnknownErrors')
            header.append('LacpErrors')
            header.append('LacpInMissMatchPkts')
            header.append('LampInPdu')
            header.append('LampInResponsePdu')
            header.append('LampOutPdu')
            header.append('LampOutResponsePdu')

        objs = self.swtch.getAllLaPortChannelIntfRefListStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['LagIntfRef'])
            values.append('%s' % o['OperState'])
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['Activity'])
            values.append('%s' % o['Timeout'])
            values.append('%s' % o['Synchronization'])
            values.append('%s' % o['Aggregatable'])
            values.append('%s' % o['Collecting'])
            values.append('%s' % o['Distributing'])
            values.append('%s' % o['Defaulted'])
            values.append('%s' % o['SystemId'])
            values.append('%s' % o['OperKey'])
            values.append('%s' % o['DrniName'])
            values.append('%s' % o['DrniSynced'])
            values.append('%s' % o['PartnerId'])
            values.append('%s' % o['PartnerKey'])
            values.append('%s' % o['DebugId'])
            values.append('%s' % o['RxMachine'])
            values.append('%s' % o['RxTime'])
            values.append('%s' % o['MuxMachine'])
            values.append('%s' % o['MuxReason'])
            values.append('%s' % o['ActorChurnMachine'])
            values.append('%s' % o['PartnerChurnMachine'])
            values.append('%s' % o['ActorChurnCount'])
            values.append('%s' % o['PartnerChurnCount'])
            values.append('%s' % o['ActorSyncTransitionCount'])
            values.append('%s' % o['PartnerSyncTransitionCount'])
            values.append('%s' % o['ActorChangeCount'])
            values.append('%s' % o['PartnerChangeCount'])
            values.append('%s' % o['ActorCdsChurnMachine'])
            values.append('%s' % o['PartnerCdsChurnMachine'])
            values.append('%s' % o['ActorCdsChurnCount'])
            values.append('%s' % o['PartnerCdsChurnCount'])
            values.append('%s' % o['LacpInPkts'])
            values.append('%s' % o['LacpOutPkts'])
            values.append('%s' % o['LacpRxErrors'])
            values.append('%s' % o['LacpTxErrors'])
            values.append('%s' % o['LacpUnknownErrors'])
            values.append('%s' % o['LacpErrors'])
            values.append('%s' % o['LacpInMissMatchPkts'])
            values.append('%s' % o['LampInPdu'])
            values.append('%s' % o['LampInResponsePdu'])
            values.append('%s' % o['LampOutPdu'])
            values.append('%s' % o['LampOutResponsePdu'])
            rows.append(values)
        self.tblPrintObject('LaPortChannelIntfRefListState', header, rows)


    def printLaPortChannelIntfRefListState(self, IntfRef, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('LagIntfRef')
            header.append('OperState')
            header.append('IfIndex')
            header.append('Activity')
            header.append('Timeout')
            header.append('Synchronization')
            header.append('Aggregatable')
            header.append('Collecting')
            header.append('Distributing')
            header.append('Defaulted')
            header.append('SystemId')
            header.append('OperKey')
            header.append('DrniName')
            header.append('DrniSynced')
            header.append('PartnerId')
            header.append('PartnerKey')
            header.append('DebugId')
            header.append('RxMachine')
            header.append('RxTime')
            header.append('MuxMachine')
            header.append('MuxReason')
            header.append('ActorChurnMachine')
            header.append('PartnerChurnMachine')
            header.append('ActorChurnCount')
            header.append('PartnerChurnCount')
            header.append('ActorSyncTransitionCount')
            header.append('PartnerSyncTransitionCount')
            header.append('ActorChangeCount')
            header.append('PartnerChangeCount')
            header.append('ActorCdsChurnMachine')
            header.append('PartnerCdsChurnMachine')
            header.append('ActorCdsChurnCount')
            header.append('PartnerCdsChurnCount')
            header.append('LacpInPkts')
            header.append('LacpOutPkts')
            header.append('LacpRxErrors')
            header.append('LacpTxErrors')
            header.append('LacpUnknownErrors')
            header.append('LacpErrors')
            header.append('LacpInMissMatchPkts')
            header.append('LampInPdu')
            header.append('LampInResponsePdu')
            header.append('LampOutPdu')
            header.append('LampOutResponsePdu')

        rawobj = self.swtch.getLaPortChannelIntfRefListState(
                                                             IntfRef)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['LagIntfRef'])
            values.append('%s' % o['OperState'])
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['Activity'])
            values.append('%s' % o['Timeout'])
            values.append('%s' % o['Synchronization'])
            values.append('%s' % o['Aggregatable'])
            values.append('%s' % o['Collecting'])
            values.append('%s' % o['Distributing'])
            values.append('%s' % o['Defaulted'])
            values.append('%s' % o['SystemId'])
            values.append('%s' % o['OperKey'])
            values.append('%s' % o['DrniName'])
            values.append('%s' % o['DrniSynced'])
            values.append('%s' % o['PartnerId'])
            values.append('%s' % o['PartnerKey'])
            values.append('%s' % o['DebugId'])
            values.append('%s' % o['RxMachine'])
            values.append('%s' % o['RxTime'])
            values.append('%s' % o['MuxMachine'])
            values.append('%s' % o['MuxReason'])
            values.append('%s' % o['ActorChurnMachine'])
            values.append('%s' % o['PartnerChurnMachine'])
            values.append('%s' % o['ActorChurnCount'])
            values.append('%s' % o['PartnerChurnCount'])
            values.append('%s' % o['ActorSyncTransitionCount'])
            values.append('%s' % o['PartnerSyncTransitionCount'])
            values.append('%s' % o['ActorChangeCount'])
            values.append('%s' % o['PartnerChangeCount'])
            values.append('%s' % o['ActorCdsChurnMachine'])
            values.append('%s' % o['PartnerCdsChurnMachine'])
            values.append('%s' % o['ActorCdsChurnCount'])
            values.append('%s' % o['PartnerCdsChurnCount'])
            values.append('%s' % o['LacpInPkts'])
            values.append('%s' % o['LacpOutPkts'])
            values.append('%s' % o['LacpRxErrors'])
            values.append('%s' % o['LacpTxErrors'])
            values.append('%s' % o['LacpUnknownErrors'])
            values.append('%s' % o['LacpErrors'])
            values.append('%s' % o['LacpInMissMatchPkts'])
            values.append('%s' % o['LampInPdu'])
            values.append('%s' % o['LampInResponsePdu'])
            values.append('%s' % o['LampOutPdu'])
            values.append('%s' % o['LampOutResponsePdu'])
            rows.append(values)
            self.tblPrintObject('LaPortChannelIntfRefListState', header, rows)

        else:
            print rawobj.content

    def printDhcpRelayGlobals(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Vrf')
            header.append('Enable')

        objs = self.swtch.getAllDhcpRelayGlobals()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Vrf'])
            values.append('%s' % o['Enable'])
            rows.append(values)
        self.tblPrintObject('DhcpRelayGlobal', header, rows)


    def printPlatformStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('ObjName')
            header.append('ProductName')
            header.append('SerialNum')
            header.append('Manufacturer')
            header.append('Vendor')
            header.append('Release')
            header.append('PlatformName')
            header.append('Version')

        objs = self.swtch.getAllPlatformStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['ObjName'])
            values.append('%s' % o['ProductName'])
            values.append('%s' % o['SerialNum'])
            values.append('%s' % o['Manufacturer'])
            values.append('%s' % o['Vendor'])
            values.append('%s' % o['Release'])
            values.append('%s' % o['PlatformName'])
            values.append('%s' % o['Version'])
            rows.append(values)
        self.tblPrintObject('PlatformState', header, rows)


    def printPlatformState(self, ObjName, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('ObjName')
            header.append('ProductName')
            header.append('SerialNum')
            header.append('Manufacturer')
            header.append('Vendor')
            header.append('Release')
            header.append('PlatformName')
            header.append('Version')

        rawobj = self.swtch.getPlatformState(
                                             ObjName)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['ObjName'])
            values.append('%s' % o['ProductName'])
            values.append('%s' % o['SerialNum'])
            values.append('%s' % o['Manufacturer'])
            values.append('%s' % o['Vendor'])
            values.append('%s' % o['Release'])
            values.append('%s' % o['PlatformName'])
            values.append('%s' % o['Version'])
            rows.append(values)
            self.tblPrintObject('PlatformState', header, rows)

        else:
            print rawobj.content

    def printBfdSessionParamStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('NumSessions')
            header.append('LocalMultiplier')
            header.append('DesiredMinTxInterval')
            header.append('RequiredMinRxInterval')
            header.append('RequiredMinEchoRxInterval')
            header.append('DemandEnabled')
            header.append('AuthenticationEnabled')
            header.append('AuthenticationType')
            header.append('AuthenticationKeyId')
            header.append('AuthenticationData')

        objs = self.swtch.getAllBfdSessionParamStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['NumSessions'])
            values.append('%s' % o['LocalMultiplier'])
            values.append('%s' % o['DesiredMinTxInterval'])
            values.append('%s' % o['RequiredMinRxInterval'])
            values.append('%s' % o['RequiredMinEchoRxInterval'])
            values.append('%s' % o['DemandEnabled'])
            values.append('%s' % o['AuthenticationEnabled'])
            values.append('%s' % o['AuthenticationType'])
            values.append('%s' % o['AuthenticationKeyId'])
            values.append('%s' % o['AuthenticationData'])
            rows.append(values)
        self.tblPrintObject('BfdSessionParamState', header, rows)


    def printBfdSessionParamState(self, Name, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('NumSessions')
            header.append('LocalMultiplier')
            header.append('DesiredMinTxInterval')
            header.append('RequiredMinRxInterval')
            header.append('RequiredMinEchoRxInterval')
            header.append('DemandEnabled')
            header.append('AuthenticationEnabled')
            header.append('AuthenticationType')
            header.append('AuthenticationKeyId')
            header.append('AuthenticationData')

        rawobj = self.swtch.getBfdSessionParamState(
                                                    Name)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['NumSessions'])
            values.append('%s' % o['LocalMultiplier'])
            values.append('%s' % o['DesiredMinTxInterval'])
            values.append('%s' % o['RequiredMinRxInterval'])
            values.append('%s' % o['RequiredMinEchoRxInterval'])
            values.append('%s' % o['DemandEnabled'])
            values.append('%s' % o['AuthenticationEnabled'])
            values.append('%s' % o['AuthenticationType'])
            values.append('%s' % o['AuthenticationKeyId'])
            values.append('%s' % o['AuthenticationData'])
            rows.append(values)
            self.tblPrintObject('BfdSessionParamState', header, rows)

        else:
            print rawobj.content

    def printCombinedBfdSessionParamStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('NumSessions')
            header.append('LocalMultiplier')
            header.append('DesiredMinTxInterval')
            header.append('RequiredMinRxInterval')
            header.append('RequiredMinEchoRxInterval')
            header.append('DemandEnabled')
            header.append('AuthenticationEnabled')
            header.append('AuthenticationType')
            header.append('AuthenticationKeyId')
            header.append('AuthenticationData')
            header.append('AuthData')
            header.append('AuthKeyId')
            header.append('AuthType')

        objs = self.swtch.getAllBfdSessionParamStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['NumSessions'])
            values.append('%s' % o['LocalMultiplier'])
            values.append('%s' % o['DesiredMinTxInterval'])
            values.append('%s' % o['RequiredMinRxInterval'])
            values.append('%s' % o['RequiredMinEchoRxInterval'])
            values.append('%s' % o['DemandEnabled'])
            values.append('%s' % o['AuthenticationEnabled'])
            values.append('%s' % o['AuthenticationType'])
            values.append('%s' % o['AuthenticationKeyId'])
            values.append('%s' % o['AuthenticationData'])
            r = self.swtch.getBfdSessionParam(o['Name'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
                values.append('%s' % o['AuthData'])
                values.append('%s' % o['AuthKeyId'])
                values.append('%s' % o['AuthType'])
            rows.append(values)
        self.tblPrintObject('BfdSessionParamState', header, rows)


    def printAsicGlobalStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('ModuleId')
            header.append('VendorId')
            header.append('PartNumber')
            header.append('RevisionId')
            header.append('ModuleTemp')

        objs = self.swtch.getAllAsicGlobalStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['ModuleId'])
            values.append('%s' % o['VendorId'])
            values.append('%s' % o['PartNumber'])
            values.append('%s' % o['RevisionId'])
            values.append('%s' % o['ModuleTemp'])
            rows.append(values)
        self.tblPrintObject('AsicGlobalState', header, rows)


    def printAsicGlobalState(self, ModuleId, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('ModuleId')
            header.append('VendorId')
            header.append('PartNumber')
            header.append('RevisionId')
            header.append('ModuleTemp')

        rawobj = self.swtch.getAsicGlobalState(
                                               ModuleId)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['ModuleId'])
            values.append('%s' % o['VendorId'])
            values.append('%s' % o['PartNumber'])
            values.append('%s' % o['RevisionId'])
            values.append('%s' % o['ModuleTemp'])
            rows.append(values)
            self.tblPrintObject('AsicGlobalState', header, rows)

        else:
            print rawobj.content

    def printOspfLsdbEntryStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('LsdbType')
            header.append('LsdbAreaId')
            header.append('LsdbLsid')
            header.append('LsdbRouterId')
            header.append('LsdbSequence')
            header.append('LsdbAge')
            header.append('LsdbChecksum')
            header.append('LsdbAdvertisement')

        objs = self.swtch.getAllOspfLsdbEntryStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['LsdbType'])
            values.append('%s' % o['LsdbAreaId'])
            values.append('%s' % o['LsdbLsid'])
            values.append('%s' % o['LsdbRouterId'])
            values.append('%s' % o['LsdbSequence'])
            values.append('%s' % o['LsdbAge'])
            values.append('%s' % o['LsdbChecksum'])
            values.append('%s' % o['LsdbAdvertisement'])
            rows.append(values)
        self.tblPrintObject('OspfLsdbEntryState', header, rows)


    def printOspfLsdbEntryState(self, LsdbType,LsdbAreaId,LsdbLsid,LsdbRouterId, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('LsdbType')
            header.append('LsdbAreaId')
            header.append('LsdbLsid')
            header.append('LsdbRouterId')
            header.append('LsdbSequence')
            header.append('LsdbAge')
            header.append('LsdbChecksum')
            header.append('LsdbAdvertisement')

        rawobj = self.swtch.getOspfLsdbEntryState(
                                                  LsdbType,
                                                  LsdbAreaId,
                                                  LsdbLsid,
                                                  LsdbRouterId)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['LsdbType'])
            values.append('%s' % o['LsdbAreaId'])
            values.append('%s' % o['LsdbLsid'])
            values.append('%s' % o['LsdbRouterId'])
            values.append('%s' % o['LsdbSequence'])
            values.append('%s' % o['LsdbAge'])
            values.append('%s' % o['LsdbChecksum'])
            values.append('%s' % o['LsdbAdvertisement'])
            rows.append(values)
            self.tblPrintObject('OspfLsdbEntryState', header, rows)

        else:
            print rawobj.content

    def printArpLinuxEntryStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IpAddr')
            header.append('HWType')
            header.append('MacAddr')
            header.append('IfName')

        objs = self.swtch.getAllArpLinuxEntryStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IpAddr'])
            values.append('%s' % o['HWType'])
            values.append('%s' % o['MacAddr'])
            values.append('%s' % o['IfName'])
            rows.append(values)
        self.tblPrintObject('ArpLinuxEntryState', header, rows)


    def printArpLinuxEntryState(self, IpAddr, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IpAddr')
            header.append('HWType')
            header.append('MacAddr')
            header.append('IfName')

        rawobj = self.swtch.getArpLinuxEntryState(
                                                  IpAddr)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['IpAddr'])
            values.append('%s' % o['HWType'])
            values.append('%s' % o['MacAddr'])
            values.append('%s' % o['IfName'])
            rows.append(values)
            self.tblPrintObject('ArpLinuxEntryState', header, rows)

        else:
            print rawobj.content

    def printStpGlobals(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Vrf')
            header.append('AdminState')

        objs = self.swtch.getAllStpGlobals()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Vrf'])
            values.append('%s' % o['AdminState'])
            rows.append(values)
        self.tblPrintObject('StpGlobal', header, rows)


    def printDistributedRelays(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('DrniName')
            header.append('PortalAddress')
            header.append('PortalSystemNumber')
            header.append('IntfReflist')
            header.append('IntfRef')
            header.append('PortalPriority')
            header.append('GatewayAlgorithm')
            header.append('NeighborAdminDRCPState')
            header.append('NeighborGatewayAlgorithm')
            header.append('ThreePortalSystem')
            header.append('IntraPortalPortProtocolDA')
            header.append('NeighborPortAlgorithm')
            header.append('EncapMethod')

        objs = self.swtch.getAllDistributedRelays()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['DrniName'])
            values.append('%s' % o['PortalAddress'])
            values.append('%s' % o['PortalSystemNumber'])
            values.append('%s' % o['IntfReflist'])
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['PortalPriority'])
            values.append('%s' % o['GatewayAlgorithm'])
            values.append('%s' % o['NeighborAdminDRCPState'])
            values.append('%s' % o['NeighborGatewayAlgorithm'])
            values.append('%s' % o['ThreePortalSystem'])
            values.append('%s' % o['IntraPortalPortProtocolDA'])
            values.append('%s' % o['NeighborPortAlgorithm'])
            values.append('%s' % o['EncapMethod'])
            rows.append(values)
        self.tblPrintObject('DistributedRelay', header, rows)


    def printBGPPolicyConditions(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('ConditionType')
            header.append('IpPrefix')
            header.append('MaskLengthRange')

        objs = self.swtch.getAllBGPPolicyConditions()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['ConditionType'])
            values.append('%s' % o['IpPrefix'])
            values.append('%s' % o['MaskLengthRange'])
            rows.append(values)
        self.tblPrintObject('BGPPolicyCondition', header, rows)


    def printOspfGlobals(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('RouterId')
            header.append('AdminStat')
            header.append('ASBdrRtrStatus')
            header.append('RestartSupport')
            header.append('RestartInterval')
            header.append('TOSSupport')
            header.append('ReferenceBandwidth')

        objs = self.swtch.getAllOspfGlobals()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['RouterId'])
            values.append('%s' % o['AdminStat'])
            values.append('%s' % o['ASBdrRtrStatus'])
            values.append('%s' % o['RestartSupport'])
            values.append('%s' % o['RestartInterval'])
            values.append('%s' % o['TOSSupport'])
            values.append('%s' % o['ReferenceBandwidth'])
            rows.append(values)
        self.tblPrintObject('OspfGlobal', header, rows)


    def printDhcpRelayHostDhcpStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('MacAddr')
            header.append('ServerIp')
            header.append('OfferedIp')
            header.append('GatewayIp')
            header.append('AcceptedIp')
            header.append('RequestedIp')
            header.append('ClientDiscover')
            header.append('ClientRequest')
            header.append('ClientRequests')
            header.append('ClientResponses')
            header.append('ServerOffer')
            header.append('ServerAck')
            header.append('ServerRequests')
            header.append('ServerResponses')

        objs = self.swtch.getAllDhcpRelayHostDhcpStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['MacAddr'])
            values.append('%s' % o['ServerIp'])
            values.append('%s' % o['OfferedIp'])
            values.append('%s' % o['GatewayIp'])
            values.append('%s' % o['AcceptedIp'])
            values.append('%s' % o['RequestedIp'])
            values.append('%s' % o['ClientDiscover'])
            values.append('%s' % o['ClientRequest'])
            values.append('%s' % o['ClientRequests'])
            values.append('%s' % o['ClientResponses'])
            values.append('%s' % o['ServerOffer'])
            values.append('%s' % o['ServerAck'])
            values.append('%s' % o['ServerRequests'])
            values.append('%s' % o['ServerResponses'])
            rows.append(values)
        self.tblPrintObject('DhcpRelayHostDhcpState', header, rows)


    def printDhcpRelayHostDhcpState(self, MacAddr, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('MacAddr')
            header.append('ServerIp')
            header.append('OfferedIp')
            header.append('GatewayIp')
            header.append('AcceptedIp')
            header.append('RequestedIp')
            header.append('ClientDiscover')
            header.append('ClientRequest')
            header.append('ClientRequests')
            header.append('ClientResponses')
            header.append('ServerOffer')
            header.append('ServerAck')
            header.append('ServerRequests')
            header.append('ServerResponses')

        rawobj = self.swtch.getDhcpRelayHostDhcpState(
                                                      MacAddr)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['MacAddr'])
            values.append('%s' % o['ServerIp'])
            values.append('%s' % o['OfferedIp'])
            values.append('%s' % o['GatewayIp'])
            values.append('%s' % o['AcceptedIp'])
            values.append('%s' % o['RequestedIp'])
            values.append('%s' % o['ClientDiscover'])
            values.append('%s' % o['ClientRequest'])
            values.append('%s' % o['ClientRequests'])
            values.append('%s' % o['ClientResponses'])
            values.append('%s' % o['ServerOffer'])
            values.append('%s' % o['ServerAck'])
            values.append('%s' % o['ServerRequests'])
            values.append('%s' % o['ServerResponses'])
            rows.append(values)
            self.tblPrintObject('DhcpRelayHostDhcpState', header, rows)

        else:
            print rawobj.content

    def printDhcpRelayIntfServerStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfId')
            header.append('ServerIp')
            header.append('Request')
            header.append('Responses')

        objs = self.swtch.getAllDhcpRelayIntfServerStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfId'])
            values.append('%s' % o['ServerIp'])
            values.append('%s' % o['Request'])
            values.append('%s' % o['Responses'])
            rows.append(values)
        self.tblPrintObject('DhcpRelayIntfServerState', header, rows)


    def printDhcpRelayIntfServerState(self, IntfId, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfId')
            header.append('ServerIp')
            header.append('Request')
            header.append('Responses')

        rawobj = self.swtch.getDhcpRelayIntfServerState(
                                                        IntfId)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfId'])
            values.append('%s' % o['ServerIp'])
            values.append('%s' % o['Request'])
            values.append('%s' % o['Responses'])
            rows.append(values)
            self.tblPrintObject('DhcpRelayIntfServerState', header, rows)

        else:
            print rawobj.content

    def printLLDPIntfStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
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

        objs = self.swtch.getAllLLDPIntfStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['SendFrames'])
            values.append('%s' % o['ReceivedFrames'])
            values.append('%s' % o['Enable'])
            values.append('%s' % o['LocalPort'])
            values.append('%s' % o['PeerMac'])
            values.append('%s' % o['PeerPort'])
            values.append('%s' % o['PeerHostName'])
            values.append('%s' % o['HoldTime'])
            values.append('%s' % o['SystemDescription'])
            values.append('%s' % o['SystemCapabilities'])
            values.append('%s' % o['EnabledCapabilities'])
            rows.append(values)   
        var1=self.tblPrintObject('LLDPIntfState', header, rows)
        #print "###############"
        #print var1
        #print "###############"
        return var1
        


    def printLLDPIntfState(self, IntfRef, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
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

        rawobj = self.swtch.getLLDPIntfState(
                                             IntfRef)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['SendFrames'])
            values.append('%s' % o['ReceivedFrames'])
            values.append('%s' % o['Enable'])
            values.append('%s' % o['LocalPort'])
            values.append('%s' % o['PeerMac'])
            values.append('%s' % o['PeerPort'])
            values.append('%s' % o['PeerHostName'])
            values.append('%s' % o['HoldTime'])
            values.append('%s' % o['SystemDescription'])
            values.append('%s' % o['SystemCapabilities'])
            values.append('%s' % o['EnabledCapabilities'])
            rows.append(values)
            self.tblPrintObject('LLDPIntfState', header, rows)

        else:
            print rawobj.content

    def printCombinedLLDPIntfStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
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
            header.append('TxRxMode')

        objs = self.swtch.getAllLLDPIntfStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['SendFrames'])
            values.append('%s' % o['ReceivedFrames'])
            values.append('%s' % o['Enable'])
            values.append('%s' % o['LocalPort'])
            values.append('%s' % o['PeerMac'])
            values.append('%s' % o['PeerPort'])
            values.append('%s' % o['PeerHostName'])
            values.append('%s' % o['HoldTime'])
            values.append('%s' % o['SystemDescription'])
            values.append('%s' % o['SystemCapabilities'])
            values.append('%s' % o['EnabledCapabilities'])
            r = self.swtch.getLLDPIntf(o['IntfRef'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
                values.append('%s' % o['TxRxMode'])
            rows.append(values)
        self.tblPrintObject('LLDPIntfState', header, rows)


    def printLeds(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('LedId')
            header.append('LedAdmin')
            header.append('LedSetColor')

        objs = self.swtch.getAllLeds()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['LedId'])
            values.append('%s' % o['LedAdmin'])
            values.append('%s' % o['LedSetColor'])
            rows.append(values)
        self.tblPrintObject('Led', header, rows)


    def printPolicyDefinitions(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('Priority')
            header.append('StatementList')
            header.append('MatchType')
            header.append('PolicyType')

        objs = self.swtch.getAllPolicyDefinitions()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['Priority'])
            values.append('%s' % o['StatementList'])
            values.append('%s' % o['MatchType'])
            values.append('%s' % o['PolicyType'])
            rows.append(values)
        var = self.tblPrintObject('PolicyDefinition', header, rows)
        return var

    def printAclStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('AclName')
            header.append('Direction')
            header.append('RuleNameList')
            header.append('IntfList')

        objs = self.swtch.getAllAclStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['AclName'])
            values.append('%s' % o['Direction'])
            values.append('%s' % o['RuleNameList'])
            values.append('%s' % o['IntfList'])
            rows.append(values)
        self.tblPrintObject('AclState', header, rows)


    def printAclState(self, AclName,Direction, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('AclName')
            header.append('Direction')
            header.append('RuleNameList')
            header.append('IntfList')

        rawobj = self.swtch.getAclState(
                                        AclName,
                                        Direction)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['AclName'])
            values.append('%s' % o['Direction'])
            values.append('%s' % o['RuleNameList'])
            values.append('%s' % o['IntfList'])
            rows.append(values)
            self.tblPrintObject('AclState', header, rows)

        else:
            print rawobj.content

    def printCombinedAclStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('AclName')
            header.append('Direction')
            header.append('RuleNameList')
            header.append('IntfList')
            header.append('AclType')

        objs = self.swtch.getAllAclStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['AclName'])
            values.append('%s' % o['Direction'])
            values.append('%s' % o['RuleNameList'])
            values.append('%s' % o['IntfList'])
            r = self.swtch.getAcl(o['AclName'], o['Direction'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
                values.append('%s' % o['AclType'])
            rows.append(values)
        self.tblPrintObject('AclState', header, rows)


    def printEthernetPMs(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Resource')
            header.append('IntfRef')
            header.append('PMClassBEnable')
            header.append('PMClassCEnable')
            header.append('HighWarnThreshold')
            header.append('LowAlarmThreshold')
            header.append('PMClassAEnable')
            header.append('HighAlarmThreshold')
            header.append('LowWarnThreshold')

        objs = self.swtch.getAllEthernetPMs()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Resource'])
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['PMClassBEnable'])
            values.append('%s' % o['PMClassCEnable'])
            values.append('%s' % o['HighWarnThreshold'])
            values.append('%s' % o['LowAlarmThreshold'])
            values.append('%s' % o['PMClassAEnable'])
            values.append('%s' % o['HighAlarmThreshold'])
            values.append('%s' % o['LowWarnThreshold'])
            rows.append(values)
        self.tblPrintObject('EthernetPM', header, rows)


    def printOspfVirtNbrEntryStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('VirtNbrRtrId')
            header.append('VirtNbrArea')
            header.append('VirtNbrIpAddr')
            header.append('VirtNbrOptions')
            header.append('VirtNbrState')
            header.append('VirtNbrEvents')
            header.append('VirtNbrHelloSuppressed')

        objs = self.swtch.getAllOspfVirtNbrEntryStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['VirtNbrRtrId'])
            values.append('%s' % o['VirtNbrArea'])
            values.append('%s' % o['VirtNbrIpAddr'])
            values.append('%s' % o['VirtNbrOptions'])
            values.append('%s' % o['VirtNbrState'])
            values.append('%s' % o['VirtNbrEvents'])
            values.append('%s' % o['VirtNbrHelloSuppressed'])
            rows.append(values)
        self.tblPrintObject('OspfVirtNbrEntryState', header, rows)


    def printOspfVirtNbrEntryState(self, VirtNbrRtrId,VirtNbrArea, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('VirtNbrRtrId')
            header.append('VirtNbrArea')
            header.append('VirtNbrIpAddr')
            header.append('VirtNbrOptions')
            header.append('VirtNbrState')
            header.append('VirtNbrEvents')
            header.append('VirtNbrHelloSuppressed')

        rawobj = self.swtch.getOspfVirtNbrEntryState(
                                                     VirtNbrRtrId,
                                                     VirtNbrArea)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['VirtNbrRtrId'])
            values.append('%s' % o['VirtNbrArea'])
            values.append('%s' % o['VirtNbrIpAddr'])
            values.append('%s' % o['VirtNbrOptions'])
            values.append('%s' % o['VirtNbrState'])
            values.append('%s' % o['VirtNbrEvents'])
            values.append('%s' % o['VirtNbrHelloSuppressed'])
            rows.append(values)
            self.tblPrintObject('OspfVirtNbrEntryState', header, rows)

        else:
            print rawobj.content

    def printDWDMModuleClntIntfStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('ClntIntfId')
            header.append('ModuleId')
            header.append('PRBSTxErrCntLane0')
            header.append('PRBSTxErrCntLane1')
            header.append('PRBSTxErrCntLane2')
            header.append('PRBSTxErrCntLane3')

        objs = self.swtch.getAllDWDMModuleClntIntfStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['ClntIntfId'])
            values.append('%s' % o['ModuleId'])
            values.append('%s' % o['PRBSTxErrCntLane0'])
            values.append('%s' % o['PRBSTxErrCntLane1'])
            values.append('%s' % o['PRBSTxErrCntLane2'])
            values.append('%s' % o['PRBSTxErrCntLane3'])
            rows.append(values)
        self.tblPrintObject('DWDMModuleClntIntfState', header, rows)


    def printDWDMModuleClntIntfState(self, ClntIntfId,ModuleId, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('ClntIntfId')
            header.append('ModuleId')
            header.append('PRBSTxErrCntLane0')
            header.append('PRBSTxErrCntLane1')
            header.append('PRBSTxErrCntLane2')
            header.append('PRBSTxErrCntLane3')

        rawobj = self.swtch.getDWDMModuleClntIntfState(
                                                       ClntIntfId,
                                                       ModuleId)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['ClntIntfId'])
            values.append('%s' % o['ModuleId'])
            values.append('%s' % o['PRBSTxErrCntLane0'])
            values.append('%s' % o['PRBSTxErrCntLane1'])
            values.append('%s' % o['PRBSTxErrCntLane2'])
            values.append('%s' % o['PRBSTxErrCntLane3'])
            rows.append(values)
            self.tblPrintObject('DWDMModuleClntIntfState', header, rows)

        else:
            print rawobj.content

    def printCombinedDWDMModuleClntIntfStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('ClntIntfId')
            header.append('ModuleId')
            header.append('PRBSTxErrCntLane0')
            header.append('PRBSTxErrCntLane1')
            header.append('PRBSTxErrCntLane2')
            header.append('PRBSTxErrCntLane3')
            header.append('NwLaneTributaryToClntIntfMap')
            header.append('HostTxEqDfe')
            header.append('HostRxSerializerTap1Gain')
            header.append('RxPRBSPattern')
            header.append('HostRxSerializerTap2Delay')
            header.append('HostRxSerializerTap2Gain')
            header.append('HostRxSerializerTap0Delay')
            header.append('HostTxEqCtle')
            header.append('TxPRBSPattern')
            header.append('HostTxEqLfCtle')
            header.append('AdminState')
            header.append('RXFECDecDisable')
            header.append('EnableTxPRBSChecker')
            header.append('EnableHostLoopback')
            header.append('HostRxSerializerTap0Gain')
            header.append('TXFECDecDisable')
            header.append('EnableRxPRBS')
            header.append('EnableIntSerdesNWLoopback')

        objs = self.swtch.getAllDWDMModuleClntIntfStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['ClntIntfId'])
            values.append('%s' % o['ModuleId'])
            values.append('%s' % o['PRBSTxErrCntLane0'])
            values.append('%s' % o['PRBSTxErrCntLane1'])
            values.append('%s' % o['PRBSTxErrCntLane2'])
            values.append('%s' % o['PRBSTxErrCntLane3'])
            r = self.swtch.getDWDMModuleClntIntf(o['ClntIntfId'], o['ModuleId'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
                values.append('%s' % o['NwLaneTributaryToClntIntfMap'])
                values.append('%s' % o['HostTxEqDfe'])
                values.append('%s' % o['HostRxSerializerTap1Gain'])
                values.append('%s' % o['RxPRBSPattern'])
                values.append('%s' % o['HostRxSerializerTap2Delay'])
                values.append('%s' % o['HostRxSerializerTap2Gain'])
                values.append('%s' % o['HostRxSerializerTap0Delay'])
                values.append('%s' % o['HostTxEqCtle'])
                values.append('%s' % o['TxPRBSPattern'])
                values.append('%s' % o['HostTxEqLfCtle'])
                values.append('%s' % o['AdminState'])
                values.append('%s' % o['RXFECDecDisable'])
                values.append('%s' % o['EnableTxPRBSChecker'])
                values.append('%s' % o['EnableHostLoopback'])
                values.append('%s' % o['HostRxSerializerTap0Gain'])
                values.append('%s' % o['TXFECDecDisable'])
                values.append('%s' % o['EnableRxPRBS'])
                values.append('%s' % o['EnableIntSerdesNWLoopback'])
            rows.append(values)
        self.tblPrintObject('DWDMModuleClntIntfState', header, rows)


    def printRouteStatStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Vrf')
            header.append('TotalRouteCount')
            header.append('ECMPRouteCount')
            header.append('V4RouteCount')
            header.append('V6RouteCount')
            header.append('PerProtocolRouteCountList')

        objs = self.swtch.getAllRouteStatStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Vrf'])
            values.append('%s' % o['TotalRouteCount'])
            values.append('%s' % o['ECMPRouteCount'])
            values.append('%s' % o['V4RouteCount'])
            values.append('%s' % o['V6RouteCount'])
            values.append('%s' % o['PerProtocolRouteCountList'])
            rows.append(values)
        self.tblPrintObject('RouteStatState', header, rows)


    def printRouteStatState(self, Vrf, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Vrf')
            header.append('TotalRouteCount')
            header.append('ECMPRouteCount')
            header.append('V4RouteCount')
            header.append('V6RouteCount')
            header.append('PerProtocolRouteCountList')

        rawobj = self.swtch.getRouteStatState(
                                              Vrf)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['Vrf'])
            values.append('%s' % o['TotalRouteCount'])
            values.append('%s' % o['ECMPRouteCount'])
            values.append('%s' % o['V4RouteCount'])
            values.append('%s' % o['V6RouteCount'])
            values.append('%s' % o['PerProtocolRouteCountList'])
            rows.append(values)
            self.tblPrintObject('RouteStatState', header, rows)

        else:
            print rawobj.content

    def printRouteDistanceStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Protocol')
            header.append('Distance')

        objs = self.swtch.getAllRouteDistanceStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Protocol'])
            values.append('%s' % o['Distance'])
            rows.append(values)
        self.tblPrintObject('RouteDistanceState', header, rows)


    def printRouteDistanceState(self, Protocol, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Protocol')
            header.append('Distance')

        rawobj = self.swtch.getRouteDistanceState(
                                                  Protocol)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['Protocol'])
            values.append('%s' % o['Distance'])
            rows.append(values)
            self.tblPrintObject('RouteDistanceState', header, rows)

        else:
            print rawobj.content

    def printLogicalIntfs(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('Type')

        objs = self.swtch.getAllLogicalIntfs()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['Type'])
            rows.append(values)
        self.tblPrintObject('LogicalIntf', header, rows)


    def printBGPv6NeighborStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('NeighborAddress')
            header.append('Description')
            header.append('PeerGroup')
            header.append('PeerType')
            header.append('SessionState')
            header.append('PeerAS')
            header.append('LocalAS')
            header.append('UpdateSource')
            header.append('RouteReflectorClusterId')
            header.append('RouteReflectorClient')
            header.append('MultiHopEnable')
            header.append('MultiHopTTL')
            header.append('ConnectRetryTime')
            header.append('HoldTime')
            header.append('KeepaliveTime')
            header.append('AddPathsRx')
            header.append('AddPathsMaxTx')
            header.append('BfdNeighborState')
            header.append('MaxPrefixes')
            header.append('MaxPrefixesThresholdPct')
            header.append('MaxPrefixesDisconnect')
            header.append('MaxPrefixesRestartTimer')
            header.append('TotalPrefixes')
            header.append('AdjRIBInFilter')
            header.append('AdjRIBOutFilter')
            header.append('Messages')
            header.append('Queues')
            header.append('SessionStateDuration')
            header.append('Disabled')

        objs = self.swtch.getAllBGPv6NeighborStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['NeighborAddress'])
            values.append('%s' % o['Description'])
            values.append('%s' % o['PeerGroup'])
            values.append('%s' % o['PeerType'])
            values.append('%s' % o['SessionState'])
            values.append('%s' % o['PeerAS'])
            values.append('%s' % o['LocalAS'])
            values.append('%s' % o['UpdateSource'])
            values.append('%s' % o['RouteReflectorClusterId'])
            values.append('%s' % o['RouteReflectorClient'])
            values.append('%s' % o['MultiHopEnable'])
            values.append('%s' % o['MultiHopTTL'])
            values.append('%s' % o['ConnectRetryTime'])
            values.append('%s' % o['HoldTime'])
            values.append('%s' % o['KeepaliveTime'])
            values.append('%s' % o['AddPathsRx'])
            values.append('%s' % o['AddPathsMaxTx'])
            values.append('%s' % o['BfdNeighborState'])
            values.append('%s' % o['MaxPrefixes'])
            values.append('%s' % o['MaxPrefixesThresholdPct'])
            values.append('%s' % o['MaxPrefixesDisconnect'])
            values.append('%s' % o['MaxPrefixesRestartTimer'])
            values.append('%s' % o['TotalPrefixes'])
            values.append('%s' % o['AdjRIBInFilter'])
            values.append('%s' % o['AdjRIBOutFilter'])
            values.append('%s' % o['Messages'])
            values.append('%s' % o['Queues'])
            values.append('%s' % o['SessionStateDuration'])
            values.append('%s' % o['Disabled'])
            rows.append(values)
        self.tblPrintObject('BGPv6NeighborState', header, rows)


    def printBGPv6NeighborState(self, IntfRef,NeighborAddress, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('NeighborAddress')
            header.append('Description')
            header.append('PeerGroup')
            header.append('PeerType')
            header.append('SessionState')
            header.append('PeerAS')
            header.append('LocalAS')
            header.append('UpdateSource')
            header.append('RouteReflectorClusterId')
            header.append('RouteReflectorClient')
            header.append('MultiHopEnable')
            header.append('MultiHopTTL')
            header.append('ConnectRetryTime')
            header.append('HoldTime')
            header.append('KeepaliveTime')
            header.append('AddPathsRx')
            header.append('AddPathsMaxTx')
            header.append('BfdNeighborState')
            header.append('MaxPrefixes')
            header.append('MaxPrefixesThresholdPct')
            header.append('MaxPrefixesDisconnect')
            header.append('MaxPrefixesRestartTimer')
            header.append('TotalPrefixes')
            header.append('AdjRIBInFilter')
            header.append('AdjRIBOutFilter')
            header.append('Messages')
            header.append('Queues')
            header.append('SessionStateDuration')
            header.append('Disabled')

        rawobj = self.swtch.getBGPv6NeighborState(
                                                  IntfRef,
                                                  NeighborAddress)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['NeighborAddress'])
            values.append('%s' % o['Description'])
            values.append('%s' % o['PeerGroup'])
            values.append('%s' % o['PeerType'])
            values.append('%s' % o['SessionState'])
            values.append('%s' % o['PeerAS'])
            values.append('%s' % o['LocalAS'])
            values.append('%s' % o['UpdateSource'])
            values.append('%s' % o['RouteReflectorClusterId'])
            values.append('%s' % o['RouteReflectorClient'])
            values.append('%s' % o['MultiHopEnable'])
            values.append('%s' % o['MultiHopTTL'])
            values.append('%s' % o['ConnectRetryTime'])
            values.append('%s' % o['HoldTime'])
            values.append('%s' % o['KeepaliveTime'])
            values.append('%s' % o['AddPathsRx'])
            values.append('%s' % o['AddPathsMaxTx'])
            values.append('%s' % o['BfdNeighborState'])
            values.append('%s' % o['MaxPrefixes'])
            values.append('%s' % o['MaxPrefixesThresholdPct'])
            values.append('%s' % o['MaxPrefixesDisconnect'])
            values.append('%s' % o['MaxPrefixesRestartTimer'])
            values.append('%s' % o['TotalPrefixes'])
            values.append('%s' % o['AdjRIBInFilter'])
            values.append('%s' % o['AdjRIBOutFilter'])
            values.append('%s' % o['Messages'])
            values.append('%s' % o['Queues'])
            values.append('%s' % o['SessionStateDuration'])
            values.append('%s' % o['Disabled'])
            rows.append(values)
            self.tblPrintObject('BGPv6NeighborState', header, rows)

        else:
            print rawobj.content

    def printCombinedBGPv6NeighborStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('NeighborAddress')
            header.append('Description')
            header.append('PeerGroup')
            header.append('PeerType')
            header.append('SessionState')
            header.append('PeerAS')
            header.append('LocalAS')
            header.append('UpdateSource')
            header.append('RouteReflectorClusterId')
            header.append('RouteReflectorClient')
            header.append('MultiHopEnable')
            header.append('MultiHopTTL')
            header.append('ConnectRetryTime')
            header.append('HoldTime')
            header.append('KeepaliveTime')
            header.append('AddPathsRx')
            header.append('AddPathsMaxTx')
            header.append('BfdNeighborState')
            header.append('MaxPrefixes')
            header.append('MaxPrefixesThresholdPct')
            header.append('MaxPrefixesDisconnect')
            header.append('MaxPrefixesRestartTimer')
            header.append('TotalPrefixes')
            header.append('AdjRIBInFilter')
            header.append('AdjRIBOutFilter')
            header.append('Messages')
            header.append('Queues')
            header.append('SessionStateDuration')
            header.append('Disabled')
            header.append('BfdEnable')
            header.append('BfdSessionParam')

        objs = self.swtch.getAllBGPv6NeighborStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['NeighborAddress'])
            values.append('%s' % o['Description'])
            values.append('%s' % o['PeerGroup'])
            values.append('%s' % o['PeerType'])
            values.append('%s' % o['SessionState'])
            values.append('%s' % o['PeerAS'])
            values.append('%s' % o['LocalAS'])
            values.append('%s' % o['UpdateSource'])
            values.append('%s' % o['RouteReflectorClusterId'])
            values.append('%s' % o['RouteReflectorClient'])
            values.append('%s' % o['MultiHopEnable'])
            values.append('%s' % o['MultiHopTTL'])
            values.append('%s' % o['ConnectRetryTime'])
            values.append('%s' % o['HoldTime'])
            values.append('%s' % o['KeepaliveTime'])
            values.append('%s' % o['AddPathsRx'])
            values.append('%s' % o['AddPathsMaxTx'])
            values.append('%s' % o['BfdNeighborState'])
            values.append('%s' % o['MaxPrefixes'])
            values.append('%s' % o['MaxPrefixesThresholdPct'])
            values.append('%s' % o['MaxPrefixesDisconnect'])
            values.append('%s' % o['MaxPrefixesRestartTimer'])
            values.append('%s' % o['TotalPrefixes'])
            values.append('%s' % o['AdjRIBInFilter'])
            values.append('%s' % o['AdjRIBOutFilter'])
            values.append('%s' % o['Messages'])
            values.append('%s' % o['Queues'])
            values.append('%s' % o['SessionStateDuration'])
            values.append('%s' % o['Disabled'])
            r = self.swtch.getBGPv6Neighbor(o['IntfRef'], o['NeighborAddress'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
                values.append('%s' % o['BfdEnable'])
                values.append('%s' % o['BfdSessionParam'])
            rows.append(values)
        self.tblPrintObject('BGPv6NeighborState', header, rows)


    def printLacpGlobals(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Vrf')
            header.append('AdminState')

        objs = self.swtch.getAllLacpGlobals()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Vrf'])
            values.append('%s' % o['AdminState'])
            rows.append(values)
        self.tblPrintObject('LacpGlobal', header, rows)


    def printMacTableEntryStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('MacAddr')
            header.append('Port')
            header.append('VlanId')

        objs = self.swtch.getAllMacTableEntryStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['MacAddr'])
            values.append('%s' % o['Port'])
            values.append('%s' % o['VlanId'])
            rows.append(values)
        self.tblPrintObject('MacTableEntryState', header, rows)


    def printMacTableEntryState(self, MacAddr, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('MacAddr')
            header.append('Port')
            header.append('VlanId')

        rawobj = self.swtch.getMacTableEntryState(
                                                  MacAddr)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['MacAddr'])
            values.append('%s' % o['Port'])
            values.append('%s' % o['VlanId'])
            rows.append(values)
            self.tblPrintObject('MacTableEntryState', header, rows)

        else:
            print rawobj.content

    def printFanSensorPMDataStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Class')
            header.append('Name')
            header.append('Data')

        objs = self.swtch.getAllFanSensorPMDataStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Class'])
            values.append('%s' % o['Name'])
            values.append('%s' % o['Data'])
            rows.append(values)
        self.tblPrintObject('FanSensorPMDataState', header, rows)


    def printFanSensorPMDataState(self, Class,Name, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Class')
            header.append('Name')
            header.append('Data')

        rawobj = self.swtch.getFanSensorPMDataState(
                                                    Class,
                                                    Name)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['Class'])
            values.append('%s' % o['Name'])
            values.append('%s' % o['Data'])
            rows.append(values)
            self.tblPrintObject('FanSensorPMDataState', header, rows)

        else:
            print rawobj.content

    def printOspfNbrEntryStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('NbrIpAddr')
            header.append('NbrAddressLessIndex')
            header.append('NbrRtrId')
            header.append('NbrOptions')
            header.append('NbrState')
            header.append('NbrEvents')
            header.append('NbrHelloSuppressed')

        objs = self.swtch.getAllOspfNbrEntryStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['NbrIpAddr'])
            values.append('%s' % o['NbrAddressLessIndex'])
            values.append('%s' % o['NbrRtrId'])
            values.append('%s' % o['NbrOptions'])
            values.append('%s' % o['NbrState'])
            values.append('%s' % o['NbrEvents'])
            values.append('%s' % o['NbrHelloSuppressed'])
            rows.append(values)
        self.tblPrintObject('OspfNbrEntryState', header, rows)


    def printOspfNbrEntryState(self, NbrIpAddr,NbrAddressLessIndex, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('NbrIpAddr')
            header.append('NbrAddressLessIndex')
            header.append('NbrRtrId')
            header.append('NbrOptions')
            header.append('NbrState')
            header.append('NbrEvents')
            header.append('NbrHelloSuppressed')

        rawobj = self.swtch.getOspfNbrEntryState(
                                                 NbrIpAddr,
                                                 NbrAddressLessIndex)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['NbrIpAddr'])
            values.append('%s' % o['NbrAddressLessIndex'])
            values.append('%s' % o['NbrRtrId'])
            values.append('%s' % o['NbrOptions'])
            values.append('%s' % o['NbrState'])
            values.append('%s' % o['NbrEvents'])
            values.append('%s' % o['NbrHelloSuppressed'])
            rows.append(values)
            self.tblPrintObject('OspfNbrEntryState', header, rows)

        else:
            print rawobj.content

    def printSystemParams(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Vrf')
            header.append('MgmtIp')
            header.append('Hostname')
            header.append('SwitchMac')
            header.append('SwVersion')
            header.append('Description')

        objs = self.swtch.getAllSystemParams()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Vrf'])
            values.append('%s' % o['MgmtIp'])
            values.append('%s' % o['Hostname'])
            values.append('%s' % o['SwitchMac'])
            values.append('%s' % o['SwVersion'])
            values.append('%s' % o['Description'])
            rows.append(values)
        self.tblPrintObject('SystemParam', header, rows)


    def printBfdGlobals(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Vrf')
            header.append('Enable')

        objs = self.swtch.getAllBfdGlobals()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Vrf'])
            values.append('%s' % o['Enable'])
            rows.append(values)
        self.tblPrintObject('BfdGlobal', header, rows)


    def printVoltageSensors(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('HigherAlarmThreshold')
            header.append('HigherWarningThreshold')
            header.append('LowerWarningThreshold')
            header.append('LowerAlarmThreshold')
            header.append('PMClassCAdminState')
            header.append('PMClassAAdminState')
            header.append('AdminState')
            header.append('PMClassBAdminState')

        objs = self.swtch.getAllVoltageSensors()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['HigherAlarmThreshold'])
            values.append('%s' % o['HigherWarningThreshold'])
            values.append('%s' % o['LowerWarningThreshold'])
            values.append('%s' % o['LowerAlarmThreshold'])
            values.append('%s' % o['PMClassCAdminState'])
            values.append('%s' % o['PMClassAAdminState'])
            values.append('%s' % o['AdminState'])
            values.append('%s' % o['PMClassBAdminState'])
            rows.append(values)
        self.tblPrintObject('VoltageSensor', header, rows)


    def printAlarmStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('EventId')
            header.append('EventName')
            header.append('SrcObjName')
            header.append('OwnerName')
            header.append('OwnerId')
            header.append('Severity')
            header.append('Description')
            header.append('OccuranceTime')
            header.append('SrcObjKey')
            header.append('SrcObjUUID')
            header.append('ResolutionTime')
            header.append('ResolutionReason')

        objs = self.swtch.getAllAlarmStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['EventId'])
            values.append('%s' % o['EventName'])
            values.append('%s' % o['SrcObjName'])
            values.append('%s' % o['OwnerName'])
            values.append('%s' % o['OwnerId'])
            values.append('%s' % o['Severity'])
            values.append('%s' % o['Description'])
            values.append('%s' % o['OccuranceTime'])
            values.append('%s' % o['SrcObjKey'])
            values.append('%s' % o['SrcObjUUID'])
            values.append('%s' % o['ResolutionTime'])
            values.append('%s' % o['ResolutionReason'])
            rows.append(values)
        self.tblPrintObject('AlarmState', header, rows)


    def printAlarmState(self, EventId,EventName,SrcObjName,OwnerName,OwnerId, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('EventId')
            header.append('EventName')
            header.append('SrcObjName')
            header.append('OwnerName')
            header.append('OwnerId')
            header.append('Severity')
            header.append('Description')
            header.append('OccuranceTime')
            header.append('SrcObjKey')
            header.append('SrcObjUUID')
            header.append('ResolutionTime')
            header.append('ResolutionReason')

        rawobj = self.swtch.getAlarmState(
                                          EventId,
                                          EventName,
                                          SrcObjName,
                                          OwnerName,
                                          OwnerId)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['EventId'])
            values.append('%s' % o['EventName'])
            values.append('%s' % o['SrcObjName'])
            values.append('%s' % o['OwnerName'])
            values.append('%s' % o['OwnerId'])
            values.append('%s' % o['Severity'])
            values.append('%s' % o['Description'])
            values.append('%s' % o['OccuranceTime'])
            values.append('%s' % o['SrcObjKey'])
            values.append('%s' % o['SrcObjUUID'])
            values.append('%s' % o['ResolutionTime'])
            values.append('%s' % o['ResolutionReason'])
            rows.append(values)
            self.tblPrintObject('AlarmState', header, rows)

        else:
            print rawobj.content

    def printQsfpPMDataStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Resource')
            header.append('Class')
            header.append('QsfpId')
            header.append('Data')

        objs = self.swtch.getAllQsfpPMDataStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Resource'])
            values.append('%s' % o['Class'])
            values.append('%s' % o['QsfpId'])
            values.append('%s' % o['Data'])
            rows.append(values)
        self.tblPrintObject('QsfpPMDataState', header, rows)


    def printQsfpPMDataState(self, Resource,Class,QsfpId, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Resource')
            header.append('Class')
            header.append('QsfpId')
            header.append('Data')

        rawobj = self.swtch.getQsfpPMDataState(
                                               Resource,
                                               Class,
                                               QsfpId)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['Resource'])
            values.append('%s' % o['Class'])
            values.append('%s' % o['QsfpId'])
            values.append('%s' % o['Data'])
            rows.append(values)
            self.tblPrintObject('QsfpPMDataState', header, rows)

        else:
            print rawobj.content

    def printAclRuleStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('RuleName')
            header.append('AclType')
            header.append('IntfList')
            header.append('HwPresence')
            header.append('HitCount')

        objs = self.swtch.getAllAclRuleStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['RuleName'])
            values.append('%s' % o['AclType'])
            values.append('%s' % o['IntfList'])
            values.append('%s' % o['HwPresence'])
            values.append('%s' % o['HitCount'])
            rows.append(values)
        self.tblPrintObject('AclRuleState', header, rows)


    def printAclRuleState(self, RuleName, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('RuleName')
            header.append('AclType')
            header.append('IntfList')
            header.append('HwPresence')
            header.append('HitCount')

        rawobj = self.swtch.getAclRuleState(
                                            RuleName)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['RuleName'])
            values.append('%s' % o['AclType'])
            values.append('%s' % o['IntfList'])
            values.append('%s' % o['HwPresence'])
            values.append('%s' % o['HitCount'])
            rows.append(values)
            self.tblPrintObject('AclRuleState', header, rows)

        else:
            print rawobj.content

    def printCombinedAclRuleStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('RuleName')
            header.append('AclType')
            header.append('IntfList')
            header.append('HwPresence')
            header.append('HitCount')
            header.append('SourceMac')
            header.append('DestMac')
            header.append('SourceIp')
            header.append('DestIp')
            header.append('SourceMask')
            header.append('DestMask')
            header.append('Proto')
            header.append('SrcPort')
            header.append('L4DstPort')
            header.append('L4MinPort')
            header.append('L4SrcPort')
            header.append('Action')
            header.append('L4MaxPort')
            header.append('DstPort')
            header.append('L4PortMatch')

        objs = self.swtch.getAllAclRuleStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['RuleName'])
            values.append('%s' % o['AclType'])
            values.append('%s' % o['IntfList'])
            values.append('%s' % o['HwPresence'])
            values.append('%s' % o['HitCount'])
            r = self.swtch.getAclRule(o['RuleName'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
                values.append('%s' % o['SourceMac'])
                values.append('%s' % o['DestMac'])
                values.append('%s' % o['SourceIp'])
                values.append('%s' % o['DestIp'])
                values.append('%s' % o['SourceMask'])
                values.append('%s' % o['DestMask'])
                values.append('%s' % o['Proto'])
                values.append('%s' % o['SrcPort'])
                values.append('%s' % o['L4DstPort'])
                values.append('%s' % o['L4MinPort'])
                values.append('%s' % o['L4SrcPort'])
                values.append('%s' % o['Action'])
                values.append('%s' % o['L4MaxPort'])
                values.append('%s' % o['DstPort'])
                values.append('%s' % o['L4PortMatch'])
            rows.append(values)
        self.tblPrintObject('AclRuleState', header, rows)


    def printBGPPolicyStmts(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('MatchConditions')
            header.append('Conditions')
            header.append('Actions')

        objs = self.swtch.getAllBGPPolicyStmts()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['MatchConditions'])
            values.append('%s' % o['Conditions'])
            values.append('%s' % o['Actions'])
            rows.append(values)
        self.tblPrintObject('BGPPolicyStmt', header, rows)


    def printAsicGlobalPMs(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Resource')
            header.append('ModuleId')
            header.append('PMClassBEnable')
            header.append('HighWarnThreshold')
            header.append('LowAlarmThreshold')
            header.append('PMClassCEnable')
            header.append('PMClassAEnable')
            header.append('LowWarnThreshold')
            header.append('HighAlarmThreshold')

        objs = self.swtch.getAllAsicGlobalPMs()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Resource'])
            values.append('%s' % o['ModuleId'])
            values.append('%s' % o['PMClassBEnable'])
            values.append('%s' % o['HighWarnThreshold'])
            values.append('%s' % o['LowAlarmThreshold'])
            values.append('%s' % o['PMClassCEnable'])
            values.append('%s' % o['PMClassAEnable'])
            values.append('%s' % o['LowWarnThreshold'])
            values.append('%s' % o['HighAlarmThreshold'])
            rows.append(values)
        self.tblPrintObject('AsicGlobalPM', header, rows)


    def printIPv4RouteHwStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('DestinationNw')
            header.append('NextHopIps')
            header.append('RouteCreatedTime')
            header.append('RouteUpdatedTime')

        objs = self.swtch.getAllIPv4RouteHwStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['DestinationNw'])
            values.append('%s' % o['NextHopIps'])
            values.append('%s' % o['RouteCreatedTime'])
            values.append('%s' % o['RouteUpdatedTime'])
            rows.append(values)
        self.tblPrintObject('IPv4RouteHwState', header, rows)


    def printIPv4RouteHwState(self, DestinationNw, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('DestinationNw')
            header.append('NextHopIps')
            header.append('RouteCreatedTime')
            header.append('RouteUpdatedTime')

        rawobj = self.swtch.getIPv4RouteHwState(
                                                DestinationNw)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['DestinationNw'])
            values.append('%s' % o['NextHopIps'])
            values.append('%s' % o['RouteCreatedTime'])
            values.append('%s' % o['RouteUpdatedTime'])
            rows.append(values)
            self.tblPrintObject('IPv4RouteHwState', header, rows)

        else:
            print rawobj.content

    def printArpGlobals(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Vrf')
            header.append('Timeout')

        objs = self.swtch.getAllArpGlobals()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Vrf'])
            values.append('%s' % o['Timeout'])
            rows.append(values)
        self.tblPrintObject('ArpGlobal', header, rows)


    def printBGPv4PeerGroups(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('PeerAS')
            header.append('LocalAS')
            header.append('UpdateSource')
            header.append('AuthPassword')
            header.append('Description')
            header.append('AdjRIBInFilter')
            header.append('AdjRIBOutFilter')
            header.append('MaxPrefixesRestartTimer')
            header.append('MultiHopEnable')
            header.append('MaxPrefixesDisconnect')
            header.append('MultiHopTTL')
            header.append('KeepaliveTime')
            header.append('RouteReflectorClusterId')
            header.append('MaxPrefixes')
            header.append('AddPathsMaxTx')
            header.append('AddPathsRx')
            header.append('RouteReflectorClient')
            header.append('MaxPrefixesThresholdPct')
            header.append('HoldTime')
            header.append('ConnectRetryTime')

        objs = self.swtch.getAllBGPv4PeerGroups()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['PeerAS'])
            values.append('%s' % o['LocalAS'])
            values.append('%s' % o['UpdateSource'])
            values.append('%s' % o['AuthPassword'])
            values.append('%s' % o['Description'])
            values.append('%s' % o['AdjRIBInFilter'])
            values.append('%s' % o['AdjRIBOutFilter'])
            values.append('%s' % o['MaxPrefixesRestartTimer'])
            values.append('%s' % o['MultiHopEnable'])
            values.append('%s' % o['MaxPrefixesDisconnect'])
            values.append('%s' % o['MultiHopTTL'])
            values.append('%s' % o['KeepaliveTime'])
            values.append('%s' % o['RouteReflectorClusterId'])
            values.append('%s' % o['MaxPrefixes'])
            values.append('%s' % o['AddPathsMaxTx'])
            values.append('%s' % o['AddPathsRx'])
            values.append('%s' % o['RouteReflectorClient'])
            values.append('%s' % o['MaxPrefixesThresholdPct'])
            values.append('%s' % o['HoldTime'])
            values.append('%s' % o['ConnectRetryTime'])
            rows.append(values)
        var = self.tblPrintObject('BGPv4PeerGroup', header, rows)
        return var

    def printIPv4RouteStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('DestinationNw')
            header.append('Protocol')
            header.append('IsNetworkReachable')
            header.append('RouteCreatedTime')
            header.append('RouteUpdatedTime')
            header.append('NextHopList')
            header.append('PolicyList')
            header.append('NextBestRoute')

        objs = self.swtch.getAllIPv4RouteStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['DestinationNw'])
            values.append('%s' % o['Protocol'])
            values.append('%s' % o['IsNetworkReachable'])
            values.append('%s' % o['RouteCreatedTime'])
            values.append('%s' % o['RouteUpdatedTime'])
            values.append('%s' % o['NextHopList'])
            values.append('%s' % o['PolicyList'])
            values.append('%s' % o['NextBestRoute'])
            rows.append(values)
        self.tblPrintObject('IPv4RouteState', header, rows)


    def printIPv4RouteState(self, DestinationNw, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('DestinationNw')
            header.append('Protocol')
            header.append('IsNetworkReachable')
            header.append('RouteCreatedTime')
            header.append('RouteUpdatedTime')
            header.append('NextHopList')
            header.append('PolicyList')
            header.append('NextBestRoute')

        rawobj = self.swtch.getIPv4RouteState(
                                              DestinationNw)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['DestinationNw'])
            values.append('%s' % o['Protocol'])
            values.append('%s' % o['IsNetworkReachable'])
            values.append('%s' % o['RouteCreatedTime'])
            values.append('%s' % o['RouteUpdatedTime'])
            values.append('%s' % o['NextHopList'])
            values.append('%s' % o['PolicyList'])
            values.append('%s' % o['NextBestRoute'])
            rows.append(values)
            var = self.tblPrintObject('IPv4RouteState', header, rows)
            return var
        else:
            print rawobj.content

    def printCombinedIPv4RouteStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('DestinationNw')
            header.append('Protocol')
            header.append('IsNetworkReachable')
            header.append('RouteCreatedTime')
            header.append('RouteUpdatedTime')
            header.append('NextHopList')
            header.append('PolicyList')
            header.append('NextBestRoute')
            header.append('NetworkMask')
            header.append('NextHop')
            header.append('NullRoute')
            header.append('Cost')

        objs = self.swtch.getAllIPv4RouteStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['DestinationNw'])
            values.append('%s' % o['Protocol'])
            values.append('%s' % o['IsNetworkReachable'])
            values.append('%s' % o['RouteCreatedTime'])
            values.append('%s' % o['RouteUpdatedTime'])
            values.append('%s' % o['NextHopList'])
            values.append('%s' % o['PolicyList'])
            values.append('%s' % o['NextBestRoute'])
            r = self.swtch.getIPv4Route(o['DestinationNw'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
                values.append('%s' % o['NetworkMask'])
                values.append('%s' % o['NextHop'])
                values.append('%s' % o['NullRoute'])
                values.append('%s' % o['Cost'])
            rows.append(values)
        self.tblPrintObject('IPv4RouteState', header, rows)


    def printPowerConverterSensorStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('CurrentPower')

        objs = self.swtch.getAllPowerConverterSensorStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['CurrentPower'])
            rows.append(values)
        self.tblPrintObject('PowerConverterSensorState', header, rows)


    def printPowerConverterSensorState(self, Name, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('CurrentPower')

        rawobj = self.swtch.getPowerConverterSensorState(
                                                         Name)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['CurrentPower'])
            rows.append(values)
            self.tblPrintObject('PowerConverterSensorState', header, rows)

        else:
            print rawobj.content

    def printCombinedPowerConverterSensorStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('CurrentPower')
            header.append('HigherAlarmThreshold')
            header.append('HigherWarningThreshold')
            header.append('LowerWarningThreshold')
            header.append('LowerAlarmThreshold')
            header.append('PMClassCAdminState')
            header.append('PMClassAAdminState')
            header.append('AdminState')
            header.append('PMClassBAdminState')

        objs = self.swtch.getAllPowerConverterSensorStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['CurrentPower'])
            r = self.swtch.getPowerConverterSensor(o['Name'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
                values.append('%s' % o['HigherAlarmThreshold'])
                values.append('%s' % o['HigherWarningThreshold'])
                values.append('%s' % o['LowerWarningThreshold'])
                values.append('%s' % o['LowerAlarmThreshold'])
                values.append('%s' % o['PMClassCAdminState'])
                values.append('%s' % o['PMClassAAdminState'])
                values.append('%s' % o['AdminState'])
                values.append('%s' % o['PMClassBAdminState'])
            rows.append(values)
        self.tblPrintObject('PowerConverterSensorState', header, rows)


    def printQsfpStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('QsfpId')
            header.append('Present')
            header.append('VendorName')
            header.append('VendorOUI')
            header.append('VendorPartNumber')
            header.append('VendorRevision')
            header.append('VendorSerialNumber')
            header.append('DataCode')
            header.append('Temperature')
            header.append('Voltage')
            header.append('CurrBER')
            header.append('AccBER')
            header.append('MinBER')
            header.append('MaxBER')
            header.append('UDF0')
            header.append('UDF1')
            header.append('UDF2')
            header.append('UDF3')

        objs = self.swtch.getAllQsfpStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['QsfpId'])
            values.append('%s' % o['Present'])
            values.append('%s' % o['VendorName'])
            values.append('%s' % o['VendorOUI'])
            values.append('%s' % o['VendorPartNumber'])
            values.append('%s' % o['VendorRevision'])
            values.append('%s' % o['VendorSerialNumber'])
            values.append('%s' % o['DataCode'])
            values.append('%s' % o['Temperature'])
            values.append('%s' % o['Voltage'])
            values.append('%s' % o['CurrBER'])
            values.append('%s' % o['AccBER'])
            values.append('%s' % o['MinBER'])
            values.append('%s' % o['MaxBER'])
            values.append('%s' % o['UDF0'])
            values.append('%s' % o['UDF1'])
            values.append('%s' % o['UDF2'])
            values.append('%s' % o['UDF3'])
            rows.append(values)
        self.tblPrintObject('QsfpState', header, rows)


    def printQsfpState(self, QsfpId, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('QsfpId')
            header.append('Present')
            header.append('VendorName')
            header.append('VendorOUI')
            header.append('VendorPartNumber')
            header.append('VendorRevision')
            header.append('VendorSerialNumber')
            header.append('DataCode')
            header.append('Temperature')
            header.append('Voltage')
            header.append('CurrBER')
            header.append('AccBER')
            header.append('MinBER')
            header.append('MaxBER')
            header.append('UDF0')
            header.append('UDF1')
            header.append('UDF2')
            header.append('UDF3')

        rawobj = self.swtch.getQsfpState(
                                         QsfpId)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['QsfpId'])
            values.append('%s' % o['Present'])
            values.append('%s' % o['VendorName'])
            values.append('%s' % o['VendorOUI'])
            values.append('%s' % o['VendorPartNumber'])
            values.append('%s' % o['VendorRevision'])
            values.append('%s' % o['VendorSerialNumber'])
            values.append('%s' % o['DataCode'])
            values.append('%s' % o['Temperature'])
            values.append('%s' % o['Voltage'])
            values.append('%s' % o['CurrBER'])
            values.append('%s' % o['AccBER'])
            values.append('%s' % o['MinBER'])
            values.append('%s' % o['MaxBER'])
            values.append('%s' % o['UDF0'])
            values.append('%s' % o['UDF1'])
            values.append('%s' % o['UDF2'])
            values.append('%s' % o['UDF3'])
            rows.append(values)
            self.tblPrintObject('QsfpState', header, rows)

        else:
            print rawobj.content

    def printCombinedQsfpStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('QsfpId')
            header.append('Present')
            header.append('VendorName')
            header.append('VendorOUI')
            header.append('VendorPartNumber')
            header.append('VendorRevision')
            header.append('VendorSerialNumber')
            header.append('DataCode')
            header.append('Temperature')
            header.append('Voltage')
            header.append('CurrBER')
            header.append('AccBER')
            header.append('MinBER')
            header.append('MaxBER')
            header.append('UDF0')
            header.append('UDF1')
            header.append('UDF2')
            header.append('UDF3')
            header.append('HigherAlarmTemperature')
            header.append('HigherAlarmVoltage')
            header.append('HigherWarningTemperature')
            header.append('HigherWarningVoltage')
            header.append('LowerAlarmTemperature')
            header.append('LowerAlarmVoltage')
            header.append('LowerWarningTemperature')
            header.append('LowerWarningVoltage')
            header.append('PMClassBAdminState')
            header.append('PMClassCAdminState')
            header.append('PMClassAAdminState')
            header.append('AdminState')

        objs = self.swtch.getAllQsfpStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['QsfpId'])
            values.append('%s' % o['Present'])
            values.append('%s' % o['VendorName'])
            values.append('%s' % o['VendorOUI'])
            values.append('%s' % o['VendorPartNumber'])
            values.append('%s' % o['VendorRevision'])
            values.append('%s' % o['VendorSerialNumber'])
            values.append('%s' % o['DataCode'])
            values.append('%s' % o['Temperature'])
            values.append('%s' % o['Voltage'])
            values.append('%s' % o['CurrBER'])
            values.append('%s' % o['AccBER'])
            values.append('%s' % o['MinBER'])
            values.append('%s' % o['MaxBER'])
            values.append('%s' % o['UDF0'])
            values.append('%s' % o['UDF1'])
            values.append('%s' % o['UDF2'])
            values.append('%s' % o['UDF3'])
            r = self.swtch.getQsfp(o['QsfpId'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
                values.append('%s' % o['HigherAlarmTemperature'])
                values.append('%s' % o['HigherAlarmVoltage'])
                values.append('%s' % o['HigherWarningTemperature'])
                values.append('%s' % o['HigherWarningVoltage'])
                values.append('%s' % o['LowerAlarmTemperature'])
                values.append('%s' % o['LowerAlarmVoltage'])
                values.append('%s' % o['LowerWarningTemperature'])
                values.append('%s' % o['LowerWarningVoltage'])
                values.append('%s' % o['PMClassBAdminState'])
                values.append('%s' % o['PMClassCAdminState'])
                values.append('%s' % o['PMClassAAdminState'])
                values.append('%s' % o['AdminState'])
            rows.append(values)
        self.tblPrintObject('QsfpState', header, rows)


    def printBfdGlobalStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Vrf')
            header.append('Enable')
            header.append('NumTotalSessions')
            header.append('NumUpSessions')
            header.append('NumDownSessions')
            header.append('NumAdminDownSessions')

        objs = self.swtch.getAllBfdGlobalStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Vrf'])
            values.append('%s' % o['Enable'])
            values.append('%s' % o['NumTotalSessions'])
            values.append('%s' % o['NumUpSessions'])
            values.append('%s' % o['NumDownSessions'])
            values.append('%s' % o['NumAdminDownSessions'])
            rows.append(values)
        self.tblPrintObject('BfdGlobalState', header, rows)


    def printBfdGlobalState(self, Vrf, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Vrf')
            header.append('Enable')
            header.append('NumTotalSessions')
            header.append('NumUpSessions')
            header.append('NumDownSessions')
            header.append('NumAdminDownSessions')

        rawobj = self.swtch.getBfdGlobalState(
                                              Vrf)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['Vrf'])
            values.append('%s' % o['Enable'])
            values.append('%s' % o['NumTotalSessions'])
            values.append('%s' % o['NumUpSessions'])
            values.append('%s' % o['NumDownSessions'])
            values.append('%s' % o['NumAdminDownSessions'])
            rows.append(values)
            self.tblPrintObject('BfdGlobalState', header, rows)

        else:
            print rawobj.content

    def printCombinedBfdGlobalStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Vrf')
            header.append('Enable')
            header.append('NumTotalSessions')
            header.append('NumUpSessions')
            header.append('NumDownSessions')
            header.append('NumAdminDownSessions')

        objs = self.swtch.getAllBfdGlobalStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Vrf'])
            values.append('%s' % o['Enable'])
            values.append('%s' % o['NumTotalSessions'])
            values.append('%s' % o['NumUpSessions'])
            values.append('%s' % o['NumDownSessions'])
            values.append('%s' % o['NumAdminDownSessions'])
            r = self.swtch.getBfdGlobal(o['Vrf'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
            rows.append(values)
        self.tblPrintObject('BfdGlobalState', header, rows)


    def printQsfpChannelStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('ChannelNum')
            header.append('QsfpId')
            header.append('Present')
            header.append('RXPower')
            header.append('TXPower')
            header.append('TXBias')

        objs = self.swtch.getAllQsfpChannelStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['ChannelNum'])
            values.append('%s' % o['QsfpId'])
            values.append('%s' % o['Present'])
            values.append('%s' % o['RXPower'])
            values.append('%s' % o['TXPower'])
            values.append('%s' % o['TXBias'])
            rows.append(values)
        self.tblPrintObject('QsfpChannelState', header, rows)


    def printQsfpChannelState(self, ChannelNum,QsfpId, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('ChannelNum')
            header.append('QsfpId')
            header.append('Present')
            header.append('RXPower')
            header.append('TXPower')
            header.append('TXBias')

        rawobj = self.swtch.getQsfpChannelState(
                                                ChannelNum,
                                                QsfpId)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['ChannelNum'])
            values.append('%s' % o['QsfpId'])
            values.append('%s' % o['Present'])
            values.append('%s' % o['RXPower'])
            values.append('%s' % o['TXPower'])
            values.append('%s' % o['TXBias'])
            rows.append(values)
            self.tblPrintObject('QsfpChannelState', header, rows)

        else:
            print rawobj.content

    def printCombinedQsfpChannelStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('ChannelNum')
            header.append('QsfpId')
            header.append('Present')
            header.append('RXPower')
            header.append('TXPower')
            header.append('TXBias')
            header.append('HigherAlarmRXPower')
            header.append('HigherAlarmTXPower')
            header.append('HigherAlarmTXBias')
            header.append('HigherWarningRXPower')
            header.append('HigherWarningTXPower')
            header.append('HigherWarningTXBias')
            header.append('LowerAlarmRXPower')
            header.append('LowerAlarmTXPower')
            header.append('LowerAlarmTXBias')
            header.append('LowerWarningRXPower')
            header.append('LowerWarningTXPower')
            header.append('LowerWarningTXBias')
            header.append('PMClassBAdminState')
            header.append('PMClassCAdminState')
            header.append('PMClassAAdminState')
            header.append('AdminState')

        objs = self.swtch.getAllQsfpChannelStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['ChannelNum'])
            values.append('%s' % o['QsfpId'])
            values.append('%s' % o['Present'])
            values.append('%s' % o['RXPower'])
            values.append('%s' % o['TXPower'])
            values.append('%s' % o['TXBias'])
            r = self.swtch.getQsfpChannel(o['ChannelNum'], o['QsfpId'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
                values.append('%s' % o['HigherAlarmRXPower'])
                values.append('%s' % o['HigherAlarmTXPower'])
                values.append('%s' % o['HigherAlarmTXBias'])
                values.append('%s' % o['HigherWarningRXPower'])
                values.append('%s' % o['HigherWarningTXPower'])
                values.append('%s' % o['HigherWarningTXBias'])
                values.append('%s' % o['LowerAlarmRXPower'])
                values.append('%s' % o['LowerAlarmTXPower'])
                values.append('%s' % o['LowerAlarmTXBias'])
                values.append('%s' % o['LowerWarningRXPower'])
                values.append('%s' % o['LowerWarningTXPower'])
                values.append('%s' % o['LowerWarningTXBias'])
                values.append('%s' % o['PMClassBAdminState'])
                values.append('%s' % o['PMClassCAdminState'])
                values.append('%s' % o['PMClassAAdminState'])
                values.append('%s' % o['AdminState'])
            rows.append(values)
        self.tblPrintObject('QsfpChannelState', header, rows)


    def printFanStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('FanId')
            header.append('OperMode')
            header.append('OperSpeed')
            header.append('OperDirection')
            header.append('Status')
            header.append('Model')
            header.append('SerialNum')
            header.append('LedId')

        objs = self.swtch.getAllFanStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['FanId'])
            values.append('%s' % o['OperMode'])
            values.append('%s' % o['OperSpeed'])
            values.append('%s' % o['OperDirection'])
            values.append('%s' % o['Status'])
            values.append('%s' % o['Model'])
            values.append('%s' % o['SerialNum'])
            values.append('%s' % o['LedId'])
            rows.append(values)
        self.tblPrintObject('FanState', header, rows)


    def printFanState(self, FanId, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('FanId')
            header.append('OperMode')
            header.append('OperSpeed')
            header.append('OperDirection')
            header.append('Status')
            header.append('Model')
            header.append('SerialNum')
            header.append('LedId')

        rawobj = self.swtch.getFanState(
                                        FanId)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['FanId'])
            values.append('%s' % o['OperMode'])
            values.append('%s' % o['OperSpeed'])
            values.append('%s' % o['OperDirection'])
            values.append('%s' % o['Status'])
            values.append('%s' % o['Model'])
            values.append('%s' % o['SerialNum'])
            values.append('%s' % o['LedId'])
            rows.append(values)
            self.tblPrintObject('FanState', header, rows)

        else:
            print rawobj.content

    def printCombinedFanStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('FanId')
            header.append('OperMode')
            header.append('OperSpeed')
            header.append('OperDirection')
            header.append('Status')
            header.append('Model')
            header.append('SerialNum')
            header.append('LedId')
            header.append('AdminState')
            header.append('AdminSpeed')

        objs = self.swtch.getAllFanStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['FanId'])
            values.append('%s' % o['OperMode'])
            values.append('%s' % o['OperSpeed'])
            values.append('%s' % o['OperDirection'])
            values.append('%s' % o['Status'])
            values.append('%s' % o['Model'])
            values.append('%s' % o['SerialNum'])
            values.append('%s' % o['LedId'])
            r = self.swtch.getFan(o['FanId'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
                values.append('%s' % o['AdminState'])
                values.append('%s' % o['AdminSpeed'])
            rows.append(values)
        self.tblPrintObject('FanState', header, rows)


    def printBGPGlobalStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('RouterId')
            header.append('AS')
            header.append('UseMultiplePaths')
            header.append('EBGPMaxPaths')
            header.append('EBGPAllowMultipleAS')
            header.append('IBGPMaxPaths')
            header.append('TotalPaths')
            header.append('Totalv4Prefixes')
            header.append('Totalv6Prefixes')

        objs = self.swtch.getAllBGPGlobalStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['RouterId'])
            values.append('%s' % o['AS'])
            values.append('%s' % o['UseMultiplePaths'])
            values.append('%s' % o['EBGPMaxPaths'])
            values.append('%s' % o['EBGPAllowMultipleAS'])
            values.append('%s' % o['IBGPMaxPaths'])
            values.append('%s' % o['TotalPaths'])
            values.append('%s' % o['Totalv4Prefixes'])
            values.append('%s' % o['Totalv6Prefixes'])
            rows.append(values)
        self.tblPrintObject('BGPGlobalState', header, rows)


    def printBGPGlobalState(self, RouterId, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('RouterId')
            header.append('AS')
            header.append('UseMultiplePaths')
            header.append('EBGPMaxPaths')
            header.append('EBGPAllowMultipleAS')
            header.append('IBGPMaxPaths')
            header.append('TotalPaths')
            header.append('Totalv4Prefixes')
            header.append('Totalv6Prefixes')

        rawobj = self.swtch.getBGPGlobalState(
                                              RouterId)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['RouterId'])
            values.append('%s' % o['AS'])
            values.append('%s' % o['UseMultiplePaths'])
            values.append('%s' % o['EBGPMaxPaths'])
            values.append('%s' % o['EBGPAllowMultipleAS'])
            values.append('%s' % o['IBGPMaxPaths'])
            values.append('%s' % o['TotalPaths'])
            values.append('%s' % o['Totalv4Prefixes'])
            values.append('%s' % o['Totalv6Prefixes'])
            rows.append(values)
            self.tblPrintObject('BGPGlobalState', header, rows)

        else:
            print rawobj.content

    def printCombinedBGPGlobalStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('RouterId')
            header.append('AS')
            header.append('UseMultiplePaths')
            header.append('EBGPMaxPaths')
            header.append('EBGPAllowMultipleAS')
            header.append('IBGPMaxPaths')
            header.append('TotalPaths')
            header.append('Totalv4Prefixes')
            header.append('Totalv6Prefixes')
            header.append('Vrf')
            header.append('ASNum')
            header.append('Redistribution')

        objs = self.swtch.getAllBGPGlobalStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['RouterId'])
            values.append('%s' % o['AS'])
            values.append('%s' % o['UseMultiplePaths'])
            values.append('%s' % o['EBGPMaxPaths'])
            values.append('%s' % o['EBGPAllowMultipleAS'])
            values.append('%s' % o['IBGPMaxPaths'])
            values.append('%s' % o['TotalPaths'])
            values.append('%s' % o['Totalv4Prefixes'])
            values.append('%s' % o['Totalv6Prefixes'])
            r = self.swtch.getBGPGlobal(o['RouterId'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
                values.append('%s' % o['Vrf'])
                values.append('%s' % o['ASNum'])
                values.append('%s' % o['Redistribution'])
            rows.append(values)
        self.tblPrintObject('BGPGlobalState', header, rows)


    def printBfdSessionStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IpAddr')
            header.append('SessionId')
            header.append('ParamName')
            header.append('IntfRef')
            header.append('InterfaceSpecific')
            header.append('PerLinkSession')
            header.append('LocalMacAddr')
            header.append('RemoteMacAddr')
            header.append('RegisteredProtocols')
            header.append('SessionState')
            header.append('RemoteSessionState')
            header.append('LocalDiscriminator')
            header.append('RemoteDiscriminator')
            header.append('LocalDiagType')
            header.append('DesiredMinTxInterval')
            header.append('RequiredMinRxInterval')
            header.append('RemoteMinRxInterval')
            header.append('DetectionMultiplier')
            header.append('RemoteDetectionMultiplier')
            header.append('DemandMode')
            header.append('RemoteDemandMode')
            header.append('AuthSeqKnown')
            header.append('AuthType')
            header.append('ReceivedAuthSeq')
            header.append('SentAuthSeq')
            header.append('NumTxPackets')
            header.append('NumRxPackets')
            header.append('ToDownCount')
            header.append('ToUpCount')
            header.append('UpDuration')

        objs = self.swtch.getAllBfdSessionStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IpAddr'])
            values.append('%s' % o['SessionId'])
            values.append('%s' % o['ParamName'])
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['InterfaceSpecific'])
            values.append('%s' % o['PerLinkSession'])
            values.append('%s' % o['LocalMacAddr'])
            values.append('%s' % o['RemoteMacAddr'])
            values.append('%s' % o['RegisteredProtocols'])
            values.append('%s' % o['SessionState'])
            values.append('%s' % o['RemoteSessionState'])
            values.append('%s' % o['LocalDiscriminator'])
            values.append('%s' % o['RemoteDiscriminator'])
            values.append('%s' % o['LocalDiagType'])
            values.append('%s' % o['DesiredMinTxInterval'])
            values.append('%s' % o['RequiredMinRxInterval'])
            values.append('%s' % o['RemoteMinRxInterval'])
            values.append('%s' % o['DetectionMultiplier'])
            values.append('%s' % o['RemoteDetectionMultiplier'])
            values.append('%s' % o['DemandMode'])
            values.append('%s' % o['RemoteDemandMode'])
            values.append('%s' % o['AuthSeqKnown'])
            values.append('%s' % o['AuthType'])
            values.append('%s' % o['ReceivedAuthSeq'])
            values.append('%s' % o['SentAuthSeq'])
            values.append('%s' % o['NumTxPackets'])
            values.append('%s' % o['NumRxPackets'])
            values.append('%s' % o['ToDownCount'])
            values.append('%s' % o['ToUpCount'])
            values.append('%s' % o['UpDuration'])
            rows.append(values)
        self.tblPrintObject('BfdSessionState', header, rows)


    def printBfdSessionState(self, IpAddr, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IpAddr')
            header.append('SessionId')
            header.append('ParamName')
            header.append('IntfRef')
            header.append('InterfaceSpecific')
            header.append('PerLinkSession')
            header.append('LocalMacAddr')
            header.append('RemoteMacAddr')
            header.append('RegisteredProtocols')
            header.append('SessionState')
            header.append('RemoteSessionState')
            header.append('LocalDiscriminator')
            header.append('RemoteDiscriminator')
            header.append('LocalDiagType')
            header.append('DesiredMinTxInterval')
            header.append('RequiredMinRxInterval')
            header.append('RemoteMinRxInterval')
            header.append('DetectionMultiplier')
            header.append('RemoteDetectionMultiplier')
            header.append('DemandMode')
            header.append('RemoteDemandMode')
            header.append('AuthSeqKnown')
            header.append('AuthType')
            header.append('ReceivedAuthSeq')
            header.append('SentAuthSeq')
            header.append('NumTxPackets')
            header.append('NumRxPackets')
            header.append('ToDownCount')
            header.append('ToUpCount')
            header.append('UpDuration')

        rawobj = self.swtch.getBfdSessionState(
                                               IpAddr)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['IpAddr'])
            values.append('%s' % o['SessionId'])
            values.append('%s' % o['ParamName'])
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['InterfaceSpecific'])
            values.append('%s' % o['PerLinkSession'])
            values.append('%s' % o['LocalMacAddr'])
            values.append('%s' % o['RemoteMacAddr'])
            values.append('%s' % o['RegisteredProtocols'])
            values.append('%s' % o['SessionState'])
            values.append('%s' % o['RemoteSessionState'])
            values.append('%s' % o['LocalDiscriminator'])
            values.append('%s' % o['RemoteDiscriminator'])
            values.append('%s' % o['LocalDiagType'])
            values.append('%s' % o['DesiredMinTxInterval'])
            values.append('%s' % o['RequiredMinRxInterval'])
            values.append('%s' % o['RemoteMinRxInterval'])
            values.append('%s' % o['DetectionMultiplier'])
            values.append('%s' % o['RemoteDetectionMultiplier'])
            values.append('%s' % o['DemandMode'])
            values.append('%s' % o['RemoteDemandMode'])
            values.append('%s' % o['AuthSeqKnown'])
            values.append('%s' % o['AuthType'])
            values.append('%s' % o['ReceivedAuthSeq'])
            values.append('%s' % o['SentAuthSeq'])
            values.append('%s' % o['NumTxPackets'])
            values.append('%s' % o['NumRxPackets'])
            values.append('%s' % o['ToDownCount'])
            values.append('%s' % o['ToUpCount'])
            values.append('%s' % o['UpDuration'])
            rows.append(values)
            self.tblPrintObject('BfdSessionState', header, rows)

        else:
            print rawobj.content

    def printCombinedBfdSessionStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IpAddr')
            header.append('SessionId')
            header.append('ParamName')
            header.append('IntfRef')
            header.append('InterfaceSpecific')
            header.append('PerLinkSession')
            header.append('LocalMacAddr')
            header.append('RemoteMacAddr')
            header.append('RegisteredProtocols')
            header.append('SessionState')
            header.append('RemoteSessionState')
            header.append('LocalDiscriminator')
            header.append('RemoteDiscriminator')
            header.append('LocalDiagType')
            header.append('DesiredMinTxInterval')
            header.append('RequiredMinRxInterval')
            header.append('RemoteMinRxInterval')
            header.append('DetectionMultiplier')
            header.append('RemoteDetectionMultiplier')
            header.append('DemandMode')
            header.append('RemoteDemandMode')
            header.append('AuthSeqKnown')
            header.append('AuthType')
            header.append('ReceivedAuthSeq')
            header.append('SentAuthSeq')
            header.append('NumTxPackets')
            header.append('NumRxPackets')
            header.append('ToDownCount')
            header.append('ToUpCount')
            header.append('UpDuration')
            header.append('Interface')
            header.append('Owner')
            header.append('PerLink')

        objs = self.swtch.getAllBfdSessionStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IpAddr'])
            values.append('%s' % o['SessionId'])
            values.append('%s' % o['ParamName'])
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['InterfaceSpecific'])
            values.append('%s' % o['PerLinkSession'])
            values.append('%s' % o['LocalMacAddr'])
            values.append('%s' % o['RemoteMacAddr'])
            values.append('%s' % o['RegisteredProtocols'])
            values.append('%s' % o['SessionState'])
            values.append('%s' % o['RemoteSessionState'])
            values.append('%s' % o['LocalDiscriminator'])
            values.append('%s' % o['RemoteDiscriminator'])
            values.append('%s' % o['LocalDiagType'])
            values.append('%s' % o['DesiredMinTxInterval'])
            values.append('%s' % o['RequiredMinRxInterval'])
            values.append('%s' % o['RemoteMinRxInterval'])
            values.append('%s' % o['DetectionMultiplier'])
            values.append('%s' % o['RemoteDetectionMultiplier'])
            values.append('%s' % o['DemandMode'])
            values.append('%s' % o['RemoteDemandMode'])
            values.append('%s' % o['AuthSeqKnown'])
            values.append('%s' % o['AuthType'])
            values.append('%s' % o['ReceivedAuthSeq'])
            values.append('%s' % o['SentAuthSeq'])
            values.append('%s' % o['NumTxPackets'])
            values.append('%s' % o['NumRxPackets'])
            values.append('%s' % o['ToDownCount'])
            values.append('%s' % o['ToUpCount'])
            values.append('%s' % o['UpDuration'])
            r = self.swtch.getBfdSession(o['IpAddr'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
                values.append('%s' % o['Interface'])
                values.append('%s' % o['Owner'])
                values.append('%s' % o['PerLink'])
            rows.append(values)
        self.tblPrintObject('BfdSessionState', header, rows)


    def printOspfEventStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Index')
            header.append('TimeStamp')
            header.append('EventType')
            header.append('EventInfo')

        objs = self.swtch.getAllOspfEventStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Index'])
            values.append('%s' % o['TimeStamp'])
            values.append('%s' % o['EventType'])
            values.append('%s' % o['EventInfo'])
            rows.append(values)
        self.tblPrintObject('OspfEventState', header, rows)


    def printOspfEventState(self, Index, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Index')
            header.append('TimeStamp')
            header.append('EventType')
            header.append('EventInfo')

        rawobj = self.swtch.getOspfEventState(
                                              Index)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['Index'])
            values.append('%s' % o['TimeStamp'])
            values.append('%s' % o['EventType'])
            values.append('%s' % o['EventInfo'])
            rows.append(values)
            self.tblPrintObject('OspfEventState', header, rows)

        else:
            print rawobj.content

    def printLLDPIntfs(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('Enable')
            header.append('TxRxMode')

        objs = self.swtch.getAllLLDPIntfs()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['Enable'])
            values.append('%s' % o['TxRxMode'])
            rows.append(values)
        self.tblPrintObject('LLDPIntf', header, rows)


    def printBufferGlobalStatStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('DeviceId')
            header.append('BufferStat')
            header.append('EgressBufferStat')
            header.append('IngressBufferStat')

        objs = self.swtch.getAllBufferGlobalStatStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['DeviceId'])
            values.append('%s' % o['BufferStat'])
            values.append('%s' % o['EgressBufferStat'])
            values.append('%s' % o['IngressBufferStat'])
            rows.append(values)
        self.tblPrintObject('BufferGlobalStatState', header, rows)


    def printBufferGlobalStatState(self, DeviceId, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('DeviceId')
            header.append('BufferStat')
            header.append('EgressBufferStat')
            header.append('IngressBufferStat')

        rawobj = self.swtch.getBufferGlobalStatState(
                                                     DeviceId)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['DeviceId'])
            values.append('%s' % o['BufferStat'])
            values.append('%s' % o['EgressBufferStat'])
            values.append('%s' % o['IngressBufferStat'])
            rows.append(values)
            self.tblPrintObject('BufferGlobalStatState', header, rows)

        else:
            print rawobj.content

    def printIPv6IntfStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('IfIndex')
            header.append('IpAddr')
            header.append('OperState')
            header.append('NumUpEvents')
            header.append('LastUpEventTime')
            header.append('NumDownEvents')
            header.append('LastDownEventTime')
            header.append('L2IntfType')
            header.append('L2IntfId')

        objs = self.swtch.getAllIPv6IntfStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['IpAddr'])
            values.append('%s' % o['OperState'])
            values.append('%s' % o['NumUpEvents'])
            values.append('%s' % o['LastUpEventTime'])
            values.append('%s' % o['NumDownEvents'])
            values.append('%s' % o['LastDownEventTime'])
            values.append('%s' % o['L2IntfType'])
            values.append('%s' % o['L2IntfId'])
            rows.append(values)
        var = self.tblPrintObject('IPv6IntfState', header, rows)
        return var

    def printIPv6IntfState(self, IntfRef, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('IfIndex')
            header.append('IpAddr')
            header.append('OperState')
            header.append('NumUpEvents')
            header.append('LastUpEventTime')
            header.append('NumDownEvents')
            header.append('LastDownEventTime')
            header.append('L2IntfType')
            header.append('L2IntfId')

        rawobj = self.swtch.getIPv6IntfState(
                                             IntfRef)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['IpAddr'])
            values.append('%s' % o['OperState'])
            values.append('%s' % o['NumUpEvents'])
            values.append('%s' % o['LastUpEventTime'])
            values.append('%s' % o['NumDownEvents'])
            values.append('%s' % o['LastDownEventTime'])
            values.append('%s' % o['L2IntfType'])
            values.append('%s' % o['L2IntfId'])
            rows.append(values)
            self.tblPrintObject('IPv6IntfState', header, rows)

        else:
            print rawobj.content

    def printCombinedIPv6IntfStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('IfIndex')
            header.append('IpAddr')
            header.append('OperState')
            header.append('NumUpEvents')
            header.append('LastUpEventTime')
            header.append('NumDownEvents')
            header.append('LastDownEventTime')
            header.append('L2IntfType')
            header.append('L2IntfId')
            header.append('AdminState')
            header.append('LinkIp')

        objs = self.swtch.getAllIPv6IntfStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['IpAddr'])
            values.append('%s' % o['OperState'])
            values.append('%s' % o['NumUpEvents'])
            values.append('%s' % o['LastUpEventTime'])
            values.append('%s' % o['NumDownEvents'])
            values.append('%s' % o['LastDownEventTime'])
            values.append('%s' % o['L2IntfType'])
            values.append('%s' % o['L2IntfId'])
            r = self.swtch.getIPv6Intf(o['IntfRef'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
                values.append('%s' % o['AdminState'])
                values.append('%s' % o['LinkIp'])
            rows.append(values)
        self.tblPrintObject('IPv6IntfState', header, rows)


    def printIPv4Intfs(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('IpAddr')
            header.append('AdminState')

        objs = self.swtch.getAllIPv4Intfs()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['IpAddr'])
            values.append('%s' % o['AdminState'])
            rows.append(values)
        self.tblPrintObject('IPv4Intf', header, rows)


    def printPolicyStmtStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('MatchConditions')
            header.append('Conditions')
            header.append('Action')
            header.append('PolicyList')

        objs = self.swtch.getAllPolicyStmtStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['MatchConditions'])
            values.append('%s' % o['Conditions'])
            values.append('%s' % o['Action'])
            values.append('%s' % o['PolicyList'])
            rows.append(values)
        self.tblPrintObject('PolicyStmtState', header, rows)


    def printPolicyStmtState(self, Name, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('MatchConditions')
            header.append('Conditions')
            header.append('Action')
            header.append('PolicyList')

        rawobj = self.swtch.getPolicyStmtState(
                                               Name)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['MatchConditions'])
            values.append('%s' % o['Conditions'])
            values.append('%s' % o['Action'])
            values.append('%s' % o['PolicyList'])
            rows.append(values)
            self.tblPrintObject('PolicyStmtState', header, rows)

        else:
            print rawobj.content

    def printCombinedPolicyStmtStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('MatchConditions')
            header.append('Conditions')
            header.append('Action')
            header.append('PolicyList')

        objs = self.swtch.getAllPolicyStmtStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['MatchConditions'])
            values.append('%s' % o['Conditions'])
            values.append('%s' % o['Action'])
            values.append('%s' % o['PolicyList'])
            r = self.swtch.getPolicyStmt(o['Name'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
            rows.append(values)
        self.tblPrintObject('PolicyStmtState', header, rows)


    def printPowerConverterSensorPMDataStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Class')
            header.append('Name')
            header.append('Data')

        objs = self.swtch.getAllPowerConverterSensorPMDataStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Class'])
            values.append('%s' % o['Name'])
            values.append('%s' % o['Data'])
            rows.append(values)
        self.tblPrintObject('PowerConverterSensorPMDataState', header, rows)


    def printPowerConverterSensorPMDataState(self, Class,Name, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Class')
            header.append('Name')
            header.append('Data')

        rawobj = self.swtch.getPowerConverterSensorPMDataState(
                                                               Class,
                                                               Name)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['Class'])
            values.append('%s' % o['Name'])
            values.append('%s' % o['Data'])
            rows.append(values)
            self.tblPrintObject('PowerConverterSensorPMDataState', header, rows)

        else:
            print rawobj.content

    def printIPv6Routes(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('DestinationNw')
            header.append('NetworkMask')
            header.append('NextHop')
            header.append('Protocol')
            header.append('NullRoute')
            header.append('Cost')

        objs = self.swtch.getAllIPv6Routes()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['DestinationNw'])
            values.append('%s' % o['NetworkMask'])
            values.append('%s' % o['NextHop'])
            values.append('%s' % o['Protocol'])
            values.append('%s' % o['NullRoute'])
            values.append('%s' % o['Cost'])
            rows.append(values)
        self.tblPrintObject('IPv6Route', header, rows)


    def printNDPEntryStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IpAddr')
            header.append('MacAddr')
            header.append('Vlan')
            header.append('Intf')
            header.append('IfIndex')

        objs = self.swtch.getAllNDPEntryStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IpAddr'])
            values.append('%s' % o['MacAddr'])
            values.append('%s' % o['Vlan'])
            values.append('%s' % o['Intf'])
            values.append('%s' % o['IfIndex'])
            rows.append(values)
        self.tblPrintObject('NDPEntryState', header, rows)


    def printNDPEntryState(self, IpAddr, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IpAddr')
            header.append('MacAddr')
            header.append('Vlan')
            header.append('Intf')
            header.append('IfIndex')

        rawobj = self.swtch.getNDPEntryState(
                                             IpAddr)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['IpAddr'])
            values.append('%s' % o['MacAddr'])
            values.append('%s' % o['Vlan'])
            values.append('%s' % o['Intf'])
            values.append('%s' % o['IfIndex'])
            rows.append(values)
            self.tblPrintObject('NDPEntryState', header, rows)

        else:
            print rawobj.content

    def printDWDMModuleClntIntfs(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('ClntIntfId')
            header.append('ModuleId')
            header.append('NwLaneTributaryToClntIntfMap')
            header.append('HostTxEqDfe')
            header.append('HostRxSerializerTap1Gain')
            header.append('RxPRBSPattern')
            header.append('HostRxSerializerTap2Delay')
            header.append('HostRxSerializerTap2Gain')
            header.append('HostRxSerializerTap0Delay')
            header.append('HostTxEqCtle')
            header.append('TxPRBSPattern')
            header.append('HostTxEqLfCtle')
            header.append('AdminState')
            header.append('RXFECDecDisable')
            header.append('EnableTxPRBSChecker')
            header.append('EnableHostLoopback')
            header.append('HostRxSerializerTap0Gain')
            header.append('TXFECDecDisable')
            header.append('EnableRxPRBS')
            header.append('EnableIntSerdesNWLoopback')

        objs = self.swtch.getAllDWDMModuleClntIntfs()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['ClntIntfId'])
            values.append('%s' % o['ModuleId'])
            values.append('%s' % o['NwLaneTributaryToClntIntfMap'])
            values.append('%s' % o['HostTxEqDfe'])
            values.append('%s' % o['HostRxSerializerTap1Gain'])
            values.append('%s' % o['RxPRBSPattern'])
            values.append('%s' % o['HostRxSerializerTap2Delay'])
            values.append('%s' % o['HostRxSerializerTap2Gain'])
            values.append('%s' % o['HostRxSerializerTap0Delay'])
            values.append('%s' % o['HostTxEqCtle'])
            values.append('%s' % o['TxPRBSPattern'])
            values.append('%s' % o['HostTxEqLfCtle'])
            values.append('%s' % o['AdminState'])
            values.append('%s' % o['RXFECDecDisable'])
            values.append('%s' % o['EnableTxPRBSChecker'])
            values.append('%s' % o['EnableHostLoopback'])
            values.append('%s' % o['HostRxSerializerTap0Gain'])
            values.append('%s' % o['TXFECDecDisable'])
            values.append('%s' % o['EnableRxPRBS'])
            values.append('%s' % o['EnableIntSerdesNWLoopback'])
            rows.append(values)
        self.tblPrintObject('DWDMModuleClntIntf', header, rows)


    def printTemperatureSensorStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('CurrentTemperature')

        objs = self.swtch.getAllTemperatureSensorStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['CurrentTemperature'])
            rows.append(values)
        self.tblPrintObject('TemperatureSensorState', header, rows)


    def printTemperatureSensorState(self, Name, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('CurrentTemperature')

        rawobj = self.swtch.getTemperatureSensorState(
                                                      Name)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['CurrentTemperature'])
            rows.append(values)
            self.tblPrintObject('TemperatureSensorState', header, rows)

        else:
            print rawobj.content

    def printCombinedTemperatureSensorStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('CurrentTemperature')
            header.append('HigherAlarmThreshold')
            header.append('HigherWarningThreshold')
            header.append('LowerWarningThreshold')
            header.append('LowerAlarmThreshold')
            header.append('PMClassCAdminState')
            header.append('PMClassAAdminState')
            header.append('AdminState')
            header.append('PMClassBAdminState')

        objs = self.swtch.getAllTemperatureSensorStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['CurrentTemperature'])
            r = self.swtch.getTemperatureSensor(o['Name'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
                values.append('%s' % o['HigherAlarmThreshold'])
                values.append('%s' % o['HigherWarningThreshold'])
                values.append('%s' % o['LowerWarningThreshold'])
                values.append('%s' % o['LowerAlarmThreshold'])
                values.append('%s' % o['PMClassCAdminState'])
                values.append('%s' % o['PMClassAAdminState'])
                values.append('%s' % o['AdminState'])
                values.append('%s' % o['PMClassBAdminState'])
            rows.append(values)
        self.tblPrintObject('TemperatureSensorState', header, rows)


    def printRouteStatsPerInterfaceStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Intfref')
            header.append('V4Routes')
            header.append('V6Routes')

        objs = self.swtch.getAllRouteStatsPerInterfaceStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Intfref'])
            values.append('%s' % o['V4Routes'])
            values.append('%s' % o['V6Routes'])
            rows.append(values)
        self.tblPrintObject('RouteStatsPerInterfaceState', header, rows)


    def printRouteStatsPerInterfaceState(self, Intfref, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Intfref')
            header.append('V4Routes')
            header.append('V6Routes')

        rawobj = self.swtch.getRouteStatsPerInterfaceState(
                                                           Intfref)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['Intfref'])
            values.append('%s' % o['V4Routes'])
            values.append('%s' % o['V6Routes'])
            rows.append(values)
            self.tblPrintObject('RouteStatsPerInterfaceState', header, rows)

        else:
            print rawobj.content

    def printNDPGlobalStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Vrf')
            header.append('RetransmitInterval')
            header.append('ReachableTime')
            header.append('RouterAdvertisementInterval')
            header.append('Neighbors')
            header.append('TotalTxPackets')
            header.append('TotalRxPackets')

        objs = self.swtch.getAllNDPGlobalStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Vrf'])
            values.append('%s' % o['RetransmitInterval'])
            values.append('%s' % o['ReachableTime'])
            values.append('%s' % o['RouterAdvertisementInterval'])
            values.append('%s' % o['Neighbors'])
            values.append('%s' % o['TotalTxPackets'])
            values.append('%s' % o['TotalRxPackets'])
            rows.append(values)
        self.tblPrintObject('NDPGlobalState', header, rows)


    def printNDPGlobalState(self, Vrf, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Vrf')
            header.append('RetransmitInterval')
            header.append('ReachableTime')
            header.append('RouterAdvertisementInterval')
            header.append('Neighbors')
            header.append('TotalTxPackets')
            header.append('TotalRxPackets')

        rawobj = self.swtch.getNDPGlobalState(
                                              Vrf)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['Vrf'])
            values.append('%s' % o['RetransmitInterval'])
            values.append('%s' % o['ReachableTime'])
            values.append('%s' % o['RouterAdvertisementInterval'])
            values.append('%s' % o['Neighbors'])
            values.append('%s' % o['TotalTxPackets'])
            values.append('%s' % o['TotalRxPackets'])
            rows.append(values)
            self.tblPrintObject('NDPGlobalState', header, rows)

        else:
            print rawobj.content

    def printCombinedNDPGlobalStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Vrf')
            header.append('RetransmitInterval')
            header.append('ReachableTime')
            header.append('RouterAdvertisementInterval')
            header.append('Neighbors')
            header.append('TotalTxPackets')
            header.append('TotalRxPackets')

        objs = self.swtch.getAllNDPGlobalStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Vrf'])
            values.append('%s' % o['RetransmitInterval'])
            values.append('%s' % o['ReachableTime'])
            values.append('%s' % o['RouterAdvertisementInterval'])
            values.append('%s' % o['Neighbors'])
            values.append('%s' % o['TotalTxPackets'])
            values.append('%s' % o['TotalRxPackets'])
            r = self.swtch.getNDPGlobal(o['Vrf'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
            rows.append(values)
        self.tblPrintObject('NDPGlobalState', header, rows)


    def printLacpGlobalStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Vrf')
            header.append('AggList')
            header.append('DistributedRelayList')
            header.append('DistributedRelayAttachedList')
            header.append('AggOperStateUpList')
            header.append('DistributedRelayUpList')
            header.append('LacpErrorsInPkts')
            header.append('LacpMissMatchPkts')
            header.append('LacpTotalRxPkts')
            header.append('LacpTotalTxPkts')
            header.append('AdminState')

        objs = self.swtch.getAllLacpGlobalStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Vrf'])
            values.append('%s' % o['AggList'])
            values.append('%s' % o['DistributedRelayList'])
            values.append('%s' % o['DistributedRelayAttachedList'])
            values.append('%s' % o['AggOperStateUpList'])
            values.append('%s' % o['DistributedRelayUpList'])
            values.append('%s' % o['LacpErrorsInPkts'])
            values.append('%s' % o['LacpMissMatchPkts'])
            values.append('%s' % o['LacpTotalRxPkts'])
            values.append('%s' % o['LacpTotalTxPkts'])
            values.append('%s' % o['AdminState'])
            rows.append(values)
        self.tblPrintObject('LacpGlobalState', header, rows)


    def printLacpGlobalState(self, Vrf, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Vrf')
            header.append('AggList')
            header.append('DistributedRelayList')
            header.append('DistributedRelayAttachedList')
            header.append('AggOperStateUpList')
            header.append('DistributedRelayUpList')
            header.append('LacpErrorsInPkts')
            header.append('LacpMissMatchPkts')
            header.append('LacpTotalRxPkts')
            header.append('LacpTotalTxPkts')
            header.append('AdminState')

        rawobj = self.swtch.getLacpGlobalState(
                                               Vrf)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['Vrf'])
            values.append('%s' % o['AggList'])
            values.append('%s' % o['DistributedRelayList'])
            values.append('%s' % o['DistributedRelayAttachedList'])
            values.append('%s' % o['AggOperStateUpList'])
            values.append('%s' % o['DistributedRelayUpList'])
            values.append('%s' % o['LacpErrorsInPkts'])
            values.append('%s' % o['LacpMissMatchPkts'])
            values.append('%s' % o['LacpTotalRxPkts'])
            values.append('%s' % o['LacpTotalTxPkts'])
            values.append('%s' % o['AdminState'])
            rows.append(values)
            self.tblPrintObject('LacpGlobalState', header, rows)

        else:
            print rawobj.content

    def printCombinedLacpGlobalStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Vrf')
            header.append('AggList')
            header.append('DistributedRelayList')
            header.append('DistributedRelayAttachedList')
            header.append('AggOperStateUpList')
            header.append('DistributedRelayUpList')
            header.append('LacpErrorsInPkts')
            header.append('LacpMissMatchPkts')
            header.append('LacpTotalRxPkts')
            header.append('LacpTotalTxPkts')
            header.append('AdminState')

        objs = self.swtch.getAllLacpGlobalStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Vrf'])
            values.append('%s' % o['AggList'])
            values.append('%s' % o['DistributedRelayList'])
            values.append('%s' % o['DistributedRelayAttachedList'])
            values.append('%s' % o['AggOperStateUpList'])
            values.append('%s' % o['DistributedRelayUpList'])
            values.append('%s' % o['LacpErrorsInPkts'])
            values.append('%s' % o['LacpMissMatchPkts'])
            values.append('%s' % o['LacpTotalRxPkts'])
            values.append('%s' % o['LacpTotalTxPkts'])
            values.append('%s' % o['AdminState'])
            r = self.swtch.getLacpGlobal(o['Vrf'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
            rows.append(values)
        self.tblPrintObject('LacpGlobalState', header, rows)


    def printQsfps(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('QsfpId')
            header.append('HigherAlarmTemperature')
            header.append('HigherAlarmVoltage')
            header.append('HigherWarningTemperature')
            header.append('HigherWarningVoltage')
            header.append('LowerAlarmTemperature')
            header.append('LowerAlarmVoltage')
            header.append('LowerWarningTemperature')
            header.append('LowerWarningVoltage')
            header.append('PMClassBAdminState')
            header.append('PMClassCAdminState')
            header.append('PMClassAAdminState')
            header.append('AdminState')

        objs = self.swtch.getAllQsfps()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['QsfpId'])
            values.append('%s' % o['HigherAlarmTemperature'])
            values.append('%s' % o['HigherAlarmVoltage'])
            values.append('%s' % o['HigherWarningTemperature'])
            values.append('%s' % o['HigherWarningVoltage'])
            values.append('%s' % o['LowerAlarmTemperature'])
            values.append('%s' % o['LowerAlarmVoltage'])
            values.append('%s' % o['LowerWarningTemperature'])
            values.append('%s' % o['LowerWarningVoltage'])
            values.append('%s' % o['PMClassBAdminState'])
            values.append('%s' % o['PMClassCAdminState'])
            values.append('%s' % o['PMClassAAdminState'])
            values.append('%s' % o['AdminState'])
            rows.append(values)
        self.tblPrintObject('Qsfp', header, rows)


    def printVoltageSensorPMDataStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Class')
            header.append('Name')
            header.append('Data')

        objs = self.swtch.getAllVoltageSensorPMDataStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Class'])
            values.append('%s' % o['Name'])
            values.append('%s' % o['Data'])
            rows.append(values)
        self.tblPrintObject('VoltageSensorPMDataState', header, rows)


    def printVoltageSensorPMDataState(self, Class,Name, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Class')
            header.append('Name')
            header.append('Data')

        rawobj = self.swtch.getVoltageSensorPMDataState(
                                                        Class,
                                                        Name)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['Class'])
            values.append('%s' % o['Name'])
            values.append('%s' % o['Data'])
            rows.append(values)
            self.tblPrintObject('VoltageSensorPMDataState', header, rows)

        else:
            print rawobj.content

    def printIPV6AdjStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('IfIndex')
            header.append('LinkScopeIp')
            header.append('GlobalScopeIp')
            header.append('SendPackets')
            header.append('ReceivedPackets')
            header.append('Neighbors')

        objs = self.swtch.getAllIPV6AdjStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['LinkScopeIp'])
            values.append('%s' % o['GlobalScopeIp'])
            values.append('%s' % o['SendPackets'])
            values.append('%s' % o['ReceivedPackets'])
            values.append('%s' % o['Neighbors'])
            rows.append(values)
        self.tblPrintObject('IPV6AdjState', header, rows)


    def printIPV6AdjState(self, IntfRef, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('IfIndex')
            header.append('LinkScopeIp')
            header.append('GlobalScopeIp')
            header.append('SendPackets')
            header.append('ReceivedPackets')
            header.append('Neighbors')

        rawobj = self.swtch.getIPV6AdjState(
                                            IntfRef)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['LinkScopeIp'])
            values.append('%s' % o['GlobalScopeIp'])
            values.append('%s' % o['SendPackets'])
            values.append('%s' % o['ReceivedPackets'])
            values.append('%s' % o['Neighbors'])
            rows.append(values)
            self.tblPrintObject('IPV6AdjState', header, rows)

        else:
            print rawobj.content

    def printDhcpIntfConfigs(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('Subnet')
            header.append('SubnetMask')
            header.append('IPAddrRange')
            header.append('BroadcastAddr')
            header.append('RouterAddr')
            header.append('DNSServerAddr')
            header.append('DomainName')
            header.append('Enable')

        objs = self.swtch.getAllDhcpIntfConfigs()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['Subnet'])
            values.append('%s' % o['SubnetMask'])
            values.append('%s' % o['IPAddrRange'])
            values.append('%s' % o['BroadcastAddr'])
            values.append('%s' % o['RouterAddr'])
            values.append('%s' % o['DNSServerAddr'])
            values.append('%s' % o['DomainName'])
            values.append('%s' % o['Enable'])
            rows.append(values)
        self.tblPrintObject('DhcpIntfConfig', header, rows)


    def printQsfpChannelPMDataStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('ChannelNum')
            header.append('Class')
            header.append('Resource')
            header.append('QsfpId')
            header.append('Data')

        objs = self.swtch.getAllQsfpChannelPMDataStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['ChannelNum'])
            values.append('%s' % o['Class'])
            values.append('%s' % o['Resource'])
            values.append('%s' % o['QsfpId'])
            values.append('%s' % o['Data'])
            rows.append(values)
        self.tblPrintObject('QsfpChannelPMDataState', header, rows)


    def printQsfpChannelPMDataState(self, ChannelNum,Class,Resource,QsfpId, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('ChannelNum')
            header.append('Class')
            header.append('Resource')
            header.append('QsfpId')
            header.append('Data')

        rawobj = self.swtch.getQsfpChannelPMDataState(
                                                      ChannelNum,
                                                      Class,
                                                      Resource,
                                                      QsfpId)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['ChannelNum'])
            values.append('%s' % o['Class'])
            values.append('%s' % o['Resource'])
            values.append('%s' % o['QsfpId'])
            values.append('%s' % o['Data'])
            rows.append(values)
            self.tblPrintObject('QsfpChannelPMDataState', header, rows)

        else:
            print rawobj.content

    def printVrrpIntfStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('VRID')
            header.append('IfIndex')
            header.append('IntfIpAddr')
            header.append('Priority')
            header.append('VirtualIPv4Addr')
            header.append('AdvertisementInterval')
            header.append('PreemptMode')
            header.append('VirtualRouterMACAddress')
            header.append('SkewTime')
            header.append('MasterDownTimer')
            header.append('VrrpState')

        objs = self.swtch.getAllVrrpIntfStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['VRID'])
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['IntfIpAddr'])
            values.append('%s' % o['Priority'])
            values.append('%s' % o['VirtualIPv4Addr'])
            values.append('%s' % o['AdvertisementInterval'])
            values.append('%s' % o['PreemptMode'])
            values.append('%s' % o['VirtualRouterMACAddress'])
            values.append('%s' % o['SkewTime'])
            values.append('%s' % o['MasterDownTimer'])
            values.append('%s' % o['VrrpState'])
            rows.append(values)
        self.tblPrintObject('VrrpIntfState', header, rows)


    def printVrrpIntfState(self, VRID,IfIndex, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('VRID')
            header.append('IfIndex')
            header.append('IntfIpAddr')
            header.append('Priority')
            header.append('VirtualIPv4Addr')
            header.append('AdvertisementInterval')
            header.append('PreemptMode')
            header.append('VirtualRouterMACAddress')
            header.append('SkewTime')
            header.append('MasterDownTimer')
            header.append('VrrpState')

        rawobj = self.swtch.getVrrpIntfState(
                                             VRID,
                                             IfIndex)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['VRID'])
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['IntfIpAddr'])
            values.append('%s' % o['Priority'])
            values.append('%s' % o['VirtualIPv4Addr'])
            values.append('%s' % o['AdvertisementInterval'])
            values.append('%s' % o['PreemptMode'])
            values.append('%s' % o['VirtualRouterMACAddress'])
            values.append('%s' % o['SkewTime'])
            values.append('%s' % o['MasterDownTimer'])
            values.append('%s' % o['VrrpState'])
            rows.append(values)
            self.tblPrintObject('VrrpIntfState', header, rows)

        else:
            print rawobj.content

    def printCombinedVrrpIntfStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('VRID')
            header.append('IfIndex')
            header.append('IntfIpAddr')
            header.append('Priority')
            header.append('VirtualIPv4Addr')
            header.append('AdvertisementInterval')
            header.append('PreemptMode')
            header.append('VirtualRouterMACAddress')
            header.append('SkewTime')
            header.append('MasterDownTimer')
            header.append('VrrpState')
            header.append('AcceptMode')

        objs = self.swtch.getAllVrrpIntfStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['VRID'])
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['IntfIpAddr'])
            values.append('%s' % o['Priority'])
            values.append('%s' % o['VirtualIPv4Addr'])
            values.append('%s' % o['AdvertisementInterval'])
            values.append('%s' % o['PreemptMode'])
            values.append('%s' % o['VirtualRouterMACAddress'])
            values.append('%s' % o['SkewTime'])
            values.append('%s' % o['MasterDownTimer'])
            values.append('%s' % o['VrrpState'])
            r = self.swtch.getVrrpIntf(o['VRID'], o['IfIndex'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
                values.append('%s' % o['AcceptMode'])
            rows.append(values)
        self.tblPrintObject('VrrpIntfState', header, rows)


    def printSystemStatusStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('Ready')
            header.append('Reason')
            header.append('UpTime')
            header.append('NumCreateCalls')
            header.append('NumDeleteCalls')
            header.append('NumUpdateCalls')
            header.append('NumGetCalls')
            header.append('NumActionCalls')
            header.append('FlexDaemons')

        objs = self.swtch.getAllSystemStatusStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['Ready'])
            values.append('%s' % o['Reason'])
            values.append('%s' % o['UpTime'])
            values.append('%s' % o['NumCreateCalls'])
            values.append('%s' % o['NumDeleteCalls'])
            values.append('%s' % o['NumUpdateCalls'])
            values.append('%s' % o['NumGetCalls'])
            values.append('%s' % o['NumActionCalls'])
            values.append('%s' % o['FlexDaemons'])
            rows.append(values)
        self.tblPrintObject('SystemStatusState', header, rows)


    def printSystemStatusState(self, Name, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('Ready')
            header.append('Reason')
            header.append('UpTime')
            header.append('NumCreateCalls')
            header.append('NumDeleteCalls')
            header.append('NumUpdateCalls')
            header.append('NumGetCalls')
            header.append('NumActionCalls')
            header.append('FlexDaemons')

        rawobj = self.swtch.getSystemStatusState(
                                                 Name)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['Ready'])
            values.append('%s' % o['Reason'])
            values.append('%s' % o['UpTime'])
            values.append('%s' % o['NumCreateCalls'])
            values.append('%s' % o['NumDeleteCalls'])
            values.append('%s' % o['NumUpdateCalls'])
            values.append('%s' % o['NumGetCalls'])
            values.append('%s' % o['NumActionCalls'])
            values.append('%s' % o['FlexDaemons'])
            rows.append(values)
            self.tblPrintObject('SystemStatusState', header, rows)

        else:
            print rawobj.content

    def printFanSensors(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('HigherAlarmThreshold')
            header.append('HigherWarningThreshold')
            header.append('LowerWarningThreshold')
            header.append('LowerAlarmThreshold')
            header.append('PMClassCAdminState')
            header.append('PMClassAAdminState')
            header.append('AdminState')
            header.append('PMClassBAdminState')

        objs = self.swtch.getAllFanSensors()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['HigherAlarmThreshold'])
            values.append('%s' % o['HigherWarningThreshold'])
            values.append('%s' % o['LowerWarningThreshold'])
            values.append('%s' % o['LowerAlarmThreshold'])
            values.append('%s' % o['PMClassCAdminState'])
            values.append('%s' % o['PMClassAAdminState'])
            values.append('%s' % o['AdminState'])
            values.append('%s' % o['PMClassBAdminState'])
            rows.append(values)
        self.tblPrintObject('FanSensor', header, rows)


    def printIpTableAcls(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('Action')
            header.append('IpAddr')
            header.append('Protocol')
            header.append('Port')
            header.append('PhysicalPort')

        objs = self.swtch.getAllIpTableAcls()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['Action'])
            values.append('%s' % o['IpAddr'])
            values.append('%s' % o['Protocol'])
            values.append('%s' % o['Port'])
            values.append('%s' % o['PhysicalPort'])
            rows.append(values)
        self.tblPrintObject('IpTableAcl', header, rows)


    def printIppLinkStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('DrNameRef')
            header.append('IPPID')
            header.append('PortConversationPasses')
            header.append('GatewayConversationDirection')
            header.append('DRCPDUsRx')
            header.append('DRCPDUsTx')
            header.append('DRCPRxState')
            header.append('LastRxTime')
            header.append('DiffPortalReason')

        objs = self.swtch.getAllIppLinkStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['DrNameRef'])
            values.append('%s' % o['IPPID'])
            values.append('%s' % o['PortConversationPasses'])
            values.append('%s' % o['GatewayConversationDirection'])
            values.append('%s' % o['DRCPDUsRx'])
            values.append('%s' % o['DRCPDUsTx'])
            values.append('%s' % o['DRCPRxState'])
            values.append('%s' % o['LastRxTime'])
            values.append('%s' % o['DiffPortalReason'])
            rows.append(values)
        self.tblPrintObject('IppLinkState', header, rows)


    def printIppLinkState(self, IntfRef,DrNameRef, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('DrNameRef')
            header.append('IPPID')
            header.append('PortConversationPasses')
            header.append('GatewayConversationDirection')
            header.append('DRCPDUsRx')
            header.append('DRCPDUsTx')
            header.append('DRCPRxState')
            header.append('LastRxTime')
            header.append('DiffPortalReason')

        rawobj = self.swtch.getIppLinkState(
                                            IntfRef,
                                            DrNameRef)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['DrNameRef'])
            values.append('%s' % o['IPPID'])
            values.append('%s' % o['PortConversationPasses'])
            values.append('%s' % o['GatewayConversationDirection'])
            values.append('%s' % o['DRCPDUsRx'])
            values.append('%s' % o['DRCPDUsTx'])
            values.append('%s' % o['DRCPRxState'])
            values.append('%s' % o['LastRxTime'])
            values.append('%s' % o['DiffPortalReason'])
            rows.append(values)
            self.tblPrintObject('IppLinkState', header, rows)

        else:
            print rawobj.content

    def printDWDMModuleNwIntfStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('NwIntfId')
            header.append('ModuleId')
            header.append('TxChanGridSpacing')
            header.append('CurrentBER')
            header.append('MinBEROverPMInterval')
            header.append('AvgBEROverPMInterval')
            header.append('MaxBEROverPMInterval')
            header.append('CurrUncorrectableFECBlkCnt')
            header.append('UncorrectableFECBlkCntOverPMInt')
            header.append('PRBSRxErrCnt')
            header.append('RxPower')
            header.append('ChanFrequency')
            header.append('CurrChromDisp')
            header.append('AvgChromDispOverPMInt')
            header.append('MinChromDispOverPMInt')
            header.append('MaxChromDispOverPMInt')

        objs = self.swtch.getAllDWDMModuleNwIntfStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['NwIntfId'])
            values.append('%s' % o['ModuleId'])
            values.append('%s' % o['TxChanGridSpacing'])
            values.append('%s' % o['CurrentBER'])
            values.append('%s' % o['MinBEROverPMInterval'])
            values.append('%s' % o['AvgBEROverPMInterval'])
            values.append('%s' % o['MaxBEROverPMInterval'])
            values.append('%s' % o['CurrUncorrectableFECBlkCnt'])
            values.append('%s' % o['UncorrectableFECBlkCntOverPMInt'])
            values.append('%s' % o['PRBSRxErrCnt'])
            values.append('%s' % o['RxPower'])
            values.append('%s' % o['ChanFrequency'])
            values.append('%s' % o['CurrChromDisp'])
            values.append('%s' % o['AvgChromDispOverPMInt'])
            values.append('%s' % o['MinChromDispOverPMInt'])
            values.append('%s' % o['MaxChromDispOverPMInt'])
            rows.append(values)
        self.tblPrintObject('DWDMModuleNwIntfState', header, rows)


    def printDWDMModuleNwIntfState(self, NwIntfId,ModuleId, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('NwIntfId')
            header.append('ModuleId')
            header.append('TxChanGridSpacing')
            header.append('CurrentBER')
            header.append('MinBEROverPMInterval')
            header.append('AvgBEROverPMInterval')
            header.append('MaxBEROverPMInterval')
            header.append('CurrUncorrectableFECBlkCnt')
            header.append('UncorrectableFECBlkCntOverPMInt')
            header.append('PRBSRxErrCnt')
            header.append('RxPower')
            header.append('ChanFrequency')
            header.append('CurrChromDisp')
            header.append('AvgChromDispOverPMInt')
            header.append('MinChromDispOverPMInt')
            header.append('MaxChromDispOverPMInt')

        rawobj = self.swtch.getDWDMModuleNwIntfState(
                                                     NwIntfId,
                                                     ModuleId)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['NwIntfId'])
            values.append('%s' % o['ModuleId'])
            values.append('%s' % o['TxChanGridSpacing'])
            values.append('%s' % o['CurrentBER'])
            values.append('%s' % o['MinBEROverPMInterval'])
            values.append('%s' % o['AvgBEROverPMInterval'])
            values.append('%s' % o['MaxBEROverPMInterval'])
            values.append('%s' % o['CurrUncorrectableFECBlkCnt'])
            values.append('%s' % o['UncorrectableFECBlkCntOverPMInt'])
            values.append('%s' % o['PRBSRxErrCnt'])
            values.append('%s' % o['RxPower'])
            values.append('%s' % o['ChanFrequency'])
            values.append('%s' % o['CurrChromDisp'])
            values.append('%s' % o['AvgChromDispOverPMInt'])
            values.append('%s' % o['MinChromDispOverPMInt'])
            values.append('%s' % o['MaxChromDispOverPMInt'])
            rows.append(values)
            self.tblPrintObject('DWDMModuleNwIntfState', header, rows)

        else:
            print rawobj.content

    def printCombinedDWDMModuleNwIntfStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('NwIntfId')
            header.append('ModuleId')
            header.append('TxChanGridSpacing')
            header.append('CurrentBER')
            header.append('MinBEROverPMInterval')
            header.append('AvgBEROverPMInterval')
            header.append('MaxBEROverPMInterval')
            header.append('CurrUncorrectableFECBlkCnt')
            header.append('UncorrectableFECBlkCntOverPMInt')
            header.append('PRBSRxErrCnt')
            header.append('RxPower')
            header.append('ChanFrequency')
            header.append('CurrChromDisp')
            header.append('AvgChromDispOverPMInt')
            header.append('MinChromDispOverPMInt')
            header.append('MaxChromDispOverPMInt')
            header.append('ClntIntfIdToTributary0Map')
            header.append('ClntIntfIdToTributary1Map')
            header.append('EnableRxPRBSChecker')
            header.append('TxPulseShapeFltrRollOff')
            header.append('TxPower')
            header.append('RxPRBSInvertPattern')
            header.append('TxPowerRampdBmPerSec')
            header.append('EnableTxPRBS')
            header.append('TxPRBSInvertPattern')
            header.append('AdminState')
            header.append('ChannelNumber')
            header.append('FECMode')
            header.append('ModulationFmt')
            header.append('TxPulseShapeFltrType')
            header.append('RxPRBSPattern')
            header.append('TxPRBSPattern')
            header.append('DiffEncoding')

        objs = self.swtch.getAllDWDMModuleNwIntfStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['NwIntfId'])
            values.append('%s' % o['ModuleId'])
            values.append('%s' % o['TxChanGridSpacing'])
            values.append('%s' % o['CurrentBER'])
            values.append('%s' % o['MinBEROverPMInterval'])
            values.append('%s' % o['AvgBEROverPMInterval'])
            values.append('%s' % o['MaxBEROverPMInterval'])
            values.append('%s' % o['CurrUncorrectableFECBlkCnt'])
            values.append('%s' % o['UncorrectableFECBlkCntOverPMInt'])
            values.append('%s' % o['PRBSRxErrCnt'])
            values.append('%s' % o['RxPower'])
            values.append('%s' % o['ChanFrequency'])
            values.append('%s' % o['CurrChromDisp'])
            values.append('%s' % o['AvgChromDispOverPMInt'])
            values.append('%s' % o['MinChromDispOverPMInt'])
            values.append('%s' % o['MaxChromDispOverPMInt'])
            r = self.swtch.getDWDMModuleNwIntf(o['NwIntfId'], o['ModuleId'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
                values.append('%s' % o['ClntIntfIdToTributary0Map'])
                values.append('%s' % o['ClntIntfIdToTributary1Map'])
                values.append('%s' % o['EnableRxPRBSChecker'])
                values.append('%s' % o['TxPulseShapeFltrRollOff'])
                values.append('%s' % o['TxPower'])
                values.append('%s' % o['RxPRBSInvertPattern'])
                values.append('%s' % o['TxPowerRampdBmPerSec'])
                values.append('%s' % o['EnableTxPRBS'])
                values.append('%s' % o['TxPRBSInvertPattern'])
                values.append('%s' % o['AdminState'])
                values.append('%s' % o['ChannelNumber'])
                values.append('%s' % o['FECMode'])
                values.append('%s' % o['ModulationFmt'])
                values.append('%s' % o['TxPulseShapeFltrType'])
                values.append('%s' % o['RxPRBSPattern'])
                values.append('%s' % o['TxPRBSPattern'])
                values.append('%s' % o['DiffEncoding'])
            rows.append(values)
        self.tblPrintObject('DWDMModuleNwIntfState', header, rows)


    def printOspfIfEntrys(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IfIpAddress')
            header.append('AddressLessIf')
            header.append('IfAdminStat')
            header.append('IfAreaId')
            header.append('IfType')
            header.append('IfRtrPriority')
            header.append('IfTransitDelay')
            header.append('IfRetransInterval')
            header.append('IfPollInterval')
            header.append('IfAuthKey')
            header.append('IfAuthType')
            header.append('IfHelloInterval')
            header.append('IfRtrDeadInterval')

        objs = self.swtch.getAllOspfIfEntrys()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IfIpAddress'])
            values.append('%s' % o['AddressLessIf'])
            values.append('%s' % o['IfAdminStat'])
            values.append('%s' % o['IfAreaId'])
            values.append('%s' % o['IfType'])
            values.append('%s' % o['IfRtrPriority'])
            values.append('%s' % o['IfTransitDelay'])
            values.append('%s' % o['IfRetransInterval'])
            values.append('%s' % o['IfPollInterval'])
            values.append('%s' % o['IfAuthKey'])
            values.append('%s' % o['IfAuthType'])
            values.append('%s' % o['IfHelloInterval'])
            values.append('%s' % o['IfRtrDeadInterval'])
            rows.append(values)
        self.tblPrintObject('OspfIfEntry', header, rows)


    def printBufferPortStatStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('IfIndex')
            header.append('EgressPort')
            header.append('IngressPort')
            header.append('PortBufferStat')

        objs = self.swtch.getAllBufferPortStatStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['EgressPort'])
            values.append('%s' % o['IngressPort'])
            values.append('%s' % o['PortBufferStat'])
            rows.append(values)
        self.tblPrintObject('BufferPortStatState', header, rows)


    def printBufferPortStatState(self, IntfRef, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('IfIndex')
            header.append('EgressPort')
            header.append('IngressPort')
            header.append('PortBufferStat')

        rawobj = self.swtch.getBufferPortStatState(
                                                   IntfRef)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['EgressPort'])
            values.append('%s' % o['IngressPort'])
            values.append('%s' % o['PortBufferStat'])
            rows.append(values)
            self.tblPrintObject('BufferPortStatState', header, rows)

        else:
            print rawobj.content

    def printBGPGlobals(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Vrf')
            header.append('ASNum')
            header.append('UseMultiplePaths')
            header.append('EBGPMaxPaths')
            header.append('EBGPAllowMultipleAS')
            header.append('RouterId')
            header.append('IBGPMaxPaths')
            header.append('Redistribution')

        objs = self.swtch.getAllBGPGlobals()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Vrf'])
            values.append('%s' % o['ASNum'])
            values.append('%s' % o['UseMultiplePaths'])
            values.append('%s' % o['EBGPMaxPaths'])
            values.append('%s' % o['EBGPAllowMultipleAS'])
            values.append('%s' % o['RouterId'])
            values.append('%s' % o['IBGPMaxPaths'])
            values.append('%s' % o['Redistribution'])
            rows.append(values)
        self.tblPrintObject('BGPGlobal', header, rows)


    def printTemperatureSensorPMDataStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Class')
            header.append('Name')
            header.append('Data')

        objs = self.swtch.getAllTemperatureSensorPMDataStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Class'])
            values.append('%s' % o['Name'])
            values.append('%s' % o['Data'])
            rows.append(values)
        self.tblPrintObject('TemperatureSensorPMDataState', header, rows)


    def printTemperatureSensorPMDataState(self, Class,Name, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Class')
            header.append('Name')
            header.append('Data')

        rawobj = self.swtch.getTemperatureSensorPMDataState(
                                                            Class,
                                                            Name)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['Class'])
            values.append('%s' % o['Name'])
            values.append('%s' % o['Data'])
            rows.append(values)
            self.tblPrintObject('TemperatureSensorPMDataState', header, rows)

        else:
            print rawobj.content

    def printOspfAreaEntryStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('AreaId')
            header.append('SpfRuns')
            header.append('AreaBdrRtrCount')
            header.append('AsBdrRtrCount')
            header.append('AreaLsaCount')

        objs = self.swtch.getAllOspfAreaEntryStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['AreaId'])
            values.append('%s' % o['SpfRuns'])
            values.append('%s' % o['AreaBdrRtrCount'])
            values.append('%s' % o['AsBdrRtrCount'])
            values.append('%s' % o['AreaLsaCount'])
            rows.append(values)
        self.tblPrintObject('OspfAreaEntryState', header, rows)


    def printOspfAreaEntryState(self, AreaId, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('AreaId')
            header.append('SpfRuns')
            header.append('AreaBdrRtrCount')
            header.append('AsBdrRtrCount')
            header.append('AreaLsaCount')

        rawobj = self.swtch.getOspfAreaEntryState(
                                                  AreaId)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['AreaId'])
            values.append('%s' % o['SpfRuns'])
            values.append('%s' % o['AreaBdrRtrCount'])
            values.append('%s' % o['AsBdrRtrCount'])
            values.append('%s' % o['AreaLsaCount'])
            rows.append(values)
            self.tblPrintObject('OspfAreaEntryState', header, rows)

        else:
            print rawobj.content

    def printCombinedOspfAreaEntryStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('AreaId')
            header.append('SpfRuns')
            header.append('AreaBdrRtrCount')
            header.append('AsBdrRtrCount')
            header.append('AreaLsaCount')
            header.append('AuthType')
            header.append('ImportAsExtern')
            header.append('AreaSummary')
            header.append('AreaNssaTranslatorRole')
            header.append('StubDefaultCost')

        objs = self.swtch.getAllOspfAreaEntryStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['AreaId'])
            values.append('%s' % o['SpfRuns'])
            values.append('%s' % o['AreaBdrRtrCount'])
            values.append('%s' % o['AsBdrRtrCount'])
            values.append('%s' % o['AreaLsaCount'])
            r = self.swtch.getOspfAreaEntry(o['AreaId'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
                values.append('%s' % o['AuthType'])
                values.append('%s' % o['ImportAsExtern'])
                values.append('%s' % o['AreaSummary'])
                values.append('%s' % o['AreaNssaTranslatorRole'])
                values.append('%s' % o['StubDefaultCost'])
            rows.append(values)
        self.tblPrintObject('OspfAreaEntryState', header, rows)


    def printLLDPGlobalStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Vrf')
            header.append('Enable')
            header.append('TranmitInterval')
            header.append('Neighbors')
            header.append('TotalTxFrames')
            header.append('TotalRxFrames')

        objs = self.swtch.getAllLLDPGlobalStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Vrf'])
            values.append('%s' % o['Enable'])
            values.append('%s' % o['TranmitInterval'])
            values.append('%s' % o['Neighbors'])
            values.append('%s' % o['TotalTxFrames'])
            values.append('%s' % o['TotalRxFrames'])
            rows.append(values)
        self.tblPrintObject('LLDPGlobalState', header, rows)


    def printLLDPGlobalState(self, Vrf, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Vrf')
            header.append('Enable')
            header.append('TranmitInterval')
            header.append('Neighbors')
            header.append('TotalTxFrames')
            header.append('TotalRxFrames')

        rawobj = self.swtch.getLLDPGlobalState(
                                               Vrf)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['Vrf'])
            values.append('%s' % o['Enable'])
            values.append('%s' % o['TranmitInterval'])
            values.append('%s' % o['Neighbors'])
            values.append('%s' % o['TotalTxFrames'])
            values.append('%s' % o['TotalRxFrames'])
            rows.append(values)
            self.tblPrintObject('LLDPGlobalState', header, rows)

        else:
            print rawobj.content

    def printCombinedLLDPGlobalStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Vrf')
            header.append('Enable')
            header.append('TranmitInterval')
            header.append('Neighbors')
            header.append('TotalTxFrames')
            header.append('TotalRxFrames')
            header.append('TxRxMode')
            header.append('SnoopAndDrop')

        objs = self.swtch.getAllLLDPGlobalStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Vrf'])
            values.append('%s' % o['Enable'])
            values.append('%s' % o['TranmitInterval'])
            values.append('%s' % o['Neighbors'])
            values.append('%s' % o['TotalTxFrames'])
            values.append('%s' % o['TotalRxFrames'])
            r = self.swtch.getLLDPGlobal(o['Vrf'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
                values.append('%s' % o['TxRxMode'])
                values.append('%s' % o['SnoopAndDrop'])
            rows.append(values)
        self.tblPrintObject('LLDPGlobalState', header, rows)


    def printEthernetPMStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('Resource')
            header.append('ClassAPMData')
            header.append('ClassBPMData')
            header.append('ClassCPMData')

        objs = self.swtch.getAllEthernetPMStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['Resource'])
            values.append('%s' % o['ClassAPMData'])
            values.append('%s' % o['ClassBPMData'])
            values.append('%s' % o['ClassCPMData'])
            rows.append(values)
        self.tblPrintObject('EthernetPMState', header, rows)


    def printEthernetPMState(self, IntfRef,Resource, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('Resource')
            header.append('ClassAPMData')
            header.append('ClassBPMData')
            header.append('ClassCPMData')

        rawobj = self.swtch.getEthernetPMState(
                                               IntfRef,
                                               Resource)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['Resource'])
            values.append('%s' % o['ClassAPMData'])
            values.append('%s' % o['ClassBPMData'])
            values.append('%s' % o['ClassCPMData'])
            rows.append(values)
            self.tblPrintObject('EthernetPMState', header, rows)

        else:
            print rawobj.content

    def printCombinedEthernetPMStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('Resource')
            header.append('ClassAPMData')
            header.append('ClassBPMData')
            header.append('ClassCPMData')
            header.append('PMClassBEnable')
            header.append('PMClassCEnable')
            header.append('HighWarnThreshold')
            header.append('LowAlarmThreshold')
            header.append('PMClassAEnable')
            header.append('HighAlarmThreshold')
            header.append('LowWarnThreshold')

        objs = self.swtch.getAllEthernetPMStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['Resource'])
            values.append('%s' % o['ClassAPMData'])
            values.append('%s' % o['ClassBPMData'])
            values.append('%s' % o['ClassCPMData'])
            r = self.swtch.getEthernetPM(o['IntfRef'], o['Resource'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
                values.append('%s' % o['PMClassBEnable'])
                values.append('%s' % o['PMClassCEnable'])
                values.append('%s' % o['HighWarnThreshold'])
                values.append('%s' % o['LowAlarmThreshold'])
                values.append('%s' % o['PMClassAEnable'])
                values.append('%s' % o['HighAlarmThreshold'])
                values.append('%s' % o['LowWarnThreshold'])
            rows.append(values)
        self.tblPrintObject('EthernetPMState', header, rows)


    def printNDPGlobals(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Vrf')
            header.append('RetransmitInterval')
            header.append('RouterAdvertisementInterval')
            header.append('ReachableTime')

        objs = self.swtch.getAllNDPGlobals()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Vrf'])
            values.append('%s' % o['RetransmitInterval'])
            values.append('%s' % o['RouterAdvertisementInterval'])
            values.append('%s' % o['ReachableTime'])
            rows.append(values)
        self.tblPrintObject('NDPGlobal', header, rows)


    def printPsuStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('PsuId')
            header.append('AdminState')
            header.append('ModelNum')
            header.append('SerialNum')
            header.append('Vin')
            header.append('Vout')
            header.append('Iin')
            header.append('Iout')
            header.append('Pin')
            header.append('Pout')
            header.append('Fan')
            header.append('FanId')
            header.append('LedId')

        objs = self.swtch.getAllPsuStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['PsuId'])
            values.append('%s' % o['AdminState'])
            values.append('%s' % o['ModelNum'])
            values.append('%s' % o['SerialNum'])
            values.append('%s' % o['Vin'])
            values.append('%s' % o['Vout'])
            values.append('%s' % o['Iin'])
            values.append('%s' % o['Iout'])
            values.append('%s' % o['Pin'])
            values.append('%s' % o['Pout'])
            values.append('%s' % o['Fan'])
            values.append('%s' % o['FanId'])
            values.append('%s' % o['LedId'])
            rows.append(values)
        self.tblPrintObject('PsuState', header, rows)


    def printPsuState(self, PsuId, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('PsuId')
            header.append('AdminState')
            header.append('ModelNum')
            header.append('SerialNum')
            header.append('Vin')
            header.append('Vout')
            header.append('Iin')
            header.append('Iout')
            header.append('Pin')
            header.append('Pout')
            header.append('Fan')
            header.append('FanId')
            header.append('LedId')

        rawobj = self.swtch.getPsuState(
                                        PsuId)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['PsuId'])
            values.append('%s' % o['AdminState'])
            values.append('%s' % o['ModelNum'])
            values.append('%s' % o['SerialNum'])
            values.append('%s' % o['Vin'])
            values.append('%s' % o['Vout'])
            values.append('%s' % o['Iin'])
            values.append('%s' % o['Iout'])
            values.append('%s' % o['Pin'])
            values.append('%s' % o['Pout'])
            values.append('%s' % o['Fan'])
            values.append('%s' % o['FanId'])
            values.append('%s' % o['LedId'])
            rows.append(values)
            self.tblPrintObject('PsuState', header, rows)

        else:
            print rawobj.content

    def printCombinedPsuStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('PsuId')
            header.append('AdminState')
            header.append('ModelNum')
            header.append('SerialNum')
            header.append('Vin')
            header.append('Vout')
            header.append('Iin')
            header.append('Iout')
            header.append('Pin')
            header.append('Pout')
            header.append('Fan')
            header.append('FanId')
            header.append('LedId')

        objs = self.swtch.getAllPsuStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['PsuId'])
            values.append('%s' % o['AdminState'])
            values.append('%s' % o['ModelNum'])
            values.append('%s' % o['SerialNum'])
            values.append('%s' % o['Vin'])
            values.append('%s' % o['Vout'])
            values.append('%s' % o['Iin'])
            values.append('%s' % o['Iout'])
            values.append('%s' % o['Pin'])
            values.append('%s' % o['Pout'])
            values.append('%s' % o['Fan'])
            values.append('%s' % o['FanId'])
            values.append('%s' % o['LedId'])
            r = self.swtch.getPsu(o['PsuId'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
            rows.append(values)
        self.tblPrintObject('PsuState', header, rows)


    def printBfdSessions(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IpAddr')
            header.append('Interface')
            header.append('Owner')
            header.append('PerLink')
            header.append('ParamName')

        objs = self.swtch.getAllBfdSessions()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IpAddr'])
            values.append('%s' % o['Interface'])
            values.append('%s' % o['Owner'])
            values.append('%s' % o['PerLink'])
            values.append('%s' % o['ParamName'])
            rows.append(values)
        self.tblPrintObject('BfdSession', header, rows)


    def printPolicyConditionStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('ConditionInfo')
            header.append('PolicyStmtList')

        objs = self.swtch.getAllPolicyConditionStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['ConditionInfo'])
            values.append('%s' % o['PolicyStmtList'])
            rows.append(values)
        var = self.tblPrintObject('PolicyConditionState', header, rows)
        return var


    def printPolicyConditionState(self, Name, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('ConditionInfo')
            header.append('PolicyStmtList')

        rawobj = self.swtch.getPolicyConditionState(
                                                    Name)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['ConditionInfo'])
            values.append('%s' % o['PolicyStmtList'])
            rows.append(values)
            self.tblPrintObject('PolicyConditionState', header, rows)

        else:
            print rawobj.content

    def printCombinedPolicyConditionStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('ConditionInfo')
            header.append('PolicyStmtList')
            header.append('ConditionType')
            header.append('Protocol')
            header.append('IpPrefix')
            header.append('MaskLengthRange')
            header.append('PrefixSet')

        objs = self.swtch.getAllPolicyConditionStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['ConditionInfo'])
            values.append('%s' % o['PolicyStmtList'])
            r = self.swtch.getPolicyCondition(o['Name'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
                values.append('%s' % o['ConditionType'])
                values.append('%s' % o['Protocol'])
                values.append('%s' % o['IpPrefix'])
                values.append('%s' % o['MaskLengthRange'])
                values.append('%s' % o['PrefixSet'])
            rows.append(values)
        self.tblPrintObject('PolicyConditionState', header, rows)


    def printVrrpIntfs(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('VRID')
            header.append('IfIndex')
            header.append('VirtualIPv4Addr')
            header.append('PreemptMode')
            header.append('Priority')
            header.append('AdvertisementInterval')
            header.append('AcceptMode')

        objs = self.swtch.getAllVrrpIntfs()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['VRID'])
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['VirtualIPv4Addr'])
            values.append('%s' % o['PreemptMode'])
            values.append('%s' % o['Priority'])
            values.append('%s' % o['AdvertisementInterval'])
            values.append('%s' % o['AcceptMode'])
            rows.append(values)
        self.tblPrintObject('VrrpIntf', header, rows)


    def printXponderGlobalStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('XponderId')
            header.append('XponderMode')
            header.append('XponderDescription')

        objs = self.swtch.getAllXponderGlobalStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['XponderId'])
            values.append('%s' % o['XponderMode'])
            values.append('%s' % o['XponderDescription'])
            rows.append(values)
        self.tblPrintObject('XponderGlobalState', header, rows)


    def printXponderGlobalState(self, XponderId, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('XponderId')
            header.append('XponderMode')
            header.append('XponderDescription')

        rawobj = self.swtch.getXponderGlobalState(
                                                  XponderId)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['XponderId'])
            values.append('%s' % o['XponderMode'])
            values.append('%s' % o['XponderDescription'])
            rows.append(values)
            self.tblPrintObject('XponderGlobalState', header, rows)

        else:
            print rawobj.content

    def printCombinedXponderGlobalStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('XponderId')
            header.append('XponderMode')
            header.append('XponderDescription')

        objs = self.swtch.getAllXponderGlobalStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['XponderId'])
            values.append('%s' % o['XponderMode'])
            values.append('%s' % o['XponderDescription'])
            r = self.swtch.getXponderGlobal(o['XponderId'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
            rows.append(values)
        self.tblPrintObject('XponderGlobalState', header, rows)


    def printLLDPGlobals(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Vrf')
            header.append('TxRxMode')
            header.append('SnoopAndDrop')
            header.append('Enable')
            header.append('TranmitInterval')

        objs = self.swtch.getAllLLDPGlobals()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Vrf'])
            values.append('%s' % o['TxRxMode'])
            values.append('%s' % o['SnoopAndDrop'])
            values.append('%s' % o['Enable'])
            values.append('%s' % o['TranmitInterval'])
            rows.append(values)
        self.tblPrintObject('LLDPGlobal', header, rows)


    def printIPv6RouteHwStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('DestinationNw')
            header.append('NextHopIps')
            header.append('RouteCreatedTime')
            header.append('RouteUpdatedTime')

        objs = self.swtch.getAllIPv6RouteHwStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['DestinationNw'])
            values.append('%s' % o['NextHopIps'])
            values.append('%s' % o['RouteCreatedTime'])
            values.append('%s' % o['RouteUpdatedTime'])
            rows.append(values)
        self.tblPrintObject('IPv6RouteHwState', header, rows)


    def printIPv6RouteHwState(self, DestinationNw, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('DestinationNw')
            header.append('NextHopIps')
            header.append('RouteCreatedTime')
            header.append('RouteUpdatedTime')

        rawobj = self.swtch.getIPv6RouteHwState(
                                                DestinationNw)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['DestinationNw'])
            values.append('%s' % o['NextHopIps'])
            values.append('%s' % o['RouteCreatedTime'])
            values.append('%s' % o['RouteUpdatedTime'])
            rows.append(values)
            self.tblPrintObject('IPv6RouteHwState', header, rows)

        else:
            print rawobj.content

    def printSubIPv4Intfs(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('IpAddr')
            header.append('Type')
            header.append('MacAddr')
            header.append('Enable')

        objs = self.swtch.getAllSubIPv4Intfs()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['IpAddr'])
            values.append('%s' % o['Type'])
            values.append('%s' % o['MacAddr'])
            values.append('%s' % o['Enable'])
            rows.append(values)
        self.tblPrintObject('SubIPv4Intf', header, rows)


    def printSfpStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('SfpId')
            header.append('SfpSpeed')
            header.append('SfpLOS')
            header.append('SfpPresent')
            header.append('SfpType')
            header.append('SerialNum')
            header.append('EEPROM')

        objs = self.swtch.getAllSfpStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['SfpId'])
            values.append('%s' % o['SfpSpeed'])
            values.append('%s' % o['SfpLOS'])
            values.append('%s' % o['SfpPresent'])
            values.append('%s' % o['SfpType'])
            values.append('%s' % o['SerialNum'])
            values.append('%s' % o['EEPROM'])
            rows.append(values)
        self.tblPrintObject('SfpState', header, rows)


    def printSfpState(self, SfpId, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('SfpId')
            header.append('SfpSpeed')
            header.append('SfpLOS')
            header.append('SfpPresent')
            header.append('SfpType')
            header.append('SerialNum')
            header.append('EEPROM')

        rawobj = self.swtch.getSfpState(
                                        SfpId)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['SfpId'])
            values.append('%s' % o['SfpSpeed'])
            values.append('%s' % o['SfpLOS'])
            values.append('%s' % o['SfpPresent'])
            values.append('%s' % o['SfpType'])
            values.append('%s' % o['SerialNum'])
            values.append('%s' % o['EEPROM'])
            rows.append(values)
            self.tblPrintObject('SfpState', header, rows)

        else:
            print rawobj.content

    def printCombinedSfpStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('SfpId')
            header.append('SfpSpeed')
            header.append('SfpLOS')
            header.append('SfpPresent')
            header.append('SfpType')
            header.append('SerialNum')
            header.append('EEPROM')
            header.append('AdminState')

        objs = self.swtch.getAllSfpStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['SfpId'])
            values.append('%s' % o['SfpSpeed'])
            values.append('%s' % o['SfpLOS'])
            values.append('%s' % o['SfpPresent'])
            values.append('%s' % o['SfpType'])
            values.append('%s' % o['SerialNum'])
            values.append('%s' % o['EEPROM'])
            r = self.swtch.getSfp(o['SfpId'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
                values.append('%s' % o['AdminState'])
            rows.append(values)
        self.tblPrintObject('SfpState', header, rows)


    def printPolicyDefinitionStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('IpPrefixList')

        objs = self.swtch.getAllPolicyDefinitionStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['IpPrefixList'])
            rows.append(values)
        self.tblPrintObject('PolicyDefinitionState', header, rows)


    def printPolicyDefinitionState(self, Name, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('IpPrefixList')

        rawobj = self.swtch.getPolicyDefinitionState(
                                                     Name)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['IpPrefixList'])
            rows.append(values)
            self.tblPrintObject('PolicyDefinitionState', header, rows)

        else:
            print rawobj.content

    def printCombinedPolicyDefinitionStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('IpPrefixList')
            header.append('Priority')
            header.append('StatementList')
            header.append('MatchType')
            header.append('PolicyType')

        objs = self.swtch.getAllPolicyDefinitionStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['IpPrefixList'])
            r = self.swtch.getPolicyDefinition(o['Name'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
                values.append('%s' % o['Priority'])
                values.append('%s' % o['StatementList'])
                values.append('%s' % o['MatchType'])
                values.append('%s' % o['PolicyType'])
            rows.append(values)
        self.tblPrintObject('PolicyDefinitionState', header, rows)


    def printVlanStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('VlanId')
            header.append('VlanName')
            header.append('OperState')
            header.append('IfIndex')
            header.append('SysInternalDescription')

        objs = self.swtch.getAllVlanStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['VlanId'])
            values.append('%s' % o['VlanName'])
            values.append('%s' % o['OperState'])
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['SysInternalDescription'])
            rows.append(values)
        self.tblPrintObject('VlanState', header, rows)


    def printVlanState(self, VlanId, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('VlanId')
            header.append('VlanName')
            header.append('OperState')
            header.append('IfIndex')
            header.append('SysInternalDescription')

        rawobj = self.swtch.getVlanState(
                                         VlanId)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['VlanId'])
            values.append('%s' % o['VlanName'])
            values.append('%s' % o['OperState'])
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['SysInternalDescription'])
            rows.append(values)
            self.tblPrintObject('VlanState', header, rows)

        else:
            print rawobj.content

    def printCombinedVlanStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('VlanId')
            header.append('VlanName')
            header.append('OperState')
            header.append('IfIndex')
            #header.append('SysInternalDescription')
            header.append('IntfList')
            header.append('UntagIntfList')
            #header.append('AdminState')

        objs = self.swtch.getAllVlanStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['VlanId'])
            values.append('%s' % o['VlanName'])
            values.append('%s' % o['OperState'])
            values.append('%s' % o['IfIndex'])
            #values.append('%s' % o['SysInternalDescription'])
            r = self.swtch.getVlan(o['VlanId'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
                values.append('%s' % o['IntfList'])
                values.append('%s' % o['UntagIntfList'])
                #values.append('%s' % o['AdminState'])
            rows.append(values)
        var = self.tblPrintObject('VlanState', header, rows)
        return var

    def printIsisGlobalStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Vrf')
            header.append('Enable')

        objs = self.swtch.getAllIsisGlobalStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Vrf'])
            values.append('%s' % o['Enable'])
            rows.append(values)
        self.tblPrintObject('IsisGlobalState', header, rows)


    def printIsisGlobalState(self, Vrf, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Vrf')
            header.append('Enable')

        rawobj = self.swtch.getIsisGlobalState(
                                               Vrf)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['Vrf'])
            values.append('%s' % o['Enable'])
            rows.append(values)
            self.tblPrintObject('IsisGlobalState', header, rows)

        else:
            print rawobj.content

    def printCombinedIsisGlobalStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Vrf')
            header.append('Enable')

        objs = self.swtch.getAllIsisGlobalStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Vrf'])
            values.append('%s' % o['Enable'])
            r = self.swtch.getIsisGlobal(o['Vrf'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
            rows.append(values)
        self.tblPrintObject('IsisGlobalState', header, rows)


    def printLogicalIntfStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('IfIndex')
            header.append('SrcMac')
            header.append('OperState')
            header.append('IfInOctets')
            header.append('IfInUcastPkts')
            header.append('IfInDiscards')
            header.append('IfInErrors')
            header.append('IfInUnknownProtos')
            header.append('IfOutOctets')
            header.append('IfOutUcastPkts')
            header.append('IfOutDiscards')
            header.append('IfOutErrors')

        objs = self.swtch.getAllLogicalIntfStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['SrcMac'])
            values.append('%s' % o['OperState'])
            values.append('%s' % o['IfInOctets'])
            values.append('%s' % o['IfInUcastPkts'])
            values.append('%s' % o['IfInDiscards'])
            values.append('%s' % o['IfInErrors'])
            values.append('%s' % o['IfInUnknownProtos'])
            values.append('%s' % o['IfOutOctets'])
            values.append('%s' % o['IfOutUcastPkts'])
            values.append('%s' % o['IfOutDiscards'])
            values.append('%s' % o['IfOutErrors'])
            rows.append(values)
        self.tblPrintObject('LogicalIntfState', header, rows)


    def printLogicalIntfState(self, Name, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('IfIndex')
            header.append('SrcMac')
            header.append('OperState')
            header.append('IfInOctets')
            header.append('IfInUcastPkts')
            header.append('IfInDiscards')
            header.append('IfInErrors')
            header.append('IfInUnknownProtos')
            header.append('IfOutOctets')
            header.append('IfOutUcastPkts')
            header.append('IfOutDiscards')
            header.append('IfOutErrors')

        rawobj = self.swtch.getLogicalIntfState(
                                                Name)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['SrcMac'])
            values.append('%s' % o['OperState'])
            values.append('%s' % o['IfInOctets'])
            values.append('%s' % o['IfInUcastPkts'])
            values.append('%s' % o['IfInDiscards'])
            values.append('%s' % o['IfInErrors'])
            values.append('%s' % o['IfInUnknownProtos'])
            values.append('%s' % o['IfOutOctets'])
            values.append('%s' % o['IfOutUcastPkts'])
            values.append('%s' % o['IfOutDiscards'])
            values.append('%s' % o['IfOutErrors'])
            rows.append(values)
            self.tblPrintObject('LogicalIntfState', header, rows)

        else:
            print rawobj.content

    def printCombinedLogicalIntfStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('IfIndex')
            header.append('SrcMac')
            header.append('OperState')
            header.append('IfInOctets')
            header.append('IfInUcastPkts')
            header.append('IfInDiscards')
            header.append('IfInErrors')
            header.append('IfInUnknownProtos')
            header.append('IfOutOctets')
            header.append('IfOutUcastPkts')
            header.append('IfOutDiscards')
            header.append('IfOutErrors')
            header.append('Type')

        objs = self.swtch.getAllLogicalIntfStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['SrcMac'])
            values.append('%s' % o['OperState'])
            values.append('%s' % o['IfInOctets'])
            values.append('%s' % o['IfInUcastPkts'])
            values.append('%s' % o['IfInDiscards'])
            values.append('%s' % o['IfInErrors'])
            values.append('%s' % o['IfInUnknownProtos'])
            values.append('%s' % o['IfOutOctets'])
            values.append('%s' % o['IfOutUcastPkts'])
            values.append('%s' % o['IfOutDiscards'])
            values.append('%s' % o['IfOutErrors'])
            r = self.swtch.getLogicalIntf(o['Name'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
                values.append('%s' % o['Type'])
            rows.append(values)
        self.tblPrintObject('LogicalIntfState', header, rows)


    def printBGPv6Aggregates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IpPrefix')
            header.append('SendSummaryOnly')
            header.append('GenerateASSet')

        objs = self.swtch.getAllBGPv6Aggregates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IpPrefix'])
            values.append('%s' % o['SendSummaryOnly'])
            values.append('%s' % o['GenerateASSet'])
            rows.append(values)
        self.tblPrintObject('BGPv6Aggregate', header, rows)


    def printThermalStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('ThermalId')
            header.append('Location')
            header.append('Temperature')
            header.append('LowerWatermarkTemperature')
            header.append('UpperWatermarkTemperature')
            header.append('ShutdownTemperature')

        objs = self.swtch.getAllThermalStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['ThermalId'])
            values.append('%s' % o['Location'])
            values.append('%s' % o['Temperature'])
            values.append('%s' % o['LowerWatermarkTemperature'])
            values.append('%s' % o['UpperWatermarkTemperature'])
            values.append('%s' % o['ShutdownTemperature'])
            rows.append(values)
        self.tblPrintObject('ThermalState', header, rows)


    def printThermalState(self, ThermalId, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('ThermalId')
            header.append('Location')
            header.append('Temperature')
            header.append('LowerWatermarkTemperature')
            header.append('UpperWatermarkTemperature')
            header.append('ShutdownTemperature')

        rawobj = self.swtch.getThermalState(
                                            ThermalId)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['ThermalId'])
            values.append('%s' % o['Location'])
            values.append('%s' % o['Temperature'])
            values.append('%s' % o['LowerWatermarkTemperature'])
            values.append('%s' % o['UpperWatermarkTemperature'])
            values.append('%s' % o['ShutdownTemperature'])
            rows.append(values)
            self.tblPrintObject('ThermalState', header, rows)

        else:
            print rawobj.content

    def printPolicyPrefixSets(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('PrefixList')

        objs = self.swtch.getAllPolicyPrefixSets()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['PrefixList'])
            rows.append(values)
        self.tblPrintObject('PolicyPrefixSet', header, rows)


    def printLinkScopeIpStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('LinkScopeIp')
            header.append('IntfRef')
            header.append('IfIndex')
            header.append('Used')

        objs = self.swtch.getAllLinkScopeIpStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['LinkScopeIp'])
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['Used'])
            rows.append(values)
        self.tblPrintObject('LinkScopeIpState', header, rows)


    def printLinkScopeIpState(self, LinkScopeIp, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('LinkScopeIp')
            header.append('IntfRef')
            header.append('IfIndex')
            header.append('Used')

        rawobj = self.swtch.getLinkScopeIpState(
                                                LinkScopeIp)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['LinkScopeIp'])
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['Used'])
            rows.append(values)
            self.tblPrintObject('LinkScopeIpState', header, rows)

        else:
            print rawobj.content

    def printStpBridgeInstances(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Vlan')
            header.append('HelloTime')
            header.append('ForwardDelay')
            header.append('MaxAge')
            header.append('TxHoldCount')
            header.append('Priority')
            header.append('ForceVersion')
            header.append('Address')

        objs = self.swtch.getAllStpBridgeInstances()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Vlan'])
            values.append('%s' % o['HelloTime'])
            values.append('%s' % o['ForwardDelay'])
            values.append('%s' % o['MaxAge'])
            values.append('%s' % o['TxHoldCount'])
            values.append('%s' % o['Priority'])
            values.append('%s' % o['ForceVersion'])
            values.append('%s' % o['Address'])
            rows.append(values)
        self.tblPrintObject('StpBridgeInstance', header, rows)


    def printOspfVirtIfEntrys(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('VirtIfNeighbor')
            header.append('VirtIfAreaId')
            header.append('VirtIfTransitDelay')
            header.append('VirtIfRetransInterval')
            header.append('VirtIfHelloInterval')
            header.append('VirtIfRtrDeadInterval')
            header.append('VirtIfAuthKey')
            header.append('VirtIfAuthType')

        objs = self.swtch.getAllOspfVirtIfEntrys()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['VirtIfNeighbor'])
            values.append('%s' % o['VirtIfAreaId'])
            values.append('%s' % o['VirtIfTransitDelay'])
            values.append('%s' % o['VirtIfRetransInterval'])
            values.append('%s' % o['VirtIfHelloInterval'])
            values.append('%s' % o['VirtIfRtrDeadInterval'])
            values.append('%s' % o['VirtIfAuthKey'])
            values.append('%s' % o['VirtIfAuthType'])
            rows.append(values)
        self.tblPrintObject('OspfVirtIfEntry', header, rows)


    def printStpBridgeInstanceStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Vlan')
            header.append('IfIndex')
            header.append('Address')
            header.append('Priority')
            header.append('ProtocolSpecification')
            header.append('TimeSinceTopologyChange')
            header.append('TopChanges')
            header.append('DesignatedRoot')
            header.append('RootCost')
            header.append('RootPort')
            header.append('MaxAge')
            header.append('HelloTime')
            header.append('HoldTime')
            header.append('ForwardDelay')
            header.append('BridgeMaxAge')
            header.append('BridgeHelloTime')
            header.append('BridgeHoldTime')
            header.append('BridgeForwardDelay')
            header.append('TxHoldCount')

        objs = self.swtch.getAllStpBridgeInstanceStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Vlan'])
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['Address'])
            values.append('%s' % o['Priority'])
            values.append('%s' % o['ProtocolSpecification'])
            values.append('%s' % o['TimeSinceTopologyChange'])
            values.append('%s' % o['TopChanges'])
            values.append('%s' % o['DesignatedRoot'])
            values.append('%s' % o['RootCost'])
            values.append('%s' % o['RootPort'])
            values.append('%s' % o['MaxAge'])
            values.append('%s' % o['HelloTime'])
            values.append('%s' % o['HoldTime'])
            values.append('%s' % o['ForwardDelay'])
            values.append('%s' % o['BridgeMaxAge'])
            values.append('%s' % o['BridgeHelloTime'])
            values.append('%s' % o['BridgeHoldTime'])
            values.append('%s' % o['BridgeForwardDelay'])
            values.append('%s' % o['TxHoldCount'])
            rows.append(values)
        self.tblPrintObject('StpBridgeInstanceState', header, rows)


    def printStpBridgeInstanceState(self, Vlan, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Vlan')
            header.append('IfIndex')
            header.append('Address')
            header.append('Priority')
            header.append('ProtocolSpecification')
            header.append('TimeSinceTopologyChange')
            header.append('TopChanges')
            header.append('DesignatedRoot')
            header.append('RootCost')
            header.append('RootPort')
            header.append('MaxAge')
            header.append('HelloTime')
            header.append('HoldTime')
            header.append('ForwardDelay')
            header.append('BridgeMaxAge')
            header.append('BridgeHelloTime')
            header.append('BridgeHoldTime')
            header.append('BridgeForwardDelay')
            header.append('TxHoldCount')

        rawobj = self.swtch.getStpBridgeInstanceState(
                                                      Vlan)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['Vlan'])
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['Address'])
            values.append('%s' % o['Priority'])
            values.append('%s' % o['ProtocolSpecification'])
            values.append('%s' % o['TimeSinceTopologyChange'])
            values.append('%s' % o['TopChanges'])
            values.append('%s' % o['DesignatedRoot'])
            values.append('%s' % o['RootCost'])
            values.append('%s' % o['RootPort'])
            values.append('%s' % o['MaxAge'])
            values.append('%s' % o['HelloTime'])
            values.append('%s' % o['HoldTime'])
            values.append('%s' % o['ForwardDelay'])
            values.append('%s' % o['BridgeMaxAge'])
            values.append('%s' % o['BridgeHelloTime'])
            values.append('%s' % o['BridgeHoldTime'])
            values.append('%s' % o['BridgeForwardDelay'])
            values.append('%s' % o['TxHoldCount'])
            rows.append(values)
            self.tblPrintObject('StpBridgeInstanceState', header, rows)

        else:
            print rawobj.content

    def printCombinedStpBridgeInstanceStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Vlan')
            header.append('IfIndex')
            header.append('Address')
            header.append('Priority')
            header.append('ProtocolSpecification')
            header.append('TimeSinceTopologyChange')
            header.append('TopChanges')
            header.append('DesignatedRoot')
            header.append('RootCost')
            header.append('RootPort')
            header.append('MaxAge')
            header.append('HelloTime')
            header.append('HoldTime')
            header.append('ForwardDelay')
            header.append('BridgeMaxAge')
            header.append('BridgeHelloTime')
            header.append('BridgeHoldTime')
            header.append('BridgeForwardDelay')
            header.append('TxHoldCount')
            header.append('ForceVersion')

        objs = self.swtch.getAllStpBridgeInstanceStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Vlan'])
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['Address'])
            values.append('%s' % o['Priority'])
            values.append('%s' % o['ProtocolSpecification'])
            values.append('%s' % o['TimeSinceTopologyChange'])
            values.append('%s' % o['TopChanges'])
            values.append('%s' % o['DesignatedRoot'])
            values.append('%s' % o['RootCost'])
            values.append('%s' % o['RootPort'])
            values.append('%s' % o['MaxAge'])
            values.append('%s' % o['HelloTime'])
            values.append('%s' % o['HoldTime'])
            values.append('%s' % o['ForwardDelay'])
            values.append('%s' % o['BridgeMaxAge'])
            values.append('%s' % o['BridgeHelloTime'])
            values.append('%s' % o['BridgeHoldTime'])
            values.append('%s' % o['BridgeForwardDelay'])
            values.append('%s' % o['TxHoldCount'])
            r = self.swtch.getStpBridgeInstance(o['Vlan'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
                values.append('%s' % o['ForceVersion'])
            rows.append(values)
        self.tblPrintObject('StpBridgeInstanceState', header, rows)


    def printAsicSummaryStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('ModuleId')
            header.append('NumPortsUp')
            header.append('NumPortsDown')
            header.append('NumVlans')
            header.append('NumV4Intfs')
            header.append('NumV6Intfs')
            header.append('NumV4Adjs')
            header.append('NumV6Adjs')
            header.append('NumV4Routes')
            header.append('NumV6Routes')
            header.append('NumECMPRoutes')

        objs = self.swtch.getAllAsicSummaryStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['ModuleId'])
            values.append('%s' % o['NumPortsUp'])
            values.append('%s' % o['NumPortsDown'])
            values.append('%s' % o['NumVlans'])
            values.append('%s' % o['NumV4Intfs'])
            values.append('%s' % o['NumV6Intfs'])
            values.append('%s' % o['NumV4Adjs'])
            values.append('%s' % o['NumV6Adjs'])
            values.append('%s' % o['NumV4Routes'])
            values.append('%s' % o['NumV6Routes'])
            values.append('%s' % o['NumECMPRoutes'])
            rows.append(values)
        self.tblPrintObject('AsicSummaryState', header, rows)


    def printAsicSummaryState(self, ModuleId, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('ModuleId')
            header.append('NumPortsUp')
            header.append('NumPortsDown')
            header.append('NumVlans')
            header.append('NumV4Intfs')
            header.append('NumV6Intfs')
            header.append('NumV4Adjs')
            header.append('NumV6Adjs')
            header.append('NumV4Routes')
            header.append('NumV6Routes')
            header.append('NumECMPRoutes')

        rawobj = self.swtch.getAsicSummaryState(
                                                ModuleId)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['ModuleId'])
            values.append('%s' % o['NumPortsUp'])
            values.append('%s' % o['NumPortsDown'])
            values.append('%s' % o['NumVlans'])
            values.append('%s' % o['NumV4Intfs'])
            values.append('%s' % o['NumV6Intfs'])
            values.append('%s' % o['NumV4Adjs'])
            values.append('%s' % o['NumV6Adjs'])
            values.append('%s' % o['NumV4Routes'])
            values.append('%s' % o['NumV6Routes'])
            values.append('%s' % o['NumECMPRoutes'])
            rows.append(values)
            self.tblPrintObject('AsicSummaryState', header, rows)

        else:
            print rawobj.content

    def printBGPPolicyActionStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('ActionInfo')
            header.append('PolicyStmtList')

        objs = self.swtch.getAllBGPPolicyActionStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['ActionInfo'])
            values.append('%s' % o['PolicyStmtList'])
            rows.append(values)
        self.tblPrintObject('BGPPolicyActionState', header, rows)


    def printBGPPolicyActionState(self, Name, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('ActionInfo')
            header.append('PolicyStmtList')

        rawobj = self.swtch.getBGPPolicyActionState(
                                                    Name)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['ActionInfo'])
            values.append('%s' % o['PolicyStmtList'])
            rows.append(values)
            self.tblPrintObject('BGPPolicyActionState', header, rows)

        else:
            print rawobj.content

    def printCombinedBGPPolicyActionStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('ActionInfo')
            header.append('PolicyStmtList')
            header.append('ActionType')
            header.append('GenerateASSet')
            header.append('SendSummaryOnly')

        objs = self.swtch.getAllBGPPolicyActionStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['ActionInfo'])
            values.append('%s' % o['PolicyStmtList'])
            r = self.swtch.getBGPPolicyAction(o['Name'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
                values.append('%s' % o['ActionType'])
                values.append('%s' % o['GenerateASSet'])
                values.append('%s' % o['SendSummaryOnly'])
            rows.append(values)
        self.tblPrintObject('BGPPolicyActionState', header, rows)


    def printVxlanInstances(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Vni')
            header.append('VlanId')

        objs = self.swtch.getAllVxlanInstances()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Vni'])
            values.append('%s' % o['VlanId'])
            rows.append(values)
        self.tblPrintObject('VxlanInstance', header, rows)


    def printBGPPolicyDefinitionStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('HitCounter')
            header.append('IpPrefixList')

        objs = self.swtch.getAllBGPPolicyDefinitionStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['HitCounter'])
            values.append('%s' % o['IpPrefixList'])
            rows.append(values)
        self.tblPrintObject('BGPPolicyDefinitionState', header, rows)


    def printBGPPolicyDefinitionState(self, Name, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('HitCounter')
            header.append('IpPrefixList')

        rawobj = self.swtch.getBGPPolicyDefinitionState(
                                                        Name)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['HitCounter'])
            values.append('%s' % o['IpPrefixList'])
            rows.append(values)
            self.tblPrintObject('BGPPolicyDefinitionState', header, rows)

        else:
            print rawobj.content

    def printCombinedBGPPolicyDefinitionStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('HitCounter')
            header.append('IpPrefixList')
            header.append('Precedence')
            header.append('MatchType')
            header.append('StatementList')

        objs = self.swtch.getAllBGPPolicyDefinitionStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['HitCounter'])
            values.append('%s' % o['IpPrefixList'])
            r = self.swtch.getBGPPolicyDefinition(o['Name'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
                values.append('%s' % o['Precedence'])
                values.append('%s' % o['MatchType'])
                values.append('%s' % o['StatementList'])
            rows.append(values)
        self.tblPrintObject('BGPPolicyDefinitionState', header, rows)


    def printLedStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('LedId')
            header.append('LedIdentify')
            header.append('LedState')
            header.append('LedColor')

        objs = self.swtch.getAllLedStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['LedId'])
            values.append('%s' % o['LedIdentify'])
            values.append('%s' % o['LedState'])
            values.append('%s' % o['LedColor'])
            rows.append(values)
        self.tblPrintObject('LedState', header, rows)


    def printLedState(self, LedId, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('LedId')
            header.append('LedIdentify')
            header.append('LedState')
            header.append('LedColor')

        rawobj = self.swtch.getLedState(
                                        LedId)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['LedId'])
            values.append('%s' % o['LedIdentify'])
            values.append('%s' % o['LedState'])
            values.append('%s' % o['LedColor'])
            rows.append(values)
            self.tblPrintObject('LedState', header, rows)

        else:
            print rawobj.content

    def printCombinedLedStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('LedId')
            header.append('LedIdentify')
            header.append('LedState')
            header.append('LedColor')
            header.append('LedAdmin')
            header.append('LedSetColor')

        objs = self.swtch.getAllLedStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['LedId'])
            values.append('%s' % o['LedIdentify'])
            values.append('%s' % o['LedState'])
            values.append('%s' % o['LedColor'])
            r = self.swtch.getLed(o['LedId'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
                values.append('%s' % o['LedAdmin'])
                values.append('%s' % o['LedSetColor'])
            rows.append(values)
        self.tblPrintObject('LedState', header, rows)


    def printIPv4IntfStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('IfIndex')
            header.append('IpAddr')
            header.append('OperState')
            header.append('NumUpEvents')
            header.append('LastUpEventTime')
            header.append('NumDownEvents')
            header.append('LastDownEventTime')
            header.append('L2IntfType')
            header.append('L2IntfId')

        objs = self.swtch.getAllIPv4IntfStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['IpAddr'])
            values.append('%s' % o['OperState'])
            values.append('%s' % o['NumUpEvents'])
            values.append('%s' % o['LastUpEventTime'])
            values.append('%s' % o['NumDownEvents'])
            values.append('%s' % o['LastDownEventTime'])
            values.append('%s' % o['L2IntfType'])
            values.append('%s' % o['L2IntfId'])
            rows.append(values)
        var = self.tblPrintObject('IPv4IntfState', header, rows)
        return var

    def printIPv4IntfState(self, IntfRef, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('IfIndex')
            header.append('IpAddr')
            header.append('OperState')
            header.append('NumUpEvents')
            header.append('LastUpEventTime')
            header.append('NumDownEvents')
            header.append('LastDownEventTime')
            header.append('L2IntfType')
            header.append('L2IntfId')

        rawobj = self.swtch.getIPv4IntfState(
                                             IntfRef)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['IpAddr'])
            values.append('%s' % o['OperState'])
            values.append('%s' % o['NumUpEvents'])
            values.append('%s' % o['LastUpEventTime'])
            values.append('%s' % o['NumDownEvents'])
            values.append('%s' % o['LastDownEventTime'])
            values.append('%s' % o['L2IntfType'])
            values.append('%s' % o['L2IntfId'])
            rows.append(values)
            self.tblPrintObject('IPv4IntfState', header, rows)

        else:
            print rawobj.content

    def printCombinedIPv4IntfStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('IfIndex')
            header.append('IpAddr')
            header.append('OperState')
            header.append('NumUpEvents')
            header.append('LastUpEventTime')
            header.append('NumDownEvents')
            header.append('LastDownEventTime')
            header.append('L2IntfType')
            header.append('L2IntfId')
            header.append('AdminState')

        objs = self.swtch.getAllIPv4IntfStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['IpAddr'])
            values.append('%s' % o['OperState'])
            values.append('%s' % o['NumUpEvents'])
            values.append('%s' % o['LastUpEventTime'])
            values.append('%s' % o['NumDownEvents'])
            values.append('%s' % o['LastDownEventTime'])
            values.append('%s' % o['L2IntfType'])
            values.append('%s' % o['L2IntfId'])
            r = self.swtch.getIPv4Intf(o['IntfRef'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
                values.append('%s' % o['AdminState'])
            rows.append(values)
        self.tblPrintObject('IPv4IntfState', header, rows)


    def printPortStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('IfIndex')
            header.append('Name')
            header.append('OperState')
            header.append('NumUpEvents')
            header.append('LastUpEventTime')
            header.append('NumDownEvents')
            header.append('LastDownEventTime')
            header.append('Pvid')
            header.append('IfInOctets')
            header.append('IfInUcastPkts')
            header.append('IfInDiscards')
            header.append('IfInErrors')
            header.append('IfInUnknownProtos')
            header.append('IfOutOctets')
            header.append('IfOutUcastPkts')
            header.append('IfOutDiscards')
            header.append('IfOutErrors')
            header.append('IfEtherUnderSizePktCnt')
            header.append('IfEtherOverSizePktCnt')
            header.append('IfEtherFragments')
            header.append('IfEtherCRCAlignError')
            header.append('IfEtherJabber')
            header.append('IfEtherPkts')
            header.append('IfEtherMCPkts')
            header.append('IfEtherBcastPkts')
            header.append('IfEtherPkts64OrLessOctets')
            header.append('IfEtherPkts65To127Octets')
            header.append('IfEtherPkts128To255Octets')
            header.append('IfEtherPkts256To511Octets')
            header.append('IfEtherPkts512To1023Octets')
            header.append('IfEtherPkts1024To1518Octets')
            header.append('ErrDisableReason')
            header.append('PresentInHW')
            header.append('ConfigMode')
            header.append('PRBSRxErrCnt')

        objs = self.swtch.getAllPortStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['Name'])
            values.append('%s' % o['OperState'])
            values.append('%s' % o['NumUpEvents'])
            values.append('%s' % o['LastUpEventTime'])
            values.append('%s' % o['NumDownEvents'])
            values.append('%s' % o['LastDownEventTime'])
            values.append('%s' % o['Pvid'])
            values.append('%s' % o['IfInOctets'])
            values.append('%s' % o['IfInUcastPkts'])
            values.append('%s' % o['IfInDiscards'])
            values.append('%s' % o['IfInErrors'])
            values.append('%s' % o['IfInUnknownProtos'])
            values.append('%s' % o['IfOutOctets'])
            values.append('%s' % o['IfOutUcastPkts'])
            values.append('%s' % o['IfOutDiscards'])
            values.append('%s' % o['IfOutErrors'])
            values.append('%s' % o['IfEtherUnderSizePktCnt'])
            values.append('%s' % o['IfEtherOverSizePktCnt'])
            values.append('%s' % o['IfEtherFragments'])
            values.append('%s' % o['IfEtherCRCAlignError'])
            values.append('%s' % o['IfEtherJabber'])
            values.append('%s' % o['IfEtherPkts'])
            values.append('%s' % o['IfEtherMCPkts'])
            values.append('%s' % o['IfEtherBcastPkts'])
            values.append('%s' % o['IfEtherPkts64OrLessOctets'])
            values.append('%s' % o['IfEtherPkts65To127Octets'])
            values.append('%s' % o['IfEtherPkts128To255Octets'])
            values.append('%s' % o['IfEtherPkts256To511Octets'])
            values.append('%s' % o['IfEtherPkts512To1023Octets'])
            values.append('%s' % o['IfEtherPkts1024To1518Octets'])
            values.append('%s' % o['ErrDisableReason'])
            values.append('%s' % o['PresentInHW'])
            values.append('%s' % o['ConfigMode'])
            values.append('%s' % o['PRBSRxErrCnt'])
            rows.append(values)
        self.tblPrintObject('PortState', header, rows)


    def printPortState(self, IntfRef, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('IfIndex')
            header.append('Name')
            header.append('OperState')
            header.append('NumUpEvents')
            header.append('LastUpEventTime')
            header.append('NumDownEvents')
            header.append('LastDownEventTime')
            header.append('Pvid')
            header.append('IfInOctets')
            header.append('IfInUcastPkts')
            header.append('IfInDiscards')
            header.append('IfInErrors')
            header.append('IfInUnknownProtos')
            header.append('IfOutOctets')
            header.append('IfOutUcastPkts')
            header.append('IfOutDiscards')
            header.append('IfOutErrors')
            header.append('IfEtherUnderSizePktCnt')
            header.append('IfEtherOverSizePktCnt')
            header.append('IfEtherFragments')
            header.append('IfEtherCRCAlignError')
            header.append('IfEtherJabber')
            header.append('IfEtherPkts')
            header.append('IfEtherMCPkts')
            header.append('IfEtherBcastPkts')
            header.append('IfEtherPkts64OrLessOctets')
            header.append('IfEtherPkts65To127Octets')
            header.append('IfEtherPkts128To255Octets')
            header.append('IfEtherPkts256To511Octets')
            header.append('IfEtherPkts512To1023Octets')
            header.append('IfEtherPkts1024To1518Octets')
            header.append('ErrDisableReason')
            header.append('PresentInHW')
            header.append('ConfigMode')
            header.append('PRBSRxErrCnt')

        rawobj = self.swtch.getPortState(
                                         IntfRef)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['Name'])
            values.append('%s' % o['OperState'])
            values.append('%s' % o['NumUpEvents'])
            values.append('%s' % o['LastUpEventTime'])
            values.append('%s' % o['NumDownEvents'])
            values.append('%s' % o['LastDownEventTime'])
            values.append('%s' % o['Pvid'])
            values.append('%s' % o['IfInOctets'])
            values.append('%s' % o['IfInUcastPkts'])
            values.append('%s' % o['IfInDiscards'])
            values.append('%s' % o['IfInErrors'])
            values.append('%s' % o['IfInUnknownProtos'])
            values.append('%s' % o['IfOutOctets'])
            values.append('%s' % o['IfOutUcastPkts'])
            values.append('%s' % o['IfOutDiscards'])
            values.append('%s' % o['IfOutErrors'])
            values.append('%s' % o['IfEtherUnderSizePktCnt'])
            values.append('%s' % o['IfEtherOverSizePktCnt'])
            values.append('%s' % o['IfEtherFragments'])
            values.append('%s' % o['IfEtherCRCAlignError'])
            values.append('%s' % o['IfEtherJabber'])
            values.append('%s' % o['IfEtherPkts'])
            values.append('%s' % o['IfEtherMCPkts'])
            values.append('%s' % o['IfEtherBcastPkts'])
            values.append('%s' % o['IfEtherPkts64OrLessOctets'])
            values.append('%s' % o['IfEtherPkts65To127Octets'])
            values.append('%s' % o['IfEtherPkts128To255Octets'])
            values.append('%s' % o['IfEtherPkts256To511Octets'])
            values.append('%s' % o['IfEtherPkts512To1023Octets'])
            values.append('%s' % o['IfEtherPkts1024To1518Octets'])
            values.append('%s' % o['ErrDisableReason'])
            values.append('%s' % o['PresentInHW'])
            values.append('%s' % o['ConfigMode'])
            values.append('%s' % o['PRBSRxErrCnt'])
            rows.append(values)
            self.tblPrintObject('PortState', header, rows)

        else:
            print rawobj.content

    def printCombinedPortStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('IfIndex')
            header.append('Name')
            header.append('OperState')
            header.append('NumUpEvents')
            header.append('LastUpEventTime')
            header.append('NumDownEvents')
            header.append('LastDownEventTime')
            header.append('Pvid')
            header.append('IfInOctets')
            header.append('IfInUcastPkts')
            header.append('IfInDiscards')
            header.append('IfInErrors')
            header.append('IfInUnknownProtos')
            header.append('IfOutOctets')
            header.append('IfOutUcastPkts')
            header.append('IfOutDiscards')
            header.append('IfOutErrors')
            header.append('IfEtherUnderSizePktCnt')
            header.append('IfEtherOverSizePktCnt')
            header.append('IfEtherFragments')
            header.append('IfEtherCRCAlignError')
            header.append('IfEtherJabber')
            header.append('IfEtherPkts')
            header.append('IfEtherMCPkts')
            header.append('IfEtherBcastPkts')
            header.append('IfEtherPkts64OrLessOctets')
            header.append('IfEtherPkts65To127Octets')
            header.append('IfEtherPkts128To255Octets')
            header.append('IfEtherPkts256To511Octets')
            header.append('IfEtherPkts512To1023Octets')
            header.append('IfEtherPkts1024To1518Octets')
            header.append('ErrDisableReason')
            header.append('PresentInHW')
            header.append('ConfigMode')
            header.append('PRBSRxErrCnt')
            header.append('PhyIntfType')
            header.append('MacAddr')
            header.append('Speed')
            header.append('MediaType')
            header.append('Mtu')
            header.append('BreakOutMode')
            header.append('PRBSRxEnable')
            header.append('Description')
            header.append('PRBSPolynomial')
            header.append('Duplex')
            header.append('LoopbackMode')
            header.append('EnableFEC')
            header.append('AdminState')
            header.append('Autoneg')
            header.append('PRBSTxEnable')

        objs = self.swtch.getAllPortStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['Name'])
            values.append('%s' % o['OperState'])
            values.append('%s' % o['NumUpEvents'])
            values.append('%s' % o['LastUpEventTime'])
            values.append('%s' % o['NumDownEvents'])
            values.append('%s' % o['LastDownEventTime'])
            values.append('%s' % o['Pvid'])
            values.append('%s' % o['IfInOctets'])
            values.append('%s' % o['IfInUcastPkts'])
            values.append('%s' % o['IfInDiscards'])
            values.append('%s' % o['IfInErrors'])
            values.append('%s' % o['IfInUnknownProtos'])
            values.append('%s' % o['IfOutOctets'])
            values.append('%s' % o['IfOutUcastPkts'])
            values.append('%s' % o['IfOutDiscards'])
            values.append('%s' % o['IfOutErrors'])
            values.append('%s' % o['IfEtherUnderSizePktCnt'])
            values.append('%s' % o['IfEtherOverSizePktCnt'])
            values.append('%s' % o['IfEtherFragments'])
            values.append('%s' % o['IfEtherCRCAlignError'])
            values.append('%s' % o['IfEtherJabber'])
            values.append('%s' % o['IfEtherPkts'])
            values.append('%s' % o['IfEtherMCPkts'])
            values.append('%s' % o['IfEtherBcastPkts'])
            values.append('%s' % o['IfEtherPkts64OrLessOctets'])
            values.append('%s' % o['IfEtherPkts65To127Octets'])
            values.append('%s' % o['IfEtherPkts128To255Octets'])
            values.append('%s' % o['IfEtherPkts256To511Octets'])
            values.append('%s' % o['IfEtherPkts512To1023Octets'])
            values.append('%s' % o['IfEtherPkts1024To1518Octets'])
            values.append('%s' % o['ErrDisableReason'])
            values.append('%s' % o['PresentInHW'])
            values.append('%s' % o['ConfigMode'])
            values.append('%s' % o['PRBSRxErrCnt'])
            r = self.swtch.getPort(o['IntfRef'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
                values.append('%s' % o['PhyIntfType'])
                values.append('%s' % o['MacAddr'])
                values.append('%s' % o['Speed'])
                values.append('%s' % o['MediaType'])
                values.append('%s' % o['Mtu'])
                values.append('%s' % o['BreakOutMode'])
                values.append('%s' % o['PRBSRxEnable'])
                values.append('%s' % o['Description'])
                values.append('%s' % o['PRBSPolynomial'])
                values.append('%s' % o['Duplex'])
                values.append('%s' % o['LoopbackMode'])
                values.append('%s' % o['EnableFEC'])
                values.append('%s' % o['AdminState'])
                values.append('%s' % o['Autoneg'])
                values.append('%s' % o['PRBSTxEnable'])
            rows.append(values)
        self.tblPrintObject('PortState', header, rows)


    def printSfps(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('SfpId')
            header.append('AdminState')

        objs = self.swtch.getAllSfps()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['SfpId'])
            values.append('%s' % o['AdminState'])
            rows.append(values)
        self.tblPrintObject('Sfp', header, rows)


    def printBGPPolicyActions(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('ActionType')
            header.append('GenerateASSet')
            header.append('SendSummaryOnly')

        objs = self.swtch.getAllBGPPolicyActions()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['ActionType'])
            values.append('%s' % o['GenerateASSet'])
            values.append('%s' % o['SendSummaryOnly'])
            rows.append(values)
        self.tblPrintObject('BGPPolicyAction', header, rows)


    def printSystemSwVersionStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('FlexswitchVersion')
            header.append('Repos')

        objs = self.swtch.getAllSystemSwVersionStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['FlexswitchVersion'])
            values.append('%s' % o['Repos'])
            rows.append(values)
        self.tblPrintObject('SystemSwVersionState', header, rows)


    def printSystemSwVersionState(self, FlexswitchVersion, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('FlexswitchVersion')
            header.append('Repos')

        rawobj = self.swtch.getSystemSwVersionState(
                                                    FlexswitchVersion)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['FlexswitchVersion'])
            values.append('%s' % o['Repos'])
            rows.append(values)
            self.tblPrintObject('SystemSwVersionState', header, rows)

        else:
            print rawobj.content

    def printDaemonStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('Enable')
            header.append('State')
            header.append('Reason')
            header.append('StartTime')
            header.append('KeepAlive')
            header.append('RestartCount')
            header.append('RestartTime')
            header.append('RestartReason')

        objs = self.swtch.getAllDaemonStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['Enable'])
            values.append('%s' % o['State'])
            values.append('%s' % o['Reason'])
            values.append('%s' % o['StartTime'])
            values.append('%s' % o['KeepAlive'])
            values.append('%s' % o['RestartCount'])
            values.append('%s' % o['RestartTime'])
            values.append('%s' % o['RestartReason'])
            rows.append(values)
        self.tblPrintObject('DaemonState', header, rows)


    def printDaemonState(self, Name, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('Enable')
            header.append('State')
            header.append('Reason')
            header.append('StartTime')
            header.append('KeepAlive')
            header.append('RestartCount')
            header.append('RestartTime')
            header.append('RestartReason')

        rawobj = self.swtch.getDaemonState(
                                           Name)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['Enable'])
            values.append('%s' % o['State'])
            values.append('%s' % o['Reason'])
            values.append('%s' % o['StartTime'])
            values.append('%s' % o['KeepAlive'])
            values.append('%s' % o['RestartCount'])
            values.append('%s' % o['RestartTime'])
            values.append('%s' % o['RestartReason'])
            rows.append(values)
            self.tblPrintObject('DaemonState', header, rows)

        else:
            print rawobj.content

    def printCombinedDaemonStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('Enable')
            header.append('State')
            header.append('Reason')
            header.append('StartTime')
            header.append('KeepAlive')
            header.append('RestartCount')
            header.append('RestartTime')
            header.append('RestartReason')
            header.append('WatchDog')

        objs = self.swtch.getAllDaemonStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['Enable'])
            values.append('%s' % o['State'])
            values.append('%s' % o['Reason'])
            values.append('%s' % o['StartTime'])
            values.append('%s' % o['KeepAlive'])
            values.append('%s' % o['RestartCount'])
            values.append('%s' % o['RestartTime'])
            values.append('%s' % o['RestartReason'])
            r = self.swtch.getDaemon(o['Name'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
                values.append('%s' % o['WatchDog'])
            rows.append(values)
        self.tblPrintObject('DaemonState', header, rows)


    def printSystemParamStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Vrf')
            header.append('MgmtIp')
            header.append('Hostname')
            header.append('SwitchMac')
            header.append('SwVersion')
            header.append('Description')
            header.append('Distro')
            header.append('Kernel')

        objs = self.swtch.getAllSystemParamStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Vrf'])
            values.append('%s' % o['MgmtIp'])
            values.append('%s' % o['Hostname'])
            values.append('%s' % o['SwitchMac'])
            values.append('%s' % o['SwVersion'])
            values.append('%s' % o['Description'])
            values.append('%s' % o['Distro'])
            values.append('%s' % o['Kernel'])
            rows.append(values)
        self.tblPrintObject('SystemParamState', header, rows)


    def printSystemParamState(self, Vrf, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Vrf')
            header.append('MgmtIp')
            header.append('Hostname')
            header.append('SwitchMac')
            header.append('SwVersion')
            header.append('Description')
            header.append('Distro')
            header.append('Kernel')

        rawobj = self.swtch.getSystemParamState(
                                                Vrf)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['Vrf'])
            values.append('%s' % o['MgmtIp'])
            values.append('%s' % o['Hostname'])
            values.append('%s' % o['SwitchMac'])
            values.append('%s' % o['SwVersion'])
            values.append('%s' % o['Description'])
            values.append('%s' % o['Distro'])
            values.append('%s' % o['Kernel'])
            rows.append(values)
            self.tblPrintObject('SystemParamState', header, rows)

        else:
            print rawobj.content

    def printCombinedSystemParamStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Vrf')
            header.append('MgmtIp')
            header.append('Hostname')
            header.append('SwitchMac')
            header.append('SwVersion')
            header.append('Description')
            header.append('Distro')
            header.append('Kernel')

        objs = self.swtch.getAllSystemParamStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Vrf'])
            values.append('%s' % o['MgmtIp'])
            values.append('%s' % o['Hostname'])
            values.append('%s' % o['SwitchMac'])
            values.append('%s' % o['SwVersion'])
            values.append('%s' % o['Description'])
            values.append('%s' % o['Distro'])
            values.append('%s' % o['Kernel'])
            r = self.swtch.getSystemParam(o['Vrf'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
            rows.append(values)
        self.tblPrintObject('SystemParamState', header, rows)


    def printVoltageSensorStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('CurrentVoltage')

        objs = self.swtch.getAllVoltageSensorStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['CurrentVoltage'])
            rows.append(values)
        self.tblPrintObject('VoltageSensorState', header, rows)


    def printVoltageSensorState(self, Name, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('CurrentVoltage')

        rawobj = self.swtch.getVoltageSensorState(
                                                  Name)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['CurrentVoltage'])
            rows.append(values)
            self.tblPrintObject('VoltageSensorState', header, rows)

        else:
            print rawobj.content

    def printCombinedVoltageSensorStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('CurrentVoltage')
            header.append('HigherAlarmThreshold')
            header.append('HigherWarningThreshold')
            header.append('LowerWarningThreshold')
            header.append('LowerAlarmThreshold')
            header.append('PMClassCAdminState')
            header.append('PMClassAAdminState')
            header.append('AdminState')
            header.append('PMClassBAdminState')

        objs = self.swtch.getAllVoltageSensorStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['CurrentVoltage'])
            r = self.swtch.getVoltageSensor(o['Name'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
                values.append('%s' % o['HigherAlarmThreshold'])
                values.append('%s' % o['HigherWarningThreshold'])
                values.append('%s' % o['LowerWarningThreshold'])
                values.append('%s' % o['LowerAlarmThreshold'])
                values.append('%s' % o['PMClassCAdminState'])
                values.append('%s' % o['PMClassAAdminState'])
                values.append('%s' % o['AdminState'])
                values.append('%s' % o['PMClassBAdminState'])
            rows.append(values)
        self.tblPrintObject('VoltageSensorState', header, rows)


    def printDWDMModuleNwIntfPMStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Resource')
            header.append('NwIntfId')
            header.append('Type')
            header.append('Class')
            header.append('ModuleId')
            header.append('Data')

        objs = self.swtch.getAllDWDMModuleNwIntfPMStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Resource'])
            values.append('%s' % o['NwIntfId'])
            values.append('%s' % o['Type'])
            values.append('%s' % o['Class'])
            values.append('%s' % o['ModuleId'])
            values.append('%s' % o['Data'])
            rows.append(values)
        self.tblPrintObject('DWDMModuleNwIntfPMState', header, rows)


    def printDWDMModuleNwIntfPMState(self, Resource,NwIntfId,Type,Class,ModuleId, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Resource')
            header.append('NwIntfId')
            header.append('Type')
            header.append('Class')
            header.append('ModuleId')
            header.append('Data')

        rawobj = self.swtch.getDWDMModuleNwIntfPMState(
                                                       Resource,
                                                       NwIntfId,
                                                       Type,
                                                       Class,
                                                       ModuleId)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['Resource'])
            values.append('%s' % o['NwIntfId'])
            values.append('%s' % o['Type'])
            values.append('%s' % o['Class'])
            values.append('%s' % o['ModuleId'])
            values.append('%s' % o['Data'])
            rows.append(values)
            self.tblPrintObject('DWDMModuleNwIntfPMState', header, rows)

        else:
            print rawobj.content

    def printDWDMModules(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('ModuleId')
            header.append('EnableExtPMTickSrc')
            header.append('PMInterval')
            header.append('AdminState')
            header.append('IndependentLaneMode')

        objs = self.swtch.getAllDWDMModules()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['ModuleId'])
            values.append('%s' % o['EnableExtPMTickSrc'])
            values.append('%s' % o['PMInterval'])
            values.append('%s' % o['AdminState'])
            values.append('%s' % o['IndependentLaneMode'])
            rows.append(values)
        self.tblPrintObject('DWDMModule', header, rows)


    def printAcls(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('AclName')
            header.append('Direction')
            header.append('AclType')
            header.append('IntfList')
            header.append('RuleNameList')

        objs = self.swtch.getAllAcls()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['AclName'])
            values.append('%s' % o['Direction'])
            values.append('%s' % o['AclType'])
            values.append('%s' % o['IntfList'])
            values.append('%s' % o['RuleNameList'])
            rows.append(values)
        self.tblPrintObject('Acl', header, rows)


    def printBGPv6Neighbors(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('NeighborAddress')
            header.append('Description')
            header.append('PeerGroup')
            header.append('PeerAS')
            header.append('LocalAS')
            header.append('UpdateSource')
            header.append('AdjRIBInFilter')
            header.append('AdjRIBOutFilter')
            header.append('BfdEnable')
            header.append('MultiHopTTL')
            header.append('KeepaliveTime')
            header.append('AddPathsRx')
            header.append('RouteReflectorClient')
            header.append('MaxPrefixesRestartTimer')
            header.append('MultiHopEnable')
            header.append('RouteReflectorClusterId')
            header.append('MaxPrefixesDisconnect')
            header.append('AddPathsMaxTx')
            header.append('MaxPrefixes')
            header.append('MaxPrefixesThresholdPct')
            header.append('BfdSessionParam')
            header.append('Disabled')
            header.append('HoldTime')
            header.append('ConnectRetryTime')

        objs = self.swtch.getAllBGPv6Neighbors()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['NeighborAddress'])
            values.append('%s' % o['Description'])
            values.append('%s' % o['PeerGroup'])
            values.append('%s' % o['PeerAS'])
            values.append('%s' % o['LocalAS'])
            values.append('%s' % o['UpdateSource'])
            values.append('%s' % o['AdjRIBInFilter'])
            values.append('%s' % o['AdjRIBOutFilter'])
            values.append('%s' % o['BfdEnable'])
            values.append('%s' % o['MultiHopTTL'])
            values.append('%s' % o['KeepaliveTime'])
            values.append('%s' % o['AddPathsRx'])
            values.append('%s' % o['RouteReflectorClient'])
            values.append('%s' % o['MaxPrefixesRestartTimer'])
            values.append('%s' % o['MultiHopEnable'])
            values.append('%s' % o['RouteReflectorClusterId'])
            values.append('%s' % o['MaxPrefixesDisconnect'])
            values.append('%s' % o['AddPathsMaxTx'])
            values.append('%s' % o['MaxPrefixes'])
            values.append('%s' % o['MaxPrefixesThresholdPct'])
            values.append('%s' % o['BfdSessionParam'])
            values.append('%s' % o['Disabled'])
            values.append('%s' % o['HoldTime'])
            values.append('%s' % o['ConnectRetryTime'])
            rows.append(values)
        self.tblPrintObject('BGPv6Neighbor', header, rows)


    def printStpPorts(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Vlan')
            header.append('IntfRef')
            header.append('PathCost')
            header.append('AdminEdgePort')
            header.append('ProtocolMigration')
            header.append('BridgeAssurance')
            header.append('Priority')
            header.append('AdminState')
            header.append('BpduGuard')
            header.append('AdminPointToPoint')
            header.append('BpduGuardInterval')
            header.append('AdminPathCost')
            header.append('PathCost32')

        objs = self.swtch.getAllStpPorts()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Vlan'])
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['PathCost'])
            values.append('%s' % o['AdminEdgePort'])
            values.append('%s' % o['ProtocolMigration'])
            values.append('%s' % o['BridgeAssurance'])
            values.append('%s' % o['Priority'])
            values.append('%s' % o['AdminState'])
            values.append('%s' % o['BpduGuard'])
            values.append('%s' % o['AdminPointToPoint'])
            values.append('%s' % o['BpduGuardInterval'])
            values.append('%s' % o['AdminPathCost'])
            values.append('%s' % o['PathCost32'])
            rows.append(values)
        self.tblPrintObject('StpPort', header, rows)


    def printIPv4Routes(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('DestinationNw')
            header.append('NetworkMask')
            header.append('NextHop')
            header.append('Protocol')
            header.append('NullRoute')
            header.append('Cost')

        objs = self.swtch.getAllIPv4Routes()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['DestinationNw'])
            values.append('%s' % o['NetworkMask'])
            values.append('%s' % o['NextHop'])
            values.append('%s' % o['Protocol'])
            values.append('%s' % o['NullRoute'])
            values.append('%s' % o['Cost'])
            rows.append(values)
        self.tblPrintObject('IPv4Route', header, rows)


    def printBGPv6PeerGroups(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('PeerAS')
            header.append('LocalAS')
            header.append('UpdateSource')
            header.append('Description')
            header.append('AdjRIBInFilter')
            header.append('AdjRIBOutFilter')
            header.append('MaxPrefixesRestartTimer')
            header.append('MultiHopEnable')
            header.append('MaxPrefixesDisconnect')
            header.append('MultiHopTTL')
            header.append('KeepaliveTime')
            header.append('RouteReflectorClusterId')
            header.append('AddPathsMaxTx')
            header.append('AddPathsRx')
            header.append('RouteReflectorClient')
            header.append('MaxPrefixesThresholdPct')
            header.append('HoldTime')
            header.append('MaxPrefixes')
            header.append('ConnectRetryTime')

        objs = self.swtch.getAllBGPv6PeerGroups()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['PeerAS'])
            values.append('%s' % o['LocalAS'])
            values.append('%s' % o['UpdateSource'])
            values.append('%s' % o['Description'])
            values.append('%s' % o['AdjRIBInFilter'])
            values.append('%s' % o['AdjRIBOutFilter'])
            values.append('%s' % o['MaxPrefixesRestartTimer'])
            values.append('%s' % o['MultiHopEnable'])
            values.append('%s' % o['MaxPrefixesDisconnect'])
            values.append('%s' % o['MultiHopTTL'])
            values.append('%s' % o['KeepaliveTime'])
            values.append('%s' % o['RouteReflectorClusterId'])
            values.append('%s' % o['AddPathsMaxTx'])
            values.append('%s' % o['AddPathsRx'])
            values.append('%s' % o['RouteReflectorClient'])
            values.append('%s' % o['MaxPrefixesThresholdPct'])
            values.append('%s' % o['HoldTime'])
            values.append('%s' % o['MaxPrefixes'])
            values.append('%s' % o['ConnectRetryTime'])
            rows.append(values)
        self.tblPrintObject('BGPv6PeerGroup', header, rows)


    def printArpEntryHwStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IpAddr')
            header.append('MacAddr')
            header.append('Vlan')
            header.append('Port')

        objs = self.swtch.getAllArpEntryHwStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IpAddr'])
            values.append('%s' % o['MacAddr'])
            values.append('%s' % o['Vlan'])
            values.append('%s' % o['Port'])
            rows.append(values)
        self.tblPrintObject('ArpEntryHwState', header, rows)


    def printArpEntryHwState(self, IpAddr, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IpAddr')
            header.append('MacAddr')
            header.append('Vlan')
            header.append('Port')

        rawobj = self.swtch.getArpEntryHwState(
                                               IpAddr)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['IpAddr'])
            values.append('%s' % o['MacAddr'])
            values.append('%s' % o['Vlan'])
            values.append('%s' % o['Port'])
            rows.append(values)
            self.tblPrintObject('ArpEntryHwState', header, rows)

        else:
            print rawobj.content

    def printOspfGlobalStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('RouterId')
            header.append('VersionNumber')
            header.append('AreaBdrRtrStatus')
            header.append('ExternLsaCount')
            header.append('OpaqueLsaSupport')
            header.append('RestartExitReason')

        objs = self.swtch.getAllOspfGlobalStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['RouterId'])
            values.append('%s' % o['VersionNumber'])
            values.append('%s' % o['AreaBdrRtrStatus'])
            values.append('%s' % o['ExternLsaCount'])
            values.append('%s' % o['OpaqueLsaSupport'])
            values.append('%s' % o['RestartExitReason'])
            rows.append(values)
        self.tblPrintObject('OspfGlobalState', header, rows)


    def printOspfGlobalState(self, RouterId, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('RouterId')
            header.append('VersionNumber')
            header.append('AreaBdrRtrStatus')
            header.append('ExternLsaCount')
            header.append('OpaqueLsaSupport')
            header.append('RestartExitReason')

        rawobj = self.swtch.getOspfGlobalState(
                                               RouterId)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['RouterId'])
            values.append('%s' % o['VersionNumber'])
            values.append('%s' % o['AreaBdrRtrStatus'])
            values.append('%s' % o['ExternLsaCount'])
            values.append('%s' % o['OpaqueLsaSupport'])
            values.append('%s' % o['RestartExitReason'])
            rows.append(values)
            self.tblPrintObject('OspfGlobalState', header, rows)

        else:
            print rawobj.content

    def printCombinedOspfGlobalStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('RouterId')
            header.append('VersionNumber')
            header.append('AreaBdrRtrStatus')
            header.append('ExternLsaCount')
            header.append('OpaqueLsaSupport')
            header.append('RestartExitReason')
            header.append('AdminStat')
            header.append('ASBdrRtrStatus')
            header.append('RestartSupport')
            header.append('RestartInterval')
            header.append('TOSSupport')
            header.append('ReferenceBandwidth')

        objs = self.swtch.getAllOspfGlobalStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['RouterId'])
            values.append('%s' % o['VersionNumber'])
            values.append('%s' % o['AreaBdrRtrStatus'])
            values.append('%s' % o['ExternLsaCount'])
            values.append('%s' % o['OpaqueLsaSupport'])
            values.append('%s' % o['RestartExitReason'])
            r = self.swtch.getOspfGlobal(o['RouterId'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
                values.append('%s' % o['AdminStat'])
                values.append('%s' % o['ASBdrRtrStatus'])
                values.append('%s' % o['RestartSupport'])
                values.append('%s' % o['RestartInterval'])
                values.append('%s' % o['TOSSupport'])
                values.append('%s' % o['ReferenceBandwidth'])
            rows.append(values)
        self.tblPrintObject('OspfGlobalState', header, rows)


    def printIPv6Intfs(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('IpAddr')
            header.append('AdminState')
            header.append('LinkIp')

        objs = self.swtch.getAllIPv6Intfs()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['IpAddr'])
            values.append('%s' % o['AdminState'])
            values.append('%s' % o['LinkIp'])
            rows.append(values)
        self.tblPrintObject('IPv6Intf', header, rows)


    def printRouteStatsPerProtocolStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Protocol')
            header.append('V4Routes')
            header.append('V6Routes')

        objs = self.swtch.getAllRouteStatsPerProtocolStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Protocol'])
            values.append('%s' % o['V4Routes'])
            values.append('%s' % o['V6Routes'])
            rows.append(values)
        var = self.tblPrintObject('RouteStatsPerProtocolState', header, rows)
        return var

    def printRouteStatsPerProtocolState(self, Protocol, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Protocol')
            header.append('V4Routes')
            header.append('V6Routes')

        rawobj = self.swtch.getRouteStatsPerProtocolState(
                                                          Protocol)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['Protocol'])
            values.append('%s' % o['V4Routes'])
            values.append('%s' % o['V6Routes'])
            rows.append(values)
            self.tblPrintObject('RouteStatsPerProtocolState', header, rows)

        else:
            print rawobj.content

    def printIsisGlobals(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Vrf')
            header.append('Enable')

        objs = self.swtch.getAllIsisGlobals()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Vrf'])
            values.append('%s' % o['Enable'])
            rows.append(values)
        self.tblPrintObject('IsisGlobal', header, rows)


    def printBGPv6RouteStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('CIDRLen')
            header.append('Network')
            header.append('Paths')

        objs = self.swtch.getAllBGPv6RouteStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['CIDRLen'])
            values.append('%s' % o['Network'])
            values.append('%s' % o['Paths'])
            rows.append(values)
        self.tblPrintObject('BGPv6RouteState', header, rows)


    def printBGPv6RouteState(self, CIDRLen,Network, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('CIDRLen')
            header.append('Network')
            header.append('Paths')

        rawobj = self.swtch.getBGPv6RouteState(
                                               CIDRLen,
                                               Network)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['CIDRLen'])
            values.append('%s' % o['Network'])
            values.append('%s' % o['Paths'])
            rows.append(values)
            self.tblPrintObject('BGPv6RouteState', header, rows)

        else:
            print rawobj.content

    def printBGPv4RouteStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('CIDRLen')
            header.append('Network')
            header.append('Paths')

        objs = self.swtch.getAllBGPv4RouteStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['CIDRLen'])
            values.append('%s' % o['Network'])
            values.append('%s' % o['Paths'])
            rows.append(values)
        self.tblPrintObject('BGPv4RouteState', header, rows)


    def printBGPv4RouteState(self, CIDRLen,Network, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('CIDRLen')
            header.append('Network')
            header.append('Paths')

        rawobj = self.swtch.getBGPv4RouteState(
                                               CIDRLen,
                                               Network)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['CIDRLen'])
            values.append('%s' % o['Network'])
            values.append('%s' % o['Paths'])
            rows.append(values)
            self.tblPrintObject('BGPv4RouteState', header, rows)

        else:
            print rawobj.content

    def printVrrpVridStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('VRID')
            header.append('IfIndex')
            header.append('AdverRx')
            header.append('AdverTx')
            header.append('LastAdverRx')
            header.append('LastAdverTx')
            header.append('MasterIp')
            header.append('CurrentState')
            header.append('PreviousState')
            header.append('TransitionReason')

        objs = self.swtch.getAllVrrpVridStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['VRID'])
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['AdverRx'])
            values.append('%s' % o['AdverTx'])
            values.append('%s' % o['LastAdverRx'])
            values.append('%s' % o['LastAdverTx'])
            values.append('%s' % o['MasterIp'])
            values.append('%s' % o['CurrentState'])
            values.append('%s' % o['PreviousState'])
            values.append('%s' % o['TransitionReason'])
            rows.append(values)
        self.tblPrintObject('VrrpVridState', header, rows)


    def printVrrpVridState(self, VRID,IfIndex, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('VRID')
            header.append('IfIndex')
            header.append('AdverRx')
            header.append('AdverTx')
            header.append('LastAdverRx')
            header.append('LastAdverTx')
            header.append('MasterIp')
            header.append('CurrentState')
            header.append('PreviousState')
            header.append('TransitionReason')

        rawobj = self.swtch.getVrrpVridState(
                                             VRID,
                                             IfIndex)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['VRID'])
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['AdverRx'])
            values.append('%s' % o['AdverTx'])
            values.append('%s' % o['LastAdverRx'])
            values.append('%s' % o['LastAdverTx'])
            values.append('%s' % o['MasterIp'])
            values.append('%s' % o['CurrentState'])
            values.append('%s' % o['PreviousState'])
            values.append('%s' % o['TransitionReason'])
            rows.append(values)
            self.tblPrintObject('VrrpVridState', header, rows)

        else:
            print rawobj.content

    def printAsicGlobalPMStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Resource')
            header.append('ModuleId')
            header.append('ClassAPMData')
            header.append('ClassBPMData')
            header.append('ClassCPMData')

        objs = self.swtch.getAllAsicGlobalPMStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Resource'])
            values.append('%s' % o['ModuleId'])
            values.append('%s' % o['ClassAPMData'])
            values.append('%s' % o['ClassBPMData'])
            values.append('%s' % o['ClassCPMData'])
            rows.append(values)
        self.tblPrintObject('AsicGlobalPMState', header, rows)


    def printAsicGlobalPMState(self, Resource,ModuleId, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Resource')
            header.append('ModuleId')
            header.append('ClassAPMData')
            header.append('ClassBPMData')
            header.append('ClassCPMData')

        rawobj = self.swtch.getAsicGlobalPMState(
                                                 Resource,
                                                 ModuleId)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['Resource'])
            values.append('%s' % o['ModuleId'])
            values.append('%s' % o['ClassAPMData'])
            values.append('%s' % o['ClassBPMData'])
            values.append('%s' % o['ClassCPMData'])
            rows.append(values)
            self.tblPrintObject('AsicGlobalPMState', header, rows)

        else:
            print rawobj.content

    def printCombinedAsicGlobalPMStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Resource')
            header.append('ModuleId')
            header.append('ClassAPMData')
            header.append('ClassBPMData')
            header.append('ClassCPMData')
            header.append('PMClassBEnable')
            header.append('HighWarnThreshold')
            header.append('LowAlarmThreshold')
            header.append('PMClassCEnable')
            header.append('PMClassAEnable')
            header.append('LowWarnThreshold')
            header.append('HighAlarmThreshold')

        objs = self.swtch.getAllAsicGlobalPMStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Resource'])
            values.append('%s' % o['ModuleId'])
            values.append('%s' % o['ClassAPMData'])
            values.append('%s' % o['ClassBPMData'])
            values.append('%s' % o['ClassCPMData'])
            r = self.swtch.getAsicGlobalPM(o['Resource'], o['ModuleId'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
                values.append('%s' % o['PMClassBEnable'])
                values.append('%s' % o['HighWarnThreshold'])
                values.append('%s' % o['LowAlarmThreshold'])
                values.append('%s' % o['PMClassCEnable'])
                values.append('%s' % o['PMClassAEnable'])
                values.append('%s' % o['LowWarnThreshold'])
                values.append('%s' % o['HighAlarmThreshold'])
            rows.append(values)
        self.tblPrintObject('AsicGlobalPMState', header, rows)


    def printFaultStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('EventId')
            header.append('EventName')
            header.append('SrcObjName')
            header.append('OwnerName')
            header.append('OwnerId')
            header.append('Description')
            header.append('OccuranceTime')
            header.append('SrcObjKey')
            header.append('SrcObjUUID')
            header.append('ResolutionTime')
            header.append('ResolutionReason')

        objs = self.swtch.getAllFaultStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['EventId'])
            values.append('%s' % o['EventName'])
            values.append('%s' % o['SrcObjName'])
            values.append('%s' % o['OwnerName'])
            values.append('%s' % o['OwnerId'])
            values.append('%s' % o['Description'])
            values.append('%s' % o['OccuranceTime'])
            values.append('%s' % o['SrcObjKey'])
            values.append('%s' % o['SrcObjUUID'])
            values.append('%s' % o['ResolutionTime'])
            values.append('%s' % o['ResolutionReason'])
            rows.append(values)
        self.tblPrintObject('FaultState', header, rows)


    def printFaultState(self, EventId,EventName,SrcObjName,OwnerName,OwnerId, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('EventId')
            header.append('EventName')
            header.append('SrcObjName')
            header.append('OwnerName')
            header.append('OwnerId')
            header.append('Description')
            header.append('OccuranceTime')
            header.append('SrcObjKey')
            header.append('SrcObjUUID')
            header.append('ResolutionTime')
            header.append('ResolutionReason')

        rawobj = self.swtch.getFaultState(
                                          EventId,
                                          EventName,
                                          SrcObjName,
                                          OwnerName,
                                          OwnerId)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['EventId'])
            values.append('%s' % o['EventName'])
            values.append('%s' % o['SrcObjName'])
            values.append('%s' % o['OwnerName'])
            values.append('%s' % o['OwnerId'])
            values.append('%s' % o['Description'])
            values.append('%s' % o['OccuranceTime'])
            values.append('%s' % o['SrcObjKey'])
            values.append('%s' % o['SrcObjUUID'])
            values.append('%s' % o['ResolutionTime'])
            values.append('%s' % o['ResolutionReason'])
            rows.append(values)
            self.tblPrintObject('FaultState', header, rows)

        else:
            print rawobj.content

    def printBGPv4Aggregates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IpPrefix')
            header.append('SendSummaryOnly')
            header.append('GenerateASSet')

        objs = self.swtch.getAllBGPv4Aggregates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IpPrefix'])
            values.append('%s' % o['SendSummaryOnly'])
            values.append('%s' % o['GenerateASSet'])
            rows.append(values)
        self.tblPrintObject('BGPv4Aggregate', header, rows)


    def printBGPPolicyDefinitions(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('Precedence')
            header.append('MatchType')
            header.append('StatementList')

        objs = self.swtch.getAllBGPPolicyDefinitions()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['Precedence'])
            values.append('%s' % o['MatchType'])
            values.append('%s' % o['StatementList'])
            rows.append(values)
        self.tblPrintObject('BGPPolicyDefinition', header, rows)


    def printPolicyConditions(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Name')
            header.append('ConditionType')
            header.append('Protocol')
            header.append('IpPrefix')
            header.append('MaskLengthRange')
            header.append('PrefixSet')

        objs = self.swtch.getAllPolicyConditions()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Name'])
            values.append('%s' % o['ConditionType'])
            values.append('%s' % o['Protocol'])
            values.append('%s' % o['IpPrefix'])
            values.append('%s' % o['MaskLengthRange'])
            values.append('%s' % o['PrefixSet'])
            rows.append(values)
        self.tblPrintObject('PolicyCondition', header, rows)


    def printPorts(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IntfRef')
            header.append('IfIndex')
            header.append('PhyIntfType')
            header.append('MacAddr')
            header.append('Speed')
            header.append('MediaType')
            header.append('Mtu')
            header.append('BreakOutMode')
            header.append('PRBSRxEnable')
            header.append('Description')
            header.append('PRBSPolynomial')
            header.append('Duplex')
            header.append('LoopbackMode')
            header.append('EnableFEC')
            header.append('AdminState')
            header.append('Autoneg')
            header.append('PRBSTxEnable')

        objs = self.swtch.getAllPorts()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IntfRef'])
            values.append('%s' % o['IfIndex'])
            values.append('%s' % o['PhyIntfType'])
            values.append('%s' % o['MacAddr'])
            values.append('%s' % o['Speed'])
            values.append('%s' % o['MediaType'])
            values.append('%s' % o['Mtu'])
            values.append('%s' % o['BreakOutMode'])
            values.append('%s' % o['PRBSRxEnable'])
            values.append('%s' % o['Description'])
            values.append('%s' % o['PRBSPolynomial'])
            values.append('%s' % o['Duplex'])
            values.append('%s' % o['LoopbackMode'])
            values.append('%s' % o['EnableFEC'])
            values.append('%s' % o['AdminState'])
            values.append('%s' % o['Autoneg'])
            values.append('%s' % o['PRBSTxEnable'])
            rows.append(values)
        self.tblPrintObject('Port', header, rows)


    def printOspfIfEntryStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IfIpAddress')
            header.append('AddressLessIf')
            header.append('IfState')
            header.append('IfDesignatedRouter')
            header.append('IfBackupDesignatedRouter')
            header.append('IfEvents')
            header.append('IfLsaCount')
            header.append('IfDesignatedRouterId')
            header.append('IfBackupDesignatedRouterId')

        objs = self.swtch.getAllOspfIfEntryStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IfIpAddress'])
            values.append('%s' % o['AddressLessIf'])
            values.append('%s' % o['IfState'])
            values.append('%s' % o['IfDesignatedRouter'])
            values.append('%s' % o['IfBackupDesignatedRouter'])
            values.append('%s' % o['IfEvents'])
            values.append('%s' % o['IfLsaCount'])
            values.append('%s' % o['IfDesignatedRouterId'])
            values.append('%s' % o['IfBackupDesignatedRouterId'])
            rows.append(values)
        self.tblPrintObject('OspfIfEntryState', header, rows)


    def printOspfIfEntryState(self, IfIpAddress,AddressLessIf, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IfIpAddress')
            header.append('AddressLessIf')
            header.append('IfState')
            header.append('IfDesignatedRouter')
            header.append('IfBackupDesignatedRouter')
            header.append('IfEvents')
            header.append('IfLsaCount')
            header.append('IfDesignatedRouterId')
            header.append('IfBackupDesignatedRouterId')

        rawobj = self.swtch.getOspfIfEntryState(
                                                IfIpAddress,
                                                AddressLessIf)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['IfIpAddress'])
            values.append('%s' % o['AddressLessIf'])
            values.append('%s' % o['IfState'])
            values.append('%s' % o['IfDesignatedRouter'])
            values.append('%s' % o['IfBackupDesignatedRouter'])
            values.append('%s' % o['IfEvents'])
            values.append('%s' % o['IfLsaCount'])
            values.append('%s' % o['IfDesignatedRouterId'])
            values.append('%s' % o['IfBackupDesignatedRouterId'])
            rows.append(values)
            self.tblPrintObject('OspfIfEntryState', header, rows)

        else:
            print rawobj.content

    def printCombinedOspfIfEntryStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('IfIpAddress')
            header.append('AddressLessIf')
            header.append('IfState')
            header.append('IfDesignatedRouter')
            header.append('IfBackupDesignatedRouter')
            header.append('IfEvents')
            header.append('IfLsaCount')
            header.append('IfDesignatedRouterId')
            header.append('IfBackupDesignatedRouterId')
            header.append('IfAdminStat')
            header.append('IfAreaId')
            header.append('IfType')
            header.append('IfRtrPriority')
            header.append('IfTransitDelay')
            header.append('IfRetransInterval')
            header.append('IfPollInterval')
            header.append('IfAuthKey')
            header.append('IfAuthType')
            header.append('IfHelloInterval')
            header.append('IfRtrDeadInterval')

        objs = self.swtch.getAllOspfIfEntryStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['IfIpAddress'])
            values.append('%s' % o['AddressLessIf'])
            values.append('%s' % o['IfState'])
            values.append('%s' % o['IfDesignatedRouter'])
            values.append('%s' % o['IfBackupDesignatedRouter'])
            values.append('%s' % o['IfEvents'])
            values.append('%s' % o['IfLsaCount'])
            values.append('%s' % o['IfDesignatedRouterId'])
            values.append('%s' % o['IfBackupDesignatedRouterId'])
            r = self.swtch.getOspfIfEntry(o['IfIpAddress'], o['AddressLessIf'])
            if r.status_code in self.httpSuccessCodes:
                o = r.json()['Object']
                values.append('%s' % o['IfAdminStat'])
                values.append('%s' % o['IfAreaId'])
                values.append('%s' % o['IfType'])
                values.append('%s' % o['IfRtrPriority'])
                values.append('%s' % o['IfTransitDelay'])
                values.append('%s' % o['IfRetransInterval'])
                values.append('%s' % o['IfPollInterval'])
                values.append('%s' % o['IfAuthKey'])
                values.append('%s' % o['IfAuthType'])
                values.append('%s' % o['IfHelloInterval'])
                values.append('%s' % o['IfRtrDeadInterval'])
            rows.append(values)
        self.tblPrintObject('OspfIfEntryState', header, rows)


    def printRIBEventStates(self, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Index')
            header.append('TimeStamp')
            header.append('EventInfo')

        objs = self.swtch.getAllRIBEventStates()
        for obj in objs:
            o = obj['Object']
            values = []
            values.append('%s' % o['Index'])
            values.append('%s' % o['TimeStamp'])
            values.append('%s' % o['EventInfo'])
            rows.append(values)
        self.tblPrintObject('RIBEventState', header, rows)


    def printRIBEventState(self, Index, addHeader=True, brief=None):
        header = []; rows = []
        if addHeader:
            header.append('Index')
            header.append('TimeStamp')
            header.append('EventInfo')

        rawobj = self.swtch.getRIBEventState(
                                             Index)
        if rawobj.status_code in self.httpSuccessCodes:
            obj = rawobj.json()
            o = obj['Object']
            values = []
            values.append('%s' % o['Index'])
            values.append('%s' % o['TimeStamp'])
            values.append('%s' % o['EventInfo'])
            rows.append(values)
            self.tblPrintObject('RIBEventState', header, rows)

        else:
            print rawobj.content
