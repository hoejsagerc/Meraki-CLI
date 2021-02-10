"""
    NAME
        prompt_configs.py
    CREATED
        23.01.2021
    DESCRIPTION
        This file contains the different actions defining the prompt
        which is show to the user.
    UPDATED
        23.01.2021
"""

import json
import requests
import os
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.styles import Style


__all__ = ['con_toolbox', 'r_prompt', 'menu_welcome', 'rprompt_style', 'get_net_name', 'get_net_id', 'get_mx_name', 'get_mx_serial', 'get_interface', 'delete_history_file', 'select_interface_range']


#TODO - Working on ...........................

#TODO - .......................................



def con_toolbox(api_key):
    url = "https://api.meraki.com/api/v1/organizations"

    payload = None

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }

    response = requests.request('GET', url, headers=headers, data = payload)
    org = response.json()[0]['name']
    return HTML('Organisation: <b><style bg="ansired">{}</style></b>!'.format(org))


def r_prompt(network_name):
    if network_name == "none":
        return f'<None>'
    else:    
        return f'<{network_name}>'

rprompt_style = Style.from_dict({
    'rprompt': 'bg:#ff0066 #ffffff',
})


def menu_welcome():
    return """
    '##::::'##:'########::'##:::'##:::::::::::'######::'##:::::::'####:
    ###::'###: ##.... ##: ##::'##:::::::::::'##... ##: ##:::::::. ##::
    ####'####: ##:::: ##: ##:'##:::::::::::: ##:::..:: ##:::::::: ##::
    ## ### ##: ########:: #####::::::::::::: ##::::::: ##:::::::: ##::
    ##. #: ##: ##.. ##::: ##. ##:::::::::::: ##::::::: ##:::::::: ##::
    ##:.:: ##: ##::. ##:: ##:. ##::::::::::: ##::: ##: ##:::::::: ##::
    ##:::: ##: ##:::. ##: ##::. ##:'#######:. ######:: ########:'####:
    ..:::::..::..:::::..::..::::..::.......:::......:::........::....::

        Cisco Meraki CLI for                    by Christian Hoejsager
            Managing Meraki Networks...
    

    Name        ; Meraki CLI
    Version     : 0.0.1
    Homepage    : https://hoejsager.com/meraki_cli
    GitHub      : https://github.com/hoejsagerc/Meraki-CLI/

    Total Commands: 4

    """



def get_net_name(org_id, api_key, net_str):
    """
    Function to select a network and store the name and id in a variable

    Args:
        org_id ([Function])-: [Call the function org_id(api_key)]
        api_key ([String]): [API Key proviced by the user]

    Returns:
        [String]: [network_name (name of the network)]
        [String]: [network_id (id of the network)]
    """

    network = net_str.split()
    if len(net_str.split()) > 2:
        index_len = len(net_str)
        network_name = ""
#       if len(net_str.split()) > 2:
        for x in net_str.split()[2:index_len + 1]:
            network_name += x
            network_name += " "
        network_name = network_name.rstrip()
    else:
        network_name = net_str.spli()[2]
    
    url = "https://api.meraki.com/api/v1/organizations/{}/networks".format(org_id)

    payload = None

    headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": api_key
}

    response = requests.request('GET', url, headers=headers, data = payload)

    network_list_names = []

    for net in response.json():
        network_list_names.append(net['name'])
    
    if network_name in network_list_names:
        pass
    else:
        print("No network with that name was found in your organisation...")
        network_name = ""
    
    return network_name 




def get_net_id(org_id, api_key, network_name):
    """Function for retrieving the network ID and return it

    Args:
        org_id ([Function])-: [Call the function org_id(api_key)]
        api_key ([String]): [API Key proviced by the user]
        network_name ([String]): [The name of the chosen network]

    Returns:
        [String]: [The network ID]
    """

    url = "https://api.meraki.com/api/v1/organizations/{}/networks".format(org_id)

    payload = None

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }

    response = requests.request('GET', url, headers=headers, data = payload)

    for net in response.json():
        if net['name'] == network_name:
            return net['id']


def get_mx_name(api_key, net_id, mx_str):

    mx = mx_str.split()
    if len(mx_str.split()) > 2:
        index_len = len(mx_str)
        mx_name = ""
        for x in mx_str.split()[2:index_len + 1]:
            mx_name += x
            mx_name += " "
        mx_name = mx_name.rstrip()
    else:
        mx_name = mx_str.spli()[2]

    url = "https://api.meraki.com/api/v1/networks/{}/devices".format(net_id)

    payload = None

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }
    try:
        response = requests.request('GET', url, headers=headers, data = payload)

        for device in response.json():
            if "MX" in device['model']:
                try:
                    if mx_name == device['name']:
                        return mx_name
                    else:
                        print("Couldn't find device in network...")
                
                except:
                    pass
    except:
        print("Couldn't find the mx...")


def get_mx_serial(api_key, net_id, mx_name):

    url = "https://api.meraki.com/api/v1/networks/{}/devices".format(net_id)

    payload = None

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }

    response = requests.request('GET', url, headers=headers, data = payload)

    try:    
        for device in response.json():
            if "MX" in device['model']:
                try:
                    if mx_name == device['name']:
                        mx_serial = device['serial']
                        return mx_serial

                except:
                    pass
    except:
        print("Couldn't find mx...")


def get_interface(int_str):
    """Function for collecting the interface number

    Returns:
        Variable (String): [The String variable containing the port number]
    """
    
    #interface = str(input("Enter interface number: "))
    interface = int_str.split()
    if len(int_str.split()) > 2:
        index_len = len(int_str)
        interface = ""
        for x in int_str.split()[2:index_len + 1]:
            interface += x
            interface += " "
        interface = interface.rstrip()
    else:
        interface = int_str.spli()[2]


    return interface


def select_interface_range(command):

    split = (command.split()[3].split('-'))

    num1 = int(split[0]) 
    num2 = int(split[1])
    range_list = list(range(num1, num2))
    range_list.append(num2)
    print(range_list)

    return range_list





def delete_history_file():
    if os.path.exists("history.txt"):
        os.remove("history.txt")
    else:
        return "The file cannot be found..."