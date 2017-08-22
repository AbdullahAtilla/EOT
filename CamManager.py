import cv2
import time
import os.path



##This function check whether usb camera is available, if not, it use the integrated camera.
def camChoise():
	if cv2.VideoCapture(1).isOpened(): #first check usb camera
		return 1  #if it is available, use port 1 (usb camera)
	else:
		return 0  #if not, use port 1 (integrated camera)
## end of the function
############################################################################################



#This function capture image via camera, and save them into 'captured_img' folder.
def get_image():
	cap = cv2.VideoCapture(camChoise()) ##open the camera 
	# Capture frame-by-frame
	time.sleep(0.1) ##allow the camera to warmup
	success, frame = cap.read()
	
	# do what you want with frame here
	# and then save to file

	imgID = 1 #give id to images for save into folder


	while os.path.exists('captured_img/%d.png' % (imgID)): #check the image with its name exist in folder
		imgID = imgID + 1 #if exist, try with new name


	if success:
		cv2.imwrite('captured_img/%d.png' % (imgID), frame) ##save image backup to the path
		cv2.imwrite('captured_img/last.png', frame) ##save the current image to the path
		cv2.waitKey(200)

		cap.release() # When everything done, release the capture
		cv2.destroyAllWindows()

	return str('captured_img/%d.png' % (imgID))
###### end of the function
#################################################################################################
