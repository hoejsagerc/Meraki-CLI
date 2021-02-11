import json
import requests

__all__ = ['update_vlans']


def format_input(usr_input):
    if len(usr_input.split()) > 1:
        output = (usr_input.split())[2]
        return output


def update_vlans(api_key, net_id, vlan_id):
    """Function for updating already created Vlans

    Args:
        api_key ([String]): [User provided api keys]
        net_id ([String]): [Network Id]
    """

    vlan_id = format_input(vlan_id)

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }

    url = "https://api.meraki.com/api/v1/networks/{}/appliance/vlans".format(net_id)

    payload = None

    response = requests.request('GET', url, headers=headers, data = payload)

    for vlan in response.json():
        if str(vlan['id']) == vlan_id:
            old_name = vlan['name']
            old_ip = str(vlan['applianceIp'])
            old_subnet = str(vlan['subnet'])

    print(f'Change vlan name: {old_name}. Press enter to leave the same')
    vlan_name = input("Please enter the new Vlan name: ")
    print(f'Change the vlan Gateway IP: {old_ip}. Press enter to leave the same')
    vlan_ip = input("Please enter the new Appliance Ip: ")
    print(f'Change the vlan Subnet: {old_subnet}. Pres enter to leave the same')
    vlan_subnet = input("Please enter the new Subnet: ")

    if vlan_name == "":
        vlan_name = old_name
    
    if vlan_ip == "":
        vlan_ip = old_ip

    if vlan_subnet == "":
        vlan_subnet = old_subnet

    url = "https://api.meraki.com/api/v1/networks/{}/appliance/vlans/{}".format(net_id, vlan_id)

    payload = {
        "name": vlan_name,
        "applianceIp": vlan_ip,
        "subnet": vlan_subnet,
    }

    response = requests.request('PUT', url, headers=headers, data = json.dumps(payload))

    if response.status_code == 200:
        print("Vlan was updated successfully!")
    else:
        print("An error occured, couldn't update the vlan...")



