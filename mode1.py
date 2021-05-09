import cv2
import numpy as np                             
import RPi.GPIO as GPIO
import os
GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)
from time import sleep

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainner/trainner.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
fontscale = 1
fontcolor = (255, 255, 255)
GPIO.output(13, GPIO.LOW)
head="new visitor came!!"
exit_yes=-1

GPIO.output(13, GPIO.LOW)

while exit_yes!=1:
ret, im = cam.read()
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(gray, 1.2, 5)
for (x, y, w, h) in faces:
cv2.rectangle(im, (x, y), (x + w, y + h), (0, 0, 225), 2)
Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
if (conf < 50):
if (Id == 2):                     “The ID for the dataset was taken before”
cv2.putText(im, "Abdullah", (x, y), font, 1, 255, 2)
GPIO.output(13, GPIO.HIGH)  “To trigger output pin”
exit_yes=1
sleep(5)
GPIO.output(13, GPIO.LOW)
else:
GPIO.output(13, GPIO.LOW)  
cv2.putText(im, "unknown,Call owner please!!", (x, y), font, 1, 255, 2)
cv2.imshow('im', im)
if (cv2.waitKey(30) == ord('q')):
break
if(exit_yes==1):
break

cam.release()
cv2.destroyAllWindows()
