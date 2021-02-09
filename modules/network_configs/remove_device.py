import json
import requests

__all__ = ['remove_network_device']


def remove_network_device(net_id, api_key):
    """Function for removing devices from a network

    Args:
        net_id ([String]): [Network ID]
        api_key ([String]): [User Provided API Key]
    """

    url = "https://api.meraki.com/api/v1/networks/{}/devices/remove".format(net_id)

    serial = input("Enter the serial number of the device you want to remove: ")

    payload = { "serial": serial }

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }

    response = requests.request('POST', url, headers=headers, data = json.dumps(payload))

    if response.status_code == 204:
        print(f"Device {serial} was removed from network.")
    else:
        print("An error occured couldn't remove the device from the network.")
