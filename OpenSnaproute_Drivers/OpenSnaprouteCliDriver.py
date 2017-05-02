#!/usr/bin/env python
"""
Created on 20-Nov-2016

Author: Terralogic team

OpenSnaprouteCliDriver is the basic driver which will handle the OpenSnaproute functions.

"""

import io
import sys
import os
import re
import ast
import pxssh
import getpass
import time
import string
import xmldict
import pexpect
import testfail
import xlrd
import simplejson as json
import logger as log
from robot.libraries.BuiltIn import BuiltIn
from flexswitchV2 import FlexSwitch
from flexprintV2 import FlexSwitchShow
sys.path.append(os.path.abspath('../../py'))
global step


def checkpoint(string_value, device_id=''):
    """
    Print the Checkpoint
    """
    log.step("*** %s" % string_value)


def device_parser(device=""):
    """
    Gets the device details
    """
    xml = open('OpenSnaproute.params').read()
    parsed_info = xmldict.xml_to_dict(xml)
    if device != "":
        device = str(device)
        device_name = parsed_info['TestCase']['Device'][device]
        return device_name
    else:
        device_name = parsed_info['TestCase']['Device']
        return device_name


def get_device_info(device):
    """
    Returns the information of the particular device
    """
    device_param = open('device.params').read()
    device_info = device_param.splitlines()
    for value in device_info:
        pattern = device
        match = re.search(pattern, value)
        if match:
            device_list = value.split(',')
            return device_list


def assign_ip(mode, fab_devices, csw_devices, asw_devices, subnet, fab=None, csw=None, asw=None, interface_dict=None, interface_ip_dict=None):
    """
    Assigns the IPv4 address to the routers using SDK function
    """
    list1 = []
    count = 0
    if mode == "no":
        for i in range(0, int(fab_devices)):
            list1.append(fab[i])
        for i in range(0, int(csw_devices)):
            list1.append(csw[i])
        for i in range(0, int(asw_devices)):
            list1.append(asw[i])
    if mode == "yes":
        for i in fab:
            list1.append(i)
        for i in csw:
            list1.append(i)
        for i in asw:
            list1.append(i)
    if mode == "yes" or mode =="no":
        for i in range(len(list1)):
            need_count = 0
            received_count = 0
            device = list1[i]
            device_name = device_parser(device)
            log.info("login to %s and configure IP address" % device_name)
            device_info = get_device_info(device_name)

            ip_address = device_info[1]
            switch = FlexSwitch(ip_address, 8080)   # Instantiate object to talk to flexSwitch
            for j in range(len(list1)):
                if device != list1[j]:
                    device_ip = "%s_%s_interface_ip" % (device, list1[j])
                    device_interface = "%s_%s_eth" % (device, list1[j])
                    if device_ip in interface_ip_dict.keys() and device_interface in interface_dict.keys():
                        need_count += 1
                        result = switch.create_ipv4_intf(interface_dict[device_interface], interface_ip_dict[device_ip] + subnet, admin_state='UP')
                        if result.ok or result.status_code == 500:
                            received_count += 1
                        else:
                            log.failure("Failed to Configure IP %s on %s" % (interface_dict[device_interface], device_name))
            if need_count == received_count:
                log.success("IP configured successfully on %s" % device_name)
                count += 1

    if count == len(list1):
        log.success("IP is configured successfully")
        return True
    else:
        log.failure("IP is not configured")
        return False


def remove_ip(mode, fab_devices, csw_devices, asw_devices, subnet, fab=None, csw=None, asw=None, interface_dict=None, interface_ip_dict=None):
    """
    Deletes the interfaces and IPv4 address from the routers using SDK function
    """
    list1 = []
    count = 0
    if mode == "no":
        for i in range(0, int(fab_devices)):
            list1.append(fab[i])
        for i in range(0, int(csw_devices)):
            list1.append(csw[i])
        for i in range(0, int(asw_devices)):
            list1.append(asw[i])
    if mode == "yes":
        for i in fab:
            list1.append(i)
        for i in csw:
            list1.append(i)
        for i in asw:
            list1.append(i)
    if mode == "yes" or mode == "no":
        for i in range(len(list1)):
            need_count = 0
            received_count = 0
            device = list1[i]
            device_name = device_parser(device)
            log.info("login to %s and remove IP address" % device_name)
            device_info = get_device_info(device_name)
            ip_address = device_info[1]
            switch = FlexSwitch(ip_address, 8080)  # Instantiate object to talk to flexSwitch
            for j in range(len(list1)):
                if device != list1[j]:
                    device_ip = "%s_%s_interface_ip" % (device, list1[j])
                    device_interface = "%s_%s_eth" % (device, list1[j])
                    if device_ip in interface_ip_dict.keys() and device_interface in interface_dict.keys():
                        need_count += 1
                        delete_ipv4_intf = switch.delete_ipv4_intf(interface_dict[device_interface])
                        if delete_ipv4_intf.status_code == 410:
                            received_count += 1
                        else:
                            log.failure("Failed to delete IP %s on %s" % (interface_dict[device_interface], device_name))
            if need_count == received_count:
                log.success("IP removed successfully on %s" % device_name)
                count += 1
    if count == len(list1):
        log.success("IP removed successfully")
        return True
    else:
        log.failure("IP not removed ")
        return False


def assign_bgp(mode, fab_devices, csw_devices, asw_devices, fab=None, csw=None, asw=None, interface_ip_dict=None, asnum=None, router_id=None):
    """
    Assigns the BGP IPv4 address to the routers using SDK function
    """
    list1 = []
    count = 0
    if mode == "no":
        for i in range(0, int(fab_devices)):
            list1.append(fab[i])
        for i in range(0, int(csw_devices)):
            list1.append(csw[i])
        for i in range(0, int(asw_devices)):
            list1.append(asw[i])
    if mode == "yes":
        for i in fab:
            list1.append(i)
        for i in csw:
            list1.append(i)
        for i in asw:
            list1.append(i)
    if mode == "yes" or mode == "no":
        for i in range(len(list1)):
            need_count = 0
            received_count = 0
            device = list1[i]
            device_name = device_parser(device)
            device_info = get_device_info(device_name)
            log.info("log-in to %s and loading BGP configuration" % device_name)
            ip_address = device_info[1]
            switch = FlexSwitch(ip_address, 8080)  # Instantiate object to talk to flexSwitch
            local = asnum[device]
            router_id_val = router_id[device]
            switch.update_bgp_global("default", asnum=local, router_id=router_id_val)
            for j in range(len(list1)):
                peer = asnum[list1[j]]
                if device != list1[j]:
                    device_ip = "%s_%s_interface_ip" % (list1[j], device)
                    if device_ip in interface_ip_dict.keys():
                        need_count += 1
                        result = switch.create_bgpv4_neighbor("", interface_ip_dict[device_ip], peer_as=peer, local_as=local)
                        if result.ok or result.status_code == 500:
                            received_count += 1
                        else:
                            log.failure("Failed to Configure BGP neighbor %s on %s" % (interface_ip_dict[device_ip], device_name))
            if need_count == received_count:
                log.success("BGP is configured successfully on %s " % device_name)
                count += 1

    if count == len(list1):
        log.success("BGP is configured successfully")
        return True
    else:
        log.failure("BGP is not configured")
        return False


def remove_bgp(mode, fab_devices, csw_devices, asw_devices, fab=None, csw=None, asw=None, interface_ip_dict=None, asnum=None, router_id=None):
    """
    Removes the bgp IPv4 neighbor address from the routers using SDK function
    """

    list1 = []
    count = 0
    if mode == "no":
        for i in range(0, int(fab_devices)):
            list1.append(fab[i])
        for i in range(0, int(csw_devices)):
            list1.append(csw[i])
        for i in range(0, int(asw_devices)):
            list1.append(asw[i])
    if mode == "yes":
        for i in fab:
            list1.append(i)
        for i in csw:
            list1.append(i)
        for i in asw:
            list1.append(i)
    if mode == "yes" or mode == "no":
        for i in range(len(list1)):
            need_count = 0
            received_count = 0
            device = list1[i]
            device_name = device_parser(device)
            device_info = get_device_info(device_name)
            ip_address = device_info[1]
            log.info("log-in to %s and removing BGP configuration" % device_name)
            switch = FlexSwitch(ip_address, 8080)  # Instantiate object to talk to flexSwitch
            for j in range(len(list1)):
                if device != list1[j]:
                    device_ip = "%s_%s_interface_ip" % (list1[j], device)
                    if device_ip in interface_ip_dict.keys():
                        need_count += 1
                        remove_bgpv4_neighbor = switch.delete_bgpv4_neighbor("", interface_ip_dict[device_ip])

                        if remove_bgpv4_neighbor.status_code == 410:
                            received_count += 1
                        else:
                            log.failure("Failed to remove BGP neighbor %s on %s" % (interface_ip_dict[device_ip], device_name))
            if need_count == received_count:
                count += 1
                log.success("BGP is removed successfully on %s" % device_name)

    if count == len(list1):
        log.success("BGP is removed successfully")
        return True
    else:
        log.failure("BGP is not removed ")
        return False


def create_policy_condition_name(mode, fab_devices, csw_devices, asw_devices, fab=None, csw=None, asw=None, condition_name='', condition_type='', protocol='', ip_prefix='', mask_length_range='', prefix_set=''):
    """
    configures Policy condition
    """
    list1 = []
    if mode == "no":
        for i in range(0, int(fab_devices)):
            list1.append(fab[i])
        for i in range(0, int(csw_devices)):
            list1.append(csw[i])
        for i in range(0, int(asw_devices)):
            list1.append(asw[i])
    if mode == "yes":
        for i in fab:
            list1.append(i)
        for i in csw:
            list1.append(i)
        for i in asw:
            list1.append(i)
    count = 0
    for i in range(len(list1)):
        device = list1[i]
        device_name = device_parser(device)
        log.info("Loading into %s" % device_name)
        device_info = get_device_info(device_name)
        ip_address = device_info[1]
        switch = FlexSwitch(ip_address, 8080)
        # switch1 = FlexSwitchShow(ip_address, 8080)
        result = switch.create_policy_condition(condition_name, condition_type, protocol, ip_prefix, mask_length_range, prefix_set)
        if result.ok or result.status_code == 500:
            log.success("Policy Condition is created and verified on %s" % device_name)
            count += 1
        else:
            log.failure("Policy Condition is not created properly on %s" % device_name)
    if count == len(list1):
        log.success("Policy Condition is created ")
        return True
    else:
        log.failure(" Policy Condition is not created ")
        return False


def create_policy_statement(mode, fab_devices, csw_devices, asw_devices, fab=None, csw=None, asw=None, stmt_name='', condition_name='', action='', match_conditions=''):
    """
    Configures Policy statement
    """
    list1 = []
    count = 0
    if mode == "no":
        for i in range(0, int(fab_devices)):
            list1.append(fab[i])
        for i in range(0, int(csw_devices)):
            list1.append(csw[i])
        for i in range(0, int(asw_devices)):
            list1.append(asw[i])
    if mode == "yes":
        for i in fab:
            list1.append(i)
        for i in csw:
            list1.append(i)
        for i in asw:
            list1.append(i)
    cond_name = [condition_name]
    for i in range(len(list1)):
        device = list1[i]
        device_name = device_parser(device)
        log.info("Loading into %s" % device_name)
        device_info = get_device_info(device_name)
        ip_address = device_info[1]
        switch = FlexSwitch(ip_address, 8080)
        result = switch.create_policy_stmt(name=stmt_name, conditions=cond_name, action=action, match_conditions=match_conditions)
        if result.ok or result.status_code == 500:
            log.success("Policy statement is created and verified on %s" % device_name)
            count += 1
        else:
            log.failure("Policy statement is not created properly on %s" % device_name)
    if count == len(list1):
        log.success("Policy statement is created ")
        return True
    else:
        log.failure(" Policy statement is not created ")
        return False


def create_policy_definitions(mode, fab_devices, csw_devices, asw_devices, fab=None, csw=None, asw=None, stmt_name='', pol_def_name='', priority='', match_type='', policy_type=''):
    """
    Configures Policy Definition
    """
    list1 = []
    if mode == "no":
        for i in range(0, int(fab_devices)):
            list1.append(fab[i])
        for i in range(0, int(csw_devices)):
            list1.append(csw[i])
        for i in range(0, int(asw_devices)):
            list1.append(asw[i])
    if mode == "yes":
        for i in fab:
            list1.append(i)
        for i in csw:
            list1.append(i)
        for i in asw:
            list1.append(i)
    count = 0
    stmt_list = [{"Priority": int(priority), "Statement": str(stmt_name)}]
    for i in range(len(list1)):
        device = list1[i]
        device_name = device_parser(device)
        log.info("Loading into %s " % device_name)
        device_info = get_device_info(device_name)
        ip_address = device_info[1]
        switch = FlexSwitch(ip_address, 8080)
        result = switch.create_policy_definition(str(pol_def_name), int(priority), stmt_list, match_type=str(match_type), policy_type=policy_type)
        if result.ok or result.status_code == 500:
            log.success("Policy Definitions is created and verified on %s" % device_name)
            count += 1
        else:
            log.failure("Policy Definitions is not created properly on %s" % device_name)
    if count == len(list1):
        log.success("Policy Definitions is created ")
        return True
    else:
        log.failure(" Policy Definitions is not created ")
        return False


def flap_state(mode, fab_devices, csw_devices, asw_devices, fab=None, csw=None, asw=None, interface_dict=None):
    """
    Makes interface state UP and Down
    """
    list1 = []
    if mode == "no":
        for i in range(0, int(fab_devices)):
            list1.append(fab[i])
        for i in range(0, int(csw_devices)):
            list1.append(csw[i])
        for i in range(0, int(asw_devices)):
            list1.append(asw[i])
    if mode == "yes":
        for i in fab:
            list1.append(i)
        for i in csw:
            list1.append(i)
        for i in asw:
            list1.append(i)
    need_count = 0
    received_count = 0
    count = 0
    for i in range(len(list1)):
        device = list1[i]
        device_name = device_parser(device)
        device_info = get_device_info(device_name)
        ip_address = device_info[1]
        switch = FlexSwitch(ip_address, 8080)  # Instantiate object to talk to flexSwitch
        for j in range(len(list1)):
            if device != list1[j]:
                device_interface = "%s_%s_eth" % (device, list1[j])
                if device_interface in interface_dict.keys():
                    need_count += 1
                    result = switch.update_port(interface_dict[device_interface], admin_state='DOWN')
                    if result.ok or result.status_code == 500:
                        log.info("Setting %s DOWN" % interface_dict[device_interface])
                        count += 1
                    time.sleep(1)
                    result = switch.update_port(interface_dict[device_interface], admin_state='UP')
                    if result.ok or result.status_code == 500:
                        log.info("Setting %s UP" % interface_dict[device_interface])
                        received_count += 1
    if need_count == received_count and need_count == count and count == received_count:
        log.success("flap state is done")
        return True
    else:
        log.failure("flap state is not done")
        return False


def create_bgp_global(mode, fab_devices, csw_devices, asw_devices, fab=None, csw=None, asw=None, asnum=None, router_id=None, redistribution='', pol_name=''):
    """
    Creates BGP global functionality
    """
    list1 = []
    count = 0
    redistribute = []
    if mode == "no":
        for i in range(0, int(fab_devices)):
            list1.append(fab[i])
        for i in range(0, int(csw_devices)):
            list1.append(csw[i])
        for i in range(0, int(asw_devices)):
            list1.append(asw[i])
    if mode == "yes":
        for i in fab:
            list1.append(i)
        for i in csw:
            list1.append(i)
        for i in asw:
            list1.append(i)
    if redistribution != '':
        redistribute = [{"Sources": redistribution, "Policy": pol_name}]
    for i in range(len(list1)):
        device = list1[i]
        device_name = device_parser(device)
        device_info = get_device_info(device_name)
        ip_address = device_info[1]
        switch = FlexSwitch(ip_address, 8080)  # Instantiate object to talk to flexSwitch
        local = asnum[device]
        router_id_val = router_id[device]
        log.info("log-in to %s and configuring router" % device_name)
        result = switch.update_bgp_global("default", asnum=local, router_id=router_id_val, redistribution=redistribute)
        if result.ok or result.status_code == 500:
            count += 1
            log.success("router is configured on %s" % device_name)
        else:
            log.failure("Failed to Configure router on %s" % device_name)
    if count == len(list1):
        log.success("router is configured")
        return True
    else:
        log.info("Failed to Configure")
        return False


def neighbor_state_all(state_value, mode, fab_devices, csw_devices, asw_devices, fab=None, csw=None, asw=None, interface_ip_dict=None):
    """
    Checks the neighbor state in all devices
    """
    list1 = []
    if mode == "no":
        for i in range(0, int(fab_devices)):
            list1.append(fab[i])
        for i in range(0, int(csw_devices)):
            list1.append(csw[i])
        for i in range(0, int(asw_devices)):
            list1.append(asw[i])
    if mode == "yes":
        for i in fab:
            list1.append(i)
        for i in csw:
            list1.append(i)
        for i in asw:
            list1.append(i)
    device_count = 0
    for i in list1:
        device = i
        device_name = device_parser(device)
        log.step("Checking for %s in %s" % (state_value, device_name))
        log.info("Log-in into %s to check for %s state" % (device_name, state_value))
        device_name = device_parser(device)
        device_info = get_device_info(device_name)
        ip_address = device_info[1]
        switch = FlexSwitch(ip_address, 8080)
        output = switch.get_all_bgpv4_neighbor_states()
        log.details(output)
        rec_count = 0
        dev_count = 0
        list2 = []
        flag = 0
        for eachline in output:
            for j in range(len(list1)):
                if device != list1[j]:
                    dev_count = dev_count+1
                    device_ip = "%s_%s_interface_ip" % (list1[j], device)
                    if device_ip in interface_ip_dict.keys():
                        if list1[j] not in list2:
                            list2.append(list1[j])
                        ip_actual = interface_ip_dict[device_ip]
                        ip_actual = "'%s'" % ip_actual
                        if ip_actual in str(eachline) and "'SessionState': 6" in str(eachline):
                            rec_count += 1
                            flag = 1
                            break
        if rec_count == len(list2) and flag == 1:
            log.success("Required %s state is achieved in %s" % (state_value, device_name))
            device_count += 1
        else:
            log.failure("Required %s state is not achieved on %s" % (state_value, device_name))
    if device_count == len(list1):
        log.success("Neighborship is get %s state on all devices" % state_value)
        return True
    else:
        log.failure("Neighborship is not get %s state on all devices" % state_value)
        return False


def device_neighbor_check(state_value, source_device, destination_device, interface_ip_dict=None):
    """
    Checks the  neighbor state in a particular device
    """
    log.step("Checking for %s in %s" % (state_value, device_parser(source_device)))
    log.info("Log-in into %s to check for %s state" % (device_parser(source_device), state_value))
    device_name = device_parser(source_device)
    log.step("Checking for %s in %s" % (state_value, device_name))
    log.info("Log-in into %s to check for %s state" % (device_name, state_value))
    device_name = device_parser(source_device)
    device_info = get_device_info(device_name)
    ip_address = device_info[1]
    switch = FlexSwitch(ip_address, 8080)
    output = switch.get_all_bgpv4_neighbor_states()
    log.details(output)
    flag = 0
    device_ip = "%s_%s_interface_ip" % (destination_device, source_device)
    ip_actual = interface_ip_dict[device_ip]
    ip_actual = "'%s'" % ip_actual
    for eachline in output:
        if state_value == 'Estab':
            if ip_actual in str(eachline) and "'SessionState': 6" in str(eachline):
                flag = 1
                break
        if state_value != 'Estab':
            if ip_actual in str(eachline) and "'SessionState': 6" not in str(eachline):
                flag = 1
                break
    if flag == 1:
        log.success("neighbor ip %s is in % state" % (ip_actual, state_value))
        return True
    else:
        log.failure("neighbor ip %s is not in % state" % (ip_actual, state_value))
        return False


def trigger(device, ip, interface_ip_dict=None, interface_dict=None):
    """
    Triggers the Link failure
    """
    device_name = device_parser(device)
    device_info = get_device_info(device_name)
    ip_address = device_info[1]
    port = []
    flag = 1
    count = 0
    log.info("trigger link failure is verifying on %s for the address %s" % (device_name, ip))
    switch = FlexSwitch(ip_address, 8080)
    while flag == 1:
        result = bestpath(switch, ip)
        log.details(result)
        pattern = r"[\{u'A-z:, \s*0-9./+\}-]*NextHopIntRef':\s*u'(\w+)[', \s*u'A-z:0-9]*Ip':\s*u'(\d+.\d+.\d+.\d+).*"
        match = re.match(pattern, str(result))
        if match:
            add = match.group(1)
            log.info("BestPath port: %s" % add)
            eth = match.group(1)
            state(device, eth, state_value="DOWN")
            time.sleep(5)
            port.append(eth)
            count = count+1
        else:
            flag = 0
            log.info("No bestpath found")
            log.info("bringing up all the shut down interfaces")
            for i in range(0, len(port)):
                    state(device, port[i], state_value='UP')

    if count > 1:
        log.success("Trigger Link Failure is verified")
        return True
    else:
        log.failure("No Best/alternate Path Found")
        return False


def bestpath(switch, ip):
    """
    Finds the Best path
    """

    result = switch.get_ipv4_route_state(ip)
    if result.ok:
        return result.json()
    else:
        return 0


def loopback(mode, device, loopback_name, ip, subnet):
    """
    Creates or removes loopback interface
    """
    device_name = device_parser(device)
    device_info = get_device_info(device_name)
    ip_address = device_info[1]
    if mode == 'config':
        log.info("Creating Logical address on  %s" % device_name)
        switch = FlexSwitch(ip_address, 8080)
        result = switch.create_logical_intf(loopback_name)
        if result.ok or result.status_code == 500:
            result = switch.create_ipv4_intf(loopback_name, ip + subnet)
            if result.ok or result.status_code == 500:
                log.success("logical interface is created on %s" % device_name)
                return True
            else:
                log.failure("logical interface is not created")
                return False
        else:
            log.failure("logical interface is not created")
            return False
    if mode == 'remove':
        log.info("Removing Logical address on  %s" % device_name)
        switch = FlexSwitch(ip_address, 8080)
        result = switch.delete_ipv4_intf(loopback_name)
        if result.status_code == 410:
            result = switch.delete_logical_intf(loopback_name)
            if result.status_code == 410:
                log.success("logical interface is removed on  %s" % device_name)
                return True
            else:
                log.failure("logical interface is not created")
                return False
    else:
        log.failure("logical interface is not created")
        return False


def reset_bgp_neighbor(device, ip):
    """
    Resets/clears the BGP with IP address
    """

    device_name = device_parser(device)
    device_info = get_device_info(device_name)
    ip_address = device_info[1]
    log.info("Reset/clear BGP process on  %s" % device_name)
    switch = FlexSwitch(ip_address, 8080)
    result = switch.reset_bgpv4_neighbor_by_ip_addr(ip)
    if result.ok:
        log.success("BGP process reseted on  %s" % device_name)
        return True
    else:
        log.failure("BGP Process no reseted")
        return False


def best_ip(device, ip, interface_ip_dict=None, interface_dict=None):
    """
    Gives the best path ip
    """
    device_name = device_parser(device)
    device_info = get_device_info(device_name)
    ip_address = device_info[1]
    log.info("Checking for best path port on  %s for the address %s" % (device_name, ip))
    switch = FlexSwitch(ip_address, 8080)
    result = bestpath(switch, ip)
    if result:
        pattern = r"[\{u'A-z:, \s*0-9./+\}-]*NextHopIntRef':\s*u'(\w+)[', \s*u'A-z:0-9]*Ip':\s*u'(\d+.\d+.\d+.\d+).*"
        match = re.match(pattern, str(result))
        if match:
            log.success("best path %s" % match.group(2))
            return True
    else:
        log.failure("no best path found")
        return False


def state(device, port, state_value=''):
    """
    Makes interface state UP and Down
    """
    device_name = device_parser(device)
    device_info = get_device_info(device_name)
    ip_address = device_info[1]
    switch = FlexSwitch(ip_address, 8080)
    if state_value == "DOWN":
        log.info("shutdown the interface %s on %s" %(port, device_name))
        result = switch.update_port(port, admin_state='DOWN')
        if result.ok or result.status_code == 500:
            log.success("port %s is down" % port)
            return True
        else:
            log.failure("Fail to set port %s to down state" % port)
            return False
    if state_value == "UP":
        log.info("Making the interface %s  UP on %s " % (port, device_name))
        result = switch.update_port(port, admin_state='UP')
        if result.ok or result.status_code == 500:
            log.success("port %s is up" % port)
            return True
        else:
            log.failure("Fail to set port %s  to up state" % port)
            return False


def connect(device):
    """
    Establishes connection to the device
    """
    try:
        device_name = device_parser(device)
        device_info = get_device_info(device_name)
        ip_address = device_info[1]
        port = device_info[2]
        user = device_info[3]
        password = device_info[4]
        s.login (ip_address, user, password)
        return s
    except pxssh.ExceptionPxssh, e:
        log.info( "pxssh failed on login.")

"""
def connect(device):

    device_name = device_parser(device)
    device_info = get_device_info(device_name)
    ip_address = device_info[1]
    port = device_info[2]
    user = device_info[3]
    password = device_info[4]
    log.info(ip_address)
    refused = "ssh: connect to host %s port 22: Connection refused" % ip_address
    child=pexpect.spawn("ssh %s@%s" % (user, ip_address))
    child.expect('password:')     # put in the prompt you expect after sending SSH
    child.sendline('root')
    child.expect('#')
    child.sendline(' ')
    child.expect('#')
    child.sendline('\n ping 10.0.5.1 -c 5 ')
    child.expect('#')
    log.info(child.before)
    log.info("11111111111111111111111111111111111")                     
    return child



def connect(device):

    Establishes connection to the device

    device_name = device_parser(device)
    device_info = get_device_info(device_name)
    ip_address = device_info[1]
    port = device_info[2]
    user = device_info[3]
    password = device_info[4]
    refused = "ssh: connect to host %s port 22: Connection refused" % ip_address
    connection_info = pexpect.spawn("ssh %s@%s" % (user, ip_address))
    expect = 7
    while expect == 7:
        expect = connection_info.expect(["Are you sure you want to continue connecting", "password:", pexpect.EOF, pexpect.TIMEOUT, refused, '>|#|$', "Host key verification failed."], 120)
        expect = 1
        if expect == 0:   # Accept key, then expect either a password prompt or access
            connection_info.sendline('yes')
            expect = 7   # Run the loop again
            continue
        if expect == 1:   # Password required
            log.info("###########################################################")
            connection_info.sendline(password)
            connection_info.expect('>|#|$')
            if not connection_info.expect:
                log.failure("Password for %s is incorrect" % device_name)
                raise testfail.TestFailed("Password for %s is incorrect" % device_name)
        elif expect == 2:
            log.failure("End of File Encountered while Connecting %s" % device_name)
            raise testfail.TestFailed("End of File Encountered while Connecting %s " % device_name)
        elif expect == 3:   # timeout
            log.failure("Timeout of the session encountered while connecting")
            raise testfail.TestFailed("Timeout of the session encountered")
        elif expect == 4:
            log.failure("Connection to %s refudes" % device_name)
            raise testfail.TestFailed("Connection to '%s refused" % device_name)
        elif expect == 5:
            pass
        elif expect == 6:
            # cmd='ssh-keygen -R ['+ip_address+']:'+port
            cmd = 'ssh-keygen -f "/home/naveen/.ssh/known_hosts" -R ' + ip_address
            os.system(cmd)
            connection_info = pexpect.spawn("ssh -p %s %s@%s" % (port, user, ip_address), env={"TERM": "xterm-mono"}, maxread=50000)
            expect = 7
            continue
        connection_info.expect('>|#|$')
        connection_info.sendline("ping 10.0.5.1 -c 5")
        connection_info.expect('>|#|$')
        log.info(connection_info.before)
    return connection_info

"""
def case(string_value, device_id=''):
    """
    Print the CASE info
    """
    log.case("<<< %s" % string_value)


def delay(delay_value='', message=''):
    """
    Makes the process wait for the Specified time.
    delay  15  please wait for 60 seconds then check for BGP "state: Established"
    """
    if time != '':
        log.info(message)
        time.sleep(int(delay_value))
        return True
    else:
        return False


def get_testcase_params(testcase="", test=""):
    """
    Gets the prarameters_details for a particular testcase
    """
    testcase = str(testcase)
    if test == "":
        xml = open('OpenSnaproute.params').read()
        tc_list = xmldict.xml_to_dict(xml)
        testcase_info = tc_list['TestCase'][testcase]
        return testcase_info
    elif test != "":
        xml = open('OpenSnaproute.params').read()
        tc_list = xmldict.xml_to_dict(xml)
        test_values = tc_list['TestCase'][testcase][test]
        return test_values


def parse_device(device=""):
    """
    Parses the params file and fetches the Device information in a dictionary format
    """
    xml = open('OpenSnaproute.params').read()
    parsed_info = xmldict.xml_to_dict(xml)
    if device != "":
        device = str(device)
        device_name = parsed_info['TestCase']['Device'][device]
        return device_name
    else:
        device_name = parsed_info['TestCase']['Device']
        return device_name


def enable_lldp(mode, fab_devices, csw_devices, asw_devices, fab=None, csw=None, asw=None):
    """
    "Enables the LLDP Globally
    """
    list1 = []
    count = 0
    if mode == "no":
        for i in range(0, int(fab_devices)):
            list1.append(fab[i])
        for i in range(0, int(csw_devices)):
            list1.append(csw[i])
        for i in range(0, int(asw_devices)):
            list1.append(asw[i])
    if mode == "yes":
        for i in fab:
            list1.append(i)
        for i in csw:
            list1.append(i)
        for i in asw:
            list1.append(i)
    for i in range(len(list1)):
        device = list1[i]
        device_name = device_parser(device)
        device_info = get_device_info(device_name)
        log.info("Log-in to %s to enable LLDP" % device_name)
        ip_address = device_info[1]
        switch = FlexSwitch(ip_address, 8080)
        result = switch.update_lldp_global("default", enable="True", tranmit_interval=30)
        if result.ok or result.status_code == 500:
            log.success("LLDP is enabled on %s" % device_name)
            count += 1

    if count == len(list1):
        log.success("LLDP is enabled")
        return True
    else:
        log.failure("LLDP is not enabled")
        return False


def lldp_neighbor_info(mode, fab_devices, csw_devices, asw_devices, devices=None, fab=None, csw=None, asw=None, interface_dict=None):
    """
    verifies the LLDP neighbour information.
    """
    result_list = []
    if mode == 'yes':
        for device in devices:
            device_name = device_parser(device)
            device_info = get_device_info(device_name)
            ip_address = device_info[1]
            switch = FlexSwitchShow(ip_address, 8080)
            test_name = BuiltIn().get_variable_value("${TEST_NAME}")
            device_name = parse_device(device)
            device_params = get_testcase_params(test_name, device_name)
            log.step("Checking LLDP Neighbor Information For The Device: %s" % device_name)
            lldp_dict = ast.literal_eval(device_params)
            result = switch.print_lldp_intf_states()
            log.details(result)
            fd = open("sample.txt", "w+")
            fd.write(result)
            fd.close()
            f = open("sample.txt", "r")
            j = 0
            count = 0
            line = f.readlines()
            for eachline in line:
                pattern1 = r'\s*([A-z0-9]*)\s*\d*\s*\d*\s*\d*\s*True\s*([A-z0-9]*)\s*[A-z0-9:]*\s*([A-z0-9]*)\s*([A-z0-9]*).*'
                match = re.match(pattern1, eachline)
                if match:
                    neighbor_port_id = match.group(3)
                    port_id = match.group(1)
                    dest1 = match.group(4).lower()
                    for loop in range(len(lldp_dict)):
                        source = lldp_dict[loop][j]
                        dest = lldp_dict[loop][j+1]
                        source_params = source.split(':')
                        dest_params = dest.split(':')
                        source_name = source_params[0]
                        source_port = source_params[1]
                        dest_name = dest_params[0]
                        dest_port = dest_params[1]
                        if source_port == port_id and dest_port == neighbor_port_id and dest_name.lower() == dest1:
                            log.info("port %s of %s Is connected to Port %s of %s" % (port_id, device_name, neighbor_port_id, dest1))
                            count += 1
                            break
            os.remove("sample.txt")
            if count == len(lldp_dict):
                log.success("LLDP Neighbor Information Matched With The Given Information\n")
                result_list.append("Pass")
            else:
                log.failure("LLDP Neighbor Information Does Not Matches With The Given Information\n")
                result_list.append("Fail")
            count = 0
            if "Fail" in result_list:
                raise testfail.TestFailed("LLDP neighbor information does not matches with the given information\n")

    if mode == 'no':
        list1 = []
        list2 = []
        rise = 0
        count = 0
        for i in range(0, int(fab_devices)):
            list1.append(fab[i])
        for i in range(0, int(csw_devices)):
            list1.append(csw[i])
        for i in range(0, int(asw_devices)):
            list1.append(asw[i])
        for i in range(0, len(list1)):
            device_n = list1[i]
            for device in list1:
                if device != device_n:
                    device_interface = "%s_%s_eth" % (device_n, device)
                    if device_interface in interface_dict.keys():
                        list2.append(device)
                        rise += 1
            device_name = device_parser(device_n)
            device_info = get_device_info(device_name)
            ip_address = device_info[1]
            switch = FlexSwitchShow(ip_address, 8080)
            test_name = BuiltIn().get_variable_value("${TEST_NAME}")
            device_name = parse_device(device_n)
            device_params = get_testcase_params(test_name, device_name)
            log.step("Checking LLDP Neighbor Information For The Device: %s" % device_name)
            lldp_dict = ast.literal_eval(device_params)
            result = switch.print_lldp_intf_states()
            log.details(result)
            fd = open("sample.txt", "w+")
            fd.write(result)
            fd.close()
            f = open("sample.txt", "r")
            line = f.readlines()
            for eachline in line:
                pattern1 = r'\s*([A-z0-9]*)\s*\d*\s*\d*\s*\d*\s*True\s*([A-z0-9]*)\s*[A-z0-9:]*\s*([A-z0-9]*)\s*([A-z0-9]*).*'
                match = re.match(pattern1, eachline)
                if match:
                    neighbor_port_id = match.group(3)
                    port_id = match.group(1)
                    dest1 = match.group(4)
                    dest1 = dest1.lower()
                for device in list2:
                    flag = 0
                    j = 0
                    dest_n = parse_device(device)
                    dest_n = dest_n.lower()
                    if match:
                        for loop in range(len(lldp_dict)):
                            source = lldp_dict[loop][j]
                            dest = lldp_dict[loop][j+1]
                            source_params = source.split(':')
                            dest_params = dest.split(':')
                            source_name = source_params[0]
                            source_port = source_params[1]
                            dest_name = dest_params[0]
                            dest_port = dest_params[1]
                            if source_port == port_id and dest_port == neighbor_port_id and dest_n == dest1.lower():
                                log.info("port %s of %s Is connected to Port %s od %s" %(port_id, device_name, neighbor_port_id, dest1))
                                count += 1
                                flag = 1
                                break
                    if flag == 1:
                        flag = 0
                        break
            if count == rise:
                log.success("LLDP Neighbor Information Matched With The Given Information\n")
                result_list.append("Pass")
            else:
                log.failure("LLDP Neighbor Information Does Not Matches With The Given Information\n")
                result_list.append("Fail")
            count = 0
            rise = 0
            list2 = []
        os.remove("sample.txt")
        if "Fail" in result_list:
            raise testfail.TestFailed("LLDP neighbor information does not matches with the given information\n")


def host(mode, fab_devices, csw_devices, asw_devices, fab=None, csw=None, asw=None, hostname=None):
    """
    Renames the host name
    """
    list1 = []
    if mode == "no":
        for i in range(0, int(fab_devices)):
            list1.append(fab[i])
        for i in range(0, int(csw_devices)):
            list1.append(csw[i])
        for i in range(0, int(asw_devices)):
            list1.append(asw[i])
    if mode == "yes":
        for i in fab:
            list1.append(i)
        for i in csw:
            list1.append(i)
        for i in asw:
            list1.append(i)
    for i in range(len(list1)):
        device = list1[i]
        device_name = device_parser(device)
        connection_info = connect(device)
        log.info("log into %s to specify Hostname" % device_name)
        connection_info.sendline(hostname[list1[i]])
        connection_info.expect("#")


def parse(path, sheet_name):
    """
    Parse the XL sheet for LLDP Testcase
    """
    workbook = xlrd.open_workbook(path)
    sheet = workbook.sheet_by_name(sheet_name)
    device = []
    list1 = []
    keys = [sheet.cell(0, col_index).value for col_index in xrange(sheet.ncols)]
    dictionary = {}
    column = 2
    # col = 1
    for row_index in  xrange(1, sheet.nrows):
        # cell = sheet.cell(row_index, col)
        if sheet.cell(row_index, column).value == '':
            continue
        for col_index in xrange(sheet.ncols):
            if keys[col_index] == 'Device2' or keys[col_index] == 'Device1':
                key = sheet.cell(row_index, col_index).value.lower()
                if sheet.cell(row_index, col_index).value not in device:
                    device.append(sheet.cell(row_index, col_index).value.lower())
            if keys[col_index] == 'Port1':
                value = sheet.cell(row_index, col_index).value
                dictionary[str(key)] = (str(value)).lower()
            if keys[col_index] == 'Port2':
                value = sheet.cell(row_index, col_index).value
                dictionary[str(key)] = (str(value)).lower()
                list1.append(dictionary)
                dictionary = {}
    return list1


def lldp_neighbor_info_v2(mode, path, sheet_name, fab_devices, csw_devices, asw_devices, devices=None, fab=None, csw=None, asw=None, interface_dict=None):
    """
    Verifies the LLDP neighbour information using XLsheet.
    """
    result_list = []
    lldp = parse(path, sheet_name)
    list1 = []
    if mode == "yes":
        for i in fab:
            list1.append(i)
        for i in csw:
            list1.append(i)
        for i in asw:
            list1.append(i)
        for i in range(0, len(list1)):
            device_n = list1[i]
            rise = 0
            for device in list1:
                if device != device_n:
                    device_interface = "%s_%s_eth" % (device_n, device)
                    if device_interface in interface_dict.keys():
                        rise += 1
            device_name = device_parser(device_n)
            device_info = get_device_info(device_name)
            ip_address = device_info[1]
            switch = FlexSwitchShow(ip_address, 8080)
            test_name = BuiltIn().get_variable_value("${TEST_NAME}")
            log.step("Checking LLDP Neighbor Information For The Device: %s" % device_name)
            result = switch.print_lldp_intf_states()
            log.details(result)
            fd = open("sample.txt", "w+")
            fd.write(result)
            fd.close()
            f = open("sample.txt", "r")
            count = 0
            line = f.readlines()
            for eachline in line:
                pattern1 = r'\s*([A-z0-9]*)\s*\d*\s*\d*\s*\d*\s*True\s*([A-z0-9]*)\s*[A-z0-9:]*\s*([A-z0-9]*)\s*([A-z0-9.]*)\s+[A-z0-9.]*\s+Flex'         
                match = re.match(pattern1, eachline)
                if match:
                    device_name = device_name.lower()
                    neighbor_portid = match.group(3)
                    portid = match.group(1)
                    destination = match.group(4)
                    destination_device = destination.lower()
                    for lldp_s in lldp:
                        if device_name in str(lldp_s) and destination_device in str(lldp_s):
                            if neighbor_portid == lldp_s[destination_device] and portid == lldp_s[device_name]:
                                log.info("port %s of %s is Connected to Port %s of %s" %(portid, device_name, neighbor_portid, destination_device))
                                count += 1
                                break
            if count == rise and count != 0:
                log.success("LLDP Neighbor Information Matched With The Given Information\n")
                result_list.append("Pass")
            else:
                log.failure("LLDP Neighbor Information Does Not Matches With The Given Information\n")
                result_list.append("Fail")
            count = 0
        if "Fail" in result_list:
            raise testfail.TestFailed("LLDP neighbor information does not matches with the given information\n")

    if mode == 'no':
        list1 = []
        list2 = []
        rise = 0
        count = 0
        for i in range(0, int(fab_devices)):
            list1.append(fab[i])
        for i in range(0, int(csw_devices)):
            list1.append(csw[i])
        for i in range(0, int(asw_devices)):
            list1.append(asw[i])
        for i in range(0, len(list1)):
            device_n = list1[i]
            for device in list1:
                if device != device_n:
                    device_interface = "%s_%s_eth" % (device_n, device)
                    if device_interface in interface_dict.keys():
                        list2.append(device)
                        rise += 1
            device_name = device_parser(device_n)
            device_info = get_device_info(device_name)
            ip_address = device_info[1]
            switch = FlexSwitchShow(ip_address, 8080)
            test_name = BuiltIn().get_variable_value("${TEST_NAME}")
            log.step("Checking LLDP Neighbor Information For The Device: %s" % device_name)
            result = switch.print_lldp_intf_states()
            log.details(result)
            fd = open("sample.txt", "w+")
            fd.write(result)
            fd.close()
            f = open("sample.txt", "r")
            line = f.readlines()
            device_name = device_name.lower()
            for eachline in line:
                pattern1 = r'\s*([A-z0-9]*)\s*\d*\s*\d*\s*\d*\s*True\s*([A-z0-9]*)\s*[A-z0-9:]*\s*([A-z0-9]*)\s*([A-z0-9.]*)\s+[A-z0-9.]*\s+Flex'
                match = re.match(pattern1, eachline)
                if match:
                    neighbor_portid = match.group(3)
                    portid = match.group(1)
                    destination = match.group(4)
                    destination_device = destination.lower()
                for device in list2:
                    flag = 0
                    dest_name = device_parser(device)
                    dest_name = dest_name.lower()
                    if match:
                        for lldp_s in lldp:
                            if device_name in str(lldp_s) and destination_device in str(lldp_s):
                                if neighbor_portid == lldp_s[destination_device] and portid == lldp_s[device_name] and dest_name.lower() == destination_device:
                                    log.info("port %s of %s is connected to port %s of %s" % (portid, device_name, neighbor_portid, destination_device))
                                    count += 1
                                    flag = 1
                                    break
                    if flag == 1:
                        flag = 0
                        break
            if count == rise and count != 0:
                log.success("LLDP Neighbor Information Matched With The Given Information\n")
                result_list.append("Pass")
            else:
                log.failure("LLDP Neighbor Information Does Not Matches With The Given Information\n")
                result_list.append("Fail")
            count = 0
            rise = 0
            list2 = []
        if "Fail" in result_list:
            raise testfail.TestFailed("LLDP neighbor information does not matches with the given information\n")


def static_route_configuration(device, dest_net, nexthop_ip, interface):
    """
    configures static route using SDK function
    """

    device_name = device_parser(device)
    device_info = get_device_info(device_name)
    ip_address = device_info[1]
    switch = FlexSwitch(ip_address, 8080)
    log.info("creating Static route on %s" % device_name)
    result = switch.create_ipv4_route(dest_net, "255.255.255.254", [{"NextHopIp": nexthop_ip}])
    if result.ok or result.status_code == 500:
        log.success("static route is configured")
        return True
    else:
        log.failure("Failed to Configure static route on %s" % device_name)
        return False


def ping(device_src, device_dest, dest_ip):
    """
    Tests the connectinity between source and destination devices
    """
    log.info("Checking reachability between %s and %s using PING" % (device_parser(device_src), device_parser(device_dest)))
    log.info("Logging into: %s" % device_parser(device_src))
    device_connect = connect(device_src)
    log.info("Device %s Log-in successful" % device_parser(device_src))
    log.info("start pinging from SOURCE-%s to DESTINATION-%s of IP- %s" % (device_parser(device_src), device_parser(device_dest), dest_ip))
    device_connect.sendline("ping %s -c 5" % dest_ip)
    device_connect.prompt()
    time.sleep(20)
    log.info(device_connect.before)
    ping_results = device_connect.before
    pat = r'\s*\d+\s+\w+\s+\w+,\s+\d+\s+\w+,\s+(\d+)%\s+packet loss'
    match = re.search(pat, ping_results)
    if match:
        packet_loss = match.group(1)
        log.info(packet_loss)
        if packet_loss == '0':
            log.success("PING Successful!!No Packet Loss")
            return True
        else:
            log.info("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            raise AssertionError("PING UNSUCCESSFUL")

    else:
        raise AssertionError("PING UNSUCCESSFUL")


def delete_peer_group(device, peer_group_id):
    """
    Deletes the peer group using SDK function
    """
    device_name = device_parser(device)
    device_info = get_device_info(device_name)
    ip_address = device_info[1]
    switch = FlexSwitch(ip_address, 8080)
    result = switch.delete_bgpv4_peer_group(peer_group_id)
    if result.status_code == 410:
        log.success("Peer-Group is removed in %s" % device_name)
        return True

    else:
        log.failure("Failed to remove Peer-Group on %s" % device_name)
        return False


def assign_ipv6(mode, fab_devices, csw_devices, asw_devices, subnet, fab=None, csw=None, asw=None, interface_dict=None, interface_ipv6_dict=None):
    """
    Assigns IPv6 address to the routers
    """
    list1 = []
    count = 0
    if mode == "no":
        for i in range(0, int(fab_devices)):
            list1.append(fab[i])
        for i in range(0, int(csw_devices)):
            list1.append(csw[i])
        for i in range(0, int(asw_devices)):
            list1.append(asw[i])
        for i in range(len(list1)):
            count1 = 0
            count2 = 0
            device = list1[i]
            device_name = device_parser(device)
            log.info("login to %s and configure IP address" % device_name)
            device_info = get_device_info(device_name)
            ip_address = device_info[1]
            switch = FlexSwitch(ip_address, 8080)   # Instantiate object to talk to flexSwitch
            for j in range(len(list1)):
                if device != list1[j]:
                    device_ip = "%s_%s_interface_ip" % (device, list1[j])
                    device_interface = "%s_%s_eth" % (device, list1[j])
                    if device_ip in interface_ipv6_dict.keys() and device_interface in interface_dict.keys():
                        count1 += 1
                        result = switch.create_ipv6_intf(interface_dict[device_interface], interface_ipv6_dict[device_ip]+ subnet, admin_state='UP')
                        if result.ok or result.status_code == 500:
                            count2 += 1
                        else:
                            log.failure("Failed to Configure IPv6 %s on %s" %(interface_dict[device_interface], device_name))
            if count1 == count2:
                log.success("IPv6 is configured successfully on %s" % device_name)
                count += 1
    if mode == "yes":
        for i in fab:
            list1.append(i)
        for i in csw:
            list1.append(i)
        for i in asw:
            list1.append(i)
        for i in range(len(list1)):
            count1 = 0
            count2 = 0
            device = list1[i]
            device_name = device_parser(device)
            log.info("login to %s and configure IP address" % device_name)
            device_info = get_device_info(device_name)
            ip_address = device_info[1]
            switch = FlexSwitch(ip_address, 8080)  # Instantiate object to talk to flexSwitch
            for j in range(len(list1)):
                if device != list1[j]:
                    device_ip = "%s_%s_interface_ip" % (device, list1[j])
                    device_interface = "%s_%s_eth" % (device, list1[j])
                    if device_ip in interface_ipv6_dict.keys() and device_interface in interface_dict.keys():
                        count1 += 1
                        result = switch.createIPv6Intf(interface_dict[device_interface], interface_ipv6_dict[device_ip]+subnet, AdminState='UP')
                        if result.ok or result.status_code == 500:
                            count2 += 1
                        else:
                            log.failure("Failed to Configure IPv6 %s on %s" %(interface_dict[device_interface], device_name))
            if count1 == count2:
                log.success("IPv6 is configured successfully on %s" % device_name)
                count += 1
    if count == len(list1):
        log.success("IP is configured successfully")
        return True
    else:
        log.failure("IP is not configured")
        return False


def remove_ipv6(mode, fab_devices, csw_devices, asw_devices, subnet, fab=None, csw=None, asw=None, interface_dict=None, interface_ipv6_dict=None):
    """
    Deletes the interfaces and IPv6 address from the routers
    """
    list1 = []
    count = 0
    if mode == "no":
        for i in range(0, int(fab_devices)):
            list1.append(fab[i])
        for i in range(0, int(csw_devices)):
            list1.append(csw[i])
        for i in range(0, int(asw_devices)):
            list1.append(asw[i])
        for i in range(len(list1)):
            count1 = 0
            count2 = 0
            device = list1[i]
            device_name = device_parser(device)
            log.info("login to %s and configure IPv6 address" % device_name)
            device_info = get_device_info(device_name)
            ip_address = device_info[1]
            switch = FlexSwitch(ip_address, 8080)  # Instantiate object to talk to flexSwitch
            for j in range(len(list1)):
                if device != list1[j]:
                    device_ip = "%s_%s_interface_ip" % (device, list1[j])
                    device_interface = "%s_%s_eth" % (device, list1[j])
                    if device_ip in interface_ipv6_dict.keys() and device_interface in interface_dict.keys():
                        count1 += 1
                        delete_ipv6_intf = switch.delete_ipv6_intf(interface_dict[device_interface])
                        if delete_ipv6_intf.status_code == 410:
                            count2 += 1
                        else:
                            log.failure("Failed to remove IPv6 %s on %s" % (interface_dict[device_interface], device_name))
            if count1 == count2:
                log.success("IPv6 is removed successfully on %s" % device_name)
                count += 1
    if mode == "yes":
        for i in fab:
            list1.append(i)
        for i in csw:
            list1.append(i)
        for i in asw:
            list1.append(i)
        count = 0
        for i in range(len(list1)):
            count1 = 0
            count2 = 0
            device = list1[i]
            device_name = device_parser(device)
            device_info = get_device_info(device_name)
            log.info("login to %s and configure IPv6 address" % device_name)
            ip_address = device_info[1]
            switch = FlexSwitch(ip_address, 8080)  # Instantiate object to talk to flexSwitch
            for j in range(len(list1)):
                if device != list1[j]:
                    device_ip = "%s_%s_interface_ip" % (device, list1[j])
                    device_interface = "%s_%s_eth" % (device, list1[j])
                    if device_ip in interface_ipv6_dict.keys() and device_interface in interface_dict.keys():
                        count1 += 1
                        delete_ipv6_intf = switch.delete_ipv6_intf(interface_dict[device_interface])
                        if delete_ipv6_intf.status_code == 410:
                            count2 += 1
                        else:
                            log.failure("Failed to remove IPV6 %s on %s" % (interface_dict[device_interface], device_name))
                            return False
            if count1 == count2:
                log.success("IPv6 is removed successfully on %s" % device_name)
                count += 1

    if count == len(list1):
        log.success("IPv6 is removed successfully")
        return True
    else:
        log.failure("IPv6 is not removed ")
        return False


def assign_bgpv6(mode, fab_devices, csw_devices, asw_devices, fab=None, csw=None, asw=None, interface_ipv6_dict=None, asnum=None, router_id=None):
    """
    Assigns the BGP IPv6 address to the routers
    """
    list1 = []
    count = 0
    if mode == "no":
        for i in range(0, int(fab_devices)):
            list1.append(fab[i])
        for i in range(0, int(csw_devices)):
            list1.append(csw[i])
        for i in range(0, int(asw_devices)):
            list1.append(asw[i])
        for i in range(len(list1)):
            count1 = 0
            count2 = 0
            device = list1[i]
            device_name = device_parser(device)
            device_info = get_device_info(device_name)
            log.info("log-in to %s  and loading BGP Configuration" % device_name)
            ip_address = device_info[1]
            switch = FlexSwitch(ip_address, 8080)  # Instantiate object to talk to flexSwitch
            local = asnum[device]
            router_id_val = router_id[device]
            switch.update_bgp_global("default", asnum=local, router_id=router_id_val)
            for j in range(len(list1)):
                peer = asnum[list1[j]]
                if device != list1[j]:
                    device_ip = "%s_%s_interface_ip" % (list1[j], device)
                    if device_ip in interface_ipv6_dict.keys():
                        count1 += 1
                        result = switch.create_bgpv6_neighbor("", interface_ipv6_dict[device_ip], peer_as=peer, local_as=local)
                        if result.ok or result.status_code == 500:
                            count2 += 1
                        else:
                            log.failure("Failed to Configure BGP neighbor %s on %s" % (interface_ipv6_dict[device_ip], device_name))

            if count1 == count2:
                log.success("BGP Configured successfully on %s" % device_name)
                count += 1
    if mode == "yes":
        for i in fab:
            list1.append(i)
        for i in csw:
            list1.append(i)
        for i in asw:
            list1.append(i)
        for i in range(len(list1)):
            count1 = 0
            count2 = 0
            device = list1[i]
            device_name = device_parser(device)
            device_info = get_device_info(device_name)
            ip_address = device_info[1]
            switch = FlexSwitch(ip_address, 8080)  # Instantiate object to talk to flexSwitch
            local = asnum[device]
            router_id_val = router_id[device]
            switch.update_bgp_global("default", asnum=local, router_id=router_id_val)
            log.info("log-in to %s and loading BGP Configuration" % device_name)
            for j in range(len(list1)):
                peer = asnum[list1[j]]
                if device != list1[j]:
                    device_ip = "%s_%s_interface_ip" % (list1[j], device)
                    if device_ip in interface_ipv6_dict.keys():
                        count1 += 1
                        result = switch.create_bgpv6_neighbor("", interface_ipv6_dict[device_ip], peer_as=peer, local_as=local)
                        if result.ok or result.status_code == 500:
                            count2 += 1
                        else:
                            log.failure("Failed to Configure BGP neighbor %s on %s" % (interface_ipv6_dict[device_ip], device_name))

            if count1 == count2:
                log.success("BGP Configured successfully on %s" % device_name)
                count += 1
    if count == len(list1):
        log.success("BGP is configured successfully")
        return True
    else:
        log.failure("BGP is not configured")
        return False


def remove_bgpv6(mode, fab_devices, csw_devices, asw_devices, fab=None, csw=None, asw=None, interface_ipv6_dict=None, asnum=None, router_id=None):
    """
    Removes the bgp IPv6 neighbor address from the routers
    """
    list1 = []
    count = 0
    if mode == "no":
        for i in range(0, int(fab_devices)):
            list1.append(fab[i])
        for i in range(0, int(csw_devices)):
            list1.append(csw[i])
        for i in range(0, int(asw_devices)):
            list1.append(asw[i])
    if mode == "yes":
        for i in fab:
            list1.append(i)
        for i in csw:
            list1.append(i)
        for i in asw:
            list1.append(i)
    for i in range(len(list1)):
        count1 = 0
        count2 = 0
        device = list1[i]
        device_name = device_parser(device)
        device_info = get_device_info(device_name)
        ip_address = device_info[1]
        log.info("log-in to %s and remove BGP Configuration" % device_name)
        switch = FlexSwitch(ip_address, 8080)  # Instantiate object to talk to flexSwitch
        local = asnum[device]
        router_id_val = router_id[device]
        switch.update_bgp_global("default", asnum=local, router_id=router_id_val)
        for j in range(len(list1)):
            peer = asnum[list1[j]]
            if device != list1[j]:
                device_ip = "%s_%s_interface_ip" % (list1[j], device)
                if device_ip in interface_ipv6_dict.keys():
                    count1 += 1
                    remove_bgpv6_neighbor = switch.delete_bgpv6_neighbor("", interface_ipv6_dict[device_ip])
                    if remove_bgpv6_neighbor.status_code == 410:
                        count2 += 1
                    else:
                        log.failure("Failed to remove BGP neighbor %s on %s" % (interface_ipv6_dict[device_ip], device_name))
        if count1 == count2:
            log.success("BGP Configuration removed on %s" % device_name)
            count += 1

    if count == len(list1):
        log.success("BGP is removed successfully")
        return True
    else:
        log.failure("BGP is not removed ")
        return False


def neighbor_ipv6_state_all(state_value, mode, fab_devices, csw_devices, asw_devices, fab=None, csw=None, asw=None, interface_ip_dict=None):
    """
    Checks for the IPv6 neighborship state for entire routers
    """
    list1 = []
    if mode == "no":
        for i in range(0, int(fab_devices)):
            list1.append(fab[i])
        for i in range(0, int(csw_devices)):
            list1.append(csw[i])
        for i in range(0, int(asw_devices)):
            list1.append(asw[i])
    if mode == "yes":
        for i in fab:
            list1.append(i)
        for i in csw:
            list1.append(i)
        for i in asw:
            list1.append(i)
    device_count = 0
    for i in list1:
        device = i
        device_name = device_parser(device)
        log.step("Checking for %s in %s" % (state_value, device_name))
        log.info("Log-in into %s to check for %s state" % (device_name, state_value))
        device_name = device_parser(device)
        device_info = get_device_info(device_name)
        ip_address = device_info[1]
        switch = FlexSwitch(ip_address, 8080)
        output = switch.get_all_bgpv6_neighbor_states()
        log.details(output)
        rec_count = 0
        dev_count = 0
        list2 = []
        flag = 0
        for eachline in output:
            for j in range(len(list1)):
                if device != list1[j]:
                    dev_count += 1
                    device_ip = "%s_%s_interface_ip" % (list1[j], device)
                    if device_ip in interface_ip_dict.keys():
                        if list1[j] not in list2:
                            list2.append(list1[j])
                        ip_actual = interface_ip_dict[device_ip]
                        ip_actual = "'%s'" % ip_actual
                        if ip_actual in str(eachline) and "'SessionState': 6" in str(eachline):
                            rec_count += 1
                            flag = 1
                            break
        if rec_count == len(list2) and flag == 1:
            log.success("Required %s state is achieved in %s" % (state_value, device_name))
            device_count += 1
        else:
            log.failure("Required %s state is not achieved in %s" % (state_value, device_name))
    if device_count == len(list1):
        log.success("Neighborship is get %s  state on all devices" % state_value)
        return True
    else:
        log.failure("Neighborship is not get %s state on all devices" % state_value)
        return False


def create_bfd_neighbor(device, bfd_name, neighbor_ip, asnum, peeras):
    """
    Adds BFD to the neighbor
    """
    device_name = device_parser(device)
    device_info = get_device_info(device_name)
    ip_address = device_info[1]
    switch = FlexSwitch(ip_address, 8080)
    result = switch.update_bgpv4_neighbor(intf_ref='', neighbor_address=neighbor_ip, peer_as=peeras, local_as=asnum, bfd_enable="True", bfd_session_param=bfd_name)
    if result.ok or result.status_code == 500:
        log.success("BFD is assigned to neighbor on %s" % device_name)
        return True
    else:
        log.failure("Failed to assign bfd to neighbor on %s " % device_name)
        return False


def check_bfd(mode, device, device1, interface_dict=None):
    """
    Validates the BFD state using CLI
    """
    flag = 0
    device_name = device_parser(device)
    device_interface = "%s_%s_interface_ip" % (device1, device)
    ip_address = interface_dict[device_interface]
    log.step("Checking BFD state in %s" % device_name)
    log.info("Log-in into %s to check for neighbor" % device_name)
    connection_info = connect(device)
    connection_info.sendline("snap_cli ")
    connection_info.prompt()
    connection_info.sendline("enable ")
    connection_info.prompt()
    connection_info.sendline("show bfd session")
    connection_info.prompt()
    result = connection_info.before
    log.details(result)
    fd = open("sample.txt", "w+")
    fd.write(result)
    fd.close()
    f = open("sample.txt", "r")
    line = f.readlines()
    pattern = r'\s*(\d*.\d*.)\s*\d*/\d*\s*[A-z]*, \s*\d*\s*\d*\s*\d*\s*([A-z]*).*'
    pattern1 = r'\s*(\d*.\d*).*'
    for eachline in range(len(line)):
        match = re.search(pattern, line[eachline])
        if match:
            eachline += 1
            match1 = re.search(pattern1, line[eachline])
            ip_new = "%s%s" % (match.group(1), match1.group(1))
            if mode == "noshutdown":
                if ip_new == ip_address and match.group(2) == "up":
                    flag = 1
                    log.success("BFD state is UP on %s" % device_name)
                    return True
                else:
                    log.failure("BFD state is not up on %s" % device_name)
                    return False
            if mode == "shutdown":
                if ip_new == ip_address and match.group(2) == "down":
                    flag = 1
                    log.success("BFD state is DOWN on %s" % device_name)
                    return True
                else:
                    log.failure("BFD state is not DOWN on %s" % device_name)
                    return False
    if flag == 0:
        log.failure("BFD state or ip address is not found in %s" % device_name)
        return False


def interface_vlan(device, vlanid, intf=''):
    """
    Adds VLAN to the interface
    """
    device_name = device_parser(device)
    device_info = get_device_info(device_name)
    ip_address = device_info[1]
    switch = FlexSwitch(ip_address, 8080)
    result = switch.update_vlan(vlanid, admin_state="UP", intf_list=[intf])
    if result.ok or result.status_code == 500:
        if intf == '':
            log.success("Vlan interface is deleted on %s" % device_name)
            return True
        else:
            log.success("Vlan interface is created on %s" % device_name)
            return True
    else:
        log.failure("Failed to create/remove Vlan interface on %s" % device_name)
        return False


def vlan_config(device, vlan_id):
    """
    Creates VLAN
    """
    device_name = device_parser(device)
    device_info = get_device_info(device_name)
    ip_address = device_info[1]
    switch = FlexSwitch(ip_address, 8080)  # Instantiate object to talk to flexSwitch
    create_vlan = switch.create_vlan(vlan_id, None, None)
    if create_vlan.ok or create_vlan.status_code == 500:
        log.success("Vlan is created on %s " % device_name)
        return True
    else:
        log.failure("Failed to create Vlan on %s" % device_name)
        return False


def delete_vlan(device, vlan_id):
    """
    Deletes VLAN
    """
    device_name = device_parser(device)
    device_info = get_device_info(device_name)
    ip_address = device_info[1]
    switch = FlexSwitch(ip_address, 8080)  # Instantiate object to talk to flexSwitch
    delete_vlan1 = switch.delete_vlan(int(vlan_id))
    if delete_vlan1.status_code == 410:
        log.success("Vlan is removed in %s" % device_name)
        return True
    else:
        log.failure("Failed to delete Vlan on %s" % device_name)
        return False


def check_vlan_status(device, vlan_id, state_value, interface):
    """
    Create BGP with peer-group
    """
    flag = 0
    vlan = "vlan%s" % vlan_id
    device_name = device_parser(device)
    log.info("Loading into %s" % device_name)
    device_info = get_device_info(device_name)
    ip_address = device_info[1]
    switch1 = FlexSwitchShow(ip_address, 8080)
    result = switch1.print_combined_vlan_states()
    log.details(result)
    fd = open("sample.txt", "w+")
    fd.write(result)
    fd.close()
    f = open("sample.txt", "r")
    line = f.readlines()
    for eachline in range(len(line)):
        if vlan_id in line[eachline] and state_value in line[eachline] and interface in line[eachline]:
            flag = 1
            log.success("VLAN verified on %s" % device_name)
            return True
    if flag == 0:
        log.failure("VLAN is not configured correctly on %s" % device_name)
        return False


def create_bgpv4_neighbor_attribute(device, local, neighbor_address, password='', peergroup='', peeras=''):
    """
    Create BGP with peer-group
    """
    device_name = device_parser(device)
    device_info = get_device_info(device_name)
    ip_address = device_info[1]
    switch = FlexSwitch(ip_address, 8080)
    result = switch.create_bgpv4_neighbor('', neighbor_address, peer_as=peeras, local_as=local, auth_password=password, peer_group=peergroup)
    if result.ok:
        if password != '':
            log.success("BGP neighbor with password is configured on %s" % device_name)
            return True
        if peergroup != '':
            log.success("BGP neighbor with peergroup is configured on %s" % device_name)
            return True
        else:
            log.success("BGP neighbor is configured on %s" % device_name)
            return True
    else:
        log.failure("Failed to Configure BGP on %s" % device_name)
        return False


def create_peergroup(device, name, peeras):
    """
    Create the peer group
    """
    device_name = device_parser(device)
    device_info = get_device_info(device_name)
    ip_address = device_info[1]
    switch = FlexSwitch(ip_address, 8080)
    result = switch.create_bgpv4_peer_group(name, peer_as=str(peeras))
    if result.ok or result.status_code == 500:
        log.success("peer group is configured on %s" % device_name)
        return True
    else:
        log.failure("Failed to Configure peer group on %s" % device_name)
        return False


def update_bgp_neighbor(device, neighbor_address, local=None, password=None, keep_alive_time=None, hold_time=None, retrytime=None):
    """
    Updates the BGP 
    """
    device_name = device_parser(device)
    device_info = get_device_info(device_name)
    ip_address = device_info[1]
    switch = FlexSwitch(ip_address, 8080)
    log.info("log into %s on the neighbor ip %s to update" % (device_name, neighbor_address))
    result = switch.update_bgpv4_neighbor('', neighbor_address, local_as=local, auth_password=password, keep_alive_time=keep_alive_time, hold_time=hold_time, connect_retry_time=retrytime)
    if result.ok or result.status_code == 500:
        log.success("BGP neighbor is updated on %s" % device_name)
        return True

    else:
        log.failure("Failed to update BGP neighbor on %s" % device_name)
        return False


def create_bfd_session(device, bfd_name, minrx, interval, multiplier):
    """
    Creates BFD Session 
    """
    device_name = device_parser(device)
    device_info = get_device_info(device_name)
    ip_address = device_info[1]
    switch = FlexSwitch(ip_address, 8080)
    result = switch.create_bfd_session_param(name=bfd_name, required_min_rx_interval=minrx, required_min_echo_rx_interval=interval, local_multiplier=multiplier)
    if result.ok or result.status_code == 500:
        log.success("BFD Session Param is created on %s" % device_name)
        return True
    else:
        log.failure("Failed to create BFD Session Param on %s " % device_name)
        return False


def delete_bfd_session(device, bfd_name):
    """
    Deletes BFD Session
    """
    device_name = device_parser(device)
    device_info = get_device_info(device_name)
    ip_address = device_info[1]
    switch = FlexSwitch(ip_address, 8080)
    result = switch.delete_bfd_session_param(bfd_name)
    if result.status_code == 410:
        log.success("BFD Session Param is deleted on %s" % device_name)
        return True
    else:
        log.failure("Failed to delete BFD Session Param on %s" % device_name)
        return False


def delete_interface(device, intf_name):
    """
    Deletes particular interface
    """
    device_name = device_parser(device)
    device_info = get_device_info(device_name)
    ip_address = device_info[1]
    switch = FlexSwitch(ip_address, 8080)

    result = switch.delete_ipv4_intf(intf_name)
    if result.status_code == 410:
        log.success("IP removed successfully on %s" % device_name)
        return True

    else:
        log.failure("Failed to delete IP %s on %s" % (intf_name, device_name))
        return False


def create_interface(device, interface, interface_ip):
    """
    Creates particular interface
    """
    device_name = device_parser(device)
    device_info = get_device_info(device_name)
    ip_address = device_info[1]
    switch = FlexSwitch(ip_address, 8080)
    result = switch.create_ipv4_intf(interface, interface_ip)
    if result.ok or result.status_code == 500:
        log.success("%s is added to interface %s on %s" % (interface_ip, interface, device_name))
        return True
    else:
        log.failure("Failed to create %s to interface %s on %s" % (interface_ip, interface, device_name))
        return False


def assign_bgp_rrclient(mode, fab_devices, csw_devices, asw_devices, fab=None, csw=None, asw=None, interface_ip_dict=None, asnum=None, router_id=None):
    """
    Assigns the BGP IPv4 address to the routers and assign route reflector Client on the Leaf nodes
    """
    list1 = []
    count = 0
    device_count1 = 0
    device_count = 0
    non_leaf_count = 0
    if mode == "no":
        for i in range(0, int(fab_devices)):
            list1.append(fab[i])
            device_count += 1
            non_leaf_count += 1
        for i in range(0, int(csw_devices)):
            list1.append(csw[i])
            device_count += 1
            non_leaf_count += 1
        for i in range(0, int(asw_devices)):
            list1.append(asw[i])
            device_count += 1
        for i in range(len(list1)):
            need_count = 0
            received_count = 0
            device = list1[i]
            device_name = device_parser(device)
            device_info = get_device_info(device_name)
            log.info("log-in to %s and loading BGP configuration" % device_name)
            ip_address = device_info[1]
            switch = FlexSwitch(ip_address, 8080)  # Instantiate object to talk to flexSwitch
            local = asnum[device]
            router_id_val = router_id[device]
            switch.update_bgp_global("default", asnum=local, router_id=router_id_val)
            device_count1 += 1
            for j in range(len(list1)):
                peer = asnum[list1[j]]
                if device != list1[j]:
                    device_ip = "%s_%s_interface_ip" % (list1[j], device)
                    if device_ip in interface_ip_dict.keys():
                        need_count += 1
                        if device_count1 <= non_leaf_count:
                            result = switch.create_bgpv4_neighbor("", interface_ip_dict[device_ip], peer_as=peer, local_as=local)
                            if result.ok or result.status_code == 500:
                                received_count += 1
                            else:
                                log.failure("Failed to Configure BGP neighbor %s on %s" % (interface_ip_dict[device_ip], device_name))
                        if non_leaf_count < device_count1 <= device_count:
                            result = switch.create_bgpv4_neighbor("", interface_ip_dict[device_ip], peer_as=peer, local_as=local, route_reflector_client="True")
                            if result.ok or result.status_code == 500:
                                received_count += 1
                            else:
                                log.failure("Failed to Configure BGP neighbor %s on %s" % (interface_ip_dict[device_ip], device_name))
            if need_count == received_count:
                log.success("BGP is configured successfully on %s" % device_name)
                count += 1
    if mode == "yes":
        for i in fab:
            list1.append(i)
            device_count += 1
            non_leaf_count += 1
        for i in csw:
            list1.append(i)
            device_count += 1
            non_leaf_count += 1
        for i in asw:
            list1.append(i)
            device_count += 1
        for i in range(len(list1)):
            need_count = 0
            received_count = 0
            device = list1[i]
            device_name = device_parser(device)
            device_info = get_device_info(device_name)
            log.info("log-in to %s and loading BGP configuration" % device_name)
            ip_address = device_info[1]
            switch = FlexSwitch(ip_address, 8080)  # Instantiate object to talk to flexSwitch
            local = asnum[device]
            router_id_val = router_id[device]
            switch.update_bgp_global("default", asnum=local, router_id=router_id_val)
            device_count1 += 1
            for j in range(len(list1)):
                peer = asnum[list1[j]]
                if device != list1[j]:
                    device_ip = "%s_%s_interface_ip" % (list1[j], device)
                    if device_ip in interface_ip_dict.keys():
                        need_count += 1
                        if device_count1 <= non_leaf_count:
                            # print device, list1[j]
                            result = switch.create_bgpv4_neighbor("", interface_ip_dict[device_ip], peer_as=peer, local_as=local)
                            if result.ok or result.status_code == 500:
                                received_count += 1
                            else:
                                log.failure("Failed to Configure BGP neighbor %s on %s" % (interface_ip_dict[device_ip], device_name))
                        if non_leaf_count < device_count1 <= device_count:
                            result = switch.create_bgpv4_neighbor("", interface_ip_dict[device_ip], peer_as=peer, local_as=local, route_reflector_client="True")
                            if result.ok or result.status_code == 500:
                                received_count += 1
                            else:
                                log.failure("Failed to Configure BGP neighbor %s on %s " % (interface_ip_dict[device_ip], device_name))
            if need_count == received_count:
                log.success("BGP is configured successfully on %s" % device_name)
                count += 1
    if count == len(list1):
        log.success("BGP is configured successfully")
        return True
    else:
        log.failure("BGP is not configured")
        return False
