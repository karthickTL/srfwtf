"""
Devices Params file
*******************
"""
DEVICE_LIST = ['device1', 'device2', 'device3', 'device4', 'device5',
               'device6', 'device7', 'device8', 'device9', 'device10',
               'device11', 'device12', 'device13', 'device14',
               'device15', 'device16']

"""
DeviceID :  device1
DeviceName :  FAB05
Variables :   device1_IP details
"""
ASNUM = {'device1': "64700", 'device2': "64700", 'device3': "64700",
         'device4': "64700", 'device5': "64850", 'device6': "64850",
         'device7': "64850", 'device8': "64850", 'device9': "64851",
         'device10': "64851", 'device11': "64851", 'device12': "64851",
         'device13': "64850", 'device14': "64850", 'device15': "64851",
         'device16': "64851"}

ROUTERID = {'device1': "10.0.20.0", 'device2': "10.0.20.32",
            'device3': "10.0.20.64", 'device4': "10.0.20.96",
            'device5': "10.0.20.1", 'device6': "10.0.20.3",
            'device7': "10.0.20.5", 'device8': "10.0.20.7",
            'device9': "10.0.20.9", 'device10': "10.0.20.11",
            'device11': "10.0.20.13", 'device12': "10.0.20.15",
            'device13': "10.0.4.1", 'device14': "10.0.4.3",
            'device15': "10.0.8.1", 'device16': "10.0.8.3"}


# if yes then it load configuration for all the devices
# if no then it load configuration according to conut of fab,csw,asw
DEVICE_ALL = "yes"
FAB_COUNT = 1
CSW_COUNT = 2
ASW_COUNT = 1
SUBNET = "/31"

INTERFACE_DICT = {"device1_device5_eth": "eth1",
                  "device1_device6_eth": "eth2",
                  "device1_device7_eth": "eth3",
                  "device1_device8_eth": "eth4",
                  "device1_device9_eth": "eth5",
                  "device1_device10_eth": "eth6",
                  "device1_device11_eth": "eth7",
                  "device1_device12_eth": "eth8",

                  "device2_device5_eth": "eth9",
                  "device2_device6_eth": "eth10",
                  "device2_device7_eth": "eth11",
                  "device2_device8_eth": "eth12",
                  "device2_device9_eth": "eth13",
                  "device2_device10_eth": "eth14",
                  "device2_device11_eth": "eth15",
                  "device2_device12_eth": "eth16",

                  "device3_device5_eth": "eth17",
                  "device3_device6_eth": "eth18",
                  "device3_device7_eth": "eth19",
                  "device3_device8_eth": "eth20",
                  "device3_device9_eth": "eth21",
                  "device3_device10_eth": "eth22",
                  "device3_device11_eth": "eth23",
                  "device3_device12_eth": "eth24",

                  "device4_device5_eth": "eth25",
                  "device4_device6_eth": "eth26",
                  "device4_device7_eth": "eth27",
                  "device4_device8_eth": "eth28",
                  "device4_device9_eth": "eth29",
                  "device4_device10_eth": "eth30",
                  "device4_device11_eth": "eth31",
                  "device4_device12_eth": "eth32",

                  "device5_device1_eth": "eth33",
                  "device5_device2_eth": "eth34",
                  "device5_device3_eth": "eth35",
                  "device5_device4_eth": "eth36",
                  "device5_device13_eth": "eth37",
                  "device5_device14_eth": "eth38",

                  "device6_device1_eth": "eth39",
                  "device6_device2_eth": "eth40",
                  "device6_device3_eth": "eth41",
                  "device6_device4_eth": "eth42",
                  "device6_device13_eth": "eth43",
                  "device6_device14_eth": "eth44",

                  "device7_device1_eth": "eth45",
                  "device7_device2_eth": "eth46",
                  "device7_device3_eth": "eth47",
                  "device7_device4_eth": "eth48",
                  "device7_device13_eth": "eth49",
                  "device7_device14_eth": "eth50",

                  "device8_device1_eth": "eth51",
                  "device8_device2_eth": "eth52",
                  "device8_device3_eth": "eth53",
                  "device8_device4_eth": "eth54",
                  "device8_device13_eth": "eth55",
                  "device8_device14_eth": "eth56",

                  "device9_device1_eth": "eth57",
                  "device9_device2_eth": "eth58",
                  "device9_device3_eth": "eth59",
                  "device9_device4_eth": "eth60",
                  "device9_device15_eth": "eth61",
                  "device9_device16_eth": "eth62",

                  "device10_device1_eth": "eth63",
                  "device10_device2_eth": "eth64",
                  "device10_device3_eth": "eth65",
                  "device10_device4_eth": "eth66",
                  "device10_device15_eth": "eth67",
                  "device10_device16_eth": "eth68",

                  "device11_device1_eth": "eth69",
                  "device11_device2_eth": "eth70",
                  "device11_device3_eth": "eth71",
                  "device11_device4_eth": "eth72",
                  "device11_device15_eth": "eth73",
                  "device11_device16_eth": "eth74",

                  "device12_device1_eth": "eth75",
                  "device12_device2_eth": "eth76",
                  "device12_device3_eth": "eth77",
                  "device12_device4_eth": "eth78",
                  "device12_device15_eth": "eth79",
                  "device12_device16_eth": "eth80",

                  "device13_device5_eth": "eth81",
                  "device13_device6_eth": "eth82",
                  "device13_device7_eth": "eth83",
                  "device13_device8_eth": "eth84",

                  "device14_device5_eth": "eth85",
                  "device14_device6_eth": "eth86",
                  "device14_device7_eth": "eth87",
                  "device14_device8_eth": "eth88",

                  "device15_device9_eth": "eth89",
                  "device15_device10_eth": "eth90",
                  "device15_device11_eth": "eth91",
                  "device15_device12_eth": "eth92",

                  "device16_device9_eth": "eth93",
                  "device16_device10_eth": "eth94",
                  "device16_device11_eth": "eth95",
                  "device16_device12_eth": "eth96"}

# FAB05
INTERFACE_IP_DICT = {'device1_device5_interface_ip ': "10.0.20.0",
                     'device1_device6_interface_ip ': "10.0.20.2",
                     'device1_device7_interface_ip ': "10.0.20.4",
                     'device1_device8_interface_ip ': "10.0.20.6",
                     'device1_device9_interface_ip ': "10.0.20.8",
                     'device1_device10_interface_ip ': "10.0.20.10",
                     'device1_device11_interface_ip ': "10.0.20.12",
                     'device1_device12_interface_ip ': "10.0.20.14",

                     'device2_device5_interface_ip ': "10.0.20.32",
                     'device2_device6_interface_ip ': "10.0.20.34",
                     'device2_device7_interface_ip ': "10.0.20.36",
                     'device2_device8_interface_ip ': "10.0.20.38",
                     'device2_device9_interface_ip ': "10.0.20.40",
                     'device2_device10_interface_ip ': "10.0.20.42",
                     'device2_device11_interface_ip ': "10.0.20.44",
                     'device2_device12_interface_ip ': "10.0.20.46",

                     'device3_device5_interface_ip ': "10.0.20.64",
                     'device3_device6_interface_ip ': "10.0.20.66",
                     'device3_device7_interface_ip ': "10.0.20.68",
                     'device3_device8_interface_ip ': "10.0.20.70",
                     'device3_device9_interface_ip ': "10.0.20.72",
                     'device3_device10_interface_ip ': "10.0.20.74",
                     'device3_device11_interface_ip ': "10.0.20.76",
                     'device3_device12_interface_ip ': "10.0.20.78",

                     'device4_device5_interface_ip ': "10.0.20.96",
                     'device4_device6_interface_ip ': "10.0.20.98",
                     'device4_device7_interface_ip ': "10.0.20.100",
                     'device4_device8_interface_ip ': "10.0.20.102",
                     'device4_device9_interface_ip ': "10.0.20.104",
                     'device4_device10_interface_ip ': "10.0.20.106",
                     'device4_device11_interface_ip ': "10.0.20.108",
                     'device4_device12_interface_ip ': "10.0.20.110",

                     'device5_device1_interface_ip ': "10.0.20.1",
                     'device5_device2_interface_ip ': "10.0.20.33",
                     'device5_device3_interface_ip ': "10.0.20.65",
                     'device5_device4_interface_ip ': "10.0.20.97",
                     'device5_device13_interface_ip ': "10.0.4.0",
                     'device5_device14_interface_ip ': "10.0.4.2",

                     'device6_device1_interface_ip ': "10.0.20.3",
                     'device6_device2_interface_ip ': "10.0.20.35",
                     'device6_device3_interface_ip ': "10.0.20.67",
                     'device6_device4_interface_ip ': "10.0.20.99",
                     'device6_device13_interface_ip ': "10.0.5.0",
                     'device6_device14_interface_ip ': "10.0.5.2",

                     'device7_device1_interface_ip ': "10.0.20.5",
                     'device7_device2_interface_ip ': "10.0.20.37",
                     'device7_device3_interface_ip ': "10.0.20.69",
                     'device7_device4_interface_ip ': "10.0.20.101",
                     'device7_device13_interface_ip ': "10.0.6.0",
                     'device7_device14_interface_ip ': "10.0.6.2",

                     'device8_device1_interface_ip ': "10.0.20.7",
                     'device8_device2_interface_ip ': "10.0.20.39",
                     'device8_device3_interface_ip ': "10.0.20.71",
                     'device8_device4_interface_ip ': "10.0.20.103",
                     'device8_device13_interface_ip ': "10.0.7.0",
                     'device8_device14_interface_ip ': "10.0.7.2",

                     'device9_device1_interface_ip ': "10.0.20.9",
                     'device9_device2_interface_ip ': "10.0.20.41",
                     'device9_device3_interface_ip ': "10.0.20.73",
                     'device9_device4_interface_ip ': "10.0.20.105",
                     'device9_device15_interface_ip ': "10.0.8.0",
                     'device9_device16_interface_ip ': "10.0.8.2",

                     'device10_device1_interface_ip ': "10.0.20.11",
                     'device10_device2_interface_ip ': "10.0.20.43",
                     'device10_device3_interface_ip ': "10.0.20.75",
                     'device10_device4_interface_ip ': "10.0.20.107",
                     'device10_device15_interface_ip ': "10.0.9.0",
                     'device10_device16_interface_ip ': "10.0.9.2",

                     'device11_device1_interface_ip ': "10.0.20.13",
                     'device11_device2_interface_ip ': "10.0.20.45",
                     'device11_device3_interface_ip ': "10.0.20.77",
                     'device11_device4_interface_ip ': "10.0.20.109",
                     'device11_device15_interface_ip ': "10.0.10.0",
                     'device11_device16_interface_ip ': "10.0.10.2",

                     'device12_device1_interface_ip ': "10.0.20.15",
                     'device12_device2_interface_ip ': "10.0.20.47",
                     'device12_device3_interface_ip ': "10.0.20.79",
                     'device12_device4_interface_ip ': "10.0.20.111",
                     'device12_device15_interface_ip ': "10.0.11.0",
                     'device12_device16_interface_ip ': "10.0.11.2",

                     'device13_device5_interface_ip ': "10.0.4.1",
                     'device13_device6_interface_ip ': "10.0.5.1",
                     'device13_device7_interface_ip ': "10.0.6.1",
                     'device13_device8_interface_ip ': "10.0.7.1",

                     'device14_device5_interface_ip ': "10.0.4.3",
                     'device14_device6_interface_ip ': "10.0.5.3",
                     'device14_device7_interface_ip ': "10.0.6.3",
                     'device14_device8_interface_ip ': "10.0.7.3",

                     'device15_device9_interface_ip ': "10.0.8.1",
                     'device15_device10_interface_ip ': "10.0.9.1",
                     'device15_device11_interface_ip ': "10.0.10.1",
                     'device15_device12_interface_ip ': "10.0.11.1",

                     'device16_device9_interface_ip ': "10.0.8.3",
                     'device16_device10_interface_ip ': "10.0.9.3",
                     'device16_device11_interface_ip ': "10.0.10.3",
                     'device16_device12_interface_ip ': "10.0.11.3"}

FAB = ["device1", "device2", "device3", "device4"]
CSW = ["device5", "device6", "device7", "device8", "device9",
       "device10", "device11", "device12"]
ASW = ["device13", "device14", "device15", "device16"]


# bgp policy creation
CONDITION_NAME = 'PeerNetwork'
CONDITIONTYPE = 'MatchProtocol'
PROTOCOL = 'CONNECTED'
IPPREFIX = ''
MASKLENGTHRANGE = ''
PREFIXSET = ''

STMT_NAME = 'PeerPolicyStatement'
ACTION = 'permit'
MATCHCONDITIONS = 'any'

POL_DEF_NAME = 'PeerPolicy'
PRIORITY = '1'
MATCHTYPE = 'all'
POLICYTYPE = 'ALL'



#TriggerLink Failure
DEVICE = "device16"
DESTINATION_NETWORK = "10.0.4.0/31"
