USE EOT_DATA;

#######################
## STORED PROCEDURES ##
#######################


 DELIMITER //
 ##This procedure displays all the data about measurement;
 ## Measurement time, status code, description about status,  measured data,
 ## unit type, location adress of camera, camera node and photo path
 CREATE PROCEDURE display_measurement_data()
   BEGIN
   
    SELECT DISTINCT (Measurement.m_time) , MStatus.statCode, MStatus.description, Measurement.m_data, Unit.u_type, 
					Location.address, Camera.node, Photo.path
    FROM Measurement, Photo, MStatus, Camera, Unit, Location 
    WHERE 
		Photo.path IN 
		(SELECT path FROM Photo WHERE ID = Measurement.photoID) 
	AND
		MStatus.statCode IN 
		(SELECT statCode FROM MStatus WHERE ID = Measurement.statusID)
	AND
		MStatus.description IN 
		(SELECT description FROM MStatus WHERE ID = Measurement.statusID)
	AND 
		Unit.u_type IN
        (SELECT u_type FROM Unit WHERE ID = Measurement.unitID)
	AND
		Location.address IN
        (SELECT address FROM Location WHERE ID IN
        (SELECT locationID FROM Camera WHERE ID IN
        (SELECT ID FROM Camera WHERE ID = Photo.cameraID)))
	AND
		Camera.node IN
        (SELECT node FROM Camera WHERE ID = Photo.cameraID)
	
    ORDER BY Measurement.m_time ASC;
        
   END //
 DELIMITER ;
 
 ##call display_measurement_data();
 ##DROP PROCEDURE IF EXISTS display_measurement_data;
 
 
     