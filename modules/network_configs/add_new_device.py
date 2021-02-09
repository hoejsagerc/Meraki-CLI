import json
import requests

__all__ = ['add_device_to_network']


def add_device_to_network(net_id, api_key):
    """Function for adding devices to a network. Important note - you may not have
    spaces between the serial numbers when entering them in.

    Args:
        net_id ([String]): [Network ID]
        api_key ([API Key]): [User Provided API Key]
    """

    url = "https://api.meraki.com/api/v1/networks/{}/devices/claim".format(net_id)

    input_serials = input("Enter the serial numbers seperated by ',': ")
    serials = list(input_serials.split(","))

    payload = {
        "serials": serials 
    }

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }

    print(json.dumps(payload, indent=4, sort_keys=True))

    response = requests.request('POST', url, headers=headers, data = json.dumps(payload))

    print(response.status_code)

    if response.status_code == 200:
        for serial in serials:
            print(f'Device: {serial} was claimed to the network.')
    else:
        print("An error occured, couldn't claim the devices. Remember you may not have spaces between each serial number.")