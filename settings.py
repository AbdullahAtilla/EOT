import argparse
import ConfigManager



parser = argparse.ArgumentParser() ##Create argument parser
parser.add_argument('-c',  '--config',       help='Display Configurations', required=False, action='store_true',) ##Create new argument '-c   or --config'
parser.add_argument('-dbu','--dbuser',       help='Set database user [ python settings.py -dbu <username> ]',     required=False, action='store',type=str) ##Create new argument '-dbu or --dbuser'
parser.add_argument('-dbp','--dbpassword',   help='Set database password [ python settings.py -dbp <password> ]', required=False, action='store', type=str) ##Create new argument '-dbp or --dbpassword'
parser.add_argument('-dbh','--dbhost',       help='Set database host [ python settings.py -dbh <host> ]', required=False, action='store', type=str) ##Create new argument '-dbh or --dbhost'
parser.add_argument('-loc','--location',     help='Set camera location [ python settings.py -loc <location address> ]', required=False, action='store', type=str) ##Create new argument '-loc or --location'
parser.add_argument('-n',  '--node',         help='Set camera node [ python settings.py -n <CameraNode> ]', required=False, action='store', type=int) ##Create new argument '-n or --node'
parser.add_argument('-u',  '--unit',         help='Set measurement unit [ python settings.py -u <unit> ]',  required=False, action='store', type=str) ##Create new argument '-u or --unit'
parser.add_argument('-ti', '--timeinterval', help='Set time interval that capture image [ python settings.py -ti <TimeInterval> ]', required=False, action='store', type=int) ##Create new argument '-ti or --timeinterval'



 
args = parser.parse_args() ##assign arguments to variable 'args' so you can call an argument by 'args.argument'


###################
if args.config:   ##If config argument choosen
   dbuser       = ConfigManager.ConfigSectionMap("Basic_Conf")['databaseuser'] ##Assign DB username from config/config.ini file  into variable 'dbuser'
   dbpass       = ConfigManager.ConfigSectionMap("Basic_Conf")['databasepass'] ##Assign DB password from config/config.ini file  into variable 'dbpass'
   dbhost       = ConfigManager.ConfigSectionMap("Basic_Conf")['host']     ##Assign DB host from config/config.ini file  into variable 'dbhost'
   location     = ConfigManager.ConfigSectionMap("Basic_Conf")['location'] ##Assign Location address from config/config.ini file into variable 'location'
   camNode      = ConfigManager.ConfigSectionMap("Basic_Conf")['cameranode'] ##Assign Camera node type from config/config.ini file into variable 'camNode'
   unit         = ConfigManager.ConfigSectionMap("Basic_Conf")['unit']     ##Assign Unit type from config/config.ini file into variable 'unit'
   timeInterval = ConfigManager.ConfigSectionMap("Basic_Conf")['timeinterval'] ##Assign Time Interval from config/config.ini file into variable 'timeInterval'

   ##Print configuration
   print("\n==================================")
   print("Database User: " +dbuser+ "\nDatabase Pass: " +dbpass+ "\nHost: " +dbhost+ "\nLocation: " +location+ "\nCameraNode: " +camNode+ "\nUnit: " +unit+ "\nTime Interval: " +timeInterval)
   print("==================================\n")



##################
elif args.dbuser:

   ConfigManager.setConfigOption('Basic_Conf','databaseuser', args.dbuser) ## Set database user with new value

   dbuser = ConfigManager.ConfigSectionMap("Basic_Conf")['databaseuser'] ##Assign DB username from config/config.ini file  into variable 'dbuser'

   ##Print database user
   print("\n==================================")
   print("Database User: " +dbuser)
   print("==================================\n")
   print(args.dbuser)



###################
elif args.dbpassword:

   ConfigManager.setConfigOption('Basic_Conf','databasepass', args.dbpassword) ## Set database password with new value

   dbpassword = ConfigManager.ConfigSectionMap("Basic_Conf")['databasepass'] ##Assign DB password from config/config.ini file  into variable 'dbpass'
  
   ##Print database password
   print("\n==================================")
   print("Database Password: " +dbpassword)
   print("==================================\n")


###################
elif args.dbhost:

   ConfigManager.setConfigOption('Basic_Conf','host', args.dbhost) ## Set database host with new value

   dbhost = ConfigManager.ConfigSectionMap("Basic_Conf")['host'] ##Assign DB host from config/config.ini file  into variable 'dbhost'
  
   ##Print database host
   print("\n==================================")
   print("Host: " +dbhost)
   print("==================================\n")


###################
elif args.location:

   ConfigManager.setConfigOption('Basic_Conf','location', args.location) ## Set location with new value

   location = ConfigManager.ConfigSectionMap("Basic_Conf")['location'] ##Assign Location of camera from config/config.ini file  into variable 'location'
   
   ##Print location
   print("\n==================================")
   print("Location: " +location)
   print("==================================\n")


###################
elif args.node:

   ConfigManager.setConfigOption('Basic_Conf','cameranode', args.node) ## Set camera node with new value

   node = ConfigManager.ConfigSectionMap("Basic_Conf")['cameranode'] ##Assign camera node from config/config.ini file  into variable 'node'
   
   ##Print node
   print("\n==================================")
   print("Node: " +node)
   print("==================================\n")



###################
elif args.unit:
   
   ConfigManager.setConfigOption('Basic_Conf','Unit', args.unit) ## Set unit with new value

   unit = ConfigManager.ConfigSectionMap("Basic_Conf")['unit'] ##Assign unit from config/config.ini file  into variable 'unit'

   ##Print unit
   print("\n==================================")
   print("Unit: " +unit)
   print("==================================\n")



###################
elif args.timeinterval:

   ConfigManager.setConfigOption('Basic_Conf','timeinterval', args.timeinterval) ## Set time interval with new value

   timeinterval = ConfigManager.ConfigSectionMap("Basic_Conf")['timeinterval'] ##Assign time interval from config/config.ini file  into variable 'timeinterval'
   
   ##Print time interval
   print("\n==================================")
   print("Time Interval: " +timeinterval)
   print("==================================\n")


