*** Settings ***
Documentation    Test Suite ID 		: 	LINKED_IN_BGP_01
...
...              Test Suite Name 	: 	OpenSnaproute_BGP_02
...
...              Created 			:	23-Nov-2016
...
...              Status 		 	: 	Completed 
...
...              @authors	    	: 	TERRALOGIC TEAM
...
...              Abstract 		    :   This test suite examines the basic functionalities of OpenSnaproute using "Dockers Setup"
...
...              Test-cases List 	:	1.Verify IPv4 BGP on all devices	
...              		        	: 	2.Trigger link failure and link recovery. Measure convergence time and verify system status.


Library  OperatingSystem
Library  Collections

Library	  /home/${USER}/BGP/OpenSnaproute/OpenSnaproute_Drivers/OpenSnaprouteCliDriver.py  
Variables   /home/${USER}/BGP/OpenSnaproute/OpenSnaproute_Variables/BGP_Variables.py
Suite Setup   Loading Basic Configuration
Suite Teardown   Deleting Basic Configuration



*** Variables ***
${USER}  openswitch



*** TestCases ***

Testcase1
    [Documentation]  Verify IPv4 BGP on all devices
    Sleep  120s
    CHECKPOINT  1.1 Check for the ipv4 bgp-neighbourship on all the devices
    TC1:check_bgp_neighbourship

	
Testcase2
    [Documentation]  Trigger link failure and link recovery. 
    Policy
    Sleep  30s
    CHECKPOINT  2.5 Checking trigger link failure
    ${out}=  TRIGGER  ${device}  ${destination_network}  ${interface_ip_dict}  ${interface_dict}
    Should Be True  ${out}



*** keywords ***
 

Load-Base-configuration
    CHECKPOINT   assigning IP and verifying  
    ${out} =  ASSIGN_IP  ${device_all}  ${fab_count}  ${csw_count}  ${asw_count}  ${subnet}  ${fab}  ${csw}  ${asw}  ${interface_dict}  ${interface_ip_dict}
    Should Be True  ${out}

    CHECKPOINT   assigning BGP and verifying  
    ${out} =  ASSIGN_BGP_RRCLIENT  ${device_all}  ${fab_count}  ${csw_count}  ${asw_count}  ${fab}  ${csw}  ${asw}  ${interface_ip_dict}  ${asnum}  ${routerid}
    Should Be True  ${out}
    

	
Enabling the Interface
    ${out}=  FLAP_STATE  ${device_all}  ${fab_count}  ${csw_count}  ${asw_count}  ${fab}  ${csw}  ${asw}  ${interface_dict}
    Should Be True  ${out}


	
Remove-Base-configuration
    CHECKPOINT   Removing IP and verifying  
    ${out}=  REMOVE_IP  ${device_all}  ${fab_count}  ${csw_count}  ${asw_count}  ${subnet}  ${fab}  ${csw}  ${asw}  ${interface_dict}  ${interface_ip_dict}
    Should Be True  ${out}
	
    CHECKPOINT   removing BGP and verifying  
    ${out}=  REMOVE_BGP  ${device_all}  ${fab_count}  ${csw_count}  ${asw_count}  ${fab}  ${csw}  ${asw}  ${interface_ip_dict}  ${asnum}  ${routerid} 
    Should Be True  ${out}


	
TC1:check_bgp_neighbourship
    ${out}=  NEIGHBOR_STATE_ALL  Estab  ${device_all}  ${fab_count}  ${csw_count}  ${asw_count}  ${fab}  ${csw}  ${asw}  ${interface_ip_dict}
    Should Be True  ${out}


	
Policy 
    CHECKPOINT  Creating a policy Condition
    ${out} =  CREATE_POLICY_CONDITION_NAME  ${device_all}  ${fab_count}  ${csw_count}  ${asw_count}  ${fab}  ${csw}  ${asw}  ${Condition_name}  ${ConditionType}  ${Protocol}  ${IpPrefix}  ${MaskLengthRange}  ${PrefixSet}  
    Should Be True  ${out}

    CHECKPOINT  Creating a policy statement
    ${out} =  CREATE_POLICY_STATEMENT  ${device_all}  ${fab_count}  ${csw_count}  ${asw_count}  ${fab}  ${csw}  ${asw}  ${stmt_name}  ${Condition_name}  ${Action}  ${MatchConditions} 
    Should Be True  ${out}

    CHECKPOINT  Creating a policy definition
    ${out} =  CREATE_POLICY_DEFINITIONS  ${device_all}  ${fab_count}  ${csw_count}  ${asw_count}  ${fab}  ${csw}  ${asw}  ${stmt_name}  ${Pol_def_name}  ${Priority}  ${MatchType}  ${PolicyType}
    Should Be True  ${out}

    CHECKPOINT  Adding the policy in BGP
    ${out}=  CREATE_BGP_GLOBAL  ${device_all}  ${fab_count}  ${csw_count}  ${asw_count}  ${fab}  ${csw}  ${asw}  ${asnum}  ${routerid}  redistribution=${Protocol}  pol_name=${Pol_def_name}  
    Should Be True  ${out}


#*****************************Test Setup Keywords**************************************


Loading Basic Configuration
    CHECKPOINT   flaping the state and verifying
    Enabling the Interface
	
    CHECKPOINT   load base configuration on devices and verifying
    Load-Base-configuration


#*****************************Test Teardown Keywords**************************************


Deleting Basic Configuration

    CHECKPOINT   Removing configuration on devices and verifying
    Remove-Base-configuration

















