# Main.py

import cv2
import numpy as np
import os

import DetectChars
import DetectPlates
import PossiblePlate
import PiCamManager
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

    timeInterval = int(ConfigManager.ConfigSectionMap("Basic_Conf")['timeinterval']) ##Assign time interval into variable from config/config.ini file
    threading.Timer(timeInterval, main).start()    ## called main() function every 'timeInterval' seconds
    
    cv2.useOptimized();
    blnKNNTrainingSuccessful = DetectChars.loadKNNDataAndTrainKNN()         # attempt KNN training

    if blnKNNTrainingSuccessful == False:                               # if KNN training was not successful
        print("\nerror: KNN traning was not successful\n")               # show error message
        return                                                          # and exit program
    # end if

    photo_path = PiCamManager.get_Pimage() ##open camera and capture image
    imgOriginalScene  = cv2.imread("captured_img/last.png")  # open captured image from directory


    if imgOriginalScene is None:                            # if image was not read successfully
        print("\nerror: image not read from file \n\n")     # print error message to std out
        os.system("pause")                                  # pause so user can see error message
        return                                              # and exit program
    # end if

    listOfPossiblePlates = DetectPlates.detectPlatesInScene(imgOriginalScene)           # detect plates

    listOfPossiblePlates = DetectChars.detectCharsInPlates(listOfPossiblePlates)        # detect chars in plates


    if len(listOfPossiblePlates) == 0:                          # if no plates were found
        print("\nno plates were detected\n")             # inform user no plates were found
    else:                                                       # else
                # if we get in here list of possible plates has at leat one plate

                # sort the list of possible plates in DESCENDING order (most number of chars to least number of chars)
        listOfPossiblePlates.sort(key = lambda possiblePlate: len(possiblePlate.strChars), reverse = True)

                # suppose the plate with the most recognized chars (the first plate in sorted by string length descending order) is the actual plate
        licPlate = listOfPossiblePlates[0]
        
        if len(licPlate.strChars) == 0:                     # if no chars were found in the plate
            print("\nno characters were detected\n\n")       # show message
            return                                          # and exit program
        # end if

        print("\ncharacters read from image = " + licPlate.strChars + "\n")       # write license plate text to std out
        print("----------------------------------------")


        mTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  ##assign timestamp of measurement to variable 'mTime'
        DBManager.insert_data(mTime, int(licPlate.strChars), photo_path) ##insert data into database; timestamp - measured data - photo path

    # end if else

    return
# end main
###################################################################################################

if __name__ == "__main__":
    main()


















