import mysql.connector
from mysql.connector import errorcode


########################################
##CONNECTION ARGUMENTS #################
########################################

config = {
	'user'             : 'root',
	'password'         : '00000.Aa',
	'host'             : '127.0.0.1',
	'database'         : 'EOT_DATA',
	'raise_on_warnings': True,
}

#########################################




##################
##   VARIABLES  ## 
##################
statcode   =  100;
cameraid   =  1;
unitid     =  1;

###################






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
	add_photo = ("INSERT INTO EOT_DATA.Photo(path) VALUES ('%s')" % photoPath ) ##Insert photo query

	selectPhotoID = ("SELECT ID FROM EOT_DATA.Photo WHERE path LIKE '%s'" % photoPath) ##Select photoID via its path query

	selectStatID  = ("SELECT ID FROM MStatus WHERE statCode = %s" % statcode) ##Select status ID via statCode query 
	##Insert measurement data query
	add_measurement = ("INSERT INTO EOT_DATA.Measurement (m_time, statusID, m_data, unitID, photoID) VALUES (%(m_time)s, %(statusID)s, %(m_data)s, %(unitID)s , %(photoID)s)")



	##End Queries ######


	try:

		con = connect() ##create CONNECTION
		cursor = con.cursor() ##setup cursor


		cursor.execute(add_photo) ##add photo into database with its path
		cursor.execute(selectPhotoID) ##Select related photo's id
		photoid = cursor.fetchone()[0] ##Assign related photo's id into variable 'photoid'

		cursor.execute(selectStatID) ##Select related status ID
		statID  =  cursor.fetchone()[0] ##Assign related status ID into variable 'statID'

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
		con.close() ##At last, close the database connection
		print('Data has not inserted. Rollback!')
	##end try / except

###END OF THE FUNCTION
#######################################################################
