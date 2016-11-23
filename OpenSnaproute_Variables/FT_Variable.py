'''
Topology diagram :
---------------------------------------5-NODES-OpenSwitch TOPOLOGY----------------------

 	NODES : #FAB05, #FAB06, #CSW01, #CSW02, #ASW01

				 	1.1.1.1/32
						|   # 64700
                                              FAB05--------------FAB06
	10.0.20.0/31			    .0|    |.2			10.0.20.2/31
  				|--------------    -----------------
			      .1|				    |.3
                  #64850     CSW01                                CSW02  #64850
			     .0	|				     |.0
				|				     |
				----------------     ----------------
	10.0.4.0/31			     .1	|    | .1		10.0.5.0/31
						 ASW01   #64900
-----------------------------------------------------------------------------------------
'''
'''
Devices Params file
*******************
'''
'''
Device List
'''
device_list=['device1','device2','device3','device4']

fab=["device1"]
csw=["device2","device3"]
asw=["device4"]

'''
Autonomous system number
'''
asnum={'device1':"64700",'device2':"64850",'device3':"64850",'device4':"64900"}

'''
Router ID
'''
routerid={'device1':"10.0.20.0",'device2':"10.0.20.1",'device3':"10.0.20.3",'device4':"10.0.4.1"}

'''
Hostname
'''
hostname={
'device1':"curl -X PATCH --header 'Content-Type: application/x-www-form-urlencoded' --header 'Accept: application/json' -d '{\"Hostname\":\"FAB05\"}' 'http://localhost:8080/public/v1/config/SystemParam'",
'device2':"curl -X PATCH --header 'Content-Type: application/x-www-form-urlencoded' --header 'Accept: application/json' -d '{\"Hostname\":\"CSW01\"}' 'http://localhost:8080/public/v1/config/SystemParam'",
'device3':"curl -X PATCH --header 'Content-Type: application/x-www-form-urlencoded' --header 'Accept: application/json' -d '{\"Hostname\":\"CSW02\"}' 'http://localhost:8080/public/v1/config/SystemParam'",
'device4':"curl -X PATCH --header 'Content-Type: application/x-www-form-urlencoded' --header 'Accept: application/json' -d '{\"Hostname\":\"ASW01\"}' 'http://localhost:8080/public/v1/config/SystemParam'"
}


#if yes then it load configuration for all the devices
#if no then it load configuration according to count of fab,csw,asw
device_all="no"
fab_count = 1
csw_count =  2
asw_count = 1
subnet = "/31"
subnet_v6 = "/64"
count_asw_peergroup=0
null = ""

'''
Interfaces of the routers
'''
interface_dict={"device1_device2_eth":"eth25",
"device1_device3_eth":"eth35",

"device2_device1_eth":"eth45",
"device2_device4_eth":"eth55",

"device3_device1_eth":"eth65",
"device3_device4_eth":"eth75",

"device4_device2_eth":"eth85",
"device4_device3_eth":"eth95"}


'''
IPv4 address of the routers
'''
interface_ip_dict={'device1_device2_interface_ip ':"10.0.20.0",
'device1_device3_interface_ip ':"10.0.20.2",

'device2_device1_interface_ip ':"10.0.20.1",
'device2_device4_interface_ip ':"10.0.4.0",

'device3_device1_interface_ip ':"10.0.20.3",
'device3_device4_interface_ip ':"10.0.5.0",

'device4_device2_interface_ip ':"10.0.4.1",
'device4_device3_interface_ip ':"10.0.5.1"}


'''
IPv6 address of the routers
'''
interface_ipv6_dict={'device1_device2_interface_ip ':"2001::1",
'device1_device3_interface_ip ':"2002::1",

'device2_device1_interface_ip ':"2001::2",
'device2_device4_interface_ip ':"3005::1",

'device3_device1_interface_ip ':"2002::2",
'device3_device4_interface_ip ':"3006::1",

'device4_device2_interface_ip ':"3005::2",
'device4_device3_interface_ip ':"3006::2"}


'''
Devices Params file
*******************
'''
'''
DeviceID : device1
DeviceName : FAB05 
Variables :  device1_IP details
'''
#interface
device1_interface_1="eth25"
device1_interface_2="eth35"

# IPv4
device1_interface1_device2_interface1="10.0.20.0/31"
device1_interface2_device3_interface1="10.0.20.2/31"
        
#bgp
device1_asnum="64700"
device1_router_id="10.0.20.0"
device1_neighbour1_IP="10.0.20.1"
device1_neighbour2_IP="10.0.20.3"

#peer_as
device1_peer_as_1="64850"
device1_peer_as_2="64850"



'''
DeviceID : device2
DeviceName : CSW01 
Variables :  device2_IP details
'''
#Interface
device2_interface_1="eth45"
device2_interface_2="eth55"

#IPv4
device2_interface1_device1_interface1="10.0.20.1/31"
device2_interface2_device4_interface1="10.0.4.0/31"

#bgp
device2_asnum="64850"
device2_router_id="10.0.20.1"
device2_neighbour1_IP="10.0.20.0"
device2_neighbour2_IP="10.0.4.1"

#peer_as
device2_peer_as_1="64700"
device2_peer_as_2="64900"


'''
DeviceID : device3
DeviceName : csw02 
Variables :  device3_IP details
'''
#Interface
device3_interface_1="eth65"
device3_interface_2="eth75"

#IPv4
device3_interface1_device1_interface2="10.0.20.3/31"
device3_interface2_device4_interface2="10.0.5.0/31"

#bgp
device3_asnum="64850"
device3_router_id="10.0.20.3"
device3_neighbour1_IP="10.0.20.2"
device3_neighbour2_IP="10.0.5.1"

#peer_as
device3_peer_as_1="64700"
device3_peer_as_2="64900"

'''
DeviceID : device4
DeviceName : asw01
Variables :  device4_IP details
'''
#Interface
device4_interface_1="eth85"
device4_interface_2="eth95"

#IPv4
device4_interface1_device2_interface2="10.0.4.1/31"
device4_interface2_device3_interface2="10.0.5.1/31"

#bgp
device4_asnum="64900"
device4_router_id="10.0.4.1"
device4_neighbour1_IP="10.0.4.0"
device4_neighbour2_IP="10.0.5.0"

#peer_as
device4_peer_as_1="64850"
device4_peer_as_2="64850"


'''
Testcase Attributes
'''

#peer group
device1_peer_as = "64850"
device4_peer_as = "64850"
peer_group_id="Terra"
Peer_group_name='peer_group '+peer_group_id
Peer_attribute ='peer_as '+device4_peer_as

#password authentication
device3_auth_Password_1="terralogic"
device3_auth_Password_2="test"
device4_auth_Password_1="terralogic"
Auth_password='password '+device4_auth_Password_1
Auth_new_password='password '+device3_auth_Password_2


#bgp timers
bgp_timer1="timers_keep_alive 30"
bgp_timer2="timers_hold_time 100"
keep_alive_time="30"
hold_time="100"

#static routing
device1_configure_static_route = "curl -H \"Content-Type: application/json\" -d '{\"DestinationNw\": \"10.0.5.0\", \"NetworkMask\": \"255.255.255.254\", \"Protocol\": \"STATIC\", \"NextHop\": [{\"NextHopIp\": \"10.0.20.3\", \"NextHopIntRef\":\"eth35\"}]}' http://localhost:8080/public/v1/config/IPv4Route"

device4_configure_static_route = "curl -H \"Content-Type: application/json\" -d '{\"DestinationNw\": \"10.0.20.2\", \"NetworkMask\": \"255.255.255.254\", \"Protocol\": \"STATIC\", \"NextHop\": [{\"NextHopIp\": \"10.0.5.0\", \"NextHopIntRef\":\"eth95\"}]}' http://localhost:8080/public/v1/config/IPv4Route"

device1_dest_network="10.0.5.0"
device1_nextHopIp="10.0.20.3"
device1_interface="eth35"

device4_dest_network="10.0.20.2"
device4_nextHopIp="10.0.5.0"
device4_interface="eth95"

device4_interface2_device3_interface2_no_subnet="10.0.5.1"
device1_interface2_device3_interface1_no_subnet="10.0.20.2"

#vlan
device1_vlan_interface="vlan10"
device2_vlan_interface="vlan10"

device1_interface_1_vlan="25"
device2_interface_1_vlan="45"  

vlan_id="10"

#BFD
bfd_mode_down="shutdown"
bfd_mode_up="noshutdown"
bfd_name="Session2"
minrx=150
interval=150 
multiplier=3

