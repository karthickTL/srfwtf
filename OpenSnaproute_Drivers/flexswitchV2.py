#!/usr/bin/python
import requests
import json
import urllib2
from requests.packages.urllib3.exceptions import InsecureRequestWarning

headers = {'Accept' : 'application/json', 'Content-Type' : 'application/json'}
patchheaders = {'Conent-Type':'application/json-patch+json'}
#def processReturnCode (method) :
#    def returnDetails (self, *args, **kwargs) :
#        r = method(self, *args, **kwargs)
#        if r.status_code in self.httpSuccessCodes:
#            return (r.json(), None)
#        else:
#            ret = {}
#            try:
#                ret = r.json()
#            except:
#                print 'Did not receive Json. HTTP Status %s: Code %s ' %(r.reason, r.status_code) 
#                return ret, r.reason
#            print 'Error from server. Error code %s, Error Message: %s' %(r.status_code, r.json()['Error']) 
#            return (r.json(), "Error")
#    return returnDetails
class FlexSwitch( object):
    httpSuccessCodes = [200, 201, 202, 204]
    def  __init__ (self, ip, port, user=None, passwd=None, timeout=15):
        self.ip    = ip
        self.port  = port
        self.timeout = timeout
        self.authenticate = False
        if user is not None:
            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
            self.authenticate = True
            self.user = user
            self.passwd = passwd
            self.cfgUrlBase = 'https://%s/public/v1/config/'%(ip)
            self.stateUrlBase = 'https://%s/public/v1/state/'%(ip)
            self.actionUrlBase = 'https://%s/public/v1/action/'%(ip)
        else:
            self.cfgUrlBase = 'http://%s:%s/public/v1/config/'%(ip,str(port))
            self.stateUrlBase = 'http://%s:%s/public/v1/state/'%(ip,str(port))
            self.actionUrlBase = 'http://%s:%s/public/v1/action/'%(ip,str(port))

    def getObjects(self, objName, urlPath):
        currentMarker = 0
        nextMarker = 0
        count = 100
        more = True
        entries = []
        while more == True:
            more = False
            qry = '%s/%ss?CurrentMarker=%d&NextMarker=%d&Count=%d' %(urlPath, objName, currentMarker, nextMarker, count)
            if self.authenticate == True:
                response = requests.get(qry, timeout=self.timeout, auth=(self.user, self.passwd), varify=False)
            else:
                response = requests.get(qry, timeout=self.timeout)
            if response.status_code in self.httpSuccessCodes:
                data = response.json()
                more =  data['MoreExist']
                currentMarker =  data['NextMarker']
                NextMarker    =  data['NextMarker']
                if data['Objects'] != None:
                    entries.extend(data['Objects'])
            else:
                print 'Server returned Error for %s' %(qry)
        return entries

    def getObject(self, objName, obj, urlPath):
        qry = '%s/%s' %(urlPath, objName)
        if self.authenticate == True:
            response = requests.get(qry, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False)
        else:
            response = requests.get(qry, data=json.dumps(obj), headers=headers, timeout=self.timeout)
        if response.status_code in self.httpSuccessCodes:
            data = response.json()
            if data['Object'] != None:
                entry = (data['Object'])
            else:
                print 'Server returned Error for %s' %(qry)
        return entry

    def getObjectById(self, objName, Id, urlPath):
        qry = '%s/%s/%s' %(urlPath, objName, Id)
        if self.authenticate == True:
            response = requests.get(qry, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False)
        else:
            response = requests.get(qry, headers=headers, timeout=self.timeout)
        if response.status_code in self.httpSuccessCodes:
            data = response.json()
            if data['Object'] != None:
                entry = (data['Object'])
            else:
                print 'Server returned Error for %s' %(qry)
        return entry

    def getArpEntryState(self,
                         IpAddr):
        obj =  { 
                'IpAddr' : IpAddr,
                }
        reqUrl =  self.stateUrlBase + 'ArpEntry'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getArpEntryStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'ArpEntry'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllArpEntryStates(self):
        return self.getObjects('ArpEntry', self.stateUrlBase)


    def getPlatformMgmtDeviceState(self,
                                   DeviceName):
        obj =  { 
                'DeviceName' : DeviceName,
                }
        reqUrl =  self.stateUrlBase + 'PlatformMgmtDevice'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getPlatformMgmtDeviceStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'PlatformMgmtDevice'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllPlatformMgmtDeviceStates(self):
        return self.getObjects('PlatformMgmtDevice', self.stateUrlBase)


    def getOspfIPv4RouteState(self,
                              DestId,
                              DestType,
                              AddrMask):
        obj =  { 
                'DestId' : DestId,
                'DestType' : DestType,
                'AddrMask' : AddrMask,
                }
        reqUrl =  self.stateUrlBase + 'OspfIPv4Route'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getOspfIPv4RouteStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'OspfIPv4Route'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllOspfIPv4RouteStates(self):
        return self.getObjects('OspfIPv4Route', self.stateUrlBase)


    def updateTemperatureSensor(self,
                                Name,
                                HigherAlarmThreshold = None,
                                HigherWarningThreshold = None,
                                LowerWarningThreshold = None,
                                LowerAlarmThreshold = None,
                                PMClassCAdminState = None,
                                PMClassAAdminState = None,
                                AdminState = None,
                                PMClassBAdminState = None):
        obj =  {}
        if Name != None :
            obj['Name'] = Name

        if HigherAlarmThreshold != None :
            obj['HigherAlarmThreshold'] = HigherAlarmThreshold

        if HigherWarningThreshold != None :
            obj['HigherWarningThreshold'] = HigherWarningThreshold

        if LowerWarningThreshold != None :
            obj['LowerWarningThreshold'] = LowerWarningThreshold

        if LowerAlarmThreshold != None :
            obj['LowerAlarmThreshold'] = LowerAlarmThreshold

        if PMClassCAdminState != None :
            obj['PMClassCAdminState'] = PMClassCAdminState

        if PMClassAAdminState != None :
            obj['PMClassAAdminState'] = PMClassAAdminState

        if AdminState != None :
            obj['AdminState'] = AdminState

        if PMClassBAdminState != None :
            obj['PMClassBAdminState'] = PMClassBAdminState

        reqUrl =  self.cfgUrlBase+'TemperatureSensor'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateTemperatureSensorById(self,
                                     objectId,
                                     HigherAlarmThreshold = None,
                                     HigherWarningThreshold = None,
                                     LowerWarningThreshold = None,
                                     LowerAlarmThreshold = None,
                                     PMClassCAdminState = None,
                                     PMClassAAdminState = None,
                                     AdminState = None,
                                     PMClassBAdminState = None):
        obj =  {}
        if HigherAlarmThreshold !=  None:
            obj['HigherAlarmThreshold'] = HigherAlarmThreshold

        if HigherWarningThreshold !=  None:
            obj['HigherWarningThreshold'] = HigherWarningThreshold

        if LowerWarningThreshold !=  None:
            obj['LowerWarningThreshold'] = LowerWarningThreshold

        if LowerAlarmThreshold !=  None:
            obj['LowerAlarmThreshold'] = LowerAlarmThreshold

        if PMClassCAdminState !=  None:
            obj['PMClassCAdminState'] = PMClassCAdminState

        if PMClassAAdminState !=  None:
            obj['PMClassAAdminState'] = PMClassAAdminState

        if AdminState !=  None:
            obj['AdminState'] = AdminState

        if PMClassBAdminState !=  None:
            obj['PMClassBAdminState'] = PMClassBAdminState

        reqUrl =  self.cfgUrlBase+'TemperatureSensor'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateTemperatureSensor(self,
                                     Name,
                                     op,
                                     path,
                                     value,):
        obj =  {}
        obj['Name'] = Name
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'TemperatureSensor'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getTemperatureSensor(self,
                             Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.cfgUrlBase + 'TemperatureSensor'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getTemperatureSensorById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'TemperatureSensor'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllTemperatureSensors(self):
        return self.getObjects('TemperatureSensor', self.cfgUrlBase)


    def getNdpEntryHwState(self,
                           IpAddr):
        obj =  { 
                'IpAddr' : IpAddr,
                }
        reqUrl =  self.stateUrlBase + 'NdpEntryHw'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getNdpEntryHwStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'NdpEntryHw'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllNdpEntryHwStates(self):
        return self.getObjects('NdpEntryHw', self.stateUrlBase)


    """
    .. automethod :: executeFaultEnable(self,
        :param string OwnerName : Fault owner name Fault owner name
        :param string EventName : Fault event name Fault event name
        :param bool Enable : Enable/Disbale control Enable/Disbale control

	"""
    def executeFaultEnable(self,
                           OwnerName,
                           EventName,
                           Enable):
        obj =  { 
                'OwnerName' : OwnerName,
                'EventName' : EventName,
                'Enable' : True if Enable else False,
                }
        reqUrl =  self.actionUrlBase+'FaultEnable'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    """
    .. automethod :: createPolicyStmt(self,
        :param string Name : Policy Statement Name Policy Statement Name
        :param string Conditions : List of conditions added to this policy statement List of conditions added to this policy statement
        :param string Action : Action for this policy statement Action for this policy statement
        :param string MatchConditions : Specifies whether to match all/any of the conditions of this policy statement Specifies whether to match all/any of the conditions of this policy statement

	"""
    def createPolicyStmt(self,
                         Name,
                         Conditions,
                         Action='deny',
                         MatchConditions='all'):
        obj =  { 
                'Name' : Name,
                'Conditions' : Conditions,
                'Action' : Action,
                'MatchConditions' : MatchConditions,
                }
        reqUrl =  self.cfgUrlBase+'PolicyStmt'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deletePolicyStmt(self,
                         Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.cfgUrlBase+'PolicyStmt'
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deletePolicyStmtById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'PolicyStmt'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        else:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        return r

    def updatePolicyStmt(self,
                         Name,
                         Conditions = None,
                         Action = None,
                         MatchConditions = None):
        obj =  {}
        if Name != None :
            obj['Name'] = Name

        if Conditions != None :
            obj['Conditions'] = Conditions

        if Action != None :
            obj['Action'] = Action

        if MatchConditions != None :
            obj['MatchConditions'] = MatchConditions

        reqUrl =  self.cfgUrlBase+'PolicyStmt'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updatePolicyStmtById(self,
                              objectId,
                              Conditions = None,
                              Action = None,
                              MatchConditions = None):
        obj =  {}
        if Conditions !=  None:
            obj['Conditions'] = Conditions

        if Action !=  None:
            obj['Action'] = Action

        if MatchConditions !=  None:
            obj['MatchConditions'] = MatchConditions

        reqUrl =  self.cfgUrlBase+'PolicyStmt'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdatePolicyStmt(self,
                              Name,
                              op,
                              path,
                              value,):
        obj =  {}
        obj['Name'] = Name
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'PolicyStmt'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getPolicyStmt(self,
                      Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.cfgUrlBase + 'PolicyStmt'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getPolicyStmtById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'PolicyStmt'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllPolicyStmts(self):
        return self.getObjects('PolicyStmt', self.cfgUrlBase)


    def updateQsfpChannel(self,
                          ChannelNum,
                          QsfpId,
                          HigherAlarmRXPower = None,
                          HigherAlarmTXPower = None,
                          HigherAlarmTXBias = None,
                          HigherWarningRXPower = None,
                          HigherWarningTXPower = None,
                          HigherWarningTXBias = None,
                          LowerAlarmRXPower = None,
                          LowerAlarmTXPower = None,
                          LowerAlarmTXBias = None,
                          LowerWarningRXPower = None,
                          LowerWarningTXPower = None,
                          LowerWarningTXBias = None,
                          PMClassBAdminState = None,
                          PMClassCAdminState = None,
                          PMClassAAdminState = None,
                          AdminState = None):
        obj =  {}
        if ChannelNum != None :
            obj['ChannelNum'] = int(ChannelNum)

        if QsfpId != None :
            obj['QsfpId'] = int(QsfpId)

        if HigherAlarmRXPower != None :
            obj['HigherAlarmRXPower'] = HigherAlarmRXPower

        if HigherAlarmTXPower != None :
            obj['HigherAlarmTXPower'] = HigherAlarmTXPower

        if HigherAlarmTXBias != None :
            obj['HigherAlarmTXBias'] = HigherAlarmTXBias

        if HigherWarningRXPower != None :
            obj['HigherWarningRXPower'] = HigherWarningRXPower

        if HigherWarningTXPower != None :
            obj['HigherWarningTXPower'] = HigherWarningTXPower

        if HigherWarningTXBias != None :
            obj['HigherWarningTXBias'] = HigherWarningTXBias

        if LowerAlarmRXPower != None :
            obj['LowerAlarmRXPower'] = LowerAlarmRXPower

        if LowerAlarmTXPower != None :
            obj['LowerAlarmTXPower'] = LowerAlarmTXPower

        if LowerAlarmTXBias != None :
            obj['LowerAlarmTXBias'] = LowerAlarmTXBias

        if LowerWarningRXPower != None :
            obj['LowerWarningRXPower'] = LowerWarningRXPower

        if LowerWarningTXPower != None :
            obj['LowerWarningTXPower'] = LowerWarningTXPower

        if LowerWarningTXBias != None :
            obj['LowerWarningTXBias'] = LowerWarningTXBias

        if PMClassBAdminState != None :
            obj['PMClassBAdminState'] = PMClassBAdminState

        if PMClassCAdminState != None :
            obj['PMClassCAdminState'] = PMClassCAdminState

        if PMClassAAdminState != None :
            obj['PMClassAAdminState'] = PMClassAAdminState

        if AdminState != None :
            obj['AdminState'] = AdminState

        reqUrl =  self.cfgUrlBase+'QsfpChannel'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateQsfpChannelById(self,
                               objectId,
                               HigherAlarmRXPower = None,
                               HigherAlarmTXPower = None,
                               HigherAlarmTXBias = None,
                               HigherWarningRXPower = None,
                               HigherWarningTXPower = None,
                               HigherWarningTXBias = None,
                               LowerAlarmRXPower = None,
                               LowerAlarmTXPower = None,
                               LowerAlarmTXBias = None,
                               LowerWarningRXPower = None,
                               LowerWarningTXPower = None,
                               LowerWarningTXBias = None,
                               PMClassBAdminState = None,
                               PMClassCAdminState = None,
                               PMClassAAdminState = None,
                               AdminState = None):
        obj =  {}
        if HigherAlarmRXPower !=  None:
            obj['HigherAlarmRXPower'] = HigherAlarmRXPower

        if HigherAlarmTXPower !=  None:
            obj['HigherAlarmTXPower'] = HigherAlarmTXPower

        if HigherAlarmTXBias !=  None:
            obj['HigherAlarmTXBias'] = HigherAlarmTXBias

        if HigherWarningRXPower !=  None:
            obj['HigherWarningRXPower'] = HigherWarningRXPower

        if HigherWarningTXPower !=  None:
            obj['HigherWarningTXPower'] = HigherWarningTXPower

        if HigherWarningTXBias !=  None:
            obj['HigherWarningTXBias'] = HigherWarningTXBias

        if LowerAlarmRXPower !=  None:
            obj['LowerAlarmRXPower'] = LowerAlarmRXPower

        if LowerAlarmTXPower !=  None:
            obj['LowerAlarmTXPower'] = LowerAlarmTXPower

        if LowerAlarmTXBias !=  None:
            obj['LowerAlarmTXBias'] = LowerAlarmTXBias

        if LowerWarningRXPower !=  None:
            obj['LowerWarningRXPower'] = LowerWarningRXPower

        if LowerWarningTXPower !=  None:
            obj['LowerWarningTXPower'] = LowerWarningTXPower

        if LowerWarningTXBias !=  None:
            obj['LowerWarningTXBias'] = LowerWarningTXBias

        if PMClassBAdminState !=  None:
            obj['PMClassBAdminState'] = PMClassBAdminState

        if PMClassCAdminState !=  None:
            obj['PMClassCAdminState'] = PMClassCAdminState

        if PMClassAAdminState !=  None:
            obj['PMClassAAdminState'] = PMClassAAdminState

        if AdminState !=  None:
            obj['AdminState'] = AdminState

        reqUrl =  self.cfgUrlBase+'QsfpChannel'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateQsfpChannel(self,
                               ChannelNum,
                               QsfpId,
                               op,
                               path,
                               value,):
        obj =  {}
        obj['ChannelNum'] = ChannelNum
        obj['QsfpId'] = QsfpId
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'QsfpChannel'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getQsfpChannel(self,
                       ChannelNum,
                       QsfpId):
        obj =  { 
                'ChannelNum' : int(ChannelNum),
                'QsfpId' : int(QsfpId),
                }
        reqUrl =  self.cfgUrlBase + 'QsfpChannel'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getQsfpChannelById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'QsfpChannel'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllQsfpChannels(self):
        return self.getObjects('QsfpChannel', self.cfgUrlBase)


    def updatePowerConverterSensor(self,
                                   Name,
                                   HigherAlarmThreshold = None,
                                   HigherWarningThreshold = None,
                                   LowerWarningThreshold = None,
                                   LowerAlarmThreshold = None,
                                   PMClassCAdminState = None,
                                   PMClassAAdminState = None,
                                   AdminState = None,
                                   PMClassBAdminState = None):
        obj =  {}
        if Name != None :
            obj['Name'] = Name

        if HigherAlarmThreshold != None :
            obj['HigherAlarmThreshold'] = HigherAlarmThreshold

        if HigherWarningThreshold != None :
            obj['HigherWarningThreshold'] = HigherWarningThreshold

        if LowerWarningThreshold != None :
            obj['LowerWarningThreshold'] = LowerWarningThreshold

        if LowerAlarmThreshold != None :
            obj['LowerAlarmThreshold'] = LowerAlarmThreshold

        if PMClassCAdminState != None :
            obj['PMClassCAdminState'] = PMClassCAdminState

        if PMClassAAdminState != None :
            obj['PMClassAAdminState'] = PMClassAAdminState

        if AdminState != None :
            obj['AdminState'] = AdminState

        if PMClassBAdminState != None :
            obj['PMClassBAdminState'] = PMClassBAdminState

        reqUrl =  self.cfgUrlBase+'PowerConverterSensor'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updatePowerConverterSensorById(self,
                                        objectId,
                                        HigherAlarmThreshold = None,
                                        HigherWarningThreshold = None,
                                        LowerWarningThreshold = None,
                                        LowerAlarmThreshold = None,
                                        PMClassCAdminState = None,
                                        PMClassAAdminState = None,
                                        AdminState = None,
                                        PMClassBAdminState = None):
        obj =  {}
        if HigherAlarmThreshold !=  None:
            obj['HigherAlarmThreshold'] = HigherAlarmThreshold

        if HigherWarningThreshold !=  None:
            obj['HigherWarningThreshold'] = HigherWarningThreshold

        if LowerWarningThreshold !=  None:
            obj['LowerWarningThreshold'] = LowerWarningThreshold

        if LowerAlarmThreshold !=  None:
            obj['LowerAlarmThreshold'] = LowerAlarmThreshold

        if PMClassCAdminState !=  None:
            obj['PMClassCAdminState'] = PMClassCAdminState

        if PMClassAAdminState !=  None:
            obj['PMClassAAdminState'] = PMClassAAdminState

        if AdminState !=  None:
            obj['AdminState'] = AdminState

        if PMClassBAdminState !=  None:
            obj['PMClassBAdminState'] = PMClassBAdminState

        reqUrl =  self.cfgUrlBase+'PowerConverterSensor'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdatePowerConverterSensor(self,
                                        Name,
                                        op,
                                        path,
                                        value,):
        obj =  {}
        obj['Name'] = Name
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'PowerConverterSensor'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getPowerConverterSensor(self,
                                Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.cfgUrlBase + 'PowerConverterSensor'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getPowerConverterSensorById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'PowerConverterSensor'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllPowerConverterSensors(self):
        return self.getObjects('PowerConverterSensor', self.cfgUrlBase)


    """
    .. automethod :: createVlan(self,
        :param int32 VlanId : 802.1Q tag/Vlan ID for vlan being provisioned 802.1Q tag/Vlan ID for vlan being provisioned
        :param string IntfList : List of interface names or ifindex values to  be added as tagged members of the vlan List of interface names or ifindex values to  be added as tagged members of the vlan
        :param string UntagIntfList : List of interface names or ifindex values to  be added as untagged members of the vlan List of interface names or ifindex values to  be added as untagged members of the vlan
        :param string AdminState : Administrative state of this vlan interface Administrative state of this vlan interface

	"""
    def createVlan(self,
                   VlanId,
                   IntfList,
                   UntagIntfList,
                   AdminState='UP'):
        obj =  { 
                'VlanId' : int(VlanId),
                'IntfList' : IntfList,
                'UntagIntfList' : UntagIntfList,
                'AdminState' : AdminState,
                }
        reqUrl =  self.cfgUrlBase+'Vlan'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteVlan(self,
                   VlanId):
        obj =  { 
                'VlanId' : VlanId,
                }
        reqUrl =  self.cfgUrlBase+'Vlan'
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteVlanById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'Vlan'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        else:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        return r

    def updateVlan(self,
                   VlanId,
                   IntfList = None,
                   UntagIntfList = None,
                   AdminState = None):
        obj =  {}
        if VlanId != None :
            obj['VlanId'] = int(VlanId)

        if IntfList != None :
            obj['IntfList'] = IntfList

        if UntagIntfList != None :
            obj['UntagIntfList'] = UntagIntfList

        if AdminState != None :
            obj['AdminState'] = AdminState

        reqUrl =  self.cfgUrlBase+'Vlan'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateVlanById(self,
                        objectId,
                        IntfList = None,
                        UntagIntfList = None,
                        AdminState = None):
        obj =  {}
        if IntfList !=  None:
            obj['IntfList'] = IntfList

        if UntagIntfList !=  None:
            obj['UntagIntfList'] = UntagIntfList

        if AdminState !=  None:
            obj['AdminState'] = AdminState

        reqUrl =  self.cfgUrlBase+'Vlan'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateVlan(self,
                        VlanId,
                        op,
                        path,
                        value,):
        obj =  {}
        obj['VlanId'] = VlanId
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'Vlan'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getVlan(self,
                VlanId):
        obj =  { 
                'VlanId' : int(VlanId),
                }
        reqUrl =  self.cfgUrlBase + 'Vlan'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getVlanById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'Vlan'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllVlans(self):
        return self.getObjects('Vlan', self.cfgUrlBase)


    def updateDWDMModuleNwIntf(self,
                               NwIntfId,
                               ModuleId,
                               ClntIntfIdToTributary0Map = None,
                               ClntIntfIdToTributary1Map = None,
                               EnableRxPRBSChecker = None,
                               TxPulseShapeFltrRollOff = None,
                               TxPower = None,
                               RxPRBSInvertPattern = None,
                               TxPowerRampdBmPerSec = None,
                               EnableTxPRBS = None,
                               TxPRBSInvertPattern = None,
                               AdminState = None,
                               ChannelNumber = None,
                               FECMode = None,
                               ModulationFmt = None,
                               TxPulseShapeFltrType = None,
                               RxPRBSPattern = None,
                               TxPRBSPattern = None,
                               DiffEncoding = None):
        obj =  {}
        if NwIntfId != None :
            obj['NwIntfId'] = int(NwIntfId)

        if ModuleId != None :
            obj['ModuleId'] = int(ModuleId)

        if ClntIntfIdToTributary0Map != None :
            obj['ClntIntfIdToTributary0Map'] = int(ClntIntfIdToTributary0Map)

        if ClntIntfIdToTributary1Map != None :
            obj['ClntIntfIdToTributary1Map'] = int(ClntIntfIdToTributary1Map)

        if EnableRxPRBSChecker != None :
            obj['EnableRxPRBSChecker'] = True if EnableRxPRBSChecker else False

        if TxPulseShapeFltrRollOff != None :
            obj['TxPulseShapeFltrRollOff'] = TxPulseShapeFltrRollOff

        if TxPower != None :
            obj['TxPower'] = TxPower

        if RxPRBSInvertPattern != None :
            obj['RxPRBSInvertPattern'] = True if RxPRBSInvertPattern else False

        if TxPowerRampdBmPerSec != None :
            obj['TxPowerRampdBmPerSec'] = TxPowerRampdBmPerSec

        if EnableTxPRBS != None :
            obj['EnableTxPRBS'] = True if EnableTxPRBS else False

        if TxPRBSInvertPattern != None :
            obj['TxPRBSInvertPattern'] = True if TxPRBSInvertPattern else False

        if AdminState != None :
            obj['AdminState'] = AdminState

        if ChannelNumber != None :
            obj['ChannelNumber'] = int(ChannelNumber)

        if FECMode != None :
            obj['FECMode'] = FECMode

        if ModulationFmt != None :
            obj['ModulationFmt'] = ModulationFmt

        if TxPulseShapeFltrType != None :
            obj['TxPulseShapeFltrType'] = TxPulseShapeFltrType

        if RxPRBSPattern != None :
            obj['RxPRBSPattern'] = RxPRBSPattern

        if TxPRBSPattern != None :
            obj['TxPRBSPattern'] = TxPRBSPattern

        if DiffEncoding != None :
            obj['DiffEncoding'] = True if DiffEncoding else False

        reqUrl =  self.cfgUrlBase+'DWDMModuleNwIntf'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateDWDMModuleNwIntfById(self,
                                    objectId,
                                    ClntIntfIdToTributary0Map = None,
                                    ClntIntfIdToTributary1Map = None,
                                    EnableRxPRBSChecker = None,
                                    TxPulseShapeFltrRollOff = None,
                                    TxPower = None,
                                    RxPRBSInvertPattern = None,
                                    TxPowerRampdBmPerSec = None,
                                    EnableTxPRBS = None,
                                    TxPRBSInvertPattern = None,
                                    AdminState = None,
                                    ChannelNumber = None,
                                    FECMode = None,
                                    ModulationFmt = None,
                                    TxPulseShapeFltrType = None,
                                    RxPRBSPattern = None,
                                    TxPRBSPattern = None,
                                    DiffEncoding = None):
        obj =  {}
        if ClntIntfIdToTributary0Map !=  None:
            obj['ClntIntfIdToTributary0Map'] = ClntIntfIdToTributary0Map

        if ClntIntfIdToTributary1Map !=  None:
            obj['ClntIntfIdToTributary1Map'] = ClntIntfIdToTributary1Map

        if EnableRxPRBSChecker !=  None:
            obj['EnableRxPRBSChecker'] = EnableRxPRBSChecker

        if TxPulseShapeFltrRollOff !=  None:
            obj['TxPulseShapeFltrRollOff'] = TxPulseShapeFltrRollOff

        if TxPower !=  None:
            obj['TxPower'] = TxPower

        if RxPRBSInvertPattern !=  None:
            obj['RxPRBSInvertPattern'] = RxPRBSInvertPattern

        if TxPowerRampdBmPerSec !=  None:
            obj['TxPowerRampdBmPerSec'] = TxPowerRampdBmPerSec

        if EnableTxPRBS !=  None:
            obj['EnableTxPRBS'] = EnableTxPRBS

        if TxPRBSInvertPattern !=  None:
            obj['TxPRBSInvertPattern'] = TxPRBSInvertPattern

        if AdminState !=  None:
            obj['AdminState'] = AdminState

        if ChannelNumber !=  None:
            obj['ChannelNumber'] = ChannelNumber

        if FECMode !=  None:
            obj['FECMode'] = FECMode

        if ModulationFmt !=  None:
            obj['ModulationFmt'] = ModulationFmt

        if TxPulseShapeFltrType !=  None:
            obj['TxPulseShapeFltrType'] = TxPulseShapeFltrType

        if RxPRBSPattern !=  None:
            obj['RxPRBSPattern'] = RxPRBSPattern

        if TxPRBSPattern !=  None:
            obj['TxPRBSPattern'] = TxPRBSPattern

        if DiffEncoding !=  None:
            obj['DiffEncoding'] = DiffEncoding

        reqUrl =  self.cfgUrlBase+'DWDMModuleNwIntf'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateDWDMModuleNwIntf(self,
                                    NwIntfId,
                                    ModuleId,
                                    op,
                                    path,
                                    value,):
        obj =  {}
        obj['NwIntfId'] = NwIntfId
        obj['ModuleId'] = ModuleId
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'DWDMModuleNwIntf'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getDWDMModuleNwIntf(self,
                            NwIntfId,
                            ModuleId):
        obj =  { 
                'NwIntfId' : int(NwIntfId),
                'ModuleId' : int(ModuleId),
                }
        reqUrl =  self.cfgUrlBase + 'DWDMModuleNwIntf'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getDWDMModuleNwIntfById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'DWDMModuleNwIntf'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllDWDMModuleNwIntfs(self):
        return self.getObjects('DWDMModuleNwIntf', self.cfgUrlBase)


    """
    .. automethod :: createComponentLogging(self,
        :param string Module : Module name to set logging level Module name to set logging level
        :param string Level : Logging level Logging level

	"""
    def createComponentLogging(self,
                               Module,
                               Level='info'):
        obj =  { 
                'Module' : Module,
                'Level' : Level,
                }
        reqUrl =  self.cfgUrlBase+'ComponentLogging'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteComponentLogging(self,
                               Module):
        obj =  { 
                'Module' : Module,
                }
        reqUrl =  self.cfgUrlBase+'ComponentLogging'
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteComponentLoggingById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'ComponentLogging'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        else:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        return r

    def updateComponentLogging(self,
                               Module,
                               Level = None):
        obj =  {}
        if Module != None :
            obj['Module'] = Module

        if Level != None :
            obj['Level'] = Level

        reqUrl =  self.cfgUrlBase+'ComponentLogging'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateComponentLoggingById(self,
                                    objectId,
                                    Level = None):
        obj =  {}
        if Level !=  None:
            obj['Level'] = Level

        reqUrl =  self.cfgUrlBase+'ComponentLogging'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateComponentLogging(self,
                                    Module,
                                    op,
                                    path,
                                    value,):
        obj =  {}
        obj['Module'] = Module
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'ComponentLogging'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getComponentLogging(self,
                            Module):
        obj =  { 
                'Module' : Module,
                }
        reqUrl =  self.cfgUrlBase + 'ComponentLogging'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getComponentLoggingById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'ComponentLogging'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllComponentLoggings(self):
        return self.getObjects('ComponentLogging', self.cfgUrlBase)


    def updateFan(self,
                  FanId,
                  AdminState = None,
                  AdminSpeed = None):
        obj =  {}
        if FanId != None :
            obj['FanId'] = int(FanId)

        if AdminState != None :
            obj['AdminState'] = AdminState

        if AdminSpeed != None :
            obj['AdminSpeed'] = int(AdminSpeed)

        reqUrl =  self.cfgUrlBase+'Fan'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateFanById(self,
                       objectId,
                       AdminState = None,
                       AdminSpeed = None):
        obj =  {}
        if AdminState !=  None:
            obj['AdminState'] = AdminState

        if AdminSpeed !=  None:
            obj['AdminSpeed'] = AdminSpeed

        reqUrl =  self.cfgUrlBase+'Fan'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateFan(self,
                       FanId,
                       op,
                       path,
                       value,):
        obj =  {}
        obj['FanId'] = FanId
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'Fan'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getFan(self,
               FanId):
        obj =  { 
                'FanId' : int(FanId),
                }
        reqUrl =  self.cfgUrlBase + 'Fan'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getFanById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'Fan'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllFans(self):
        return self.getObjects('Fan', self.cfgUrlBase)


    """
    .. automethod :: createSubIPv6Intf(self,
        :param string IntfRef : Intf name of system generated id (ifindex) of the ipv4Intf where sub interface is to be configured Intf name of system generated id (ifindex) of the ipv4Intf where sub interface is to be configured
        :param string IpAddr : Ip Address for the interface Ip Address for the interface
        :param string Type : Type of interface Type of interface
        :param string MacAddr : Mac address to be used for the sub interface. If none specified IPv4Intf mac address will be used Mac address to be used for the sub interface. If none specified IPv4Intf mac address will be used
        :param bool Enable : Enable or disable this interface Enable or disable this interface

	"""
    def createSubIPv6Intf(self,
                          IntfRef,
                          IpAddr,
                          Type,
                          MacAddr,
                          Enable=False):
        obj =  { 
                'IntfRef' : IntfRef,
                'IpAddr' : IpAddr,
                'Type' : Type,
                'MacAddr' : MacAddr,
                'Enable' : True if Enable else False,
                }
        reqUrl =  self.cfgUrlBase+'SubIPv6Intf'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteSubIPv6Intf(self,
                          IntfRef,
                          IpAddr):
        obj =  { 
                'IntfRef' : IntfRef,
                'IpAddr' : IpAddr,
                }
        reqUrl =  self.cfgUrlBase+'SubIPv6Intf'
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteSubIPv6IntfById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'SubIPv6Intf'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        else:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        return r

    def updateSubIPv6Intf(self,
                          IntfRef,
                          IpAddr,
                          Type = None,
                          MacAddr = None,
                          Enable = None):
        obj =  {}
        if IntfRef != None :
            obj['IntfRef'] = IntfRef

        if IpAddr != None :
            obj['IpAddr'] = IpAddr

        if Type != None :
            obj['Type'] = Type

        if MacAddr != None :
            obj['MacAddr'] = MacAddr

        if Enable != None :
            obj['Enable'] = True if Enable else False

        reqUrl =  self.cfgUrlBase+'SubIPv6Intf'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateSubIPv6IntfById(self,
                               objectId,
                               Type = None,
                               MacAddr = None,
                               Enable = None):
        obj =  {}
        if Type !=  None:
            obj['Type'] = Type

        if MacAddr !=  None:
            obj['MacAddr'] = MacAddr

        if Enable !=  None:
            obj['Enable'] = Enable

        reqUrl =  self.cfgUrlBase+'SubIPv6Intf'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateSubIPv6Intf(self,
                               IntfRef,
                               IpAddr,
                               op,
                               path,
                               value,):
        obj =  {}
        obj['IntfRef'] = IntfRef
        obj['IpAddr'] = IpAddr
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'SubIPv6Intf'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getSubIPv6Intf(self,
                       IntfRef,
                       IpAddr):
        obj =  { 
                'IntfRef' : IntfRef,
                'IpAddr' : IpAddr,
                }
        reqUrl =  self.cfgUrlBase + 'SubIPv6Intf'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getSubIPv6IntfById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'SubIPv6Intf'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllSubIPv6Intfs(self):
        return self.getObjects('SubIPv6Intf', self.cfgUrlBase)


    def getIPv6RouteState(self,
                          DestinationNw):
        obj =  { 
                'DestinationNw' : DestinationNw,
                }
        reqUrl =  self.stateUrlBase + 'IPv6Route'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getIPv6RouteStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'IPv6Route'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllIPv6RouteStates(self):
        return self.getObjects('IPv6Route', self.stateUrlBase)


    def getPolicyPrefixSetState(self,
                                Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.stateUrlBase + 'PolicyPrefixSet'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getPolicyPrefixSetStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'PolicyPrefixSet'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllPolicyPrefixSetStates(self):
        return self.getObjects('PolicyPrefixSet', self.stateUrlBase)


    def updatePsu(self,
                  PsuId,
                  AdminState = None):
        obj =  {}
        if PsuId != None :
            obj['PsuId'] = int(PsuId)

        if AdminState != None :
            obj['AdminState'] = AdminState

        reqUrl =  self.cfgUrlBase+'Psu'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updatePsuById(self,
                       objectId,
                       AdminState = None):
        obj =  {}
        if AdminState !=  None:
            obj['AdminState'] = AdminState

        reqUrl =  self.cfgUrlBase+'Psu'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdatePsu(self,
                       PsuId,
                       op,
                       path,
                       value,):
        obj =  {}
        obj['PsuId'] = PsuId
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'Psu'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getPsu(self,
               PsuId):
        obj =  { 
                'PsuId' : int(PsuId),
                }
        reqUrl =  self.cfgUrlBase + 'Psu'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getPsuById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'Psu'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllPsus(self):
        return self.getObjects('Psu', self.cfgUrlBase)


    def getBGPv4NeighborState(self,
                              IntfRef,
                              NeighborAddress):
        print "From The flxex Swithc"
	obj =  { 
                'IntfRef' : IntfRef,
                'NeighborAddress' : NeighborAddress,
                }
        print json.dumps(obj)
	reqUrl =  self.stateUrlBase + 'BGPv4Neighbor'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
		print r
        return r

    def getBGPv4NeighborStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'BGPv4Neighbor'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllBGPv4NeighborStates(self):
        return self.getObjects('BGPv4Neighbor', self.stateUrlBase)


    """
    .. automethod :: executeArpRefreshByIPv4Addr(self,
        :param string IpAddr : Neighbor's IP Address for which corresponding Arp entry needed to be re-learned Neighbor's IP Address for which corresponding Arp entry needed to be re-learned

	"""
    def executeArpRefreshByIPv4Addr(self,
                                    IpAddr):
        obj =  { 
                'IpAddr' : IpAddr,
                }
        reqUrl =  self.actionUrlBase+'ArpRefreshByIPv4Addr'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateXponderGlobal(self,
                            XponderId,
                            XponderDescription = None,
                            XponderMode = None):
        obj =  {}
        if XponderId != None :
            obj['XponderId'] = int(XponderId)

        if XponderDescription != None :
            obj['XponderDescription'] = XponderDescription

        if XponderMode != None :
            obj['XponderMode'] = XponderMode

        reqUrl =  self.cfgUrlBase+'XponderGlobal'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateXponderGlobalById(self,
                                 objectId,
                                 XponderDescription = None,
                                 XponderMode = None):
        obj =  {}
        if XponderDescription !=  None:
            obj['XponderDescription'] = XponderDescription

        if XponderMode !=  None:
            obj['XponderMode'] = XponderMode

        reqUrl =  self.cfgUrlBase+'XponderGlobal'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateXponderGlobal(self,
                                 XponderId,
                                 op,
                                 path,
                                 value,):
        obj =  {}
        obj['XponderId'] = XponderId
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'XponderGlobal'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getXponderGlobal(self,
                         XponderId):
        obj =  { 
                'XponderId' : int(XponderId),
                }
        reqUrl =  self.cfgUrlBase + 'XponderGlobal'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getXponderGlobalById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'XponderGlobal'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllXponderGlobals(self):
        return self.getObjects('XponderGlobal', self.cfgUrlBase)


    """
    .. automethod :: createOspfAreaEntry(self,
        :param string AreaId : A 32-bit integer uniquely identifying an area. Area ID 0.0.0.0 is used for the OSPF backbone. A 32-bit integer uniquely identifying an area. Area ID 0.0.0.0 is used for the OSPF backbone.
        :param int32 AuthType : The authentication type specified for an area. The authentication type specified for an area.
        :param int32 ImportAsExtern : Indicates if an area is a stub area Indicates if an area is a stub area
        :param int32 AreaSummary : The variable ospfAreaSummary controls the import of summary LSAs into stub and NSSA areas. It has no effect on other areas.  If it is noAreaSummary The variable ospfAreaSummary controls the import of summary LSAs into stub and NSSA areas. It has no effect on other areas.  If it is noAreaSummary
        :param int32 AreaNssaTranslatorRole : Indicates an NSSA border router's ability to perform NSSA translation of type-7 LSAs into type-5 LSAs. Indicates an NSSA border router's ability to perform NSSA translation of type-7 LSAs into type-5 LSAs.
        :param int32 StubDefaultCost : For ABR this cost indicates default cost for summary LSA. For ABR this cost indicates default cost for summary LSA.

	"""
    def createOspfAreaEntry(self,
                            AreaId,
                            AuthType,
                            ImportAsExtern,
                            AreaSummary,
                            AreaNssaTranslatorRole,
                            StubDefaultCost=10):
        obj =  { 
                'AreaId' : AreaId,
                'AuthType' : int(AuthType),
                'ImportAsExtern' : int(ImportAsExtern),
                'AreaSummary' : int(AreaSummary),
                'AreaNssaTranslatorRole' : int(AreaNssaTranslatorRole),
                'StubDefaultCost' : int(StubDefaultCost),
                }
        reqUrl =  self.cfgUrlBase+'OspfAreaEntry'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteOspfAreaEntry(self,
                            AreaId):
        obj =  { 
                'AreaId' : AreaId,
                }
        reqUrl =  self.cfgUrlBase+'OspfAreaEntry'
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteOspfAreaEntryById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'OspfAreaEntry'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        else:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        return r

    def updateOspfAreaEntry(self,
                            AreaId,
                            AuthType = None,
                            ImportAsExtern = None,
                            AreaSummary = None,
                            AreaNssaTranslatorRole = None,
                            StubDefaultCost = None):
        obj =  {}
        if AreaId != None :
            obj['AreaId'] = AreaId

        if AuthType != None :
            obj['AuthType'] = int(AuthType)

        if ImportAsExtern != None :
            obj['ImportAsExtern'] = int(ImportAsExtern)

        if AreaSummary != None :
            obj['AreaSummary'] = int(AreaSummary)

        if AreaNssaTranslatorRole != None :
            obj['AreaNssaTranslatorRole'] = int(AreaNssaTranslatorRole)

        if StubDefaultCost != None :
            obj['StubDefaultCost'] = int(StubDefaultCost)

        reqUrl =  self.cfgUrlBase+'OspfAreaEntry'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateOspfAreaEntryById(self,
                                 objectId,
                                 AuthType = None,
                                 ImportAsExtern = None,
                                 AreaSummary = None,
                                 AreaNssaTranslatorRole = None,
                                 StubDefaultCost = None):
        obj =  {}
        if AuthType !=  None:
            obj['AuthType'] = AuthType

        if ImportAsExtern !=  None:
            obj['ImportAsExtern'] = ImportAsExtern

        if AreaSummary !=  None:
            obj['AreaSummary'] = AreaSummary

        if AreaNssaTranslatorRole !=  None:
            obj['AreaNssaTranslatorRole'] = AreaNssaTranslatorRole

        if StubDefaultCost !=  None:
            obj['StubDefaultCost'] = StubDefaultCost

        reqUrl =  self.cfgUrlBase+'OspfAreaEntry'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateOspfAreaEntry(self,
                                 AreaId,
                                 op,
                                 path,
                                 value,):
        obj =  {}
        obj['AreaId'] = AreaId
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'OspfAreaEntry'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getOspfAreaEntry(self,
                         AreaId):
        obj =  { 
                'AreaId' : AreaId,
                }
        reqUrl =  self.cfgUrlBase + 'OspfAreaEntry'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getOspfAreaEntryById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'OspfAreaEntry'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllOspfAreaEntrys(self):
        return self.getObjects('OspfAreaEntry', self.cfgUrlBase)


    """
    .. automethod :: createVxlanVtepInstance(self,
        :param string Intf : VTEP instance identifier name. should be defined as either vtep<id#> or <id#> if the later then 'vtep' will be prepended to the <id#> example VTEP instance identifier name. should be defined as either vtep<id#> or <id#> if the later then 'vtep' will be prepended to the <id#> example
        :param string IntfRef : Source interface where the source ip will be derived from.  If an interface is not supplied the src-ip will be used. This attribute takes presedence over src-ip attribute. Source interface where the source ip will be derived from.  If an interface is not supplied the src-ip will be used. This attribute takes presedence over src-ip attribute.
        :param uint32 Vni : Reference to the vxlan domain that this vtep is attached to Reference to the vxlan domain that this vtep is attached to
        :param string DstIp : Destination IP address for the static VxLAN tunnel Destination IP address for the static VxLAN tunnel
        :param uint16 VlanId : Vlan Id to encapsulate with the vtep tunnel ethernet header Vlan Id to encapsulate with the vtep tunnel ethernet header
        :param uint16 TOS : Type of Service Type of Service
        :param uint32 Mtu : Set the MTU to be applied to all VTEP within this VxLAN Set the MTU to be applied to all VTEP within this VxLAN
        :param int32 InnerVlanHandlingMode : The inner vlan tag handling mode. The inner vlan tag handling mode.
        :param uint16 TTL : TTL of the Vxlan tunnel TTL of the Vxlan tunnel
        :param string SrcIp : Source IP address for the VxLAN tunnel Source IP address for the VxLAN tunnel
        :param uint16 DstUDP : vxlan udp port.  Deafult is the iana default udp port vxlan udp port.  Deafult is the iana default udp port

	"""
    def createVxlanVtepInstance(self,
                                Intf,
                                IntfRef,
                                Vni,
                                DstIp,
                                VlanId,
                                TOS=0,
                                Mtu=1550,
                                InnerVlanHandlingMode=0,
                                TTL=255,
                                SrcIp='0.0.0.0',
                                DstUDP=4789):
        obj =  { 
                'Intf' : Intf,
                'IntfRef' : IntfRef,
                'Vni' : int(Vni),
                'DstIp' : DstIp,
                'VlanId' : int(VlanId),
                'TOS' : int(TOS),
                'Mtu' : int(Mtu),
                'InnerVlanHandlingMode' : int(InnerVlanHandlingMode),
                'TTL' : int(TTL),
                'SrcIp' : SrcIp,
                'DstUDP' : int(DstUDP),
                }
        reqUrl =  self.cfgUrlBase+'VxlanVtepInstance'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteVxlanVtepInstance(self,
                                Intf):
        obj =  { 
                'Intf' : Intf,
                }
        reqUrl =  self.cfgUrlBase+'VxlanVtepInstance'
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteVxlanVtepInstanceById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'VxlanVtepInstance'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        else:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        return r

    def updateVxlanVtepInstance(self,
                                Intf,
                                IntfRef = None,
                                Vni = None,
                                DstIp = None,
                                VlanId = None,
                                TOS = None,
                                Mtu = None,
                                InnerVlanHandlingMode = None,
                                TTL = None,
                                SrcIp = None,
                                DstUDP = None):
        obj =  {}
        if Intf != None :
            obj['Intf'] = Intf

        if IntfRef != None :
            obj['IntfRef'] = IntfRef

        if Vni != None :
            obj['Vni'] = int(Vni)

        if DstIp != None :
            obj['DstIp'] = DstIp

        if VlanId != None :
            obj['VlanId'] = int(VlanId)

        if TOS != None :
            obj['TOS'] = int(TOS)

        if Mtu != None :
            obj['Mtu'] = int(Mtu)

        if InnerVlanHandlingMode != None :
            obj['InnerVlanHandlingMode'] = int(InnerVlanHandlingMode)

        if TTL != None :
            obj['TTL'] = int(TTL)

        if SrcIp != None :
            obj['SrcIp'] = SrcIp

        if DstUDP != None :
            obj['DstUDP'] = int(DstUDP)

        reqUrl =  self.cfgUrlBase+'VxlanVtepInstance'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateVxlanVtepInstanceById(self,
                                     objectId,
                                     IntfRef = None,
                                     Vni = None,
                                     DstIp = None,
                                     VlanId = None,
                                     TOS = None,
                                     Mtu = None,
                                     InnerVlanHandlingMode = None,
                                     TTL = None,
                                     SrcIp = None,
                                     DstUDP = None):
        obj =  {}
        if IntfRef !=  None:
            obj['IntfRef'] = IntfRef

        if Vni !=  None:
            obj['Vni'] = Vni

        if DstIp !=  None:
            obj['DstIp'] = DstIp

        if VlanId !=  None:
            obj['VlanId'] = VlanId

        if TOS !=  None:
            obj['TOS'] = TOS

        if Mtu !=  None:
            obj['Mtu'] = Mtu

        if InnerVlanHandlingMode !=  None:
            obj['InnerVlanHandlingMode'] = InnerVlanHandlingMode

        if TTL !=  None:
            obj['TTL'] = TTL

        if SrcIp !=  None:
            obj['SrcIp'] = SrcIp

        if DstUDP !=  None:
            obj['DstUDP'] = DstUDP

        reqUrl =  self.cfgUrlBase+'VxlanVtepInstance'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateVxlanVtepInstance(self,
                                     Intf,
                                     op,
                                     path,
                                     value,):
        obj =  {}
        obj['Intf'] = Intf
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'VxlanVtepInstance'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getVxlanVtepInstance(self,
                             Intf):
        obj =  { 
                'Intf' : Intf,
                }
        reqUrl =  self.cfgUrlBase + 'VxlanVtepInstance'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getVxlanVtepInstanceById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'VxlanVtepInstance'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllVxlanVtepInstances(self):
        return self.getObjects('VxlanVtepInstance', self.cfgUrlBase)


    def getLaPortChannelState(self,
                              IntfRef):
        obj =  { 
                'IntfRef' : IntfRef,
                }
        reqUrl =  self.stateUrlBase + 'LaPortChannel'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getLaPortChannelStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'LaPortChannel'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllLaPortChannelStates(self):
        return self.getObjects('LaPortChannel', self.stateUrlBase)


    """
    .. automethod :: createDhcpGlobalConfig(self,
        :param string DhcpConfigKey : DHCP global config DHCP global config
        :param bool Enable : DHCP Server enable/disable control DEFAULT DHCP Server enable/disable control DEFAULT
        :param uint32 DefaultLeaseTime : Default Lease Time in seconds DEFAULT Default Lease Time in seconds DEFAULT
        :param uint32 MaxLeaseTime : Max Lease Time in seconds DEFAULT Max Lease Time in seconds DEFAULT

	"""
    def createDhcpGlobalConfig(self,
                               Enable,
                               DefaultLeaseTime,
                               MaxLeaseTime):
        obj =  { 
                'DhcpConfigKey' : 'default',
                'Enable' : True if Enable else False,
                'DefaultLeaseTime' : int(DefaultLeaseTime),
                'MaxLeaseTime' : int(MaxLeaseTime),
                }
        reqUrl =  self.cfgUrlBase+'DhcpGlobalConfig'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteDhcpGlobalConfig(self,
                               DhcpConfigKey):
        obj =  { 
                'DhcpConfigKey' : DhcpConfigKey,
                }
        reqUrl =  self.cfgUrlBase+'DhcpGlobalConfig'
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteDhcpGlobalConfigById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'DhcpGlobalConfig'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        else:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        return r

    def updateDhcpGlobalConfig(self,
                               DhcpConfigKey,
                               Enable = None,
                               DefaultLeaseTime = None,
                               MaxLeaseTime = None):
        obj =  {}
        if DhcpConfigKey != None :
            obj['DhcpConfigKey'] = DhcpConfigKey

        if Enable != None :
            obj['Enable'] = True if Enable else False

        if DefaultLeaseTime != None :
            obj['DefaultLeaseTime'] = int(DefaultLeaseTime)

        if MaxLeaseTime != None :
            obj['MaxLeaseTime'] = int(MaxLeaseTime)

        reqUrl =  self.cfgUrlBase+'DhcpGlobalConfig'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateDhcpGlobalConfigById(self,
                                    objectId,
                                    Enable = None,
                                    DefaultLeaseTime = None,
                                    MaxLeaseTime = None):
        obj =  {}
        if Enable !=  None:
            obj['Enable'] = Enable

        if DefaultLeaseTime !=  None:
            obj['DefaultLeaseTime'] = DefaultLeaseTime

        if MaxLeaseTime !=  None:
            obj['MaxLeaseTime'] = MaxLeaseTime

        reqUrl =  self.cfgUrlBase+'DhcpGlobalConfig'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateDhcpGlobalConfig(self,
                                    DhcpConfigKey,
                                    op,
                                    path,
                                    value,):
        obj =  {}
        obj['DhcpConfigKey'] = DhcpConfigKey
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'DhcpGlobalConfig'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getDhcpGlobalConfig(self,
                            DhcpConfigKey):
        obj =  { 
                'DhcpConfigKey' : DhcpConfigKey,
                }
        reqUrl =  self.cfgUrlBase + 'DhcpGlobalConfig'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getDhcpGlobalConfigById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'DhcpGlobalConfig'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllDhcpGlobalConfigs(self):
        return self.getObjects('DhcpGlobalConfig', self.cfgUrlBase)


    """
    .. automethod :: createDhcpRelayIntf(self,
        :param int32 IfIndex : Interface index for which Relay Agent Config needs to be done Interface index for which Relay Agent Config needs to be done
        :param bool Enable : Enabling/Disabling relay agent per interface Enabling/Disabling relay agent per interface
        :param string ServerIp : Dhcp Server(s) where relay agent can relay client dhcp requests Dhcp Server(s) where relay agent can relay client dhcp requests

	"""
    def createDhcpRelayIntf(self,
                            IfIndex,
                            Enable,
                            ServerIp):
        obj =  { 
                'IfIndex' : int(IfIndex),
                'Enable' : True if Enable else False,
                'ServerIp' : ServerIp,
                }
        reqUrl =  self.cfgUrlBase+'DhcpRelayIntf'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteDhcpRelayIntf(self,
                            IfIndex):
        obj =  { 
                'IfIndex' : IfIndex,
                }
        reqUrl =  self.cfgUrlBase+'DhcpRelayIntf'
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteDhcpRelayIntfById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'DhcpRelayIntf'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        else:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        return r

    def updateDhcpRelayIntf(self,
                            IfIndex,
                            Enable = None,
                            ServerIp = None):
        obj =  {}
        if IfIndex != None :
            obj['IfIndex'] = int(IfIndex)

        if Enable != None :
            obj['Enable'] = True if Enable else False

        if ServerIp != None :
            obj['ServerIp'] = ServerIp

        reqUrl =  self.cfgUrlBase+'DhcpRelayIntf'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateDhcpRelayIntfById(self,
                                 objectId,
                                 Enable = None,
                                 ServerIp = None):
        obj =  {}
        if Enable !=  None:
            obj['Enable'] = Enable

        if ServerIp !=  None:
            obj['ServerIp'] = ServerIp

        reqUrl =  self.cfgUrlBase+'DhcpRelayIntf'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateDhcpRelayIntf(self,
                                 IfIndex,
                                 op,
                                 path,
                                 value,):
        obj =  {}
        obj['IfIndex'] = IfIndex
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'DhcpRelayIntf'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getDhcpRelayIntf(self,
                         IfIndex):
        obj =  { 
                'IfIndex' : int(IfIndex),
                }
        reqUrl =  self.cfgUrlBase + 'DhcpRelayIntf'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getDhcpRelayIntfById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'DhcpRelayIntf'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllDhcpRelayIntfs(self):
        return self.getObjects('DhcpRelayIntf', self.cfgUrlBase)


    def getDistributedRelayState(self,
                                 DrniName):
        obj =  { 
                'DrniName' : DrniName,
                }
        reqUrl =  self.stateUrlBase + 'DistributedRelay'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getDistributedRelayStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'DistributedRelay'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllDistributedRelayStates(self):
        return self.getObjects('DistributedRelay', self.stateUrlBase)


    """
    .. automethod :: createAclRule(self,
        :param string RuleName : Acl rule name Acl rule name
        :param string SourceMac : Source MAC address. Source MAC address.
        :param string DestMac : Destination MAC address Destination MAC address
        :param string SourceIp : Source IP address Source IP address
        :param string DestIp : Destination IP address Destination IP address
        :param string SourceMask : Network mask for source IP Network mask for source IP
        :param string DestMask : Network mark for dest IP Network mark for dest IP
        :param string Proto : Protocol type Protocol type
        :param string SrcPort : Source Port Source Port
        :param int32 L4DstPort : TCP/UDP destionation port TCP/UDP destionation port
        :param int32 L4MinPort : Min port when l4 port is specified as range Min port when l4 port is specified as range
        :param int32 L4SrcPort : TCP/UDP source port TCP/UDP source port
        :param string Action : Type of action (Allow/Deny) Type of action (Allow/Deny)
        :param int32 L4MaxPort : Max port when l4 port is specified as range Max port when l4 port is specified as range
        :param string DstPort : Dest Port Dest Port
        :param string L4PortMatch : match condition can be EQ(equal) match condition can be EQ(equal)

	"""
    def createAclRule(self,
                      RuleName,
                      SourceMac,
                      DestMac,
                      SourceIp,
                      DestIp,
                      SourceMask,
                      DestMask,
                      Proto,
                      SrcPort,
                      L4DstPort,
                      L4MinPort=0,
                      L4SrcPort=0,
                      Action='Allow',
                      L4MaxPort=0,
                      DstPort='0',
                      L4PortMatch='NA'):
        obj =  { 
                'RuleName' : RuleName,
                'SourceMac' : SourceMac,
                'DestMac' : DestMac,
                'SourceIp' : SourceIp,
                'DestIp' : DestIp,
                'SourceMask' : SourceMask,
                'DestMask' : DestMask,
                'Proto' : Proto,
                'SrcPort' : SrcPort,
                'L4DstPort' : int(L4DstPort),
                'L4MinPort' : int(L4MinPort),
                'L4SrcPort' : int(L4SrcPort),
                'Action' : Action,
                'L4MaxPort' : int(L4MaxPort),
                'DstPort' : DstPort,
                'L4PortMatch' : L4PortMatch,
                }
        reqUrl =  self.cfgUrlBase+'AclRule'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteAclRule(self,
                      RuleName):
        obj =  { 
                'RuleName' : RuleName,
                }
        reqUrl =  self.cfgUrlBase+'AclRule'
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteAclRuleById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'AclRule'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        else:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        return r

    def updateAclRule(self,
                      RuleName,
                      SourceMac = None,
                      DestMac = None,
                      SourceIp = None,
                      DestIp = None,
                      SourceMask = None,
                      DestMask = None,
                      Proto = None,
                      SrcPort = None,
                      L4DstPort = None,
                      L4MinPort = None,
                      L4SrcPort = None,
                      Action = None,
                      L4MaxPort = None,
                      DstPort = None,
                      L4PortMatch = None):
        obj =  {}
        if RuleName != None :
            obj['RuleName'] = RuleName

        if SourceMac != None :
            obj['SourceMac'] = SourceMac

        if DestMac != None :
            obj['DestMac'] = DestMac

        if SourceIp != None :
            obj['SourceIp'] = SourceIp

        if DestIp != None :
            obj['DestIp'] = DestIp

        if SourceMask != None :
            obj['SourceMask'] = SourceMask

        if DestMask != None :
            obj['DestMask'] = DestMask

        if Proto != None :
            obj['Proto'] = Proto

        if SrcPort != None :
            obj['SrcPort'] = SrcPort

        if L4DstPort != None :
            obj['L4DstPort'] = int(L4DstPort)

        if L4MinPort != None :
            obj['L4MinPort'] = int(L4MinPort)

        if L4SrcPort != None :
            obj['L4SrcPort'] = int(L4SrcPort)

        if Action != None :
            obj['Action'] = Action

        if L4MaxPort != None :
            obj['L4MaxPort'] = int(L4MaxPort)

        if DstPort != None :
            obj['DstPort'] = DstPort

        if L4PortMatch != None :
            obj['L4PortMatch'] = L4PortMatch

        reqUrl =  self.cfgUrlBase+'AclRule'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateAclRuleById(self,
                           objectId,
                           SourceMac = None,
                           DestMac = None,
                           SourceIp = None,
                           DestIp = None,
                           SourceMask = None,
                           DestMask = None,
                           Proto = None,
                           SrcPort = None,
                           L4DstPort = None,
                           L4MinPort = None,
                           L4SrcPort = None,
                           Action = None,
                           L4MaxPort = None,
                           DstPort = None,
                           L4PortMatch = None):
        obj =  {}
        if SourceMac !=  None:
            obj['SourceMac'] = SourceMac

        if DestMac !=  None:
            obj['DestMac'] = DestMac

        if SourceIp !=  None:
            obj['SourceIp'] = SourceIp

        if DestIp !=  None:
            obj['DestIp'] = DestIp

        if SourceMask !=  None:
            obj['SourceMask'] = SourceMask

        if DestMask !=  None:
            obj['DestMask'] = DestMask

        if Proto !=  None:
            obj['Proto'] = Proto

        if SrcPort !=  None:
            obj['SrcPort'] = SrcPort

        if L4DstPort !=  None:
            obj['L4DstPort'] = L4DstPort

        if L4MinPort !=  None:
            obj['L4MinPort'] = L4MinPort

        if L4SrcPort !=  None:
            obj['L4SrcPort'] = L4SrcPort

        if Action !=  None:
            obj['Action'] = Action

        if L4MaxPort !=  None:
            obj['L4MaxPort'] = L4MaxPort

        if DstPort !=  None:
            obj['DstPort'] = DstPort

        if L4PortMatch !=  None:
            obj['L4PortMatch'] = L4PortMatch

        reqUrl =  self.cfgUrlBase+'AclRule'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateAclRule(self,
                           RuleName,
                           op,
                           path,
                           value,):
        obj =  {}
        obj['RuleName'] = RuleName
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'AclRule'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getAclRule(self,
                   RuleName):
        obj =  { 
                'RuleName' : RuleName,
                }
        reqUrl =  self.cfgUrlBase + 'AclRule'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getAclRuleById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'AclRule'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllAclRules(self):
        return self.getObjects('AclRule', self.cfgUrlBase)


    """
    .. automethod :: createBGPv4Neighbor(self,
        :param string IntfRef : Interface of the BGP neighbor Interface of the BGP neighbor
        :param string NeighborAddress : Address of the BGP neighbor Address of the BGP neighbor
        :param string Description : Description of the BGP neighbor Description of the BGP neighbor
        :param string PeerGroup : Peer group of the BGP neighbor Peer group of the BGP neighbor
        :param string PeerAS : Peer AS of the BGP neighbor Peer AS of the BGP neighbor
        :param string LocalAS : Local AS of the BGP neighbor Local AS of the BGP neighbor
        :param string UpdateSource : Source IP to connect to the BGP neighbor Source IP to connect to the BGP neighbor
        :param string AuthPassword : Password to connect to the BGP neighbor Password to connect to the BGP neighbor
        :param string AdjRIBInFilter : Policy that is applied for Adj-RIB-In prefix filtering Policy that is applied for Adj-RIB-In prefix filtering
        :param string AdjRIBOutFilter : Policy that is applied for Adj-RIB-Out prefix filtering Policy that is applied for Adj-RIB-Out prefix filtering
        :param bool BfdEnable : Enable/Disable BFD for the BGP neighbor Enable/Disable BFD for the BGP neighbor
        :param uint8 MultiHopTTL : TTL for multi hop BGP neighbor TTL for multi hop BGP neighbor
        :param uint32 KeepaliveTime : Keep alive time for the BGP neighbor Keep alive time for the BGP neighbor
        :param bool AddPathsRx : Receive additional paths from BGP neighbor Receive additional paths from BGP neighbor
        :param bool RouteReflectorClient : Set/Clear BGP neighbor as a route reflector client Set/Clear BGP neighbor as a route reflector client
        :param uint8 MaxPrefixesRestartTimer : Time in seconds to wait before we start BGP peer session when we receive max prefixes Time in seconds to wait before we start BGP peer session when we receive max prefixes
        :param bool MultiHopEnable : Enable/Disable multi hop for BGP neighbor Enable/Disable multi hop for BGP neighbor
        :param uint32 RouteReflectorClusterId : Cluster Id of the internal BGP neighbor route reflector client Cluster Id of the internal BGP neighbor route reflector client
        :param bool MaxPrefixesDisconnect : Disconnect the BGP peer session when we receive the max prefixes from the neighbor Disconnect the BGP peer session when we receive the max prefixes from the neighbor
        :param uint8 AddPathsMaxTx : Max number of additional paths that can be transmitted to BGP neighbor Max number of additional paths that can be transmitted to BGP neighbor
        :param uint32 MaxPrefixes : Maximum number of prefixes that can be received from the BGP neighbor Maximum number of prefixes that can be received from the BGP neighbor
        :param uint8 MaxPrefixesThresholdPct : The percentage of maximum prefixes before we start logging The percentage of maximum prefixes before we start logging
        :param string BfdSessionParam : Bfd session param name to be applied Bfd session param name to be applied
        :param bool Disabled : Enable/Disable the BGP neighbor Enable/Disable the BGP neighbor
        :param uint32 HoldTime : Hold time for the BGP neighbor Hold time for the BGP neighbor
        :param uint32 ConnectRetryTime : Connect retry time to connect to BGP neighbor after disconnect Connect retry time to connect to BGP neighbor after disconnect

	"""
    def createBGPv4Neighbor(self,
                            IntfRef,
                            NeighborAddress,
                            Description='',
                            PeerGroup='',
                            PeerAS='',
                            LocalAS='',
                            UpdateSource='',
                            AuthPassword='',
                            AdjRIBInFilter='',
                            AdjRIBOutFilter='',
                            BfdEnable=False,
                            MultiHopTTL=0,
                            KeepaliveTime=0,
                            AddPathsRx=False,
                            RouteReflectorClient=False,
                            MaxPrefixesRestartTimer=0,
                            MultiHopEnable=False,
                            RouteReflectorClusterId=0,
                            MaxPrefixesDisconnect=False,
                            AddPathsMaxTx=0,
                            MaxPrefixes=0,
                            MaxPrefixesThresholdPct=80,
                            BfdSessionParam='default',
                            Disabled=False,
                            HoldTime=0,
                            ConnectRetryTime=0):
        obj =  { 
                'IntfRef' : IntfRef,
                'NeighborAddress' : NeighborAddress,
                'Description' : Description,
                'PeerGroup' : PeerGroup,
                'PeerAS' : PeerAS,
                'LocalAS' : LocalAS,
                'UpdateSource' : UpdateSource,
                'AuthPassword' : AuthPassword,
                'AdjRIBInFilter' : AdjRIBInFilter,
                'AdjRIBOutFilter' : AdjRIBOutFilter,
                'BfdEnable' : True if BfdEnable else False,
                'MultiHopTTL' : int(MultiHopTTL),
                'KeepaliveTime' : int(KeepaliveTime),
                'AddPathsRx' : True if AddPathsRx else False,
                'RouteReflectorClient' : True if RouteReflectorClient else False,
                'MaxPrefixesRestartTimer' : int(MaxPrefixesRestartTimer),
                'MultiHopEnable' : True if MultiHopEnable else False,
                'RouteReflectorClusterId' : int(RouteReflectorClusterId),
                'MaxPrefixesDisconnect' : True if MaxPrefixesDisconnect else False,
                'AddPathsMaxTx' : int(AddPathsMaxTx),
                'MaxPrefixes' : int(MaxPrefixes),
                'MaxPrefixesThresholdPct' : int(MaxPrefixesThresholdPct),
                'BfdSessionParam' : BfdSessionParam,
                'Disabled' : True if Disabled else False,
                'HoldTime' : int(HoldTime),
                'ConnectRetryTime' : int(ConnectRetryTime),
                }
        reqUrl =  self.cfgUrlBase+'BGPv4Neighbor'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteBGPv4Neighbor(self,
                            IntfRef,
                            NeighborAddress):
        obj =  { 
                'IntfRef' : IntfRef,
                'NeighborAddress' : NeighborAddress,
                }
        reqUrl =  self.cfgUrlBase+'BGPv4Neighbor'
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteBGPv4NeighborById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'BGPv4Neighbor'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        else:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        return r

    def updateBGPv4Neighbor(self,
                            IntfRef,
                            NeighborAddress,
                            Description = None,
                            PeerGroup = None,
                            PeerAS = None,
                            LocalAS = None,
                            UpdateSource = None,
                            AuthPassword = None,
                            AdjRIBInFilter = None,
                            AdjRIBOutFilter = None,
                            BfdEnable = None,
                            MultiHopTTL = None,
                            KeepaliveTime = None,
                            AddPathsRx = None,
                            RouteReflectorClient = None,
                            MaxPrefixesRestartTimer = None,
                            MultiHopEnable = None,
                            RouteReflectorClusterId = None,
                            MaxPrefixesDisconnect = None,
                            AddPathsMaxTx = None,
                            MaxPrefixes = None,
                            MaxPrefixesThresholdPct = None,
                            BfdSessionParam = None,
                            Disabled = None,
                            HoldTime = None,
                            ConnectRetryTime = None):
        obj =  {}
        if IntfRef != None :
            obj['IntfRef'] = IntfRef

        if NeighborAddress != None :
            obj['NeighborAddress'] = NeighborAddress

        if Description != None :
            obj['Description'] = Description

        if PeerGroup != None :
            obj['PeerGroup'] = PeerGroup

        if PeerAS != None :
            obj['PeerAS'] = PeerAS

        if LocalAS != None :
            obj['LocalAS'] = LocalAS

        if UpdateSource != None :
            obj['UpdateSource'] = UpdateSource

        if AuthPassword != None :
            obj['AuthPassword'] = AuthPassword

        if AdjRIBInFilter != None :
            obj['AdjRIBInFilter'] = AdjRIBInFilter

        if AdjRIBOutFilter != None :
            obj['AdjRIBOutFilter'] = AdjRIBOutFilter

        if BfdEnable != None :
            obj['BfdEnable'] = True if BfdEnable else False

        if MultiHopTTL != None :
            obj['MultiHopTTL'] = int(MultiHopTTL)

        if KeepaliveTime != None :
            obj['KeepaliveTime'] = int(KeepaliveTime)

        if AddPathsRx != None :
            obj['AddPathsRx'] = True if AddPathsRx else False

        if RouteReflectorClient != None :
            obj['RouteReflectorClient'] = True if RouteReflectorClient else False

        if MaxPrefixesRestartTimer != None :
            obj['MaxPrefixesRestartTimer'] = int(MaxPrefixesRestartTimer)

        if MultiHopEnable != None :
            obj['MultiHopEnable'] = True if MultiHopEnable else False

        if RouteReflectorClusterId != None :
            obj['RouteReflectorClusterId'] = int(RouteReflectorClusterId)

        if MaxPrefixesDisconnect != None :
            obj['MaxPrefixesDisconnect'] = True if MaxPrefixesDisconnect else False

        if AddPathsMaxTx != None :
            obj['AddPathsMaxTx'] = int(AddPathsMaxTx)

        if MaxPrefixes != None :
            obj['MaxPrefixes'] = int(MaxPrefixes)

        if MaxPrefixesThresholdPct != None :
            obj['MaxPrefixesThresholdPct'] = int(MaxPrefixesThresholdPct)

        if BfdSessionParam != None :
            obj['BfdSessionParam'] = BfdSessionParam

        if Disabled != None :
            obj['Disabled'] = True if Disabled else False

        if HoldTime != None :
            obj['HoldTime'] = int(HoldTime)

        if ConnectRetryTime != None :
            obj['ConnectRetryTime'] = int(ConnectRetryTime)

        reqUrl =  self.cfgUrlBase+'BGPv4Neighbor'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateBGPv4NeighborById(self,
                                 objectId,
                                 Description = None,
                                 PeerGroup = None,
                                 PeerAS = None,
                                 LocalAS = None,
                                 UpdateSource = None,
                                 AuthPassword = None,
                                 AdjRIBInFilter = None,
                                 AdjRIBOutFilter = None,
                                 BfdEnable = None,
                                 MultiHopTTL = None,
                                 KeepaliveTime = None,
                                 AddPathsRx = None,
                                 RouteReflectorClient = None,
                                 MaxPrefixesRestartTimer = None,
                                 MultiHopEnable = None,
                                 RouteReflectorClusterId = None,
                                 MaxPrefixesDisconnect = None,
                                 AddPathsMaxTx = None,
                                 MaxPrefixes = None,
                                 MaxPrefixesThresholdPct = None,
                                 BfdSessionParam = None,
                                 Disabled = None,
                                 HoldTime = None,
                                 ConnectRetryTime = None):
        obj =  {}
        if Description !=  None:
            obj['Description'] = Description

        if PeerGroup !=  None:
            obj['PeerGroup'] = PeerGroup

        if PeerAS !=  None:
            obj['PeerAS'] = PeerAS

        if LocalAS !=  None:
            obj['LocalAS'] = LocalAS

        if UpdateSource !=  None:
            obj['UpdateSource'] = UpdateSource

        if AuthPassword !=  None:
            obj['AuthPassword'] = AuthPassword

        if AdjRIBInFilter !=  None:
            obj['AdjRIBInFilter'] = AdjRIBInFilter

        if AdjRIBOutFilter !=  None:
            obj['AdjRIBOutFilter'] = AdjRIBOutFilter

        if BfdEnable !=  None:
            obj['BfdEnable'] = BfdEnable

        if MultiHopTTL !=  None:
            obj['MultiHopTTL'] = MultiHopTTL

        if KeepaliveTime !=  None:
            obj['KeepaliveTime'] = KeepaliveTime

        if AddPathsRx !=  None:
            obj['AddPathsRx'] = AddPathsRx

        if RouteReflectorClient !=  None:
            obj['RouteReflectorClient'] = RouteReflectorClient

        if MaxPrefixesRestartTimer !=  None:
            obj['MaxPrefixesRestartTimer'] = MaxPrefixesRestartTimer

        if MultiHopEnable !=  None:
            obj['MultiHopEnable'] = MultiHopEnable

        if RouteReflectorClusterId !=  None:
            obj['RouteReflectorClusterId'] = RouteReflectorClusterId

        if MaxPrefixesDisconnect !=  None:
            obj['MaxPrefixesDisconnect'] = MaxPrefixesDisconnect

        if AddPathsMaxTx !=  None:
            obj['AddPathsMaxTx'] = AddPathsMaxTx

        if MaxPrefixes !=  None:
            obj['MaxPrefixes'] = MaxPrefixes

        if MaxPrefixesThresholdPct !=  None:
            obj['MaxPrefixesThresholdPct'] = MaxPrefixesThresholdPct

        if BfdSessionParam !=  None:
            obj['BfdSessionParam'] = BfdSessionParam

        if Disabled !=  None:
            obj['Disabled'] = Disabled

        if HoldTime !=  None:
            obj['HoldTime'] = HoldTime

        if ConnectRetryTime !=  None:
            obj['ConnectRetryTime'] = ConnectRetryTime

        reqUrl =  self.cfgUrlBase+'BGPv4Neighbor'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateBGPv4Neighbor(self,
                                 IntfRef,
                                 NeighborAddress,
                                 op,
                                 path,
                                 value,):
        obj =  {}
        obj['IntfRef'] = IntfRef
        obj['NeighborAddress'] = NeighborAddress
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'BGPv4Neighbor'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getBGPv4Neighbor(self,
                         IntfRef,
                         NeighborAddress):
        obj =  { 
                'IntfRef' : IntfRef,
                'NeighborAddress' : NeighborAddress,
                }
        reqUrl =  self.cfgUrlBase + 'BGPv4Neighbor'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getBGPv4NeighborById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'BGPv4Neighbor'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllBGPv4Neighbors(self):
        return self.getObjects('BGPv4Neighbor', self.cfgUrlBase)


    """
    .. automethod :: executeSaveConfig(self,
        :param string FileName : FileName for the saved config FileName for the saved config

	"""
    def executeSaveConfig(self,
                          FileName='startup-config'):
        obj =  { 
                'FileName' : FileName,
                }
        reqUrl =  self.actionUrlBase+'SaveConfig'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    """
    .. automethod :: createOspfIfMetricEntry(self,
        :param int32 IfMetricAddressLessIf : For the purpose of easing the instancing of addressed and addressless interfaces; this variable takes the value 0 on interfaces with IP addresses and the value of ifIndex for interfaces having no IP address.  On row creation For the purpose of easing the instancing of addressed and addressless interfaces; this variable takes the value 0 on interfaces with IP addresses and the value of ifIndex for interfaces having no IP address.  On row creation
        :param int32 IfMetricTOS : The Type of Service metric being referenced. On row creation The Type of Service metric being referenced. On row creation
        :param string IfMetricIpAddress : The IP address of this OSPF interface.  On row creation The IP address of this OSPF interface.  On row creation
        :param int32 IfMetricValue : The metric of using this Type of Service on this interface.  The default value of the TOS 0 metric is 10^8 / ifSpeed. The metric of using this Type of Service on this interface.  The default value of the TOS 0 metric is 10^8 / ifSpeed.

	"""
    def createOspfIfMetricEntry(self,
                                IfMetricAddressLessIf,
                                IfMetricTOS,
                                IfMetricIpAddress,
                                IfMetricValue):
        obj =  { 
                'IfMetricAddressLessIf' : int(IfMetricAddressLessIf),
                'IfMetricTOS' : int(IfMetricTOS),
                'IfMetricIpAddress' : IfMetricIpAddress,
                'IfMetricValue' : int(IfMetricValue),
                }
        reqUrl =  self.cfgUrlBase+'OspfIfMetricEntry'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteOspfIfMetricEntry(self,
                                IfMetricAddressLessIf,
                                IfMetricTOS,
                                IfMetricIpAddress):
        obj =  { 
                'IfMetricAddressLessIf' : IfMetricAddressLessIf,
                'IfMetricTOS' : IfMetricTOS,
                'IfMetricIpAddress' : IfMetricIpAddress,
                }
        reqUrl =  self.cfgUrlBase+'OspfIfMetricEntry'
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteOspfIfMetricEntryById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'OspfIfMetricEntry'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        else:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        return r

    def updateOspfIfMetricEntry(self,
                                IfMetricAddressLessIf,
                                IfMetricTOS,
                                IfMetricIpAddress,
                                IfMetricValue = None):
        obj =  {}
        if IfMetricAddressLessIf != None :
            obj['IfMetricAddressLessIf'] = int(IfMetricAddressLessIf)

        if IfMetricTOS != None :
            obj['IfMetricTOS'] = int(IfMetricTOS)

        if IfMetricIpAddress != None :
            obj['IfMetricIpAddress'] = IfMetricIpAddress

        if IfMetricValue != None :
            obj['IfMetricValue'] = int(IfMetricValue)

        reqUrl =  self.cfgUrlBase+'OspfIfMetricEntry'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateOspfIfMetricEntryById(self,
                                     objectId,
                                     IfMetricValue = None):
        obj =  {}
        if IfMetricValue !=  None:
            obj['IfMetricValue'] = IfMetricValue

        reqUrl =  self.cfgUrlBase+'OspfIfMetricEntry'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateOspfIfMetricEntry(self,
                                     IfMetricAddressLessIf,
                                     IfMetricTOS,
                                     IfMetricIpAddress,
                                     op,
                                     path,
                                     value,):
        obj =  {}
        obj['IfMetricAddressLessIf'] = IfMetricAddressLessIf
        obj['IfMetricTOS'] = IfMetricTOS
        obj['IfMetricIpAddress'] = IfMetricIpAddress
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'OspfIfMetricEntry'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getOspfIfMetricEntry(self,
                             IfMetricAddressLessIf,
                             IfMetricTOS,
                             IfMetricIpAddress):
        obj =  { 
                'IfMetricAddressLessIf' : int(IfMetricAddressLessIf),
                'IfMetricTOS' : int(IfMetricTOS),
                'IfMetricIpAddress' : IfMetricIpAddress,
                }
        reqUrl =  self.cfgUrlBase + 'OspfIfMetricEntry'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getOspfIfMetricEntryById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'OspfIfMetricEntry'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllOspfIfMetricEntrys(self):
        return self.getObjects('OspfIfMetricEntry', self.cfgUrlBase)


    def getStpPortState(self,
                        IntfRef,
                        Vlan):
        obj =  { 
                'IntfRef' : IntfRef,
                'Vlan' : int(Vlan),
                }
        reqUrl =  self.stateUrlBase + 'StpPort'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getStpPortStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'StpPort'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllStpPortStates(self):
        return self.getObjects('StpPort', self.stateUrlBase)


    def getCoppStatState(self,
                         Protocol):
        obj =  { 
                'Protocol' : Protocol,
                }
        reqUrl =  self.stateUrlBase + 'CoppStat'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getCoppStatStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'CoppStat'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllCoppStatStates(self):
        return self.getObjects('CoppStat', self.stateUrlBase)


    """
    .. automethod :: createFMgrGlobal(self,
        :param string Vrf : System Vrf System Vrf
        :param bool Enable : Enable Fault Manager Enable Fault Manager

	"""
    def createFMgrGlobal(self,
                         Enable):
        obj =  { 
                'Vrf' : 'default',
                'Enable' : True if Enable else False,
                }
        reqUrl =  self.cfgUrlBase+'FMgrGlobal'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteFMgrGlobal(self,
                         Vrf):
        obj =  { 
                'Vrf' : Vrf,
                }
        reqUrl =  self.cfgUrlBase+'FMgrGlobal'
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteFMgrGlobalById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'FMgrGlobal'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        else:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        return r

    def updateFMgrGlobal(self,
                         Vrf,
                         Enable = None):
        obj =  {}
        if Vrf != None :
            obj['Vrf'] = Vrf

        if Enable != None :
            obj['Enable'] = True if Enable else False

        reqUrl =  self.cfgUrlBase+'FMgrGlobal'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateFMgrGlobalById(self,
                              objectId,
                              Enable = None):
        obj =  {}
        if Enable !=  None:
            obj['Enable'] = Enable

        reqUrl =  self.cfgUrlBase+'FMgrGlobal'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateFMgrGlobal(self,
                              Vrf,
                              op,
                              path,
                              value,):
        obj =  {}
        obj['Vrf'] = Vrf
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'FMgrGlobal'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getFMgrGlobal(self,
                      Vrf):
        obj =  { 
                'Vrf' : Vrf,
                }
        reqUrl =  self.cfgUrlBase + 'FMgrGlobal'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getFMgrGlobalById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'FMgrGlobal'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllFMgrGlobals(self):
        return self.getObjects('FMgrGlobal', self.cfgUrlBase)


    def updateNotifierEnable(self,
                             Vrf,
                             AlarmEnable = None,
                             FaultEnable = None,
                             EventEnable = None):
        obj =  {}
        if Vrf != None :
            obj['Vrf'] = Vrf

        if AlarmEnable != None :
            obj['AlarmEnable'] = True if AlarmEnable else False

        if FaultEnable != None :
            obj['FaultEnable'] = True if FaultEnable else False

        if EventEnable != None :
            obj['EventEnable'] = True if EventEnable else False

        reqUrl =  self.cfgUrlBase+'NotifierEnable'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateNotifierEnableById(self,
                                  objectId,
                                  AlarmEnable = None,
                                  FaultEnable = None,
                                  EventEnable = None):
        obj =  {}
        if AlarmEnable !=  None:
            obj['AlarmEnable'] = AlarmEnable

        if FaultEnable !=  None:
            obj['FaultEnable'] = FaultEnable

        if EventEnable !=  None:
            obj['EventEnable'] = EventEnable

        reqUrl =  self.cfgUrlBase+'NotifierEnable'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateNotifierEnable(self,
                                  Vrf,
                                  op,
                                  path,
                                  value,):
        obj =  {}
        obj['Vrf'] = Vrf
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'NotifierEnable'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getNotifierEnable(self,
                          Vrf):
        obj =  { 
                'Vrf' : Vrf,
                }
        reqUrl =  self.cfgUrlBase + 'NotifierEnable'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getNotifierEnableById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'NotifierEnable'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllNotifierEnables(self):
        return self.getObjects('NotifierEnable', self.cfgUrlBase)


    """
    .. automethod :: executeDWDMModuleSetBootPartition(self,
        :param uint8 ModuleId : DWDM Module identifier DWDM Module identifier
        :param string Partition : Active/StandBy Active/StandBy

	"""
    def executeDWDMModuleSetBootPartition(self,
                                          ModuleId,
                                          Partition):
        obj =  { 
                'ModuleId' : int(ModuleId),
                'Partition' : Partition,
                }
        reqUrl =  self.actionUrlBase+'DWDMModuleSetBootPartition'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    """
    .. automethod :: createLaPortChannel(self,
        :param string IntfRef : Id of the lag group Id of the lag group
        :param string IntfRefList : List of current member interfaces for the aggregate List of current member interfaces for the aggregate
        :param uint16 MinLinks : Specifies the mininum number of member interfaces that must be active for the aggregate interface to be available Specifies the mininum number of member interfaces that must be active for the aggregate interface to be available
        :param uint16 SystemPriority : Sytem priority used by the node on this LAG interface. Lower value is higher priority for determining which node is the controlling system. Sytem priority used by the node on this LAG interface. Lower value is higher priority for determining which node is the controlling system.
        :param int32 Interval : Set the period between LACP messages -- uses the lacp-period-type enumeration. Set the period between LACP messages -- uses the lacp-period-type enumeration.
        :param int32 LagHash : The tx hashing algorithm used by the lag group The tx hashing algorithm used by the lag group
        :param string AdminState : Convenient way to disable/enable a lag group.  The behaviour should be such that all traffic should stop.  LACP frames should continue to be processed Convenient way to disable/enable a lag group.  The behaviour should be such that all traffic should stop.  LACP frames should continue to be processed
        :param string SystemIdMac : The MAC address portion of the nodes System ID. This is combined with the system priority to construct the 8-octet system-id The MAC address portion of the nodes System ID. This is combined with the system priority to construct the 8-octet system-id
        :param int32 LagType : Sets the type of LAG Sets the type of LAG
        :param int32 LacpMode : ACTIVE is to initiate the transmission of LACP packets. PASSIVE is to wait for peer to initiate the transmission of LACP packets. ACTIVE is to initiate the transmission of LACP packets. PASSIVE is to wait for peer to initiate the transmission of LACP packets.

	"""
    def createLaPortChannel(self,
                            IntfRef,
                            IntfRefList,
                            MinLinks=1,
                            SystemPriority=32768,
                            Interval=1,
                            LagHash=0,
                            AdminState='UP',
                            SystemIdMac='00-00-00-00-00-00',
                            LagType=0,
                            LacpMode=0):
        obj =  { 
                'IntfRef' : IntfRef,
                'IntfRefList' : IntfRefList,
                'MinLinks' : int(MinLinks),
                'SystemPriority' : int(SystemPriority),
                'Interval' : int(Interval),
                'LagHash' : int(LagHash),
                'AdminState' : AdminState,
                'SystemIdMac' : SystemIdMac,
                'LagType' : int(LagType),
                'LacpMode' : int(LacpMode),
                }
        reqUrl =  self.cfgUrlBase+'LaPortChannel'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteLaPortChannel(self,
                            IntfRef):
        obj =  { 
                'IntfRef' : IntfRef,
                }
        reqUrl =  self.cfgUrlBase+'LaPortChannel'
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteLaPortChannelById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'LaPortChannel'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        else:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        return r

    def updateLaPortChannel(self,
                            IntfRef,
                            IntfRefList = None,
                            MinLinks = None,
                            SystemPriority = None,
                            Interval = None,
                            LagHash = None,
                            AdminState = None,
                            SystemIdMac = None,
                            LagType = None,
                            LacpMode = None):
        obj =  {}
        if IntfRef != None :
            obj['IntfRef'] = IntfRef

        if IntfRefList != None :
            obj['IntfRefList'] = IntfRefList

        if MinLinks != None :
            obj['MinLinks'] = int(MinLinks)

        if SystemPriority != None :
            obj['SystemPriority'] = int(SystemPriority)

        if Interval != None :
            obj['Interval'] = int(Interval)

        if LagHash != None :
            obj['LagHash'] = int(LagHash)

        if AdminState != None :
            obj['AdminState'] = AdminState

        if SystemIdMac != None :
            obj['SystemIdMac'] = SystemIdMac

        if LagType != None :
            obj['LagType'] = int(LagType)

        if LacpMode != None :
            obj['LacpMode'] = int(LacpMode)

        reqUrl =  self.cfgUrlBase+'LaPortChannel'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateLaPortChannelById(self,
                                 objectId,
                                 IntfRefList = None,
                                 MinLinks = None,
                                 SystemPriority = None,
                                 Interval = None,
                                 LagHash = None,
                                 AdminState = None,
                                 SystemIdMac = None,
                                 LagType = None,
                                 LacpMode = None):
        obj =  {}
        if IntfRefList !=  None:
            obj['IntfRefList'] = IntfRefList

        if MinLinks !=  None:
            obj['MinLinks'] = MinLinks

        if SystemPriority !=  None:
            obj['SystemPriority'] = SystemPriority

        if Interval !=  None:
            obj['Interval'] = Interval

        if LagHash !=  None:
            obj['LagHash'] = LagHash

        if AdminState !=  None:
            obj['AdminState'] = AdminState

        if SystemIdMac !=  None:
            obj['SystemIdMac'] = SystemIdMac

        if LagType !=  None:
            obj['LagType'] = LagType

        if LacpMode !=  None:
            obj['LacpMode'] = LacpMode

        reqUrl =  self.cfgUrlBase+'LaPortChannel'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateLaPortChannel(self,
                                 IntfRef,
                                 op,
                                 path,
                                 value,):
        obj =  {}
        obj['IntfRef'] = IntfRef
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'LaPortChannel'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getLaPortChannel(self,
                         IntfRef):
        obj =  { 
                'IntfRef' : IntfRef,
                }
        reqUrl =  self.cfgUrlBase + 'LaPortChannel'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getLaPortChannelById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'LaPortChannel'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllLaPortChannels(self):
        return self.getObjects('LaPortChannel', self.cfgUrlBase)


    def getBGPPolicyConditionState(self,
                                   Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.stateUrlBase + 'BGPPolicyCondition'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getBGPPolicyConditionStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'BGPPolicyCondition'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllBGPPolicyConditionStates(self):
        return self.getObjects('BGPPolicyCondition', self.stateUrlBase)


    def getApiInfoState(self,
                        Url):
        obj =  { 
                'Url' : Url,
                }
        reqUrl =  self.stateUrlBase + 'ApiInfo'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getApiInfoStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'ApiInfo'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllApiInfoStates(self):
        return self.getObjects('ApiInfo', self.stateUrlBase)


    def getFanSensorState(self,
                          Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.stateUrlBase + 'FanSensor'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getFanSensorStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'FanSensor'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllFanSensorStates(self):
        return self.getObjects('FanSensor', self.stateUrlBase)


    """
    .. automethod :: createBfdSessionParam(self,
        :param string Name : Session parameters Session parameters
        :param uint32 RequiredMinRxInterval : Required minimum rx interval in ms Required minimum rx interval in ms
        :param string AuthData : Authentication password Authentication password
        :param bool DemandEnabled : Enable or disable demand mode Enable or disable demand mode
        :param uint32 AuthKeyId : Authentication key id Authentication key id
        :param string AuthType : Authentication type Authentication type
        :param uint32 DesiredMinTxInterval : Desired minimum tx interval in ms Desired minimum tx interval in ms
        :param bool AuthenticationEnabled : Enable or disable authentication Enable or disable authentication
        :param uint32 RequiredMinEchoRxInterval : Required minimum echo rx interval in ms Required minimum echo rx interval in ms
        :param uint32 LocalMultiplier : Detection multiplier Detection multiplier

	"""
    def createBfdSessionParam(self,
                              Name,
                              RequiredMinRxInterval=1000,
                              AuthData='snaproute',
                              DemandEnabled=False,
                              AuthKeyId=1,
                              AuthType='simple',
                              DesiredMinTxInterval=1000,
                              AuthenticationEnabled=False,
                              RequiredMinEchoRxInterval=0,
                              LocalMultiplier=3):
        obj =  { 
                'Name' : Name,
                'RequiredMinRxInterval' : int(RequiredMinRxInterval),
                'AuthData' : AuthData,
                'DemandEnabled' : True if DemandEnabled else False,
                'AuthKeyId' : int(AuthKeyId),
                'AuthType' : AuthType,
                'DesiredMinTxInterval' : int(DesiredMinTxInterval),
                'AuthenticationEnabled' : True if AuthenticationEnabled else False,
                'RequiredMinEchoRxInterval' : int(RequiredMinEchoRxInterval),
                'LocalMultiplier' : int(LocalMultiplier),
                }
        reqUrl =  self.cfgUrlBase+'BfdSessionParam'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteBfdSessionParam(self,
                              Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.cfgUrlBase+'BfdSessionParam'
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteBfdSessionParamById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'BfdSessionParam'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        else:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        return r

    def updateBfdSessionParam(self,
                              Name,
                              RequiredMinRxInterval = None,
                              AuthData = None,
                              DemandEnabled = None,
                              AuthKeyId = None,
                              AuthType = None,
                              DesiredMinTxInterval = None,
                              AuthenticationEnabled = None,
                              RequiredMinEchoRxInterval = None,
                              LocalMultiplier = None):
        obj =  {}
        if Name != None :
            obj['Name'] = Name

        if RequiredMinRxInterval != None :
            obj['RequiredMinRxInterval'] = int(RequiredMinRxInterval)

        if AuthData != None :
            obj['AuthData'] = AuthData

        if DemandEnabled != None :
            obj['DemandEnabled'] = True if DemandEnabled else False

        if AuthKeyId != None :
            obj['AuthKeyId'] = int(AuthKeyId)

        if AuthType != None :
            obj['AuthType'] = AuthType

        if DesiredMinTxInterval != None :
            obj['DesiredMinTxInterval'] = int(DesiredMinTxInterval)

        if AuthenticationEnabled != None :
            obj['AuthenticationEnabled'] = True if AuthenticationEnabled else False

        if RequiredMinEchoRxInterval != None :
            obj['RequiredMinEchoRxInterval'] = int(RequiredMinEchoRxInterval)

        if LocalMultiplier != None :
            obj['LocalMultiplier'] = int(LocalMultiplier)

        reqUrl =  self.cfgUrlBase+'BfdSessionParam'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateBfdSessionParamById(self,
                                   objectId,
                                   RequiredMinRxInterval = None,
                                   AuthData = None,
                                   DemandEnabled = None,
                                   AuthKeyId = None,
                                   AuthType = None,
                                   DesiredMinTxInterval = None,
                                   AuthenticationEnabled = None,
                                   RequiredMinEchoRxInterval = None,
                                   LocalMultiplier = None):
        obj =  {}
        if RequiredMinRxInterval !=  None:
            obj['RequiredMinRxInterval'] = RequiredMinRxInterval

        if AuthData !=  None:
            obj['AuthData'] = AuthData

        if DemandEnabled !=  None:
            obj['DemandEnabled'] = DemandEnabled

        if AuthKeyId !=  None:
            obj['AuthKeyId'] = AuthKeyId

        if AuthType !=  None:
            obj['AuthType'] = AuthType

        if DesiredMinTxInterval !=  None:
            obj['DesiredMinTxInterval'] = DesiredMinTxInterval

        if AuthenticationEnabled !=  None:
            obj['AuthenticationEnabled'] = AuthenticationEnabled

        if RequiredMinEchoRxInterval !=  None:
            obj['RequiredMinEchoRxInterval'] = RequiredMinEchoRxInterval

        if LocalMultiplier !=  None:
            obj['LocalMultiplier'] = LocalMultiplier

        reqUrl =  self.cfgUrlBase+'BfdSessionParam'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateBfdSessionParam(self,
                                   Name,
                                   op,
                                   path,
                                   value,):
        obj =  {}
        obj['Name'] = Name
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'BfdSessionParam'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getBfdSessionParam(self,
                           Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.cfgUrlBase + 'BfdSessionParam'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getBfdSessionParamById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'BfdSessionParam'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllBfdSessionParams(self):
        return self.getObjects('BfdSessionParam', self.cfgUrlBase)


    def getConfigLogState(self,
                          SeqNum,
                          API,
                          Time):
        obj =  { 
                'SeqNum' : int(SeqNum),
                'API' : API,
                'Time' : Time,
                }
        reqUrl =  self.stateUrlBase + 'ConfigLog'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getConfigLogStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'ConfigLog'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllConfigLogStates(self):
        return self.getObjects('ConfigLog', self.stateUrlBase)


    """
    .. automethod :: executeGlobalLogging(self,
        :param string Level : Logging level Logging level

	"""
    def executeGlobalLogging(self,
                             Level='info'):
        obj =  { 
                'Level' : Level,
                }
        reqUrl =  self.actionUrlBase+'GlobalLogging'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getBGPPolicyStmtState(self,
                              Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.stateUrlBase + 'BGPPolicyStmt'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getBGPPolicyStmtStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'BGPPolicyStmt'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllBGPPolicyStmtStates(self):
        return self.getObjects('BGPPolicyStmt', self.stateUrlBase)


    def getDWDMModuleState(self,
                           ModuleId):
        obj =  { 
                'ModuleId' : int(ModuleId),
                }
        reqUrl =  self.stateUrlBase + 'DWDMModule'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getDWDMModuleStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'DWDMModule'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllDWDMModuleStates(self):
        return self.getObjects('DWDMModule', self.stateUrlBase)


    def getDhcpRelayIntfState(self,
                              IfIndex):
        obj =  { 
                'IfIndex' : int(IfIndex),
                }
        reqUrl =  self.stateUrlBase + 'DhcpRelayIntf'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getDhcpRelayIntfStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'DhcpRelayIntf'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllDhcpRelayIntfStates(self):
        return self.getObjects('DhcpRelayIntf', self.stateUrlBase)


    def getLaPortChannelIntfRefListState(self,
                                         IntfRef):
        obj =  { 
                'IntfRef' : IntfRef,
                }
        reqUrl =  self.stateUrlBase + 'LaPortChannelIntfRefList'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getLaPortChannelIntfRefListStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'LaPortChannelIntfRefList'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllLaPortChannelIntfRefListStates(self):
        return self.getObjects('LaPortChannelIntfRefList', self.stateUrlBase)


    def updateDhcpRelayGlobal(self,
                              Vrf,
                              Enable = None):
        obj =  {}
        if Vrf != None :
            obj['Vrf'] = Vrf

        if Enable != None :
            obj['Enable'] = True if Enable else False

        reqUrl =  self.cfgUrlBase+'DhcpRelayGlobal'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateDhcpRelayGlobalById(self,
                                   objectId,
                                   Enable = None):
        obj =  {}
        if Enable !=  None:
            obj['Enable'] = Enable

        reqUrl =  self.cfgUrlBase+'DhcpRelayGlobal'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateDhcpRelayGlobal(self,
                                   Vrf,
                                   op,
                                   path,
                                   value,):
        obj =  {}
        obj['Vrf'] = Vrf
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'DhcpRelayGlobal'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getDhcpRelayGlobal(self,
                           Vrf):
        obj =  { 
                'Vrf' : Vrf,
                }
        reqUrl =  self.cfgUrlBase + 'DhcpRelayGlobal'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getDhcpRelayGlobalById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'DhcpRelayGlobal'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllDhcpRelayGlobals(self):
        return self.getObjects('DhcpRelayGlobal', self.cfgUrlBase)


    def getPlatformState(self,
                         ObjName):
        obj =  { 
                'ObjName' : ObjName,
                }
        reqUrl =  self.stateUrlBase + 'Platform'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getPlatformStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'Platform'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllPlatformStates(self):
        return self.getObjects('Platform', self.stateUrlBase)


    def getBfdSessionParamState(self,
                                Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.stateUrlBase + 'BfdSessionParam'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getBfdSessionParamStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'BfdSessionParam'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllBfdSessionParamStates(self):
        return self.getObjects('BfdSessionParam', self.stateUrlBase)


    """
    .. automethod :: executeDaemon(self,
        :param string Name : Daemon name Daemon name
        :param bool Enable : Enable the flexswitch daemon Enable the flexswitch daemon
        :param bool WatchDog : Enable watchdog for daemon Enable watchdog for daemon

	"""
    def executeDaemon(self,
                      Name,
                      Enable,
                      WatchDog):
        obj =  { 
                'Name' : Name,
                'Enable' : True if Enable else False,
                'WatchDog' : True if WatchDog else False,
                }
        reqUrl =  self.actionUrlBase+'Daemon'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getAsicGlobalState(self,
                           ModuleId):
        obj =  { 
                'ModuleId' : int(ModuleId),
                }
        reqUrl =  self.stateUrlBase + 'AsicGlobal'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getAsicGlobalStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'AsicGlobal'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllAsicGlobalStates(self):
        return self.getObjects('AsicGlobal', self.stateUrlBase)


    def getOspfLsdbEntryState(self,
                              LsdbType,
                              LsdbAreaId,
                              LsdbLsid,
                              LsdbRouterId):
        obj =  { 
                'LsdbType' : int(LsdbType),
                'LsdbAreaId' : LsdbAreaId,
                'LsdbLsid' : LsdbLsid,
                'LsdbRouterId' : LsdbRouterId,
                }
        reqUrl =  self.stateUrlBase + 'OspfLsdbEntry'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getOspfLsdbEntryStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'OspfLsdbEntry'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllOspfLsdbEntryStates(self):
        return self.getObjects('OspfLsdbEntry', self.stateUrlBase)


    def getArpLinuxEntryState(self,
                              IpAddr):
        obj =  { 
                'IpAddr' : IpAddr,
                }
        reqUrl =  self.stateUrlBase + 'ArpLinuxEntry'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getArpLinuxEntryStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'ArpLinuxEntry'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllArpLinuxEntryStates(self):
        return self.getObjects('ArpLinuxEntry', self.stateUrlBase)


    def updateStpGlobal(self,
                        Vrf,
                        AdminState = None):
        obj =  {}
        if Vrf != None :
            obj['Vrf'] = Vrf

        if AdminState != None :
            obj['AdminState'] = AdminState

        reqUrl =  self.cfgUrlBase+'StpGlobal'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateStpGlobalById(self,
                             objectId,
                             AdminState = None):
        obj =  {}
        if AdminState !=  None:
            obj['AdminState'] = AdminState

        reqUrl =  self.cfgUrlBase+'StpGlobal'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateStpGlobal(self,
                             Vrf,
                             op,
                             path,
                             value,):
        obj =  {}
        obj['Vrf'] = Vrf
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'StpGlobal'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getStpGlobal(self,
                     Vrf):
        obj =  { 
                'Vrf' : Vrf,
                }
        reqUrl =  self.cfgUrlBase + 'StpGlobal'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getStpGlobalById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'StpGlobal'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllStpGlobals(self):
        return self.getObjects('StpGlobal', self.cfgUrlBase)


    """
    .. automethod :: createDistributedRelay(self,
        :param string DrniName : The unique identifier allocated to this Distributed Relay by the local System. This attribute identifies a Distributed Relay instance among the subordinate managed objects of the containing object. The unique identifier allocated to this Distributed Relay by the local System. This attribute identifies a Distributed Relay instance among the subordinate managed objects of the containing object.
        :param string PortalAddress : A read-write identifier of a particular Portal. Portal-Addr has to be unique among at least all of the potential Portal Systems to which a given Portal System might be attached via an IPL Intra-Portal Link. Also used as the Actors System ID (6.3.2) for the emulated system A read-write identifier of a particular Portal. Portal-Addr has to be unique among at least all of the potential Portal Systems to which a given Portal System might be attached via an IPL Intra-Portal Link. Also used as the Actors System ID (6.3.2) for the emulated system
        :param uint8 PortalSystemNumber : A read-write identifier of this particular Portal System within a Portal. It is the responsibility of the network administrator to ensure that these numbers are unique among the Portal Systems with the same aDrniPortalAddr (7.4.1.1.4) A read-write identifier of this particular Portal System within a Portal. It is the responsibility of the network administrator to ensure that these numbers are unique among the Portal Systems with the same aDrniPortalAddr (7.4.1.1.4)
        :param string IntfReflist : Read-write list of the Interface Identifiers of the Ports to the Intra-Portal Links assigned to this Distributed Relay. Each Interface Identifier Read-write list of the Interface Identifiers of the Ports to the Intra-Portal Links assigned to this Distributed Relay. Each Interface Identifier
        :param string IntfRef : Read-write Interface Identifier of the Aggregator Port assigned to this Distributed Relay Read-write Interface Identifier of the Aggregator Port assigned to this Distributed Relay
        :param uint16 PortalPriority : A 2octet read-write value indicating the priority value associated with the Portals System ID. Also used as the Actors System Priority (6.3.2) for the emulated system. A 2octet read-write value indicating the priority value associated with the Portals System ID. Also used as the Actors System Priority (6.3.2) for the emulated system.
        :param string GatewayAlgorithm : This object identifies the algorithm used by the DR Function to assign frames to a Gateway Conversation ID. Table 9-7 provides the IEEE 802.1 OUI (00 This object identifies the algorithm used by the DR Function to assign frames to a Gateway Conversation ID. Table 9-7 provides the IEEE 802.1 OUI (00
        :param string NeighborAdminDRCPState : A string of 8 bits A string of 8 bits
        :param string NeighborGatewayAlgorithm : TThis object identifies the value for the Gateway algorithm of the Neighbor Portal System TThis object identifies the value for the Gateway algorithm of the Neighbor Portal System
        :param bool ThreePortalSystem : A read-write Boolean value indicating whether this Portal System is part of a Portal consisting of three Portal Systems or not. Value 1 stands for a Portal of three Portal Systems A read-write Boolean value indicating whether this Portal System is part of a Portal consisting of three Portal Systems or not. Value 1 stands for a Portal of three Portal Systems
        :param string IntraPortalPortProtocolDA : A 6-octet read-write MAC Address value specifying the DA to be used when sending DRCPDUs A 6-octet read-write MAC Address value specifying the DA to be used when sending DRCPDUs
        :param string NeighborPortAlgorithm : This object identifies the value for the Port Algorithm of the Neighbor Portal System This object identifies the value for the Port Algorithm of the Neighbor Portal System
        :param string EncapMethod : This managed object is applicable only when Network / IPL sharing by time (9.3.2.1) or Network / IPL sharing by tag (9.3.2.2) or Network / IPL sharing by encapsulation (9.3.2.3) is supported. The object identifies the value representing the encapsulation method that is used to transport IPL frames to the Neighbor Portal System when the IPL and network link are sharing the same physical link. It consists of the 3-octet OUI or CID identifying the organization that is responsible for this encapsulation and one following octet used to identify the encapsulation method defined by that organization. Table 9-11 provides the IEEE 802.1 OUI (00-80-C2) encapsulation method encodings. A Default value of 0x00-80-C2-00 indicates that the IPL is using a separate physical or Aggregation link. A value of 1 indicates that Network / IPL sharing by time (9.3.2.1) is used. A value of 2 indicates that the encapsulation method used is the same as the one used by network frames and that Network / IPL sharing by tag (9.3.2.2) is used This managed object is applicable only when Network / IPL sharing by time (9.3.2.1) or Network / IPL sharing by tag (9.3.2.2) or Network / IPL sharing by encapsulation (9.3.2.3) is supported. The object identifies the value representing the encapsulation method that is used to transport IPL frames to the Neighbor Portal System when the IPL and network link are sharing the same physical link. It consists of the 3-octet OUI or CID identifying the organization that is responsible for this encapsulation and one following octet used to identify the encapsulation method defined by that organization. Table 9-11 provides the IEEE 802.1 OUI (00-80-C2) encapsulation method encodings. A Default value of 0x00-80-C2-00 indicates that the IPL is using a separate physical or Aggregation link. A value of 1 indicates that Network / IPL sharing by time (9.3.2.1) is used. A value of 2 indicates that the encapsulation method used is the same as the one used by network frames and that Network / IPL sharing by tag (9.3.2.2) is used

	"""
    def createDistributedRelay(self,
                               DrniName,
                               PortalAddress,
                               PortalSystemNumber,
                               IntfReflist,
                               IntfRef,
                               PortalPriority=32768,
                               GatewayAlgorithm='00-80-C2-01',
                               NeighborAdminDRCPState='00000000',
                               NeighborGatewayAlgorithm='00-80-C2-01',
                               ThreePortalSystem=False,
                               IntraPortalPortProtocolDA='01-80-C2-00-00-03',
                               NeighborPortAlgorithm='00-80-C2-01',
                               EncapMethod='00-80-C2-01'):
        obj =  { 
                'DrniName' : DrniName,
                'PortalAddress' : PortalAddress,
                'PortalSystemNumber' : int(PortalSystemNumber),
                'IntfReflist' : IntfReflist,
                'IntfRef' : IntfRef,
                'PortalPriority' : int(PortalPriority),
                'GatewayAlgorithm' : GatewayAlgorithm,
                'NeighborAdminDRCPState' : NeighborAdminDRCPState,
                'NeighborGatewayAlgorithm' : NeighborGatewayAlgorithm,
                'ThreePortalSystem' : True if ThreePortalSystem else False,
                'IntraPortalPortProtocolDA' : IntraPortalPortProtocolDA,
                'NeighborPortAlgorithm' : NeighborPortAlgorithm,
                'EncapMethod' : EncapMethod,
                }
        reqUrl =  self.cfgUrlBase+'DistributedRelay'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteDistributedRelay(self,
                               DrniName):
        obj =  { 
                'DrniName' : DrniName,
                }
        reqUrl =  self.cfgUrlBase+'DistributedRelay'
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteDistributedRelayById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'DistributedRelay'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        else:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        return r

    def updateDistributedRelay(self,
                               DrniName,
                               PortalAddress = None,
                               PortalSystemNumber = None,
                               IntfReflist = None,
                               IntfRef = None,
                               PortalPriority = None,
                               GatewayAlgorithm = None,
                               NeighborAdminDRCPState = None,
                               NeighborGatewayAlgorithm = None,
                               ThreePortalSystem = None,
                               IntraPortalPortProtocolDA = None,
                               NeighborPortAlgorithm = None,
                               EncapMethod = None):
        obj =  {}
        if DrniName != None :
            obj['DrniName'] = DrniName

        if PortalAddress != None :
            obj['PortalAddress'] = PortalAddress

        if PortalSystemNumber != None :
            obj['PortalSystemNumber'] = int(PortalSystemNumber)

        if IntfReflist != None :
            obj['IntfReflist'] = IntfReflist

        if IntfRef != None :
            obj['IntfRef'] = IntfRef

        if PortalPriority != None :
            obj['PortalPriority'] = int(PortalPriority)

        if GatewayAlgorithm != None :
            obj['GatewayAlgorithm'] = GatewayAlgorithm

        if NeighborAdminDRCPState != None :
            obj['NeighborAdminDRCPState'] = NeighborAdminDRCPState

        if NeighborGatewayAlgorithm != None :
            obj['NeighborGatewayAlgorithm'] = NeighborGatewayAlgorithm

        if ThreePortalSystem != None :
            obj['ThreePortalSystem'] = True if ThreePortalSystem else False

        if IntraPortalPortProtocolDA != None :
            obj['IntraPortalPortProtocolDA'] = IntraPortalPortProtocolDA

        if NeighborPortAlgorithm != None :
            obj['NeighborPortAlgorithm'] = NeighborPortAlgorithm

        if EncapMethod != None :
            obj['EncapMethod'] = EncapMethod

        reqUrl =  self.cfgUrlBase+'DistributedRelay'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateDistributedRelayById(self,
                                    objectId,
                                    PortalAddress = None,
                                    PortalSystemNumber = None,
                                    IntfReflist = None,
                                    IntfRef = None,
                                    PortalPriority = None,
                                    GatewayAlgorithm = None,
                                    NeighborAdminDRCPState = None,
                                    NeighborGatewayAlgorithm = None,
                                    ThreePortalSystem = None,
                                    IntraPortalPortProtocolDA = None,
                                    NeighborPortAlgorithm = None,
                                    EncapMethod = None):
        obj =  {}
        if PortalAddress !=  None:
            obj['PortalAddress'] = PortalAddress

        if PortalSystemNumber !=  None:
            obj['PortalSystemNumber'] = PortalSystemNumber

        if IntfReflist !=  None:
            obj['IntfReflist'] = IntfReflist

        if IntfRef !=  None:
            obj['IntfRef'] = IntfRef

        if PortalPriority !=  None:
            obj['PortalPriority'] = PortalPriority

        if GatewayAlgorithm !=  None:
            obj['GatewayAlgorithm'] = GatewayAlgorithm

        if NeighborAdminDRCPState !=  None:
            obj['NeighborAdminDRCPState'] = NeighborAdminDRCPState

        if NeighborGatewayAlgorithm !=  None:
            obj['NeighborGatewayAlgorithm'] = NeighborGatewayAlgorithm

        if ThreePortalSystem !=  None:
            obj['ThreePortalSystem'] = ThreePortalSystem

        if IntraPortalPortProtocolDA !=  None:
            obj['IntraPortalPortProtocolDA'] = IntraPortalPortProtocolDA

        if NeighborPortAlgorithm !=  None:
            obj['NeighborPortAlgorithm'] = NeighborPortAlgorithm

        if EncapMethod !=  None:
            obj['EncapMethod'] = EncapMethod

        reqUrl =  self.cfgUrlBase+'DistributedRelay'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateDistributedRelay(self,
                                    DrniName,
                                    op,
                                    path,
                                    value,):
        obj =  {}
        obj['DrniName'] = DrniName
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'DistributedRelay'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getDistributedRelay(self,
                            DrniName):
        obj =  { 
                'DrniName' : DrniName,
                }
        reqUrl =  self.cfgUrlBase + 'DistributedRelay'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getDistributedRelayById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'DistributedRelay'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllDistributedRelays(self):
        return self.getObjects('DistributedRelay', self.cfgUrlBase)


    """
    .. automethod :: createBGPPolicyCondition(self,
        :param string Name : Name of the BGP policy condition Name of the BGP policy condition
        :param string ConditionType : Type of the BGP policy condition. Type of the BGP policy condition.
        :param string IpPrefix : IP adddress to match in CIDR format IP adddress to match in CIDR format
        :param string MaskLengthRange : IP address mask lenght range to match IP address mask lenght range to match

	"""
    def createBGPPolicyCondition(self,
                                 Name,
                                 ConditionType,
                                 IpPrefix,
                                 MaskLengthRange):
        obj =  { 
                'Name' : Name,
                'ConditionType' : ConditionType,
                'IpPrefix' : IpPrefix,
                'MaskLengthRange' : MaskLengthRange,
                }
        reqUrl =  self.cfgUrlBase+'BGPPolicyCondition'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteBGPPolicyCondition(self,
                                 Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.cfgUrlBase+'BGPPolicyCondition'
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteBGPPolicyConditionById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'BGPPolicyCondition'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        else:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        return r

    def updateBGPPolicyCondition(self,
                                 Name,
                                 ConditionType = None,
                                 IpPrefix = None,
                                 MaskLengthRange = None):
        obj =  {}
        if Name != None :
            obj['Name'] = Name

        if ConditionType != None :
            obj['ConditionType'] = ConditionType

        if IpPrefix != None :
            obj['IpPrefix'] = IpPrefix

        if MaskLengthRange != None :
            obj['MaskLengthRange'] = MaskLengthRange

        reqUrl =  self.cfgUrlBase+'BGPPolicyCondition'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateBGPPolicyConditionById(self,
                                      objectId,
                                      ConditionType = None,
                                      IpPrefix = None,
                                      MaskLengthRange = None):
        obj =  {}
        if ConditionType !=  None:
            obj['ConditionType'] = ConditionType

        if IpPrefix !=  None:
            obj['IpPrefix'] = IpPrefix

        if MaskLengthRange !=  None:
            obj['MaskLengthRange'] = MaskLengthRange

        reqUrl =  self.cfgUrlBase+'BGPPolicyCondition'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateBGPPolicyCondition(self,
                                      Name,
                                      op,
                                      path,
                                      value,):
        obj =  {}
        obj['Name'] = Name
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'BGPPolicyCondition'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getBGPPolicyCondition(self,
                              Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.cfgUrlBase + 'BGPPolicyCondition'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getBGPPolicyConditionById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'BGPPolicyCondition'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllBGPPolicyConditions(self):
        return self.getObjects('BGPPolicyCondition', self.cfgUrlBase)


    """
    .. automethod :: createOspfGlobal(self,
        :param string RouterId : A 32-bit integer uniquely identifying the router in the Autonomous System. By convention A 32-bit integer uniquely identifying the router in the Autonomous System. By convention
        :param int32 AdminStat : Indicates if OSPF is enabled globally Indicates if OSPF is enabled globally
        :param bool ASBdrRtrStatus : A flag to note whether this router is configured as an Autonomous System Border Router.  This object is persistent and when written the entity SHOULD save the change to non-volatile storage. A flag to note whether this router is configured as an Autonomous System Border Router.  This object is persistent and when written the entity SHOULD save the change to non-volatile storage.
        :param int32 RestartSupport : *** This element is added for future use. *** The router's support for OSPF graceful restart. Options include *** This element is added for future use. *** The router's support for OSPF graceful restart. Options include
        :param int32 RestartInterval : *** This element is added for future use. *** Configured OSPF graceful restart timeout interval. This object is persistent and when written the entity SHOULD save the change to non-volatile storage. *** This element is added for future use. *** Configured OSPF graceful restart timeout interval. This object is persistent and when written the entity SHOULD save the change to non-volatile storage.
        :param bool TOSSupport : *** This element is added for future use. *** The router's support for type-of-service routing. This object is persistent and when written the entity SHOULD save the change to non-volatile storage. *** This element is added for future use. *** The router's support for type-of-service routing. This object is persistent and when written the entity SHOULD save the change to non-volatile storage.
        :param uint32 ReferenceBandwidth : Reference bandwidth in kilobits/second for calculating default interface metrics. Unit Reference bandwidth in kilobits/second for calculating default interface metrics. Unit

	"""
    def createOspfGlobal(self,
                         RouterId,
                         AdminStat,
                         ASBdrRtrStatus,
                         RestartSupport,
                         RestartInterval,
                         TOSSupport=False,
                         ReferenceBandwidth=100):
        obj =  { 
                'RouterId' : RouterId,
                'AdminStat' : int(AdminStat),
                'ASBdrRtrStatus' : True if ASBdrRtrStatus else False,
                'RestartSupport' : int(RestartSupport),
                'RestartInterval' : int(RestartInterval),
                'TOSSupport' : True if TOSSupport else False,
                'ReferenceBandwidth' : int(ReferenceBandwidth),
                }
        reqUrl =  self.cfgUrlBase+'OspfGlobal'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteOspfGlobal(self,
                         RouterId):
        obj =  { 
                'RouterId' : RouterId,
                }
        reqUrl =  self.cfgUrlBase+'OspfGlobal'
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteOspfGlobalById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'OspfGlobal'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        else:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        return r

    def updateOspfGlobal(self,
                         RouterId,
                         AdminStat = None,
                         ASBdrRtrStatus = None,
                         RestartSupport = None,
                         RestartInterval = None,
                         TOSSupport = None,
                         ReferenceBandwidth = None):
        obj =  {}
        if RouterId != None :
            obj['RouterId'] = RouterId

        if AdminStat != None :
            obj['AdminStat'] = int(AdminStat)

        if ASBdrRtrStatus != None :
            obj['ASBdrRtrStatus'] = True if ASBdrRtrStatus else False

        if RestartSupport != None :
            obj['RestartSupport'] = int(RestartSupport)

        if RestartInterval != None :
            obj['RestartInterval'] = int(RestartInterval)

        if TOSSupport != None :
            obj['TOSSupport'] = True if TOSSupport else False

        if ReferenceBandwidth != None :
            obj['ReferenceBandwidth'] = int(ReferenceBandwidth)

        reqUrl =  self.cfgUrlBase+'OspfGlobal'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateOspfGlobalById(self,
                              objectId,
                              AdminStat = None,
                              ASBdrRtrStatus = None,
                              RestartSupport = None,
                              RestartInterval = None,
                              TOSSupport = None,
                              ReferenceBandwidth = None):
        obj =  {}
        if AdminStat !=  None:
            obj['AdminStat'] = AdminStat

        if ASBdrRtrStatus !=  None:
            obj['ASBdrRtrStatus'] = ASBdrRtrStatus

        if RestartSupport !=  None:
            obj['RestartSupport'] = RestartSupport

        if RestartInterval !=  None:
            obj['RestartInterval'] = RestartInterval

        if TOSSupport !=  None:
            obj['TOSSupport'] = TOSSupport

        if ReferenceBandwidth !=  None:
            obj['ReferenceBandwidth'] = ReferenceBandwidth

        reqUrl =  self.cfgUrlBase+'OspfGlobal'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateOspfGlobal(self,
                              RouterId,
                              op,
                              path,
                              value,):
        obj =  {}
        obj['RouterId'] = RouterId
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'OspfGlobal'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getOspfGlobal(self,
                      RouterId):
        obj =  { 
                'RouterId' : RouterId,
                }
        reqUrl =  self.cfgUrlBase + 'OspfGlobal'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getOspfGlobalById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'OspfGlobal'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllOspfGlobals(self):
        return self.getObjects('OspfGlobal', self.cfgUrlBase)


    def getDhcpRelayHostDhcpState(self,
                                  MacAddr):
        obj =  { 
                'MacAddr' : MacAddr,
                }
        reqUrl =  self.stateUrlBase + 'DhcpRelayHostDhcp'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getDhcpRelayHostDhcpStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'DhcpRelayHostDhcp'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllDhcpRelayHostDhcpStates(self):
        return self.getObjects('DhcpRelayHostDhcp', self.stateUrlBase)


    def getDhcpRelayIntfServerState(self,
                                    IntfId):
        obj =  { 
                'IntfId' : int(IntfId),
                }
        reqUrl =  self.stateUrlBase + 'DhcpRelayIntfServer'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getDhcpRelayIntfServerStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'DhcpRelayIntfServer'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllDhcpRelayIntfServerStates(self):
        return self.getObjects('DhcpRelayIntfServer', self.stateUrlBase)


    """
    .. automethod :: executeResetBGPv4NeighborByInterface(self,
        :param string IntfRef : Interface of the BGP IPv4 neighbor to restart Interface of the BGP IPv4 neighbor to restart

	"""
    def executeResetBGPv4NeighborByInterface(self,
                                             IntfRef):
        obj =  { 
                'IntfRef' : IntfRef,
                }
        reqUrl =  self.actionUrlBase+'ResetBGPv4NeighborByInterface'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getLLDPIntfState(self,
                         IntfRef):
        obj =  { 
                'IntfRef' : IntfRef,
                }
        reqUrl =  self.stateUrlBase + 'LLDPIntf'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getLLDPIntfStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'LLDPIntf'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllLLDPIntfStates(self):
        return self.getObjects('LLDPIntf', self.stateUrlBase)


    def updateLed(self,
                  LedId,
                  LedAdmin = None,
                  LedSetColor = None):
        obj =  {}
        if LedId != None :
            obj['LedId'] = int(LedId)

        if LedAdmin != None :
            obj['LedAdmin'] = LedAdmin

        if LedSetColor != None :
            obj['LedSetColor'] = LedSetColor

        reqUrl =  self.cfgUrlBase+'Led'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateLedById(self,
                       objectId,
                       LedAdmin = None,
                       LedSetColor = None):
        obj =  {}
        if LedAdmin !=  None:
            obj['LedAdmin'] = LedAdmin

        if LedSetColor !=  None:
            obj['LedSetColor'] = LedSetColor

        reqUrl =  self.cfgUrlBase+'Led'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateLed(self,
                       LedId,
                       op,
                       path,
                       value,):
        obj =  {}
        obj['LedId'] = LedId
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'Led'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getLed(self,
               LedId):
        obj =  { 
                'LedId' : int(LedId),
                }
        reqUrl =  self.cfgUrlBase + 'Led'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getLedById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'Led'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllLeds(self):
        return self.getObjects('Led', self.cfgUrlBase)


    """
    .. automethod :: createPolicyDefinition(self,
        :param string Name : Policy Name Policy Name
        :param int32 Priority : Priority of the policy w.r.t other policies configured Priority of the policy w.r.t other policies configured
        :param PolicyDefinitionStmtPriority StatementList : Specifies list of statements along with their precedence order. Specifies list of statements along with their precedence order.
        :param string MatchType : Specifies whether to match all/any of the statements within this policy Specifies whether to match all/any of the statements within this policy
        :param string PolicyType : Specifies the intended protocol application for the policy Specifies the intended protocol application for the policy

	"""
    def createPolicyDefinition(self,
                               Name,
                               Priority,
                               StatementList,
                               MatchType='all',
                               PolicyType='ALL'):
        obj =  { 
                'Name' : Name,
                'Priority' : int(Priority),
                'StatementList' : StatementList,
                'MatchType' : MatchType,
                'PolicyType' : PolicyType,
                }
        reqUrl =  self.cfgUrlBase+'PolicyDefinition'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deletePolicyDefinition(self,
                               Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.cfgUrlBase+'PolicyDefinition'
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deletePolicyDefinitionById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'PolicyDefinition'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        else:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        return r

    def updatePolicyDefinition(self,
                               Name,
                               Priority = None,
                               StatementList = None,
                               MatchType = None,
                               PolicyType = None):
        obj =  {}
        if Name != None :
            obj['Name'] = Name

        if Priority != None :
            obj['Priority'] = int(Priority)

        if StatementList != None :
            obj['StatementList'] = StatementList

        if MatchType != None :
            obj['MatchType'] = MatchType

        if PolicyType != None :
            obj['PolicyType'] = PolicyType

        reqUrl =  self.cfgUrlBase+'PolicyDefinition'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updatePolicyDefinitionById(self,
                                    objectId,
                                    Priority = None,
                                    StatementList = None,
                                    MatchType = None,
                                    PolicyType = None):
        obj =  {}
        if Priority !=  None:
            obj['Priority'] = Priority

        if StatementList !=  None:
            obj['StatementList'] = StatementList

        if MatchType !=  None:
            obj['MatchType'] = MatchType

        if PolicyType !=  None:
            obj['PolicyType'] = PolicyType

        reqUrl =  self.cfgUrlBase+'PolicyDefinition'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdatePolicyDefinition(self,
                                    Name,
                                    op,
                                    path,
                                    value,):
        obj =  {}
        obj['Name'] = Name
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'PolicyDefinition'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getPolicyDefinition(self,
                            Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.cfgUrlBase + 'PolicyDefinition'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getPolicyDefinitionById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'PolicyDefinition'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllPolicyDefinitions(self):
        return self.getObjects('PolicyDefinition', self.cfgUrlBase)


    def getAclState(self,
                    AclName,
                    Direction):
        obj =  { 
                'AclName' : AclName,
                'Direction' : Direction,
                }
        reqUrl =  self.stateUrlBase + 'Acl'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getAclStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'Acl'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllAclStates(self):
        return self.getObjects('Acl', self.stateUrlBase)


    def updateEthernetPM(self,
                         Resource,
                         IntfRef,
                         PMClassBEnable = None,
                         PMClassCEnable = None,
                         HighWarnThreshold = None,
                         LowAlarmThreshold = None,
                         PMClassAEnable = None,
                         HighAlarmThreshold = None,
                         LowWarnThreshold = None):
        obj =  {}
        if Resource != None :
            obj['Resource'] = Resource

        if IntfRef != None :
            obj['IntfRef'] = IntfRef

        if PMClassBEnable != None :
            obj['PMClassBEnable'] = True if PMClassBEnable else False

        if PMClassCEnable != None :
            obj['PMClassCEnable'] = True if PMClassCEnable else False

        if HighWarnThreshold != None :
            obj['HighWarnThreshold'] = HighWarnThreshold

        if LowAlarmThreshold != None :
            obj['LowAlarmThreshold'] = LowAlarmThreshold

        if PMClassAEnable != None :
            obj['PMClassAEnable'] = True if PMClassAEnable else False

        if HighAlarmThreshold != None :
            obj['HighAlarmThreshold'] = HighAlarmThreshold

        if LowWarnThreshold != None :
            obj['LowWarnThreshold'] = LowWarnThreshold

        reqUrl =  self.cfgUrlBase+'EthernetPM'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateEthernetPMById(self,
                              objectId,
                              PMClassBEnable = None,
                              PMClassCEnable = None,
                              HighWarnThreshold = None,
                              LowAlarmThreshold = None,
                              PMClassAEnable = None,
                              HighAlarmThreshold = None,
                              LowWarnThreshold = None):
        obj =  {}
        if PMClassBEnable !=  None:
            obj['PMClassBEnable'] = PMClassBEnable

        if PMClassCEnable !=  None:
            obj['PMClassCEnable'] = PMClassCEnable

        if HighWarnThreshold !=  None:
            obj['HighWarnThreshold'] = HighWarnThreshold

        if LowAlarmThreshold !=  None:
            obj['LowAlarmThreshold'] = LowAlarmThreshold

        if PMClassAEnable !=  None:
            obj['PMClassAEnable'] = PMClassAEnable

        if HighAlarmThreshold !=  None:
            obj['HighAlarmThreshold'] = HighAlarmThreshold

        if LowWarnThreshold !=  None:
            obj['LowWarnThreshold'] = LowWarnThreshold

        reqUrl =  self.cfgUrlBase+'EthernetPM'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateEthernetPM(self,
                              Resource,
                              IntfRef,
                              op,
                              path,
                              value,):
        obj =  {}
        obj['Resource'] = Resource
        obj['IntfRef'] = IntfRef
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'EthernetPM'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getEthernetPM(self,
                      Resource,
                      IntfRef):
        obj =  { 
                'Resource' : Resource,
                'IntfRef' : IntfRef,
                }
        reqUrl =  self.cfgUrlBase + 'EthernetPM'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getEthernetPMById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'EthernetPM'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllEthernetPMs(self):
        return self.getObjects('EthernetPM', self.cfgUrlBase)


    def getOspfVirtNbrEntryState(self,
                                 VirtNbrRtrId,
                                 VirtNbrArea):
        obj =  { 
                'VirtNbrRtrId' : VirtNbrRtrId,
                'VirtNbrArea' : VirtNbrArea,
                }
        reqUrl =  self.stateUrlBase + 'OspfVirtNbrEntry'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getOspfVirtNbrEntryStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'OspfVirtNbrEntry'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllOspfVirtNbrEntryStates(self):
        return self.getObjects('OspfVirtNbrEntry', self.stateUrlBase)


    def getDWDMModuleClntIntfState(self,
                                   ClntIntfId,
                                   ModuleId):
        obj =  { 
                'ClntIntfId' : int(ClntIntfId),
                'ModuleId' : int(ModuleId),
                }
        reqUrl =  self.stateUrlBase + 'DWDMModuleClntIntf'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getDWDMModuleClntIntfStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'DWDMModuleClntIntf'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllDWDMModuleClntIntfStates(self):
        return self.getObjects('DWDMModuleClntIntf', self.stateUrlBase)


    def getRouteStatState(self,
                          Vrf):
        obj =  { 
                'Vrf' : Vrf,
                }
        reqUrl =  self.stateUrlBase + 'RouteStat'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getRouteStatStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'RouteStat'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllRouteStatStates(self):
        return self.getObjects('RouteStat', self.stateUrlBase)


    def getRouteDistanceState(self,
                              Protocol):
        obj =  { 
                'Protocol' : Protocol,
                }
        reqUrl =  self.stateUrlBase + 'RouteDistance'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getRouteDistanceStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'RouteDistance'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllRouteDistanceStates(self):
        return self.getObjects('RouteDistance', self.stateUrlBase)


    """
    .. automethod :: createLogicalIntf(self,
        :param string Name : Name of logical interface Name of logical interface
        :param string Type : Type of logical interface (e.x. loopback) Type of logical interface (e.x. loopback)

	"""
    def createLogicalIntf(self,
                          Name,
                          Type='Loopback'):
        obj =  { 
                'Name' : Name,
                'Type' : Type,
                }
        reqUrl =  self.cfgUrlBase+'LogicalIntf'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteLogicalIntf(self,
                          Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.cfgUrlBase+'LogicalIntf'
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteLogicalIntfById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'LogicalIntf'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        else:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        return r

    def updateLogicalIntf(self,
                          Name,
                          Type = None):
        obj =  {}
        if Name != None :
            obj['Name'] = Name

        if Type != None :
            obj['Type'] = Type

        reqUrl =  self.cfgUrlBase+'LogicalIntf'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateLogicalIntfById(self,
                               objectId,
                               Type = None):
        obj =  {}
        if Type !=  None:
            obj['Type'] = Type

        reqUrl =  self.cfgUrlBase+'LogicalIntf'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateLogicalIntf(self,
                               Name,
                               op,
                               path,
                               value,):
        obj =  {}
        obj['Name'] = Name
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'LogicalIntf'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getLogicalIntf(self,
                       Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.cfgUrlBase + 'LogicalIntf'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getLogicalIntfById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'LogicalIntf'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllLogicalIntfs(self):
        return self.getObjects('LogicalIntf', self.cfgUrlBase)


    def getBGPv6NeighborState(self,
                              IntfRef,
                              NeighborAddress):
        obj =  { 
                'IntfRef' : IntfRef,
                'NeighborAddress' : NeighborAddress,
                }
        reqUrl =  self.stateUrlBase + 'BGPv6Neighbor'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getBGPv6NeighborStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'BGPv6Neighbor'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllBGPv6NeighborStates(self):
        return self.getObjects('BGPv6Neighbor', self.stateUrlBase)


    def updateLacpGlobal(self,
                         Vrf,
                         AdminState = None):
        obj =  {}
        if Vrf != None :
            obj['Vrf'] = Vrf

        if AdminState != None :
            obj['AdminState'] = AdminState

        reqUrl =  self.cfgUrlBase+'LacpGlobal'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateLacpGlobalById(self,
                              objectId,
                              AdminState = None):
        obj =  {}
        if AdminState !=  None:
            obj['AdminState'] = AdminState

        reqUrl =  self.cfgUrlBase+'LacpGlobal'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateLacpGlobal(self,
                              Vrf,
                              op,
                              path,
                              value,):
        obj =  {}
        obj['Vrf'] = Vrf
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'LacpGlobal'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getLacpGlobal(self,
                      Vrf):
        obj =  { 
                'Vrf' : Vrf,
                }
        reqUrl =  self.cfgUrlBase + 'LacpGlobal'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getLacpGlobalById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'LacpGlobal'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllLacpGlobals(self):
        return self.getObjects('LacpGlobal', self.cfgUrlBase)


    """
    .. automethod :: executeForceApplyConfig(self,

	"""
    def executeForceApplyConfig(self):
        obj =  { 
                }
        reqUrl =  self.actionUrlBase+'ForceApplyConfig'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getMacTableEntryState(self,
                              MacAddr):
        obj =  { 
                'MacAddr' : MacAddr,
                }
        reqUrl =  self.stateUrlBase + 'MacTableEntry'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getMacTableEntryStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'MacTableEntry'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllMacTableEntryStates(self):
        return self.getObjects('MacTableEntry', self.stateUrlBase)


    def getFanSensorPMDataState(self,
                                Class,
                                Name):
        obj =  { 
                'Class' : Class,
                'Name' : Name,
                }
        reqUrl =  self.stateUrlBase + 'FanSensorPMData'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getFanSensorPMDataStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'FanSensorPMData'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllFanSensorPMDataStates(self):
        return self.getObjects('FanSensorPMData', self.stateUrlBase)


    def getOspfNbrEntryState(self,
                             NbrIpAddr,
                             NbrAddressLessIndex):
        obj =  { 
                'NbrIpAddr' : NbrIpAddr,
                'NbrAddressLessIndex' : int(NbrAddressLessIndex),
                }
        reqUrl =  self.stateUrlBase + 'OspfNbrEntry'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getOspfNbrEntryStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'OspfNbrEntry'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllOspfNbrEntryStates(self):
        return self.getObjects('OspfNbrEntry', self.stateUrlBase)


    def updateSystemParam(self,
                          Vrf,
                          MgmtIp = None,
                          Hostname = None,
                          SwitchMac = None,
                          SwVersion = None,
                          Description = None):
        obj =  {}
        if Vrf != None :
            obj['Vrf'] = Vrf

        if MgmtIp != None :
            obj['MgmtIp'] = MgmtIp

        if Hostname != None :
            obj['Hostname'] = Hostname

        if SwitchMac != None :
            obj['SwitchMac'] = SwitchMac

        if SwVersion != None :
            obj['SwVersion'] = SwVersion

        if Description != None :
            obj['Description'] = Description

        reqUrl =  self.cfgUrlBase+'SystemParam'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateSystemParamById(self,
                               objectId,
                               MgmtIp = None,
                               Hostname = None,
                               SwitchMac = None,
                               SwVersion = None,
                               Description = None):
        obj =  {}
        if MgmtIp !=  None:
            obj['MgmtIp'] = MgmtIp

        if Hostname !=  None:
            obj['Hostname'] = Hostname

        if SwitchMac !=  None:
            obj['SwitchMac'] = SwitchMac

        if SwVersion !=  None:
            obj['SwVersion'] = SwVersion

        if Description !=  None:
            obj['Description'] = Description

        reqUrl =  self.cfgUrlBase+'SystemParam'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateSystemParam(self,
                               Vrf,
                               op,
                               path,
                               value,):
        obj =  {}
        obj['Vrf'] = Vrf
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'SystemParam'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getSystemParam(self,
                       Vrf):
        obj =  { 
                'Vrf' : Vrf,
                }
        reqUrl =  self.cfgUrlBase + 'SystemParam'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getSystemParamById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'SystemParam'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllSystemParams(self):
        return self.getObjects('SystemParam', self.cfgUrlBase)


    def updateBfdGlobal(self,
                        Vrf,
                        Enable = None):
        obj =  {}
        if Vrf != None :
            obj['Vrf'] = Vrf

        if Enable != None :
            obj['Enable'] = True if Enable else False

        reqUrl =  self.cfgUrlBase+'BfdGlobal'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateBfdGlobalById(self,
                             objectId,
                             Enable = None):
        obj =  {}
        if Enable !=  None:
            obj['Enable'] = Enable

        reqUrl =  self.cfgUrlBase+'BfdGlobal'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateBfdGlobal(self,
                             Vrf,
                             op,
                             path,
                             value,):
        obj =  {}
        obj['Vrf'] = Vrf
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'BfdGlobal'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getBfdGlobal(self,
                     Vrf):
        obj =  { 
                'Vrf' : Vrf,
                }
        reqUrl =  self.cfgUrlBase + 'BfdGlobal'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getBfdGlobalById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'BfdGlobal'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllBfdGlobals(self):
        return self.getObjects('BfdGlobal', self.cfgUrlBase)


    """
    .. automethod :: executeResetBGPv6NeighborByInterface(self,
        :param string IntfRef : Interface of the BGP IPv6 neighbor to restart Interface of the BGP IPv6 neighbor to restart

	"""
    def executeResetBGPv6NeighborByInterface(self,
                                             IntfRef):
        obj =  { 
                'IntfRef' : IntfRef,
                }
        reqUrl =  self.actionUrlBase+'ResetBGPv6NeighborByInterface'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateVoltageSensor(self,
                            Name,
                            HigherAlarmThreshold = None,
                            HigherWarningThreshold = None,
                            LowerWarningThreshold = None,
                            LowerAlarmThreshold = None,
                            PMClassCAdminState = None,
                            PMClassAAdminState = None,
                            AdminState = None,
                            PMClassBAdminState = None):
        obj =  {}
        if Name != None :
            obj['Name'] = Name

        if HigherAlarmThreshold != None :
            obj['HigherAlarmThreshold'] = HigherAlarmThreshold

        if HigherWarningThreshold != None :
            obj['HigherWarningThreshold'] = HigherWarningThreshold

        if LowerWarningThreshold != None :
            obj['LowerWarningThreshold'] = LowerWarningThreshold

        if LowerAlarmThreshold != None :
            obj['LowerAlarmThreshold'] = LowerAlarmThreshold

        if PMClassCAdminState != None :
            obj['PMClassCAdminState'] = PMClassCAdminState

        if PMClassAAdminState != None :
            obj['PMClassAAdminState'] = PMClassAAdminState

        if AdminState != None :
            obj['AdminState'] = AdminState

        if PMClassBAdminState != None :
            obj['PMClassBAdminState'] = PMClassBAdminState

        reqUrl =  self.cfgUrlBase+'VoltageSensor'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateVoltageSensorById(self,
                                 objectId,
                                 HigherAlarmThreshold = None,
                                 HigherWarningThreshold = None,
                                 LowerWarningThreshold = None,
                                 LowerAlarmThreshold = None,
                                 PMClassCAdminState = None,
                                 PMClassAAdminState = None,
                                 AdminState = None,
                                 PMClassBAdminState = None):
        obj =  {}
        if HigherAlarmThreshold !=  None:
            obj['HigherAlarmThreshold'] = HigherAlarmThreshold

        if HigherWarningThreshold !=  None:
            obj['HigherWarningThreshold'] = HigherWarningThreshold

        if LowerWarningThreshold !=  None:
            obj['LowerWarningThreshold'] = LowerWarningThreshold

        if LowerAlarmThreshold !=  None:
            obj['LowerAlarmThreshold'] = LowerAlarmThreshold

        if PMClassCAdminState !=  None:
            obj['PMClassCAdminState'] = PMClassCAdminState

        if PMClassAAdminState !=  None:
            obj['PMClassAAdminState'] = PMClassAAdminState

        if AdminState !=  None:
            obj['AdminState'] = AdminState

        if PMClassBAdminState !=  None:
            obj['PMClassBAdminState'] = PMClassBAdminState

        reqUrl =  self.cfgUrlBase+'VoltageSensor'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateVoltageSensor(self,
                                 Name,
                                 op,
                                 path,
                                 value,):
        obj =  {}
        obj['Name'] = Name
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'VoltageSensor'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getVoltageSensor(self,
                         Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.cfgUrlBase + 'VoltageSensor'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getVoltageSensorById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'VoltageSensor'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllVoltageSensors(self):
        return self.getObjects('VoltageSensor', self.cfgUrlBase)


    def getAlarmState(self,
                      EventId,
                      EventName,
                      SrcObjName,
                      OwnerName,
                      OwnerId):
        obj =  { 
                'EventId' : int(EventId),
                'EventName' : EventName,
                'SrcObjName' : SrcObjName,
                'OwnerName' : OwnerName,
                'OwnerId' : int(OwnerId),
                }
        reqUrl =  self.stateUrlBase + 'Alarm'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getAlarmStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'Alarm'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllAlarmStates(self):
        return self.getObjects('Alarm', self.stateUrlBase)


    def getQsfpPMDataState(self,
                           Resource,
                           Class,
                           QsfpId):
        obj =  { 
                'Resource' : Resource,
                'Class' : Class,
                'QsfpId' : int(QsfpId),
                }
        reqUrl =  self.stateUrlBase + 'QsfpPMData'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getQsfpPMDataStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'QsfpPMData'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllQsfpPMDataStates(self):
        return self.getObjects('QsfpPMData', self.stateUrlBase)


    def getAclRuleState(self,
                        RuleName):
        obj =  { 
                'RuleName' : RuleName,
                }
        reqUrl =  self.stateUrlBase + 'AclRule'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getAclRuleStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'AclRule'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllAclRuleStates(self):
        return self.getObjects('AclRule', self.stateUrlBase)


    """
    .. automethod :: createBGPPolicyStmt(self,
        :param string Name : Name of the BGP policy statement Name of the BGP policy statement
        :param string MatchConditions : Match conditions all/any Match conditions all/any
        :param string Conditions : List of conditions List of conditions
        :param string Actions : List of actions List of actions

	"""
    def createBGPPolicyStmt(self,
                            Name,
                            MatchConditions,
                            Conditions,
                            Actions):
        obj =  { 
                'Name' : Name,
                'MatchConditions' : MatchConditions,
                'Conditions' : Conditions,
                'Actions' : Actions,
                }
        reqUrl =  self.cfgUrlBase+'BGPPolicyStmt'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteBGPPolicyStmt(self,
                            Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.cfgUrlBase+'BGPPolicyStmt'
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteBGPPolicyStmtById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'BGPPolicyStmt'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        else:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        return r

    def updateBGPPolicyStmt(self,
                            Name,
                            MatchConditions = None,
                            Conditions = None,
                            Actions = None):
        obj =  {}
        if Name != None :
            obj['Name'] = Name

        if MatchConditions != None :
            obj['MatchConditions'] = MatchConditions

        if Conditions != None :
            obj['Conditions'] = Conditions

        if Actions != None :
            obj['Actions'] = Actions

        reqUrl =  self.cfgUrlBase+'BGPPolicyStmt'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateBGPPolicyStmtById(self,
                                 objectId,
                                 MatchConditions = None,
                                 Conditions = None,
                                 Actions = None):
        obj =  {}
        if MatchConditions !=  None:
            obj['MatchConditions'] = MatchConditions

        if Conditions !=  None:
            obj['Conditions'] = Conditions

        if Actions !=  None:
            obj['Actions'] = Actions

        reqUrl =  self.cfgUrlBase+'BGPPolicyStmt'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateBGPPolicyStmt(self,
                                 Name,
                                 op,
                                 path,
                                 value,):
        obj =  {}
        obj['Name'] = Name
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'BGPPolicyStmt'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getBGPPolicyStmt(self,
                         Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.cfgUrlBase + 'BGPPolicyStmt'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getBGPPolicyStmtById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'BGPPolicyStmt'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllBGPPolicyStmts(self):
        return self.getObjects('BGPPolicyStmt', self.cfgUrlBase)


    def updateAsicGlobalPM(self,
                           Resource,
                           ModuleId,
                           PMClassBEnable = None,
                           HighWarnThreshold = None,
                           LowAlarmThreshold = None,
                           PMClassCEnable = None,
                           PMClassAEnable = None,
                           LowWarnThreshold = None,
                           HighAlarmThreshold = None):
        obj =  {}
        if Resource != None :
            obj['Resource'] = Resource

        if ModuleId != None :
            obj['ModuleId'] = int(ModuleId)

        if PMClassBEnable != None :
            obj['PMClassBEnable'] = True if PMClassBEnable else False

        if HighWarnThreshold != None :
            obj['HighWarnThreshold'] = HighWarnThreshold

        if LowAlarmThreshold != None :
            obj['LowAlarmThreshold'] = LowAlarmThreshold

        if PMClassCEnable != None :
            obj['PMClassCEnable'] = True if PMClassCEnable else False

        if PMClassAEnable != None :
            obj['PMClassAEnable'] = True if PMClassAEnable else False

        if LowWarnThreshold != None :
            obj['LowWarnThreshold'] = LowWarnThreshold

        if HighAlarmThreshold != None :
            obj['HighAlarmThreshold'] = HighAlarmThreshold

        reqUrl =  self.cfgUrlBase+'AsicGlobalPM'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateAsicGlobalPMById(self,
                                objectId,
                                PMClassBEnable = None,
                                HighWarnThreshold = None,
                                LowAlarmThreshold = None,
                                PMClassCEnable = None,
                                PMClassAEnable = None,
                                LowWarnThreshold = None,
                                HighAlarmThreshold = None):
        obj =  {}
        if PMClassBEnable !=  None:
            obj['PMClassBEnable'] = PMClassBEnable

        if HighWarnThreshold !=  None:
            obj['HighWarnThreshold'] = HighWarnThreshold

        if LowAlarmThreshold !=  None:
            obj['LowAlarmThreshold'] = LowAlarmThreshold

        if PMClassCEnable !=  None:
            obj['PMClassCEnable'] = PMClassCEnable

        if PMClassAEnable !=  None:
            obj['PMClassAEnable'] = PMClassAEnable

        if LowWarnThreshold !=  None:
            obj['LowWarnThreshold'] = LowWarnThreshold

        if HighAlarmThreshold !=  None:
            obj['HighAlarmThreshold'] = HighAlarmThreshold

        reqUrl =  self.cfgUrlBase+'AsicGlobalPM'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateAsicGlobalPM(self,
                                Resource,
                                ModuleId,
                                op,
                                path,
                                value,):
        obj =  {}
        obj['Resource'] = Resource
        obj['ModuleId'] = ModuleId
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'AsicGlobalPM'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getAsicGlobalPM(self,
                        Resource,
                        ModuleId):
        obj =  { 
                'Resource' : Resource,
                'ModuleId' : int(ModuleId),
                }
        reqUrl =  self.cfgUrlBase + 'AsicGlobalPM'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getAsicGlobalPMById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'AsicGlobalPM'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllAsicGlobalPMs(self):
        return self.getObjects('AsicGlobalPM', self.cfgUrlBase)


    def getIPv4RouteHwState(self,
                            DestinationNw):
        obj =  { 
                'DestinationNw' : DestinationNw,
                }
        reqUrl =  self.stateUrlBase + 'IPv4RouteHw'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getIPv4RouteHwStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'IPv4RouteHw'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllIPv4RouteHwStates(self):
        return self.getObjects('IPv4RouteHw', self.stateUrlBase)


    def updateArpGlobal(self,
                        Vrf,
                        Timeout = None):
        obj =  {}
        if Vrf != None :
            obj['Vrf'] = Vrf

        if Timeout != None :
            obj['Timeout'] = int(Timeout)

        reqUrl =  self.cfgUrlBase+'ArpGlobal'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateArpGlobalById(self,
                             objectId,
                             Timeout = None):
        obj =  {}
        if Timeout !=  None:
            obj['Timeout'] = Timeout

        reqUrl =  self.cfgUrlBase+'ArpGlobal'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateArpGlobal(self,
                             Vrf,
                             op,
                             path,
                             value,):
        obj =  {}
        obj['Vrf'] = Vrf
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'ArpGlobal'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getArpGlobal(self,
                     Vrf):
        obj =  { 
                'Vrf' : Vrf,
                }
        reqUrl =  self.cfgUrlBase + 'ArpGlobal'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getArpGlobalById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'ArpGlobal'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllArpGlobals(self):
        return self.getObjects('ArpGlobal', self.cfgUrlBase)


    """
    .. automethod :: createBGPv4PeerGroup(self,
        :param string Name : Name of the BGP peer group Name of the BGP peer group
        :param string PeerAS : Peer AS of the BGP neighbor Peer AS of the BGP neighbor
        :param string LocalAS : Local AS of the BGP neighbor Local AS of the BGP neighbor
        :param string UpdateSource : Source IP to connect to the BGP neighbor Source IP to connect to the BGP neighbor
        :param string AuthPassword : Password to connect to the BGP neighbor Password to connect to the BGP neighbor
        :param string Description : Description of the BGP neighbor Description of the BGP neighbor
        :param string AdjRIBInFilter : Policy that is applied for Adj-RIB-In prefix filtering Policy that is applied for Adj-RIB-In prefix filtering
        :param string AdjRIBOutFilter : Policy that is applied for Adj-RIB-Out prefix filtering Policy that is applied for Adj-RIB-Out prefix filtering
        :param uint8 MaxPrefixesRestartTimer : Time to wait before we start BGP peer session when we receive max prefixes Time to wait before we start BGP peer session when we receive max prefixes
        :param bool MultiHopEnable : Enable/Disable multi hop for BGP neighbor Enable/Disable multi hop for BGP neighbor
        :param bool MaxPrefixesDisconnect : Disconnect the BGP peer session when we receive the max prefixes from the neighbor Disconnect the BGP peer session when we receive the max prefixes from the neighbor
        :param uint8 MultiHopTTL : TTL for multi hop BGP neighbor TTL for multi hop BGP neighbor
        :param uint32 KeepaliveTime : Keep alive time for the BGP neighbor Keep alive time for the BGP neighbor
        :param uint32 RouteReflectorClusterId : Cluster Id of the internal BGP neighbor route reflector client Cluster Id of the internal BGP neighbor route reflector client
        :param uint32 MaxPrefixes : Maximum number of prefixes that can be received from the BGP neighbor Maximum number of prefixes that can be received from the BGP neighbor
        :param uint8 AddPathsMaxTx : Max number of additional paths that can be transmitted to BGP neighbor Max number of additional paths that can be transmitted to BGP neighbor
        :param bool AddPathsRx : Receive additional paths from BGP neighbor Receive additional paths from BGP neighbor
        :param bool RouteReflectorClient : Set/Clear BGP neighbor as a route reflector client Set/Clear BGP neighbor as a route reflector client
        :param uint8 MaxPrefixesThresholdPct : The percentage of maximum prefixes before we start logging The percentage of maximum prefixes before we start logging
        :param uint32 HoldTime : Hold time for the BGP neighbor Hold time for the BGP neighbor
        :param uint32 ConnectRetryTime : Connect retry time to connect to BGP neighbor after disconnect Connect retry time to connect to BGP neighbor after disconnect

	"""
    def createBGPv4PeerGroup(self,
                             Name,
                             PeerAS='',
                             LocalAS='',
                             UpdateSource='',
                             AuthPassword='',
                             Description='',
                             AdjRIBInFilter='',
                             AdjRIBOutFilter='',
                             MaxPrefixesRestartTimer=0,
                             MultiHopEnable=False,
                             MaxPrefixesDisconnect=False,
                             MultiHopTTL=0,
                             KeepaliveTime=0,
                             RouteReflectorClusterId=0,
                             MaxPrefixes=0,
                             AddPathsMaxTx=0,
                             AddPathsRx=False,
                             RouteReflectorClient=False,
                             MaxPrefixesThresholdPct=80,
                             HoldTime=0,
                             ConnectRetryTime=0):
        obj =  { 
                'Name' : Name,
                'PeerAS' : PeerAS,
                'LocalAS' : LocalAS,
                'UpdateSource' : UpdateSource,
                'AuthPassword' : AuthPassword,
                'Description' : Description,
                'AdjRIBInFilter' : AdjRIBInFilter,
                'AdjRIBOutFilter' : AdjRIBOutFilter,
                'MaxPrefixesRestartTimer' : int(MaxPrefixesRestartTimer),
                'MultiHopEnable' : True if MultiHopEnable else False,
                'MaxPrefixesDisconnect' : True if MaxPrefixesDisconnect else False,
                'MultiHopTTL' : int(MultiHopTTL),
                'KeepaliveTime' : int(KeepaliveTime),
                'RouteReflectorClusterId' : int(RouteReflectorClusterId),
                'MaxPrefixes' : int(MaxPrefixes),
                'AddPathsMaxTx' : int(AddPathsMaxTx),
                'AddPathsRx' : True if AddPathsRx else False,
                'RouteReflectorClient' : True if RouteReflectorClient else False,
                'MaxPrefixesThresholdPct' : int(MaxPrefixesThresholdPct),
                'HoldTime' : int(HoldTime),
                'ConnectRetryTime' : int(ConnectRetryTime),
                }
        reqUrl =  self.cfgUrlBase+'BGPv4PeerGroup'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteBGPv4PeerGroup(self,
                             Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.cfgUrlBase+'BGPv4PeerGroup'
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteBGPv4PeerGroupById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'BGPv4PeerGroup'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        else:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        return r

    def updateBGPv4PeerGroup(self,
                             Name,
                             PeerAS = None,
                             LocalAS = None,
                             UpdateSource = None,
                             AuthPassword = None,
                             Description = None,
                             AdjRIBInFilter = None,
                             AdjRIBOutFilter = None,
                             MaxPrefixesRestartTimer = None,
                             MultiHopEnable = None,
                             MaxPrefixesDisconnect = None,
                             MultiHopTTL = None,
                             KeepaliveTime = None,
                             RouteReflectorClusterId = None,
                             MaxPrefixes = None,
                             AddPathsMaxTx = None,
                             AddPathsRx = None,
                             RouteReflectorClient = None,
                             MaxPrefixesThresholdPct = None,
                             HoldTime = None,
                             ConnectRetryTime = None):
        obj =  {}
        if Name != None :
            obj['Name'] = Name

        if PeerAS != None :
            obj['PeerAS'] = PeerAS

        if LocalAS != None :
            obj['LocalAS'] = LocalAS

        if UpdateSource != None :
            obj['UpdateSource'] = UpdateSource

        if AuthPassword != None :
            obj['AuthPassword'] = AuthPassword

        if Description != None :
            obj['Description'] = Description

        if AdjRIBInFilter != None :
            obj['AdjRIBInFilter'] = AdjRIBInFilter

        if AdjRIBOutFilter != None :
            obj['AdjRIBOutFilter'] = AdjRIBOutFilter

        if MaxPrefixesRestartTimer != None :
            obj['MaxPrefixesRestartTimer'] = int(MaxPrefixesRestartTimer)

        if MultiHopEnable != None :
            obj['MultiHopEnable'] = True if MultiHopEnable else False

        if MaxPrefixesDisconnect != None :
            obj['MaxPrefixesDisconnect'] = True if MaxPrefixesDisconnect else False

        if MultiHopTTL != None :
            obj['MultiHopTTL'] = int(MultiHopTTL)

        if KeepaliveTime != None :
            obj['KeepaliveTime'] = int(KeepaliveTime)

        if RouteReflectorClusterId != None :
            obj['RouteReflectorClusterId'] = int(RouteReflectorClusterId)

        if MaxPrefixes != None :
            obj['MaxPrefixes'] = int(MaxPrefixes)

        if AddPathsMaxTx != None :
            obj['AddPathsMaxTx'] = int(AddPathsMaxTx)

        if AddPathsRx != None :
            obj['AddPathsRx'] = True if AddPathsRx else False

        if RouteReflectorClient != None :
            obj['RouteReflectorClient'] = True if RouteReflectorClient else False

        if MaxPrefixesThresholdPct != None :
            obj['MaxPrefixesThresholdPct'] = int(MaxPrefixesThresholdPct)

        if HoldTime != None :
            obj['HoldTime'] = int(HoldTime)

        if ConnectRetryTime != None :
            obj['ConnectRetryTime'] = int(ConnectRetryTime)

        reqUrl =  self.cfgUrlBase+'BGPv4PeerGroup'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateBGPv4PeerGroupById(self,
                                  objectId,
                                  PeerAS = None,
                                  LocalAS = None,
                                  UpdateSource = None,
                                  AuthPassword = None,
                                  Description = None,
                                  AdjRIBInFilter = None,
                                  AdjRIBOutFilter = None,
                                  MaxPrefixesRestartTimer = None,
                                  MultiHopEnable = None,
                                  MaxPrefixesDisconnect = None,
                                  MultiHopTTL = None,
                                  KeepaliveTime = None,
                                  RouteReflectorClusterId = None,
                                  MaxPrefixes = None,
                                  AddPathsMaxTx = None,
                                  AddPathsRx = None,
                                  RouteReflectorClient = None,
                                  MaxPrefixesThresholdPct = None,
                                  HoldTime = None,
                                  ConnectRetryTime = None):
        obj =  {}
        if PeerAS !=  None:
            obj['PeerAS'] = PeerAS

        if LocalAS !=  None:
            obj['LocalAS'] = LocalAS

        if UpdateSource !=  None:
            obj['UpdateSource'] = UpdateSource

        if AuthPassword !=  None:
            obj['AuthPassword'] = AuthPassword

        if Description !=  None:
            obj['Description'] = Description

        if AdjRIBInFilter !=  None:
            obj['AdjRIBInFilter'] = AdjRIBInFilter

        if AdjRIBOutFilter !=  None:
            obj['AdjRIBOutFilter'] = AdjRIBOutFilter

        if MaxPrefixesRestartTimer !=  None:
            obj['MaxPrefixesRestartTimer'] = MaxPrefixesRestartTimer

        if MultiHopEnable !=  None:
            obj['MultiHopEnable'] = MultiHopEnable

        if MaxPrefixesDisconnect !=  None:
            obj['MaxPrefixesDisconnect'] = MaxPrefixesDisconnect

        if MultiHopTTL !=  None:
            obj['MultiHopTTL'] = MultiHopTTL

        if KeepaliveTime !=  None:
            obj['KeepaliveTime'] = KeepaliveTime

        if RouteReflectorClusterId !=  None:
            obj['RouteReflectorClusterId'] = RouteReflectorClusterId

        if MaxPrefixes !=  None:
            obj['MaxPrefixes'] = MaxPrefixes

        if AddPathsMaxTx !=  None:
            obj['AddPathsMaxTx'] = AddPathsMaxTx

        if AddPathsRx !=  None:
            obj['AddPathsRx'] = AddPathsRx

        if RouteReflectorClient !=  None:
            obj['RouteReflectorClient'] = RouteReflectorClient

        if MaxPrefixesThresholdPct !=  None:
            obj['MaxPrefixesThresholdPct'] = MaxPrefixesThresholdPct

        if HoldTime !=  None:
            obj['HoldTime'] = HoldTime

        if ConnectRetryTime !=  None:
            obj['ConnectRetryTime'] = ConnectRetryTime

        reqUrl =  self.cfgUrlBase+'BGPv4PeerGroup'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateBGPv4PeerGroup(self,
                                  Name,
                                  op,
                                  path,
                                  value,):
        obj =  {}
        obj['Name'] = Name
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'BGPv4PeerGroup'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getBGPv4PeerGroup(self,
                          Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.cfgUrlBase + 'BGPv4PeerGroup'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getBGPv4PeerGroupById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'BGPv4PeerGroup'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllBGPv4PeerGroups(self):
        return self.getObjects('BGPv4PeerGroup', self.cfgUrlBase)


    def getIPv4RouteState(self,
                          DestinationNw):
        obj =  { 
                'DestinationNw' : DestinationNw,
                }
        reqUrl =  self.stateUrlBase + 'IPv4Route'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getIPv4RouteStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'IPv4Route'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllIPv4RouteStates(self):
        return self.getObjects('IPv4Route', self.stateUrlBase)


    def getPowerConverterSensorState(self,
                                     Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.stateUrlBase + 'PowerConverterSensor'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getPowerConverterSensorStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'PowerConverterSensor'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllPowerConverterSensorStates(self):
        return self.getObjects('PowerConverterSensor', self.stateUrlBase)


    def getQsfpState(self,
                     QsfpId):
        obj =  { 
                'QsfpId' : int(QsfpId),
                }
        reqUrl =  self.stateUrlBase + 'Qsfp'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getQsfpStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'Qsfp'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllQsfpStates(self):
        return self.getObjects('Qsfp', self.stateUrlBase)


    def getBfdGlobalState(self,
                          Vrf):
        obj =  { 
                'Vrf' : Vrf,
                }
        reqUrl =  self.stateUrlBase + 'BfdGlobal'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getBfdGlobalStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'BfdGlobal'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllBfdGlobalStates(self):
        return self.getObjects('BfdGlobal', self.stateUrlBase)


    """
    .. automethod :: executeNdpDeleteByIfName(self,
        :param string IfName : All the NDP learned for end host on given L3 interface will be deleted All the NDP learned for end host on given L3 interface will be deleted

	"""
    def executeNdpDeleteByIfName(self,
                                 IfName):
        obj =  { 
                'IfName' : IfName,
                }
        reqUrl =  self.actionUrlBase+'NdpDeleteByIfName'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getQsfpChannelState(self,
                            ChannelNum,
                            QsfpId):
        obj =  { 
                'ChannelNum' : int(ChannelNum),
                'QsfpId' : int(QsfpId),
                }
        reqUrl =  self.stateUrlBase + 'QsfpChannel'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getQsfpChannelStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'QsfpChannel'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllQsfpChannelStates(self):
        return self.getObjects('QsfpChannel', self.stateUrlBase)


    def getFanState(self,
                    FanId):
        obj =  { 
                'FanId' : int(FanId),
                }
        reqUrl =  self.stateUrlBase + 'Fan'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getFanStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'Fan'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllFanStates(self):
        return self.getObjects('Fan', self.stateUrlBase)


    """
    .. automethod :: executeFaultClear(self,
        :param string OwnerName : Fault owner name Fault owner name
        :param string EventName : Fault event name Fault event name
        :param string SrcObjUUID : Source object Key UUID Source object Key UUID

	"""
    def executeFaultClear(self,
                          OwnerName,
                          EventName,
                          SrcObjUUID):
        obj =  { 
                'OwnerName' : OwnerName,
                'EventName' : EventName,
                'SrcObjUUID' : SrcObjUUID,
                }
        reqUrl =  self.actionUrlBase+'FaultClear'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    """
    .. automethod :: executeResetConfig(self,

	"""
    def executeResetConfig(self):
        obj =  { 
                }
        reqUrl =  self.actionUrlBase+'ResetConfig'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getBGPGlobalState(self,
                          RouterId):
        obj =  { 
                'RouterId' : RouterId,
                }
        reqUrl =  self.stateUrlBase + 'BGPGlobal'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getBGPGlobalStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'BGPGlobal'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllBGPGlobalStates(self):
        return self.getObjects('BGPGlobal', self.stateUrlBase)


    def getBfdSessionState(self,
                           IpAddr):
        obj =  { 
                'IpAddr' : IpAddr,
                }
        reqUrl =  self.stateUrlBase + 'BfdSession'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getBfdSessionStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'BfdSession'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllBfdSessionStates(self):
        return self.getObjects('BfdSession', self.stateUrlBase)


    def getOspfEventState(self,
                          Index):
        obj =  { 
                'Index' : int(Index),
                }
        reqUrl =  self.stateUrlBase + 'OspfEvent'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getOspfEventStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'OspfEvent'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllOspfEventStates(self):
        return self.getObjects('OspfEvent', self.stateUrlBase)


    def updateLLDPIntf(self,
                       IntfRef,
                       Enable = None,
                       TxRxMode = None):
        obj =  {}
        if IntfRef != None :
            obj['IntfRef'] = IntfRef

        if Enable != None :
            obj['Enable'] = True if Enable else False

        if TxRxMode != None :
            obj['TxRxMode'] = TxRxMode

        reqUrl =  self.cfgUrlBase+'LLDPIntf'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateLLDPIntfById(self,
                            objectId,
                            Enable = None,
                            TxRxMode = None):
        obj =  {}
        if Enable !=  None:
            obj['Enable'] = Enable

        if TxRxMode !=  None:
            obj['TxRxMode'] = TxRxMode

        reqUrl =  self.cfgUrlBase+'LLDPIntf'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateLLDPIntf(self,
                            IntfRef,
                            op,
                            path,
                            value,):
        obj =  {}
        obj['IntfRef'] = IntfRef
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'LLDPIntf'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getLLDPIntf(self,
                    IntfRef):
        obj =  { 
                'IntfRef' : IntfRef,
                }
        reqUrl =  self.cfgUrlBase + 'LLDPIntf'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getLLDPIntfById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'LLDPIntf'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllLLDPIntfs(self):
        return self.getObjects('LLDPIntf', self.cfgUrlBase)


    def getBufferGlobalStatState(self,
                                 DeviceId):
        obj =  { 
                'DeviceId' : int(DeviceId),
                }
        reqUrl =  self.stateUrlBase + 'BufferGlobalStat'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getBufferGlobalStatStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'BufferGlobalStat'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllBufferGlobalStatStates(self):
        return self.getObjects('BufferGlobalStat', self.stateUrlBase)


    def getIPv6IntfState(self,
                         IntfRef):
        obj =  { 
                'IntfRef' : IntfRef,
                }
        reqUrl =  self.stateUrlBase + 'IPv6Intf'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getIPv6IntfStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'IPv6Intf'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllIPv6IntfStates(self):
        return self.getObjects('IPv6Intf', self.stateUrlBase)


    """
    .. automethod :: createIPv4Intf(self,
        :param string IntfRef : Interface name or ifindex of port/lag or vlan on which this IPv4 object is configured Interface name or ifindex of port/lag or vlan on which this IPv4 object is configured
        :param string IpAddr : Interface IP/Net mask in CIDR format to provision on switch interface Interface IP/Net mask in CIDR format to provision on switch interface
        :param string AdminState : Administrative state of this IP interface Administrative state of this IP interface

	"""
    def createIPv4Intf(self,
                       IntfRef,
                       IpAddr,
                       AdminState='UP'):
        obj =  { 
                'IntfRef' : IntfRef,
                'IpAddr' : IpAddr,
                'AdminState' : AdminState,
                }
        reqUrl =  self.cfgUrlBase+'IPv4Intf'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteIPv4Intf(self,
                       IntfRef):
        obj =  { 
                'IntfRef' : IntfRef,
                }
        reqUrl =  self.cfgUrlBase+'IPv4Intf'
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteIPv4IntfById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'IPv4Intf'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        else:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        return r

    def updateIPv4Intf(self,
                       IntfRef,
                       IpAddr = None,
                       AdminState = None):
        obj =  {}
        if IntfRef != None :
            obj['IntfRef'] = IntfRef

        if IpAddr != None :
            obj['IpAddr'] = IpAddr

        if AdminState != None :
            obj['AdminState'] = AdminState

        reqUrl =  self.cfgUrlBase+'IPv4Intf'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateIPv4IntfById(self,
                            objectId,
                            IpAddr = None,
                            AdminState = None):
        obj =  {}
        if IpAddr !=  None:
            obj['IpAddr'] = IpAddr

        if AdminState !=  None:
            obj['AdminState'] = AdminState

        reqUrl =  self.cfgUrlBase+'IPv4Intf'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateIPv4Intf(self,
                            IntfRef,
                            op,
                            path,
                            value,):
        obj =  {}
        obj['IntfRef'] = IntfRef
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'IPv4Intf'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getIPv4Intf(self,
                    IntfRef):
        obj =  { 
                'IntfRef' : IntfRef,
                }
        reqUrl =  self.cfgUrlBase + 'IPv4Intf'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getIPv4IntfById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'IPv4Intf'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllIPv4Intfs(self):
        return self.getObjects('IPv4Intf', self.cfgUrlBase)


    def getPolicyStmtState(self,
                           Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.stateUrlBase + 'PolicyStmt'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getPolicyStmtStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'PolicyStmt'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllPolicyStmtStates(self):
        return self.getObjects('PolicyStmt', self.stateUrlBase)


    def getPowerConverterSensorPMDataState(self,
                                           Class,
                                           Name):
        obj =  { 
                'Class' : Class,
                'Name' : Name,
                }
        reqUrl =  self.stateUrlBase + 'PowerConverterSensorPMData'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getPowerConverterSensorPMDataStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'PowerConverterSensorPMData'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllPowerConverterSensorPMDataStates(self):
        return self.getObjects('PowerConverterSensorPMData', self.stateUrlBase)


    """
    .. automethod :: createIPv6Route(self,
        :param string DestinationNw : IP address of the route IP address of the route
        :param string NetworkMask : mask of the route mask of the route
        :param NextHopInfo NextHop :  
        :param string Protocol : Protocol type of the route Protocol type of the route
        :param bool NullRoute : Specify if this is a null route Specify if this is a null route
        :param uint32 Cost : Cost of this route Cost of this route

	"""
    def createIPv6Route(self,
                        DestinationNw,
                        NetworkMask,
                        NextHop,
                        Protocol='STATIC',
                        NullRoute=False,
                        Cost=0):
        obj =  { 
                'DestinationNw' : DestinationNw,
                'NetworkMask' : NetworkMask,
                'NextHop' : NextHop,
                'Protocol' : Protocol,
                'NullRoute' : True if NullRoute else False,
                'Cost' : int(Cost),
                }
        reqUrl =  self.cfgUrlBase+'IPv6Route'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteIPv6Route(self,
                        DestinationNw,
                        NetworkMask):
        obj =  { 
                'DestinationNw' : DestinationNw,
                'NetworkMask' : NetworkMask,
                }
        reqUrl =  self.cfgUrlBase+'IPv6Route'
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteIPv6RouteById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'IPv6Route'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        else:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        return r

    def updateIPv6Route(self,
                        DestinationNw,
                        NetworkMask,
                        NextHop = None,
                        Protocol = None,
                        NullRoute = None,
                        Cost = None):
        obj =  {}
        if DestinationNw != None :
            obj['DestinationNw'] = DestinationNw

        if NetworkMask != None :
            obj['NetworkMask'] = NetworkMask

        if NextHop != None :
            obj['NextHop'] = NextHop

        if Protocol != None :
            obj['Protocol'] = Protocol

        if NullRoute != None :
            obj['NullRoute'] = True if NullRoute else False

        if Cost != None :
            obj['Cost'] = int(Cost)

        reqUrl =  self.cfgUrlBase+'IPv6Route'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateIPv6RouteById(self,
                             objectId,
                             NextHop = None,
                             Protocol = None,
                             NullRoute = None,
                             Cost = None):
        obj =  {}
        if NextHop !=  None:
            obj['NextHop'] = NextHop

        if Protocol !=  None:
            obj['Protocol'] = Protocol

        if NullRoute !=  None:
            obj['NullRoute'] = NullRoute

        if Cost !=  None:
            obj['Cost'] = Cost

        reqUrl =  self.cfgUrlBase+'IPv6Route'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateIPv6Route(self,
                             DestinationNw,
                             NetworkMask,
                             op,
                             path,
                             value,):
        obj =  {}
        obj['DestinationNw'] = DestinationNw
        obj['NetworkMask'] = NetworkMask
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'IPv6Route'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getIPv6Route(self,
                     DestinationNw,
                     NetworkMask):
        obj =  { 
                'DestinationNw' : DestinationNw,
                'NetworkMask' : NetworkMask,
                }
        reqUrl =  self.cfgUrlBase + 'IPv6Route'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getIPv6RouteById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'IPv6Route'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllIPv6Routes(self):
        return self.getObjects('IPv6Route', self.cfgUrlBase)


    def getNDPEntryState(self,
                         IpAddr):
        obj =  { 
                'IpAddr' : IpAddr,
                }
        reqUrl =  self.stateUrlBase + 'NDPEntry'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getNDPEntryStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'NDPEntry'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllNDPEntryStates(self):
        return self.getObjects('NDPEntry', self.stateUrlBase)


    def updateDWDMModuleClntIntf(self,
                                 ClntIntfId,
                                 ModuleId,
                                 NwLaneTributaryToClntIntfMap = None,
                                 HostTxEqDfe = None,
                                 HostRxSerializerTap1Gain = None,
                                 RxPRBSPattern = None,
                                 HostRxSerializerTap2Delay = None,
                                 HostRxSerializerTap2Gain = None,
                                 HostRxSerializerTap0Delay = None,
                                 HostTxEqCtle = None,
                                 TxPRBSPattern = None,
                                 HostTxEqLfCtle = None,
                                 AdminState = None,
                                 RXFECDecDisable = None,
                                 EnableTxPRBSChecker = None,
                                 EnableHostLoopback = None,
                                 HostRxSerializerTap0Gain = None,
                                 TXFECDecDisable = None,
                                 EnableRxPRBS = None,
                                 EnableIntSerdesNWLoopback = None):
        obj =  {}
        if ClntIntfId != None :
            obj['ClntIntfId'] = int(ClntIntfId)

        if ModuleId != None :
            obj['ModuleId'] = int(ModuleId)

        if NwLaneTributaryToClntIntfMap != None :
            obj['NwLaneTributaryToClntIntfMap'] = int(NwLaneTributaryToClntIntfMap)

        if HostTxEqDfe != None :
            obj['HostTxEqDfe'] = int(HostTxEqDfe)

        if HostRxSerializerTap1Gain != None :
            obj['HostRxSerializerTap1Gain'] = int(HostRxSerializerTap1Gain)

        if RxPRBSPattern != None :
            obj['RxPRBSPattern'] = RxPRBSPattern

        if HostRxSerializerTap2Delay != None :
            obj['HostRxSerializerTap2Delay'] = int(HostRxSerializerTap2Delay)

        if HostRxSerializerTap2Gain != None :
            obj['HostRxSerializerTap2Gain'] = int(HostRxSerializerTap2Gain)

        if HostRxSerializerTap0Delay != None :
            obj['HostRxSerializerTap0Delay'] = int(HostRxSerializerTap0Delay)

        if HostTxEqCtle != None :
            obj['HostTxEqCtle'] = int(HostTxEqCtle)

        if TxPRBSPattern != None :
            obj['TxPRBSPattern'] = TxPRBSPattern

        if HostTxEqLfCtle != None :
            obj['HostTxEqLfCtle'] = int(HostTxEqLfCtle)

        if AdminState != None :
            obj['AdminState'] = AdminState

        if RXFECDecDisable != None :
            obj['RXFECDecDisable'] = True if RXFECDecDisable else False

        if EnableTxPRBSChecker != None :
            obj['EnableTxPRBSChecker'] = True if EnableTxPRBSChecker else False

        if EnableHostLoopback != None :
            obj['EnableHostLoopback'] = True if EnableHostLoopback else False

        if HostRxSerializerTap0Gain != None :
            obj['HostRxSerializerTap0Gain'] = int(HostRxSerializerTap0Gain)

        if TXFECDecDisable != None :
            obj['TXFECDecDisable'] = True if TXFECDecDisable else False

        if EnableRxPRBS != None :
            obj['EnableRxPRBS'] = True if EnableRxPRBS else False

        if EnableIntSerdesNWLoopback != None :
            obj['EnableIntSerdesNWLoopback'] = True if EnableIntSerdesNWLoopback else False

        reqUrl =  self.cfgUrlBase+'DWDMModuleClntIntf'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateDWDMModuleClntIntfById(self,
                                      objectId,
                                      NwLaneTributaryToClntIntfMap = None,
                                      HostTxEqDfe = None,
                                      HostRxSerializerTap1Gain = None,
                                      RxPRBSPattern = None,
                                      HostRxSerializerTap2Delay = None,
                                      HostRxSerializerTap2Gain = None,
                                      HostRxSerializerTap0Delay = None,
                                      HostTxEqCtle = None,
                                      TxPRBSPattern = None,
                                      HostTxEqLfCtle = None,
                                      AdminState = None,
                                      RXFECDecDisable = None,
                                      EnableTxPRBSChecker = None,
                                      EnableHostLoopback = None,
                                      HostRxSerializerTap0Gain = None,
                                      TXFECDecDisable = None,
                                      EnableRxPRBS = None,
                                      EnableIntSerdesNWLoopback = None):
        obj =  {}
        if NwLaneTributaryToClntIntfMap !=  None:
            obj['NwLaneTributaryToClntIntfMap'] = NwLaneTributaryToClntIntfMap

        if HostTxEqDfe !=  None:
            obj['HostTxEqDfe'] = HostTxEqDfe

        if HostRxSerializerTap1Gain !=  None:
            obj['HostRxSerializerTap1Gain'] = HostRxSerializerTap1Gain

        if RxPRBSPattern !=  None:
            obj['RxPRBSPattern'] = RxPRBSPattern

        if HostRxSerializerTap2Delay !=  None:
            obj['HostRxSerializerTap2Delay'] = HostRxSerializerTap2Delay

        if HostRxSerializerTap2Gain !=  None:
            obj['HostRxSerializerTap2Gain'] = HostRxSerializerTap2Gain

        if HostRxSerializerTap0Delay !=  None:
            obj['HostRxSerializerTap0Delay'] = HostRxSerializerTap0Delay

        if HostTxEqCtle !=  None:
            obj['HostTxEqCtle'] = HostTxEqCtle

        if TxPRBSPattern !=  None:
            obj['TxPRBSPattern'] = TxPRBSPattern

        if HostTxEqLfCtle !=  None:
            obj['HostTxEqLfCtle'] = HostTxEqLfCtle

        if AdminState !=  None:
            obj['AdminState'] = AdminState

        if RXFECDecDisable !=  None:
            obj['RXFECDecDisable'] = RXFECDecDisable

        if EnableTxPRBSChecker !=  None:
            obj['EnableTxPRBSChecker'] = EnableTxPRBSChecker

        if EnableHostLoopback !=  None:
            obj['EnableHostLoopback'] = EnableHostLoopback

        if HostRxSerializerTap0Gain !=  None:
            obj['HostRxSerializerTap0Gain'] = HostRxSerializerTap0Gain

        if TXFECDecDisable !=  None:
            obj['TXFECDecDisable'] = TXFECDecDisable

        if EnableRxPRBS !=  None:
            obj['EnableRxPRBS'] = EnableRxPRBS

        if EnableIntSerdesNWLoopback !=  None:
            obj['EnableIntSerdesNWLoopback'] = EnableIntSerdesNWLoopback

        reqUrl =  self.cfgUrlBase+'DWDMModuleClntIntf'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateDWDMModuleClntIntf(self,
                                      ClntIntfId,
                                      ModuleId,
                                      op,
                                      path,
                                      value,):
        obj =  {}
        obj['ClntIntfId'] = ClntIntfId
        obj['ModuleId'] = ModuleId
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'DWDMModuleClntIntf'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getDWDMModuleClntIntf(self,
                              ClntIntfId,
                              ModuleId):
        obj =  { 
                'ClntIntfId' : int(ClntIntfId),
                'ModuleId' : int(ModuleId),
                }
        reqUrl =  self.cfgUrlBase + 'DWDMModuleClntIntf'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getDWDMModuleClntIntfById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'DWDMModuleClntIntf'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllDWDMModuleClntIntfs(self):
        return self.getObjects('DWDMModuleClntIntf', self.cfgUrlBase)


    def getTemperatureSensorState(self,
                                  Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.stateUrlBase + 'TemperatureSensor'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getTemperatureSensorStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'TemperatureSensor'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllTemperatureSensorStates(self):
        return self.getObjects('TemperatureSensor', self.stateUrlBase)


    def getRouteStatsPerInterfaceState(self,
                                       Intfref):
        obj =  { 
                'Intfref' : Intfref,
                }
        reqUrl =  self.stateUrlBase + 'RouteStatsPerInterface'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getRouteStatsPerInterfaceStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'RouteStatsPerInterface'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllRouteStatsPerInterfaceStates(self):
        return self.getObjects('RouteStatsPerInterface', self.stateUrlBase)


    def getNDPGlobalState(self,
                          Vrf):
        obj =  { 
                'Vrf' : Vrf,
                }
        reqUrl =  self.stateUrlBase + 'NDPGlobal'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getNDPGlobalStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'NDPGlobal'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllNDPGlobalStates(self):
        return self.getObjects('NDPGlobal', self.stateUrlBase)


    def getLacpGlobalState(self,
                           Vrf):
        obj =  { 
                'Vrf' : Vrf,
                }
        reqUrl =  self.stateUrlBase + 'LacpGlobal'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getLacpGlobalStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'LacpGlobal'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllLacpGlobalStates(self):
        return self.getObjects('LacpGlobal', self.stateUrlBase)


    def updateQsfp(self,
                   QsfpId,
                   HigherAlarmTemperature = None,
                   HigherAlarmVoltage = None,
                   HigherWarningTemperature = None,
                   HigherWarningVoltage = None,
                   LowerAlarmTemperature = None,
                   LowerAlarmVoltage = None,
                   LowerWarningTemperature = None,
                   LowerWarningVoltage = None,
                   PMClassBAdminState = None,
                   PMClassCAdminState = None,
                   PMClassAAdminState = None,
                   AdminState = None):
        obj =  {}
        if QsfpId != None :
            obj['QsfpId'] = int(QsfpId)

        if HigherAlarmTemperature != None :
            obj['HigherAlarmTemperature'] = HigherAlarmTemperature

        if HigherAlarmVoltage != None :
            obj['HigherAlarmVoltage'] = HigherAlarmVoltage

        if HigherWarningTemperature != None :
            obj['HigherWarningTemperature'] = HigherWarningTemperature

        if HigherWarningVoltage != None :
            obj['HigherWarningVoltage'] = HigherWarningVoltage

        if LowerAlarmTemperature != None :
            obj['LowerAlarmTemperature'] = LowerAlarmTemperature

        if LowerAlarmVoltage != None :
            obj['LowerAlarmVoltage'] = LowerAlarmVoltage

        if LowerWarningTemperature != None :
            obj['LowerWarningTemperature'] = LowerWarningTemperature

        if LowerWarningVoltage != None :
            obj['LowerWarningVoltage'] = LowerWarningVoltage

        if PMClassBAdminState != None :
            obj['PMClassBAdminState'] = PMClassBAdminState

        if PMClassCAdminState != None :
            obj['PMClassCAdminState'] = PMClassCAdminState

        if PMClassAAdminState != None :
            obj['PMClassAAdminState'] = PMClassAAdminState

        if AdminState != None :
            obj['AdminState'] = AdminState

        reqUrl =  self.cfgUrlBase+'Qsfp'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateQsfpById(self,
                        objectId,
                        HigherAlarmTemperature = None,
                        HigherAlarmVoltage = None,
                        HigherWarningTemperature = None,
                        HigherWarningVoltage = None,
                        LowerAlarmTemperature = None,
                        LowerAlarmVoltage = None,
                        LowerWarningTemperature = None,
                        LowerWarningVoltage = None,
                        PMClassBAdminState = None,
                        PMClassCAdminState = None,
                        PMClassAAdminState = None,
                        AdminState = None):
        obj =  {}
        if HigherAlarmTemperature !=  None:
            obj['HigherAlarmTemperature'] = HigherAlarmTemperature

        if HigherAlarmVoltage !=  None:
            obj['HigherAlarmVoltage'] = HigherAlarmVoltage

        if HigherWarningTemperature !=  None:
            obj['HigherWarningTemperature'] = HigherWarningTemperature

        if HigherWarningVoltage !=  None:
            obj['HigherWarningVoltage'] = HigherWarningVoltage

        if LowerAlarmTemperature !=  None:
            obj['LowerAlarmTemperature'] = LowerAlarmTemperature

        if LowerAlarmVoltage !=  None:
            obj['LowerAlarmVoltage'] = LowerAlarmVoltage

        if LowerWarningTemperature !=  None:
            obj['LowerWarningTemperature'] = LowerWarningTemperature

        if LowerWarningVoltage !=  None:
            obj['LowerWarningVoltage'] = LowerWarningVoltage

        if PMClassBAdminState !=  None:
            obj['PMClassBAdminState'] = PMClassBAdminState

        if PMClassCAdminState !=  None:
            obj['PMClassCAdminState'] = PMClassCAdminState

        if PMClassAAdminState !=  None:
            obj['PMClassAAdminState'] = PMClassAAdminState

        if AdminState !=  None:
            obj['AdminState'] = AdminState

        reqUrl =  self.cfgUrlBase+'Qsfp'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateQsfp(self,
                        QsfpId,
                        op,
                        path,
                        value,):
        obj =  {}
        obj['QsfpId'] = QsfpId
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'Qsfp'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getQsfp(self,
                QsfpId):
        obj =  { 
                'QsfpId' : int(QsfpId),
                }
        reqUrl =  self.cfgUrlBase + 'Qsfp'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getQsfpById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'Qsfp'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllQsfps(self):
        return self.getObjects('Qsfp', self.cfgUrlBase)


    def getVoltageSensorPMDataState(self,
                                    Class,
                                    Name):
        obj =  { 
                'Class' : Class,
                'Name' : Name,
                }
        reqUrl =  self.stateUrlBase + 'VoltageSensorPMData'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getVoltageSensorPMDataStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'VoltageSensorPMData'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllVoltageSensorPMDataStates(self):
        return self.getObjects('VoltageSensorPMData', self.stateUrlBase)


    def getIPV6AdjState(self,
                        IntfRef):
        obj =  { 
                'IntfRef' : IntfRef,
                }
        reqUrl =  self.stateUrlBase + 'IPV6Adj'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getIPV6AdjStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'IPV6Adj'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllIPV6AdjStates(self):
        return self.getObjects('IPV6Adj', self.stateUrlBase)


    """
    .. automethod :: executeNdpDeleteByIPv6Addr(self,
        :param string IpAddr : End Host IPV6 Address for which corresponding NDP entry needs to be deleted End Host IPV6 Address for which corresponding NDP entry needs to be deleted

	"""
    def executeNdpDeleteByIPv6Addr(self,
                                   IpAddr):
        obj =  { 
                'IpAddr' : IpAddr,
                }
        reqUrl =  self.actionUrlBase+'NdpDeleteByIPv6Addr'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    """
    .. automethod :: createDhcpIntfConfig(self,
        :param string IntfRef : Interface name or ifindex of L3 interface object on which Dhcp Server need to be configured Interface name or ifindex of L3 interface object on which Dhcp Server need to be configured
        :param string Subnet : Subnet Subnet
        :param string SubnetMask : Subnet Mask Subnet Mask
        :param string IPAddrRange : Range of IP Addresses DEFAULT Range of IP Addresses DEFAULT
        :param string BroadcastAddr : Broadcast Address DEFAULT Broadcast Address DEFAULT
        :param string RouterAddr : Router Address DEFAULT Router Address DEFAULT
        :param string DNSServerAddr : Comma seperated List of DNS Server Address DEFAULT Comma seperated List of DNS Server Address DEFAULT
        :param string DomainName : Domain Name Address DEFAULT Domain Name Address DEFAULT
        :param bool Enable : Enable and Disable Control DEFAULT Enable and Disable Control DEFAULT

	"""
    def createDhcpIntfConfig(self,
                             IntfRef,
                             Subnet,
                             SubnetMask,
                             IPAddrRange,
                             BroadcastAddr,
                             RouterAddr,
                             DNSServerAddr,
                             DomainName,
                             Enable):
        obj =  { 
                'IntfRef' : IntfRef,
                'Subnet' : Subnet,
                'SubnetMask' : SubnetMask,
                'IPAddrRange' : IPAddrRange,
                'BroadcastAddr' : BroadcastAddr,
                'RouterAddr' : RouterAddr,
                'DNSServerAddr' : DNSServerAddr,
                'DomainName' : DomainName,
                'Enable' : True if Enable else False,
                }
        reqUrl =  self.cfgUrlBase+'DhcpIntfConfig'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteDhcpIntfConfig(self,
                             IntfRef):
        obj =  { 
                'IntfRef' : IntfRef,
                }
        reqUrl =  self.cfgUrlBase+'DhcpIntfConfig'
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteDhcpIntfConfigById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'DhcpIntfConfig'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        else:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        return r

    def updateDhcpIntfConfig(self,
                             IntfRef,
                             Subnet = None,
                             SubnetMask = None,
                             IPAddrRange = None,
                             BroadcastAddr = None,
                             RouterAddr = None,
                             DNSServerAddr = None,
                             DomainName = None,
                             Enable = None):
        obj =  {}
        if IntfRef != None :
            obj['IntfRef'] = IntfRef

        if Subnet != None :
            obj['Subnet'] = Subnet

        if SubnetMask != None :
            obj['SubnetMask'] = SubnetMask

        if IPAddrRange != None :
            obj['IPAddrRange'] = IPAddrRange

        if BroadcastAddr != None :
            obj['BroadcastAddr'] = BroadcastAddr

        if RouterAddr != None :
            obj['RouterAddr'] = RouterAddr

        if DNSServerAddr != None :
            obj['DNSServerAddr'] = DNSServerAddr

        if DomainName != None :
            obj['DomainName'] = DomainName

        if Enable != None :
            obj['Enable'] = True if Enable else False

        reqUrl =  self.cfgUrlBase+'DhcpIntfConfig'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateDhcpIntfConfigById(self,
                                  objectId,
                                  Subnet = None,
                                  SubnetMask = None,
                                  IPAddrRange = None,
                                  BroadcastAddr = None,
                                  RouterAddr = None,
                                  DNSServerAddr = None,
                                  DomainName = None,
                                  Enable = None):
        obj =  {}
        if Subnet !=  None:
            obj['Subnet'] = Subnet

        if SubnetMask !=  None:
            obj['SubnetMask'] = SubnetMask

        if IPAddrRange !=  None:
            obj['IPAddrRange'] = IPAddrRange

        if BroadcastAddr !=  None:
            obj['BroadcastAddr'] = BroadcastAddr

        if RouterAddr !=  None:
            obj['RouterAddr'] = RouterAddr

        if DNSServerAddr !=  None:
            obj['DNSServerAddr'] = DNSServerAddr

        if DomainName !=  None:
            obj['DomainName'] = DomainName

        if Enable !=  None:
            obj['Enable'] = Enable

        reqUrl =  self.cfgUrlBase+'DhcpIntfConfig'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateDhcpIntfConfig(self,
                                  IntfRef,
                                  op,
                                  path,
                                  value,):
        obj =  {}
        obj['IntfRef'] = IntfRef
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'DhcpIntfConfig'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getDhcpIntfConfig(self,
                          IntfRef):
        obj =  { 
                'IntfRef' : IntfRef,
                }
        reqUrl =  self.cfgUrlBase + 'DhcpIntfConfig'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getDhcpIntfConfigById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'DhcpIntfConfig'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllDhcpIntfConfigs(self):
        return self.getObjects('DhcpIntfConfig', self.cfgUrlBase)


    def getQsfpChannelPMDataState(self,
                                  ChannelNum,
                                  Class,
                                  Resource,
                                  QsfpId):
        obj =  { 
                'ChannelNum' : int(ChannelNum),
                'Class' : Class,
                'Resource' : Resource,
                'QsfpId' : int(QsfpId),
                }
        reqUrl =  self.stateUrlBase + 'QsfpChannelPMData'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getQsfpChannelPMDataStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'QsfpChannelPMData'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllQsfpChannelPMDataStates(self):
        return self.getObjects('QsfpChannelPMData', self.stateUrlBase)


    def getVrrpIntfState(self,
                         VRID,
                         IfIndex):
        obj =  { 
                'VRID' : int(VRID),
                'IfIndex' : int(IfIndex),
                }
        reqUrl =  self.stateUrlBase + 'VrrpIntf'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getVrrpIntfStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'VrrpIntf'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllVrrpIntfStates(self):
        return self.getObjects('VrrpIntf', self.stateUrlBase)


    def getSystemStatusState(self,
                             Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.stateUrlBase + 'SystemStatus'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getSystemStatusStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'SystemStatus'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllSystemStatusStates(self):
        return self.getObjects('SystemStatus', self.stateUrlBase)


    """
    .. automethod :: executeArpDeleteByIPv4Addr(self,
        :param string IpAddr : End Host IP Address for which corresponding Arp entry needed to be deleted End Host IP Address for which corresponding Arp entry needed to be deleted

	"""
    def executeArpDeleteByIPv4Addr(self,
                                   IpAddr):
        obj =  { 
                'IpAddr' : IpAddr,
                }
        reqUrl =  self.actionUrlBase+'ArpDeleteByIPv4Addr'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateFanSensor(self,
                        Name,
                        HigherAlarmThreshold = None,
                        HigherWarningThreshold = None,
                        LowerWarningThreshold = None,
                        LowerAlarmThreshold = None,
                        PMClassCAdminState = None,
                        PMClassAAdminState = None,
                        AdminState = None,
                        PMClassBAdminState = None):
        obj =  {}
        if Name != None :
            obj['Name'] = Name

        if HigherAlarmThreshold != None :
            obj['HigherAlarmThreshold'] = int(HigherAlarmThreshold)

        if HigherWarningThreshold != None :
            obj['HigherWarningThreshold'] = int(HigherWarningThreshold)

        if LowerWarningThreshold != None :
            obj['LowerWarningThreshold'] = int(LowerWarningThreshold)

        if LowerAlarmThreshold != None :
            obj['LowerAlarmThreshold'] = int(LowerAlarmThreshold)

        if PMClassCAdminState != None :
            obj['PMClassCAdminState'] = PMClassCAdminState

        if PMClassAAdminState != None :
            obj['PMClassAAdminState'] = PMClassAAdminState

        if AdminState != None :
            obj['AdminState'] = AdminState

        if PMClassBAdminState != None :
            obj['PMClassBAdminState'] = PMClassBAdminState

        reqUrl =  self.cfgUrlBase+'FanSensor'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateFanSensorById(self,
                             objectId,
                             HigherAlarmThreshold = None,
                             HigherWarningThreshold = None,
                             LowerWarningThreshold = None,
                             LowerAlarmThreshold = None,
                             PMClassCAdminState = None,
                             PMClassAAdminState = None,
                             AdminState = None,
                             PMClassBAdminState = None):
        obj =  {}
        if HigherAlarmThreshold !=  None:
            obj['HigherAlarmThreshold'] = HigherAlarmThreshold

        if HigherWarningThreshold !=  None:
            obj['HigherWarningThreshold'] = HigherWarningThreshold

        if LowerWarningThreshold !=  None:
            obj['LowerWarningThreshold'] = LowerWarningThreshold

        if LowerAlarmThreshold !=  None:
            obj['LowerAlarmThreshold'] = LowerAlarmThreshold

        if PMClassCAdminState !=  None:
            obj['PMClassCAdminState'] = PMClassCAdminState

        if PMClassAAdminState !=  None:
            obj['PMClassAAdminState'] = PMClassAAdminState

        if AdminState !=  None:
            obj['AdminState'] = AdminState

        if PMClassBAdminState !=  None:
            obj['PMClassBAdminState'] = PMClassBAdminState

        reqUrl =  self.cfgUrlBase+'FanSensor'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateFanSensor(self,
                             Name,
                             op,
                             path,
                             value,):
        obj =  {}
        obj['Name'] = Name
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'FanSensor'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getFanSensor(self,
                     Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.cfgUrlBase + 'FanSensor'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getFanSensorById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'FanSensor'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllFanSensors(self):
        return self.getObjects('FanSensor', self.cfgUrlBase)


    """
    .. automethod :: createIpTableAcl(self,
        :param string Name : Ip Table ACL rule name Ip Table ACL rule name
        :param string Action : ACCEPT or DROP ACCEPT or DROP
        :param string IpAddr : ip address of subnet or host ip address of subnet or host
        :param string Protocol :  
        :param string Port :  
        :param string PhysicalPort : IfIndex where the acl rule is to be applied IfIndex where the acl rule is to be applied

	"""
    def createIpTableAcl(self,
                         Name,
                         Action,
                         IpAddr,
                         Protocol,
                         Port='all',
                         PhysicalPort='all'):
        obj =  { 
                'Name' : Name,
                'Action' : Action,
                'IpAddr' : IpAddr,
                'Protocol' : Protocol,
                'Port' : Port,
                'PhysicalPort' : PhysicalPort,
                }
        reqUrl =  self.cfgUrlBase+'IpTableAcl'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteIpTableAcl(self,
                         Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.cfgUrlBase+'IpTableAcl'
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteIpTableAclById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'IpTableAcl'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        else:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        return r

    def updateIpTableAcl(self,
                         Name,
                         Action = None,
                         IpAddr = None,
                         Protocol = None,
                         Port = None,
                         PhysicalPort = None):
        obj =  {}
        if Name != None :
            obj['Name'] = Name

        if Action != None :
            obj['Action'] = Action

        if IpAddr != None :
            obj['IpAddr'] = IpAddr

        if Protocol != None :
            obj['Protocol'] = Protocol

        if Port != None :
            obj['Port'] = Port

        if PhysicalPort != None :
            obj['PhysicalPort'] = PhysicalPort

        reqUrl =  self.cfgUrlBase+'IpTableAcl'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateIpTableAclById(self,
                              objectId,
                              Action = None,
                              IpAddr = None,
                              Protocol = None,
                              Port = None,
                              PhysicalPort = None):
        obj =  {}
        if Action !=  None:
            obj['Action'] = Action

        if IpAddr !=  None:
            obj['IpAddr'] = IpAddr

        if Protocol !=  None:
            obj['Protocol'] = Protocol

        if Port !=  None:
            obj['Port'] = Port

        if PhysicalPort !=  None:
            obj['PhysicalPort'] = PhysicalPort

        reqUrl =  self.cfgUrlBase+'IpTableAcl'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateIpTableAcl(self,
                              Name,
                              op,
                              path,
                              value,):
        obj =  {}
        obj['Name'] = Name
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'IpTableAcl'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getIpTableAcl(self,
                      Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.cfgUrlBase + 'IpTableAcl'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getIpTableAclById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'IpTableAcl'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllIpTableAcls(self):
        return self.getObjects('IpTableAcl', self.cfgUrlBase)


    def getIppLinkState(self,
                        IntfRef,
                        DrNameRef):
        obj =  { 
                'IntfRef' : IntfRef,
                'DrNameRef' : DrNameRef,
                }
        reqUrl =  self.stateUrlBase + 'IppLink'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getIppLinkStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'IppLink'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllIppLinkStates(self):
        return self.getObjects('IppLink', self.stateUrlBase)


    def getDWDMModuleNwIntfState(self,
                                 NwIntfId,
                                 ModuleId):
        obj =  { 
                'NwIntfId' : int(NwIntfId),
                'ModuleId' : int(ModuleId),
                }
        reqUrl =  self.stateUrlBase + 'DWDMModuleNwIntf'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getDWDMModuleNwIntfStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'DWDMModuleNwIntf'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllDWDMModuleNwIntfStates(self):
        return self.getObjects('DWDMModuleNwIntf', self.stateUrlBase)


    """
    .. automethod :: createOspfIfEntry(self,
        :param string IfIpAddress : The IP address of this OSPF interface. The IP address of this OSPF interface.
        :param int32 AddressLessIf : For the purpose of easing the instancing of addressed and addressless interfaces; this variable takes the value 0 on interfaces with IP addresses and the corresponding value of ifIndex for interfaces having no IP address. For the purpose of easing the instancing of addressed and addressless interfaces; this variable takes the value 0 on interfaces with IP addresses and the corresponding value of ifIndex for interfaces having no IP address.
        :param int32 IfAdminStat : Indiacates if OSPF is enabled on this interface Indiacates if OSPF is enabled on this interface
        :param string IfAreaId : A 32-bit integer uniquely identifying the area to which the interface connects.  Area ID 0.0.0.0 is used for the OSPF backbone. A 32-bit integer uniquely identifying the area to which the interface connects.  Area ID 0.0.0.0 is used for the OSPF backbone.
        :param string IfType : The OSPF interface type. By way of a default The OSPF interface type. By way of a default
        :param int32 IfRtrPriority : The priority of this interface.  Used in multi-access networks The priority of this interface.  Used in multi-access networks
        :param int32 IfTransitDelay : The estimated number of seconds it takes to transmit a link state update packet over this interface.  Note that the minimal value SHOULD be 1 second. The estimated number of seconds it takes to transmit a link state update packet over this interface.  Note that the minimal value SHOULD be 1 second.
        :param int32 IfRetransInterval : The number of seconds between link state advertisement retransmissions The number of seconds between link state advertisement retransmissions
        :param int32 IfPollInterval : The larger time interval The larger time interval
        :param string IfAuthKey : *** This element is added for future use. *** The cleartext password used as an OSPF authentication key when simplePassword security is enabled.  This object does not access any OSPF cryptogaphic (e.g. *** This element is added for future use. *** The cleartext password used as an OSPF authentication key when simplePassword security is enabled.  This object does not access any OSPF cryptogaphic (e.g.
        :param int32 IfAuthType : The authentication type specified for an interface.  Note that this object can be used to engage in significant attacks against an OSPF router. The authentication type specified for an interface.  Note that this object can be used to engage in significant attacks against an OSPF router.
        :param int32 IfHelloInterval : The length of time The length of time
        :param int32 IfRtrDeadInterval : The number of seconds that a router's Hello packets have not been seen before its neighbors declare the router down. This should be some multiple of the Hello interval.  This value must be the same for all routers attached to a common network. The number of seconds that a router's Hello packets have not been seen before its neighbors declare the router down. This should be some multiple of the Hello interval.  This value must be the same for all routers attached to a common network.

	"""
    def createOspfIfEntry(self,
                          IfIpAddress,
                          AddressLessIf,
                          IfAdminStat,
                          IfAreaId,
                          IfType,
                          IfRtrPriority,
                          IfTransitDelay,
                          IfRetransInterval,
                          IfPollInterval,
                          IfAuthKey,
                          IfAuthType,
                          IfHelloInterval=10,
                          IfRtrDeadInterval=40):
        obj =  { 
                'IfIpAddress' : IfIpAddress,
                'AddressLessIf' : int(AddressLessIf),
                'IfAdminStat' : int(IfAdminStat),
                'IfAreaId' : IfAreaId,
                'IfType' : IfType,
                'IfRtrPriority' : int(IfRtrPriority),
                'IfTransitDelay' : int(IfTransitDelay),
                'IfRetransInterval' : int(IfRetransInterval),
                'IfPollInterval' : int(IfPollInterval),
                'IfAuthKey' : IfAuthKey,
                'IfAuthType' : int(IfAuthType),
                'IfHelloInterval' : int(IfHelloInterval),
                'IfRtrDeadInterval' : int(IfRtrDeadInterval),
                }
        reqUrl =  self.cfgUrlBase+'OspfIfEntry'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteOspfIfEntry(self,
                          IfIpAddress,
                          AddressLessIf):
        obj =  { 
                'IfIpAddress' : IfIpAddress,
                'AddressLessIf' : AddressLessIf,
                }
        reqUrl =  self.cfgUrlBase+'OspfIfEntry'
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteOspfIfEntryById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'OspfIfEntry'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        else:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        return r

    def updateOspfIfEntry(self,
                          IfIpAddress,
                          AddressLessIf,
                          IfAdminStat = None,
                          IfAreaId = None,
                          IfType = None,
                          IfRtrPriority = None,
                          IfTransitDelay = None,
                          IfRetransInterval = None,
                          IfPollInterval = None,
                          IfAuthKey = None,
                          IfAuthType = None,
                          IfHelloInterval = None,
                          IfRtrDeadInterval = None):
        obj =  {}
        if IfIpAddress != None :
            obj['IfIpAddress'] = IfIpAddress

        if AddressLessIf != None :
            obj['AddressLessIf'] = int(AddressLessIf)

        if IfAdminStat != None :
            obj['IfAdminStat'] = int(IfAdminStat)

        if IfAreaId != None :
            obj['IfAreaId'] = IfAreaId

        if IfType != None :
            obj['IfType'] = IfType

        if IfRtrPriority != None :
            obj['IfRtrPriority'] = int(IfRtrPriority)

        if IfTransitDelay != None :
            obj['IfTransitDelay'] = int(IfTransitDelay)

        if IfRetransInterval != None :
            obj['IfRetransInterval'] = int(IfRetransInterval)

        if IfPollInterval != None :
            obj['IfPollInterval'] = int(IfPollInterval)

        if IfAuthKey != None :
            obj['IfAuthKey'] = IfAuthKey

        if IfAuthType != None :
            obj['IfAuthType'] = int(IfAuthType)

        if IfHelloInterval != None :
            obj['IfHelloInterval'] = int(IfHelloInterval)

        if IfRtrDeadInterval != None :
            obj['IfRtrDeadInterval'] = int(IfRtrDeadInterval)

        reqUrl =  self.cfgUrlBase+'OspfIfEntry'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateOspfIfEntryById(self,
                               objectId,
                               IfAdminStat = None,
                               IfAreaId = None,
                               IfType = None,
                               IfRtrPriority = None,
                               IfTransitDelay = None,
                               IfRetransInterval = None,
                               IfPollInterval = None,
                               IfAuthKey = None,
                               IfAuthType = None,
                               IfHelloInterval = None,
                               IfRtrDeadInterval = None):
        obj =  {}
        if IfAdminStat !=  None:
            obj['IfAdminStat'] = IfAdminStat

        if IfAreaId !=  None:
            obj['IfAreaId'] = IfAreaId

        if IfType !=  None:
            obj['IfType'] = IfType

        if IfRtrPriority !=  None:
            obj['IfRtrPriority'] = IfRtrPriority

        if IfTransitDelay !=  None:
            obj['IfTransitDelay'] = IfTransitDelay

        if IfRetransInterval !=  None:
            obj['IfRetransInterval'] = IfRetransInterval

        if IfPollInterval !=  None:
            obj['IfPollInterval'] = IfPollInterval

        if IfAuthKey !=  None:
            obj['IfAuthKey'] = IfAuthKey

        if IfAuthType !=  None:
            obj['IfAuthType'] = IfAuthType

        if IfHelloInterval !=  None:
            obj['IfHelloInterval'] = IfHelloInterval

        if IfRtrDeadInterval !=  None:
            obj['IfRtrDeadInterval'] = IfRtrDeadInterval

        reqUrl =  self.cfgUrlBase+'OspfIfEntry'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateOspfIfEntry(self,
                               IfIpAddress,
                               AddressLessIf,
                               op,
                               path,
                               value,):
        obj =  {}
        obj['IfIpAddress'] = IfIpAddress
        obj['AddressLessIf'] = AddressLessIf
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'OspfIfEntry'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getOspfIfEntry(self,
                       IfIpAddress,
                       AddressLessIf):
        obj =  { 
                'IfIpAddress' : IfIpAddress,
                'AddressLessIf' : int(AddressLessIf),
                }
        reqUrl =  self.cfgUrlBase + 'OspfIfEntry'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getOspfIfEntryById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'OspfIfEntry'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllOspfIfEntrys(self):
        return self.getObjects('OspfIfEntry', self.cfgUrlBase)


    def getBufferPortStatState(self,
                               IntfRef):
        obj =  { 
                'IntfRef' : IntfRef,
                }
        reqUrl =  self.stateUrlBase + 'BufferPortStat'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getBufferPortStatStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'BufferPortStat'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllBufferPortStatStates(self):
        return self.getObjects('BufferPortStat', self.stateUrlBase)


    def updateBGPGlobal(self,
                        Vrf,
                        ASNum = None,
                        UseMultiplePaths = None,
                        EBGPMaxPaths = None,
                        EBGPAllowMultipleAS = None,
                        RouterId = None,
                        IBGPMaxPaths = None,
                        Redistribution = None):
        obj =  {}
        if Vrf != None :
            obj['Vrf'] = Vrf

        if ASNum != None :
            obj['ASNum'] = ASNum

        if UseMultiplePaths != None :
            obj['UseMultiplePaths'] = True if UseMultiplePaths else False

        if EBGPMaxPaths != None :
            obj['EBGPMaxPaths'] = int(EBGPMaxPaths)

        if EBGPAllowMultipleAS != None :
            obj['EBGPAllowMultipleAS'] = True if EBGPAllowMultipleAS else False

        if RouterId != None :
            obj['RouterId'] = RouterId

        if IBGPMaxPaths != None :
            obj['IBGPMaxPaths'] = int(IBGPMaxPaths)

        if Redistribution != None :
            obj['Redistribution'] = Redistribution

        reqUrl =  self.cfgUrlBase+'BGPGlobal'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateBGPGlobalById(self,
                             objectId,
                             ASNum = None,
                             UseMultiplePaths = None,
                             EBGPMaxPaths = None,
                             EBGPAllowMultipleAS = None,
                             RouterId = None,
                             IBGPMaxPaths = None,
                             Redistribution = None):
        obj =  {}
        if ASNum !=  None:
            obj['ASNum'] = ASNum

        if UseMultiplePaths !=  None:
            obj['UseMultiplePaths'] = UseMultiplePaths

        if EBGPMaxPaths !=  None:
            obj['EBGPMaxPaths'] = EBGPMaxPaths

        if EBGPAllowMultipleAS !=  None:
            obj['EBGPAllowMultipleAS'] = EBGPAllowMultipleAS

        if RouterId !=  None:
            obj['RouterId'] = RouterId

        if IBGPMaxPaths !=  None:
            obj['IBGPMaxPaths'] = IBGPMaxPaths

        if Redistribution !=  None:
            obj['Redistribution'] = Redistribution

        reqUrl =  self.cfgUrlBase+'BGPGlobal'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateBGPGlobal(self,
                             Vrf,
                             op,
                             path,
                             value,):
        obj =  {}
        obj['Vrf'] = Vrf
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'BGPGlobal'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getBGPGlobal(self,
                     Vrf):
        obj =  { 
                'Vrf' : Vrf,
                }
        reqUrl =  self.cfgUrlBase + 'BGPGlobal'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getBGPGlobalById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'BGPGlobal'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllBGPGlobals(self):
        return self.getObjects('BGPGlobal', self.cfgUrlBase)


    def getTemperatureSensorPMDataState(self,
                                        Class,
                                        Name):
        obj =  { 
                'Class' : Class,
                'Name' : Name,
                }
        reqUrl =  self.stateUrlBase + 'TemperatureSensorPMData'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getTemperatureSensorPMDataStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'TemperatureSensorPMData'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllTemperatureSensorPMDataStates(self):
        return self.getObjects('TemperatureSensorPMData', self.stateUrlBase)


    def getOspfAreaEntryState(self,
                              AreaId):
        obj =  { 
                'AreaId' : AreaId,
                }
        reqUrl =  self.stateUrlBase + 'OspfAreaEntry'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getOspfAreaEntryStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'OspfAreaEntry'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllOspfAreaEntryStates(self):
        return self.getObjects('OspfAreaEntry', self.stateUrlBase)


    def getLLDPGlobalState(self,
                           Vrf):
        obj =  { 
                'Vrf' : Vrf,
                }
        reqUrl =  self.stateUrlBase + 'LLDPGlobal'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getLLDPGlobalStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'LLDPGlobal'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllLLDPGlobalStates(self):
        return self.getObjects('LLDPGlobal', self.stateUrlBase)


    def getEthernetPMState(self,
                           IntfRef,
                           Resource):
        obj =  { 
                'IntfRef' : IntfRef,
                'Resource' : Resource,
                }
        reqUrl =  self.stateUrlBase + 'EthernetPM'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getEthernetPMStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'EthernetPM'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllEthernetPMStates(self):
        return self.getObjects('EthernetPM', self.stateUrlBase)


    def updateNDPGlobal(self,
                        Vrf,
                        RetransmitInterval = None,
                        RouterAdvertisementInterval = None,
                        ReachableTime = None):
        obj =  {}
        if Vrf != None :
            obj['Vrf'] = Vrf

        if RetransmitInterval != None :
            obj['RetransmitInterval'] = int(RetransmitInterval)

        if RouterAdvertisementInterval != None :
            obj['RouterAdvertisementInterval'] = int(RouterAdvertisementInterval)

        if ReachableTime != None :
            obj['ReachableTime'] = int(ReachableTime)

        reqUrl =  self.cfgUrlBase+'NDPGlobal'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateNDPGlobalById(self,
                             objectId,
                             RetransmitInterval = None,
                             RouterAdvertisementInterval = None,
                             ReachableTime = None):
        obj =  {}
        if RetransmitInterval !=  None:
            obj['RetransmitInterval'] = RetransmitInterval

        if RouterAdvertisementInterval !=  None:
            obj['RouterAdvertisementInterval'] = RouterAdvertisementInterval

        if ReachableTime !=  None:
            obj['ReachableTime'] = ReachableTime

        reqUrl =  self.cfgUrlBase+'NDPGlobal'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateNDPGlobal(self,
                             Vrf,
                             op,
                             path,
                             value,):
        obj =  {}
        obj['Vrf'] = Vrf
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'NDPGlobal'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getNDPGlobal(self,
                     Vrf):
        obj =  { 
                'Vrf' : Vrf,
                }
        reqUrl =  self.cfgUrlBase + 'NDPGlobal'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getNDPGlobalById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'NDPGlobal'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllNDPGlobals(self):
        return self.getObjects('NDPGlobal', self.cfgUrlBase)


    def getPsuState(self,
                    PsuId):
        obj =  { 
                'PsuId' : int(PsuId),
                }
        reqUrl =  self.stateUrlBase + 'Psu'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getPsuStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'Psu'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllPsuStates(self):
        return self.getObjects('Psu', self.stateUrlBase)


    """
    .. automethod :: createBfdSession(self,
        :param string IpAddr : BFD neighbor IP address BFD neighbor IP address
        :param string Interface : Name of the interface this session has to be established on Name of the interface this session has to be established on
        :param string Owner : Module requesting BFD session configuration Module requesting BFD session configuration
        :param bool PerLink : Run BFD sessions on individual link of a LAG if the neighbor is reachable through LAG Run BFD sessions on individual link of a LAG if the neighbor is reachable through LAG
        :param string ParamName : Name of the session parameters object to be applied on this session Name of the session parameters object to be applied on this session

	"""
    def createBfdSession(self,
                         IpAddr,
                         Interface='None',
                         Owner='user',
                         PerLink=False,
                         ParamName='default'):
        obj =  { 
                'IpAddr' : IpAddr,
                'Interface' : Interface,
                'Owner' : Owner,
                'PerLink' : True if PerLink else False,
                'ParamName' : ParamName,
                }
        reqUrl =  self.cfgUrlBase+'BfdSession'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteBfdSession(self,
                         IpAddr):
        obj =  { 
                'IpAddr' : IpAddr,
                }
        reqUrl =  self.cfgUrlBase+'BfdSession'
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteBfdSessionById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'BfdSession'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        else:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        return r

    def updateBfdSession(self,
                         IpAddr,
                         Interface = None,
                         Owner = None,
                         PerLink = None,
                         ParamName = None):
        obj =  {}
        if IpAddr != None :
            obj['IpAddr'] = IpAddr

        if Interface != None :
            obj['Interface'] = Interface

        if Owner != None :
            obj['Owner'] = Owner

        if PerLink != None :
            obj['PerLink'] = True if PerLink else False

        if ParamName != None :
            obj['ParamName'] = ParamName

        reqUrl =  self.cfgUrlBase+'BfdSession'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateBfdSessionById(self,
                              objectId,
                              Interface = None,
                              Owner = None,
                              PerLink = None,
                              ParamName = None):
        obj =  {}
        if Interface !=  None:
            obj['Interface'] = Interface

        if Owner !=  None:
            obj['Owner'] = Owner

        if PerLink !=  None:
            obj['PerLink'] = PerLink

        if ParamName !=  None:
            obj['ParamName'] = ParamName

        reqUrl =  self.cfgUrlBase+'BfdSession'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateBfdSession(self,
                              IpAddr,
                              op,
                              path,
                              value,):
        obj =  {}
        obj['IpAddr'] = IpAddr
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'BfdSession'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getBfdSession(self,
                      IpAddr):
        obj =  { 
                'IpAddr' : IpAddr,
                }
        reqUrl =  self.cfgUrlBase + 'BfdSession'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getBfdSessionById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'BfdSession'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllBfdSessions(self):
        return self.getObjects('BfdSession', self.cfgUrlBase)


    def getPolicyConditionState(self,
                                Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.stateUrlBase + 'PolicyCondition'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getPolicyConditionStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'PolicyCondition'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllPolicyConditionStates(self):
        return self.getObjects('PolicyCondition', self.stateUrlBase)


    """
    .. automethod :: createVrrpIntf(self,
        :param int32 VRID : Virtual Router's Unique Identifier Virtual Router's Unique Identifier
        :param int32 IfIndex : Interface index for which VRRP Config needs to be done Interface index for which VRRP Config needs to be done
        :param string VirtualIPv4Addr : Virtual Router Identifier Virtual Router Identifier
        :param bool PreemptMode : Controls whether a (starting or restarting) higher-priority Backup router preempts a lower-priority Master router Controls whether a (starting or restarting) higher-priority Backup router preempts a lower-priority Master router
        :param int32 Priority : Sending VRRP router's priority for the virtual router Sending VRRP router's priority for the virtual router
        :param int32 AdvertisementInterval : Time interval between ADVERTISEMENTS Time interval between ADVERTISEMENTS
        :param bool AcceptMode : Controls whether a virtual router in Master state will accept packets addressed to the address owner's IPvX address as its own if it is not the IPvX address owner. Controls whether a virtual router in Master state will accept packets addressed to the address owner's IPvX address as its own if it is not the IPvX address owner.

	"""
    def createVrrpIntf(self,
                       VRID,
                       IfIndex,
                       VirtualIPv4Addr,
                       PreemptMode=True,
                       Priority=100,
                       AdvertisementInterval=1,
                       AcceptMode=False):
        obj =  { 
                'VRID' : int(VRID),
                'IfIndex' : int(IfIndex),
                'VirtualIPv4Addr' : VirtualIPv4Addr,
                'PreemptMode' : True if PreemptMode else False,
                'Priority' : int(Priority),
                'AdvertisementInterval' : int(AdvertisementInterval),
                'AcceptMode' : True if AcceptMode else False,
                }
        reqUrl =  self.cfgUrlBase+'VrrpIntf'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteVrrpIntf(self,
                       VRID,
                       IfIndex):
        obj =  { 
                'VRID' : VRID,
                'IfIndex' : IfIndex,
                }
        reqUrl =  self.cfgUrlBase+'VrrpIntf'
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteVrrpIntfById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'VrrpIntf'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        else:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        return r

    def updateVrrpIntf(self,
                       VRID,
                       IfIndex,
                       VirtualIPv4Addr = None,
                       PreemptMode = None,
                       Priority = None,
                       AdvertisementInterval = None,
                       AcceptMode = None):
        obj =  {}
        if VRID != None :
            obj['VRID'] = int(VRID)

        if IfIndex != None :
            obj['IfIndex'] = int(IfIndex)

        if VirtualIPv4Addr != None :
            obj['VirtualIPv4Addr'] = VirtualIPv4Addr

        if PreemptMode != None :
            obj['PreemptMode'] = True if PreemptMode else False

        if Priority != None :
            obj['Priority'] = int(Priority)

        if AdvertisementInterval != None :
            obj['AdvertisementInterval'] = int(AdvertisementInterval)

        if AcceptMode != None :
            obj['AcceptMode'] = True if AcceptMode else False

        reqUrl =  self.cfgUrlBase+'VrrpIntf'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateVrrpIntfById(self,
                            objectId,
                            VirtualIPv4Addr = None,
                            PreemptMode = None,
                            Priority = None,
                            AdvertisementInterval = None,
                            AcceptMode = None):
        obj =  {}
        if VirtualIPv4Addr !=  None:
            obj['VirtualIPv4Addr'] = VirtualIPv4Addr

        if PreemptMode !=  None:
            obj['PreemptMode'] = PreemptMode

        if Priority !=  None:
            obj['Priority'] = Priority

        if AdvertisementInterval !=  None:
            obj['AdvertisementInterval'] = AdvertisementInterval

        if AcceptMode !=  None:
            obj['AcceptMode'] = AcceptMode

        reqUrl =  self.cfgUrlBase+'VrrpIntf'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateVrrpIntf(self,
                            VRID,
                            IfIndex,
                            op,
                            path,
                            value,):
        obj =  {}
        obj['VRID'] = VRID
        obj['IfIndex'] = IfIndex
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'VrrpIntf'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getVrrpIntf(self,
                    VRID,
                    IfIndex):
        obj =  { 
                'VRID' : int(VRID),
                'IfIndex' : int(IfIndex),
                }
        reqUrl =  self.cfgUrlBase + 'VrrpIntf'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getVrrpIntfById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'VrrpIntf'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllVrrpIntfs(self):
        return self.getObjects('VrrpIntf', self.cfgUrlBase)


    def getXponderGlobalState(self,
                              XponderId):
        obj =  { 
                'XponderId' : int(XponderId),
                }
        reqUrl =  self.stateUrlBase + 'XponderGlobal'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getXponderGlobalStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'XponderGlobal'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllXponderGlobalStates(self):
        return self.getObjects('XponderGlobal', self.stateUrlBase)


    def updateLLDPGlobal(self,
                         Vrf,
                         TxRxMode = None,
                         SnoopAndDrop = None,
                         Enable = None,
                         TranmitInterval = None):
        obj =  {}
        if Vrf != None :
            obj['Vrf'] = Vrf

        if TxRxMode != None :
            obj['TxRxMode'] = TxRxMode

        if SnoopAndDrop != None :
            obj['SnoopAndDrop'] = True if SnoopAndDrop else False

        if Enable != None :
            obj['Enable'] = True if Enable else False

        if TranmitInterval != None :
            obj['TranmitInterval'] = int(TranmitInterval)

        reqUrl =  self.cfgUrlBase+'LLDPGlobal'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateLLDPGlobalById(self,
                              objectId,
                              TxRxMode = None,
                              SnoopAndDrop = None,
                              Enable = None,
                              TranmitInterval = None):
        obj =  {}
        if TxRxMode !=  None:
            obj['TxRxMode'] = TxRxMode

        if SnoopAndDrop !=  None:
            obj['SnoopAndDrop'] = SnoopAndDrop

        if Enable !=  None:
            obj['Enable'] = Enable

        if TranmitInterval !=  None:
            obj['TranmitInterval'] = TranmitInterval

        reqUrl =  self.cfgUrlBase+'LLDPGlobal'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateLLDPGlobal(self,
                              Vrf,
                              op,
                              path,
                              value,):
        obj =  {}
        obj['Vrf'] = Vrf
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'LLDPGlobal'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getLLDPGlobal(self,
                      Vrf):
        obj =  { 
                'Vrf' : Vrf,
                }
        reqUrl =  self.cfgUrlBase + 'LLDPGlobal'
        print "LLDP"
        if self.authenticate == True:
                print "LLDP1"
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                print "LLDP2"
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        print r
        return r

    def getLLDPGlobalById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'LLDPGlobal'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllLLDPGlobals(self):
        return self.getObjects('LLDPGlobal', self.cfgUrlBase)


    def getIPv6RouteHwState(self,
                            DestinationNw):
        obj =  { 
                'DestinationNw' : DestinationNw,
                }
        reqUrl =  self.stateUrlBase + 'IPv6RouteHw'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getIPv6RouteHwStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'IPv6RouteHw'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllIPv6RouteHwStates(self):
        return self.getObjects('IPv6RouteHw', self.stateUrlBase)


    """
    .. automethod :: createSubIPv4Intf(self,
        :param string IntfRef : Intf name of system generated id (ifindex) of the ipv4Intf where sub interface is to be configured Intf name of system generated id (ifindex) of the ipv4Intf where sub interface is to be configured
        :param string IpAddr : Ip Address for the interface Ip Address for the interface
        :param string Type : Type of interface Type of interface
        :param string MacAddr : Mac address to be used for the sub interface. If none specified IPv4Intf mac address will be used Mac address to be used for the sub interface. If none specified IPv4Intf mac address will be used
        :param bool Enable : Enable or disable this interface Enable or disable this interface

	"""
    def createSubIPv4Intf(self,
                          IntfRef,
                          IpAddr,
                          Type,
                          MacAddr,
                          Enable=False):
        obj =  { 
                'IntfRef' : IntfRef,
                'IpAddr' : IpAddr,
                'Type' : Type,
                'MacAddr' : MacAddr,
                'Enable' : True if Enable else False,
                }
        reqUrl =  self.cfgUrlBase+'SubIPv4Intf'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteSubIPv4Intf(self,
                          IntfRef,
                          IpAddr):
        obj =  { 
                'IntfRef' : IntfRef,
                'IpAddr' : IpAddr,
                }
        reqUrl =  self.cfgUrlBase+'SubIPv4Intf'
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteSubIPv4IntfById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'SubIPv4Intf'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        else:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        return r

    def updateSubIPv4Intf(self,
                          IntfRef,
                          IpAddr,
                          Type = None,
                          MacAddr = None,
                          Enable = None):
        obj =  {}
        if IntfRef != None :
            obj['IntfRef'] = IntfRef

        if IpAddr != None :
            obj['IpAddr'] = IpAddr

        if Type != None :
            obj['Type'] = Type

        if MacAddr != None :
            obj['MacAddr'] = MacAddr

        if Enable != None :
            obj['Enable'] = True if Enable else False

        reqUrl =  self.cfgUrlBase+'SubIPv4Intf'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateSubIPv4IntfById(self,
                               objectId,
                               Type = None,
                               MacAddr = None,
                               Enable = None):
        obj =  {}
        if Type !=  None:
            obj['Type'] = Type

        if MacAddr !=  None:
            obj['MacAddr'] = MacAddr

        if Enable !=  None:
            obj['Enable'] = Enable

        reqUrl =  self.cfgUrlBase+'SubIPv4Intf'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateSubIPv4Intf(self,
                               IntfRef,
                               IpAddr,
                               op,
                               path,
                               value,):
        obj =  {}
        obj['IntfRef'] = IntfRef
        obj['IpAddr'] = IpAddr
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'SubIPv4Intf'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getSubIPv4Intf(self,
                       IntfRef,
                       IpAddr):
        obj =  { 
                'IntfRef' : IntfRef,
                'IpAddr' : IpAddr,
                }
        reqUrl =  self.cfgUrlBase + 'SubIPv4Intf'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getSubIPv4IntfById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'SubIPv4Intf'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllSubIPv4Intfs(self):
        return self.getObjects('SubIPv4Intf', self.cfgUrlBase)


    def getSfpState(self,
                    SfpId):
        obj =  { 
                'SfpId' : int(SfpId),
                }
        reqUrl =  self.stateUrlBase + 'Sfp'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getSfpStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'Sfp'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllSfpStates(self):
        return self.getObjects('Sfp', self.stateUrlBase)


    def getPolicyDefinitionState(self,
                                 Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.stateUrlBase + 'PolicyDefinition'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getPolicyDefinitionStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'PolicyDefinition'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllPolicyDefinitionStates(self):
        return self.getObjects('PolicyDefinition', self.stateUrlBase)


    def getVlanState(self,
                     VlanId):
        obj =  { 
                'VlanId' : int(VlanId),
                }
        reqUrl =  self.stateUrlBase + 'Vlan'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getVlanStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'Vlan'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllVlanStates(self):
        return self.getObjects('Vlan', self.stateUrlBase)


    def getIsisGlobalState(self,
                           Vrf):
        obj =  { 
                'Vrf' : Vrf,
                }
        reqUrl =  self.stateUrlBase + 'IsisGlobal'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getIsisGlobalStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'IsisGlobal'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllIsisGlobalStates(self):
        return self.getObjects('IsisGlobal', self.stateUrlBase)


    def getLogicalIntfState(self,
                            Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.stateUrlBase + 'LogicalIntf'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getLogicalIntfStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'LogicalIntf'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllLogicalIntfStates(self):
        return self.getObjects('LogicalIntf', self.stateUrlBase)


    """
    .. automethod :: createBGPv6Aggregate(self,
        :param string IpPrefix : IPv6 Prefix in CIDR format to match IPv6 Prefix in CIDR format to match
        :param bool SendSummaryOnly : Send summary route only when aggregating routes Send summary route only when aggregating routes
        :param bool GenerateASSet : Generate AS set when aggregating routes Generate AS set when aggregating routes

	"""
    def createBGPv6Aggregate(self,
                             IpPrefix,
                             SendSummaryOnly=False,
                             GenerateASSet=False):
        obj =  { 
                'IpPrefix' : IpPrefix,
                'SendSummaryOnly' : True if SendSummaryOnly else False,
                'GenerateASSet' : True if GenerateASSet else False,
                }
        reqUrl =  self.cfgUrlBase+'BGPv6Aggregate'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteBGPv6Aggregate(self,
                             IpPrefix):
        obj =  { 
                'IpPrefix' : IpPrefix,
                }
        reqUrl =  self.cfgUrlBase+'BGPv6Aggregate'
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteBGPv6AggregateById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'BGPv6Aggregate'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        else:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        return r

    def updateBGPv6Aggregate(self,
                             IpPrefix,
                             SendSummaryOnly = None,
                             GenerateASSet = None):
        obj =  {}
        if IpPrefix != None :
            obj['IpPrefix'] = IpPrefix

        if SendSummaryOnly != None :
            obj['SendSummaryOnly'] = True if SendSummaryOnly else False

        if GenerateASSet != None :
            obj['GenerateASSet'] = True if GenerateASSet else False

        reqUrl =  self.cfgUrlBase+'BGPv6Aggregate'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateBGPv6AggregateById(self,
                                  objectId,
                                  SendSummaryOnly = None,
                                  GenerateASSet = None):
        obj =  {}
        if SendSummaryOnly !=  None:
            obj['SendSummaryOnly'] = SendSummaryOnly

        if GenerateASSet !=  None:
            obj['GenerateASSet'] = GenerateASSet

        reqUrl =  self.cfgUrlBase+'BGPv6Aggregate'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateBGPv6Aggregate(self,
                                  IpPrefix,
                                  op,
                                  path,
                                  value,):
        obj =  {}
        obj['IpPrefix'] = IpPrefix
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'BGPv6Aggregate'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getBGPv6Aggregate(self,
                          IpPrefix):
        obj =  { 
                'IpPrefix' : IpPrefix,
                }
        reqUrl =  self.cfgUrlBase + 'BGPv6Aggregate'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getBGPv6AggregateById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'BGPv6Aggregate'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllBGPv6Aggregates(self):
        return self.getObjects('BGPv6Aggregate', self.cfgUrlBase)


    """
    .. automethod :: executeDWDMModuleFWDownload(self,
        :param uint8 ModuleId : DWDM Module identifier DWDM Module identifier
        :param string FileName : Firmware file name or absolute file location Firmware file name or absolute file location

	"""
    def executeDWDMModuleFWDownload(self,
                                    ModuleId,
                                    FileName):
        obj =  { 
                'ModuleId' : int(ModuleId),
                'FileName' : FileName,
                }
        reqUrl =  self.actionUrlBase+'DWDMModuleFWDownload'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getThermalState(self,
                        ThermalId):
        obj =  { 
                'ThermalId' : int(ThermalId),
                }
        reqUrl =  self.stateUrlBase + 'Thermal'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getThermalStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'Thermal'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllThermalStates(self):
        return self.getObjects('Thermal', self.stateUrlBase)


    """
    .. automethod :: createPolicyPrefixSet(self,
        :param string Name : Policy Prefix set name. Policy Prefix set name.
        :param PolicyPrefix PrefixList : List of policy prefixes part of this prefix set. List of policy prefixes part of this prefix set.

	"""
    def createPolicyPrefixSet(self,
                              Name,
                              PrefixList):
        obj =  { 
                'Name' : Name,
                'PrefixList' : PrefixList,
                }
        reqUrl =  self.cfgUrlBase+'PolicyPrefixSet'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deletePolicyPrefixSet(self,
                              Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.cfgUrlBase+'PolicyPrefixSet'
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deletePolicyPrefixSetById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'PolicyPrefixSet'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        else:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        return r

    def updatePolicyPrefixSet(self,
                              Name,
                              PrefixList = None):
        obj =  {}
        if Name != None :
            obj['Name'] = Name

        if PrefixList != None :
            obj['PrefixList'] = PrefixList

        reqUrl =  self.cfgUrlBase+'PolicyPrefixSet'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updatePolicyPrefixSetById(self,
                                   objectId,
                                   PrefixList = None):
        obj =  {}
        if PrefixList !=  None:
            obj['PrefixList'] = PrefixList

        reqUrl =  self.cfgUrlBase+'PolicyPrefixSet'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdatePolicyPrefixSet(self,
                                   Name,
                                   op,
                                   path,
                                   value,):
        obj =  {}
        obj['Name'] = Name
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'PolicyPrefixSet'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getPolicyPrefixSet(self,
                           Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.cfgUrlBase + 'PolicyPrefixSet'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getPolicyPrefixSetById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'PolicyPrefixSet'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllPolicyPrefixSets(self):
        return self.getObjects('PolicyPrefixSet', self.cfgUrlBase)


    def getLinkScopeIpState(self,
                            LinkScopeIp):
        obj =  { 
                'LinkScopeIp' : LinkScopeIp,
                }
        reqUrl =  self.stateUrlBase + 'LinkScopeIp'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getLinkScopeIpStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'LinkScopeIp'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllLinkScopeIpStates(self):
        return self.getObjects('LinkScopeIp', self.stateUrlBase)


    """
    .. automethod :: executeArpDeleteByIfName(self,
        :param string IfName : All the Arp learned for end host on given L3 interface will be deleted All the Arp learned for end host on given L3 interface will be deleted

	"""
    def executeArpDeleteByIfName(self,
                                 IfName):
        obj =  { 
                'IfName' : IfName,
                }
        reqUrl =  self.actionUrlBase+'ArpDeleteByIfName'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def updateStpBridgeInstance(self,
                                Vlan,
                                HelloTime = None,
                                ForwardDelay = None,
                                MaxAge = None,
                                TxHoldCount = None,
                                Priority = None,
                                ForceVersion = None,
                                Address = None):
        obj =  {}
        if Vlan != None :
            obj['Vlan'] = int(Vlan)

        if HelloTime != None :
            obj['HelloTime'] = int(HelloTime)

        if ForwardDelay != None :
            obj['ForwardDelay'] = int(ForwardDelay)

        if MaxAge != None :
            obj['MaxAge'] = int(MaxAge)

        if TxHoldCount != None :
            obj['TxHoldCount'] = int(TxHoldCount)

        if Priority != None :
            obj['Priority'] = int(Priority)

        if ForceVersion != None :
            obj['ForceVersion'] = int(ForceVersion)

        if Address != None :
            obj['Address'] = Address

        reqUrl =  self.cfgUrlBase+'StpBridgeInstance'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateStpBridgeInstanceById(self,
                                     objectId,
                                     HelloTime = None,
                                     ForwardDelay = None,
                                     MaxAge = None,
                                     TxHoldCount = None,
                                     Priority = None,
                                     ForceVersion = None,
                                     Address = None):
        obj =  {}
        if HelloTime !=  None:
            obj['HelloTime'] = HelloTime

        if ForwardDelay !=  None:
            obj['ForwardDelay'] = ForwardDelay

        if MaxAge !=  None:
            obj['MaxAge'] = MaxAge

        if TxHoldCount !=  None:
            obj['TxHoldCount'] = TxHoldCount

        if Priority !=  None:
            obj['Priority'] = Priority

        if ForceVersion !=  None:
            obj['ForceVersion'] = ForceVersion

        if Address !=  None:
            obj['Address'] = Address

        reqUrl =  self.cfgUrlBase+'StpBridgeInstance'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateStpBridgeInstance(self,
                                     Vlan,
                                     op,
                                     path,
                                     value,):
        obj =  {}
        obj['Vlan'] = Vlan
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'StpBridgeInstance'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getStpBridgeInstance(self,
                             Vlan):
        obj =  { 
                'Vlan' : int(Vlan),
                }
        reqUrl =  self.cfgUrlBase + 'StpBridgeInstance'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getStpBridgeInstanceById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'StpBridgeInstance'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllStpBridgeInstances(self):
        return self.getObjects('StpBridgeInstance', self.cfgUrlBase)


    """
    .. automethod :: executeNdpRefreshByIfName(self,
        :param string IfName : All the NDP learned on given L3 interface will be re-learned All the NDP learned on given L3 interface will be re-learned

	"""
    def executeNdpRefreshByIfName(self,
                                  IfName):
        obj =  { 
                'IfName' : IfName,
                }
        reqUrl =  self.actionUrlBase+'NdpRefreshByIfName'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    """
    .. automethod :: createOspfVirtIfEntry(self,
        :param string VirtIfNeighbor : The Router ID of the virtual neighbor. The Router ID of the virtual neighbor.
        :param string VirtIfAreaId : The transit area that the virtual link traverses.  By definition The transit area that the virtual link traverses.  By definition
        :param int32 VirtIfTransitDelay : The estimated number of seconds it takes to transmit a Link State update packet over this interface.  Note that the minimal value SHOULD be 1 second. The estimated number of seconds it takes to transmit a Link State update packet over this interface.  Note that the minimal value SHOULD be 1 second.
        :param int32 VirtIfRetransInterval : The number of seconds between link state avertisement retransmissions The number of seconds between link state avertisement retransmissions
        :param int32 VirtIfHelloInterval : The length of time The length of time
        :param int32 VirtIfRtrDeadInterval : The number of seconds that a router's Hello packets have not been seen before its neighbors declare the router down.  This should be some multiple of the Hello interval.  This value must be the same for the virtual neighbor. The number of seconds that a router's Hello packets have not been seen before its neighbors declare the router down.  This should be some multiple of the Hello interval.  This value must be the same for the virtual neighbor.
        :param string VirtIfAuthKey : The cleartext password used as an OSPF authentication key when simplePassword security is enabled.  This object does not access any OSPF cryptogaphic (e.g. The cleartext password used as an OSPF authentication key when simplePassword security is enabled.  This object does not access any OSPF cryptogaphic (e.g.
        :param int32 VirtIfAuthType : The authentication type specified for a virtual interface.  Note that this object can be used to engage in significant attacks against an OSPF router. The authentication type specified for a virtual interface.  Note that this object can be used to engage in significant attacks against an OSPF router.

	"""
    def createOspfVirtIfEntry(self,
                              VirtIfNeighbor,
                              VirtIfAreaId,
                              VirtIfTransitDelay,
                              VirtIfRetransInterval,
                              VirtIfHelloInterval,
                              VirtIfRtrDeadInterval,
                              VirtIfAuthKey,
                              VirtIfAuthType):
        obj =  { 
                'VirtIfNeighbor' : VirtIfNeighbor,
                'VirtIfAreaId' : VirtIfAreaId,
                'VirtIfTransitDelay' : int(VirtIfTransitDelay),
                'VirtIfRetransInterval' : int(VirtIfRetransInterval),
                'VirtIfHelloInterval' : int(VirtIfHelloInterval),
                'VirtIfRtrDeadInterval' : int(VirtIfRtrDeadInterval),
                'VirtIfAuthKey' : VirtIfAuthKey,
                'VirtIfAuthType' : int(VirtIfAuthType),
                }
        reqUrl =  self.cfgUrlBase+'OspfVirtIfEntry'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteOspfVirtIfEntry(self,
                              VirtIfNeighbor,
                              VirtIfAreaId):
        obj =  { 
                'VirtIfNeighbor' : VirtIfNeighbor,
                'VirtIfAreaId' : VirtIfAreaId,
                }
        reqUrl =  self.cfgUrlBase+'OspfVirtIfEntry'
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteOspfVirtIfEntryById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'OspfVirtIfEntry'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        else:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        return r

    def updateOspfVirtIfEntry(self,
                              VirtIfNeighbor,
                              VirtIfAreaId,
                              VirtIfTransitDelay = None,
                              VirtIfRetransInterval = None,
                              VirtIfHelloInterval = None,
                              VirtIfRtrDeadInterval = None,
                              VirtIfAuthKey = None,
                              VirtIfAuthType = None):
        obj =  {}
        if VirtIfNeighbor != None :
            obj['VirtIfNeighbor'] = VirtIfNeighbor

        if VirtIfAreaId != None :
            obj['VirtIfAreaId'] = VirtIfAreaId

        if VirtIfTransitDelay != None :
            obj['VirtIfTransitDelay'] = int(VirtIfTransitDelay)

        if VirtIfRetransInterval != None :
            obj['VirtIfRetransInterval'] = int(VirtIfRetransInterval)

        if VirtIfHelloInterval != None :
            obj['VirtIfHelloInterval'] = int(VirtIfHelloInterval)

        if VirtIfRtrDeadInterval != None :
            obj['VirtIfRtrDeadInterval'] = int(VirtIfRtrDeadInterval)

        if VirtIfAuthKey != None :
            obj['VirtIfAuthKey'] = VirtIfAuthKey

        if VirtIfAuthType != None :
            obj['VirtIfAuthType'] = int(VirtIfAuthType)

        reqUrl =  self.cfgUrlBase+'OspfVirtIfEntry'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateOspfVirtIfEntryById(self,
                                   objectId,
                                   VirtIfTransitDelay = None,
                                   VirtIfRetransInterval = None,
                                   VirtIfHelloInterval = None,
                                   VirtIfRtrDeadInterval = None,
                                   VirtIfAuthKey = None,
                                   VirtIfAuthType = None):
        obj =  {}
        if VirtIfTransitDelay !=  None:
            obj['VirtIfTransitDelay'] = VirtIfTransitDelay

        if VirtIfRetransInterval !=  None:
            obj['VirtIfRetransInterval'] = VirtIfRetransInterval

        if VirtIfHelloInterval !=  None:
            obj['VirtIfHelloInterval'] = VirtIfHelloInterval

        if VirtIfRtrDeadInterval !=  None:
            obj['VirtIfRtrDeadInterval'] = VirtIfRtrDeadInterval

        if VirtIfAuthKey !=  None:
            obj['VirtIfAuthKey'] = VirtIfAuthKey

        if VirtIfAuthType !=  None:
            obj['VirtIfAuthType'] = VirtIfAuthType

        reqUrl =  self.cfgUrlBase+'OspfVirtIfEntry'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateOspfVirtIfEntry(self,
                                   VirtIfNeighbor,
                                   VirtIfAreaId,
                                   op,
                                   path,
                                   value,):
        obj =  {}
        obj['VirtIfNeighbor'] = VirtIfNeighbor
        obj['VirtIfAreaId'] = VirtIfAreaId
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'OspfVirtIfEntry'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getOspfVirtIfEntry(self,
                           VirtIfNeighbor,
                           VirtIfAreaId):
        obj =  { 
                'VirtIfNeighbor' : VirtIfNeighbor,
                'VirtIfAreaId' : VirtIfAreaId,
                }
        reqUrl =  self.cfgUrlBase + 'OspfVirtIfEntry'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getOspfVirtIfEntryById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'OspfVirtIfEntry'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllOspfVirtIfEntrys(self):
        return self.getObjects('OspfVirtIfEntry', self.cfgUrlBase)


    def getStpBridgeInstanceState(self,
                                  Vlan):
        obj =  { 
                'Vlan' : int(Vlan),
                }
        reqUrl =  self.stateUrlBase + 'StpBridgeInstance'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getStpBridgeInstanceStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'StpBridgeInstance'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllStpBridgeInstanceStates(self):
        return self.getObjects('StpBridgeInstance', self.stateUrlBase)


    def getAsicSummaryState(self,
                            ModuleId):
        obj =  { 
                'ModuleId' : int(ModuleId),
                }
        reqUrl =  self.stateUrlBase + 'AsicSummary'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getAsicSummaryStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'AsicSummary'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllAsicSummaryStates(self):
        return self.getObjects('AsicSummary', self.stateUrlBase)


    """
    .. automethod :: executeResetBGPv4NeighborByIPAddr(self,
        :param string IPAddr : IP address of the BGP IPv4 neighbor to restart IP address of the BGP IPv4 neighbor to restart

	"""
    def executeResetBGPv4NeighborByIPAddr(self,
                                          IPAddr):
        obj =  { 
                'IPAddr' : IPAddr,
                }
        reqUrl =  self.actionUrlBase+'ResetBGPv4NeighborByIPAddr'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getBGPPolicyActionState(self,
                                Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.stateUrlBase + 'BGPPolicyAction'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getBGPPolicyActionStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'BGPPolicyAction'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllBGPPolicyActionStates(self):
        return self.getObjects('BGPPolicyAction', self.stateUrlBase)


    """
    .. automethod :: createVxlanInstance(self,
        :param uint32 Vni : VNI domain VNI domain
        :param uint16 VlanId : Vlan associated with the Access targets.  Used in conjunction with a given VTEP inner-vlan-handling-mode Vlan associated with the Access targets.  Used in conjunction with a given VTEP inner-vlan-handling-mode

	"""
    def createVxlanInstance(self,
                            Vni,
                            VlanId):
        obj =  { 
                'Vni' : int(Vni),
                'VlanId' : int(VlanId),
                }
        reqUrl =  self.cfgUrlBase+'VxlanInstance'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteVxlanInstance(self,
                            Vni):
        obj =  { 
                'Vni' : Vni,
                }
        reqUrl =  self.cfgUrlBase+'VxlanInstance'
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteVxlanInstanceById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'VxlanInstance'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        else:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        return r

    def updateVxlanInstance(self,
                            Vni,
                            VlanId = None):
        obj =  {}
        if Vni != None :
            obj['Vni'] = int(Vni)

        if VlanId != None :
            obj['VlanId'] = int(VlanId)

        reqUrl =  self.cfgUrlBase+'VxlanInstance'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateVxlanInstanceById(self,
                                 objectId,
                                 VlanId = None):
        obj =  {}
        if VlanId !=  None:
            obj['VlanId'] = VlanId

        reqUrl =  self.cfgUrlBase+'VxlanInstance'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateVxlanInstance(self,
                                 Vni,
                                 op,
                                 path,
                                 value,):
        obj =  {}
        obj['Vni'] = Vni
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'VxlanInstance'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getVxlanInstance(self,
                         Vni):
        obj =  { 
                'Vni' : int(Vni),
                }
        reqUrl =  self.cfgUrlBase + 'VxlanInstance'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getVxlanInstanceById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'VxlanInstance'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllVxlanInstances(self):
        return self.getObjects('VxlanInstance', self.cfgUrlBase)


    """
    .. automethod :: executeArpRefreshByIfName(self,
        :param string IfName : All the Arp learned on given L3 interface will be re-learned All the Arp learned on given L3 interface will be re-learned

	"""
    def executeArpRefreshByIfName(self,
                                  IfName):
        obj =  { 
                'IfName' : IfName,
                }
        reqUrl =  self.actionUrlBase+'ArpRefreshByIfName'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getBGPPolicyDefinitionState(self,
                                    Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.stateUrlBase + 'BGPPolicyDefinition'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getBGPPolicyDefinitionStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'BGPPolicyDefinition'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllBGPPolicyDefinitionStates(self):
        return self.getObjects('BGPPolicyDefinition', self.stateUrlBase)


    def getLedState(self,
                    LedId):
        obj =  { 
                'LedId' : int(LedId),
                }
        reqUrl =  self.stateUrlBase + 'Led'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getLedStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'Led'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllLedStates(self):
        return self.getObjects('Led', self.stateUrlBase)


    def getIPv4IntfState(self,
                         IntfRef):
        obj =  { 
                'IntfRef' : IntfRef,
                }
        reqUrl =  self.stateUrlBase + 'IPv4Intf'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getIPv4IntfStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'IPv4Intf'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllIPv4IntfStates(self):
        return self.getObjects('IPv4Intf', self.stateUrlBase)


    def getPortState(self,
                     IntfRef):
        obj =  { 
                'IntfRef' : IntfRef,
                }
        reqUrl =  self.stateUrlBase + 'Port'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getPortStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'Port'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllPortStates(self):
        return self.getObjects('Port', self.stateUrlBase)


    def updateSfp(self,
                  SfpId,
                  AdminState = None):
        obj =  {}
        if SfpId != None :
            obj['SfpId'] = int(SfpId)

        if AdminState != None :
            obj['AdminState'] = AdminState

        reqUrl =  self.cfgUrlBase+'Sfp'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateSfpById(self,
                       objectId,
                       AdminState = None):
        obj =  {}
        if AdminState !=  None:
            obj['AdminState'] = AdminState

        reqUrl =  self.cfgUrlBase+'Sfp'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateSfp(self,
                       SfpId,
                       op,
                       path,
                       value,):
        obj =  {}
        obj['SfpId'] = SfpId
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'Sfp'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getSfp(self,
               SfpId):
        obj =  { 
                'SfpId' : int(SfpId),
                }
        reqUrl =  self.cfgUrlBase + 'Sfp'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getSfpById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'Sfp'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllSfps(self):
        return self.getObjects('Sfp', self.cfgUrlBase)


    """
    .. automethod :: createBGPPolicyAction(self,
        :param string Name : Name of the BGP policy action Name of the BGP policy action
        :param string ActionType : Type of the BGP policy action Type of the BGP policy action
        :param bool GenerateASSet : Enable/Disable generating AS set for BGP aggregate action Enable/Disable generating AS set for BGP aggregate action
        :param bool SendSummaryOnly : Enable/Disable sending summary only for BGP aggregate action Enable/Disable sending summary only for BGP aggregate action

	"""
    def createBGPPolicyAction(self,
                              Name,
                              ActionType,
                              GenerateASSet,
                              SendSummaryOnly):
        obj =  { 
                'Name' : Name,
                'ActionType' : ActionType,
                'GenerateASSet' : True if GenerateASSet else False,
                'SendSummaryOnly' : True if SendSummaryOnly else False,
                }
        reqUrl =  self.cfgUrlBase+'BGPPolicyAction'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteBGPPolicyAction(self,
                              Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.cfgUrlBase+'BGPPolicyAction'
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteBGPPolicyActionById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'BGPPolicyAction'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        else:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        return r

    def updateBGPPolicyAction(self,
                              Name,
                              ActionType = None,
                              GenerateASSet = None,
                              SendSummaryOnly = None):
        obj =  {}
        if Name != None :
            obj['Name'] = Name

        if ActionType != None :
            obj['ActionType'] = ActionType

        if GenerateASSet != None :
            obj['GenerateASSet'] = True if GenerateASSet else False

        if SendSummaryOnly != None :
            obj['SendSummaryOnly'] = True if SendSummaryOnly else False

        reqUrl =  self.cfgUrlBase+'BGPPolicyAction'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateBGPPolicyActionById(self,
                                   objectId,
                                   ActionType = None,
                                   GenerateASSet = None,
                                   SendSummaryOnly = None):
        obj =  {}
        if ActionType !=  None:
            obj['ActionType'] = ActionType

        if GenerateASSet !=  None:
            obj['GenerateASSet'] = GenerateASSet

        if SendSummaryOnly !=  None:
            obj['SendSummaryOnly'] = SendSummaryOnly

        reqUrl =  self.cfgUrlBase+'BGPPolicyAction'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateBGPPolicyAction(self,
                                   Name,
                                   op,
                                   path,
                                   value,):
        obj =  {}
        obj['Name'] = Name
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'BGPPolicyAction'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getBGPPolicyAction(self,
                           Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.cfgUrlBase + 'BGPPolicyAction'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getBGPPolicyActionById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'BGPPolicyAction'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllBGPPolicyActions(self):
        return self.getObjects('BGPPolicyAction', self.cfgUrlBase)


    """
    .. automethod :: executeAsicdClearCounters(self,
        :param string IntfRef : Clear counters on given interface Clear counters on given interface
        :param string Type : Clear counter for specific type like port Clear counter for specific type like port

	"""
    def executeAsicdClearCounters(self,
                                  IntfRef='All',
                                  Type='Port'):
        obj =  { 
                'IntfRef' : IntfRef,
                'Type' : Type,
                }
        reqUrl =  self.actionUrlBase+'AsicdClearCounters'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    """
    .. automethod :: executeResetBGPv6NeighborByIPAddr(self,
        :param string IPAddr : IP address of the BGP IPv6 neighbor to restart IP address of the BGP IPv6 neighbor to restart

	"""
    def executeResetBGPv6NeighborByIPAddr(self,
                                          IPAddr):
        obj =  { 
                'IPAddr' : IPAddr,
                }
        reqUrl =  self.actionUrlBase+'ResetBGPv6NeighborByIPAddr'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getSystemSwVersionState(self,
                                FlexswitchVersion):
        obj =  { 
                'FlexswitchVersion' : FlexswitchVersion,
                }
        reqUrl =  self.stateUrlBase + 'SystemSwVersion'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getSystemSwVersionStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'SystemSwVersion'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllSystemSwVersionStates(self):
        return self.getObjects('SystemSwVersion', self.stateUrlBase)


    """
    .. automethod :: executeNdpRefreshByIPv6Addr(self,
        :param string IpAddr : Neighbor's IPV6 Address for which corresponding NDP entry needs to be re-learned Neighbor's IPV6 Address for which corresponding NDP entry needs to be re-learned

	"""
    def executeNdpRefreshByIPv6Addr(self,
                                    IpAddr):
        obj =  { 
                'IpAddr' : IpAddr,
                }
        reqUrl =  self.actionUrlBase+'NdpRefreshByIPv6Addr'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getDaemonState(self,
                       Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.stateUrlBase + 'Daemon'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getDaemonStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'Daemon'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllDaemonStates(self):
        return self.getObjects('Daemon', self.stateUrlBase)


    def getSystemParamState(self,
                            Vrf):
        obj =  { 
                'Vrf' : Vrf,
                }
        reqUrl =  self.stateUrlBase + 'SystemParam'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getSystemParamStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'SystemParam'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllSystemParamStates(self):
        return self.getObjects('SystemParam', self.stateUrlBase)


    """
    .. automethod :: executeResetBfdSession(self,
        :param string IpAddr : Reset BFD session to this address Reset BFD session to this address

	"""
    def executeResetBfdSession(self,
                               IpAddr):
        obj =  { 
                'IpAddr' : IpAddr,
                }
        reqUrl =  self.actionUrlBase+'ResetBfdSession'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    def getVoltageSensorState(self,
                              Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.stateUrlBase + 'VoltageSensor'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getVoltageSensorStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'VoltageSensor'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllVoltageSensorStates(self):
        return self.getObjects('VoltageSensor', self.stateUrlBase)


    def getDWDMModuleNwIntfPMState(self,
                                   Resource,
                                   NwIntfId,
                                   Type,
                                   Class,
                                   ModuleId):
        obj =  { 
                'Resource' : Resource,
                'NwIntfId' : int(NwIntfId),
                'Type' : Type,
                'Class' : Class,
                'ModuleId' : int(ModuleId),
                }
        reqUrl =  self.stateUrlBase + 'DWDMModuleNwIntfPM'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getDWDMModuleNwIntfPMStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'DWDMModuleNwIntfPM'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllDWDMModuleNwIntfPMStates(self):
        return self.getObjects('DWDMModuleNwIntfPM', self.stateUrlBase)


    def updateDWDMModule(self,
                         ModuleId,
                         EnableExtPMTickSrc = None,
                         PMInterval = None,
                         AdminState = None,
                         IndependentLaneMode = None):
        obj =  {}
        if ModuleId != None :
            obj['ModuleId'] = int(ModuleId)

        if EnableExtPMTickSrc != None :
            obj['EnableExtPMTickSrc'] = True if EnableExtPMTickSrc else False

        if PMInterval != None :
            obj['PMInterval'] = int(PMInterval)

        if AdminState != None :
            obj['AdminState'] = AdminState

        if IndependentLaneMode != None :
            obj['IndependentLaneMode'] = True if IndependentLaneMode else False

        reqUrl =  self.cfgUrlBase+'DWDMModule'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateDWDMModuleById(self,
                              objectId,
                              EnableExtPMTickSrc = None,
                              PMInterval = None,
                              AdminState = None,
                              IndependentLaneMode = None):
        obj =  {}
        if EnableExtPMTickSrc !=  None:
            obj['EnableExtPMTickSrc'] = EnableExtPMTickSrc

        if PMInterval !=  None:
            obj['PMInterval'] = PMInterval

        if AdminState !=  None:
            obj['AdminState'] = AdminState

        if IndependentLaneMode !=  None:
            obj['IndependentLaneMode'] = IndependentLaneMode

        reqUrl =  self.cfgUrlBase+'DWDMModule'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateDWDMModule(self,
                              ModuleId,
                              op,
                              path,
                              value,):
        obj =  {}
        obj['ModuleId'] = ModuleId
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'DWDMModule'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getDWDMModule(self,
                      ModuleId):
        obj =  { 
                'ModuleId' : int(ModuleId),
                }
        reqUrl =  self.cfgUrlBase + 'DWDMModule'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getDWDMModuleById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'DWDMModule'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllDWDMModules(self):
        return self.getObjects('DWDMModule', self.cfgUrlBase)


    """
    .. automethod :: executeApplyConfig(self,

	"""
    def executeApplyConfig(self):
        obj =  { 
                }
        reqUrl =  self.actionUrlBase+'ApplyConfig'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers) 
        return r

    """
    .. automethod :: createAcl(self,
        :param string AclName : Acl name to be used to refer to this ACL Acl name to be used to refer to this ACL
        :param string Direction :  
        :param string AclType : Type can be IP/MAC/SVI Type can be IP/MAC/SVI
        :param string IntfList : list of IntfRef can be port/lag object list of IntfRef can be port/lag object
        :param string RuleNameList : List of rules to be applied to this ACL. This should match with AclRule RuleName List of rules to be applied to this ACL. This should match with AclRule RuleName

	"""
    def createAcl(self,
                  AclName,
                  Direction,
                  AclType,
                  IntfList,
                  RuleNameList):
        obj =  { 
                'AclName' : AclName,
                'Direction' : Direction,
                'AclType' : AclType,
                'IntfList' : IntfList,
                'RuleNameList' : RuleNameList,
                }
        reqUrl =  self.cfgUrlBase+'Acl'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteAcl(self,
                  AclName,
                  Direction):
        obj =  { 
                'AclName' : AclName,
                'Direction' : Direction,
                }
        reqUrl =  self.cfgUrlBase+'Acl'
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteAclById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'Acl'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        else:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        return r

    def updateAcl(self,
                  AclName,
                  Direction,
                  AclType = None,
                  IntfList = None,
                  RuleNameList = None):
        obj =  {}
        if AclName != None :
            obj['AclName'] = AclName

        if Direction != None :
            obj['Direction'] = Direction

        if AclType != None :
            obj['AclType'] = AclType

        if IntfList != None :
            obj['IntfList'] = IntfList

        if RuleNameList != None :
            obj['RuleNameList'] = RuleNameList

        reqUrl =  self.cfgUrlBase+'Acl'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateAclById(self,
                       objectId,
                       AclType = None,
                       IntfList = None,
                       RuleNameList = None):
        obj =  {}
        if AclType !=  None:
            obj['AclType'] = AclType

        if IntfList !=  None:
            obj['IntfList'] = IntfList

        if RuleNameList !=  None:
            obj['RuleNameList'] = RuleNameList

        reqUrl =  self.cfgUrlBase+'Acl'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateAcl(self,
                       AclName,
                       Direction,
                       op,
                       path,
                       value,):
        obj =  {}
        obj['AclName'] = AclName
        obj['Direction'] = Direction
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'Acl'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getAcl(self,
               AclName,
               Direction):
        obj =  { 
                'AclName' : AclName,
                'Direction' : Direction,
                }
        reqUrl =  self.cfgUrlBase + 'Acl'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getAclById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'Acl'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllAcls(self):
        return self.getObjects('Acl', self.cfgUrlBase)


    """
    .. automethod :: createBGPv6Neighbor(self,
        :param string IntfRef : Interface of the BGP neighbor Interface of the BGP neighbor
        :param string NeighborAddress : Address of the BGP neighbor Address of the BGP neighbor
        :param string Description : Description of the BGP neighbor Description of the BGP neighbor
        :param string PeerGroup : Peer group of the BGP neighbor Peer group of the BGP neighbor
        :param string PeerAS : Peer AS of the BGP neighbor Peer AS of the BGP neighbor
        :param string LocalAS : Local AS of the BGP neighbor Local AS of the BGP neighbor
        :param string UpdateSource : Source IP to connect to the BGP neighbor Source IP to connect to the BGP neighbor
        :param string AdjRIBInFilter : Policy that is applied for Adj-RIB-In prefix filtering Policy that is applied for Adj-RIB-In prefix filtering
        :param string AdjRIBOutFilter : Policy that is applied for Adj-RIB-Out prefix filtering Policy that is applied for Adj-RIB-Out prefix filtering
        :param bool BfdEnable : Enable/Disable BFD for the BGP neighbor Enable/Disable BFD for the BGP neighbor
        :param uint8 MultiHopTTL : TTL for multi hop BGP neighbor TTL for multi hop BGP neighbor
        :param uint32 KeepaliveTime : Keep alive time for the BGP neighbor Keep alive time for the BGP neighbor
        :param bool AddPathsRx : Receive additional paths from BGP neighbor Receive additional paths from BGP neighbor
        :param bool RouteReflectorClient : Set/Clear BGP neighbor as a route reflector client Set/Clear BGP neighbor as a route reflector client
        :param uint8 MaxPrefixesRestartTimer : Time in seconds to wait before we start BGP peer session when we receive max prefixes Time in seconds to wait before we start BGP peer session when we receive max prefixes
        :param bool MultiHopEnable : Enable/Disable multi hop for BGP neighbor Enable/Disable multi hop for BGP neighbor
        :param uint32 RouteReflectorClusterId : Cluster Id of the internal BGP neighbor route reflector client Cluster Id of the internal BGP neighbor route reflector client
        :param bool MaxPrefixesDisconnect : Disconnect the BGP peer session when we receive the max prefixes from the neighbor Disconnect the BGP peer session when we receive the max prefixes from the neighbor
        :param uint8 AddPathsMaxTx : Max number of additional paths that can be transmitted to BGP neighbor Max number of additional paths that can be transmitted to BGP neighbor
        :param uint32 MaxPrefixes : Maximum number of prefixes that can be received from the BGP neighbor Maximum number of prefixes that can be received from the BGP neighbor
        :param uint8 MaxPrefixesThresholdPct : The percentage of maximum prefixes before we start logging The percentage of maximum prefixes before we start logging
        :param string BfdSessionParam : Bfd session param name to be applied Bfd session param name to be applied
        :param bool Disabled : Enable/Disable the BGP neighbor Enable/Disable the BGP neighbor
        :param uint32 HoldTime : Hold time for the BGP neighbor Hold time for the BGP neighbor
        :param uint32 ConnectRetryTime : Connect retry time to connect to BGP neighbor after disconnect Connect retry time to connect to BGP neighbor after disconnect

	"""
    def createBGPv6Neighbor(self,
                            IntfRef,
                            NeighborAddress,
                            Description='',
                            PeerGroup='',
                            PeerAS='',
                            LocalAS='',
                            UpdateSource='',
                            AdjRIBInFilter='',
                            AdjRIBOutFilter='',
                            BfdEnable=False,
                            MultiHopTTL=0,
                            KeepaliveTime=0,
                            AddPathsRx=False,
                            RouteReflectorClient=False,
                            MaxPrefixesRestartTimer=0,
                            MultiHopEnable=False,
                            RouteReflectorClusterId=0,
                            MaxPrefixesDisconnect=False,
                            AddPathsMaxTx=0,
                            MaxPrefixes=0,
                            MaxPrefixesThresholdPct=80,
                            BfdSessionParam='default',
                            Disabled=False,
                            HoldTime=0,
                            ConnectRetryTime=0):
        obj =  { 
                'IntfRef' : IntfRef,
                'NeighborAddress' : NeighborAddress,
                'Description' : Description,
                'PeerGroup' : PeerGroup,
                'PeerAS' : PeerAS,
                'LocalAS' : LocalAS,
                'UpdateSource' : UpdateSource,
                'AdjRIBInFilter' : AdjRIBInFilter,
                'AdjRIBOutFilter' : AdjRIBOutFilter,
                'BfdEnable' : True if BfdEnable else False,
                'MultiHopTTL' : int(MultiHopTTL),
                'KeepaliveTime' : int(KeepaliveTime),
                'AddPathsRx' : True if AddPathsRx else False,
                'RouteReflectorClient' : True if RouteReflectorClient else False,
                'MaxPrefixesRestartTimer' : int(MaxPrefixesRestartTimer),
                'MultiHopEnable' : True if MultiHopEnable else False,
                'RouteReflectorClusterId' : int(RouteReflectorClusterId),
                'MaxPrefixesDisconnect' : True if MaxPrefixesDisconnect else False,
                'AddPathsMaxTx' : int(AddPathsMaxTx),
                'MaxPrefixes' : int(MaxPrefixes),
                'MaxPrefixesThresholdPct' : int(MaxPrefixesThresholdPct),
                'BfdSessionParam' : BfdSessionParam,
                'Disabled' : True if Disabled else False,
                'HoldTime' : int(HoldTime),
                'ConnectRetryTime' : int(ConnectRetryTime),
                }
        reqUrl =  self.cfgUrlBase+'BGPv6Neighbor'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteBGPv6Neighbor(self,
                            IntfRef,
                            NeighborAddress):
        obj =  { 
                'IntfRef' : IntfRef,
                'NeighborAddress' : NeighborAddress,
                }
        reqUrl =  self.cfgUrlBase+'BGPv6Neighbor'
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteBGPv6NeighborById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'BGPv6Neighbor'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        else:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        return r

    def updateBGPv6Neighbor(self,
                            IntfRef,
                            NeighborAddress,
                            Description = None,
                            PeerGroup = None,
                            PeerAS = None,
                            LocalAS = None,
                            UpdateSource = None,
                            AdjRIBInFilter = None,
                            AdjRIBOutFilter = None,
                            BfdEnable = None,
                            MultiHopTTL = None,
                            KeepaliveTime = None,
                            AddPathsRx = None,
                            RouteReflectorClient = None,
                            MaxPrefixesRestartTimer = None,
                            MultiHopEnable = None,
                            RouteReflectorClusterId = None,
                            MaxPrefixesDisconnect = None,
                            AddPathsMaxTx = None,
                            MaxPrefixes = None,
                            MaxPrefixesThresholdPct = None,
                            BfdSessionParam = None,
                            Disabled = None,
                            HoldTime = None,
                            ConnectRetryTime = None):
        obj =  {}
        if IntfRef != None :
            obj['IntfRef'] = IntfRef

        if NeighborAddress != None :
            obj['NeighborAddress'] = NeighborAddress

        if Description != None :
            obj['Description'] = Description

        if PeerGroup != None :
            obj['PeerGroup'] = PeerGroup

        if PeerAS != None :
            obj['PeerAS'] = PeerAS

        if LocalAS != None :
            obj['LocalAS'] = LocalAS

        if UpdateSource != None :
            obj['UpdateSource'] = UpdateSource

        if AdjRIBInFilter != None :
            obj['AdjRIBInFilter'] = AdjRIBInFilter

        if AdjRIBOutFilter != None :
            obj['AdjRIBOutFilter'] = AdjRIBOutFilter

        if BfdEnable != None :
            obj['BfdEnable'] = True if BfdEnable else False

        if MultiHopTTL != None :
            obj['MultiHopTTL'] = int(MultiHopTTL)

        if KeepaliveTime != None :
            obj['KeepaliveTime'] = int(KeepaliveTime)

        if AddPathsRx != None :
            obj['AddPathsRx'] = True if AddPathsRx else False

        if RouteReflectorClient != None :
            obj['RouteReflectorClient'] = True if RouteReflectorClient else False

        if MaxPrefixesRestartTimer != None :
            obj['MaxPrefixesRestartTimer'] = int(MaxPrefixesRestartTimer)

        if MultiHopEnable != None :
            obj['MultiHopEnable'] = True if MultiHopEnable else False

        if RouteReflectorClusterId != None :
            obj['RouteReflectorClusterId'] = int(RouteReflectorClusterId)

        if MaxPrefixesDisconnect != None :
            obj['MaxPrefixesDisconnect'] = True if MaxPrefixesDisconnect else False

        if AddPathsMaxTx != None :
            obj['AddPathsMaxTx'] = int(AddPathsMaxTx)

        if MaxPrefixes != None :
            obj['MaxPrefixes'] = int(MaxPrefixes)

        if MaxPrefixesThresholdPct != None :
            obj['MaxPrefixesThresholdPct'] = int(MaxPrefixesThresholdPct)

        if BfdSessionParam != None :
            obj['BfdSessionParam'] = BfdSessionParam

        if Disabled != None :
            obj['Disabled'] = True if Disabled else False

        if HoldTime != None :
            obj['HoldTime'] = int(HoldTime)

        if ConnectRetryTime != None :
            obj['ConnectRetryTime'] = int(ConnectRetryTime)

        reqUrl =  self.cfgUrlBase+'BGPv6Neighbor'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateBGPv6NeighborById(self,
                                 objectId,
                                 Description = None,
                                 PeerGroup = None,
                                 PeerAS = None,
                                 LocalAS = None,
                                 UpdateSource = None,
                                 AdjRIBInFilter = None,
                                 AdjRIBOutFilter = None,
                                 BfdEnable = None,
                                 MultiHopTTL = None,
                                 KeepaliveTime = None,
                                 AddPathsRx = None,
                                 RouteReflectorClient = None,
                                 MaxPrefixesRestartTimer = None,
                                 MultiHopEnable = None,
                                 RouteReflectorClusterId = None,
                                 MaxPrefixesDisconnect = None,
                                 AddPathsMaxTx = None,
                                 MaxPrefixes = None,
                                 MaxPrefixesThresholdPct = None,
                                 BfdSessionParam = None,
                                 Disabled = None,
                                 HoldTime = None,
                                 ConnectRetryTime = None):
        obj =  {}
        if Description !=  None:
            obj['Description'] = Description

        if PeerGroup !=  None:
            obj['PeerGroup'] = PeerGroup

        if PeerAS !=  None:
            obj['PeerAS'] = PeerAS

        if LocalAS !=  None:
            obj['LocalAS'] = LocalAS

        if UpdateSource !=  None:
            obj['UpdateSource'] = UpdateSource

        if AdjRIBInFilter !=  None:
            obj['AdjRIBInFilter'] = AdjRIBInFilter

        if AdjRIBOutFilter !=  None:
            obj['AdjRIBOutFilter'] = AdjRIBOutFilter

        if BfdEnable !=  None:
            obj['BfdEnable'] = BfdEnable

        if MultiHopTTL !=  None:
            obj['MultiHopTTL'] = MultiHopTTL

        if KeepaliveTime !=  None:
            obj['KeepaliveTime'] = KeepaliveTime

        if AddPathsRx !=  None:
            obj['AddPathsRx'] = AddPathsRx

        if RouteReflectorClient !=  None:
            obj['RouteReflectorClient'] = RouteReflectorClient

        if MaxPrefixesRestartTimer !=  None:
            obj['MaxPrefixesRestartTimer'] = MaxPrefixesRestartTimer

        if MultiHopEnable !=  None:
            obj['MultiHopEnable'] = MultiHopEnable

        if RouteReflectorClusterId !=  None:
            obj['RouteReflectorClusterId'] = RouteReflectorClusterId

        if MaxPrefixesDisconnect !=  None:
            obj['MaxPrefixesDisconnect'] = MaxPrefixesDisconnect

        if AddPathsMaxTx !=  None:
            obj['AddPathsMaxTx'] = AddPathsMaxTx

        if MaxPrefixes !=  None:
            obj['MaxPrefixes'] = MaxPrefixes

        if MaxPrefixesThresholdPct !=  None:
            obj['MaxPrefixesThresholdPct'] = MaxPrefixesThresholdPct

        if BfdSessionParam !=  None:
            obj['BfdSessionParam'] = BfdSessionParam

        if Disabled !=  None:
            obj['Disabled'] = Disabled

        if HoldTime !=  None:
            obj['HoldTime'] = HoldTime

        if ConnectRetryTime !=  None:
            obj['ConnectRetryTime'] = ConnectRetryTime

        reqUrl =  self.cfgUrlBase+'BGPv6Neighbor'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateBGPv6Neighbor(self,
                                 IntfRef,
                                 NeighborAddress,
                                 op,
                                 path,
                                 value,):
        obj =  {}
        obj['IntfRef'] = IntfRef
        obj['NeighborAddress'] = NeighborAddress
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'BGPv6Neighbor'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getBGPv6Neighbor(self,
                         IntfRef,
                         NeighborAddress):
        obj =  { 
                'IntfRef' : IntfRef,
                'NeighborAddress' : NeighborAddress,
                }
        reqUrl =  self.cfgUrlBase + 'BGPv6Neighbor'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getBGPv6NeighborById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'BGPv6Neighbor'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllBGPv6Neighbors(self):
        return self.getObjects('BGPv6Neighbor', self.cfgUrlBase)


    def updateStpPort(self,
                      Vlan,
                      IntfRef,
                      PathCost = None,
                      AdminEdgePort = None,
                      ProtocolMigration = None,
                      BridgeAssurance = None,
                      Priority = None,
                      AdminState = None,
                      BpduGuard = None,
                      AdminPointToPoint = None,
                      BpduGuardInterval = None,
                      AdminPathCost = None,
                      PathCost32 = None):
        obj =  {}
        if Vlan != None :
            obj['Vlan'] = int(Vlan)

        if IntfRef != None :
            obj['IntfRef'] = IntfRef

        if PathCost != None :
            obj['PathCost'] = int(PathCost)

        if AdminEdgePort != None :
            obj['AdminEdgePort'] = int(AdminEdgePort)

        if ProtocolMigration != None :
            obj['ProtocolMigration'] = int(ProtocolMigration)

        if BridgeAssurance != None :
            obj['BridgeAssurance'] = int(BridgeAssurance)

        if Priority != None :
            obj['Priority'] = int(Priority)

        if AdminState != None :
            obj['AdminState'] = AdminState

        if BpduGuard != None :
            obj['BpduGuard'] = int(BpduGuard)

        if AdminPointToPoint != None :
            obj['AdminPointToPoint'] = int(AdminPointToPoint)

        if BpduGuardInterval != None :
            obj['BpduGuardInterval'] = int(BpduGuardInterval)

        if AdminPathCost != None :
            obj['AdminPathCost'] = int(AdminPathCost)

        if PathCost32 != None :
            obj['PathCost32'] = int(PathCost32)

        reqUrl =  self.cfgUrlBase+'StpPort'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateStpPortById(self,
                           objectId,
                           PathCost = None,
                           AdminEdgePort = None,
                           ProtocolMigration = None,
                           BridgeAssurance = None,
                           Priority = None,
                           AdminState = None,
                           BpduGuard = None,
                           AdminPointToPoint = None,
                           BpduGuardInterval = None,
                           AdminPathCost = None,
                           PathCost32 = None):
        obj =  {}
        if PathCost !=  None:
            obj['PathCost'] = PathCost

        if AdminEdgePort !=  None:
            obj['AdminEdgePort'] = AdminEdgePort

        if ProtocolMigration !=  None:
            obj['ProtocolMigration'] = ProtocolMigration

        if BridgeAssurance !=  None:
            obj['BridgeAssurance'] = BridgeAssurance

        if Priority !=  None:
            obj['Priority'] = Priority

        if AdminState !=  None:
            obj['AdminState'] = AdminState

        if BpduGuard !=  None:
            obj['BpduGuard'] = BpduGuard

        if AdminPointToPoint !=  None:
            obj['AdminPointToPoint'] = AdminPointToPoint

        if BpduGuardInterval !=  None:
            obj['BpduGuardInterval'] = BpduGuardInterval

        if AdminPathCost !=  None:
            obj['AdminPathCost'] = AdminPathCost

        if PathCost32 !=  None:
            obj['PathCost32'] = PathCost32

        reqUrl =  self.cfgUrlBase+'StpPort'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateStpPort(self,
                           Vlan,
                           IntfRef,
                           op,
                           path,
                           value,):
        obj =  {}
        obj['Vlan'] = Vlan
        obj['IntfRef'] = IntfRef
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'StpPort'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getStpPort(self,
                   Vlan,
                   IntfRef):
        obj =  { 
                'Vlan' : int(Vlan),
                'IntfRef' : IntfRef,
                }
        reqUrl =  self.cfgUrlBase + 'StpPort'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getStpPortById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'StpPort'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllStpPorts(self):
        return self.getObjects('StpPort', self.cfgUrlBase)


    """
    .. automethod :: createIPv4Route(self,
        :param string DestinationNw : IP address of the route IP address of the route
        :param string NetworkMask : mask of the route mask of the route
        :param NextHopInfo NextHop :  
        :param string Protocol : Protocol type of the route Protocol type of the route
        :param bool NullRoute : Specify if this is a null route Specify if this is a null route
        :param uint32 Cost : Cost of this route Cost of this route

	"""
    def createIPv4Route(self,
                        DestinationNw,
                        NetworkMask,
                        NextHop,
                        Protocol='STATIC',
                        NullRoute=False,
                        Cost=0):
        obj =  { 
                'DestinationNw' : DestinationNw,
                'NetworkMask' : NetworkMask,
                'NextHop' : NextHop,
                'Protocol' : Protocol,
                'NullRoute' : True if NullRoute else False,
                'Cost' : int(Cost),
                }
        reqUrl =  self.cfgUrlBase+'IPv4Route'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteIPv4Route(self,
                        DestinationNw,
                        NetworkMask):
        obj =  { 
                'DestinationNw' : DestinationNw,
                'NetworkMask' : NetworkMask,
                }
        reqUrl =  self.cfgUrlBase+'IPv4Route'
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteIPv4RouteById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'IPv4Route'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        else:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        return r

    def updateIPv4Route(self,
                        DestinationNw,
                        NetworkMask,
                        NextHop = None,
                        Protocol = None,
                        NullRoute = None,
                        Cost = None):
        obj =  {}
        if DestinationNw != None :
            obj['DestinationNw'] = DestinationNw

        if NetworkMask != None :
            obj['NetworkMask'] = NetworkMask

        if NextHop != None :
            obj['NextHop'] = NextHop

        if Protocol != None :
            obj['Protocol'] = Protocol

        if NullRoute != None :
            obj['NullRoute'] = True if NullRoute else False

        if Cost != None :
            obj['Cost'] = int(Cost)

        reqUrl =  self.cfgUrlBase+'IPv4Route'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateIPv4RouteById(self,
                             objectId,
                             NextHop = None,
                             Protocol = None,
                             NullRoute = None,
                             Cost = None):
        obj =  {}
        if NextHop !=  None:
            obj['NextHop'] = NextHop

        if Protocol !=  None:
            obj['Protocol'] = Protocol

        if NullRoute !=  None:
            obj['NullRoute'] = NullRoute

        if Cost !=  None:
            obj['Cost'] = Cost

        reqUrl =  self.cfgUrlBase+'IPv4Route'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateIPv4Route(self,
                             DestinationNw,
                             NetworkMask,
                             op,
                             path,
                             value,):
        obj =  {}
        obj['DestinationNw'] = DestinationNw
        obj['NetworkMask'] = NetworkMask
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'IPv4Route'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getIPv4Route(self,
                     DestinationNw,
                     NetworkMask):
        obj =  { 
                'DestinationNw' : DestinationNw,
                'NetworkMask' : NetworkMask,
                }
        reqUrl =  self.cfgUrlBase + 'IPv4Route'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getIPv4RouteById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'IPv4Route'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllIPv4Routes(self):
        return self.getObjects('IPv4Route', self.cfgUrlBase)


    """
    .. automethod :: createBGPv6PeerGroup(self,
        :param string Name : Name of the BGP peer group Name of the BGP peer group
        :param string PeerAS : Peer AS of the BGP neighbor Peer AS of the BGP neighbor
        :param string LocalAS : Local AS of the BGP neighbor Local AS of the BGP neighbor
        :param string UpdateSource : Source IP to connect to the BGP neighbor Source IP to connect to the BGP neighbor
        :param string Description : Description of the BGP neighbor Description of the BGP neighbor
        :param string AdjRIBInFilter : Policy that is applied for Adj-RIB-In prefix filtering Policy that is applied for Adj-RIB-In prefix filtering
        :param string AdjRIBOutFilter : Policy that is applied for Adj-RIB-Out prefix filtering Policy that is applied for Adj-RIB-Out prefix filtering
        :param uint8 MaxPrefixesRestartTimer : Time to wait before we start BGP peer session when we receive max prefixes Time to wait before we start BGP peer session when we receive max prefixes
        :param bool MultiHopEnable : Enable/Disable multi hop for BGP neighbor Enable/Disable multi hop for BGP neighbor
        :param bool MaxPrefixesDisconnect : Disconnect the BGP peer session when we receive the max prefixes from the neighbor Disconnect the BGP peer session when we receive the max prefixes from the neighbor
        :param uint8 MultiHopTTL : TTL for multi hop BGP neighbor TTL for multi hop BGP neighbor
        :param uint32 KeepaliveTime : Keep alive time for the BGP neighbor Keep alive time for the BGP neighbor
        :param uint32 RouteReflectorClusterId : Cluster Id of the internal BGP neighbor route reflector client Cluster Id of the internal BGP neighbor route reflector client
        :param uint8 AddPathsMaxTx : Max number of additional paths that can be transmitted to BGP neighbor Max number of additional paths that can be transmitted to BGP neighbor
        :param bool AddPathsRx : Receive additional paths from BGP neighbor Receive additional paths from BGP neighbor
        :param bool RouteReflectorClient : Set/Clear BGP neighbor as a route reflector client Set/Clear BGP neighbor as a route reflector client
        :param uint8 MaxPrefixesThresholdPct : The percentage of maximum prefixes before we start logging The percentage of maximum prefixes before we start logging
        :param uint32 HoldTime : Hold time for the BGP neighbor Hold time for the BGP neighbor
        :param uint32 MaxPrefixes : Maximum number of prefixes that can be received from the BGP neighbor Maximum number of prefixes that can be received from the BGP neighbor
        :param uint32 ConnectRetryTime : Connect retry time to connect to BGP neighbor after disconnect Connect retry time to connect to BGP neighbor after disconnect

	"""
    def createBGPv6PeerGroup(self,
                             Name,
                             PeerAS='',
                             LocalAS='',
                             UpdateSource='',
                             Description='',
                             AdjRIBInFilter='',
                             AdjRIBOutFilter='',
                             MaxPrefixesRestartTimer=0,
                             MultiHopEnable=False,
                             MaxPrefixesDisconnect=False,
                             MultiHopTTL=0,
                             KeepaliveTime=0,
                             RouteReflectorClusterId=0,
                             AddPathsMaxTx=0,
                             AddPathsRx=False,
                             RouteReflectorClient=False,
                             MaxPrefixesThresholdPct=80,
                             HoldTime=0,
                             MaxPrefixes=0,
                             ConnectRetryTime=0):
        obj =  { 
                'Name' : Name,
                'PeerAS' : PeerAS,
                'LocalAS' : LocalAS,
                'UpdateSource' : UpdateSource,
                'Description' : Description,
                'AdjRIBInFilter' : AdjRIBInFilter,
                'AdjRIBOutFilter' : AdjRIBOutFilter,
                'MaxPrefixesRestartTimer' : int(MaxPrefixesRestartTimer),
                'MultiHopEnable' : True if MultiHopEnable else False,
                'MaxPrefixesDisconnect' : True if MaxPrefixesDisconnect else False,
                'MultiHopTTL' : int(MultiHopTTL),
                'KeepaliveTime' : int(KeepaliveTime),
                'RouteReflectorClusterId' : int(RouteReflectorClusterId),
                'AddPathsMaxTx' : int(AddPathsMaxTx),
                'AddPathsRx' : True if AddPathsRx else False,
                'RouteReflectorClient' : True if RouteReflectorClient else False,
                'MaxPrefixesThresholdPct' : int(MaxPrefixesThresholdPct),
                'HoldTime' : int(HoldTime),
                'MaxPrefixes' : int(MaxPrefixes),
                'ConnectRetryTime' : int(ConnectRetryTime),
                }
        reqUrl =  self.cfgUrlBase+'BGPv6PeerGroup'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteBGPv6PeerGroup(self,
                             Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.cfgUrlBase+'BGPv6PeerGroup'
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteBGPv6PeerGroupById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'BGPv6PeerGroup'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        else:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        return r

    def updateBGPv6PeerGroup(self,
                             Name,
                             PeerAS = None,
                             LocalAS = None,
                             UpdateSource = None,
                             Description = None,
                             AdjRIBInFilter = None,
                             AdjRIBOutFilter = None,
                             MaxPrefixesRestartTimer = None,
                             MultiHopEnable = None,
                             MaxPrefixesDisconnect = None,
                             MultiHopTTL = None,
                             KeepaliveTime = None,
                             RouteReflectorClusterId = None,
                             AddPathsMaxTx = None,
                             AddPathsRx = None,
                             RouteReflectorClient = None,
                             MaxPrefixesThresholdPct = None,
                             HoldTime = None,
                             MaxPrefixes = None,
                             ConnectRetryTime = None):
        obj =  {}
        if Name != None :
            obj['Name'] = Name

        if PeerAS != None :
            obj['PeerAS'] = PeerAS

        if LocalAS != None :
            obj['LocalAS'] = LocalAS

        if UpdateSource != None :
            obj['UpdateSource'] = UpdateSource

        if Description != None :
            obj['Description'] = Description

        if AdjRIBInFilter != None :
            obj['AdjRIBInFilter'] = AdjRIBInFilter

        if AdjRIBOutFilter != None :
            obj['AdjRIBOutFilter'] = AdjRIBOutFilter

        if MaxPrefixesRestartTimer != None :
            obj['MaxPrefixesRestartTimer'] = int(MaxPrefixesRestartTimer)

        if MultiHopEnable != None :
            obj['MultiHopEnable'] = True if MultiHopEnable else False

        if MaxPrefixesDisconnect != None :
            obj['MaxPrefixesDisconnect'] = True if MaxPrefixesDisconnect else False

        if MultiHopTTL != None :
            obj['MultiHopTTL'] = int(MultiHopTTL)

        if KeepaliveTime != None :
            obj['KeepaliveTime'] = int(KeepaliveTime)

        if RouteReflectorClusterId != None :
            obj['RouteReflectorClusterId'] = int(RouteReflectorClusterId)

        if AddPathsMaxTx != None :
            obj['AddPathsMaxTx'] = int(AddPathsMaxTx)

        if AddPathsRx != None :
            obj['AddPathsRx'] = True if AddPathsRx else False

        if RouteReflectorClient != None :
            obj['RouteReflectorClient'] = True if RouteReflectorClient else False

        if MaxPrefixesThresholdPct != None :
            obj['MaxPrefixesThresholdPct'] = int(MaxPrefixesThresholdPct)

        if HoldTime != None :
            obj['HoldTime'] = int(HoldTime)

        if MaxPrefixes != None :
            obj['MaxPrefixes'] = int(MaxPrefixes)

        if ConnectRetryTime != None :
            obj['ConnectRetryTime'] = int(ConnectRetryTime)

        reqUrl =  self.cfgUrlBase+'BGPv6PeerGroup'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateBGPv6PeerGroupById(self,
                                  objectId,
                                  PeerAS = None,
                                  LocalAS = None,
                                  UpdateSource = None,
                                  Description = None,
                                  AdjRIBInFilter = None,
                                  AdjRIBOutFilter = None,
                                  MaxPrefixesRestartTimer = None,
                                  MultiHopEnable = None,
                                  MaxPrefixesDisconnect = None,
                                  MultiHopTTL = None,
                                  KeepaliveTime = None,
                                  RouteReflectorClusterId = None,
                                  AddPathsMaxTx = None,
                                  AddPathsRx = None,
                                  RouteReflectorClient = None,
                                  MaxPrefixesThresholdPct = None,
                                  HoldTime = None,
                                  MaxPrefixes = None,
                                  ConnectRetryTime = None):
        obj =  {}
        if PeerAS !=  None:
            obj['PeerAS'] = PeerAS

        if LocalAS !=  None:
            obj['LocalAS'] = LocalAS

        if UpdateSource !=  None:
            obj['UpdateSource'] = UpdateSource

        if Description !=  None:
            obj['Description'] = Description

        if AdjRIBInFilter !=  None:
            obj['AdjRIBInFilter'] = AdjRIBInFilter

        if AdjRIBOutFilter !=  None:
            obj['AdjRIBOutFilter'] = AdjRIBOutFilter

        if MaxPrefixesRestartTimer !=  None:
            obj['MaxPrefixesRestartTimer'] = MaxPrefixesRestartTimer

        if MultiHopEnable !=  None:
            obj['MultiHopEnable'] = MultiHopEnable

        if MaxPrefixesDisconnect !=  None:
            obj['MaxPrefixesDisconnect'] = MaxPrefixesDisconnect

        if MultiHopTTL !=  None:
            obj['MultiHopTTL'] = MultiHopTTL

        if KeepaliveTime !=  None:
            obj['KeepaliveTime'] = KeepaliveTime

        if RouteReflectorClusterId !=  None:
            obj['RouteReflectorClusterId'] = RouteReflectorClusterId

        if AddPathsMaxTx !=  None:
            obj['AddPathsMaxTx'] = AddPathsMaxTx

        if AddPathsRx !=  None:
            obj['AddPathsRx'] = AddPathsRx

        if RouteReflectorClient !=  None:
            obj['RouteReflectorClient'] = RouteReflectorClient

        if MaxPrefixesThresholdPct !=  None:
            obj['MaxPrefixesThresholdPct'] = MaxPrefixesThresholdPct

        if HoldTime !=  None:
            obj['HoldTime'] = HoldTime

        if MaxPrefixes !=  None:
            obj['MaxPrefixes'] = MaxPrefixes

        if ConnectRetryTime !=  None:
            obj['ConnectRetryTime'] = ConnectRetryTime

        reqUrl =  self.cfgUrlBase+'BGPv6PeerGroup'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateBGPv6PeerGroup(self,
                                  Name,
                                  op,
                                  path,
                                  value,):
        obj =  {}
        obj['Name'] = Name
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'BGPv6PeerGroup'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getBGPv6PeerGroup(self,
                          Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.cfgUrlBase + 'BGPv6PeerGroup'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getBGPv6PeerGroupById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'BGPv6PeerGroup'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllBGPv6PeerGroups(self):
        return self.getObjects('BGPv6PeerGroup', self.cfgUrlBase)


    def getArpEntryHwState(self,
                           IpAddr):
        obj =  { 
                'IpAddr' : IpAddr,
                }
        reqUrl =  self.stateUrlBase + 'ArpEntryHw'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getArpEntryHwStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'ArpEntryHw'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllArpEntryHwStates(self):
        return self.getObjects('ArpEntryHw', self.stateUrlBase)


    def getOspfGlobalState(self,
                           RouterId):
        obj =  { 
                'RouterId' : RouterId,
                }
        reqUrl =  self.stateUrlBase + 'OspfGlobal'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getOspfGlobalStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'OspfGlobal'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllOspfGlobalStates(self):
        return self.getObjects('OspfGlobal', self.stateUrlBase)


    """
    .. automethod :: createIPv6Intf(self,
        :param string IntfRef : Interface name or ifindex of port/lag or vlan on which this IPv4 object is configured Interface name or ifindex of port/lag or vlan on which this IPv4 object is configured
        :param string IpAddr : Interface Global Scope IP Address/Prefix-Length to provision on switch interface Interface Global Scope IP Address/Prefix-Length to provision on switch interface
        :param string AdminState : Administrative state of this IP interface Administrative state of this IP interface
        :param bool LinkIp : Interface Link Scope IP Address auto-configured Interface Link Scope IP Address auto-configured

	"""
    def createIPv6Intf(self,
                       IntfRef,
                       IpAddr='',
                       AdminState='UP',
                       LinkIp=True):
        obj =  { 
                'IntfRef' : IntfRef,
                'IpAddr' : IpAddr,
                'AdminState' : AdminState,
                'LinkIp' : True if LinkIp else False,
                }
        reqUrl =  self.cfgUrlBase+'IPv6Intf'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteIPv6Intf(self,
                       IntfRef):
        obj =  { 
                'IntfRef' : IntfRef,
                }
        reqUrl =  self.cfgUrlBase+'IPv6Intf'
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteIPv6IntfById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'IPv6Intf'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        else:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        return r

    def updateIPv6Intf(self,
                       IntfRef,
                       IpAddr = None,
                       AdminState = None,
                       LinkIp = None):
        obj =  {}
        if IntfRef != None :
            obj['IntfRef'] = IntfRef

        if IpAddr != None :
            obj['IpAddr'] = IpAddr

        if AdminState != None :
            obj['AdminState'] = AdminState

        if LinkIp != None :
            obj['LinkIp'] = True if LinkIp else False

        reqUrl =  self.cfgUrlBase+'IPv6Intf'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateIPv6IntfById(self,
                            objectId,
                            IpAddr = None,
                            AdminState = None,
                            LinkIp = None):
        obj =  {}
        if IpAddr !=  None:
            obj['IpAddr'] = IpAddr

        if AdminState !=  None:
            obj['AdminState'] = AdminState

        if LinkIp !=  None:
            obj['LinkIp'] = LinkIp

        reqUrl =  self.cfgUrlBase+'IPv6Intf'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateIPv6Intf(self,
                            IntfRef,
                            op,
                            path,
                            value,):
        obj =  {}
        obj['IntfRef'] = IntfRef
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'IPv6Intf'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getIPv6Intf(self,
                    IntfRef):
        obj =  { 
                'IntfRef' : IntfRef,
                }
        reqUrl =  self.cfgUrlBase + 'IPv6Intf'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getIPv6IntfById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'IPv6Intf'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllIPv6Intfs(self):
        return self.getObjects('IPv6Intf', self.cfgUrlBase)


    def getRouteStatsPerProtocolState(self,
                                      Protocol):
        obj =  { 
                'Protocol' : Protocol,
                }
        reqUrl =  self.stateUrlBase + 'RouteStatsPerProtocol'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getRouteStatsPerProtocolStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'RouteStatsPerProtocol'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllRouteStatsPerProtocolStates(self):
        return self.getObjects('RouteStatsPerProtocol', self.stateUrlBase)


    def updateIsisGlobal(self,
                         Vrf,
                         Enable = None):
        obj =  {}
        if Vrf != None :
            obj['Vrf'] = Vrf

        if Enable != None :
            obj['Enable'] = True if Enable else False

        reqUrl =  self.cfgUrlBase+'IsisGlobal'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateIsisGlobalById(self,
                              objectId,
                              Enable = None):
        obj =  {}
        if Enable !=  None:
            obj['Enable'] = Enable

        reqUrl =  self.cfgUrlBase+'IsisGlobal'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateIsisGlobal(self,
                              Vrf,
                              op,
                              path,
                              value,):
        obj =  {}
        obj['Vrf'] = Vrf
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'IsisGlobal'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getIsisGlobal(self,
                      Vrf):
        obj =  { 
                'Vrf' : Vrf,
                }
        reqUrl =  self.cfgUrlBase + 'IsisGlobal'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getIsisGlobalById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'IsisGlobal'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllIsisGlobals(self):
        return self.getObjects('IsisGlobal', self.cfgUrlBase)


    def getBGPv6RouteState(self,
                           CIDRLen,
                           Network):
        obj =  { 
                'CIDRLen' : int(CIDRLen),
                'Network' : Network,
                }
        reqUrl =  self.stateUrlBase + 'BGPv6Route'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getBGPv6RouteStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'BGPv6Route'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllBGPv6RouteStates(self):
        return self.getObjects('BGPv6Route', self.stateUrlBase)


    def getBGPv4RouteState(self,
                           CIDRLen,
                           Network):
        obj =  { 
                'CIDRLen' : int(CIDRLen),
                'Network' : Network,
                }
        reqUrl =  self.stateUrlBase + 'BGPv4Route'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getBGPv4RouteStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'BGPv4Route'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllBGPv4RouteStates(self):
        return self.getObjects('BGPv4Route', self.stateUrlBase)


    def getVrrpVridState(self,
                         VRID,
                         IfIndex):
        obj =  { 
                'VRID' : int(VRID),
                'IfIndex' : int(IfIndex),
                }
        reqUrl =  self.stateUrlBase + 'VrrpVrid'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getVrrpVridStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'VrrpVrid'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllVrrpVridStates(self):
        return self.getObjects('VrrpVrid', self.stateUrlBase)


    def getAsicGlobalPMState(self,
                             Resource,
                             ModuleId):
        obj =  { 
                'Resource' : Resource,
                'ModuleId' : int(ModuleId),
                }
        reqUrl =  self.stateUrlBase + 'AsicGlobalPM'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getAsicGlobalPMStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'AsicGlobalPM'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllAsicGlobalPMStates(self):
        return self.getObjects('AsicGlobalPM', self.stateUrlBase)


    def getFaultState(self,
                      EventId,
                      EventName,
                      SrcObjName,
                      OwnerName,
                      OwnerId):
        obj =  { 
                'EventId' : int(EventId),
                'EventName' : EventName,
                'SrcObjName' : SrcObjName,
                'OwnerName' : OwnerName,
                'OwnerId' : int(OwnerId),
                }
        reqUrl =  self.stateUrlBase + 'Fault'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getFaultStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'Fault'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllFaultStates(self):
        return self.getObjects('Fault', self.stateUrlBase)


    """
    .. automethod :: createBGPv4Aggregate(self,
        :param string IpPrefix : IP Prefix in CIDR format to match IP Prefix in CIDR format to match
        :param bool SendSummaryOnly : Send summary route only when aggregating routes Send summary route only when aggregating routes
        :param bool GenerateASSet : Generate AS set when aggregating routes Generate AS set when aggregating routes

	"""
    def createBGPv4Aggregate(self,
                             IpPrefix,
                             SendSummaryOnly=False,
                             GenerateASSet=False):
        obj =  { 
                'IpPrefix' : IpPrefix,
                'SendSummaryOnly' : True if SendSummaryOnly else False,
                'GenerateASSet' : True if GenerateASSet else False,
                }
        reqUrl =  self.cfgUrlBase+'BGPv4Aggregate'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteBGPv4Aggregate(self,
                             IpPrefix):
        obj =  { 
                'IpPrefix' : IpPrefix,
                }
        reqUrl =  self.cfgUrlBase+'BGPv4Aggregate'
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteBGPv4AggregateById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'BGPv4Aggregate'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        else:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        return r

    def updateBGPv4Aggregate(self,
                             IpPrefix,
                             SendSummaryOnly = None,
                             GenerateASSet = None):
        obj =  {}
        if IpPrefix != None :
            obj['IpPrefix'] = IpPrefix

        if SendSummaryOnly != None :
            obj['SendSummaryOnly'] = True if SendSummaryOnly else False

        if GenerateASSet != None :
            obj['GenerateASSet'] = True if GenerateASSet else False

        reqUrl =  self.cfgUrlBase+'BGPv4Aggregate'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateBGPv4AggregateById(self,
                                  objectId,
                                  SendSummaryOnly = None,
                                  GenerateASSet = None):
        obj =  {}
        if SendSummaryOnly !=  None:
            obj['SendSummaryOnly'] = SendSummaryOnly

        if GenerateASSet !=  None:
            obj['GenerateASSet'] = GenerateASSet

        reqUrl =  self.cfgUrlBase+'BGPv4Aggregate'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateBGPv4Aggregate(self,
                                  IpPrefix,
                                  op,
                                  path,
                                  value,):
        obj =  {}
        obj['IpPrefix'] = IpPrefix
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'BGPv4Aggregate'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getBGPv4Aggregate(self,
                          IpPrefix):
        obj =  { 
                'IpPrefix' : IpPrefix,
                }
        reqUrl =  self.cfgUrlBase + 'BGPv4Aggregate'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getBGPv4AggregateById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'BGPv4Aggregate'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllBGPv4Aggregates(self):
        return self.getObjects('BGPv4Aggregate', self.cfgUrlBase)


    """
    .. automethod :: createBGPPolicyDefinition(self,
        :param string Name : Name of the BGP policy definition Name of the BGP policy definition
        :param int32 Precedence : Precedence of the policy definition Precedence of the policy definition
        :param string MatchType : Match type for policy definition Match type for policy definition
        :param BGPPolicyDefinitionStmtPrecedence StatementList : Precedence of statements in the policy Precedence of statements in the policy

	"""
    def createBGPPolicyDefinition(self,
                                  Name,
                                  Precedence,
                                  MatchType,
                                  StatementList):
        obj =  { 
                'Name' : Name,
                'Precedence' : int(Precedence),
                'MatchType' : MatchType,
                'StatementList' : StatementList,
                }
        reqUrl =  self.cfgUrlBase+'BGPPolicyDefinition'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteBGPPolicyDefinition(self,
                                  Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.cfgUrlBase+'BGPPolicyDefinition'
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deleteBGPPolicyDefinitionById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'BGPPolicyDefinition'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        else:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        return r

    def updateBGPPolicyDefinition(self,
                                  Name,
                                  Precedence = None,
                                  MatchType = None,
                                  StatementList = None):
        obj =  {}
        if Name != None :
            obj['Name'] = Name

        if Precedence != None :
            obj['Precedence'] = int(Precedence)

        if MatchType != None :
            obj['MatchType'] = MatchType

        if StatementList != None :
            obj['StatementList'] = StatementList

        reqUrl =  self.cfgUrlBase+'BGPPolicyDefinition'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updateBGPPolicyDefinitionById(self,
                                       objectId,
                                       Precedence = None,
                                       MatchType = None,
                                       StatementList = None):
        obj =  {}
        if Precedence !=  None:
            obj['Precedence'] = Precedence

        if MatchType !=  None:
            obj['MatchType'] = MatchType

        if StatementList !=  None:
            obj['StatementList'] = StatementList

        reqUrl =  self.cfgUrlBase+'BGPPolicyDefinition'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdateBGPPolicyDefinition(self,
                                       Name,
                                       op,
                                       path,
                                       value,):
        obj =  {}
        obj['Name'] = Name
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'BGPPolicyDefinition'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getBGPPolicyDefinition(self,
                               Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.cfgUrlBase + 'BGPPolicyDefinition'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getBGPPolicyDefinitionById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'BGPPolicyDefinition'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllBGPPolicyDefinitions(self):
        return self.getObjects('BGPPolicyDefinition', self.cfgUrlBase)


    """
    .. automethod :: createPolicyCondition(self,
        :param string Name : PolicyConditionName PolicyConditionName
        :param string ConditionType : Specifies the match criterion this condition defines Specifies the match criterion this condition defines
        :param string Protocol : Protocol to match on if the ConditionType is set to MatchProtocol Protocol to match on if the ConditionType is set to MatchProtocol
        :param string IpPrefix : Used in conjunction with MaskLengthRange to specify the IP Prefix to match on when the ConditionType is MatchDstIpPrefix/MatchSrcIpPrefix. Used in conjunction with MaskLengthRange to specify the IP Prefix to match on when the ConditionType is MatchDstIpPrefix/MatchSrcIpPrefix.
        :param string MaskLengthRange : Used in conjuction with IpPrefix to specify specify the IP Prefix to match on when the ConditionType is MatchDstIpPrefix/MatchSrcIpPrefix. Used in conjuction with IpPrefix to specify specify the IP Prefix to match on when the ConditionType is MatchDstIpPrefix/MatchSrcIpPrefix.
        :param string PrefixSet : Name of a pre-defined prefix set to be used as a condition qualifier. Name of a pre-defined prefix set to be used as a condition qualifier.

	"""
    def createPolicyCondition(self,
                              Name,
                              ConditionType,
                              Protocol,
                              IpPrefix,
                              MaskLengthRange,
                              PrefixSet=''):
        obj =  { 
                'Name' : Name,
                'ConditionType' : ConditionType,
                'Protocol' : Protocol,
                'IpPrefix' : IpPrefix,
                'MaskLengthRange' : MaskLengthRange,
                'PrefixSet' : PrefixSet,
                }
        reqUrl =  self.cfgUrlBase+'PolicyCondition'
        if self.authenticate == True:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.post(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deletePolicyCondition(self,
                              Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.cfgUrlBase+'PolicyCondition'
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.delete(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def deletePolicyConditionById(self, objectId ):
        reqUrl =  self.cfgUrlBase+'PolicyCondition'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        else:
                r = requests.delete(reqUrl, data=None, headers=headers,timeout=self.timeout) 
        return r

    def updatePolicyCondition(self,
                              Name,
                              ConditionType = None,
                              Protocol = None,
                              IpPrefix = None,
                              MaskLengthRange = None,
                              PrefixSet = None):
        obj =  {}
        if Name != None :
            obj['Name'] = Name

        if ConditionType != None :
            obj['ConditionType'] = ConditionType

        if Protocol != None :
            obj['Protocol'] = Protocol

        if IpPrefix != None :
            obj['IpPrefix'] = IpPrefix

        if MaskLengthRange != None :
            obj['MaskLengthRange'] = MaskLengthRange

        if PrefixSet != None :
            obj['PrefixSet'] = PrefixSet

        reqUrl =  self.cfgUrlBase+'PolicyCondition'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updatePolicyConditionById(self,
                                   objectId,
                                   ConditionType = None,
                                   Protocol = None,
                                   IpPrefix = None,
                                   MaskLengthRange = None,
                                   PrefixSet = None):
        obj =  {}
        if ConditionType !=  None:
            obj['ConditionType'] = ConditionType

        if Protocol !=  None:
            obj['Protocol'] = Protocol

        if IpPrefix !=  None:
            obj['IpPrefix'] = IpPrefix

        if MaskLengthRange !=  None:
            obj['MaskLengthRange'] = MaskLengthRange

        if PrefixSet !=  None:
            obj['PrefixSet'] = PrefixSet

        reqUrl =  self.cfgUrlBase+'PolicyCondition'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdatePolicyCondition(self,
                                   Name,
                                   op,
                                   path,
                                   value,):
        obj =  {}
        obj['Name'] = Name
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'PolicyCondition'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getPolicyCondition(self,
                           Name):
        obj =  { 
                'Name' : Name,
                }
        reqUrl =  self.cfgUrlBase + 'PolicyCondition'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getPolicyConditionById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'PolicyCondition'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllPolicyConditions(self):
        return self.getObjects('PolicyCondition', self.cfgUrlBase)


    def updatePort(self,
                   IntfRef,
                   IfIndex = None,
                   PhyIntfType = None,
                   MacAddr = None,
                   Speed = None,
                   MediaType = None,
                   Mtu = None,
                   BreakOutMode = None,
                   PRBSRxEnable = None,
                   Description = None,
                   PRBSPolynomial = None,
                   Duplex = None,
                   LoopbackMode = None,
                   EnableFEC = None,
                   AdminState = None,
                   Autoneg = None,
                   PRBSTxEnable = None):
        obj =  {}
        if IntfRef != None :
            obj['IntfRef'] = IntfRef

        if IfIndex != None :
            obj['IfIndex'] = int(IfIndex)

        if PhyIntfType != None :
            obj['PhyIntfType'] = PhyIntfType

        if MacAddr != None :
            obj['MacAddr'] = MacAddr

        if Speed != None :
            obj['Speed'] = int(Speed)

        if MediaType != None :
            obj['MediaType'] = MediaType

        if Mtu != None :
            obj['Mtu'] = int(Mtu)

        if BreakOutMode != None :
            obj['BreakOutMode'] = BreakOutMode

        if PRBSRxEnable != None :
            obj['PRBSRxEnable'] = True if PRBSRxEnable else False

        if Description != None :
            obj['Description'] = Description

        if PRBSPolynomial != None :
            obj['PRBSPolynomial'] = PRBSPolynomial

        if Duplex != None :
            obj['Duplex'] = Duplex

        if LoopbackMode != None :
            obj['LoopbackMode'] = LoopbackMode

        if EnableFEC != None :
            obj['EnableFEC'] = True if EnableFEC else False

        if AdminState != None :
            obj['AdminState'] = AdminState

        if Autoneg != None :
            obj['Autoneg'] = Autoneg

        if PRBSTxEnable != None :
            obj['PRBSTxEnable'] = True if PRBSTxEnable else False

        reqUrl =  self.cfgUrlBase+'Port'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def updatePortById(self,
                        objectId,
                        IfIndex = None,
                        PhyIntfType = None,
                        MacAddr = None,
                        Speed = None,
                        MediaType = None,
                        Mtu = None,
                        BreakOutMode = None,
                        PRBSRxEnable = None,
                        Description = None,
                        PRBSPolynomial = None,
                        Duplex = None,
                        LoopbackMode = None,
                        EnableFEC = None,
                        AdminState = None,
                        Autoneg = None,
                        PRBSTxEnable = None):
        obj =  {}
        if IfIndex !=  None:
            obj['IfIndex'] = IfIndex

        if PhyIntfType !=  None:
            obj['PhyIntfType'] = PhyIntfType

        if MacAddr !=  None:
            obj['MacAddr'] = MacAddr

        if Speed !=  None:
            obj['Speed'] = Speed

        if MediaType !=  None:
            obj['MediaType'] = MediaType

        if Mtu !=  None:
            obj['Mtu'] = Mtu

        if BreakOutMode !=  None:
            obj['BreakOutMode'] = BreakOutMode

        if PRBSRxEnable !=  None:
            obj['PRBSRxEnable'] = PRBSRxEnable

        if Description !=  None:
            obj['Description'] = Description

        if PRBSPolynomial !=  None:
            obj['PRBSPolynomial'] = PRBSPolynomial

        if Duplex !=  None:
            obj['Duplex'] = Duplex

        if LoopbackMode !=  None:
            obj['LoopbackMode'] = LoopbackMode

        if EnableFEC !=  None:
            obj['EnableFEC'] = EnableFEC

        if AdminState !=  None:
            obj['AdminState'] = AdminState

        if Autoneg !=  None:
            obj['Autoneg'] = Autoneg

        if PRBSTxEnable !=  None:
            obj['PRBSTxEnable'] = PRBSTxEnable

        reqUrl =  self.cfgUrlBase+'Port'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=headers,timeout=self.timeout) 
        return r

    def patchUpdatePort(self,
                        IntfRef,
                        op,
                        path,
                        value,):
        obj =  {}
        obj['IntfRef'] = IntfRef
        obj['patch']=[{'op':op,'path':path,'value':value}]
        reqUrl =  self.cfgUrlBase+'Port'
        if self.authenticate == True:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.patch(reqUrl, data=json.dumps(obj), headers=patchheaders, timeout=self.timeout) 
        return r

    def getPort(self,
                IntfRef):
        obj =  { 
                'IntfRef' : IntfRef,
                }
        reqUrl =  self.cfgUrlBase + 'Port'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getPortById(self, objectId ):
        reqUrl =  self.cfgUrlBase + 'Port'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllPorts(self):
        return self.getObjects('Port', self.cfgUrlBase)


    def getOspfIfEntryState(self,
                            IfIpAddress,
                            AddressLessIf):
        obj =  { 
                'IfIpAddress' : IfIpAddress,
                'AddressLessIf' : int(AddressLessIf),
                }
        reqUrl =  self.stateUrlBase + 'OspfIfEntry'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getOspfIfEntryStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'OspfIfEntry'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllOspfIfEntryStates(self):
        return self.getObjects('OspfIfEntry', self.stateUrlBase)


    def getRIBEventState(self,
                         Index):
        obj =  { 
                'Index' : int(Index),
                }
        reqUrl =  self.stateUrlBase + 'RIBEvent'
        if self.authenticate == True:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=json.dumps(obj), headers=headers, timeout=self.timeout) 
        return r

    def getRIBEventStateById(self, objectId ):
        reqUrl =  self.stateUrlBase + 'RIBEvent'+"/%s"%(objectId)
        if self.authenticate == True:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout, auth=(self.user, self.passwd), verify=False) 
        else:
                r = requests.get(reqUrl, data=None, headers=headers, timeout=self.timeout) 
        return r

    def getAllRIBEventStates(self):
        return self.getObjects('RIBEvent', self.stateUrlBase)

