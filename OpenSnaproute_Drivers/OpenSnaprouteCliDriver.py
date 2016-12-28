#!/usr/bin/env python
'''
Created on 20-Nov-2016

Author : Terralogic team

OpenSnaprouteCliDriver is the basic driver which will handle the OpenSnaproute functions.

'''
import xlrd
import io
import sys
import os
import simplejson as json
sys.path.append(os.path.abspath('../../py'))
from flexswitchV2 import FlexSwitch
from flexprintV2 import FlexSwitchShow

import xmldict
import pexpect
import re
import os
import ast
import time
import testfail 
import string
import sys
import logger as log
from robot.libraries.BuiltIn import BuiltIn
global step


'''
[API Documentation] 
#ID : OpenSnaproute_api_001
#Name : CHECKPOINT()
#API Feature details :
#Print the Checkpoint
'''
def CHECKPOINT(string,device_id=''):
    log.step("*** "+string)


'''
[API Documentation]
#ID : OpenSnaproute_api_002
#Name :  Deviceparser API
#API Feature details :
#1  "Deviceparser" API Parses the "TestCase.params" file
#2  Returns the device name                                     
'''

def Device_parser(device="") :
    xml = open('OpenSnaproute.params').read()
    parsedInfo = xmldict.xml_to_dict(xml)
    if device!="":
        device=str(device)
        device_name=parsedInfo['TestCase']['Device'][device]
        return device_name
    else:
        device_name=parsedInfo['TestCase']['Device']
        return device_name


'''
[API Documentation] 
#ID : OpenSnaproute_api_003
#Name : Get_deviceInfo API
#API Feature details :
#1  "Get_deviceInfo" API opens the "device.params" file
#2  Returns the information of the particular device in a list
'''

def Get_deviceInfo(device):
    deviceparam=open('device.params').read()
    deviceInfo=deviceparam.splitlines() 
    for value in deviceInfo:
        pattern=device
        match=re.search(pattern,value)
        if match:          
            deviceList=value.split(',')
            return deviceList



'''
[API Documentation]
#ID : OpenSnaproute_api_04
#Name :assignip
#API Feature details :
"Device_parser" API will assign the IPv4 address to the routers using SDK function
''' 

def assignip(mode,fab_devices,csw_devices,asw_devices,subnet,fab=[],csw=[],asw=[],interface_dict={},interface_ip_dict={}) :
    list1=[]
    c=0
    var=0
    if mode == "no" :
        for i in range(0,int(fab_devices)) :
            list1.append(fab[i])
        for i in range(0,int(csw_devices)) :
            list1.append(csw[i])
        for i in range(0,int(asw_devices)) :
            list1.append(asw[i])
        for i in range(len(list1)):
            need_count=0
            received_count=0
            device = list1[i]
            device_name=Device_parser(device)
            log.info("login to "+device_name+" and configure IP address")
            device_Info = Get_deviceInfo(device_name)
            ip_address = device_Info[1]
            swtch = FlexSwitch (ip_address, 8080)  # Instantiate object to talk to flexSwitch
            for j in range(len(list1)):
                if device != list1[j] :
                    device_ip=device+"_"+list1[j]+"_interface_ip "
                    device_interface=device+"_"+list1[j]+"_eth"    
                    if device_ip in interface_ip_dict.keys() and device_interface in interface_dict.keys():
                        need_count=need_count+1
                        result = swtch.createIPv4Intf(interface_dict[device_interface],interface_ip_dict[device_ip]+subnet,AdminState='UP')
                        if result.ok or result.status_code == 500:
                            received_count=received_count+1
                        else:
                            log.failure ("Failed to Configure IP "+interface_dict[device_interface]+"on "+device_name) 
            if need_count == received_count:
                log.success("IP configured successfully on "+device_name)
                c= c+1 
    if mode == "yes":
        for i in fab:
            list1.append(i)
        for i in csw:
            list1.append(i)
        for i in asw:
            list1.append(i)
        for i in range(len(list1)):
            need_count=0
            received_count=0
            device = list1[i]
            device_name=Device_parser(device)
            log.info("login to "+device_name+" and configure IP address")
            device_Info = Get_deviceInfo(device_name)
            ip_address = device_Info[1]
            swtch = FlexSwitch (ip_address, 8080)  # Instantiate object to talk to flexSwitch
            for j in range(len(list1)):
                if device != list1[j] :
                    device_ip=device+"_"+list1[j]+"_interface_ip "
                    device_interface=device+"_"+list1[j]+"_eth"    
                    if device_ip in interface_ip_dict.keys() and device_interface in interface_dict.keys():
                        need_count=need_count+1
                        result=swtch.createIPv4Intf(interface_dict[device_interface],interface_ip_dict[device_ip]+subnet,AdminState='UP')
                        if result.ok or result.status_code == 500:
                            received_count=received_count+1
                        else:
                            log.failure ("Failed to Configure IP "+interface_dict[device_interface]+"on "+device_name)

            if need_count == received_count:
               log.success("IP configured successfully on "+device_name)
               c= c+1
    if c == len(list1):
        log.success("IP is configured successfully")
        return True
    else:
        log.failure("IP is not configured")
        return False



'''
[API Documentation]
#ID : OpenSnaproute_api_05
#Name :removeip
#API Feature details :
"Device_parser" API will delete the interfaces and IPv4 address from the routers using SDK function
''' 
                
def removeip(mode,fab_devices,csw_devices,asw_devices,subnet,fab=[],csw=[],asw=[],interface_dict={},interface_ip_dict={}) :
    list1=[]
    c=0
    if mode == "no" :
        for i in range(0,int(fab_devices)) :
            list1.append(fab[i])
        for i in range(0,int(csw_devices)) :
            list1.append(csw[i])
        for i in range(0,int(asw_devices)) :
            list1.append(asw[i])
        for i in range(len(list1)):
            need_count=0
            received_count=0
            device = list1[i]
            device_name=Device_parser(device)
            log.info("login to "+device_name+" and remove IP address")
            device_Info = Get_deviceInfo(device_name)
            ip_address = device_Info[1]
            swtch = FlexSwitch (ip_address, 8080)  # Instantiate object to talk to flexSwitch
            for j in range(len(list1)):
                if device != list1[j] :
                    device_ip=device+"_"+list1[j]+"_interface_ip "
                    device_interface=device+"_"+list1[j]+"_eth"    
                    if device_ip in interface_ip_dict.keys() and device_interface in interface_dict.keys():
                        need_count=need_count+1
                        delete_IPv4Intf=swtch.deleteIPv4Intf(interface_dict[device_interface])
                        if delete_IPv4Intf.status_code == 410:
                            received_count=received_count+1
                        else:
                            log.failure( "Failed to delete IP "+interface_dict[device_interface]+"on "+device_name)
            if need_count == received_count :
                log.success("IP removed successfully on "+device_name)
                c= c+1     
    if mode == "yes":
        for i in fab:
            list1.append(i)
        for i in csw:
            list1.append(i)
        for i in asw:
            list1.append(i)
        for i in range(len(list1)):
            need_count=0
            received_count=0
            device = list1[i]
            device_name=Device_parser(device)
            device_Info = Get_deviceInfo(device_name)
            log.info("login to "+device_name+" and remove IP address")
            ip_address = device_Info[1]
            swtch = FlexSwitch (ip_address, 8080)  # Instantiate object to talk to flexSwitch
            for j in range(len(list1)):
                if device != list1[j] :
                    device_ip=device+"_"+list1[j]+"_interface_ip "
                    device_interface=device+"_"+list1[j]+"_eth"    
                    if device_ip in interface_ip_dict.keys() and device_interface in interface_dict.keys():
                        need_count=need_count+1
                        delete_IPv4Intf=swtch.deleteIPv4Intf(interface_dict[device_interface])
                        if delete_IPv4Intf.status_code == 410:
                            received_count=received_count+1
                        else:
                            log.failure( "Failed to delete IP "+interface_dict[device_interface]+"on "+device_name)
            if need_count == received_count :
                log.success("IP removed successfully on "+device_name)
                c= c+1
    if c == len(list1):
        log.success("IP removed successfully")
        return True
    else:
        log.failure("IP not removed ")
        return False




'''
[API Documentation]
#ID : OpenSnaproute_api_06
#Name :assignbgp
#API Feature details :
"Device_parser" API will assign the BGP IPv4 address to the routers using SDK function
''' 

def assignbgp(mode,fab_devices,csw_devices,asw_devices,fab=[],csw=[],asw=[],interface_ip_dict={},asnum={},router_id={}) :
    list1=[]
    neighbor=[]
    peer_as=[]
    c=0
    if mode == "no" :
        for i in range(0,int(fab_devices)) :
            list1.append(fab[i])
        for i in range(0,int(csw_devices)) :
            list1.append(csw[i])
        for i in range(0,int(asw_devices)) :
            list1.append(asw[i])
        for i in range(len(list1)):
            need_count=0
            received_count=0
            neighbor=[]
            peer_as=[]
            device = list1[i]
            device_name=Device_parser(device)
            device_Info = Get_deviceInfo(device_name)
            log.info("log-in to "+device_name+" and loading BGP configuration")
            ip_address = device_Info[1]
            swtch = FlexSwitch (ip_address, 8080)  # Instantiate object to talk to flexSwitch
            local=asnum[device]
            Routerid=router_id[device]
            swtch.updateBGPGlobal("default",ASNum=local,RouterId=Routerid)
            for j in range(len(list1)):
                peer=asnum[list1[j]]
                if device != list1[j] :
                    device_ip=list1[j]+"_"+device+"_interface_ip " 
                    if device_ip in interface_ip_dict.keys() :
                        need_count=need_count+1
                        result=swtch.createBGPv4Neighbor("",interface_ip_dict[device_ip],PeerAS=peer,LocalAS=local)
                        if result.ok or result.status_code == 500:
                            received_count=received_count+1
                        else:
                            log.failure ("Failed to Configure BGP neighbor "+interface_ip_dict[device_ip]+"on "+device_name)
            if need_count == received_count:
                log.success("BGP is configured successfully on "+device_name)
                c=c+1
    if mode == "yes":
        for i in fab:
            list1.append(i)
        for i in csw:
            list1.append(i)
        for i in asw:
            list1.append(i)
        for i in range(len(list1)):
            need_count=0
            received_count=0
            device = list1[i]
            device_name=Device_parser(device)
            device_Info = Get_deviceInfo(device_name)
            log.info("log-in to "+device_name+" and loading BGP configuration")
            ip_address = device_Info[1]
            swtch = FlexSwitch (ip_address, 8080)  # Instantiate object to talk to flexSwitch
            local=asnum[device]      
            Routerid=router_id[device]
            swtch.updateBGPGlobal("default",ASNum=local,RouterId=Routerid)
            for j in range(len(list1)):
                peer=asnum[list1[j]]
                if device != list1[j] :
                    device_ip=list1[j]+"_"+device+"_interface_ip " 
                    if device_ip in interface_ip_dict.keys() :
                      need_count=need_count+1
                      result=swtch.createBGPv4Neighbor("",interface_ip_dict[device_ip],PeerAS=peer,LocalAS=local)
                      if result.ok or result.status_code == 500:
                            received_count=received_count+1
                      else:
                            log.failure ("Failed to Configure BGP neighbor "+interface_ip_dict[device_ip]+"on "+device_name)
            if need_count == received_count:
                log.success("BGP is configured successfully on "+device_name)
                c=c+1
    if c == len(list1):
        log.success("BGP is configured successfully")
        return True
    else:
        log.failure("BGP is not configured")
        return False                            

                                 
'''
[API Documentation]
#ID : OpenSnaproute_api_07
#Name :removebgp
#API Feature details :
"Device_parser" API will remove the bgp IPv4 neighbor address from the routers using SDK function
''' 
               
def removebgp(mode,fab_devices,csw_devices,asw_devices,fab=[],csw=[],asw=[],interface_ip_dict={},asnum={},router_id={}) :
    list1=[]
    neighbor=[]
    peer_as=[]
    c=0
    if mode == "no" :
        for i in range(0,int(fab_devices)) :
            list1.append(fab[i])
        for i in range(0,int(csw_devices)) :
            list1.append(csw[i])
        for i in range(0,int(asw_devices)) :
            list1.append(asw[i])
        for i in range(len(list1)):
            need_count=0
            received_count=0
            device = list1[i]
            device_name=Device_parser(device)
            device_Info = Get_deviceInfo(device_name)
            log.info("log-in to "+device_name+" and removing BGP configuration")
            ip_address = device_Info[1]
            swtch = FlexSwitch (ip_address, 8080)  # Instantiate object to talk to flexSwitch
            local=asnum[device]
            Routerid=router_id[device]
            for j in range(len(list1)):
                peer=asnum[list1[j]]
                if device != list1[j] :
                    device_ip=list1[j]+"_"+device+"_interface_ip " 
                    if device_ip in interface_ip_dict.keys() :
                        need_count=need_count+1
                        removeBGPv4_Neighbor=swtch.deleteBGPv4Neighbor("",interface_ip_dict[device_ip])

                        if removeBGPv4_Neighbor.status_code == 410:
                            received_count=received_count+1
                        else:
                            log.failure( "Failed to remove BGP neighbor "+interface_ip_dict[device_ip]+"on "+device_name)
            if need_count == received_count:
                c=c+1
                log.success("BGP is removed successfully on "+device_name)
    if mode == "yes":
        for i in fab:
            list1.append(i)
        for i in csw:
            list1.append(i)
        for i in asw:
            list1.append(i)
        for i in range(len(list1)):
            need_count=0
            received_count=0
            device = list1[i]
            device_name=Device_parser(device)
            device_Info = Get_deviceInfo(device_name)
            ip_address = device_Info[1]
            log.info("log-in to "+device_name+" and removing BGP configuration")
            swtch = FlexSwitch (ip_address, 8080)  # Instantiate object to talk to flexSwitch
            local=asnum[device]      
            Routerid=router_id[device]
            for j in range(len(list1)):
                peer=asnum[list1[j]]
                if device != list1[j] :
                    device_ip=list1[j]+"_"+device+"_interface_ip " 
                    if device_ip in interface_ip_dict.keys() :
                      need_count=need_count+1
                      removeBGPv4_Neighbor=swtch.deleteBGPv4Neighbor("",interface_ip_dict[device_ip])
                      if removeBGPv4_Neighbor.status_code == 410:
                            received_count=received_count+1
                      else:
                            log.failure( "Failed to remove BGP neighbor "+interface_ip_dict[device_ip]+"on "+device_name)
            if need_count == received_count:
                c=c+1
                log.success("BGP is removed successfully on "+device_name)
    if c == len(list1):
        log.success("BGP is removed successfully")
        return True
    else:
        log.failure("BGP is not removed ")
        return False                    



'''
[API Documentation] 
#ID : OpenSnaproute_api_08
#Name : createPolicyCondition_name()
#API Feature details :
#configuring Policy condition
'''           
def createPolicyCondition_name(mode,fab_devices,csw_devices,asw_devices,fab=[],csw=[],asw=[],Condition_name='',ConditionType='',Protocol='',IpPrefix='',MaskLengthRange='',PrefixSet='') :
    list1=[]
    if mode == "no" :
        for i in range(0,int(fab_devices)) :
            list1.append(fab[i])
        for i in range(0,int(csw_devices)) :
            list1.append(csw[i])
        for i in range(0,int(asw_devices)) :
            list1.append(asw[i])
    if mode == "yes":
        for i in fab:
            list1.append(i)
        for i in csw:
            list1.append(i)
        for i in asw:
            list1.append(i)
    count =0    
    for i in range(len(list1)):
            port = []
            device = list1[i]
            device_name=Device_parser(device)
            log.info("Loading into "+device_name)
            device_Info = Get_deviceInfo(device_name)
            ip_address = device_Info[1]
            swtch = FlexSwitch (ip_address, 8080)
            swtch1 = FlexSwitchShow (ip_address, 8080)
            result=swtch.createPolicyCondition(Condition_name,ConditionType,Protocol,IpPrefix,MaskLengthRange,PrefixSet)
            #result=swtch1.printPolicyConditionStates()
            #log.details(result)
            if result.ok or result.status_code == 500:
                log.success("Policy Condition is created and verified on "+device_name)
                count =count+1
            else :
                log.failure("Policy Condition is not created properly on "+device_name)
    if count == len(list1):
        log.success("Policy Condition is created ")
        return True
    else:
        log.failure(" Policy Condition is not created ")
        return False
'''
[API Documentation] 
#ID : OpenSnaproute_api_09
#Name : createPolicyStatement()
#API Feature details :
#configuring Policy statement
'''            
def createPolicyStatement(mode,fab_devices,csw_devices,asw_devices,fab=[],csw=[],asw=[],stmt_name='',Condition_name='',action='',matchconditions='') :
    list1=[]
    count =0
    if mode == "no" :
        for i in range(0,int(fab_devices)) :
            list1.append(fab[i])
        for i in range(0,int(csw_devices)) :
            list1.append(csw[i])
        for i in range(0,int(asw_devices)) :
            list1.append(asw[i])
                        #print json.dumps(create_IPv4Intf)
    if mode == "yes":
        for i in fab:
            list1.append(i)
        for i in csw:
            list1.append(i)
        for i in asw:
            list1.append(i)
    cond_name=[] 
    cond_name.append(Condition_name)  
    for i in range(len(list1)):
            port = []
            device = list1[i]
            device_name=Device_parser(device)
            log.info("Loading into "+device_name)
            device_Info = Get_deviceInfo(device_name)
            ip_address = device_Info[1]
            swtch = FlexSwitch (ip_address, 8080)
            result = swtch.createPolicyStmt(Name=stmt_name,Conditions=cond_name, Action=action,MatchConditions=matchconditions)
            if result.ok or result.status_code == 500:
                log.success("Policy statement is created and verified on "+device_name)
                count =count+1
            else :
                log.failure("Policy statement is not created properly on "+device_name)
    if count == len(list1):
        log.success("Policy statement is created ")
        return True
    else:
        log.failure(" Policy statement is not created ")
        return False
'''
[API Documentation] 
#ID : OpenSnaproute_api_010
#Name :create_Policy_Definitions()
#API Feature details :
#configuring Policy Definition
'''            
def create_Policy_Definitions(mode,fab_devices,csw_devices,asw_devices,fab=[],csw=[],asw=[],stmt_name="",Pol_def_name="",priority="",matchtype="",policytype="") :
    list1=[]
    if mode == "no" :
        for i in range(0,int(fab_devices)) :
            list1.append(fab[i])
        for i in range(0,int(csw_devices)) :
            list1.append(csw[i])
        for i in range(0,int(asw_devices)) :
            list1.append(asw[i])
    if mode == "yes":
        for i in fab:
            list1.append(i)
        for i in csw:
            list1.append(i)
        for i in asw:
            list1.append(i)
    count =0
    stmt_list=[{"Priority": int(priority), "Statement": str(stmt_name)}]
    for i in range(len(list1)):
            port = []
            device = list1[i]
            device_name=Device_parser(device)
            log.info("Loading into "+device_name)
            device_Info = Get_deviceInfo(device_name)
            ip_address = device_Info[1]
            swtch = FlexSwitch (ip_address, 8080)
            result = swtch.createPolicyDefinition(str(Pol_def_name),int(priority),stmt_list , MatchType=str(matchtype),PolicyType=policytype)
            if result.ok or result.status_code == 500:
                log.success("Policy Definitions is created and verified on "+device_name)
                count =count+1
            else :
                log.failure("Policy Definitions is not created properly on "+device_name)
    if count == len(list1):
        log.success("Policy Definitions is created ")
        return True
    else:
        log.failure(" Policy Definitions is not created ")
        return False

'''
[API Documentation] 
#ID : OpenSnaproute_api_011
#Name : flap_state()
#API Feature details :
#To make interface state UP and Down
'''                 
                   
def flap_state(mode,fab_devices,csw_devices,asw_devices,fab=[],csw=[],asw=[],interface_dict={}) :
    list1=[]
    if mode == "no" :
        for i in range(0,int(fab_devices)) :
            list1.append(fab[i])
        for i in range(0,int(csw_devices)) :
            list1.append(csw[i])
        for i in range(0,int(asw_devices)) :
            list1.append(asw[i])
                        #print json.dumps(create_IPv4Intf)
    if mode == "yes":
        for i in fab:
            list1.append(i)
        for i in csw:
            list1.append(i)
        for i in asw:
            list1.append(i)
    need_count=0
    received_count=0
    c=0    
    for i in range(len(list1)):
            device = list1[i]
            device_name=Device_parser(device)
            device_Info = Get_deviceInfo(device_name)
            ip_address = device_Info[1]
            swtch = FlexSwitch (ip_address, 8080)  # Instantiate object to talk to flexSwitch
            for j in range(len(list1)):
                if device != list1[j] :
                    device_interface=device+"_"+list1[j]+"_eth"    
                    if device_interface in interface_dict.keys():
                        need_count=need_count+1
                        result=swtch.updatePort(interface_dict[device_interface],AdminState='DOWN')
                        if result.ok or result.status_code == 500:
                            log.info("Setting "+interface_dict[device_interface]+" DOWN")
                            c=c+1
                        time.sleep(1)
                        
                        result=swtch.updatePort(interface_dict[device_interface],AdminState='UP')
                        if result.ok or result.status_code == 500:
                            log.info("Setting "+interface_dict[device_interface]+" UP")
                            received_count=received_count+1#print json.dumps(create_IPv4Intf)
    if need_count == received_count and need_count==c and c==received_count:
       log.success("flap state is done")
       return True
    else :
       log.failure("flap state is not done")
       return False   
'''
[API Documentation] 
#ID : OpenSnaproute_api_012
#Name : createBGPGlobal()
#API Feature details :
#create BGP global functionality
'''                    
def createBGPGlobal(mode,fab_devices,csw_devices,asw_devices,fab=[],csw=[],asw=[],asnum={},router_id={},redistribution='',pol_name=''):
    list1=[]
    c=0
    if mode == "no" :
        for i in range(0,int(fab_devices)) :
            list1.append(fab[i])
        for i in range(0,int(csw_devices)) :
            list1.append(csw[i])
        for i in range(0,int(asw_devices)) :
            list1.append(asw[i])
                        #print json.dumps(create_IPv4Intf)
    if mode == "yes":
        for i in fab:
            list1.append(i)
        for i in csw:
            list1.append(i)
        for i in asw:
            list1.append(i)
    redistribute=''
    if redistribution !='':
        redistribute=[{"Sources": redistribution, "Policy": pol_name}]
    for i in range(len(list1)):
            need_count=0
            b=0
            device = list1[i]
            device_name=Device_parser(device)
            device_Info = Get_deviceInfo(device_name)
            ip_address = device_Info[1]
            swtch = FlexSwitch (ip_address, 8080)  # Instantiate object to talk to flexSwitch
            local=asnum[device]      
            Routerid=router_id[device]
            log.info("log-in to "+device_name+" and configuring router")
            result=swtch.updateBGPGlobal("default",ASNum=local,RouterId=Routerid,Redistribution=redistribute)
            if result.ok or result.status_code == 500:
               c=c+1
               log.success("router is configured on "+device_name)
            else:
               log.failure ("Failed to Configure router on "+device_name) 
    if c==len(list1):
        log.success("router is configured")
        return True
    else:
        log.info ("Failed to Configure router on "+device_name) 
        return False

'''
[API Documentation] 
#ID : OpenSnaproute_api_013
#Name :neighbor_state_all()
#API Feature details :
#Check neighbor state in a devices
'''                 
def neighbor_state_all(state,mode,fab_devices,csw_devices,asw_devices,fab=[],csw=[],asw=[],interface_ip_dict={}):
    list1=[]
    if mode == "no" :
        for i in range(0,int(fab_devices)) :
            list1.append(fab[i])
        for i in range(0,int(csw_devices)) :
            list1.append(csw[i])
        for i in range(0,int(asw_devices)) :
            list1.append(asw[i])
    if mode == "yes":
        for i in fab:
            list1.append(i)
        for i in csw:
            list1.append(i)
        for i in asw:
            list1.append(i)
    device_count=0
    for i in list1:
        flag=0
        device=i;
    	device_name=Device_parser(device)
    	log.step('Checking for '+state+' in '+device_name)
    	log.info('Log-in into '+device_name+' to check for '+state+' state')
        device_name=Device_parser(device)
        device_Info = Get_deviceInfo(device_name)
        ip_address = device_Info[1]
        swtch = FlexSwitch (ip_address, 8080)
        Output = swtch.getAllBGPv4NeighborStates() 
        log.details(Output)
    	match_count=0
    	rec_count=0
    	dev_count=0
    	list2=[]
        flag=0
    	for eachline in Output:
                    for j in range(len(list1)):
                        if device != list1[j] :
                            dev_count = dev_count+1
                            device_ip=list1[j]+"_"+device+"_interface_ip "
                            if device_ip in interface_ip_dict.keys() :
                                if list1[j] not in list2:
                                    list2.append(list1[j])
                                ip_actual=interface_ip_dict[device_ip]
                                ip_actual="'"+ip_actual+"'"
                                if (ip_actual) in str(eachline) and "'SessionState': 6" in str(eachline):
                                        rec_count=rec_count+1
                                        flag=1
                                        break
        if rec_count == len(list2) and flag==1:
            log.success("Required "+state+" state is achieved in "+device_name)
            device_count=device_count+1
        else:
            log.failure("Required "+state+" state is not achieved on "+device_name)
    if device_count == len(list1):
        log.success("Neighborship is get "+state+" state on all devices")
        return True
    else:
        log.failure("Neighborship is not get "+state+" state on all devices")
        return False
'''
[API Documentation] 
#ID : OpenSnaproute_api_014
#Name :particular_device_neighbor_check()
#API Feature details :
#Check neighbor state in a particular device
'''   
def particular_device_neighbor_check(state,source_device,destination_device,interface_ip_dict={}):
    log.step('Checking for '+state+' in '+Device_parser(source_device))
    log.info('Log-in into '+Device_parser(source_device)+' to check for '+state+' state')
    device_name=Device_parser(source_device)
    log.step('Checking for '+state+' in '+device_name)
    log.info('Log-in into '+device_name+' to check for '+state+' state')
    device_name=Device_parser(source_device)
    device_Info = Get_deviceInfo(device_name)
    ip_address = device_Info[1]
    swtch = FlexSwitch (ip_address, 8080)
    Output = swtch.getAllBGPv4NeighborStates() 
    log.details(Output)
    flag=0
    device_ip=destination_device+"_"+source_device+"_interface_ip " 
    ip_actual=interface_ip_dict[device_ip]
    ip_actual="'"+ip_actual+"'"
    for eachline in Output:
               if state == 'Estab':
                   if (ip_actual) in str(eachline) and "'SessionState': 6" in str(eachline):
                       flag = 1
                       break
               if state != 'Estab':
                   if (ip_actual) in str(eachline) and "'SessionState': 6" not in str(eachline):
                        flag = 1
                        break
    if flag == 1:
        log.success("neighbor ip "+ip_actual+ "is in "+state+" state")
        return True
    else:
        log.failure("neighbor ip "+ip_actual+ "is not in "+state+" state")
        return False  
'''
[API Documentation] 
#ID : OpenSnaproute_api_015
#Name : trigger()
#API Feature details :
#Trigger Link failure
'''   
def trigger(device,ip,interface_ip_dict={},interface_dict={}):
            list1=[]
            device_name=Device_parser(device)
            device_Info = Get_deviceInfo(device_name)
            ip_address = device_Info[1]
            port = []
            flag = 1
            count =0
            log.info("trigger link failure is verifying on "+device_name+" for the address "+ip)
            swtch = FlexSwitch (ip_address, 8080)
            while(flag==1):
               result = bestpath(swtch,ip)
               log.details(result)
               output=str(result)
               pattern=r"[\{u'A-z:,\s*0-9./+\}-]*NextHopIntRef':\s*u'(\w+)[',\s*u'A-z:0-9]*Ip':\s*u'(\d+.\d+.\d+.\d+).*"
               match=re.match(pattern,str(result))
               if result:

                 if match:
                    add=match.group(1)
                    log.info("BestPath port : "+add) 
                    eth=match.group(1)
                    state(device,eth,state="DOWN")
                    time.sleep(5)
                    port.append(eth)
                    count = count+1
                    
            
               else :
                  flag = 0
                  log.info("No bestpath found")
                  log.info("bringing up all the shut down interfaces")
                  for i in range(0,len(port)):
                      state(device,port[i],state='UP')             

            if count > 1:
                log.success("Trigger Link Failure is verified")
                return True
            else :
                log.failure("No Best/alternate Path Found")
                return False
'''
[API Documentation] 
#ID : OpenSnaproute_api_016
#Name : bestpath()
#API Feature details :
#Find Best path
'''  
def bestpath(swtch,ip):
            result = swtch.getIPv4RouteState(ip)
            if result.ok:
               return result.json()
            else :
               return 0
'''
[API Documentation] 
#ID : OpenSnaproute_api_017
#Name :bestpath()
#API Feature details :
#create or remove loopback interface
'''  
def loopback(mode,device,loopback_name,ip,subnet):
  device_name=Device_parser(device)
  device_Info = Get_deviceInfo(device_name)
  ip_address = device_Info[1]
  if mode == 'config':
     log.info("Creating Logical address on  "+device_name)
     swtch = FlexSwitch (ip_address, 8080)
     result = swtch.createLogicalIntf(loopback_name)
     if result.ok or result.status_code == 500:
         result = swtch.createIPv4Intf(loopback_name,ip+subnet)
         if result.ok or result.status_code == 500:
             log.success("logical interface is created on  "+device_name)
             return True
         else:
             log.failure("logical interface is not created")
             return False
     else:
         log.failure("logical interface is not created")
         return False
  if mode == 'remove':
     log.info("Removing Logical address on  "+device_name)
     swtch = FlexSwitch (ip_address, 8080)
     result = swtch.deleteIPv4Intf(loopback_name)
     if result.status_code == 410:
         result = swtch.deleteLogicalIntf(loopback_name)
         if result.status_code == 410:
             log.success("logical interface is removed on  "+device_name)
             return True
         else:
             log.failure("logical interface is not created")
             return False
     else:
         log.failure("logical interface is not created")
         return False
'''
[API Documentation] 
#ID : OpenSnaproute_api_018
#Name : reset_bgp_neighbor()
#API Feature details :
#Reset/clear the BGP with IP address
'''  
def reset_bgp_neighbor(device,ip):

     device_name=Device_parser(device)
     device_Info = Get_deviceInfo(device_name)
     ip_address = device_Info[1]
     log.info("Reset/clear BGP process on  "+device_name)
     swtch = FlexSwitch (ip_address, 8080)
     result = swtch.executeResetBGPv4NeighborByIPAddr(ip)
     if result.ok:
         log.success("BGP process reseted on  "+device_name)
         return True
     else:
         log.failure("BGP Process no reseted")
         return False
'''
[API Documentation] 
#ID : OpenSnaproute_api_019
#Name : best_ip()
#API Feature details :
#gives a best path ip
'''  
def best_ip(device,ip,interface_ip_dict={},interface_dict={}):
            device_name=Device_parser(device)
            device_Info = Get_deviceInfo(device_name)
            ip_address = device_Info[1]
            port = []
            flag = 1
            count =0
            log.info("Checking for best path port on  "+device_name+" for the address "+ip)
            swtch = FlexSwitch (ip_address, 8080)    
            result = bestpath(swtch,ip)
            if result:
                pattern=r"[\{u'A-z:,\s*0-9./+\}-]*NextHopIntRef':\s*u'(\w+)[',\s*u'A-z:0-9]*Ip':\s*u'(\d+.\d+.\d+.\d+).*"
                match=re.match(pattern,str(result))
                if match :
                    log.success("best path "+match.group(2))
                    return True
            else :
                log.failure("no best path found")
                return False
            

'''
[API Documentation] 
#ID : OpenSnaproute_api_020
#Name : state
#API Feature details :
#To make interface state UP and Down
'''                 
def state(device,port,state=''):
            a=[]
            device_name=Device_parser(device)
            device_Info = Get_deviceInfo(device_name)
            ip_address = device_Info[1]
            swtch = FlexSwitch (ip_address, 8080)
            if state=="DOWN":
                        log.info("shutdown the interface "+port+" on "+device_name)
                        result=swtch.updatePort(port,AdminState='DOWN')
                        if result.ok or result.status_code == 500:
                            log.success("port "+port+" is down")
                            return True
                        else :
                            log.failure("Fail to set port "+port+" to down state")
                            return False
            if state=="UP": 
                   log.info("Making the interface "+port+" UP on "+device_name)
                   result=swtch.updatePort(port,AdminState='UP')   
                   if result.ok or result.status_code == 500:
                       log.success("port "+port+" is up")
                       return True
                   else :
                       log.failure("Fail to set port "+port+" to up state")
                       return False
                   

'''
[API Documentation]
#ID : ops_api_021
#Name :  Connect()
#API Feature details :
#1 "Connect" API Connects to the particular device.
'''

def Connect(device):
    device_name=Device_parser(device)
    device_Info=Get_deviceInfo(device_name)
    ip_address=device_Info[1]
    port = device_Info[2]
    user=device_Info[3]
    password=device_Info[4]
    refused="ssh: connect to host " +ip_address+ " port 22: Connection refused"
    connectionInfo = pexpect.spawn('ssh '+user+'@'+ip_address )
    expect = 7
    while expect == 7:
        expect =connectionInfo.expect( ["Are you sure you want to continue connecting","password:",pexpect.EOF,pexpect.TIMEOUT,refused,'>|#|\$',"Host key verification failed."],120 )  
        if expect == 0:  # Accept key, then expect either a password prompt or access
            connectionInfo.sendline( 'yes' )
            expect = 7  # Run the loop again
            continue
        if expect == 1:  # Password required  
            connectionInfo.sendline(password)
            connectionInfo.expect( '>|#|\$')
            if not connectionInfo.expect:
                log.failure('Password for '+device_name+' is incorrect')
                raise testfail.testFailed('Password for '+device_name+' is incorrect')
                break
        elif expect == 2:
            log.failure('End of File Encountered while Connecting '+device_name)
            raise testfail.testFailed('End of File Encountered while Connecting '+device_name)
            break
        elif expect == 3:  # timeout
            log.failure('Timeout of the session encountered while connecting')
            raise testfail.testFailed('Timeout of the session encountered')
            break
        elif expect == 4:
            log.failure('Connection to '+device_name+' refused')
            raise testfail.testFailed('Connection to '+device_name+' refused')
            break
        elif expect == 5:
            pass
        elif expect == 6:                   
            #cmd='ssh-keygen -R ['+ip_address+']:'+port
            cmd='ssh-keygen -f "/home/openswitch/.ssh/known_hosts" -R '+ip_address
            os.system(cmd)
            connectionInfo = pexpect.spawn('ssh -p '+port +' ' +user+'@'+ip_address,env={ "TERM": "xterm-mono" },maxread=50000 )
            expect = 7
            continue
    connectionInfo.sendline("")
    connectionInfo.expect( '>|#|\$' )
    return connectionInfo
    
    

'''
[API Documentation] 
#ID : OpenSnaproute_api_022
#Name : CASE()
#API Feature details :
#Print the CASE info
'''
def CASE(string,device_id=''):
    log.case("<<< "+string)




'''
[API Documentation]
#ID : ops_api_0023
#Name : delay(delay,message)
#API Feature details :
#1 "delay" API makes the process wait for the Specified time.
'''

'''
delay  15  please wait for 60 seconds then check for BGP "state: Established"
'''
def delay(delay='',message=''):  
    if time!='':
        log.info(message)
        time.sleep(int(delay))
        return True
    else:
        return False
    






'''
[API Documentation] 
#ID : ops_api_0024
#Name : getTestCaseParams(testcase,test)
#API Feature details :
#1 API "getTestCaseParams" Parses the "OpenSnaproute.params" file.
#2 Returns the prarameters_details used in the testcase                             
'''

def getTestCaseParams(testcase="",test=""):
        testcase=str(testcase)
        if test=="":
                xml = open('OpenSnaproute.params').read()
                tc=xmldict.xml_to_dict(xml)
                testcaseInfo=tc['TestCase'][testcase]
                return testcaseInfo
        elif test!="":
                xml = open('OpenSnaproute.params').read()
                tc=xmldict.xml_to_dict(xml)
                test_values=tc['TestCase'][testcase][test]
                return test_values 





'''
[API Documentation]
#ID : ops_api_0025
#Name :parse_device(device) 
#API Feature details :
"parse_device" API opens and reads the PARAM(OpenSnaproute.params) File and Fetches and returns the Device information after converting into a Dictionary.
'''

def parse_device(device="") :
    xml = open('OpenSnaproute.params').read()
    parsedInfo = xmldict.xml_to_dict(xml)
    if device!="":
        device=str(device)
        device_name=parsedInfo['TestCase']['Device'][device]
        return device_name
    else:
        device_name=parsedInfo['TestCase']['Device']
        return device_name





'''
[API Documentation]
#ID : ops_api_0026
#Name :enablelldp(mode,fab_devices,csw_devices,asw_devices,fab=[],csw=[],asw=[]) 
#API Feature details :
"Enabling the LLDP Globally
'''
def enablelldp(mode,fab_devices,csw_devices,asw_devices,fab=[],csw=[],asw=[]) :
    list1=[]
    count=0
    if mode == "no" :
        for i in range(0,int(fab_devices)) :
            list1.append(fab[i])
        for i in range(0,int(csw_devices)) :
            list1.append(csw[i])
        for i in range(0,int(asw_devices)) :
            list1.append(asw[i])
    if mode == "yes":
        for i in fab:
            list1.append(i)
        for i in csw:
            list1.append(i)
        for i in asw:
            list1.append(i)
    for i in range(len(list1)) :
            device = list1[i]
            device_name=Device_parser(device)
            device_Info = Get_deviceInfo(device_name)
            log.info("Log-in to "+device_name+" to enable LLDP")
            ip_address = device_Info[1]
            swtch = FlexSwitch (ip_address, 8080)
            result=swtch.updateLLDPGlobal("default",Enable="True",TranmitInterval=30)
            if result.ok or result.status_code == 500:
                log.success("LLDP is enabled on "+device_name)
                count=count+1
     
    if count == len(list1):
        log.success("LLDP is enabled ")
        return True
    else :
        log.failure("LLDP is not enabled ")
        return False


'''
[API Documentation]
#ID : ops_api_0027
#Name : lldpNeighborInfo()
#API Feature details :
#1 " lldpNeighborInfo" API verifies the LLDP neighbour information.
'''



def lldpNeighborInfo(mode,fab_devices,csw_devices,asw_devices,devices=[],fab=[],csw=[],asw=[],interface_dict={}):

    Result=[]
    if mode == 'yes':
        for device in devices:
            device_name=Device_parser(device)
            device_Info = Get_deviceInfo(device_name)
            ip_address = device_Info[1]
            swtch = FlexSwitchShow (ip_address, 8080)
            test_name = BuiltIn().get_variable_value("${TEST_NAME}")      
            device_name=parse_device(device)
            device_params=getTestCaseParams(test_name,device_name)
            log.step('Checking LLDP Neighbor Information For The Device: '+device_name)
            lldp_dict = ast.literal_eval(device_params)
            result = swtch.printLLDPIntfStates()
            log.details(result)
            fd = open("sample.txt","w+")
            fd.write(result)
            fd.close()
            f = open("sample.txt","r")
            j=0
            count=0
            line = f.readlines()        
            for eachline in line :
                pattern1 = r'\s*([A-z0-9]*)\s*\d*\s*\d*\s*\d*\s*True\s*([A-z0-9]*)\s*[A-z0-9:]*\s*([A-z0-9]*)\s*([A-z0-9]*).*'
                match = re.match(pattern1,eachline)
                if match :
                    neighborportid = match.group(3) 
                    portid = match.group(1)
                    dest1 = match.group(4)
                    dest1 = dest1.lower()
                    for loop in range(len(lldp_dict)) :
                        source=lldp_dict[loop][j]
                        dest=lldp_dict[loop][j+1]
                        source_params=source.split(':')
                        dest_params=dest.split(':')
                        source_name=source_params[0]
                        source_port=source_params[1]
                        dest_name=dest_params[0]
                        dest_port=dest_params[1]
                        if source_port==portid and dest_port==neighborportid and dest_name.lower() == dest1: 
                            log.info("port "+portid+" of "+device_name+" Is Connected To Port "+neighborportid+" of "+dest1)
                            count=count+1
                            break
                            
#                    k=k+1
            os.remove("sample.txt")    
            if count==(len(lldp_dict)):
                log.success('LLDP Neighbor Information Matched With The Given Information\n')
                Result.append("Pass")
            else:
                log.failure('LLDP Neighbor Information Does Not Matches With The Given Information\n')
                Result.append("Fail") 
            count =0
            if "Fail" in Result:
                raise testfail.testFailed("LLDP neighbor information does not matches with the given information\n")
            

    if mode=='no':
        list1=[]
        list2=[]
        j=0
        rise=0
        count=0
        for i in range(0,int(fab_devices)) :
            list1.append(fab[i])
        for i in range(0,int(csw_devices)) :
            list1.append(csw[i])
        for i in range(0,int(asw_devices)) :
            list1.append(asw[i])
        for i in range(0,len(list1)):
                device_n=list1[i]
                for device in list1:
                    if device != device_n :
                        device_interface=device_n+"_"+device+"_eth"    
                        if device_interface in interface_dict.keys():
                            list2.append(device)
                            rise=rise+1
                device_name=Device_parser(device_n)
                device_Info = Get_deviceInfo(device_name)
                ip_address = device_Info[1]
                swtch = FlexSwitchShow (ip_address, 8080)
                test_name = BuiltIn().get_variable_value("${TEST_NAME}")      
                device_name=parse_device(device_n)
                device_params=getTestCaseParams(test_name,device_name)
                log.step('Checking LLDP Neighbor Information For The Device: '+device_name)
                lldp_dict = ast.literal_eval(device_params)
                result = swtch.printLLDPIntfStates()          
                log.details(result)
                fd = open("sample.txt","w+")
                fd.write(result)
                fd.close()
                f = open("sample.txt","r")
                line = f.readlines()
#               for device in list2:
#                   j=0
#                   name=parse_device(device)
#                   name=name.lower()
                #print len(line)
                #print line
                #print list2
                for eachline in line :
                        
                        pattern1 = r'\s*([A-z0-9]*)\s*\d*\s*\d*\s*\d*\s*True\s*([A-z0-9]*)\s*[A-z0-9:]*\s*([A-z0-9]*)\s*([A-z0-9]*).*'
                        match = re.match(pattern1,eachline)
 
                        if match :
                            neighborportid = match.group(3) 
                            portid = match.group(1)
                            dest1 = match.group(4)
                            dest1 = dest1.lower()
                        for device in list2:
                          flag = 0
                          j=0
                          dest_n=parse_device(device)
                          dest_n=dest_n.lower()
                          if match:
                             for loop in range(len(lldp_dict)) :
                                source=lldp_dict[loop][j]
                                dest=lldp_dict[loop][j+1]
                                source_params=source.split(':')
                                dest_params=dest.split(':')
                                source_name=source_params[0]
                                source_port=source_params[1]
                                dest_name=dest_params[0]
                                dest_port=dest_params[1] 
                                if source_port==portid and dest_port==neighborportid and dest_n == dest1.lower(): 
                                    log.info("port "+portid+" of "+device_name+" Is Connected To Port "+neighborportid+" of "+dest1)
                                    count=count+1
                                    flag = 1
                                    break
                          if flag == 1:
                              flag=0
                              break
                if count==rise:
                    log.success('LLDP Neighbor Information Matched With The Given Information\n')
                    Result.append("Pass")
                else:
                    log.failure('LLDP Neighbor Information Does Not Matches With The Given Information\n')
                    Result.append("Fail") 
                count =0
                rise = 0
                list2=[]
        os.remove("sample.txt")
        if "Fail" in Result:
                    raise testfail.testFailed("LLDP neighbor information does not matches with the given information\n") 

          
                      

        
'''
[API Documentation]
#ID : ops_api_0028
#Name : host()
#API Feature details :
#1 " To rename host
'''   
def host(mode,fab_devices,csw_devices,asw_devices,fab=[],csw=[],asw=[],hostname={}):  

    list1=[]
    if mode == "no" :
        for i in range(0,int(fab_devices)) :
            list1.append(fab[i])
        for i in range(0,int(csw_devices)) :
            list1.append(csw[i])
        for i in range(0,int(asw_devices)) :
            list1.append(asw[i])
                        #print json.dumps(create_IPv4Intf)
    if mode == "yes":
        for i in fab:
            list1.append(i)
        for i in csw:
            list1.append(i)
        for i in asw:
            list1.append(i)
    for i in range(len(list1)):
            port = []
            device = list1[i]
            device_name=Device_parser(device)
            connectionInfo=Connect(device)
            log.info("log into "+device_name+" to specify Hostname")
            connectionInfo.sendline(hostname[list1[i]])
            connectionInfo.expect("#")
'''
[API Documentation]
#ID : ops_api_0029
#Name : lldpNeighborInfo()
#API Feature details :
#1 Parse the XL sheet for LLDP Testcase
'''

def parse(path,sheet_name):

    workbook=xlrd.open_workbook(path)
    sheet=workbook.sheet_by_name(sheet_name)
    device=[]
    devices=[]
    li=[]
    keys = [sheet.cell(0, col_index).value for col_index in xrange(sheet.ncols)]
    dictionary = {}
    column=2
    col=1
    for row_index in  xrange(1, sheet.nrows):
       cell = sheet.cell(row_index,col)   
       if sheet.cell(row_index,column).value == '':
            continue
       for col_index in xrange(sheet.ncols):
            if keys[col_index]=='Device2' or keys[col_index]=='Device1' :
                key = (sheet.cell(row_index, col_index).value).lower()
                if sheet.cell(row_index, col_index).value not in device:
                    device.append((sheet.cell(row_index, col_index).value).lower())
            if keys[col_index]=='Port1':
                value = sheet.cell(row_index, col_index).value
                dictionary[str(key)] = (str(value)).lower()
            if keys[col_index]=='Port2': 
                value = sheet.cell(row_index, col_index).value
                dictionary[str(key)] = (str(value)).lower() 
                li.append(dictionary)
                dictionary={}
    return li          
'''
[API Documentation]
#ID : ops_api_0030
#Name : lldpNeighborInfo_V2()
#API Feature details :
#1 " lldpNeighborInfo" API verifies the LLDP neighbour information using XLsheet.
'''
            
def lldpNeighborInfo_V2(mode,path,sheet_name,fab_devices,csw_devices,asw_devices,devices=[],fab=[],csw=[],asw=[],interface_dict={}):
    Result=[]
    lldp = parse(path,sheet_name)
    rise=0
    list1=[]
    if mode == "yes":
        for i in fab:
            list1.append(i)
        for i in csw:
            list1.append(i)
        for i in asw:
            list1.append(i)
        for i in range(0,len(list1)):
            device_n=list1[i]
            rise = 0
            for device in list1:
                if device != device_n :
                    device_interface=device_n+"_"+device+"_eth"    
                    if device_interface in interface_dict.keys():
                        rise=rise+1
            device_name=Device_parser(device_n)
            device_Info = Get_deviceInfo(device_name)
            ip_address = device_Info[1]
            swtch = FlexSwitchShow (ip_address, 8080)
            test_name = BuiltIn().get_variable_value("${TEST_NAME}")      
            log.step('Checking LLDP Neighbor Information For The Device: '+device_name)
            result = swtch.printLLDPIntfStates()
            log.details(result)
            fd = open("sample.txt","w+")
            fd.write(result)
            fd.close()
            f = open("sample.txt","r")
            j=0
            count=0
            line = f.readlines() 
            for eachline in line :
                pattern1 = r'\s*([A-z0-9]*)\s*\d*\s*\d*\s*\d*\s*True\s*([A-z0-9]*)\s+[A-z0-9:]*\s*([A-z0-9]*)\s*([A-z0-9]*)\s*[0-9A-z.]*\s*F.*'
                match = re.match(pattern1,eachline)
                if match :
                    devicename=device_name.lower()
                    neighborportid = match.group(3) 
                    portid = match.group(1)
                    destination = match.group(4)
                    destination_devicename = destination.lower()
                    for lldp_s in lldp:
                           if (devicename in str(lldp_s) and destination_devicename in str(lldp_s)):
                                 if (neighborportid == lldp_s[destination_devicename] and portid == lldp_s[devicename]):
                                     log.info("port "+portid+" of "+devicename+" Is Connected To Port "+neighborportid+" of "+destination_devicename)
                                     count=count+1
                                     break
            if count==rise and count !=0:
                log.success('LLDP Neighbor Information Matched With The Given Information\n')
                Result.append("Pass")
            else:
                log.failure('LLDP Neighbor Information Does Not Matches With The Given Information\n')
                Result.append("Fail") 
            count =0
        if "Fail" in Result:
                raise testfail.testFailed("LLDP neighbor information does not matches with the given information\n")

    if mode=='no':
        list1=[]
        list2=[]
        j=0
        rise=0
        count=0
        for i in range(0,int(fab_devices)) :
            list1.append(fab[i])
        for i in range(0,int(csw_devices)) :
            list1.append(csw[i])
        for i in range(0,int(asw_devices)) :
            list1.append(asw[i])
        for i in range(0,len(list1)):
                device_n=list1[i]
                for device in list1:
                    if device != device_n :
                        device_interface=device_n+"_"+device+"_eth"    
                        if device_interface in interface_dict.keys():
                            list2.append(device)
                            rise=rise+1
                device_name=Device_parser(device_n)
                device_Info = Get_deviceInfo(device_name)
                ip_address = device_Info[1]
                swtch = FlexSwitchShow (ip_address, 8080)
                test_name = BuiltIn().get_variable_value("${TEST_NAME}")      
                log.step('Checking LLDP Neighbor Information For The Device: '+device_name)
                result = swtch.printLLDPIntfStates()  
                log.details(result)
                fd = open("sample.txt","w+")
                fd.write(result)
                fd.close()
                f = open("sample.txt","r")
                line = f.readlines()
                devicename=device_name.lower()
                for eachline in line :
                        
                        pattern1 = r'\s*([A-z0-9]*)\s*\d*\s*\d*\s*\d*\s*True\s*([A-z0-9]*)\s+[A-z0-9:]*\s*([A-z0-9]*)\s*([A-z0-9]*)\s*[0-9A-z.]*\s*F.*'
                        match = re.match(pattern1,eachline)
 
                        if match :
                            neighborportid = match.group(3) 
                            portid = match.group(1)
                            destination = match.group(4)
                            destination_devicename = destination.lower()
                        for device in list2:
                          flag = 0
                          j=0
                          dest_name=Device_parser(device)
                          dest_name=dest_name.lower()
                          if match:
                             for lldp_s in lldp:
                               if (devicename in str(lldp_s) and destination_devicename in str(lldp_s)):
                                 if (neighborportid == lldp_s[destination_devicename] and portid == lldp_s[devicename] and dest_name.lower() == destination_devicename):
                                     log.info("port "+portid+" of "+devicename+" Is Connected To Port "+neighborportid+" of "+destination_devicename)
                                     count=count+1
                                     flag = 1
                                     break
                          if flag == 1:
                              flag=0
                              break
                if count==rise and count !=0:
                    log.success('LLDP Neighbor Information Matched With The Given Information\n')
                    Result.append("Pass")
                else:
                    log.failure('LLDP Neighbor Information Does Not Matches With The Given Information\n')
                    Result.append("Fail") 
                count =0
                rise = 0
                list2=[]
        if "Fail" in Result:
                    raise testfail.testFailed("LLDP neighbor information does not matches with the given information\n") 



'''
[API Documentation]
#ID : OpenSnaproute_api_031
#Name :static_route_configuration
#API Feature details :
"Device_parser" API will configure the static route using SDK function
''' 

def static_route_configuration(device,dest_net,nexthop_Ip,interface):
    device_name=Device_parser(device)
    device_Info=Get_deviceInfo(device_name)
    ip_address=device_Info[1]
    swtch = FlexSwitch (ip_address, 8080)
    log.info("creating Static route on "+device_name)
    result = swtch.createIPv4Route(dest_net,"255.255.255.254", [{"NextHopIp": nexthop_Ip}])
    if result.ok or result.status_code == 500:
        log.success("static route is configured")
        return True
    else:
        log.failure("Failed to Configure static route on "+device_name) 
        return False




'''
[API Documentation]
#ID : OpenSnaproute_api_032
#Name :Ping
#API Feature details :
"Device_parser" API will do the ping test between source and destination devices
'''

def Ping(deviceSrc,deviceDest,destIP):
     log.info("Checking reachability between "+Device_parser(deviceSrc)+" and "+Device_parser(deviceDest)+" using PING.")
     log.info("Logging into :"+Device_parser(deviceSrc))
     device_connect=Connect(deviceSrc)
     log.info("Device "+Device_parser(deviceSrc)+" Log-in Successful")
     log.info("start pinging from SOURCE-"+Device_parser(deviceSrc)+" to  DESTINATION-"+Device_parser(deviceDest)+" of IP - "+destIP)
     device_connect.sendline("ping "+destIP+" -c 5")
     device_connect.expect('[#\$] ')
     time.sleep(20)
     log.details(device_connect.before)
     PingResults= device_connect.before
     pat=re.compile(r'(\n*\s*(\d+)\s*\s+packets\stransmitted\,\s+(\d+)\s+received\,\s*(\d+)\%\s+packet\s+loss)',re.MULTILINE)
     match=re.search(pat,PingResults)
     if match:
	 PacketLoss=match.group(4)
	 if PacketLoss=='0':
	     log.success("PING Successful!!No Packet Loss")
             return True
	 else:             
             raise AssertionError("PING UNSUCESSFULL")
             return False
     else:
         raise AssertionError("PING UNSUCESSFULL") 
         return False

'''
[API Documentation]
#ID : OpenSnaproute_api_033
#Name :delete_peer_group
#API Feature details :
"Device_parser" API will delete the peer group using SDK function
''' 

def delete_peer_group(device,peer_group_id) :
    device_name=Device_parser(device)
    device_Info=Get_deviceInfo(device_name)
    ip_address=device_Info[1]
    swtch = FlexSwitch (ip_address, 8080)
    result=swtch.deleteBGPv4PeerGroup(peer_group_id)
    if result.status_code == 410:
        log.success("Peer-Group is removed in "+device_name)
        return True

    else:
        log.failure("Failed to remove Peer-Group on "+device_name)
        return False
    

'''
[API Documentation]
#ID : OpenSnaproute_api_034
#Name :assignipv6
#API Feature details :
"Device_parser" API will assign the IPv6 address to the routers using SDK function
''' 

def assignipv6(mode,fab_devices,csw_devices,asw_devices,subnet,fab=[],csw=[],asw=[],interface_dict={},interface_ipv6_dict={}) :
    list1=[]
    c=0
    if mode == "no" :
        for i in range(0,int(fab_devices)) :
            list1.append(fab[i])
        for i in range(0,int(csw_devices)) :
            list1.append(csw[i])
        for i in range(0,int(asw_devices)) :
            list1.append(asw[i])
        for i in range(len(list1)):
            a=0
            b=0
            port = []       
            interface_ip=[]
            device = list1[i]
            device_name=Device_parser(device)
            log.info("login to "+device_name+" and configure IP address")
            device_Info = Get_deviceInfo(device_name)
            ip_address = device_Info[1]
            swtch = FlexSwitch (ip_address, 8080)  # Instantiate object to talk to flexSwitch
            for j in range(len(list1)):
                if device != list1[j] :
                    device_ip=device+"_"+list1[j]+"_interface_ip "
                    device_interface=device+"_"+list1[j]+"_eth"    
                    if device_ip in interface_ipv6_dict.keys() and device_interface in interface_dict.keys():
                        a=a+1
                        result=swtch.createIPv6Intf(interface_dict[device_interface],interface_ipv6_dict[device_ip]+subnet,AdminState='UP')
                        if result.ok or result.status_code == 500:
                            b=b+1
                        else:
                            log.failure("Failed to Configure IPv6 "+interface_dict[device_interface]+"on "+device_name)
            if a==b:
               log.success("IPv6 is configured successfully on "+device_name)
               c= c+1    
    if mode == "yes":
        for i in fab:
            list1.append(i)
        for i in csw:
            list1.append(i)
        for i in asw:
            list1.append(i)
        for i in range(len(list1)):
            a=0
            b=0
            device = list1[i]
            device_name=Device_parser(device)
            log.info("login to "+device_name+" and configure IP address")
            device_Info = Get_deviceInfo(device_name)
            ip_address = device_Info[1]
            swtch = FlexSwitch (ip_address, 8080)  # Instantiate object to talk to flexSwitch
            for j in range(len(list1)):
                if device != list1[j] :
                    device_ip=device+"_"+list1[j]+"_interface_ip "
                    device_interface=device+"_"+list1[j]+"_eth"    
                    if device_ip in interface_ipv6_dict.keys() and device_interface in interface_dict.keys():
                        a=a+1
                        result=swtch.createIPv6Intf(interface_dict[device_interface],interface_ipv6_dict[device_ip]+subnet,AdminState='UP')
                        if result.ok or result.status_code == 500:
                            b=b+1
                        else:
                            log.failure ("Failed to Configure IPv6 "+interface_dict[device_interface]+"on "+device_name)
            if a==b:
               log.success("IPv6 is configured successfully on "+device_name)
               c= c+1
    if c == len(list1):
        log.success("IP is configured successfully")
        return True
    else:
        log.failure("IP is not configured")
        return False


'''
[API Documentation]
#ID : OpenSnaproute_api_035
#Name :removeipv6
#API Feature details :
"Device_parser" API will delete the interfaces and IPv6 address from the routers using SDK function
''' 

def removeipv6(mode,fab_devices,csw_devices,asw_devices,subnet,fab=[],csw=[],asw=[],interface_dict={},interface_ipv6_dict={}) :
    list1=[]
    if mode == "no" :
        for i in range(0,int(fab_devices)) :
            list1.append(fab[i])
        for i in range(0,int(csw_devices)) :
            list1.append(csw[i])
        for i in range(0,int(asw_devices)) :
            list1.append(asw[i])
        c=0
        for i in range(len(list1)):
            a=0
            b=0
            port = []
            interface_ip=[]
            device = list1[i]
            device_name=Device_parser(device)
            log.info("login to "+device_name+" and configure IPv6 address")
            device_Info = Get_deviceInfo(device_name)
            ip_address = device_Info[1]
            swtch = FlexSwitch (ip_address, 8080)  # Instantiate object to talk to flexSwitch
            for j in range(len(list1)):
                if device != list1[j] :
                    device_ip=device+"_"+list1[j]+"_interface_ip "
                    device_interface=device+"_"+list1[j]+"_eth"    
                    if device_ip in interface_ipv6_dict.keys() and device_interface in interface_dict.keys():
                        a=a+1
                        delete_IPv6Intf=swtch.deleteIPv6Intf(interface_dict[device_interface])
                        if delete_IPv6Intf.status_code == 410:
                            b=b+1
                        else:
                            log.failure ("Failed to remove IPv6 "+interface_dict[device_interface]+"on "+device_name)
            if a==b :
                log.success("IPv6 is removed successfully on "+device_name)
                c= c+1
    if mode == "yes":
        for i in fab:
            list1.append(i)
        for i in csw:
            list1.append(i)
        for i in asw:
            list1.append(i)
        c=0
        for i in range(len(list1)):
            a=0
            b=0
            device = list1[i]
            device_name=Device_parser(device)
            device_Info = Get_deviceInfo(device_name)
            log.info("login to "+device_name+" and configure IPv6 address")
            ip_address = device_Info[1]
            swtch = FlexSwitch (ip_address, 8080)  # Instantiate object to talk to flexSwitch
            for j in range(len(list1)):
                if device != list1[j] :
                    device_ip=device+"_"+list1[j]+"_interface_ip "
                    device_interface=device+"_"+list1[j]+"_eth"    
                    if device_ip in interface_ipv6_dict.keys() and device_interface in interface_dict.keys():
                        a=a+1
                        delete_IPv6Intf=swtch.deleteIPv6Intf(interface_dict[device_interface])
                        if delete_IPv6Intf.status_code == 410:
                            b=b+1
                        else:
                            log.failure ("Failed to remove IPV6 "+interface_dict[device_interface]+"on "+device_name)
                            return False
            if a==b :
                log.success("IPv6 is removed successfully on "+device_name)
                c= c+1

    if c == len(list1):
        log.success("IPv6 is removed successfully")
        return True
    else:
        log.failure("IPv6 is not removed ")
        return False


'''
[API Documentation]
#ID : OpenSnaproute_api_036
#Name :assignbgpv6
#API Feature details :
"Device_parser" API will assign the BGP IPv6 address to the routers using SDK function
''' 

def assignbgpv6(mode,fab_devices,csw_devices,asw_devices,fab=[],csw=[],asw=[],interface_ipv6_dict={},asnum={},router_id={}) :
    list1=[]
    neighbor=[]
    peer_as=[]
    c=0
    if mode == "no" :
        for i in range(0,int(fab_devices)) :
            list1.append(fab[i])
        for i in range(0,int(csw_devices)) :
            list1.append(csw[i])
        for i in range(0,int(asw_devices)) :
            list1.append(asw[i])
        for i in range(len(list1)):
            a=0
            b=0
            neighbor=[]
            peer_as=[]
            device = list1[i]
            device_name=Device_parser(device)
            device_Info = Get_deviceInfo(device_name)
            log.info("log-in to "+device_name+" and loading BGP Configuration")
            ip_address = device_Info[1]
            swtch = FlexSwitch (ip_address, 8080)  # Instantiate object to talk to flexSwitch
            local=asnum[device]
            Routerid=router_id[device]
            swtch.updateBGPGlobal("default",ASNum=local,RouterId=Routerid)
            for j in range(len(list1)):
                
                peer=asnum[list1[j]]
                if device != list1[j] :
                    device_ip=list1[j]+"_"+device+"_interface_ip " 
                    if device_ip in interface_ipv6_dict.keys() :
                        a=a+1
                        result=swtch.createBGPv6Neighbor("",interface_ipv6_dict[device_ip],PeerAS=peer,LocalAS=local)
                        if result.ok or result.status_code == 500:
                            b=b+1
                        else:
                            log.failure ("Failed to Configure BGP neighbor "+interface_ipv6_dict[device_ip]+"on "+device_name)

            if a==b:
                log.success("BGP Configured successfully on "+device_name)
                c=c+1
    if mode == "yes":
        for i in fab:
            list1.append(i)
        for i in csw:
            list1.append(i)
        for i in asw:
            list1.append(i)
        for i in range(len(list1)):
            a=0
            b=0
            device = list1[i]
            device_name=Device_parser(device)
            device_Info = Get_deviceInfo(device_name)
            ip_address = device_Info[1]
            swtch = FlexSwitch (ip_address, 8080)  # Instantiate object to talk to flexSwitch
            local=asnum[device]      
            Routerid=router_id[device]
            swtch.updateBGPGlobal("default",ASNum=local,RouterId=Routerid)
            log.info("log-in to "+device_name+" and loading BGP Configuration")
            for j in range(len(list1)):
                peer=asnum[list1[j]]
                if device != list1[j] :
                    device_ip=list1[j]+"_"+device+"_interface_ip " 
                    if device_ip in interface_ipv6_dict.keys() :
                      a=a+1
                      result=swtch.createBGPv6Neighbor("",interface_ipv6_dict[device_ip],PeerAS=peer,LocalAS=local)
                      if result.ok or result.status_code == 500:
                            b=b+1
                      else:
                            log.failure ("Failed to Configure BGP neighbor "+interface_ipv6_dict[device_ip]+"on "+device_name)

            if a==b:
                log.success("BGP Configured successfully on "+device_name)
                c=c+1
    if c == len(list1):
        log.success("BGP is configured successfully")
        return True
    else:
        log.failure("BGP is not configured")
        return False  


'''
[API Documentation]
#ID : OpenSnaproute_api_037
#Name :removebgpv6
#API Feature details :
"Device_parser" API will remove the bgp IPv6 neighbor address from the routers using SDK function
''' 

def removebgpv6(mode,fab_devices,csw_devices,asw_devices,fab=[],csw=[],asw=[],interface_ipv6_dict={},asnum={},router_id={}) :
    list1=[]
    neighbor=[]
    peer_as=[]
    c=0
    if mode == "no" :
        for i in range(0,int(fab_devices)) :
            list1.append(fab[i])
        for i in range(0,int(csw_devices)) :
            list1.append(csw[i])
        for i in range(0,int(asw_devices)) :
            list1.append(asw[i])
        for i in range(len(list1)):
            a=0
            b=0
            neighbor=[]
            peer_as=[]
            device = list1[i]
            device_name=Device_parser(device)
            device_Info = Get_deviceInfo(device_name)
            ip_address = device_Info[1]
            log.info("log-in to "+device_name+" and remove BGP Configuration")
            swtch = FlexSwitch (ip_address, 8080)  # Instantiate object to talk to flexSwitch
            local=asnum[device]
            Routerid=router_id[device]
            swtch.updateBGPGlobal("default",ASNum=local,RouterId=Routerid)
            for j in range(len(list1)):
                peer=asnum[list1[j]]
                if device != list1[j] :
                    device_ip=list1[j]+"_"+device+"_interface_ip " 
                    if device_ip in interface_ipv6_dict.keys() :
                        a=a+1
                        removeBGPv6_Neighbor=swtch.deleteBGPv6Neighbor("",interface_ipv6_dict[device_ip])
                        if removeBGPv6_Neighbor.status_code == 410:
                            b=b+1
                        else:
                            log.failure( "Failed to remove BGP neighbor "+interface_ipv6_dict[device_ip]+"on "+device_name)
            if a==b:
                log.success("BGP Configuration removed on "+device_name)
                c=c+1
    if mode == "yes":
        for i in fab:
            list1.append(i)
        for i in csw:
            list1.append(i)
        for i in asw:
            list1.append(i)
        for i in range(len(list1)):
            a=0
            b=0
            device = list1[i]
            device_name=Device_parser(device)
            device_Info = Get_deviceInfo(device_name)
            ip_address = device_Info[1]
            swtch = FlexSwitch (ip_address, 8080)  # Instantiate object to talk to flexSwitch
            local=asnum[device]      
            Routerid=router_id[device]
            log.info("log-in to "+device_name+" and remove BGP Configuration")
            swtch.updateBGPGlobal("default",ASNum=local,RouterId=Routerid)
            for j in range(len(list1)):
                peer=asnum[list1[j]]
                if device != list1[j] :
                    device_ip=list1[j]+"_"+device+"_interface_ip " 
                    if device_ip in interface_ipv6_dict.keys() :
                      removeBGPv6_Neighbor=swtch.deleteBGPv6Neighbor("",interface_ipv6_dict[device_ip])
                      a=a+1
                      if removeBGPv6_Neighbor.status_code == 410:
                            b=b+1
                      else:
                            log.failure( "Failed to remove BGP neighbor "+interface_ipv6_dict[device_ip]+"on "+device_name)
            if a==b:
                log.success("BGP Configuration removed on "+device_name)
                c=c+1
    if c == len(list1):
        log.success("BGP is removed successfully")
        return True
    else:
        log.failure("BGP is not removed ")
        return False
                                

'''
[API Documentation]
#ID : OpenSnaproute_api_038
#Name :neighbor_state_all
#API Feature details :
"Device_parser" API will check for the IPv6 neighborship state for entire routers using SDK function
''' 
      
def neighbor_ipv6_state_all(state,mode,fab_devices,csw_devices,asw_devices,fab=[],csw=[],asw=[],interface_ip_dict={}):
    list1=[]
    if mode == "no" :
        for i in range(0,int(fab_devices)) :
            list1.append(fab[i])
        for i in range(0,int(csw_devices)) :
            list1.append(csw[i])
        for i in range(0,int(asw_devices)) :
            list1.append(asw[i])
    if mode == "yes":
        for i in fab:
            list1.append(i)
        for i in csw:
            list1.append(i)
        for i in asw:
            list1.append(i)
    device_count=0
    for i in list1:
        flag=0
        device=i;
    	device_name=Device_parser(device)
    	log.step('Checking for '+state+' in '+device_name)
    	log.info('Log-in into '+device_name+' to check for '+state+' state')
        device_name=Device_parser(device)
        device_Info = Get_deviceInfo(device_name)
        ip_address = device_Info[1]
        swtch = FlexSwitch (ip_address, 8080)
        Output = swtch.getAllBGPv6NeighborStates() 
        log.details(Output)
    	match_count=0
    	rec_count=0
    	dev_count=0
    	list2=[]
        flag=0
    	for eachline in Output:
                    for j in range(len(list1)):
                        if device != list1[j] :
                            dev_count = dev_count+1
                            device_ip=list1[j]+"_"+device+"_interface_ip "
                            if device_ip in interface_ip_dict.keys() :
                                if list1[j] not in list2:
                                    list2.append(list1[j])
                                ip_actual=interface_ip_dict[device_ip]
                                ip_actual="'"+ip_actual+"'"
                                if (ip_actual) in str(eachline) and "'SessionState': 6" in str(eachline):
                                        rec_count=rec_count+1
                                        flag=1
                                        break
        if rec_count == len(list2) and flag==1:
            log.success("Required "+state+" state is achieved in "+device_name)
            device_count=device_count+1
        else:
            log.failure("Required "+state+" state is not achieved on "+device_name)
    if device_count == len(list1):
        log.success("Neighborship is get "+state+" state on all devices")
        return True
    else:
        log.failure("Neighborship is not get "+state+" state on all devices")
        return False

'''
[API Documentation]
#ID : OpenSnaproute_api_039
#Name :create_bfd_neighbor(device,bfd_name,neighbor_ip,asnum) 
#API Feature details :
"Device_parser" API will add BFD to the neighbor using SDK function
'''

def create_bfd_neighbor(device,bfd_name,neighbor_ip,asnum,peeras) :

    device_name=Device_parser(device)
    device_Info=Get_deviceInfo(device_name)
    ip_address=device_Info[1]
    swtch = FlexSwitch (ip_address, 8080)
    result=swtch.updateBGPv4Neighbor(IntfRef='',NeighborAddress=neighbor_ip,PeerAS=peeras,LocalAS=asnum,BfdEnable="True",BfdSessionParam=bfd_name)
    if result.ok or result.status_code == 500:
        log.success("BFD is assigned to neighbor on "+device_name)
        return True

    else:
        log.failure("Failed to assign bfd to neighbor on "+device_name)
        return False 


'''
[API Documentation]
#ID : OpenSnaproute_api_040
#Name :check_bfd(mode,device,device1,interface_dict={})
#API Feature details :
"Device_parser" API will validate the BFD state using CLI
'''    

def check_bfd(mode,device,device1,interface_dict={}) :
    flag = 0
    device_name=Device_parser(device)
    device_interface=device1+"_"+device+"_interface_ip "
    ip_address=interface_dict[device_interface]
    log.step(' Checking BFD state in ' +device_name)
    log.info('Log-in into '+device_name+' to check for neighbor')
    connectionInfo=Connect(device)
    connectionInfo.sendline('snap_cli ')
    connectionInfo.expect('>')
    connectionInfo.sendline('enable ')
    connectionInfo.expect('#')
    connectionInfo.sendline('show bfd session')
    connectionInfo.expect('#')
    result= connectionInfo.before         
    log.details(result)
    fd = open("sample.txt","w+")
    fd.write(result)
    fd.close()
    f = open("sample.txt","r") 
    line = f.readlines()
    pattern = r'\s*(\d*.\d*.)\s*\d*/\d*\s*[A-z]*,\s*\d*\s*\d*\s*\d*\s*([A-z]*).*'
    pattern1 = r'\s*(\d*.\d*).*'
    for eachline in range (len(line)):
        match = re.search(pattern,line[eachline])
        if match:
            eachline=eachline+1
            match1=re.search(pattern1,line[eachline])
            ip_new=match.group(1)+match1.group(1)
            if mode == "noshutdown" :
                if ip_new == ip_address and match.group(2) == "up":
                    flag =1
                    log.success("BFD state is UP on "+device_name)
                    return True
                else :
                    log.failure("BFD state is not up on "+device_name)
                    return False
            if mode == "shutdown" :
                if ip_new == ip_address and match.group(2) == "down":
                    flag =1
                    log.success("BFD state is DOWN on "+device_name)
                    return True
                else :
                    log.failure("BFD state is not DOWN on "+device_name)
                    return False
    if flag == 0 :
        log.failure("BFD state or ip address is not found in "+device_name)
        return False          





'''
[API Documentation]
#ID : OpenSnaproute_api_041
#Name :interface_vlan(device,interface,vlan_id) 
#API Feature details :
"Device_parser" API will add VLAN to the interface using SDK function.
'''
def interface_vlan(device,vlanid,intf='') :
    device_name=Device_parser(device)
    device_Info=Get_deviceInfo(device_name)
    ip_address=device_Info[1]
    swtch = FlexSwitch (ip_address, 8080)
    result=swtch.updateVlan(vlanid,AdminState="None",IntfList=[intf])
    if result.ok or result.status_code == 500:
        if intf=='':
            log.success("Vlan interface is deleted on "+device_name)
            return True
        else :
            log.success("Vlan interface is created on "+device_name)     
            return True

    else:
        log.failure("Failed to create/remove Vlan interface on "+device_name)
        return False 


'''
[API Documentation]
#ID : OpenSnaproute_api_042
#Name :vlan_config(device,interface,vlan_id) 
#API Feature details :
"Device_parser" API will create VLAN using SDK function
'''

def vlan_config(device,vlan_id):
    device_name=Device_parser(device)
    device_Info = Get_deviceInfo(device_name)
    ip_address = device_Info[1]
    swtch = FlexSwitch (ip_address, 8080)  # Instantiate object to talk to flexSwitch
    create_Vlan=swtch.createVlan(vlan_id,None,None)
    if create_Vlan.ok or create_Vlan.status_code == 500:
        log.success("Vlan is created on "+device_name)
        return True

    else:
        log.failure("Failed to create Vlan on "+device_name)
        return False

'''
[API Documentation]
#ID : OpenSnaproute_api_043
#Name :deletingvlan(device,vlan_id) 
#API Feature details :
"Device_parser" API will delete VLAN using SDK function
'''

def deletingvlan(device,vlan_id):
    device_name=Device_parser(device)
    device_Info = Get_deviceInfo(device_name)
    ip_address = device_Info[1]
    swtch = FlexSwitch (ip_address, 8080)  # Instantiate object to talk to flexSwitch
    delete_Vlan=swtch.deleteVlan(int(vlan_id))
    if delete_Vlan.status_code == 410:
        log.success("Vlan is removed in "+device_name)
        return True

    else:
        log.failure("Failed to delete Vlan on "+device_name)
        return False


'''
[API Documentation]
#ID : OpenSnaproute_api_044
#Name :check_vlan_status
#API Feature details :
"Device_parser" API will check for the VLAN status using SDK function
''' 

def check_vlan_status(device,vlan_id,state,interface):
        flag=0
        vlan="vlan"+vlan_id
        device_name=Device_parser(device)
        log.info("Loading into "+device_name)
        device_Info = Get_deviceInfo(device_name)
        ip_address = device_Info[1]
        swtch1 = FlexSwitchShow (ip_address, 8080)
        result= swtch1.printCombinedVlanStates() 
        log.details(result)
        fd = open("sample.txt","w+")
        fd.write(result)
        fd.close()
        f = open("sample.txt","r") 
        line = f.readlines()
        for eachline in range (len(line)):
            if vlan_id in line[eachline] and state in line[eachline] and interface in line[eachline]:
                flag=1
                log.success("VLAN verified on "+device_name)
                return True
        if flag == 0:
            log.failure("VLAN is not configured correctly on "+device_name)
            return False



'''
[API Documentation] 
#ID : OpenSnaproute_api_045
#Name : createBGPv4Neighbor_attribute
#API Feature details :
#To create BGP with peer-group using SDK function
''' 
def createBGPv4Neighbor_attribute(device,local,neighbor_address,password='',peergroup='',peeras=''):
    device_name=Device_parser(device)
    device_Info = Get_deviceInfo(device_name)
    ip_address = device_Info[1]
    swtch = FlexSwitch (ip_address, 8080)
    result=swtch.createBGPv4Neighbor('',neighbor_address,PeerAS=peeras,LocalAS=local,AuthPassword=password,PeerGroup=peergroup)
    if result.ok:
        if password!= '':
            log.success("BGP neighbor with password is configured on "+device_name)
            return True
        if peergroup!= '':
            log.success("BGP neighbor with peergroup is configured on "+device_name)
            return True
        else:
            log.success("BGP neighbor is configured on "+device_name)
            return True
    else:
        log.failure("Failed to Configure BGP on "+device_name)
        return False

'''
[API Documentation]
#ID : OpenSnaproute_api_046
#Name :create_peergroup
#API Feature details :
"Device_parser" API will create the peer group using SDK function
'''   
def create_peergroup(device,name,peeras):
    device_name=Device_parser(device)
    device_Info = Get_deviceInfo(device_name)
    ip_address = device_Info[1]
    swtch = FlexSwitch (ip_address, 8080)

    result=swtch.createBGPv4PeerGroup(name,PeerAS=str(peeras))
    if result.ok:
        log.success("peer group is configured on "+device_name)
        return True

    else:
        log.failure("Failed to Configure peer group on "+device_name)
        return False    


'''
[API Documentation]
#ID : OpenSnaproute_api_047
#Name :update_bgpneighbor
#API Feature details :
"Device_parser" API will Update the BGP using SDK function
''' 
def update_bgpneighbor(device,neighboraddress,local=None,password=None,Keep_alive_time=None,Hold_time=None,retrytime=None):
    device_name=Device_parser(device)
    device_Info = Get_deviceInfo(device_name)
    ip_address = device_Info[1]
    swtch = FlexSwitch (ip_address, 8080)
    log.info("log into "+device_name+"on the neighbor ip "+neighboraddress+" to update")
    result=swtch.updateBGPv4Neighbor('',neighboraddress,LocalAS=local,AuthPassword=password,KeepaliveTime=Keep_alive_time,HoldTime=Hold_time,ConnectRetryTime=retrytime)
    if result.ok or result.status_code == 500:
        log.success("BGP neighbor is updated on "+device_name)
        return True

    else:
        log.failure("Failed to update BGP neighbor on "+device_name)
        return False    



'''
[API Documentation]
#ID : OpenSnaproute_api_048
#Name :creatingbfdsession
#API Feature details :
#API will create BFD Session using SDK function
''' 
def creatingbfdsession(device,bfd_name,minrx,interval,multiplier) :
    device_name=Device_parser(device)
    device_Info = Get_deviceInfo(device_name)
    ip_address = device_Info[1]
    swtch = FlexSwitch (ip_address, 8080)

    result=swtch.createBfdSessionParam(Name=bfd_name,RequiredMinRxInterval=minrx,RequiredMinEchoRxInterval=interval,LocalMultiplier=multiplier)
    if result.ok or result.status_code == 500:
        log.success("BFD Session Param is created on "+device_name)
        return True

    else:
        log.failure("Failed to create BFD Session Param on "+device_name)
        return False 

'''
[API Documentation]
#ID : OpenSnaproute_api_049
#Name :creatingbfdsession
#API Feature details :
#API will delete BFD Session using SDK function
''' 
def deletingbfdsession(device,bfd_name) :
    device_name=Device_parser(device)
    device_Info = Get_deviceInfo(device_name)
    ip_address = device_Info[1]
    swtch = FlexSwitch (ip_address, 8080)

    result=swtch.deleteBfdSessionParam(bfd_name)
    if result.status_code == 410:
        log.success("BFD Session Param is deleted on "+device_name)
        return True

    else:
        log.failure("Failed to delete BFD Session Param on "+device_name)
        return False 

'''
[API Documentation]
#ID : OpenSnaproute_api_050
#Name :deletinginterface
#API Feature details :
#API will delete particular interface using SDK function
'''
def deletinginterface(device,intf_name) :
    device_name=Device_parser(device)
    device_Info = Get_deviceInfo(device_name)
    ip_address = device_Info[1]
    swtch = FlexSwitch (ip_address, 8080)

    result=swtch.deleteIPv4Intf(intf_name)
    if result.status_code == 410:
        log.success("IP removed successfully on "+device_name)
        return True

    else:
        log.failure( "Failed to delete IP "+intf_name+"on "+device_name)
        return False 

'''
[API Documentation]
#ID : OpenSnaproute_api_051
#Name :creatinginterface
#API Feature details :
#API will create particular interface using SDK function
'''
def creatinginterface(device,interf,interfaceip) :
    device_name=Device_parser(device)
    device_Info = Get_deviceInfo(device_name)
    ip_address = device_Info[1]
    swtch = FlexSwitch (ip_address, 8080)

    result=swtch.createIPv4Intf(interf,interfaceip)
    if result.ok or result.status_code == 500:
        log.success(interfaceip+" is added to interface "+interf+" on "+device_name)
        return True

    else:
        log.failure("Failed to create "+interfaceip+"  to interface "+interf+" on "+device_name)
        return False 

'''
[API Documentation]
#ID : OpenSnaproute_api_052
#Name :assignbgp_rrclient
#API Feature details :
"Device_parser" API will assign the BGP IPv4 address to the routers using SDK function and assign route reflector Client on the Leaf nodes
''' 

def assignbgp_rrclient(mode,fab_devices,csw_devices,asw_devices,fab=[],csw=[],asw=[],interface_ip_dict={},asnum={},router_id={}) :
    list1=[]
    neighbor=[]
    peer_as=[]
    c=0 
    device_count1=0
    device_count=0
    non_leaf_count=0
    if mode == "no" :
        for i in range(0,int(fab_devices)) :
            list1.append(fab[i])
            device_count =device_count+1
            non_leaf_count = non_leaf_count+1
        for i in range(0,int(csw_devices)) :
            list1.append(csw[i])
            device_count =device_count+1
            non_leaf_count = non_leaf_count+1
        for i in range(0,int(asw_devices)) :
            list1.append(asw[i])
            device_count =device_count+1
        for i in range(len(list1)):
            need_count=0
            received_count=0
            neighbor=[]
            peer_as=[]
            device = list1[i]
            device_name=Device_parser(device)
            device_Info = Get_deviceInfo(device_name)
            log.info("log-in to "+device_name+" and loading BGP configuration")
            ip_address = device_Info[1]
            swtch = FlexSwitch (ip_address, 8080)  # Instantiate object to talk to flexSwitch
            local=asnum[device]
            Routerid=router_id[device]
            swtch.updateBGPGlobal("default",ASNum=local,RouterId=Routerid)
            device_count1=device_count1+1
            for j in range(len(list1)):
                peer=asnum[list1[j]]
                if device != list1[j] :
                    device_ip=list1[j]+"_"+device+"_interface_ip " 
                    if device_ip in interface_ip_dict.keys() :
                      need_count=need_count+1
                      if device_count1 <= non_leaf_count:
                          result=swtch.createBGPv4Neighbor("",interface_ip_dict[device_ip],PeerAS=peer,LocalAS=local)
                          if result.ok or result.status_code == 500:
                            received_count=received_count+1
                          else:
                            log.failure ("Failed to Configure BGP neighbor "+interface_ip_dict[device_ip]+"on "+device_name)
                      if device_count1 > non_leaf_count and device_count1 <=device_count:
                          result=swtch.createBGPv4Neighbor("",interface_ip_dict[device_ip],PeerAS=peer,LocalAS=local,RouteReflectorClient="True")
                          if result.ok or result.status_code == 500:
                            received_count=received_count+1
                          else:
                            log.failure ("Failed to Configure BGP neighbor "+interface_ip_dict[device_ip]+"on "+device_name)
            if need_count == received_count:
                log.success("BGP is configured successfully on "+device_name)
                c=c+1
    if mode == "yes":
        for i in fab:
            list1.append(i)
            device_count =device_count+1
            non_leaf_count = non_leaf_count+1
        for i in csw:
            list1.append(i)
            device_count =device_count+1
            non_leaf_count = non_leaf_count+1
        for i in asw:
            list1.append(i)
            device_count =device_count+1
        for i in range(len(list1)):
            need_count=0
            received_count=0
            device = list1[i]
            device_name=Device_parser(device)
            device_Info = Get_deviceInfo(device_name)
            log.info("log-in to "+device_name+" and loading BGP configuration")
            ip_address = device_Info[1]
            swtch = FlexSwitch (ip_address, 8080)  # Instantiate object to talk to flexSwitch
            local=asnum[device]      
            Routerid=router_id[device]
            swtch.updateBGPGlobal("default",ASNum=local,RouterId=Routerid)
            device_count1=device_count1+1
            for j in range(len(list1)):
                peer=asnum[list1[j]]
                if device != list1[j] :
                    device_ip=list1[j]+"_"+device+"_interface_ip " 
                    if device_ip in interface_ip_dict.keys() :
                      need_count=need_count+1
                      if device_count1 <= non_leaf_count:
                          #print device,list1[j]
                          result=swtch.createBGPv4Neighbor("",interface_ip_dict[device_ip],PeerAS=peer,LocalAS=local)
                          if result.ok or result.status_code == 500:
                            received_count=received_count+1
                          else:
                            log.failure ("Failed to Configure BGP neighbor "+interface_ip_dict[device_ip]+"on "+device_name)
                      if device_count1 > non_leaf_count and device_count1 <=device_count:
                          result=swtch.createBGPv4Neighbor("",interface_ip_dict[device_ip],PeerAS=peer,LocalAS=local,RouteReflectorClient="True")
                          if result.ok or result.status_code == 500:
                            received_count=received_count+1
                          else:
                            log.failure ("Failed to Configure BGP neighbor "+interface_ip_dict[device_ip]+"on "+device_name)
            if need_count == received_count:
                log.success("BGP is configured successfully on "+device_name)
                c=c+1
    if c == len(list1):
        log.success("BGP is configured successfully")
        return True
    else:
        log.failure("BGP is not configured")
        return False                            

