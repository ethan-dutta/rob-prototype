# Import the OpenCV library
from PIL import Image
#import pytesseract
import cv2 as cv
import threading
import os, sys, inspect #For dynamic filepaths
import imutils
from imutils.video import FPS
import time
import datetime
import numpy as np

image = cv.VideoCapture(0)

while True:

  check, frame = image.read()

  frame = cv.Canny(frame, 30,200)
 
  check, frame = image.read()
  gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
  blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
  ret, thresh = cv.threshold(blur, 200, 255, cv.THRESH_BINARY)

  contours, heirarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
  for i in contours:
      M = cv.moments(i)
      if M['m00'] != 0:
          cx = int((M['m10']/M['m00']))
          cy = int((M['m01']/M['m00']))
          centrex = int(640-cx)
          centrey = int(480-cy)
          cv.drawContours(thresh, [i], -1, (255, 0, 0), 2)
          cv.circle(thresh, (cx, cy), 7, (0, 0, 255), -1)
          cv.putText(thresh, "centre", (cx -20, cy - 20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
         
          print(f"Distance from centre x: {centrex} y: {centrey}")

  cv.imshow('video', thresh)

  exitkey = cv.waitKey(1)
  if exitkey == ord("q"):
     break

image.release()
cv.destroyAllWindows()
