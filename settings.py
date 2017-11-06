import argparse
import ConfigManager



parser = argparse.ArgumentParser() ##Create argument parser
##Create new argument '-c   or --config'
parser.add_argument('-c',  '--config', help='Display Configurations', required=False, action='store_true',) 
##Create new argument '-dbu or --dbuser'
parser.add_argument('-dbu','--dbuser', help='Set database user [ python settings.py -dbu <username> ]', required=False, action='store',type=str) 
##Create new argument '-dbp or --dbpassword'
parser.add_argument('-dbp','--dbpassword', help='Set database password [ python settings.py -dbp <password> ]', required=False, action='store', type=str) 
##Create new argument '-dbh or --dbhost'
parser.add_argument('-dbh','--dbhost', help='Set database host [ python settings.py -dbh <host> ]', required=False, action='store', type=str)
##Create new argument '-loc or --location'
parser.add_argument('-loc','--location', help='Set camera location [ python settings.py -loc <location address> ]', required=False, action='store', type=str)
##Create new argument '-n or --node' 
parser.add_argument('-n',  '--node', help='Set camera node [ python settings.py -n <CameraNode> ]', required=False, action='store', type=int)
##Create new argument '-u or --unit'
parser.add_argument('-u',  '--unit', help='Set measurement unit [ python settings.py -u <unit> ]', required=False, action='store', type=str) 
##Create new argument '-ti or --timeinterval'
parser.add_argument('-ti', '--timeinterval', help='Set time interval that capture image [ python settings.py -ti <TimeInterval> ]', required=False, action='store', type=int) 
##Create new argument '-stimg or --storeimage'
parser.add_argument('-stimg', '--storeimage', help='Enable/Disable to store captured image [ python settings.py -stimg <true/false> ]', required=False, action='store', type=str) 



##assign arguments to variable 'args' so you can call an argument by 'args.argument'
args = parser.parse_args() 


###################
if args.config:   ##If config argument choosen
   ##Assign DB username from config/config.ini file  into variable 'dbuser'
   dbuser       = ConfigManager.ConfigSectionMap("Basic_Conf")['databaseuser'] 
   ##Assign DB password from config/config.ini file  into variable 'dbpass'
   dbpass       = ConfigManager.ConfigSectionMap("Basic_Conf")['databasepass'] 
   ##Assign DB host from config/config.ini file  into variable 'dbhost'
   dbhost       = ConfigManager.ConfigSectionMap("Basic_Conf")['host']  
   ##Assign Location address from config/config.ini file into variable 'location'   
   location     = ConfigManager.ConfigSectionMap("Basic_Conf")['location'] 
   ##Assign Camera node type from config/config.ini file into variable 'camNode'
   camNode      = ConfigManager.ConfigSectionMap("Basic_Conf")['cameranode'] 
   ##Assign Unit type from config/config.ini file into variable 'unit'
   unit         = ConfigManager.ConfigSectionMap("Basic_Conf")['unit']     
   ##Assign Time Interval from config/config.ini file into variable 'timeInterval'
   timeInterval = ConfigManager.ConfigSectionMap("Basic_Conf")['timeinterval'] 
   ##Assign storeimg value from config/config.ini file into variable 'storeimg'
   storeimg     = ConfigManager.ConfigSectionMap("Basic_Conf")['storeimg'] 

   ##Print configuration
   print("\n==================================")
   print("Database User: " +dbuser+ "\nDatabase Pass: " +dbpass+ "\nHost: " +dbhost+ "\nLocation: " +location+ "\nCameraNode: " +camNode+ "\nUnit: " +unit+ "\nTime Interval: " +timeInterval+ "\nStore Image: " +storeimg)
   print("==================================\n")



##################
elif args.dbuser:

   ## Set database user with new value
   ConfigManager.setConfigOption('Basic_Conf','databaseuser', args.dbuser) 

   ##Assign DB username from config/config.ini file  into variable 'dbuser'
   dbuser = ConfigManager.ConfigSectionMap("Basic_Conf")['databaseuser'] 

   ##Print database user
   print("\n==================================")
   print("Database User: " +dbuser)
   print("==================================\n")
   print(args.dbuser)



###################
elif args.dbpassword:

   ## Set database password with new value
   ConfigManager.setConfigOption('Basic_Conf','databasepass', args.dbpassword) 

   ##Assign DB password from config/config.ini file  into variable 'dbpass'
   dbpassword = ConfigManager.ConfigSectionMap("Basic_Conf")['databasepass'] 
  
   ##Print database password
   print("\n==================================")
   print("Database Password: " +dbpassword)
   print("==================================\n")


###################
elif args.dbhost:
   ## Set database host with new value
   ConfigManager.setConfigOption('Basic_Conf','host', args.dbhost) 
   ##Assign DB host from config/config.ini file  into variable 'dbhost'
   dbhost = ConfigManager.ConfigSectionMap("Basic_Conf")['host'] 
  
   ##Print database host
   print("\n==================================")
   print("Host: " +dbhost)
   print("==================================\n")


###################
elif args.location:
   ## Set location with new value
   ConfigManager.setConfigOption('Basic_Conf','location', args.location) 
   ##Assign Location of camera from config/config.ini file  into variable 'location'
   location = ConfigManager.ConfigSectionMap("Basic_Conf")['location'] 
   
   ##Print location
   print("\n==================================")
   print("Location: " +location)
   print("==================================\n")


###################
elif args.node:

   ## Set camera node with new value
   ConfigManager.setConfigOption('Basic_Conf','cameranode', args.node) 
   ##Assign camera node from config/config.ini file  into variable 'node'
   node = ConfigManager.ConfigSectionMap("Basic_Conf")['cameranode'] 
   
   ##Print node
   print("\n==================================")
   print("Node: " +node)
   print("==================================\n")



###################
elif args.unit:  
   ## Set unit with new value
   ConfigManager.setConfigOption('Basic_Conf','Unit', args.unit) 
   ##Assign unit from config/config.ini file  into variable 'unit'
   unit = ConfigManager.ConfigSectionMap("Basic_Conf")['unit'] 

   ##Print unit
   print("\n==================================")
   print("Unit: " +unit)
   print("==================================\n")



###################
elif args.timeinterval:
   ## Set time interval with new value
   ConfigManager.setConfigOption('Basic_Conf','timeinterval', args.timeinterval) 
   ##Assign time interval from config/config.ini file  into variable 'timeinterval'
   timeinterval = ConfigManager.ConfigSectionMap("Basic_Conf")['timeinterval'] 
   
   ##Print time interval
   print("\n==================================")
   print("Time Interval: " +timeinterval)
   print("==================================\n")



###################
elif args.storeimage:
   ## Set storeimg with new value
   ConfigManager.setConfigOption('Basic_Conf','storeimg', args.storeimage) 
   ##Assign storeimg value from config/config.ini file into variable 'storeimg'
   storeimageval = ConfigManager.ConfigSectionMap("Basic_Conf")['storeimg'] 
   
   ##Print storeimg
   print("\n==================================")
   print("Store Image: " +storeimageval)
   print("==================================\n")
