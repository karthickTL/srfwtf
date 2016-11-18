#!/usr/bin/env python
'''
Created on 3-Nov-2016

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
#ID : ops_api_001
#Name :  Connect API
#API Feature details :
#1 "Connect" API Connects to the particular device.
'''

def Connect(device):
    device_name=Device_parser(device)
    device_Info=Get_deviceInfo(device_name)
    ip_address=device_Info[1]
    user=device_Info[2]
    password=device_Info[3]
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
            cmd='ssh-keygen -R ['+ip_address+']:'+port
            os.system(cmd)
            connectionInfo = pexpect.spawn('ssh -p '+port +' ' +user+'@'+ip_address,env={ "TERM": "xterm-mono" },maxread=50000 )
            expect = 7
            continue
    connectionInfo.sendline("")
    connectionInfo.expect( '>|#|\$' )
    return connectionInfo

'''
[API Documentation]
#ID : ops_api_002
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
#ID : ops_api_003
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



def CHECKPOINT(string,device_id=''):
    log.step("*** "+string)

def CASE(string,device_id=''):
    log.case("<<< "+string)




'''
[API Documentation]
#ID : ops_api_0018
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


def enablelldp(mode,fab_devices,csw_devices,asw_devices,fab=[],csw=[],asw=[]) :
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
    c=0
    for i in range(len(list1)) :
            device = list1[i]
            device_name=Device_parser(device)
            device_Info = Get_deviceInfo(device_name)
            ip_address = device_Info[1]
            swtch = FlexSwitch (ip_address, 8080)
            swtch.updateLLDPGlobal("default",Enable="True",TranmitInterval=30)
            var=showrun(list1[i],'LLDP','lldp enable')
            if var == "1":
                log.success("LLDP is enabled on "+device_name)
                c=c+1
     
    if c==len(list1):
        log.success("LLDP is enabled")
        return True
    else:
        log.success("LLDP is not enabled")
        return False        



def statedown(mode,fab_devices,csw_devices,asw_devices,fab=[],csw=[],asw=[],interface_dict={}) :
    list1=[]
    log.info("Making the interfaces state DOWN")
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
            device = list1[i]
            device_name=Device_parser(device)
            device_Info = Get_deviceInfo(device_name)
            ip_address = device_Info[1]
            swtch = FlexSwitch (ip_address, 8080)  # Instantiate object to talk to flexSwitch
            for j in range(len(list1)):
                if device != list1[j] :
                    device_interface=device+"_"+list1[j]+"_eth"    
                    if device_interface in interface_dict.keys():
                        create_IPv4Intf=swtch.updatePort(interface_dict[device_interface],AdminState='DOWN')
                        
                        #print json.dumps(create_IPv4Intf)


def stateup(mode,fab_devices,csw_devices,asw_devices,fab=[],csw=[],asw=[],interface_dict={}) :
    list1=[]
    log.info("Making the interfaces state UP")
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
            device_Info = Get_deviceInfo(device_name)
            ip_address = device_Info[1]
            connectionInfo=Connect(device)
            connectionInfo.sendline("snap_cli")
            connectionInfo.expect(">")
            connectionInfo.sendline("enable")  
            connectionInfo.expect("#")
            connectionInfo.sendline("config")  
            connectionInfo.expect("#")
            for j in range(len(list1)):
                if device != list1[j] :
                    device_interface=device+"_"+list1[j]+"_eth"    
                    if device_interface in interface_dict.keys():
     
                        eth = interface_dict[device_interface]
                        port.append(eth)
                        eth = eth[:3] + ' ' + eth[3:]
                        connectionInfo.sendline("interface "+eth)  
                        connectionInfo.expect("#")
                        connectionInfo.sendline("no shutdown")  
                        connectionInfo.expect("#")          
                        connectionInfo.sendline("apply")  
                        connectionInfo.expect("#")
                        


def showrun(device,dec,string):
        count=0
        device_name=Device_parser(device)
        connectionInfo=Connect(device)
        connectionInfo.sendline("snap_cli")
        connectionInfo.expect(">")
        connectionInfo.sendline("enable")  
        connectionInfo.expect("#")
        connectionInfo.sendline("show run")  
        connectionInfo.expect("#")
        result= connectionInfo.before         
        log.details(result)
        fd = open("sample.txt","w+")
        fd.write(result)
        fd.close()
        f = open("sample.txt","r") 
        line = f.readlines()
        for eachline in line:
            if string in eachline:
                count= count+1
        os.remove("sample.txt")
        if count == 1:
            return "1"
             
   
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
            log.info("configuring Hostname on "+device_name)
            connectionInfo=Connect(device)
            connectionInfo.sendline(hostname[list1[i]])
            connectionInfo.expect("#")
            
            
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
                key = sheet.cell(row_index, col_index).value
                if sheet.cell(row_index, col_index).value not in device:
                    device.append(sheet.cell(row_index, col_index).value)
            if keys[col_index]=='Port1':
                value = sheet.cell(row_index, col_index).value
                dictionary[str(key)] = str(value)
            if keys[col_index]=='Port2': 
                value = sheet.cell(row_index, col_index).value
                dictionary[str(key)] = str(value) 
                li.append(dictionary)
                dictionary={}
    return li          
            
def lldpNeighborInfo(mode,path,sheet_name,fab_devices,csw_devices,asw_devices,devices=[],fab=[],csw=[],asw=[],interface_dict={}):
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
                           if devicename in str(lldp_s) and destination_devicename in str(lldp_s):
                                 if neighborportid == lldp_s[destination_devicename] and portid == lldp_s[devicename]:
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
                               if devicename in str(lldp_s) and destination_devicename in str(lldp_s):
                                 if neighborportid == lldp_s[destination_devicename] and portid == lldp_s[devicename] and dest_name == destination_devicename :
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

                        
            
            
            

 
