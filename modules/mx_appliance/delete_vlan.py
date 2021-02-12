import json
import requests

__all__ = ['delete_vlan', 'format_input']


def format_input(usr_input):
    if len(usr_input.split()) > 1:
        output = (usr_input.split())[2]
        return output


def delete_vlan(api_key, net_id, vlan_id):
    """Function for deleting a vlan

    Args:
        api_key ([String]): [User provided API Key]
        net_id ([String]): [Network Id]
        vlan_id ([Int]): [Vlan Id for the vlan which should be deleted.]
    """

    vlan_id = format_input(vlan_id)

    url = "https://api.meraki.com/api/v1/networks/{}/appliance/vlans/{}".format(net_id, vlan_id)

    payload = None

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }

    response = requests.request('DELETE', url, headers=headers, data = payload)

    if response.status_code == 204:
        print(f'Vlan {vlan_id} was deleted successfully!')
    else:
        print("An error occured, couldn't delete the vlan...")

