import json
import requests

__all__ = ['change_ssid_status']


def format_input(usr_input):
    if len(usr_input.split()) == 3:
        try:
            output = (usr_input.split())[2]
            return output
        except:
            return None
    else:
        return None


def change_ssid_status(api_key, net_id, ssid_number):
    
    cmd = (ssid_number.split())[0]
    if cmd == "disable":
        payload = {
            "enabled": "false"
        }

    elif cmd == "enable":
        payload = {
            "enabled": "true"
        }
    
    ssid_number = int(format_input(ssid_number))

    headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": api_key
    }

    url = "https://api.meraki.com/api/v1/networks/{}/wireless/ssids/{}".format(net_id, ssid_number)

    response = requests.request('PUT', url, headers=headers, data = json.dumps(payload))

    if response.status_code == 200:
        if cmd == "enable":
            print("SSID was successfully enabled!")
        elif cmd == "disable":
            print("SSID was successfully disabled!")

        return response.status_code
    
    else:
        print("An error occured, couldn't disable the SSDI...")
        return response.status_code