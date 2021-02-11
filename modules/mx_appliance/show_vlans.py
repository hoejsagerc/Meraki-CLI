import json
import requests

__all__ = ['show_vlans', 'show_vlans_brief']


def show_vlans(api_key, net_id):
    """Function for displaying verbose Vlan information

    Args:
        api_key ([String]): [User provided api key]
        net_id ([String]): [Network Id]
    """

    url = "https://api.meraki.com/api/v1/networks/{}/appliance/vlans".format(net_id)

    payload = None

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }

    response = requests.request('GET', url, headers=headers, data = payload)

    if response.status_code == 200:
        print(json.dumps(response.json(), indent=4, sort_keys=True))
    else:
        print("An error occured, couln't fetch vlans...")


def show_vlans_brief(api_key, net_id):
    """Function for displaying brief Vlan information

    Args:
        api_key ([String]): [User provided api key]
        net_id ([String]): [Network Id]
    """

    url = "https://api.meraki.com/api/v1/networks/{}/appliance/vlans".format(net_id)

    payload = None

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }

    response = requests.request('GET', url, headers=headers, data = payload)

    if response.status_code == 200:
        for vlan in response.json():
            print(f'Vlan Name: ' + vlan['name'])
            print(f'Vlan Id: ' + str(vlan['id']))
            print(f'Vlan Subnet: ' + str(vlan['subnet']))
            print(f'Gateway IP: ' + str(vlan['applianceIp']))
            print("")
    
    else:
        print("An error occured, couln't fetch vlans...")
