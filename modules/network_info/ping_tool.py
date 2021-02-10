import json
import requests
import os
import platform

__all__ = ['ping_tool']

def ping_tool(api_key, net_id, host):

    print("start pinging")
    payload = None

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }
    
    if host.count(".") != 3:
        if len(host.split()) > 2:
            index_len = len(host)
            fin_string = ""
            for x in host.split()[1:index_len + 1]:
                fin_string += x
                fin_string += " "
            device = fin_string.rstrip()
            

        else:
            device = (host.split())[1]

        # checking if device is in network:
        url = "https://api.meraki.com/api/v1/networks/{}/devices".format(net_id)
        response = requests.request('GET', url, headers=headers, data = payload)

        for dev in response.json():
            if dev['name'] == device:
                if "MX" in dev['model']:
                    host = dev['wan1Ip']
                else:
                    host = dev['lanIp']

    else:
        host = (host.split())[1]


    print(f'Host: {host}')
    # pingning the device
    if host != None:
            os_type = platform.system()
            if os_type == 'Linux' or os_type == "Darwin":
                os.system(f'ping -c 4 {host}')

            elif os_type == 'Windows':
                os.system(f'ping -n 4 {host}')
    
    else:
        print("Device ip address not found...")

