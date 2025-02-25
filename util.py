import numpy as np
import cv2


def get_limits(color):
    a = np.uint8([[color]])
    hsvA = cv2.cvtColor(a, cv2.COLOR_BGR2HSV)

    lowerLimit = hsvA[0][0][0] - 10,100,100
    upperLimit = hsvA[0][0][0] + 10,255,255

    lowerLimit = np.array(lowerLimit, dtype = np.uint8)
    upperLimit = np.array(upperLimit, dtype = np.uint8)
    
    return lowerLimit,upperLimit
