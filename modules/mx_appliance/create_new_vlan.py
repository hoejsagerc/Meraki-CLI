import json
import requests

__all__ = ['create_new_vlan']


def create_new_vlan(api_key, net_id):
    """Function for creating a new appliance VLAN.

    Args:
        api_key ([String]): [User provided api key]
        net_id ([String]): [Network Id]
    """

    vlan_id = input("Please enter vlan id: ")
    vlan_name = input("Please enter vlan name: ")
    vlan_subnet = input("Please enter subnet: ")
    appliance_ip = input("Please enter Appliance IP Address: ")

    url = "https://api.meraki.com/api/v1/networks/{}/appliance/vlans".format(net_id)

    payload = {
        "id": vlan_id,
        "name": vlan_name,
        "subnet": vlan_subnet,
        "applianceIp": appliance_ip
    }

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }

    response = requests.request('POST', url, headers=headers, data = json.dumps(payload))

    if response.status_code == 201:
        print(f'Vlan {vlan_id} - {vlan_name} was created successfully!')
    else:
        print(f'An error occured, couldn\'t create the vlan - {response.status_code}')


