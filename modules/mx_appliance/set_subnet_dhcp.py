import json
import requests

__all__ = ['update_dhcp', 'format_input', 'dhcp_handling_option', 'create_payload', 'retrive_configured_vlan']


def format_input(usr_input):
    if len(usr_input.split()) == 4:
        try:
            output = (usr_input.split())[3]
            return output
        except:
            return None
    else:
        return None


def dhcp_handling_option():
    print("Options: (1)Run a DHCP server - (2)Relay DHCP to another server - (3)Do not respond to DHCP requests")
    dhcp_handling = input("Please choose option for DHCP Handling: ")
    if dhcp_handling == "1":
        dhcp_handling = "Run a DHCP server"
        option = "1"
        return dhcp_handling, option
    
    elif dhcp_handling == "2":
        dhcp_handling = "Relay DHCP to another server"
        option = "2"
        return dhcp_handling, option
    
    elif dhcp_handling == "3":
        dhcp_handling = "Do not respond to DHCP requests"
        option = "3"
        return dhcp_handling, option
    
    else:
        return None


def retrive_configured_vlan(api_key, net_id, vlan_id):

    url = "https://api.meraki.com/api/v1/networks/{}/appliance/vlans/{}".format(net_id, vlan_id)

    payload = None

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }

    response = requests.request('GET', url, headers=headers, data = payload)

    if response.status_code == 200:
        return response.status_code
    
    else:
        return None



def create_payload(old_set):
    dhcp_handling, option = dhcp_handling_option()
    if option == "1":
        dns_servers = input("Please enter DNS Server seperated with ',': ")
        dns_servers = str((dns_servers.split(","))[0] + "\n" + (dns_servers.split(","))[1])
        print("Choose lease time between: ['30 minutes'], ['1 hour'], ['4 hours'], ['12 hours'], ['1 day'] or ['1 week']")
        lease_time = input("Please enter lease time: ")
        start_range = input("Please enter the starting IP address: ")
        end_range = input("Pleas enter the end last IP address: ")
        range_description = input("Please enter a name for the reserved range: ")
        payload = {
            "name": old_set.json()['name'],
            "subnet": old_set.json()['subnet'],
            "applianceIp": old_set.json()['applianceIp'],
            "reservedIpRanges": [
                {
                    "start": start_range,
                    "end": end_range,
                    "comment": range_description
                }
            ],
            "dnsNameservers": dns_servers,
            "dhcpHandling": dhcp_handling,
            "dhcpLeaseTime": lease_time,
        }
        return dict(payload)

    elif option == "2":
        relay_server_ip = input("Please enter ip of the server you want to relay to: ")
        payload = {
            "name": old_set.json()['name'],
            "subnet": old_set.json()['subnet'],
            "applianceIp": old_set.json()['applianceIp'],
            "dhcpHandling": dhcp_handling,
            "dhcpRelayServerIps": relay_server_ip
        }
        return dict(payload)

    elif option == "3":
        payload = {
            "name": old_set.json()['name'],
            "subnet": old_set.json()['subnet'],
            "applianceIp": old_set.json()['applianceIp'],
            "dhcpHandling": dhcp_handling,
        }
        return dict(payload)
    else:
        return None


def update_dhcp(api_key, net_id, vlan_id):
    """[summary]

    Args:
        api_key ([type]): [description]
        net_id ([type]): [description]
        vlan_id ([type]): [description]
    """

    vlan_id = format_input(vlan_id)
    if vlan_id != None:

        url = "https://api.meraki.com/api/v1/networks/{}/appliance/vlans/{}".format(net_id, vlan_id)

        payload = create_payload(retrive_configured_vlan(api_key, net_id, vlan_id))
        print(json.dumps(payload, indent=4, sort_keys=True))

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-Cisco-Meraki-API-Key": api_key
        }

        response = requests.request('PUT', url, headers=headers, data = json.dumps(payload))

        if response.status_code == 200:
            print("Subnet DHCP was configured successfuly!")
            return response.status_code
        else:
            print("An error occured, coulnt't configure the Subnet DHCP")
            return response.status_code
        
    else:
        print("An error occured, couldn't find the vlan Id")
        return None