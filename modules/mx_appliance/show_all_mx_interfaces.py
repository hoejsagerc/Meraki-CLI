import json
import requests

__all__ = ['show_all_mx_interfaces']


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

        if int(number) < 10:
            print(f'Port: {number}      Enabled: {enabled}      Type: {port_type}')
        else:
            print(f'Port: {number}     Enabled: {enabled}      Type: {port_type}')