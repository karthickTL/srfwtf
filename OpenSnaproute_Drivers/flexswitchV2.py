#!/usr/bin/python
"""
flexswitchv2.py
"""
import requests
import json
import urllib2
from requests.packages.urllib3.exceptions import InsecureRequestWarning

HEADERS = {'Accept': 'application/json', 'Content-Type': 'application/json'}
PATCHHEADERS = {'Conent-Type': 'application/json-patch+json'}


class FlexSwitch(object):
    httpSuccessCodes = [200, 201, 202, 204]

    def __init__(self, ip, port, user=None, passwd=None, timeout=15):
        self.ip = ip
        self.port = port
        self.timeout = timeout
        self.authenticate = False
        if user is not None:
            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
            self.authenticate = True
            self.user = user
            self.passwd = passwd
            self.cfg_url_base = 'https://%s/public/v1/config/' % ip
            self.state_url_base = 'https://%s/public/v1/state/' % ip
            self.action_url_base = 'https://%s/public/v1/action/' % ip
        else:
            self.cfg_url_base = 'http://%s:%s/public/v1/config/' % (ip, str(port))
            self.state_url_base = 'http://%s:%s/public/v1/state/' % (ip, str(port))
            self.action_url_base = 'http://%s:%s/public/v1/action/' % (ip, str(port))

    def create_policy_stmt(self, name, conditions, action='deny', match_conditions='all'):
        """
           .. automethod :: createpolicystmt(self,
               :param string name : Policy Statement Name Policy Statement Name
               :param string conditions : List of conditions added to this policy statement List of conditions added to this policy statement
               :param string action : Action for this policy statement Action for this policy statement
               :param string match_conditions : Specifies whether to match all/any of the conditions of this policy statement Specifies whether to match all/any of the conditions of this policy statement

        """
        obj = {
                'Name': name,
                'Conditions': conditions,
                'Action': action,
                'MatchConditions': match_conditions,
                }
        req_url = self.cfg_url_base+'PolicyStmt'
        if self.authenticate:
            r = requests.post(req_url, data=json.dumps(obj), headers=HEADERS, timeout=self.timeout, auth=(self.user, self.passwd), verify=False)
        else:
            r = requests.post(req_url, data=json.dumps(obj), headers=HEADERS, timeout=self.timeout)
        return r

    def create_vlan(self, vlan_id, intf_list, untag_intf_list, admin_state='UP'):
        """
            .. automethod :: create_vlan(self,
                :param int32 vlan_id : 802.1Q tag/Vlan ID for vlan being provisioned 802.1Q tag/Vlan ID for vlan being provisioned
                :param string intf_list : List of interface names or ifindex values to  be added as tagged members of the vlan List of interface names or ifindex values to  be added as tagged members of the vlan
                :param string untag_intf_list : List of interface names or ifindex values to  be added as untagged members of the vlan List of interface names or ifindex values to  be added as untagged members of the vlan
                :param string admin_state : Administrative state of this vlan interface Administrative state of this vlan interface

        """
        obj = {
                'VlanId': int(vlan_id),
                'IntfList': intf_list,
                'UntagIntfList': untag_intf_list,
                'AdminState': admin_state,
                }
        req_url = self.cfg_url_base+'Vlan'
        if self.authenticate:
            r = requests.post(req_url, data=json.dumps(obj), headers=HEADERS, timeout=self.timeout, auth=(self.user, self.passwd), verify=False)
        else:
            r = requests.post(req_url, data=json.dumps(obj), headers=HEADERS, timeout=self.timeout)
        return r

    def delete_vlan(self, vlan_id):
        obj = {
                'VlanId': vlan_id,
                }
        req_url = self.cfg_url_base+'Vlan'
        if self.authenticate:
            r = requests.delete(req_url, data=json.dumps(obj), headers=HEADERS, timeout=self.timeout, auth=(self.user, self.passwd), verify=False)
        else:
            r = requests.delete(req_url, data=json.dumps(obj), headers=HEADERS, timeout=self.timeout)
        return r

    def update_vlan(self,
                   vlan_id,
                   intf_list=None,
                   untag_intf_list=None,
                   admin_state=None):
        obj = {}
        if vlan_id is not None:
            obj['VlanId'] = int(vlan_id)

        if intf_list is not None:
            obj['IntfList'] = intf_list

        if untag_intf_list is not None:
            obj['UntagIntfList'] = untag_intf_list

        if admin_state is not None:
            obj['AdminState'] = admin_state

        req_url = self.cfg_url_base+'Vlan'
        if self.authenticate:
            r = requests.patch(req_url, data=json.dumps(obj), headers=HEADERS, timeout=self.timeout, auth=(self.user, self.passwd), verify=False)
        else:
            r = requests.patch(req_url, data=json.dumps(obj), headers=HEADERS, timeout=self.timeout)
        return r

    def get_all_bgpv4_neighbor_states(self):
        return self.get_objects('BGPv4Neighbor', self.state_url_base)

    def create_bgpv4_neighbor(self,
                            intf_ref,
                            neighbor_address,
                            description='',
                            peer_group='',
                            peer_as='',
                            local_as='',
                            update_source='',
                            auth_password='',
                            adj_rib_in_filter='',
                            adj_rib_out_filter='',
                            bfd_enable=False,
                            multi_hop_ttl=0,
                            keep_alive_time=0,
                            add_paths_rx=False,
                            route_reflector_client=False,
                            max_prefixes_restart_timer=0,
                            multi_hop_enable=False,
                            route_reflector_cluster_id=0,
                            max_prefixes_disconnect=False,
                            add_paths_max_tx=0,
                            max_prefixes=0,
                            max_prefixes_threshold_pct=80,
                            bfd_session_param='default',
                            disabled=False,
                            hold_time=0,
                            connect_retry_time=0):
        """
           automethod :: create_bgpv4_neighbor(self,
            :param string intf_ref : Interface of the BGP neighbor Interface of the BGP neighbor
            :param string neighbor_address : Address of the BGP neighbor Address of the BGP neighbor
            :param string description : Description of the BGP neighbor Description of the BGP neighbor
            :param string peer_group : Peer group of the BGP neighbor Peer group of the BGP neighbor
            :param string peer_as : Peer AS of the BGP neighbor Peer AS of the BGP neighbor
            :param string local_as : Local AS of the BGP neighbor Local AS of the BGP neighbor
            :param string update_source : Source IP to connect to the BGP neighbor Source IP to connect to the BGP neighbor
            :param string auth_password : Password to connect to the BGP neighbor Password to connect to the BGP neighbor
            :param string adj_rib_in_filter : Policy that is applied for Adj-RIB-In prefix filtering Policy that is applied for Adj-RIB-In prefix filtering
            :param string adj_rib_out_filter : Policy that is applied for Adj-RIB-Out prefix filtering Policy that is applied for Adj-RIB-Out prefix filtering
            :param bool bfd_enable : Enable/Disable BFD for the BGP neighbor Enable/Disable BFD for the BGP neighbor
            :param uint8 multi_hop_ttl : TTL for multi hop BGP neighbor TTL for multi hop BGP neighbor
            :param uint32 keep_alive_time : Keep alive time for the BGP neighbor Keep alive time for the BGP neighbor
            :param bool add_paths_rx : Receive additional paths from BGP neighbor Receive additional paths from BGP neighbor
            :param bool route_reflector_client : Set/Clear BGP neighbor as a route reflector client Set/Clear BGP neighbor as a route reflector client
            :param uint8 max_prefixes_restart_timer : Time in seconds to wait before we start BGP peer session when we receive max prefixes Time in seconds to wait before we start BGP peer session when we receive max prefixes
            :param bool multi_hop_enable : Enable/Disable multi hop for BGP neighbor Enable/Disable multi hop for BGP neighbor
            :param uint32 route_reflector_cluster_id : Cluster Id of the internal BGP neighbor route reflector client Cluster Id of the internal BGP neighbor route reflector client
            :param bool max_prefixes_disconnect : Disconnect the BGP peer session when we receive the max prefixes from the neighbor Disconnect the BGP peer session when we receive the max prefixes from the neighbor
            :param uint8 add_paths_max_tx : Max number of additional paths that can be transmitted to BGP neighbor Max number of additional paths that can be transmitted to BGP neighbor
            :param uint32 max_prefixes : Maximum number of prefixes that can be received from the BGP neighbor Maximum number of prefixes that can be received from the BGP neighbor
            :param uint8 max_prefixes_threshold_pct : The percentage of maximum prefixes before we start logging The percentage of maximum prefixes before we start logging
            :param string bfd_session_param : Bfd session param name to be applied Bfd session param name to be applied
            :param bool disabled : Enable/Disable the BGP neighbor Enable/Disable the BGP neighbor
            :param uint32 hold_time : Hold time for the BGP neighbor Hold time for the BGP neighbor
            :param uint32 connect_retry_time : Connect retry time to connect to BGP neighbor after disconnect Connect retry time to connect to BGP neighbor after disconnect

        """
        obj = {
                'IntfRef': intf_ref,
                'NeighborAddress': neighbor_address,
                'Description': description,
                'PeerGroup': peer_group,
                'PeerAS': peer_as,
                'LocalAS': local_as,
                'UpdateSource': update_source,
                'AuthPassword': auth_password,
                'AdjRIBInFilter': adj_rib_in_filter,
                'AdjRIBOutFilter': adj_rib_out_filter,
                'BfdEnable': True if bfd_enable else False,
                'MultiHopTTL': int(multi_hop_ttl),
                'KeepaliveTime': int(keep_alive_time),
                'AddPathsRx': True if add_paths_rx else False,
                'RouteReflectorClient': True if route_reflector_client else False,
                'MaxPrefixesRestartTimer': int(max_prefixes_restart_timer),
                'MultiHopEnable': True if multi_hop_enable else False,
                'RouteReflectorClusterId': int(route_reflector_cluster_id),
                'MaxPrefixesDisconnect': True if max_prefixes_disconnect else False,
                'AddPathsMaxTx': int(add_paths_max_tx),
                'MaxPrefixes': int(max_prefixes),
                'MaxPrefixesThresholdPct': int(max_prefixes_threshold_pct),
                'BfdSessionParam': bfd_session_param,
                'Disabled': True if disabled else False,
                'HoldTime': int(hold_time),
                'ConnectRetryTime': int(connect_retry_time),
                }
        req_url = self.cfg_url_base+'BGPv4Neighbor'
        if self.authenticate:
            r = requests.post(req_url, data=json.dumps(obj), headers=HEADERS, timeout=self.timeout, auth=(self.user, self.passwd), verify=False)
        else:
            r = requests.post(req_url, data=json.dumps(obj), headers=HEADERS, timeout=self.timeout)
        return r

    def delete_bgpv4_neighbor(self, intf_ref, neighbor_address):
        obj = {
                'IntfRef': intf_ref,
                'NeighborAddress': neighbor_address,
                }
        req_url = self.cfg_url_base+'BGPv4Neighbor'
        if self.authenticate:
            r = requests.delete(req_url, data=json.dumps(obj), headers=HEADERS, timeout=self.timeout, auth=(self.user, self.passwd), verify=False)
        else:
            r = requests.delete(req_url, data=json.dumps(obj), headers=HEADERS, timeout=self.timeout)
        return r

    def update_bgpv4_neighbor(self,
                            intf_ref,
                            neighbor_address,
                            description=None,
                            peer_group=None,
                            peer_as=None,
                            local_as=None,
                            update_source=None,
                            auth_password=None,
                            adj_rib_in_filter=None,
                            adj_rib_out_filter=None,
                            bfd_enable=None,
                            multi_hop_ttl=None,
                            keep_alive_time=None,
                            add_paths_rx=None,
                            route_reflector_client=None,
                            max_prefixes_restart_timer=None,
                            multi_hop_enable=None,
                            route_reflector_cluster_id=None,
                            max_prefixes_disconnect=None,
                            add_paths_max_tx=None,
                            max_prefixes=None,
                            max_prefixes_threshold_pct=None,
                            bfd_session_param=None,
                            disabled=None,
                            hold_time=None,
                            connect_retry_time=None):
        obj = {}
        if intf_ref is not None:
            obj['IntfRef'] = intf_ref

        if neighbor_address is not None:
            obj['NeighborAddress'] = neighbor_address

        if description is not None:
            obj['Description'] = description

        if peer_group is not None:
            obj['PeerGroup'] = peer_group

        if peer_as is not None:
            obj['PeerAS'] = peer_as

        if local_as is not None:
            obj['LocalAS'] = local_as

        if update_source is not None:
            obj['UpdateSource'] = update_source

        if auth_password is not None:
            obj['AuthPassword'] = auth_password

        if adj_rib_in_filter is not None:
            obj['AdjRIBInFilter'] = adj_rib_in_filter

        if adj_rib_out_filter is not None:
            obj['AdjRIBOutFilter'] = adj_rib_out_filter

        if bfd_enable is not None:
            obj['BfdEnable'] = True if bfd_enable else False

        if multi_hop_ttl is not None:
            obj['MultiHopTTL'] = int(multi_hop_ttl)

        if keep_alive_time is not None:
            obj['KeepaliveTime'] = int(keep_alive_time)

        if add_paths_rx is not None:
            obj['AddPathsRx'] = True if add_paths_rx else False

        if route_reflector_client is not None:
            obj['RouteReflectorClient'] = True if route_reflector_client else False

        if max_prefixes_restart_timer is not None:
            obj['MaxPrefixesRestartTimer'] = int(max_prefixes_restart_timer)

        if multi_hop_enable is not None:
            obj['MultiHopEnable'] = True if multi_hop_enable else False

        if route_reflector_cluster_id is not None:
            obj['RouteReflectorClusterId'] = int(route_reflector_cluster_id)

        if max_prefixes_disconnect is not None:
            obj['MaxPrefixesDisconnect'] = True if max_prefixes_disconnect else False

        if add_paths_max_tx is not None:
            obj['AddPathsMaxTx'] = int(add_paths_max_tx)

        if max_prefixes is not None:
            obj['MaxPrefixes'] = int(max_prefixes)

        if max_prefixes_threshold_pct is not None:
            obj['MaxPrefixesThresholdPct'] = int(max_prefixes_threshold_pct)

        if bfd_session_param is not None:
            obj['BfdSessionParam'] = bfd_session_param

        if disabled is not None:
            obj['Disabled'] = True if disabled else False

        if hold_time is not None:
            obj['HoldTime'] = int(hold_time)

        if connect_retry_time is not None:
            obj['ConnectRetryTime'] = int(connect_retry_time)

        req_url = self.cfg_url_base+'BGPv4Neighbor'
        if self.authenticate:
            r = requests.patch(req_url, data=json.dumps(obj), headers=HEADERS, timeout=self.timeout, auth=(self.user, self.passwd), verify=False)
        else:
            r = requests.patch(req_url, data=json.dumps(obj), headers=HEADERS, timeout=self.timeout)
        return r

    def create_bfd_session_param(self,
                              name,
                              required_min_rx_interval=1000,
                              auth_data='snaproute',
                              demand_enabled=False,
                              auth_key_id=1,
                              auth_type='simple',
                              desired_min_tx_interval=1000,
                              authentication_enabled=False,
                              required_min_echo_rx_interval=0,
                              local_multiplier=3):
        """
            .. automethod :: createbfdsessionparam(self,
                :param string name : Session parameters Session parameters
                :param uint32 required_min_rx_interval : Required minimum rx interval in ms Required minimum rx interval in ms
                :param string auth_data : Authentication password Authentication password
                :param bool demand_enabled : Enable or disable demand mode Enable or disable demand mode
                :param uint32 auth_key_id : Authentication key id Authentication key id
                :param string auth_type : Authentication type Authentication type
                :param uint32 desired_min_tx_interval : Desired minimum tx interval in ms Desired minimum tx interval in ms
                :param bool authentication_enabled : Enable or disable authentication Enable or disable authentication
                :param uint32 required_min_echo_rx_interval : Required minimum echo rx interval in ms Required minimum echo rx interval in ms
                :param uint32 local_multiplier : Detection multiplier Detection multiplier

        """
        obj = {
                'Name': name,
                'RequiredMinRxInterval': int(required_min_rx_interval),
                'AuthData': auth_data,
                'DemandEnabled': True if demand_enabled else False,
                'AuthKeyId': int(auth_key_id),
                'AuthType': auth_type,
                'DesiredMinTxInterval': int(desired_min_tx_interval),
                'AuthenticationEnabled': True if authentication_enabled else False,
                'RequiredMinEchoRxInterval': int(required_min_echo_rx_interval),
                'LocalMultiplier': int(local_multiplier),
                }
        req_url = self.cfg_url_base+'BfdSessionParam'
        if self.authenticate:
            r = requests.post(req_url, data=json.dumps(obj), headers=HEADERS, timeout=self.timeout, auth=(self.user, self.passwd), verify=False)
        else:
            r = requests.post(req_url, data=json.dumps(obj), headers=HEADERS, timeout=self.timeout)
        return r

    def delete_bfd_session_param(self, name):
        obj = {
                'Name': name,
                }
        req_url = self.cfg_url_base+'BfdSessionParam'
        if self.authenticate:
            r = requests.delete(req_url, data=json.dumps(obj), headers=HEADERS, timeout=self.timeout, auth=(self.user, self.passwd), verify=False)
        else:
            r = requests.delete(req_url, data=json.dumps(obj), headers=HEADERS, timeout=self.timeout)
        return r

    def create_policy_definition(self,
                               name,
                               priority,
                               statement_list,
                               match_type='all',
                               policy_type='ALL'):
        """
         .. automethod :: createpolicydefinition(self,
             :param string name : Policy Name Policy Name
             :param int32 priority : Priority of the policy w.r.t other policies configured Priority of the policy w.r.t other policies configured
             :param PolicyDefinitionStmtPriority statement_list : Specifies list of statements along with their precedence order. Specifies list of statements along with their precedence order.
             :param string match_type : Specifies whether to match all/any of the statements within this policy Specifies whether to match all/any of the statements within this policy
             :param string policy_type : Specifies the intended protocol application for the policy Specifies the intended protocol application for the policy

        """
        obj = {
                'Name': name,
                'Priority': int(priority),
                'StatementList': statement_list,
                'MatchType': match_type,
                'PolicyType': policy_type,
                }
        req_url = self.cfg_url_base+'PolicyDefinition'
        if self.authenticate:
            r = requests.post(req_url, data=json.dumps(obj), headers=HEADERS, timeout=self.timeout, auth=(self.user, self.passwd), verify=False)
        else:
            r = requests.post(req_url, data=json.dumps(obj), headers=HEADERS, timeout=self.timeout)
        return r

    def create_logical_intf(self, name, type='Loopback'):
        """
        .. automethod :: createlogicalintf(self,
            :param string name : Name of logical interface Name of logical interface
            :param string type : Type of logical interface (e.x. loopback) Type of logical interface (e.x. loopback)

        """
        obj = {
                'Name': name,
                'Type': type,
                }
        req_url = self.cfg_url_base+'LogicalIntf'
        if self.authenticate:
            r = requests.post(req_url, data=json.dumps(obj), headers=HEADERS, timeout=self.timeout, auth=(self.user, self.passwd), verify=False)
        else:
            r = requests.post(req_url, data=json.dumps(obj), headers=HEADERS, timeout=self.timeout)
        return r

    def delete_logical_intf(self, name):
        obj = {
                'Name': name,
                }
        req_url = self.cfg_url_base+'LogicalIntf'
        if self.authenticate:
            r = requests.delete(req_url, data=json.dumps(obj), headers=HEADERS, timeout=self.timeout, auth=(self.user, self.passwd), verify=False)
        else:
            r = requests.delete(req_url, data=json.dumps(obj), headers=HEADERS, timeout=self.timeout)
        return r

    def get_all_bgpv6_neighbor_states(self):
        return self.get_objects('BGPv6Neighbor', self.state_url_base)

    def create_bgpv4_peer_group(self,
                             name,
                             peer_as='',
                             local_as='',
                             update_source='',
                             auth_password='',
                             description='',
                             adj_rib_in_filter='',
                             adj_rib_out_filter='',
                             max_prefixes_restart_timer=0,
                             multi_hop_enable=False,
                             max_prefixes_disconnect=False,
                             multi_hop_ttl=0,
                             keep_alive_time=0,
                             route_reflector_cluster_id=0,
                             max_prefixes=0,
                             add_paths_max_tx=0,
                             add_paths_rx=False,
                             route_reflector_client=False,
                             max_prefixes_threshold_pct=80,
                             hold_time=0,
                             connect_retry_time=0):
        """
        .. automethod :: createbgpv4peergroup(self,
            :param string name : Name of the BGP peer group Name of the BGP peer group
            :param string peer_as : Peer AS of the BGP neighbor Peer AS of the BGP neighbor
            :param string local_as : Local AS of the BGP neighbor Local AS of the BGP neighbor
            :param string update_source : Source IP to connect to the BGP neighbor Source IP to connect to the BGP neighbor
            :param string auth_password : Password to connect to the BGP neighbor Password to connect to the BGP neighbor
            :param string description : Description of the BGP neighbor Description of the BGP neighbor
            :param string adj_rib_in_filter : Policy that is applied for Adj-RIB-In prefix filtering Policy that is applied for Adj-RIB-In prefix filtering
            :param string adj_rib_out_filter : Policy that is applied for Adj-RIB-Out prefix filtering Policy that is applied for Adj-RIB-Out prefix filtering
            :param uint8 max_prefixes_restart_timer : Time to wait before we start BGP peer session when we receive max prefixes Time to wait before we start BGP peer session when we receive max prefixes
            :param bool multi_hop_enable : Enable/Disable multi hop for BGP neighbor Enable/Disable multi hop for BGP neighbor
            :param bool max_prefixes_disconnect : Disconnect the BGP peer session when we receive the max prefixes from the neighbor Disconnect the BGP peer session when we receive the max prefixes from the neighbor
            :param uint8 multi_hop_ttl : TTL for multi hop BGP neighbor TTL for multi hop BGP neighbor
            :param uint32 keep_alive_time : Keep alive time for the BGP neighbor Keep alive time for the BGP neighbor
            :param uint32 route_reflector_cluster_id : Cluster Id of the internal BGP neighbor route reflector client Cluster Id of the internal BGP neighbor route reflector client
            :param uint32 max_prefixes : Maximum number of prefixes that can be received from the BGP neighbor Maximum number of prefixes that can be received from the BGP neighbor
            :param uint8 add_paths_max_tx : Max number of additional paths that can be transmitted to BGP neighbor Max number of additional paths that can be transmitted to BGP neighbor
            :param bool add_paths_rx : Receive additional paths from BGP neighbor Receive additional paths from BGP neighbor
            :param bool route_reflector_client : Set/Clear BGP neighbor as a route reflector client Set/Clear BGP neighbor as a route reflector client
            :param uint8 max_prefixes_threshold_pct : The percentage of maximum prefixes before we start logging The percentage of maximum prefixes before we start logging
            :param uint32 hold_time : Hold time for the BGP neighbor Hold time for the BGP neighbor
            :param uint32 connect_retry_time : Connect retry time to connect to BGP neighbor after disconnect Connect retry time to connect to BGP neighbor after disconnect

        """
        obj = {
                'Name': name,
                'PeerAS': peer_as,
                'LocalAS': local_as,
                'UpdateSource': update_source,
                'AuthPassword': auth_password,
                'Description': description,
                'AdjRIBInFilter': adj_rib_in_filter,
                'AdjRIBOutFilter': adj_rib_out_filter,
                'MaxPrefixesRestartTimer': int(max_prefixes_restart_timer),
                'MultiHopEnable': True if multi_hop_enable else False,
                'MaxPrefixesDisconnect': True if max_prefixes_disconnect else False,
                'MultiHopTTL': int(multi_hop_ttl),
                'KeepaliveTime': int(keep_alive_time),
                'RouteReflectorClusterId': int(route_reflector_cluster_id),
                'MaxPrefixes': int(max_prefixes),
                'AddPathsMaxTx': int(add_paths_max_tx),
                'AddPathsRx': True if add_paths_rx else False,
                'RouteReflectorClient': True if route_reflector_client else False,
                'MaxPrefixesThresholdPct': int(max_prefixes_threshold_pct),
                'HoldTime': int(hold_time),
                'ConnectRetryTime': int(connect_retry_time),
                }
        req_url = self.cfg_url_base+'BGPv4PeerGroup'
        if self.authenticate:
            r = requests.post(req_url, data=json.dumps(obj), headers=HEADERS, timeout=self.timeout, auth=(self.user, self.passwd), verify=False)
        else:
            r = requests.post(req_url, data=json.dumps(obj), headers=HEADERS, timeout=self.timeout)
        return r

    def delete_bgpv4_peer_group(self, name):
        obj = {
                'Name': name,
                }
        req_url = self.cfg_url_base+'BGPv4PeerGroup'
        if self.authenticate:
            r = requests.delete(req_url, data=json.dumps(obj), headers=HEADERS, timeout=self.timeout, auth=(self.user, self.passwd), verify=False)
        else:
            r = requests.delete(req_url, data=json.dumps(obj), headers=HEADERS, timeout=self.timeout)
        return r

    def create_ipv4_intf(self, intf_ref, ip_addr, admin_state='UP'):
        """
        .. automethod :: createipv4intf(self,
            :param string intf_ref : Interface name or ifindex of port/lag or vlan on which this IPv4 object is configured Interface name or ifindex of port/lag or vlan on which this IPv4 object is configured
            :param string ip_addr : Interface IP/Net mask in CIDR format to provision on switch interface Interface IP/Net mask in CIDR format to provision on switch interface
            :param string admin_state : Administrative state of this IP interface Administrative state of this IP interface

        	"""
        obj = {
                'IntfRef': intf_ref,
                'IpAddr': ip_addr,
                'AdminState': admin_state,
                }
        req_url = self.cfg_url_base+'IPv4Intf'
        if self.authenticate:
            r = requests.post(req_url, data=json.dumps(obj), headers=HEADERS, timeout=self.timeout, auth=(self.user, self.passwd), verify=False)
        else:
            r = requests.post(req_url, data=json.dumps(obj), headers=HEADERS, timeout=self.timeout)
        return r

    def delete_ipv4_intf(self, intf_ref):
        obj = {
                'IntfRef': intf_ref,
                }
        req_url = self.cfg_url_base+'IPv4Intf'
        if self.authenticate:
            r = requests.delete(req_url, data=json.dumps(obj), headers=HEADERS, timeout=self.timeout, auth=(self.user, self.passwd), verify=False)
        else:
            r = requests.delete(req_url, data=json.dumps(obj), headers=HEADERS, timeout=self.timeout)
        return r

    def update_bgp_global(self,
                        vrf,
                        asnum=None,
                        use_multiple_paths=None,
                        ebgp_max_paths=None,
                        ebgp_allow_multiple_as=None,
                        router_id=None,
                        ibgp_max_paths=None,
                        redistribution=None):
        obj = {}
        if vrf is not None:
            obj['Vrf'] = vrf

        if asnum is not None:
            obj['ASNum'] = asnum

        if use_multiple_paths is not None:
            obj['UseMultiplePaths'] = True if use_multiple_paths else False

        if ebgp_max_paths is not None:
            obj['EBGPMaxPaths'] = int(ebgp_max_paths)

        if ebgp_allow_multiple_as is not None:
            obj['EBGPAllowMultipleAS'] = True if ebgp_allow_multiple_as else False

        if router_idId is not None:
            obj['RouterId'] = router_id

        if ibgp_max_paths is not None:
            obj['IBGPMaxPaths'] = int(ibgp_max_paths)

        if redistribution is not None:
            obj['Redistribution'] = redistribution

        req_url = self.cfg_url_base+'BGPGlobal'
        if self.authenticate:
            r = requests.patch(req_url, data=json.dumps(obj), headers=HEADERS, timeout=self.timeout, auth=(self.user, self.passwd), verify=False)
        else:
            r = requests.patch(req_url, data=json.dumps(obj), headers=HEADERS, timeout=self.timeout)
        return r

    def update_lldp_global(self,
                         vrf,
                         tx_rx_mode=None,
                         snoop_and_drop=None,
                         enable=None,
                         tranmit_interval=None):
        obj = {}
        if vrf is not None:
            obj['Vrf'] = vrf

        if tx_rx_mode is not None:
            obj['TxRxMode'] = tx_rx_mode

        if snoop_and_drop is not None:
            obj['SnoopAndDrop'] = True if snoop_and_drop else False

        if enable is not None:
            obj['Enable'] = True if enable else False

        if tranmit_interval is not None:
            obj['TranmitInterval'] = int(tranmit_interval)

        req_url = self.cfg_url_base+'LLDPGlobal'
        if self.authenticate:
            r = requests.patch(req_url, data=json.dumps(obj), headers=HEADERS, timeout=self.timeout, auth=(self.user, self.passwd), verify=False)
        else:
            r = requests.patch(req_url, data=json.dumps(obj), headers=HEADERS, timeout=self.timeout)
        return r

    def reset_bgpv4_neighbor_by_ip_addr(self, ip_addr):
        """
        .. automethod :: executeresetbgpv4neighborbyipaddr(self,
            :param string ip_addr : IP address of the BGP IPv4 neighbor to restart IP address of the BGP IPv4 neighbor to restart

        """
        obj = {
                'IPAddr': ip_addr,
                }
        req_url = self.action_url_base+'ResetBGPv4NeighborByIPAddr'
        if self.authenticate:
            r = requests.post(req_url, data=json.dumps(obj), headers=HEADERS, auth=(self.user, self.passwd), verify=False)
        else:
            r = requests.post(req_url, data=json.dumps(obj), headers=HEADERS)
        return r

    def create_bgpv6_neighbor(self,
                            intf_ref,
                            neighbor_address,
                            description='',
                            peer_group='',
                            peer_as='',
                            local_as='',
                            update_source='',
                            adj_rib_in_filter='',
                            adj_rib_out_filter='',
                            bfd_enable=False,
                            multi_hop_ttl=0,
                            keep_alive_time=0,
                            add_paths_rx=False,
                            route_reflector_client=False,
                            max_prefixes_restart_timer=0,
                            multi_hop_enable=False,
                            route_reflector_cluster_id=0,
                            max_prefixes_disconnect=False,
                            add_paths_max_tx=0,
                            max_prefixes=0,
                            max_prefixes_threshold_pct=80,
                            bfd_session_param='default',
                            disabled=False,
                            hold_time=0,
                            connect_retry_time=0):
        """
        automethod :: createbgpv6neighbor(self,
         :param string intf_ref : Interface of the BGP neighbor Interface of the BGP neighbor
         :param string neighbor_address : Address of the BGP neighbor Address of the BGP neighbor
         :param string description : Description of the BGP neighbor Description of the BGP neighbor
         :param string peer_group : Peer group of the BGP neighbor Peer group of the BGP neighbor
         :param string peer_as : Peer AS of the BGP neighbor Peer AS of the BGP neighbor
         :param string local_as : Local AS of the BGP neighbor Local AS of the BGP neighbor
         :param string update_source : Source IP to connect to the BGP neighbor Source IP to connect to the BGP neighbor
         :param string adj_rib_in_filter : Policy that is applied for Adj-RIB-In prefix filtering Policy that is applied for Adj-RIB-In prefix filtering
         :param string adj_rib_out_filter : Policy that is applied for Adj-RIB-Out prefix filtering Policy that is applied for Adj-RIB-Out prefix filtering
         :param bool bfd_enable : Enable/Disable BFD for the BGP neighbor Enable/Disable BFD for the BGP neighbor
         :param uint8 multi_hop_ttl : TTL for multi hop BGP neighbor TTL for multi hop BGP neighbor
         :param uint32 keep_alive_time : Keep alive time for the BGP neighbor Keep alive time for the BGP neighbor
         :param bool add_paths_rx : Receive additional paths from BGP neighbor Receive additional paths from BGP neighbor
         :param bool route_reflector_client : Set/Clear BGP neighbor as a route reflector client Set/Clear BGP neighbor as a route reflector client
         :param uint8 max_prefixes_restart_timer : Time in seconds to wait before we start BGP peer session when we receive max prefixes Time in seconds to wait before we start BGP peer session when we receive max prefixes
         :param bool multi_hop_enable : Enable/Disable multi hop for BGP neighbor Enable/Disable multi hop for BGP neighbor
         :param uint32 route_reflector_cluster_id : Cluster Id of the internal BGP neighbor route reflector client Cluster Id of the internal BGP neighbor route reflector client
         :param bool max_prefixes_disconnect : Disconnect the BGP peer session when we receive the max prefixes from the neighbor Disconnect the BGP peer session when we receive the max prefixes from the neighbor
         :param uint8 add_paths_max_tx : Max number of additional paths that can be transmitted to BGP neighbor Max number of additional paths that can be transmitted to BGP neighbor
         :param uint32 max_prefixes : Maximum number of prefixes that can be received from the BGP neighbor Maximum number of prefixes that can be received from the BGP neighbor
         :param uint8 max_prefixes_threshold_pct : The percentage of maximum prefixes before we start logging The percentage of maximum prefixes before we start logging
         :param string bfd_session_param : Bfd session param name to be applied Bfd session param name to be applied
         :param bool disabled : Enable/Disable the BGP neighbor Enable/Disable the BGP neighbor
         :param uint32 hold_time : Hold time for the BGP neighbor Hold time for the BGP neighbor
         :param uint32 connect_retry_time : Connect retry time to connect to BGP neighbor after disconnect Connect retry time to connect to BGP neighbor after disconnect

         """
        obj = {
                'IntfRef': intf_ref,
                'NeighborAddress': neighbor_address,
                'Description': description,
                'PeerGroup': peer_group,
                'PeerAS': peer_as,
                'LocalAS': local_as,
                'UpdateSource': update_source,
                'AdjRIBInFilter': adj_rib_in_filter,
                'AdjRIBOutFilter': adj_rib_out_filter,
                'BfdEnable': True if bfd_enable else False,
                'MultiHopTTL': int(multi_hop_ttl),
                'KeepaliveTime': int(keep_alive_time),
                'AddPathsRx': True if add_paths_rx else False,
                'RouteReflectorClient': True if route_reflector_client else False,
                'MaxPrefixesRestartTimer': int(max_prefixes_restart_timer),
                'MultiHopEnable': True if multi_hop_enable else False,
                'RouteReflectorClusterId': int(route_reflector_cluster_id),
                'MaxPrefixesDisconnect': True if max_prefixes_disconnect else False,
                'AddPathsMaxTx': int(add_paths_max_tx),
                'MaxPrefixes': int(max_prefixes),
                'MaxPrefixesThresholdPct': int(max_prefixes_threshold_pct),
                'BfdSessionParam': bfd_session_param,
                'Disabled': True if disabled else False,
                'HoldTime': int(hold_time),
                'ConnectRetryTime': int(connect_retry_time),
                }
        req_url = self.cfg_url_base+'BGPv6Neighbor'
        if self.authenticate:
            r = requests.post(req_url, data=json.dumps(obj), headers=HEADERS, timeout=self.timeout, auth=(self.user, self.passwd), verify=False)
        else:
            r = requests.post(req_url, data=json.dumps(obj), headers=HEADERS, timeout=self.timeout)
        return r

    def delete_bgpv6_neighbor(self, intf_ref, neighbor_address):
        obj = {
                'IntfRef': intf_ref,
                'NeighborAddress': neighbor_address,
                }
        req_url = self.cfg_url_base+'BGPv6Neighbor'
        if self.authenticate:
            r = requests.delete(req_url, data=json.dumps(obj), headers=HEADERS, timeout=self.timeout, auth=(self.user, self.passwd), verify=False)
        else:
            r = requests.delete(req_url, data=json.dumps(obj), headers=HEADERS, timeout=self.timeout)
        return r

    def create_ipv4_route(self,
                        destination_nw,
                        network_mask,
                        next_hop,
                        protocol='STATIC',
                        null_route=False,
                        cost=0):
        """
        automethod :: createipv4route(self,
         :param string destination_nw : IP address of the route IP address of the route
         :param string network_mask : mask of the route mask of the route
         :param NextHopInfo next_hop :
         :param string protocol : Protocol type of the route Protocol type of the route
         :param bool null_route : Specify if this is a null route Specify if this is a null route
         :param uint32 cost : Cost of this route Cost of this route

         """
        obj = {
                'DestinationNw': destination_nw,
                'NetworkMask': network_mask,
                'NextHop': next_hop,
                'Protocol': protocol,
                'NullRoute': True if null_route else False,
                'Cost': int(cost),
                }
        req_url = self.cfg_url_base+'IPv4Route'
        if self.authenticate:
            r = requests.post(req_url, data=json.dumps(obj), headers=HEADERS, timeout=self.timeout, auth=(self.user, self.passwd), verify=False)
        else:
            r = requests.post(req_url, data=json.dumps(obj), headers=HEADERS, timeout=self.timeout)
        return r

    def create_ipv6_intf(self, intf_ref, ip_addr='', admin_state='UP', link_ip=True):
        """
        automethod :: createipv6intf(self,
         :param string intf_ref : Interface name or ifindex of port/lag or vlan on which this IPv4 object is configured Interface name or ifindex of port/lag or vlan on which this IPv4 object is configured
         :param string ip_addr : Interface Global Scope IP Address/Prefix-Length to provision on switch interface Interface Global Scope IP Address/Prefix-Length to provision on switch interface
         :param string admin_state : Administrative state of this IP interface Administrative state of this IP interface
         :param bool link_ip : Interface Link Scope IP Address auto-configured Interface Link Scope IP Address auto-configured

         """
        obj = {
                'IntfRef': intf_ref,
                'IpAddr': ip_addr,
                'AdminState': admin_state,
                'LinkIp': True if link_ip else False,
                }
        req_url = self.cfg_url_base+'IPv6Intf'
        if self.authenticate:
            r = requests.post(req_url, data=json.dumps(obj), headers=HEADERS, timeout=self.timeout, auth=(self.user, self.passwd), verify=False)
        else:
            r = requests.post(req_url, data=json.dumps(obj), headers=HEADERS, timeout=self.timeout)
        return r

    def delete_ipv6_intf(self, intf_ref):
        obj = {
                'IntfRef': intf_ref,
                }
        req_url = self.cfg_url_base+'IPv6Intf'
        if self.authenticate:
            r = requests.delete(req_url, data=json.dumps(obj), headers=HEADERS, timeout=self.timeout, auth=(self.user, self.passwd), verify=False)
        else:
            r = requests.delete(req_url, data=json.dumps(obj), headers=HEADERS, timeout=self.timeout)
        return r

    def create_policy_condition(self,
                              name,
                              condition_type,
                              protocol,
                              ip_prefix,
                              mask_length_range,
                              prefix_set=''):
        """
        automethod :: createpolicycondition(self,
        :param string name : PolicyConditionName PolicyConditionName
        :param string condition_type : Specifies the match criterion this condition defines Specifies the match criterion this condition defines
        :param string protocol : Protocol to match on if the ConditionType is set to MatchProtocol Protocol to match on if the ConditionType is set to MatchProtocol
        :param string ip_prefix : Used in conjunction with MaskLengthRange to specify the IP Prefix to match on when the ConditionType is MatchDstIpPrefix/MatchSrcIpPrefix. Used in conjunction with MaskLengthRange to specify the IP Prefix to match on when the ConditionType is MatchDstIpPrefix/MatchSrcIpPrefix.
        :param string mask_length_range : Used in conjuction with IpPrefix to specify specify the IP Prefix to match on when the ConditionType is MatchDstIpPrefix/MatchSrcIpPrefix. Used in conjuction with IpPrefix to specify specify the IP Prefix to match on when the ConditionType is MatchDstIpPrefix/MatchSrcIpPrefix.
        :param string prefix_set : Name of a pre-defined prefix set to be used as a condition qualifier. Name of a pre-defined prefix set to be used as a condition qualifier.

        """
        obj = {
                'Name': name,
                'ConditionType': condition_type,
                'Protocol': protocol,
                'IpPrefix': ip_prefix,
                'MaskLengthRange': mask_length_range,
                'PrefixSet': prefix_set,
                }
        req_url = self.cfg_url_base+'PolicyCondition'
        if self.authenticate:
            r = requests.post(req_url, data=json.dumps(obj), headers=HEADERS, timeout=self.timeout, auth=(self.user, self.passwd), verify=False)
        else:
            r = requests.post(req_url, data=json.dumps(obj), headers=HEADERS, timeout=self.timeout)
        return r

    def update_port(self,
                   intf_ref,
                   if_index=None,
                   phy_intf_type=None,
                   mac_addr=None,
                   speed=None,
                   media_type=None,
                   mtu=None,
                   break_out_mode=None,
                   prbs_rx_enable=None,
                   description=None,
                   prbs_polynomial=None,
                   duplex=None,
                   loopback_mode=None,
                   enable_fec=None,
                   admin_state=None,
                   autoneg=None,
                   prbs_tx_enable=None):
        obj = {}
        if intf_ref is not None:
            obj['IntfRef'] = intf_ref

        if if_index is not None:
            obj['IfIndex'] = int(if_index)

        if phy_intf_type is not None:
            obj['PhyIntfType'] = phy_intf_type

        if mac_addr is not None:
            obj['MacAddr'] = mac_addr

        if speed is not None:
            obj['Speed'] = int(speed)

        if media_type is not None:
            obj['MediaType'] = media_type

        if mtu is not None:
            obj['Mtu'] = int(mtu)

        if break_out_mode is not None:
            obj['BreakOutMode'] = break_out_mode

        if prbs_rx_enable is not None:
            obj['PRBSRxEnable'] = True if prbs_rx_enable else False

        if description is not None:
            obj['Description'] = description

        if prbs_polynomial is not None:
            obj['PRBSPolynomial'] = prbs_polynomial

        if duplex is not None:
            obj['Duplex'] = duplex

        if loopback_mode is not None:
            obj['LoopbackMode'] = loopback_mode

        if enable_fec is not None:
            obj['EnableFEC'] = True if enable_fec else False

        if admin_state is not None:
            obj['AdminState'] = admin_state

        if autoneg is not None:
            obj['Autoneg'] = autoneg

        if prbs_tx_enable is not None:
            obj['PRBSTxEnable'] = True if prbs_tx_enable else False

        req_url = self.cfg_url_base+'Port'
        if self.authenticate:
            r = requests.patch(req_url, data=json.dumps(obj), headers=HEADERS, timeout=self.timeout, auth=(self.user, self.passwd), verify=False)
        else:
            r = requests.patch(req_url, data=json.dumps(obj), headers=HEADERS, timeout=self.timeout)
        return r

    def get_ipv4_route_state(self, destination_nw):
        obj = {
                'DestinationNw': destination_nw,
                }
        req_url = self.state_url_base + 'IPv4Route'
        if self.authenticate:
            r = requests.get(req_url, data=json.dumps(obj), headers=HEADERS, timeout=self.timeout, auth=(self.user, self.passwd), verify=False)
        else:
            r = requests.get(req_url, data=json.dumps(obj), headers=HEADERS, timeout=self.timeout)
        return r

    def get_all_lldp_intf_states(self):
        return self.get_objects('LLDPIntf', self.state_url_base)

    def get_objects(self, obj_name, url_path):
        current_marker = 0
        next_marker = 0
        count = 100
        more = True
        entries = []
        while more:
            more = False
            qry = '%s/%ss?CurrentMarker=%d&NextMarker=%d&Count=%d' % (url_path, obj_name, current_marker, next_marker, count)
            if self.authenticate:
                response = requests.get(qry, timeout=self.timeout, auth=(self.user, self.passwd), varify=False)
            else:
                response = requests.get(qry, timeout=self.timeout)
            if response.status_code in self.httpSuccessCodes:
                data = response.json()
                more = data['MoreExist']
                current_marker = data['NextMarker']
                next_marker = data['NextMarker']
                if data['Objects'] is not None:
                    entries.extend(data['Objects'])
            else:
                print 'Server returned Error for %s' % qry
        return entries

    def get_vlan(self, vlan_id):
        obj = {
                'VlanId': int(vlan_id),
                }
        req_url = self.cfg_url_base + 'Vlan'
        if self.authenticate:
            r = requests.get(req_url, data=json.dumps(obj), headers=HEADERS, timeout=self.timeout, auth=(self.user, self.passwd), verify=False)
        else:
            r = requests.get(req_url, data=json.dumps(obj), headers=HEADERS, timeout=self.timeout)
        return r

    def get_all_vlan_states(self):
        return self.get_objects('Vlan', self.state_url_base)
