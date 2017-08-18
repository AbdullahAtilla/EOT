########################
##EOT DATABASE QUERY  ##
########################

CREATE DATABASE EOT_DATA;
USE EOT_DATA;


#######################
## CREATING TABLES  ###
#######################

CREATE TABLE Location(  ##This table keep location information

	ID			INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    address		TEXT 	NOT NULL ##Location address
);


CREATE TABLE Camera(  ##This table keep camera informations

	ID 			INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    node		INTEGER NOT NULL, ##Camera number 
    locationID	INTEGER NOT NULL, ##Location of camera
    
    FOREIGN KEY (locationID) REFERENCES Location(ID)
);


CREATE TABLE Photo( ##This table keep photo informations

	ID			INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    path		TEXT 	NOT NULL, ##Keep photo path where the photo stored 
    cameraID	INTEGER NOT NULL DEFAULT 1, ##Related camera which obtain photo from.
    
    FOREIGN KEY (cameraID) REFERENCES Camera(ID)
);


CREATE TABLE Unit( ##This table keep units
	
    ID			INTEGER		   NOT NULL AUTO_INCREMENT PRIMARY KEY,
    u_type		VARCHAR(10)	   NOT NULL ##('°C', 'kWh' etc.)
);



CREATE TABLE MStatus( ##This table keep status codes and description
	ID				INTEGER		  NOT NULL AUTO_INCREMENT PRIMARY KEY,
    statCode		INTEGER		  NOT NULL, ##Status code (Eg. 202)
    description 	TEXT		  NOT NULL  ##Status description (Eg. 'Camera access denied' etc.)
);



CREATE TABLE Measurement( ##This table keep data which obtained from measurement
	
	ID 			INTEGER 	  NOT NULL AUTO_INCREMENT PRIMARY KEY,
    m_time 		TIMESTAMP	  NOT NULL, ##Keep data measurement time
	statusID	INTEGER		  NOT NULL, ##Keep status of data. 
    m_data		INTEGER		  , ##Keep the recognized data.
    unitID		INTEGER		  , ##Data unit (Eg. 'kWh', '°C' etc.)
    photoID		INTEGER		  ,	##Related photo which obtained data from.
    
	FOREIGN KEY (statusID)  REFERENCES MStatus(ID),
    FOREIGN KEY (unitID)    REFERENCES Unit (ID),
    FOREIGN KEY (photoID)   REFERENCES Photo(ID)
);








###############################
##Adding some basic STATUS  ###
###############################

##100's are successful statuses
INSERT INTO MStatus(statCode, description) 
VALUES (101, 'Operation successful');

##200's are 'Camera' errors
INSERT INTO MStatus(statCode, description) 
VALUES (201, 'Camera can not found!');

INSERT INTO MStatus(statCode, description) 
VALUES (202, 'Camera access denied!');

##300's are 'Recognizing' errors
INSERT INTO MStatus(statCode, description) 
VALUES (301, 'Data field on the scene can not be detected!');

INSERT INTO MStatus(statCode, description) 
VALUES (302, 'Digits on the data field can not be detected!');

INSERT INTO MStatus(statCode, description) 
VALUES (303, 'Missing digits on the data!');

##400's are 'Access & Permission' errors
INSERT INTO MStatus(statCode, description) 
VALUES (401, 'Database access denied!');

##500's are 'Data Transfer' errors
INSERT INTO MStatus(statCode, description) 
VALUES (501, 'Can not insert data on database!');

INSERT INTO MStatus(statCode, description) 
VALUES (502, 'Can not read data from database!');

##600's are 'Connection' errors
INSERT INTO MStatus(statCode, description) 
VALUES (601, 'Can not connect to database!');



##########################
##Adding basic 'Unit's  ##
##########################

INSERT INTO Unit(u_type) VALUES ('kWh');
INSERT INTO Unit(u_type) VALUES ('m3');
INSERT INTO Unit(u_type) VALUES ('lt');