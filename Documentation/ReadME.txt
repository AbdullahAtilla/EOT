################################
###          EOT             ###
###   (Eye Of the Tiger)     ###
################################


EOT is an computer vision project that aimed reading data on the counters and meters.
After complete installations written on the 'Prerequisites.txt' successfully,
you can run the program via terminal by type; 
	
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







