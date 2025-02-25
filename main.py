#HSV : Hue, Saturtation, Value
import cv2
from util import get_limits
from PIL import Image

yellow = [0,255,255] 

cam = cv2.VideoCapture(0)
while True:
    ret, frame = cam.read()
    hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowerLimit, upperLimit = get_limits(yellow)

    mask = cv2.inRange(frame, lowerLimit, upperLimit) 
    mask_ = Image.fromarray(mask)
    box = mask_.getbbox()

    if box is not None:
        x1,y1,x2,y2 = box
        cv2.rectangle(frame, (x1,y1), (x2,y2), (0,0,255), 4)

    cv2.imshow('Frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()

cv2.destroyAllWindows()