import json
import requests

__all__ = ['set_interface_access', 'set_int_range_access']


def set_interface_access(api_key, net_id, port_id):
    """Function for configuring a Trunk interface

    Args:
        api_key ([String]): [User provided API Key]
        net_id ([String]): [Network ID]
        port_id ([Port ID]): [Interface id]
    """

    int_access_policy = input('Select open to set an Open access policy or chose the desired policy: ')
    int_vlan = input('Select the desired VLAN: ')

    url = "https://api.meraki.com/api/v1/networks/{}/appliance/ports/{}".format(net_id, port_id)

    payload = {
        "enabled": "true",
        "type": "access",
        "vlan": int_vlan,
        "accessPolicy": int_access_policy,
    }

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key,
    }

    response = requests.request('PUT', url, headers=headers, data = json.dumps(payload))

    if response.status_code == 200:
        print("Interface configured successfully.")
    else:
        print("An error occured, couldn't set the access port...")



def set_int_range_access(api_key, net_id, port_range):
    """Function for configuring an interface range as access ports

    Args:
        api_key ([String]): [User provided API Key]
        net_id ([String]): [Network ID]
        port_id ([Port ID]): [Interface id]
    """

    int_access_policy = input('Select open to set an Open access policy or chose the desired policy: ')
    int_vlan = input('Select the desired VLAN: ')

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key,
    }

    payload = {
        "enabled": "true",
        "type": "access",
        "vlan": int_vlan,
        "accessPolicy": int_access_policy,
    }
    
    for port in port_range:

        url = "https://api.meraki.com/api/v1/networks/{}/appliance/ports/{}".format(net_id, port)
        response = requests.request('PUT', url, headers=headers, data = json.dumps(payload))

        if response.status_code == 200:
            print(f"Interface {port} configured successfully.")
        else:
            print("An error occured, couldn't set the access port...")    

