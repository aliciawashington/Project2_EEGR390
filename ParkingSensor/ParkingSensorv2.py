#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import sys
from pynodered import node_red

@node_red(category="pyfuncs")
def parking_resv(node, msg):
    
    GPIO.setmode(GPIO.BCM)
    #Initalization of pins
    greenLedPin = 4
    yellowLedPin = 3
    redLedPin = 2
    trigPin = 17
    echoPin = 27
    switch = sys.argv[1] #placeholder for now

    #Setting each pin as an input or output
    GPIO.setup(greenLedPin, GPIO.OUT)
    GPIO.setup(yellowLedPin, GPIO.OUT)
    GPIO.setup(redLedPin, GPIO.OUT)
    GPIO.setup(trigPin, GPIO.OUT)
    GPIO.setup(echoPin, GPIO.IN)

    try:
        while True:
            GPIO.output(trigPin, GPIO.LOW)
            time.sleep(2)
            GPIO.output(trigPin, GPIO.HIGH)
            time.sleep(0.00001)
            GPIO.output(trigPin, GPIO.LOW)
            while GPIO.input(echoPin) == 0:
                pulse_start_time = time.time()
            while GPIO.input(echoPin) == 1:
                pulse_end_time = time.time()
            pulse_duration = pulse_end_time - pulse_start_time
            distance = round(pulse_duration*17150, 2)
            msg['payload'] = distance
            print ("Distance: ",distance, " cm")

            if switch == 0:
                GPIO.output(greenLedPin, GPIO.HIGH)
                GPIO.output(yellowLedPin, GPIO.LOW)
                GPIO.output(redLedPin, GPIO.LOW)
                if (distance<=10):
                    GPIO.output(greenLedPin, GPIO.LOW)
                    GPIO.output(yellowLedPin, GPIO.LOW)
                    GPIO.output(redLedPin, GPIO.HIGH)

            if switch == 1:
                GPIO.output(greenLedPin, GPIO.LOW)
                GPIO.output(yellowLedPin, GPIO.HIGH)
                GPIO.output(redLedPin, GPIO.LOW)
                if (distance<=10):
                    GPIO.output(greenLedPin, GPIO.LOW)
                    GPIO.output(yellowLedPin, GPIO.LOW)
                    GPIO.output(redLedPin, GPIO.HIGH)

    except KeyboardInterrupt:
        print("Measurement Stopped by  User")
        GPIO.cleanup()
    return msg
