import json
from TestAPICall import find_orgid, find_org_networks

#* Printing Org Information
def prt_orginfo():
    key = input("Please enter the API Key: ")
    org_obj = find_orgid(key)
    print("Org Name: " + org_obj[0]['name'])
    print("Org ID: " + org_obj[0]['id'])



#* Printing all Org Networks
def prt_org_networks():
    key = input("Please enter the API Key: ")
    org_id = find_orgid(key)[0]['id']
    networks = find_org_networks(key, org_id)
    #print(json.dumps(networks, indent=4, sort_keys=True))


    i = 1
    for net in networks:
        print(f'Net#: {i}')
        print("Network: " + net['name'])
        print("Network Id: " + net['id'])
        print(" ")


#* Show a specific network
def show_networks(org_id):
    key = input("Please enter API Key: ")
    name = input("Please enter the network name: ")
    networks = find_org_networks(key, org_id)
    for net in networks:
        if net['name'] == name:
            print(json.dumps(net, indent=4, sort_keys=True))




#prt_org_networks()
show_networks("671599294431626151")



#prt_orginfo()