"""
    NAME
        add_remove_devices.py
    CREATED
        24.01.2021
    DESCRIPTION
        This file contains function for adding or removing devices
    UPDATED
        24.01.2021
"""

import json
import requests

__all__ = ['add_device_to_network', 'remove_network_device']


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