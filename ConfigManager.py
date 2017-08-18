#EOT ConfigManager

import configparser ##import configparser library





## Here is the function syntax;
## Config.ConfigSectionMap("Basic_Conf")['DatabaseUser']
def ConfigSectionMap(section): ##Configuration selection map
   
    Config = configparser.ConfigParser() ##Assign configparser function to 'Config' variable
    Config.read("config/config.ini")  ##Read configs from config/config.ini file.
   
    dict1 = {}  ##Select conf in the section
    options = Config.options(section) ##Select section
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1 ##Return selected value

##End function


def setConfigOption(section, option, value):
    try:

        Config = configparser.ConfigParser() ##Assign configparser function to 'Config' variable
        Config.read("config/config.ini")  ##Read configs from config/config.ini file.

        Config.set(section, option, str(value)) ##Set option with new value
        cfgfile = open("config/config.ini", 'w') ##Open the config.ini file
        Config.write(cfgfile) ## Write updated config into config.ini file 
        cfgfile.close() ## Close the file 
        print("Configuration has set successfully ..")

    except:
        print("Configuration can not set successfully !")

    return