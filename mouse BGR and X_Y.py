import cv2
import numpy as np

def click_func(event, x, y, flags, parameters):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ', ', y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        str_XY = str(x) + ', ' + str(y)
        cv2.putText(img, str_XY, (x, y),
                    font, .5,
                    (255, 255, 0), 2)
        cv2.imshow('image', img)
        
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        str_BGR = str(blue) + ', ' + str(green)+ ', ' + str(red)  
        cv2.putText(img, str_BGR, (x, y), font, .5, (0, 255, 255), 2)
        cv2.imshow('image', img)

img = cv2.imread('123.png')
cv2.imshow('image', img)

cv2.setMouseCallback('image', click_func)

cv2.waitKey(0)
cv2.destroyAllWindows()

