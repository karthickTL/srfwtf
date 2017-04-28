"""
Devices Params file
*******************
"""

"""
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
"""
"""
Device List
"""
DEVICE_LIST = ['device1', 'device2', 'device3', 'device4']

FAB = ["device1"]
CSW = ["device2", "device3"]
ASW = ["device4"]

"""
Autonomous system number
"""
ASNUM = {'device1':"64700", 'device2':"64850", 'device3':"64850", 'device4':"64900"}

"""
Router ID
"""
ROUTERID = {'device1':"10.0.20.0", 'device2':"10.0.20.1", 'device3':"10.0.20.3", 'device4':"10.0.4.1"}

"""
Hostname
"""
HOSTNAME = {
'device1': "curl -X PATCH --header 'Content-Type: application/x-www-form-urlencoded' --header 'Accept: application/json' -d '{\"Hostname\":\"FAB05\"}' 'http://localhost:8080/public/v1/config/SystemParam'",
'device2': "curl -X PATCH --header 'Content-Type: application/x-www-form-urlencoded' --header 'Accept: application/json' -d '{\"Hostname\":\"CSW01\"}' 'http://localhost:8080/public/v1/config/SystemParam'",
'device3': "curl -X PATCH --header 'Content-Type: application/x-www-form-urlencoded' --header 'Accept: application/json' -d '{\"Hostname\":\"CSW02\"}' 'http://localhost:8080/public/v1/config/SystemParam'",
'device4': "curl -X PATCH --header 'Content-Type: application/x-www-form-urlencoded' --header 'Accept: application/json' -d '{\"Hostname\":\"ASW01\"}' 'http://localhost:8080/public/v1/config/SystemParam'"
}


# if yes then it load configuration for all the devices
# if no then it load configuration according to count of fab,csw,asw
DEVICE_ALL = "no"
FAB_COUNT = 1
CSW_COUNT =  2
ASW_COUNT = 1
SUBNET = "/31"
SUBNET_V6 = "/64"
COUNT_ASW_PEERGROUP = 0
NULL = ""

"""
Interfaces of the routers
"""
INTERFACE_DICT = {"device1_device2_eth": "eth25",
                  "device1_device3_eth": "eth35",

                  "device2_device1_eth": "eth45",
                  "device2_device4_eth": "eth55",

                  "device3_device1_eth": "eth65",
                  "device3_device4_eth": "eth75",

                  "device4_device2_eth": "eth85",
                  "device4_device3_eth": "eth95"}


"""
IPv4 address of the routers
"""
INTERFACE_IP_DICT = {'device1_device2_interface_ip ': "10.0.20.0",
                     'device1_device3_interface_ip ': "10.0.20.2",

                     'device2_device1_interface_ip ': "10.0.20.1",
                     'device2_device4_interface_ip ': "10.0.4.0",

                     'device3_device1_interface_ip ': "10.0.20.3",
                     'device3_device4_interface_ip ': "10.0.5.0",

                     'device4_device2_interface_ip ': "10.0.4.1",
                     'device4_device3_interface_ip ': "10.0.5.1"}


"""
IPv6 address of the routers
"""
INTERFACE_IPV6_DICT = {'device1_device2_interface_ip ': "2001::1",
                       'device1_device3_interface_ip ': "2002::1",

                       'device2_device1_interface_ip ': "2001::2",
                       'device2_device4_interface_ip ': "3005::1",

                       'device3_device1_interface_ip ': "2002::2",
                       'device3_device4_interface_ip ': "3006::1",

                       'device4_device2_interface_ip ': "3005::2",
                       'device4_device3_interface_ip ': "3006::2"}


"""
Devices Params file
*******************
"""
"""
DeviceID : device1
DeviceName : FAB05 
Variables :  device1_IP details
"""
# interface
DEVICE1_INTERFACE_1 = "eth25"
DEVICE1_INTERFACE_2 = "eth35"

# IPv4
DEVICE1_INTERFACE1_DEVICE2_INTERFACE1 = "10.0.20.0/31"
DEVICE1_INTERFACE2_DEVICE3_INTERFACE1 = "10.0.20.2/31"
        
# bgp
DEVICE1_ASNUM = "64700"
DEVICE1_ROUTER_ID = "10.0.20.0"
DEVICE1_NEIGHBOUR1_IP = "10.0.20.1"
DEVICE1_NEIGHBOUR2_IP = "10.0.20.3"

# peer_as
DEVICE1_PEER_AS_1 = "64850"
DEVICE1_PEER_AS_2 = "64850"



"""
DeviceID : device2
DeviceName : CSW01 
Variables :  device2_IP details
"""
# Interface
DEVICE2_INTERFACE_1 = "eth45"
DEVICE2_INTERFACE_2 = "eth55"

# IPv4
DEVICE2_INTERFACE1_DEVICE1_INTERFACE1 = "10.0.20.1/31"
DEVICE2_INTERFACE2_DEVICE4_INTERFACE1 = "10.0.4.0/31"

# bgp
DEVICE2_ASNUM = "64850"
DEVICE2_ROUTER_ID = "10.0.20.1"
DEVICE2_NEIGHBOUR1_IP = "10.0.20.0"
DEVICE2_NEIGHBOUR2_IP = "10.0.4.1"

# peer_as
DEVICE2_PEER_AS_1 = "64700"
DEVICE2_PEER_AS_2 = "64900"


"""
DeviceID : device3
DeviceName : csw02 
Variables :  device3_IP details
"""
# Interface
DEVICE3_INTERFACE_1 = "eth65"
DEVICE3_INTERFACE_2 = "eth75"

# IPv4
DEVICE3_INTERFACE1_DEVICE1_INTERFACE2 = "10.0.20.3/31"
DEVICE3_INTERFACE2_DEVICE4_INTERFACE2 = "10.0.5.0/31"

# bgp
DEVICE3_ASNUM = "64850"
DEVICE3_ROUTER_ID = "10.0.20.3"
DEVICE3_NEIGHBOUR1_IP = "10.0.20.2"
DEVICE3_NEIGHBOUR2_IP = "10.0.5.1"

# peer_as
DEVICE3_PEER_AS_1 = "64700"
DEVICE3_PEER_AS_2 = "64900"

"""
DeviceID : device4
DeviceName : asw01
Variables :  device4_IP details
"""
# Interface
DEVICE4_INTERFACE_1 = "eth85"
DEVICE4_INTERFACE_2 = "eth95"

# IPv4
DEVICE4_INTERFACE1_DEVICE2_INTERFACE2 = "10.0.4.1/31"
DEVICE4_INTERFACE2_DEVICE3_INTERFACE2 = "10.0.5.1/31"

# bgp
DEVICE4_ASNUM = "64900"
DEVICE4_ROUTER_ID = "10.0.4.1"
DEVICE4_NEIGHBOUR1_IP = "10.0.4.0"
DEVICE4_NEIGHBOUR2_IP = "10.0.5.0"

# peer_as
DEVICE4_PEER_AS_1 = "64850"
DEVICE4_PEER_AS_2 = "64850"


"""
Testcase Attributes
"""

# peer group
DEVICE1_PEER_AS = "64850"
DEVICE4_PEER_AS = "64850"
PEER_GROUP_ID = "Terra"
PEER_GROUP_NAME = 'peer_group ' + PEER_GROUP_ID
PEER_ATTRIBUTE = 'peer_as ' + DEVICE4_PEER_AS

# password authentication
DEVICE3_AUTH_PASSWORD_1 = "terralogic"
DEVICE3_AUTH_PASSWORD_2 = "test"
DEVICE4_AUTH_PASSWORD_1 = "terralogic"
AUTH_PASSWORD = 'password ' + DEVICE4_AUTH_PASSWORD_1
AUTH_NEW_PASSWORD = 'password ' + DEVICE3_AUTH_PASSWORD_2


# bgp timers
BGP_TIMER1 = "timers_keep_alive 30"
BGP_TIMER2 = "timers_hold_time 100"
KEEP_ALIVE_TIME = "30"
HOLD_TIME = "100"

# static routing
DEVICE1_CONFIGURE_STATIC_ROUTE = "curl -H \"Content-Type: application/json\" -d '{\"DestinationNw\": \"10.0.5.0\", \"NetworkMask\": \"255.255.255.254\", \"Protocol\": \"STATIC\", \"NextHop\": [{\"NextHopIp\": \"10.0.20.3\", \"NextHopIntRef\":\"eth35\"}]}' http://localhost:8080/public/v1/config/IPv4Route"

DEVICE4_CONFIGURE_STATIC_ROUTE = "curl -H \"Content-Type: application/json\" -d '{\"DestinationNw\": \"10.0.20.2\", \"NetworkMask\": \"255.255.255.254\", \"Protocol\": \"STATIC\", \"NextHop\": [{\"NextHopIp\": \"10.0.5.0\", \"NextHopIntRef\":\"eth95\"}]}' http://localhost:8080/public/v1/config/IPv4Route"

DEVICE1_DEST_NETWORK = "10.0.5.0"
DEVICE1_NEXTHOPIP = "10.0.20.3"
DEVICE1_INTERFACE = "eth35"

DEVICE4_DEST_NETWORK = "10.0.20.2"
DEVICE4_NEXTHOPIP = "10.0.5.0"
DEVICE4_INTERFACE = "eth95"

DEVICE4_INTERFACE2_DEVICE3_INTERFACE2_NO_SUBNET = "10.0.5.1"
DEVICE1_INTERFACE2_DEVICE3_INTERFACE1_NO_SUBNET = "10.0.20.2"

# vlan
DEVICE1_VLAN_INTERFACE = "vlan10"
DEVICE2_VLAN_INTERFACE = "vlan10"

DEVICE1_INTERFACE_1_VLAN = "25"
DEVICE2_INTERFACE_1_VLAN = "45"

VLAN_ID = "10"

# BFD
BFD_MODE_DOWN = "shutdown"
BFD_MODE_UP = "noshutdown"
BFD_NAME = "Session2"
MINRX = 150
INTERVAL = 150
MULTIPLIER = 3

# connect_retry

RETRY_TIME = 2
