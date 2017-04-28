"""
Devices Params file
*******************
"""

"""
if yes then it load configuration for all the devices
if no then it load configuration according to conut of fab,csw,asw
"""

DEVICE_ALL = "no"
FAB_COUNT = 1
CSW_COUNT = 2
ASW_COUNT = 1
SUBNET = "/31"


"""
Device List
"""
DEVICE_LIST = ['device1', 'device2', 'device3', 'device4',
               'device5', 'device6', 'device7', 'device8',
               'device9', 'device10', 'device11', 'device12',
               'device13', 'device14', 'device15', 'device16']

"""
DeviceID : device1
DeviceName : FAB05
Variables :  device1_IP details
"""

HOSTNAME = {
    'device1': "curl -X PATCH --header 'Content-Type: application/x-www-form-urlencoded' --header 'Accept: application/json' -d '{\"Hostname\":\"FAB05\"}' 'http://localhost:8080/public/v1/config/SystemParam'",
    'device2': "curl -X PATCH --header 'Content-Type: application/x-www-form-urlencoded' --header 'Accept: application/json' -d '{\"Hostname\":\"FAB06\"}' 'http://localhost:8080/public/v1/config/SystemParam'",
    'device3': "curl -X PATCH --header 'Content-Type: application/x-www-form-urlencoded' --header 'Accept: application/json' -d '{\"Hostname\":\"FAB07\"}' 'http://localhost:8080/public/v1/config/SystemParam'",
    'device4': "curl -X PATCH --header 'Content-Type: application/x-www-form-urlencoded' --header 'Accept: application/json' -d '{\"Hostname\":\"FAB08\"}' 'http://localhost:8080/public/v1/config/SystemParam'",
    'device5': "curl -X PATCH --header 'Content-Type: application/x-www-form-urlencoded' --header 'Accept: application/json' -d '{\"Hostname\":\"CSW01\"}' 'http://localhost:8080/public/v1/config/SystemParam'",
    'device6': "curl -X PATCH --header 'Content-Type: application/x-www-form-urlencoded' --header 'Accept: application/json' -d '{\"Hostname\":\"CSW02\"}' 'http://localhost:8080/public/v1/config/SystemParam'",
    'device7': "curl -X PATCH --header 'Content-Type: application/x-www-form-urlencoded' --header 'Accept: application/json' -d '{\"Hostname\":\"CSW03\"}' 'http://localhost:8080/public/v1/config/SystemParam'",
    'device8': "curl -X PATCH --header 'Content-Type: application/x-www-form-urlencoded' --header 'Accept: application/json' -d '{\"Hostname\":\"CSW04\"}' 'http://localhost:8080/public/v1/config/SystemParam'",
    'device9': "curl -X PATCH --header 'Content-Type: application/x-www-form-urlencoded' --header 'Accept: application/json' -d '{\"Hostname\":\"CSW05\"}' 'http://localhost:8080/public/v1/config/SystemParam'",
    'device10': "curl -X PATCH --header 'Content-Type: application/x-www-form-urlencoded' --header 'Accept: application/json' -d '{\"Hostname\":\"CSW06\"}' 'http://localhost:8080/public/v1/config/SystemParam'",
    'device11': "curl -X PATCH --header 'Content-Type: application/x-www-form-urlencoded' --header 'Accept: application/json' -d '{\"Hostname\":\"CSW07\"}' 'http://localhost:8080/public/v1/config/SystemParam'",
    'device12': "curl -X PATCH --header 'Content-Type: application/x-www-form-urlencoded' --header 'Accept: application/json' -d '{\"Hostname\":\"CSW08\"}' 'http://localhost:8080/public/v1/config/SystemParam'",
    'device13': "curl -X PATCH --header 'Content-Type: application/x-www-form-urlencoded' --header 'Accept: application/json' -d '{\"Hostname\":\"ASW01\"}' 'http://localhost:8080/public/v1/config/SystemParam'",
    'device14': "curl -X PATCH --header 'Content-Type: application/x-www-form-urlencoded' --header 'Accept: application/json' -d '{\"Hostname\":\"ASW02\"}' 'http://localhost:8080/public/v1/config/SystemParam'",
    'device15': "curl -X PATCH --header 'Content-Type: application/x-www-form-urlencoded' --header 'Accept: application/json' -d '{\"Hostname\":\"ASW03\"}' 'http://localhost:8080/public/v1/config/SystemParam'",
    'device16': "curl -X PATCH --header 'Content-Type: application/x-www-form-urlencoded' --header 'Accept: application/json' -d '{\"Hostname\":\"ASW04\"}' 'http://localhost:8080/public/v1/config/SystemParam'"}


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



FAB = ["device1", "device2", "device3", "device4"]
CSW = ["device5", "device6", "device7", "device8",
       "device9", "device10", "device11", "device12"]
ASW = ["device13", "device14", "device15", "device16"]


PATH = '/home/openswitch/Downloads/srfwtf/OpenSnaproute_Testscripts/LLDPV2/LSNC_Lab_Access_NSI_for_TerraLogic.xlsx'
SHEET_NAME = "NSI"
