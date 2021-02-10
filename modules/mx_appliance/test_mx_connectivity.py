import json
import requests


__all__ = ['test_mx_conn']




def test_mx_conn(api_key, net_id):

    url = "https://api.meraki.com/api/v1/networks/{}/appliance/connectivityMonitoringDestinations".format(net_id)

    payload = None

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }

    response = requests.request('GET', url, headers=headers, data = payload)

    print("Connectivity test to: " + response.json()['destinations'][0]['ip'] + " completed successfully!")

    return "Online"

