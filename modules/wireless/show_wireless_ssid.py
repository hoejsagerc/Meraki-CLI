import json
import requests

__all__ = ['show_run_all_ssids', 'show_all_ssids', 'show_enabled_ssids']


def retrieve_ssids(api_key, net_id):

    url = "https://api.meraki.com/api/v1/networks/{}/wireless/ssids".format(net_id)

    payload = None

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }

    response = requests.request('GET', url, headers=headers, data = payload)

    return response




def show_run_all_ssids(api_key, net_id):

    response = (retrieve_ssids(api_key, net_id)).json()

    print(json.dumps(response, indent=4, sort_keys=True))


def show_all_ssids(api_key, net_id):
    
    response = (retrieve_ssids(api_key, net_id)).json()

    for resp in response:

        print(f"SID Number: " + str(resp['number']) + " - " + resp['name'])
        print("-------------------------------------------------")
        print(f"    Enabled:                " + str(resp['enabled']))
        print(f"    Visible:                " + str(resp['visible']))
        try:
            print(f"    Vlan Id:                " + str(resp['defaultVlanId']))
        except:
            pass
        print(f"    Ip Assignment:          " + resp['ipAssignmentMode'])
        print(f"    Band Selection:         " + resp['bandSelection'])
        print(f"    Mandatory DHCP:         " + str(resp['mandatoryDhcpEnabled']))
        print(f"    Splash Page:            " + resp['splashPage'])
        print(f"    Auth Mode:              " + resp['authMode'])

        if resp['authMode'] == "psk":
            print(f"    Encryption Mode:        " + resp['encryptionMode'])
            print(f"    WPA Encryption:         " + resp['wpaEncryptionMode'])

        elif resp['authMode'] == "8021x-radius":
            print(f"    Radius Failover:        " + str(resp['radiusFailoverPolicy']))
            print(f"    Radius Load Balancing:  " + str(resp['radiusLoadBalancingPolicy']))
            print(f"    Radius Override:        " + str(resp['radiusOverride']))
            print(f"    Radius Proxy Enabled:   " + str(resp['radiusProxyEnabled']))
            print(f"    Radius Server:          " + str(resp['radiusServers'][0]['host']))
            print(f"    Radius Id:              " + str(resp['radiusServers'][0]['id']))
            print(f"    Radius Port:            " + str(resp['radiusServers'][0]['port']))
        
        elif resp['authMode'] == "open":
            pass

        print("")
        print("")


def show_enabled_ssids(api_key, net_id):
    
    response = (retrieve_ssids(api_key, net_id)).json()

    for resp in response:
        if resp['enabled'] == True:
            print(f"SID Number: " + str(resp['number']) + " - " + resp['name'])
            print("-------------------------------------------------")
            print(f"    Enabled:                " + str(resp['enabled']))
            print(f"    Visible:                " + str(resp['visible']))
            try:
                print(f"    Vlan Id:                " + str(resp['defaultVlanId']))
            except:
                pass
            print(f"    Ip Assignment:          " + resp['ipAssignmentMode'])
            print(f"    Band Selection:         " + resp['bandSelection'])
            print(f"    Mandatory DHCP:         " + str(resp['mandatoryDhcpEnabled']))
            print(f"    Splash Page:            " + resp['splashPage'])
            print(f"    Auth Mode:              " + resp['authMode'])

            if resp['authMode'] == "psk":
                print(f"    Encryption Mode:        " + resp['encryptionMode'])
                print(f"    WPA Encryption:         " + resp['wpaEncryptionMode'])

            elif resp['authMode'] == "8021x-radius":
                print(f"    Radius Failover:        " + str(resp['radiusFailoverPolicy']))
                print(f"    Radius Load Balancing:  " + str(resp['radiusLoadBalancingPolicy']))
                print(f"    Radius Override:        " + str(resp['radiusOverride']))
                print(f"    Radius Proxy Enabled:   " + str(resp['radiusProxyEnabled']))
                print(f"    Radius Server:          " + str(resp['radiusServers'][0]['host']))
                print(f"    Radius Id:              " + str(resp['radiusServers'][0]['id']))
                print(f"    Radius Port:            " + str(resp['radiusServers'][0]['port']))
            
            elif resp['authMode'] == "open":
                pass

            print("")
            print("")

