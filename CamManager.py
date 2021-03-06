import cv2
import time
import os.path
import configparser

config = configparser.RawConfigParser()
config.read("config/config.ini")

##This variable keeps info whether if captured images will store at file. 
storeimg = bool(config.getboolean('Basic_Conf', 'storeimg'))


##This function check whether usb camera is available, if not, it use the integrated camera.
def camChoise():
	#first check usb camera
	if cv2.VideoCapture(1).isOpened(): 
		#if it is available, use port 1 (usb camera)
		return 1  
	else:
		#if not, use port 1 (integrated camera)
		return 0  
## end of the function
############################################################################################

##This function capture image via camera, and save them into 'captured_img' folder.
def get_image():
	# imgLocation is stores image location
	imgLocation = "the image has not stored"
	# open the camera 
	cap = cv2.VideoCapture(camChoise()) 
	# Capture frame-by-frame
	# allow the camera to warmup
	time.sleep(0.1) 
	success, frame = cap.read()
	
	# do what you want with frame here
	# and then save to file
	
	# give id to images for save into folder
	imgID = 1 


	# check the image with its name exist in folder
	while os.path.exists('captured_img/%d.png' % (imgID)): 
		imgID = imgID + 1 #if exist, try with new name


	if success:
		##If store image option has true;
		if storeimg: ##If the user wants to store image
			# save image backup to the path
			cv2.imwrite('captured_img/%d.png' % (imgID), frame)
			imgLocation = str('captured_img/%d.png' % (imgID))
		##Then, 
		# save the current image to the path
		cv2.imwrite('captured_img/last.png', frame) 
		cv2.waitKey(200)	
		
		# When everything done, release the capture
		cap.release() 
		cv2.destroyAllWindows()

	return imgLocation
###### end of the function
#################################################################################################

get_image()
