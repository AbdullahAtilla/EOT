################################
###          EOT             ###
###   (Eye Of the Tiger)     ###
################################


EOT is an computer vision project that aimed reading data on the counters and meters.
After complete installations written on the 'Prerequisites.txt' successfully,
you can run the program via terminal by type; 
	
	'$ workon cv '
	'$ cd eot/directory/path
	'$ python Main.py'




##############
## Workflow ##
##############

::: Camera 
::::::::::::::::::::::::::::::::
An integrated camera or a USB camera is required for capture image. 


::: Capture image 
::::::::::::::::::::::::::::::::
Camera captures images in a time period. 


::: Save image into directory 
::::::::::::::::::::::::::::::::
Captured images stored into 'captured_img' folder.


::: Preprocess image
::::::::::::::::::::::::::::::::
The last image named 'last.png' in the 'captured_img' file has preprocess for 
recognizing digits and data fields.


::: Detect possible chars
::::::::::::::::::::::::::::::::
After the image has preprocessed, digits seem more clearly so the program detect
possible chars on the scene.


::: Detect possible data fields
::::::::::::::::::::::::::::::::
If there is a certain distance and angle between 5 or more possible chars, 
the program identfy there as a possible data field. 


::: Detect actual data field
::::::::::::::::::::::::::::::::
After the possible data fields has recognized, the program determined the actual
data field which has most recognized chars.


::: Transfer data into database
::::::::::::::::::::::::::::::::
After the actual data field has recognized, chars in the field stored as 
actual data. The actual data transfered into database with its; 
timestamp, statusCode , unit of data, camera node and image path.




######################
## Used Algorithms  ##
######################

"k-Nearest Neighbour" algorithm is used for the digit recognition.
It is known to be very accurate but on the other hand it consumes a lot of CPU time and memory. 
But these drawbacks are not so critical to our program, 
there is sufficient time, because the counter is not rotating very fast.
For more information about k-Nearest Neighbour algorithm, visit;

http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_ml/py_knn/py_knn_understanding/py_knn_understanding.html#knn-understanding 



###############
##  USAGE    ##
###############



::Manual Usage
:::::::::::::::
After complete all the installations on the Prerequisites.txt successfully, you can launch the program from the terminal
by type;

	$ python Main.py


::Launch on startup automatically
::::::::::::::::::::::::::::::::::
If you want to launch program automatically after boot;
You should follow this steps;

1) Launch 'Startup Applications' from Dash,
2) Click on 'add',
3) Type 'EOT' on the name field
4) Browse and select 'EOT_init.sh' on the EOT folder.
5) Type a description you want ("Start EOT at boot time" etc.)
6) Save and quit

For details, visit;
https://www.howtoforge.com/tutorial/how-to-use-startup-applications-on-ubuntu/ 



::::COMMANDS
:::::::::::::::::::::


	$ python Main.py   ##Start EOT

	$ python settings.py -h   ## Display help

	$ python settings.py -c   ## Show configuration options

	$ python settings.py -dbu <username>   ## Set database user as <username>
					       ## For example; $ python settings.py -dbu root >>> set database user as 'root'

	$ python settings.py -dbp <password>   ## Set database password as <password>
					       ## For example; $ python settings.py -dbp 1234.aB

	$ python settings.py -dbh <host>    ## Set host as <host>
					    ## For example; $ python settings.py -dbh 127.0.0.1  >>> set host as 127.0.0.1		

	$ python settings.py -loc <location>   ## Set camera location as <location>
					       ## For example; $ python settings.py -loc Teknopark

	$ python settings.py -n <node>   ## Set camera node as <node> (This field must be an integer)
					 ##For example; $ python settings.py -n 5 >>> camera node 5

	$ python settings.py -u <unit>   ## Set measurement unit as <unit>
					 ## For example; $ python settings.py -u kWh

	$ python settings.py -ti <timeInterval>   ## Set time interval (seconds) to capture image as <timeInterval> (This field must be an integer)
						  ## For example;  $ python settings.py -ti 10 >>> capture image every 10 seconds.



