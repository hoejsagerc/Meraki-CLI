import getpass
import os
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.styles import Style
from Mrk_APIv1 import con_toolbox, r_prompt, org_id, show_networks, show_run_networks

api_key = "none"
network_name = "none"

rprompt_style = Style.from_dict({
    'rprompt': 'bg:#ff0066 #ffffff',
})



action = 1
while 1:
    t1_compl= WordCompleter(['enable', 'exit'], ignore_case=True)
    t1_action = prompt('> ', history=FileHistory('history.txt'), auto_suggest=AutoSuggestFromHistory(), completer=t1_compl)

    if t1_action == "enable":
        while 1:
            t2_compl = WordCompleter(['select', 'show', 'run', 'network', 'networks', 'exit'])
            if api_key == "none":
                api_key = prompt("Please enter Meraki Dashboard API Key: ")
                print(api_key)

            else:
                t2_action = prompt('# ', history=FileHistory('history.txt'), auto_suggest=AutoSuggestFromHistory(), completer=t2_compl, bottom_toolbar=con_toolbox(api_key), rprompt=r_prompt(network_name))
                
                if t2_action == "exit":
                    break
                
                elif t2_action == "select networks":
                    network_name = prompt('# ', history=FileHistory('history.txt'), auto_suggest=AutoSuggestFromHistory(), completer=t2_compl, bottom_toolbar=con_toolbox(api_key), rprompt=r_prompt(network_name))
                
                elif t2_action == "show networks":
                    show_networks(org_id(api_key), api_key)
                    t2_action = prompt('# ', history=FileHistory('history.txt'), auto_suggest=AutoSuggestFromHistory(), completer=t2_compl, bottom_toolbar=con_toolbox(api_key), rprompt=r_prompt(network_name))
                
                elif t2_action == "select network":
                    network_name = prompt("Enter Name of Network: ")
                    t2_action = prompt('# ', history=FileHistory('history.txt'), auto_suggest=AutoSuggestFromHistory(), completer=t2_compl, bottom_toolbar=con_toolbox(api_key), rprompt=r_prompt(network_name))
                    
                elif t2_action == "show run networks":
                    show_run_networks(org_id(api_key), api_key)
                    t2_action = prompt('# ', history=FileHistory('history.txt'), auto_suggest=AutoSuggestFromHistory(), completer=t2_compl,bottom_toolbar=con_toolbox(api_key),rprompt=r_prompt(network_name))



        network_name = "none"

    elif t1_action == "exit":
        break
        