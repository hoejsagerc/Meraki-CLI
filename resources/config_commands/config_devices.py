"""
    NAME
        config_devices.py
    CREATED
        24.01.2021
    DESCRIPTION
        This file contains functions for configuring devices
    UPDATED
        24.01.2021
"""

import json
import requests

__all__ = ['set_device_name']


def set_device_name(api_key):

    serial = input("Enter serial number of the device you want to name: ")
    device_name = input("Enter the new name you want to give the device: ")

    url = "https://api.meraki.com/api/v1/devices/{}".format(serial)

    payload = {
        "name": device_name
    }

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }

    response = requests.request('PUT', url, headers=headers, data = json.dumps(payload))

    if response.status_code == 200:
        print(f'The name of the device {serial} has been changed to {device_name}')

    else:
        print("An error occured, couldn't rename the device...")