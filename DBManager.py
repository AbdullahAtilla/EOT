import mysql.connector
from mysql.connector import errorcode
import ConfigManager

########################################
##CONNECTION ARGUMENTS #################
########################################

config = {
	'user'             : ConfigManager.ConfigSectionMap("Basic_Conf")['databaseuser'],
	'password'         : ConfigManager.ConfigSectionMap("Basic_Conf")['databasepass'],
	'host'             : ConfigManager.ConfigSectionMap("Basic_Conf")['host'],
	'database'         : ConfigManager.ConfigSectionMap("Basic_Conf")['databasename'],
	'raise_on_warnings': True,
}

#########################################




##############################
# VARIABLES FROM CONFIG FILE## 
##############################
statcode        = 100; ##Default code; 'Unknown'
cameraNode      = int(ConfigManager.ConfigSectionMap("Basic_Conf")['cameranode']);
unitType        = str(ConfigManager.ConfigSectionMap("Basic_Conf")['unit']);
locationAddress = str(ConfigManager.ConfigSectionMap("Basic_Conf")['location']);
############################






##############
# FUNCTIONS ##
##############



##This function make database connection
def connect():
	
	try:	##try to connect database
	  con = mysql.connector.connect(**config)
	except mysql.connector.Error as err:
	  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
	    print("Something is wrong with your user name or password")
	  elif err.errno == errorcode.ER_BAD_DB_ERROR:
	    print("Database does not exist")
	  else:
	    print(err)

	return con  ##return connection
###END OF THE FUNCTION
####################################################################





##This function insert measurement data into database
##Variables;
# mtime = measurement time
# mdata = measured data
# photoPath = path of the image which the data has read from.
def insert_data(mtime, mdata, photoPath):

	if len(str(mdata)) < 5 and len(str(mdata)) > 0 :
		statcode = int(303)
	elif len(str(mdata)) == 0 :
		statcode = int(302)
	else:
		statcode = int(101)

	#end if / else


	############
	##QUERIES###
	############
	add_photo = ("INSERT INTO EOT_DATA.Photo (path, cameraID) VALUES (%(path)s , %(cameraid)s)") ##Insert photo query

	selectPhotoID = ("SELECT ID FROM EOT_DATA.Photo WHERE Photo.path LIKE '%s'" % photoPath) ##Select photoID via its path query

	selectStatID  = ("SELECT ID FROM EOT_DATA.MStatus WHERE MStatus.statCode = %d" % statcode) ##Select status ID via statCode query 
	##Insert measurement data query
	add_measurement = ("INSERT INTO EOT_DATA.Measurement (m_time, statusID, m_data, unitID, photoID) VALUES (%(m_time)s, %(statusID)s, %(m_data)s, %(unitID)s , %(photoID)s)")

	SelectUnitID = ("SELECT ID FROM EOT_DATA.Unit WHERE Unit.u_type LIKE '%s'" % unitType) ##Select unit ID via unit type
	
	SelectCameraID = ("SELECT ID FROM EOT_DATA.Camera WHERE Camera.node = %(node)s AND Camera.locationID = %(locationID)s") ##Select camera ID via camera node

	SelectLocationID = ("SELECT ID FROM EOT_DATA.Location WHERE Location.address LIKE '%s'" % locationAddress) ##Select location ID via location address

	add_camera = ("INSERT INTO EOT_DATA.Camera (node, locationID) VALUES (%(node)s , %(locationID)s)") ##Add new camera
	add_location  = ("INSERT INTO EOT_DATA.Location (address) VALUES ('%s')" % locationAddress) ##Add new location
	add_unit  = ("INSERT INTO EOT_DATA.Unit (u_type) VALUES ('%s')" % unitType) ##Add new unit
	##End Queries ######

	try:

		con = connect() ##create CONNECTION
		cursor = con.cursor() ##setup cursor

		cursor.execute(SelectLocationID)
		locationID_data = cursor.fetchone()
		if locationID_data is None:
			cursor.execute(add_location)
			cursor.execute(SelectLocationID) ##Select camera ID
			locationID = cursor.fetchone()[0] ##Assign photo ID into variable 'cameraID'
		elif locationID_data is not None:
			locationID = locationID_data[0] ##Assign photo ID into variable 'cameraID'
		
		##end if else


		data_camera={
			'node': cameraNode,
			'locationID' : locationID,
		}


		cursor.execute(SelectCameraID, data_camera) ##Select camera ID
		cameraID_data = cursor.fetchone()
		if cameraID_data is None:
			cursor.execute(add_camera, data_camera)
			cursor.execute(SelectCameraID, data_camera) ##Select camera ID
			cameraID = cursor.fetchone()[0] ##Assign photo ID into variable 'cameraID'
		elif cameraID_data is not None:
			cameraID = cameraID_data[0] ##Assign photo ID into variable 'cameraID'
		
		##end if else

		
		data_photo={
			'path'      : photoPath,
			'cameraid'  : cameraID,
		}


		cursor.execute(add_photo, data_photo) ##add photo into database with its path
		cursor.execute(selectPhotoID) ##Select related photo's id
		photoid = cursor.fetchone()[0] ##Assign related photo's id into variable 'photoid'

		cursor.execute(selectStatID) ##Select related status ID
		statID  = cursor.fetchone()[0] ##Assign related status ID into variable 'statID'

		cursor.execute(SelectUnitID) ##Select related unit ID
		unitid_data = cursor.fetchone() ##Assign related unit ID into variable unitID
		if unitid_data is None:
			cursor.execute(add_unit)
			cursor.execute(SelectUnitID) ##Select unit ID
			unitid = cursor.fetchone()[0] ##Assign unit ID into variable 'unitid'
		elif unitid_data is not None:
			unitid = unitid_data[0] ##Assign photo ID into variable 'cameraID'



		data_measurement= {  	##data of measurement will insert into database
			'm_time'  : mtime,
			'statusID': statID,
			'm_data'  : mdata,
			'unitID'  : unitid,
			'photoID' : photoid,
		}

		cursor.execute(add_measurement, data_measurement) ##Select ID of statcode from MStatus table

		con.commit() ##try to commit operation
		cursor.close() ##close the cursor
		con.close() ##At last, close the database connection

	except:  ##If operation is not complete successfully ;
	
		con.rollback() ##rollback all the operation
		cursor.close() ##close the cursor
		con.close() ##close the database connection
		print('Data has not inserted. Rollback!')
	##end try / except


###END OF THE FUNCTION
#######################################################################
