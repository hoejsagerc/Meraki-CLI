import json
import requests


__all__ = ['set_new_net']

def set_new_net(org_id, api_key):
    """Function for creating a new network in the meraki organisation

    Args:
        org_id ([Function): [Call the function org_id(api_key)
        api_key ([String]): [User provided API Key]
        net_name ([String]): [The name of the new Network]
        time_zone ([String]): [The timezone of the network in String --> https://en.wikipedia.org/wiki/List_of_tz_database_time_zones]
        prod_type ([List]): [List of the different hardware types in the network forexample: ["appliance", "switch", "wireless"]
    """

    url = "https://api.meraki.com/api/v1/organizations/{}/networks".format(org_id)

    net_name = input("Please enter Network Name: ")
    time_zone = input("Please enter the TimeZone: ")
    p_types = input("Please enter the network product types seperated by ',': ")
    prod_types = list(p_types.split(",")) 

    payload = {
        "name": net_name,
        "timeZone": time_zone,
        "productTypes": prod_types
    }

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }

    response = requests.request('POST', url, headers=headers, data = json.dumps(payload))

    if response.status_code == 200 or response.status_code == 201:
        print(f'Network <{net_name}> was created successfully!')
    else:
        print("An error occured couldn't create the network...")
    
    return response.status_code

