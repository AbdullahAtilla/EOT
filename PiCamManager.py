## import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import os.path

##get image from the Pi cam
def get_Pimage():
	##Initialize the camera
	camera = PiCamera()
	camera.resolution = (640, 480)

	##Grab a reference to the raw capture
	rawCapture = PiRGBArray(camera)

	##Allow the camera to warmup
	time.sleep(0.1)

	##Grab image from the camera
	camera.capture(rawCapture, format="bgr")
	image = rawCapture.array

	#give id to images for save into folder
	imgID = 1 

	#check the image with its name exist in folder
	while os.path.exists('captured_img/%d.png' % (imgID)): 
		#if exist, try with new name
		imgID = imgID + 1 
	
	##end while

	##Save image into folder
	cv2.imwrite('captured_img/%d.png' % (imgID), image) 
	
	cv2.imwrite('captured_img/last.png', image)

	return str('captured_img/%d.png' % (imgID))

### End of the funtion
##############################################################


