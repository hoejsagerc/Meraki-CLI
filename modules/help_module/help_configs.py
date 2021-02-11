"""
    NAME
        prompt_configs.py
    CREATED     
        23.01.2021
    DESCRIPTION
        This file contains the varios functions for displaying
        help menus depending on where in the app the user exists.
    UPDATED
        23.01.2021
"""

__all__ = ['help_user_exec', 'help_user_enabled', 'help_global_config', 'help_selected_network', 'mx_interface_range_help', 'help_selected_mx']


def help_user_exec():
    return """
    Welcome to the Meraki CLI Tool v0.0.1

    Description:
        This tool is designed to effectively interact with a 
        Cisco Meraki Organisation, Network or Device.

        The tool works through the Meraki API v1. Documentation can 
        be found here: https://developer.cisco.com/meraki/api-v1/.
        You will therefore need access to a Meraki Organisation and
        a Meraki API Key to be able to use the tool.

    Usefull Tips:
        Through all the menus the tool will guide you with auto completion
        and command history. To Utillize these:

        - Command History: Use the arrow-keys <Up> or <Down> to either go
            back or forth in you history.
            The command history is saved in a file called: 'history.txt' and
            will be located where you have the tool installed.

        - Auto Completion: The tool provides auto completion through all the
            menus. This can be used by pressing the <Tab> key.
        
    Commands:
        Commands for getting started using the application

        - <enable> this command will prompt the user for an API key to a
            Meraki Dashboard. Once the api key is entered you will be granted
            access to the 'User Enabled' menu, where you will be able to see
            information regarding you organisation and networks. You will also
            be able to acces the 'User Config' and 'Interface Config' mode where
            you will be able to do configurations.

        - <exit> this commmand will exit the application.

        - <help / ?> this command will display the help menu.

    About:
        This application has been developed as open source. All code can be found
        on github: https://github.com/hoejsagerc/Meraki-CLI

        Author: Christian Hoejsager
        Project started: 23.01.2021
        Version: 0.0.1

    """


def help_user_enabled():
    return """

HELP:
__________________________________________________________________
help / ?.................................Shows the help menu
exit.....................................Exit to last menu
config terminal..........................Switch to global config menu
show networks............................Show verbose networks
show networks brief......................Show exact info on networks
show all network status..................Shows status on all networks
show network status [network_name].......Shows status on specific network

    """


def help_global_config():
    return """

HELP:
__________________________________________________________________
help / ?.................................Shows the help menu
exit.....................................Exit to last menu
select network [network_name]............Selects the specified network
show networks............................Displays verbose info on networks
show networks brief......................Displays info on networks
add new network..........................Create new network
delete network...........................Deletes network
show all network status..................Shows status on all networks
show network status [network_name].......Shows status on specific network

    """


def help_selected_network():
    return """

HELP:
__________________________________________________________________
help / ?.................................Shows the help menu
exit.....................................Exit to last menu
add new network device...................Adds a device to the network
delete network device....................Removes a device from the network
show network switches....................Show verbose switches in network
show network switches brief..............Shows switches in network
show network ap..........................Show verbose AP's in network
show network ap brief....................Show AP's in network
show network mx..........................Show verbose MX's in network
show network mx brief....................Show MX's in network
delete network...........................Deletes network
set device name..........................Renames a device
test network connection..................Tests if network is online

    """

def help_selected_mx():
    return """
HELP:
__________________________________________________________________
help / ?.................................Shows the help menu
exit.....................................Exit to last menu
show interfaces..........................Show information on all interfaces
set new vlan.............................Creates a new vlan
show vlans...............................Show verbose info on all vlans
show vlans brief.........................Show brief info on all vlans
update vlan..............................Update vlan information
delete vlan..............................Delete vlan from network
select interface range [x-y].............Select a range of interfaces
select interface [x].....................Select a single interface

    """


def mx_interface_range_help():
    return """
HELP:
__________________________________________________________________
help / ?.................................Shows the help menu
exit.....................................Exit to last menu
set interface access.....................Configure the range as access ports
set interface trunk......................Configure the range as trunk ports

    """