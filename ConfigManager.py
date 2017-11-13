#EOT ConfigManager

##import configparser library
import configparser 





## Here is the function syntax;
## Config.ConfigSectionMap("Basic_Conf")['DatabaseUser']
def ConfigSectionMap(section): ##Configuration selection map
    
    ##Assign configparser function to 'Config' variable
    Config = configparser.ConfigParser() 
    ##Read configs from config/config.ini file.
    Config.read("config/config.ini")  
   

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
	##Assign configparser function to 'Config' variable
        Config = configparser.ConfigParser() 
        ##Read configs from config/config.ini file.
        Config.read("config/config.ini") 
	
	##Set option with new value
        Config.set(section, option, str(value)) 
	##Open the config.ini file
        cfgfile = open("config/config.ini", 'w') 
	## Write updated config into config.ini file 
        Config.write(cfgfile) 
        cfgfile.close() ## Close the file 
        print("Configuration has set successfully ..")

    except:
        print("Configuration can not set successfully !")

    return
