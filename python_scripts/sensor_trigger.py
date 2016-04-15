#! /usr/bin/python

import RPi.GPIO as GPIO
import sys, os, time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(3, GPIO.OUT)         #camera output pin

image_num = 1

GPIO.output(3, False)

while True:
    if GPIO.input(11):                 #When output from motion sensor is LOW
        strImage = str(image_num)
        os.system("raspistill -t 1000 -hf -vf -o image" + strImage + ".jpg")
        image_num = image_num + 1
        # os.system("parse.py 1")
        GPIO.output(3, True)
        time.sleep(4)
        GPIO.output(3, False)

            




