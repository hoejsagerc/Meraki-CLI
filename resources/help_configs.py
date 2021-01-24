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

__all__ = ['help_user_exec', 'help_user_enabled', 'help_global_config', 'help_selected_network']


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
    MODE: User Enabled

    Descriotion:
        In this mode you will be able to see different information regarding
        you Meraki Organisaition such as Networks, and Devices inside these Networks.

    Commands:
        
        - <help / ?> show the help page for the 'User Enabled' Menu.

        - <config> enters the 'Global Configurations' mode.

        - <show networks brief> display a short list with the names and id's of
            all networks belonging to your organisation.
        
        - <how networks> display a verbose list of all the networks in the organisation.


    """


def help_global_config():
    return """
    MODE: Global Configuration

    Description:
        In this mode you will be able to do configurations to the network
        and organisation. You can use <select> to enter a network and set
        configurations to the desired network.
        You will be able to see which network you are working on by the prompt
        displayed in the right side.
        If the prompt in the right side displayes "None" this means you are editing
        at organisational level.

    Commands:

        - <help / ?> show the help page for the 'Global Config' Menu.

        CONFIGURATION COMMANDS:

        - <set new network> displayed an input menu guideing you through creating 
            a new network. for creating a new network you will be prompted to:
                
                * Network Name: Provivide the desired network name. Example: 
                    Test_Network01

                * TimeZone: Provide the timezone for where the network should be 
                    located. To find the available timezone 
                    see: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
                    an example could be: Europe/Copenhagen
                
                * Product Types: the product types defines the kind of network and 
                    is important do define depending on what kind of equipment you 
                    want to add to the network. The product types should be 
                    seperated by a comma and a space. 
                    An example: appliance, switch, wireless

                    product types: 'wireless', 'wireless', 'switch', 'systemsManager', 
                        'camera', 'cellularGateway', 'environmental'

        - <select network> enter the name of the network you want to chose. this 
            command is case/space sensitive. Once you have entered a network all
            following commands will be done in regards to this network. To exit
            a network, you will need to exit the Global Config Mode.


        SHOW COMMANDS:

        - <do show networks> display a verbose list of all the networks in 
            the organisation.

        - <do show networks brief> display a short list with the names 
            and id's of all networks belonging to your organisation.
            
    """


def help_selected_network():
    return """
    MODE: Selected Network

    Description:
        In this mode you will be able to do different configuraions
        depending ont the specified network you have selected.

    Commands:
        - <help / ?> Show the help page for the selected networks menu

        CONFIGURATION COMMANDS:

        - <delete network> to be able to perform this command, you must have already
            selected the specified network you want to delete. When you enter the
            command delete network, you will be prompted if your are sure you want
            to delete the network. If you press 'y' the network will be deleted.
            If you press 'n' you will cancel the process.

        
        SHOW COMMANDS:

        - <do show network switches> Displays information about all switches
            in the selected network.
        
        - <do show network switches brief> Displays brief information about
            all siwtches in the selected network.
        
        - <do show network ap> Displays information about all Access Points
            in the selected network
        
        - <do show network ap brief> Displays information about all Access Points
            in the selected network

        - <do show network mx> Displays information about all MX Gateways in the
            selected network
        
        - <do show network mx brief> Displays brief information about all MX
            Gateways in the selected network.
    """