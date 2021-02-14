import json
import requests

__all__ = ['show_subnet_dhcp']


def format_input(usr_input):
    if len(usr_input.split()) == 4:
        try:
            output = (usr_input.split())[3]
            return output
        except:
            return None
    else:
        return None


def show_subnet_dhcp(api_key, net_id, vlan_id):

    vlan_id = format_input(vlan_id)
    if vlan_id != None:

        url = "https://api.meraki.com/api/v1/networks/{}/appliance/vlans/{}".format(net_id, vlan_id)

        payload = None

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-Cisco-Meraki-API-Key": api_key
        }

        response = requests.request('GET', url, headers=headers, data = payload)

        print(json.dumps(response.json(), indent=4, sort_keys=4))

    else:
        print("An error occured, couldn't find the vlan Id")
        return None

