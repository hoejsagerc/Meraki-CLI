"""
    NAME
        show_device_configs.py
    CREATED
        24.01.2021
    DESCRIPTION
        This file is for managing all api calls for 
        showing device configurations
    UPDATED
        24.01.2021
"""
import json
import requests

__all__ = ['show_all_mx_interfaces', 'show_mx_interface']


def show_all_mx_interfaces(api_key, net_id):

    url = "https://api.meraki.com/api/v1/networks/{}/appliance/ports".format(net_id)
    vlan_url = "https://api.meraki.com/api/v1/networks/{}/appliance/vlans/settings".format(net_id) 

    payload = None

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }
    vlans_enabled = requests.request('GET', vlan_url, headers=headers, data = payload)
    print(vlans_enabled.json())

    if vlans_enabled.json()['vlansEnabled'] == False:
        vlan_payload = '''{ "vlansEnabled": true }'''
        vlan_response = requests.request('PUT', vlan_url, headers=headers, data = vlan_payload)

    response = requests.request('GET', url, headers=headers, data = payload)

    for port in response.json():
        number = str(port['number'])
        enabled = port['enabled']
        port_type = port['type']
        print(f'Port: {number}      Enabled: {enabled}      Type: {port_type}')



def show_mx_interface(api_key, net_id, port_id):
    """Function for displaying information on a MX show_mx_interfaces

    Args:
        api_key (String): [User provided api key]
        net_id (String): [Network ID]
        port_id ([String]): [Port Number]
    """

    url = "https://api.meraki.com/api/v1/networks/{}/appliance/ports/{}".format(net_id, port_id)

    payload = None

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }

    response = requests.request('GET', url, headers=headers, data = payload)

    print('Interface: ' + str(response.json()['number']))
    print('Type: ' + str(response.json()['type']))
    print('Enabled: ' + str(response.json()['enabled']))
    print("Drop Untagged Traffic: " + str(response.json()['dropUntaggedTraffic']))

    if str(response.json()['type']) == "trunk":
        print("Allowed Vlans: " + str(response.json()['allowedVlans']))
    
    elif str(response.json()['type']) == "access":
        print("Vlan: " + str(response.json()['vlan']))
        print("Access Policy: " + str(response.json()['accessPolicy']))