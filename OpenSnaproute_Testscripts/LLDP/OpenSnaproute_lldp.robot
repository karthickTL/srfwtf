*** Settings ***
Documentation    Test Suite ID 		: 	LINKED_IN_ST_01
...
...              Test Suite Name 	: 	OpenSnapeRoute_ST_02
...
...              Created 		:	03-nov-2016
...
...              Status 		: 	Completed 
...
...              @authors		: 	TERRALOGIC TEAM
...
...              Abstract 		:       This test suite examines the basic functionalities of OpenSnaproute using "Dockers Setup"
...
...         Test-case       	        :	1.Verify lldp feature.	
...                   			



Library  OperatingSystem
Library  Collections
Library  /home/${USER}/OpenSnaproute_LLDP/OpenSnaproute_Drivers/OpenSnaprouteCliDriver.py
Variables  /home/${USER}/OpenSnaproute_LLDP/OpenSnaproute_Variables/Variables.py

*** Variables ***
${USER}  openswitch2

*** TestCases ***
   

Testcase1

    [Documentation]  Verify lldp feature
    CHECKPOINT  1.1 Specifying Hostname  
    host  ${device_all}  ${fab_count}  ${csw_count}  ${asw_count}  ${fab}  ${csw}  ${asw}  ${hostname}
    CHECKPOINT  1.2 Enable the LLDP and verifying 
    TC1:Enable the LLDP 
    CHECKPOINT  1.3 Enabling the interface state on devices and verifying
    TC1:Enabling the Interface
    CHECKPOINT  1.4 Verify LLDP  
    TC1:Verify LLDP


*** keywords ***


    

TC1:Enabling the Interface
    statedown  ${device_all}  ${fab_count}  ${csw_count}  ${asw_count}  ${fab}  ${csw}  ${asw}  ${interface_dict}
    stateup  ${device_all}  ${fab_count}  ${csw_count}  ${asw_count}  ${fab}  ${csw}  ${asw}  ${interface_dict}

TC1:Verify LLDP
     lldpNeighborInfo  ${device_all}  ${fab_count}  ${csw_count}  ${asw_count}  ${device_list}  ${fab}  ${csw}  ${asw}  ${interface_dict}

TC1:Enable the LLDP 
    enablelldp  ${device_all}  ${fab_count}  ${csw_count}  ${asw_count}  ${fab}  ${csw}  ${asw}


