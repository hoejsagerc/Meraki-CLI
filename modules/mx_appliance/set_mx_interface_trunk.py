import json
import requests

__all__ = ['set_interface_trunk']


def set_interface_trunk(api_key, net_id, port_id):
    """Function for configuring an interface as a trunk

    Args:
        api_key ([type]): [description]
        net_id ([type]): [description]
        port_id ([type]): [description]
    """

    int_native_vlan = input('Enter the Native VLAN: ')
    int_allowed_vlans = input('Select "all" to enable all vlans, or enter "1, 2, 3" to specify: ')



    url = "https://api.meraki.com/api/v1/networks/{}/appliance/ports/{}".format(net_id, port_id)

    payload = {
        "enabled": "true",
        "type": "trunk",
        "dropUntaggedTraffic": "false",
        "vlan": int_native_vlan,
        "allowedVlans": int_allowed_vlans
    }

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }

    response = requests.request('PUT', url, headers=headers, data = json.dumps(payload))

    if response.status_code ==  200:
        print("Interface configured successfully.")
    else:
        print("An error occured, couldn't set the trunk...")