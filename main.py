import os
import colorama
from colorama import Fore
from colorama import Style as st
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import WordCompleter

from modules import *


clear = lambda: os.system('clear')
action = 1
api_key = "none"
network_name = "none"

clear()
delete_history_file()
print(f"{Fore.CYAN}{menu_welcome()}{st.RESET_ALL}")

while 1:
    #### USER EXEC MODE ####
    t1_compl = WordCompleter(tier1_completer(), ignore_case=True)
    t1_action = prompt('> ', history=FileHistory('history.txt'), auto_suggest=AutoSuggestFromHistory(), completer=t1_compl)
    

    if t1_action == "enable" or "en" in t1_action:

        while 1:
            t2_compl = WordCompleter(tier2_completer())

            if api_key == "none":
                try:
                    api_key = read_api_key('database.db')

                    if api_key == None:
                        break
                except:
                    print("An error occured, couldn't log you in...")
                    break
            
            else:
                ##########################* USER ENABLED MODE ##########################
                network_name = "None"
                mx_name = "None"
                mx_serial = "None"
                ms_name = "None"
                ms_serial = "None"

                t2_compl = WordCompleter(tier2_completer(), ignore_case=True)
                t2_action = prompt('#', history=FileHistory('history.txt'), auto_suggest=AutoSuggestFromHistory(), completer=t2_compl, bottom_toolbar=con_toolbox(api_key), rprompt=r_prompt(network_name))

                if t2_action == "exit" or "ex" in t2_action:
                    break
                
                elif t2_action == "help" or t2_action == "?":
                    print(f'{help_user_enabled()}')

                elif t2_action == "show networks brief" or "sho net br" in t2_action:
                    show_net_brf(org_id(api_key), api_key)
                
                elif t2_action == "show networks":
                    show_net(org_id(api_key), api_key)
                
                elif t2_action == "show all network status" or "sho net stat all" in t2_action:
                    show_net_status(org_id(api_key), api_key)
                
                elif "show network status" in t2_action:
                    show_specific_network_status(org_id(api_key), api_key, t2_action)
                
                elif t2_action == "config terminal" or "conf t" in t2_action:

                    while 1:
                        ##########################* GLOBAL CONFIGURATIONS MODE ##########################
                        t3_compl = WordCompleter(tier3_completer(), ignore_case=True)
                        t3_action = prompt('(config)#', history=FileHistory('history.txt'), auto_suggest=AutoSuggestFromHistory(), completer=t3_compl, bottom_toolbar=con_toolbox(api_key), rprompt=r_prompt(network_name))

                        if t3_action == "exit" or "ex" in t3_action:
                            break

                        elif t3_action == "help" or t3_action == "?":
                            if network_name == "None" or network_name == "":
                                print(help_global_config())
                            elif network_name != "None" or network_name != "":
                                print(help_selected_network())
                        

                        elif "select network" in t3_action or "sel net" in t3_action:
                            try:
                                network_name = get_net_name(org_id(api_key), api_key, t3_action)
                                network_id = get_net_id(org_id(api_key), api_key, network_name)
                                if network_name != "None":
                                    print(f'Network: <{network_name} with id: {network_id} has been selected.')
                            except:
                                print("An error occured, make sure you spell the network name correct. it is case sensitive...")


                        ###* -------- Set/Del Commands -------- ####
                        elif t3_action == "set new network" or "set new net" in t3_action:
                            set_new_net(org_id(api_key), api_key)
                        
                        elif t3_action == "delete network" or "del net" in t3_action:
                            if network_id == "None":
                                print("No network has been selected...")
                            else:
                                del_network(network_id, network_name, api_key)

                        elif t3_action == "set new network device" or "set new net dev" in t3_action:
                            if network_id == "None":
                                print("No network has been selected...")
                            else:
                                add_device_to_network(network_id, api_key)
                        
                        elif t3_action == "delete network device" or "del net dev" in t3_action:
                            if network_id == "None":
                                print("No network has been selected...")
                            else:
                                remove_network_device(network_id, api_key)
                        
                        elif t3_action == "set device name" or "sret dev nam" in t3_action:
                            if network_id == "None":
                                print("No network has been selected...")
                            else:
                                set_device_name(api_key)

                        

                        ###* ------- Do Show Commands ------- ###
                        # not used because of conflict with with other commands in t3_actions
                        #elif t3_action == "show networks brief" or "sho net br" in t3_action:
                        #    show_net_brf(org_id(api_key), api_key)
                        
                        #elif t3_action == "show networks" or "sho net" in t3_action:
                        #    show_net(org_id(api_key), api_key)
                        
                        elif t3_action == "show network switches" or "sho net sw" in t3_action:
                            if network_id == "None":
                                print("No network has been selected...")
                            else:
                                show_network_switches(network_id, api_key, brief=False)
                            
                        elif t3_action == "show network switches brief" or "sho net sw br" in t3_action:
                            if network_id == "None":
                                print("No network has been selected...")
                            else:
                                show_network_switches(network_id, api_key, brief=True)
                        
                        elif t3_action == "show network ap" or "sho net ap" in t3_action:
                            if network_id == "None":
                                print("No network has been selected...")
                            else:
                                show_network_aps(network_id, api_key, brief=False)

                        elif t3_action == "show network ap brief" or "sho net ap br" in t3_action:
                            if network_id == "None":
                                print("No network has been selected...")
                            else:
                                show_network_aps(network_id, api_key, brief=True)

                        elif t3_action == "show network mx" or "sho net mx" in t3_action:
                            if network_id == "None":
                                print("No network has been selected...")
                            else:
                                show_network_mx(network_id, api_key, brief=False)
                        
                        elif t3_action == "show network mx brief" or "sho net mx br" in t3_action:
                            if network_id == "None":
                                print("No network has been selected...")
                            else:
                                show_network_mx(network_id, api_key, brief=True)

                        elif "select mx" in t3_action or "sel mx" in t3_action:
                            if network_name != "None" and network_name != "":
                                mx_name = get_mx_name(api_key, network_id, t3_action)
                                mx_serial = get_mx_serial(api_key, network_id, mx_name)

                                if mx_name != "None" and mx_name != "":
                                    while 1:
                                        ##########################* MX CONFIGURATIONS ##########################

                                        interface = ""
                                        prompt_var =  f'{mx_name}(config)#'
                                        t4_compl = WordCompleter(tier4_completer(), ignore_case=True)
                                        t4_action = prompt(prompt_var, history=FileHistory('history.txt'), auto_suggest=AutoSuggestFromHistory(), completer=t4_compl, bottom_toolbar=con_toolbox(api_key), rprompt=r_prompt(network_name))

                                        if t4_action == "exit" or "ex" in t4_action:
                                            break

                                        elif t4_action == "help" or t4_action == "?":
                                            pass

                                        elif t4_action == "show interfaces" or "sho int" in t4_action:
                                            show_all_mx_interfaces(api_key, network_id)

                                        elif "select interface" in t4_action or "sel int" in t4_action:
                                            interface = get_interface(t4_action)
                                            while 1:
                                                ##########################* MX INTERFACE CONFIGURATIONS ##########################

                                                prompt_if_var = f'{mx_name}(config-if)#'
                                                mx_int_compl = WordCompleter(mx_int_completer(), ignore_case=True)
                                                mx_int_action = prompt(prompt_if_var, history=FileHistory('history.txt'), auto_suggest=AutoSuggestFromHistory(), completer=mx_int_compl, bottom_toolbar=con_toolbox(api_key), rprompt=r_prompt(network_name))

                                                if mx_int_action == 'exit' or "ex" in mx_int_action:
                                                    break

                                                elif mx_int_action == 'help' or  mx_int_action == '?':
                                                    pass

                                                elif mx_int_action == "show interface config" or "sho int conf" in mx_int_action:
                                                    show_mx_interface(api_key, network_id, interface)

                                                elif mx_int_action == "set interface trunk" or "set int tru" in mx_int_action:
                                                    set_interface_trunk(api_key, network_id, interface)

                                                elif mx_int_action == "set interface access" or "set int acc" in mx_int_action:
                                                    set_interface_access(api_key, network_id, interface)


                                else:
                                    print("You will need to give a name to the mx before you can configure it...")
                            else:
                                print("No network has been selected.")

    elif t1_action == "new user" or t1_action == "nu":
        create_connection('database.db')
        create_table('database.db')
        create_user('database.db')
        clear()
        print(f"{Fore.CYAN}{menu_welcome()}{st.RESET_ALL}")

    elif t1_action == "help" or t1_action == "?":
        print(f"{help_user_exec()}")
    
    elif t1_action == "exit" or "ex" in t1_action:
        break


