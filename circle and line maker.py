import cv2
import numpy as np

def circle_and_line_maker(event, x, y, flags, parameter):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 50, (0,0,0), 1)
        points.append((x, y))
        if len(points)>=2:
            cv2.line(img, points[-1], points[-2], (255,255,255), 1)
        cv2.imshow('image', img)

img = cv2.imread('123.png')
cv2.imshow('image', img)
points = []

cv2.setMouseCallback('image', circle_and_line_maker)

cv2.waitKey(0)
cv2.destroyAllWindows()
    