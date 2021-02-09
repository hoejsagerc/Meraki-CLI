import json
import requests

__all__ = ['del_network']

def del_network(net_id, net_name, api_key):
    """Function to delete a network from an organisation.

    Args:
        net_id ([String]): [Network ID]
        net_name ([String]): [Network Name]
        api_key ([String]): [The user provided API Key]
    """

    url = "https://api.meraki.com/api/v1/networks/{}".format(net_id)

    payload = None

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }

    answer = input(f"Your are about to delete network: {net_name} - {net_id}. Press (y/n) to proceed or cancel: ")
    if answer.lower() == "y" or answer.lower() == "yes":
        try:
            response = requests.request('DELETE', url, headers=headers, data = payload)
            print(response.text.encode('utf8'))
            if response.status_code == 204:
                print(f"Network {net_name} was successfully deleted")
            else:
                print("An error occured. Couldn't delete the network...")
        except:
            print("An error occured. Couldn't delete the network...")