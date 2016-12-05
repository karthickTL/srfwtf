*** Settings ***

Documentation    Test Suite ID 		: 	LINKED_IN_FT_01
...
...              Test Suite Name 	: 	OpenSnaproute_FT_02
...
...              Created 		:	21-Nov-2016
...
...              Status 		: 	Completed 
...
...              @authors		: 	TERRALOGIC TEAM
...
...                                     :       Mahesh                            mahesh.janya@terralogic.com
...                                     :       Karthick Ramalingum               karthick@terralogic.com
...
...              Abstract 		:       This test suite examines the basic functionalities of OpenSnaproute using "Dockers Setup"
...
...              Test-cases List        : 	1.Verify Static-Routing functionality.
...              			: 	2.Verify the IPV4 E-BGP neighbourship.
...              			: 	3.Verify ipv4-ipv6 E-BGP Neighbourship with PEER-GROUP feature.
...                                     :       4.Verify the ipv4 Neighbourship with BGP-Authentication.
...                                     :       5.Verify the "BFD-Timers" functionality.
...                                     :       6.Verify vlan basic testing.
...              			: 	7.Verify the IPV6 E-BGP neighbourship.

Library   Collections
Library   SSHLibrary
Suite Setup   IP_BGP configuration and Flap_verify the interfaces
Suite Teardown   Delete IPv4 interfaces

Library	  /home/${USER}/Downloads/Final_FT_ST/OpenSnaproute/OpenSnaproute_Drivers/OpenSnaprouteCliDriver.py  
Variables   /home/${USER}/Downloads/Final_FT_ST/OpenSnaproute/OpenSnaproute_Variables/FT_Variable.py


#---------------------------------------5-NODES-OpenSwitch TOPOLOGY----------------------
#
# 	NODES : #FAB05, #FAB06, #CSW01, #CSW02, #ASW01
#
#
#
#				 	1.1.1.1/32
#						|   # 64700
#                                              FAB05--------------FAB06
#	10.0.20.0/31			    .0|    |.2			10.0.20.2/31
#  				|--------------    -----------------
#			      .1|				    |.3
#                  #64850     CSW01                                CSW02  #64850
#			     .0	|				     |.0
#				|				     |
#				----------------     ----------------
#	10.0.4.0/31			     .1	|    | .1		10.0.5.0/31
#						 ASW01   #64900
#
#-----------------------------------------------------------------------------------------

*** Variables ***
${USER}  openswitch4
*** Testcases ***


Testcase1

    [Documentation]  Verify Static-Routing functionality.

    CASE  Verify Static-Routing functionality.
  
    CHECKPOINT  1.1 Create static routing
    TC1: Static_routing
    Sleep  60s
    CHECKPOINT  1.2 Ping test
    TC1:Ping_test

Testcase2

    [Documentation]  IPV4 Neighbourship 

    CASE  Verify the ipv4 Neighbourship 
  
    CHECKPOINT  2.1 load BGP configuration on devices and verifying
    TC2:Load-Base-configuration_bgp
    
    Sleep  120s
    
    CHECKPOINT  2.2 Check for the ipv4 bgp-neighbourship on all the devices
    TC2:check_bgp_neighbourship

    CHECKPOINT  2.3 Remove bgp configuration on devices and verifying
    TC2:Remove-Base-configuration_bgp

Testcase3

    [Documentation]  Verify ipv4 E-BGP Neighbourship with PEER-GROUP feature.  

    CASE   Verify PEER-GROUP feature
   
   
    CHECKPOINT  3.1 Creating peer-group
    TC3:creating-peer-group


    CHECKPOINT  3.2 Adding BGP neighbors to the IPv4 interfaces
    TC3:adding-bgp-neighbor
    Sleep  180s

    CHECKPOINT  3.3 Check the bgp-neighbourship for Established state
    TC3:check_bgp_neighbourship

    CHECKPOINT  3.4  Removing the peer-group
    TC3:Removing-peer-group
    
    CHECKPOINT  3.5 Removing BGP Neighbors
    TC3:Remove-Base-configuration_bgp

Testcase4

    [Documentation]  IPV4 EBGP-Authentication

    CASE  Verify the ipv4 Neighbourship with BGP-Authentication
    
    CHECKPOINT  4.1 load BGP configuration on devices and verifying
    TC4:Load-Base-configuration_bgp

    CHECKPOINT  4.2 Adding Authentication password to BGP neighbor
    TC4:Adding-authentication-password
    Sleep  60s

    CHECKPOINT  4.3 Check the bgp-neighbourship for Established state
    TC4:check_bgp_neighbourship

    CHECKPOINT  4.4 Update the bgp neighbor with wrong password
    TC4:Update-wrong_password
    Sleep  60s

    
    CHECKPOINT  4.5 Check for the bgp-neighbourship which should not be in Established state
    TC4:check_bgp_neighbourship_on_the_device

    CHECKPOINT  4.6 Update the bgp neighbor with correct password
    TC4:Update-correct_password
    Sleep  60s 

    CHECKPOINT  4.7 Check the bgp-neighbourship for Established state
    TC4:check_bgp_neighbourship_on_a_device

    CHECKPOINT  4.8 Remove bgp configuration on devices and verifying
    TC4:Remove-Base-configuration_bgp

  
Testcase5

    [Documentation]  Verify the "BFD-Timers" functionality

    CASE  Verify BFD-Timers functionality
  
    CHECKPOINT  5.1 load BGP configuration on devices and verifying
    TC5:Load-Base-configuration_bgp   
    Sleep  120s
        
    CHECKPOINT  5.2 Creating BFD session
    TC5:create-bfd-session
   
    CHECKPOINT  5.3 Adding BFD to neighbor
    TC5:create-bfd-neighbor
    Sleep  20s

    CHECKPOINT  5.4 Validating BFD for "UP" state
    TC5: Validate_bfd_state_UP
    
    CHECKPOINT  5.5 Make the interface link "DOWN"
    TC5: Interface-link-down
    Sleep  20s

    CHECKPOINT  5.6 Validating BFD for "DOWN" state
    TC5: Validate_bfd_state_DOWN
    
    CHECKPOINT  5.7 Check for the bgp-neighbourship which should not be in Established state
    TC5:check_bgp_neighbourship_on_a_device

    CHECKPOINT  5.8 Make the interface link "UP"
    TC5: Interface-link-up

    CHECKPOINT  5.9 Deleting BFD session
    TC5:delete-bfd-session

    CHECKPOINT  5.10 Remove bgp configuration on devices and verifying
    TC5:Remove-Base-configuration_bgp

Testcase6

    [Documentation]  VLAN Testing 

    CASE  Verify the VLAN Functionality 
 
    CHECKPOINT  6.1 Creating VLAN
    TC6:creating_vlan

    CHECKPOINT  6.2 Deleting the ip address
    TC6:delete_interface
    
    CHECKPOINT  6.3  Creating Vlan interface
    TC6:creating_vlan_interface
   
    CHECKPOINT  6.4 Applying VLAN into the interface
    TC6:Applying_vlan_to_interface
    Sleep  5s

    CHECKPOINT  6.5 Verify vlan status
    TC6:verify_vlan_status

    CHECKPOINT  6.6 Check reachability between the vlan-interface using PING
    TC6:ping_test
    Sleep  5s

    CHECKPOINT  6.7 Deleting VLAN from the interface
    TC6:Deleting_vlan_from_interface

    CHECKPOINT  6.8  Deleting Vlan interface
    TC6:delete_vlan_interface

    
    CHECKPOINT  6.9  Creating IPv4 interface
    TC6:creating_interface

    CHECKPOINT  6.10  Deleting VLAN
    TC6:delete_the_vlan



Testcase7
    [Documentation]  IPV6 Neighbourship 

    CASE  Verify the ipv6 Neighbourship 
   
    CHECKPOINT  7.1 load ipv6 configuration on devices and verifying
    TC7:Load-Base-configuration_ipv6
   
    CHECKPOINT  7.2 load BGP configuration on devices and verifying
    TC7:Load-Base-configuration_bgpv6    
    Sleep  120s

    CHECKPOINT  7.3 Check for the ipv4 bgp-neighbourship on all the devices
    TC7:check_bgp_neighbourshipv6

    CHECKPOINT  7.4 Remove IPV6 configuration on devices and verifying
    TC7:Remove-Base-configuration_ipv6

    CHECKPOINT  7.5 Remove bgp configuration on devices and verifying
    TC7:Remove-Base-configuration_bgpv6


*** keywords ***

Load-Base-configuration_ip
    ${out}=  assignip  ${device_all}  ${fab_count}  ${csw_count}  ${asw_count}  ${subnet}  ${fab}  ${csw}  ${asw}  ${interface_dict}  ${interface_ip_dict}
    Should Be True  ${out}

Enabling the Interface
    ${out}=  flap_state  ${device_all}  ${fab_count}  ${csw_count}  ${asw_count}  ${fab}  ${csw}  ${asw}  ${interface_dict}
    Should Be True  ${out}

Remove-Base-configuration_ip
    ${out}=  removeip  ${device_all}  ${fab_count}  ${csw_count}  ${asw_count}  ${subnet}  ${fab}  ${csw}  ${asw}  ${interface_dict}  ${interface_ip_dict}
    Should Be True  ${out}


#*****************************TestCase1 Keywords**************************************

TC1: Static_routing
    ${out}=  static_route_configuration  ${device_list[0]}  ${device1_dest_network}  ${device1_nextHopIp}  ${device1_interface}  
    Should Be True  ${out}
    ${out}=  static_route_configuration  ${device_list[3]}  ${device4_dest_network}  ${device4_nextHopIp}  ${device4_interface}  
    Should Be True  ${out}
TC1:Ping_test
    ${out}=  Ping  ${device_list[0]}  ${device_list[3]}  ${device4_interface2_device3_interface2_no_subnet}
    Should Be True  ${out}
    ${out}=  Ping  ${device_list[3]}  ${device_list[0]}  ${device1_interface2_device3_interface1_no_subnet}
    Should Be True  ${out}

#*****************************TestCase2 Keywords**************************************

TC2:Load-Base-configuration_bgp
    ${out}=  assignbgp  ${device_all}  ${fab_count}  ${csw_count}  ${asw_count}  ${fab}  ${csw}  ${asw}  ${interface_ip_dict}  ${asnum}  ${routerid}
    Should Be True  ${out}
TC2:check_bgp_neighbourship
    ${out}=  neighbor_state_all  Estab  ${device_all}  ${fab_count}  ${csw_count}  ${asw_count}  ${fab}  ${csw}  ${asw}  ${interface_ip_dict}
    Should Be True  ${out}
TC2:Remove-Base-configuration_bgp
    ${out}=  removebgp  ${device_all}  ${fab_count}  ${csw_count}  ${asw_count}  ${fab}  ${csw}  ${asw}  ${interface_ip_dict}  ${asnum}  ${routerid}
    Should Be True  ${out}

#*****************************TestCase7 Keywords**************************************

TC7:Load-Base-configuration_ipv6
    ${out}=  assignipv6  ${device_all}  ${fab_count}  ${csw_count}  ${asw_count}  ${subnet_v6}  ${fab}  ${csw}  ${asw}  ${interface_dict}  ${interface_ipv6_dict}
    Should Be True  ${out}
TC7:Remove-Base-configuration_ipv6
    ${out}=  removeipv6  ${device_all}  ${fab_count}  ${csw_count}  ${asw_count}  ${subnet_v6}  ${fab}  ${csw}  ${asw}  ${interface_dict}  ${interface_ipv6_dict}
    Should Be True  ${out}
TC7:check_bgp_neighbourshipv6
    ${out}=  neighbor_ipv6_state_all  Estab  ${device_all}  ${fab_count}  ${csw_count}  ${asw_count}  ${fab}  ${csw}  ${asw}  ${interface_ipv6_dict}  
    Should Be True  ${out}
TC7:Load-Base-configuration_bgpv6
    ${out}=  assignbgpv6  ${device_all}  ${fab_count}  ${csw_count}  ${asw_count}  ${fab}  ${csw}  ${asw}  ${interface_ipv6_dict}  ${asnum}  ${routerid}
    Should Be True  ${out}
TC7:Remove-Base-configuration_bgpv6
    ${out}=  removebgpv6  ${device_all}  ${fab_count}  ${csw_count}  ${asw_count}  ${fab}  ${csw}  ${asw}  ${interface_ipv6_dict}  ${asnum}  ${routerid}
    Should Be True  ${out}

#*****************************TestCase3 Keywords**************************************
TC3:creating-peer-group
    ${out}=  create_peergroup  ${device_list[3]}  ${peer_group_id}  ${device1_peer_as}
    Should Be True  ${out}  
TC3:adding-bgp-neighbor

    ${out}=  createBGPv4Neighbor_attribute  ${device_list[0]}  ${device1_asnum}  ${device1_neighbour1_IP}  peeras=${device1_peer_as_1}  
    Should Be True  ${out}
    ${out}=  createBGPv4Neighbor_attribute  ${device_list[0]}  ${device1_asnum}  ${device1_neighbour2_IP}  peeras=${device1_peer_as_2}  
    Should Be True  ${out}
    ${out}=  createBGPv4Neighbor_attribute  ${device_list[1]}  ${device2_asnum}  ${device2_neighbour1_IP}  peeras=${device2_peer_as_1}  
    Should Be True  ${out}
    ${out}=  createBGPv4Neighbor_attribute  ${device_list[1]}  ${device2_asnum}  ${device2_neighbour2_IP}  peeras=${device2_peer_as_2}  
    Should Be True  ${out}
    ${out}=  createBGPv4Neighbor_attribute  ${device_list[2]}  ${device3_asnum}  ${device3_neighbour1_IP}  peeras=${device3_peer_as_1}  
    Should Be True  ${out}
    ${out}=  createBGPv4Neighbor_attribute  ${device_list[2]}  ${device3_asnum}  ${device3_neighbour2_IP}  peeras=${device3_peer_as_2}  
    Should Be True  ${out}
    ${out}=  createBGPv4Neighbor_attribute  ${device_list[3]}  ${device4_asnum}  ${device4_neighbour2_IP}  peeras=${device4_peer_as_2}  
    Should Be True  ${out}
    ${out}=  createBGPv4Neighbor_attribute  ${device_list[3]}  ${device4_asnum}  ${device4_neighbour1_IP}  peergroup=${peer_group_id}
    Should Be True  ${out}    

TC3:Load-Base-configuration_bgp
    ${out}=  assignbgp  ${device_all}  ${fab_count}  ${csw_count}  ${asw_count}  ${fab}  ${csw}  ${asw}  ${interface_ip_dict}  ${asnum}  ${routerid}
    Should Be True  ${out}
TC3:check_bgp_neighbourship
    ${out}=  neighbor_state_all  Estab  ${device_all}  ${fab_count}  ${csw_count}  ${asw_count}  ${fab}  ${csw}  ${asw}  ${interface_ip_dict}
    Should Be True  ${out}
TC3:Remove-Base-configuration_bgp
    ${out}=  removebgp  ${device_all}  ${fab_count}  ${csw_count}  ${asw_count}  ${fab}  ${csw}  ${asw}  ${interface_ip_dict}  ${asnum}  ${routerid}
    Should Be True  ${out}
TC3:check_bgp_peer_group
    ${out}=  validate_peer_group  ${device_list[3]}  ${peer_group_id}  ${device1_peer_as}
    Should Be True  ${out}
TC3:check_bgp_peer_group_neighbor
    ${out}=  verifybgpfeature  ${device_list[3]}  ${device_list[1]}  ${interface_ip_dict}  search_string=${Peer_group_name}
    Should Be True  ${out}
TC3:Removing-peer-group
    ${out}=  delete_peer_group  ${device_list[3]}  ${peer_group_id}
    Should Be True  ${out}
#*****************************TestCase4 Keywords**************************************

TC4:Load-Base-configuration_bgp
    ${out}=  assignbgp  ${device_all}  ${fab_count}  ${csw_count}  ${asw_count}  ${fab}  ${csw}  ${asw}  ${interface_ip_dict}  ${asnum}  ${routerid}
    Should Be True  ${out}
TC4:check_bgp_neighbourship
    ${out}=  neighbor_state_all  Estab  ${device_all}  ${fab_count}  ${csw_count}  ${asw_count}  ${fab}  ${csw}  ${asw}  ${interface_ip_dict}
    Should Be True  ${out}
TC4:Remove-Base-configuration_bgp
    ${out}=  removebgp  ${device_all}  ${fab_count}  ${csw_count}  ${asw_count}  ${fab}  ${csw}  ${asw}  ${interface_ip_dict}  ${asnum}  ${routerid}
    Should Be True  ${out}
TC4:check_bgp_neighbourship_on_the_device
    ${out}=  particular_device_neighbor_check  Active  ${device_list[3]}  ${device_list[2]}  ${interface_ip_dict}  
    Should Be True  ${out}
TC4:check_bgp_neighbourship_on_a_device
    ${out}=  particular_device_neighbor_check  Estab  ${device_list[3]}  ${device_list[2]}  ${interface_ip_dict}  
    Should Be True  ${out}

TC4:Adding-authentication-password
    ${out}=  update_bgpneighbor  ${device_list[2]}  ${device3_neighbour2_IP}  ${device3_asnum}  password=${device3_auth_Password_1}
    Should Be True  ${out}
    ${out}=  update_bgpneighbor  ${device_list[3]}  ${device4_neighbour2_IP}  ${device4_asnum}  password=${device4_auth_Password_1}
    Should Be True  ${out}
TC4:Update-wrong_password
    ${out}=  update_bgpneighbor  ${device_list[2]}  ${device3_neighbour2_IP}  ${device3_asnum}  password=${device3_auth_Password_2}
    Should Be True  ${out}
TC4:Update-correct_password
    ${out}=  update_bgpneighbor  ${device_list[2]}  ${device3_neighbour2_IP}  ${device3_asnum}  password=${device3_auth_Password_1}
    Should Be True  ${out}



#*****************************TestCase5 Keywords**************************************
TC5:Load-Base-configuration_bgp
    ${out}=  assignbgp  ${device_all}  ${fab_count}  ${csw_count}  ${asw_count}  ${fab}  ${csw}  ${asw}  ${interface_ip_dict}  ${asnum}  ${routerid}
    Should Be True  ${out}
TC5:check_bgp_neighbourship1
    ${out}=  neighbor_state_all  Estab  ${device_all}  ${fab_count}  ${csw_count}  ${asw_count}  ${fab}  ${csw}  ${asw}  ${interface_ip_dict}
    Should Be True  ${out}
TC5:Remove-Base-configuration_bgp
    ${out}=  removebgp  ${device_all}  ${fab_count}  ${csw_count}  ${asw_count}  ${fab}  ${csw}  ${asw}  ${interface_ip_dict}  ${asnum}  ${routerid}
    Should Be True  ${out}
TC5: Validate_bfd_state_UP
    ${out}=  check_bfd  ${bfd_mode_up}  ${device_list[0]}  ${device_list[1]}  ${interface_ip_dict}
    Should Be True  ${out}
TC5: Validate_bfd_state_DOWN
    ${out}=  check_bfd  ${bfd_mode_down}  ${device_list[0]}  ${device_list[1]}  ${interface_ip_dict}
    Should Be True  ${out}
TC5:check_bgp_neighbourship_on_a_device
    ${out}=  particular_device_neighbor_check  Active  ${device_list[0]}  ${device_list[1]}  ${interface_ip_dict}  
    Should Be True  ${out}
    ${out}=  particular_device_neighbor_check  Active  ${device_list[1]}  ${device_list[0]}  ${interface_ip_dict}  
    Should Be True  ${out}
   
TC5:create-bfd-session
    ${out}=  creatingbfdsession  ${device_list[0]}  ${bfd_name}  ${minrx}  ${interval}  ${multiplier}
    Should Be True  ${out}
    ${out}=  creatingbfdsession  ${device_list[1]}  ${bfd_name}  ${minrx}  ${interval}  ${multiplier}
    Should Be True  ${out}
TC5:create-bfd-neighbor
    ${out}=  create_bfd_neighbor  ${device_list[0]}  ${bfd_name}  ${device1_neighbour1_IP}  ${device1_asnum}  ${device1_peer_as_1}
    Should Be True  ${out}
    ${out}=  create_bfd_neighbor  ${device_list[1]}  ${bfd_name}  ${device2_neighbour1_IP}  ${device2_asnum}  ${device2_peer_as_1}
    Should Be True  ${out}
TC5: Interface-link-down
    ${out}=  state  ${device_list[0]}  ${device1_interface_1}  DOWN
    Should Be True  ${out}
    ${out}=  state  ${device_list[1]}  ${device2_interface_1}  DOWN
    Should Be True  ${out}
TC5: Interface-link-up
    ${out}=  state  ${device_list[0]}  ${device1_interface_1}  UP
    Should Be True  ${out}
    ${out}=  state  ${device_list[1]}  ${device2_interface_1}  UP
    Should Be True  ${out}
TC5:delete-bfd-session
    ${out}=  deletingbfdsession  ${device_list[0]}  ${bfd_name}
    Should Be True  ${out}
    ${out}=  deletingbfdsession  ${device_list[1]}  ${bfd_name}
    Should Be True  ${out}

#*****************************TestCase6 Keywords**************************************

TC6:creating_vlan
    ${out}=  vlan_config  device1  ${vlan_id}
    Should Be True  ${out}
    ${out}=  vlan_config  device2  ${vlan_id}
    Should Be True  ${out}

TC6:verify_vlan_status
    ${out}=  check_vlan_status  device1  ${vlan_id}  UP  ${device1_interface_1}
    Should Be True  ${out}
    ${out}=  check_vlan_status  device2  ${vlan_id}  UP  ${device2_interface_1}
    Should Be True  ${out}
TC6:ping_test
    ${out}=  ping  device1  device2  ${device1_neighbour1_IP}
    Should Be True  ${out}
    ${out}=  ping  device2  device1  ${device2_neighbour1_IP}
    Should Be True  ${out}
TC6:delete_the_vlan 
    ${out}=  deletingvlan  device1  ${vlan_id}
    Should Be True  ${out}
    ${out}=  deletingvlan  device2  ${vlan_id}
    Should Be True  ${out}
TC6:delete_interface
    ${out}=  deletinginterface  ${device_list[0]}  ${device1_interface_1}
    Should Be True  ${out}
    ${out}=  deletinginterface  ${device_list[1]}  ${device2_interface_1}
    Should Be True  ${out}

TC6:creating_vlan_interface
    ${out}=  creatinginterface  ${device_list[0]}  ${device1_vlan_interface}  ${device1_interface1_device2_interface1}
    Should Be True  ${out}
    ${out}=  creatinginterface  ${device_list[1]}  ${device2_vlan_interface}  ${device2_interface1_device1_interface1}
    Should Be True  ${out}

TC6:Applying_vlan_to_interface
    ${out}=  interface_vlan  ${device_list[0]}  ${vlan_id}  ${device1_interface_1}
    Should Be True  ${out}
    ${out}=  interface_vlan  ${device_list[1]}  ${vlan_id}  ${device2_interface_1}
    Should Be True  ${out}
TC6:delete_vlan_interface
    ${out}=  deletinginterface  ${device_list[0]}  ${device1_vlan_interface}
    Should Be True  ${out}
    Sleep  5s
    ${out}=  deletinginterface  ${device_list[1]}  ${device2_vlan_interface}
    Should Be True  ${out}
TC6:creating_interface
    ${out}=  creatinginterface  ${device_list[0]}  ${device1_interface_1}  ${device1_interface1_device2_interface1}
    Should Be True  ${out}
    ${out}=  creatinginterface  ${device_list[1]}  ${device2_interface_1}  ${device2_interface1_device1_interface1}
    Should Be True  ${out}
TC6:Deleting_vlan_from_interface
    ${out}=  interface_vlan  ${device_list[0]}  ${vlan_id}
    Should Be True  ${out}
    ${out}=  interface_vlan  ${device_list[1]}  ${vlan_id}
    Should Be True  ${out}

#*****************************Test Setup Keywords**************************************

IP_BGP configuration and Flap_verify the interfaces

    
    CHECKPOINT   Enabing the interface state on devices and verifying
    Enabling the Interface

    CHECKPOINT   Load ip configuration on devices and verifying
    Load-Base-configuration_ip
    
    CHECKPOINT   Creating BGP 
    ${out}=  createBGPGlobal  ${device_all}  ${fab_count}  ${csw_count}  ${asw_count}  ${fab}  ${csw}  ${asw}  ${asnum}  ${routerid}  
    Should Be True  ${out}



#*****************************Test Teardown Keywords**************************************

Delete IPv4 interfaces

    CHECKPOINT   Remove ip configuration on devices and verifying
    Remove-Base-configuration_ip
    

