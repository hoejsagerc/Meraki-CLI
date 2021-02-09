import json
import requests

__all__ = ['show_mx_interface']


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