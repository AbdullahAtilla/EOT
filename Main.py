# Main.py

import cv2
import numpy as np
import os

import DetectChars
import DetectPlates
import PossiblePlate
import CamManager
import threading
import DBManager
from datetime import datetime
import ConfigManager

# module level variables ##########################################################################
SCALAR_BLACK = (0.0, 0.0, 0.0)
SCALAR_WHITE = (255.0, 255.0, 255.0)
SCALAR_YELLOW = (0.0, 255.0, 255.0)
SCALAR_GREEN = (0.0, 255.0, 0.0)
SCALAR_RED = (0.0, 0.0, 255.0)
###################################################################################################
def main():
    
    ##Assign time interval into variable from config/config.ini file
    timeInterval = int(ConfigManager.ConfigSectionMap("Basic_Conf")['timeinterval']) 
    
    ## calls main() function every 'timeInterval' seconds
    threading.Timer(timeInterval, main).start()
    
    cv2.useOptimized();
    # attempt KNN training
    blnKNNTrainingSuccessful = DetectChars.loadKNNDataAndTrainKNN()


    # if KNN training was not successful
    if blnKNNTrainingSuccessful == False:      
        # show error message                         
        print("\nerror: KNN traning was not successful\n")  
        # and exit program             
        return                                                          
    # end if


    ##open camera and capture image
    photo_path = CamManager.get_image() 
    # open captured image from directory
    imgOriginalScene  = cv2.imread("captured_img/last.png")  

    # if image was not read successfully
    if imgOriginalScene is None:                       
        # print error message to std out     
        print("\nerror: image not read from file \n\n")
        # pause so user can see error message
        os.system("pause") 
        # and exit program                                 
        return                                              
    # end if

    # detect plates
    listOfPossiblePlates = DetectPlates.detectPlatesInScene(imgOriginalScene)           
    # detect chars in plates
    listOfPossiblePlates = DetectChars.detectCharsInPlates(listOfPossiblePlates)        

    # if no plates were found
    if len(listOfPossiblePlates) == 0:      
        # inform user no plates were found                    
        print("\nno plates were detected\n")             
    else:                                                       
        # if we get in here list of possible plates has at least one plate
        # sort the list of possible plates in DESCENDING order (most number of chars to least number of chars)
        listOfPossiblePlates.sort(key = lambda possiblePlate: len(possiblePlate.strChars), reverse = True)

        # suppose the plate with the most recognized chars (the first plate in sorted by string length descending order) is the actual plate
        licPlate = listOfPossiblePlates[0]

        # if no chars were found in the plate
        if len(licPlate.strChars) == 0:       
            # show message              
            print("\nno characters were detected\n\n")
            # and exit program       
            return                                          
        # end if

        # write license plate text to std out
        print("\ncharacters read from image = " + licPlate.strChars + "\n")       
        print("----------------------------------------")

        # assign timestamp of measurement to variable 'mTime'
        mTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  
        # insert data into database; timestamp - measured data - photo path
        DBManager.insert_data(mTime, int(licPlate.strChars), photo_path) 

    # end if else

    return
# end main
###################################################################################################

if __name__ == "__main__":
    main()


















