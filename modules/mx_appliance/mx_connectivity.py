import json
import requests


__all__ = ['mx_conn']




def mx_conn(api_key, net_id):
    """Function for testing if a Meraki mx device is onlined

    Args:
        api_key ([String]): User provided API Key
        net_id ([String]): Network Id

    Returns:
        [type]: Returns the String Online
    """

    url = "https://api.meraki.com/api/v1/networks/{}/appliance/connectivityMonitoringDestinations".format(net_id)

    payload = None

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }

    response = requests.request('GET', url, headers=headers, data = payload)

    if response.status_code == 200:
        print("Connectivity test to: " + response.json()['destinations'][0]['ip'] + " completed successfully!")

        return "Online"

    else:
        return "Offline"

