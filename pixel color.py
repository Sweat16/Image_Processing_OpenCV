import cv2
import numpy as np

def pixel_color(event, x, y, flags, parameter):
    if event == cv2.EVENT_LBUTTONDOWN:
       blue = img[x, y, 0]
       green = img[x, y, 1]
       red = img[x, y, 2]
       cv2.circle(img, (x, y), 3, (0,0,255), 10)
       
       my_color_image = np.zeros((512, 512,3), np.uint8)
       
       my_color_image[:] = [blue, green, red]
       
       cv2.imshow('color', my_color_image)

img = cv2.imread('IMG_20191121_144757.jpg')
cv2.imshow('image', img)
points = []

cv2.setMouseCallback('image', pixel_color)

cv2.waitKey(0)
cv2.destroyAllWindows()
    