#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
#Initalization of pins
greenLedPin = 4
yellowLedPin = 3
redLedPin = 2
trigPin = 17
echoPin = 27
switch = 22 #placeholder for now

#Setting each pin as an input or output
GPIO.setup(greenLedPin, GPIO.OUT)
GPIO.setup(yellowLedPin, GPIO.OUT)
GPIO.setup(redLedPin, GPIO.OUT)
GPIO.setup(trigPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)
GPIO.setup(switch, GPIO.IN)

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
        print ("Distance: ",distance, " cm")

        if GPIO.input(switch) == GPIO.LOW:
            GPIO.output(greenLedPin, GPIO.HIGH)
            GPIO.output(yellowLedPin, GPIO.LOW)
            GPIO.output(redLedPin, GPIO.LOW)
            if (distance<=10):
                GPIO.output(greenLedPin, GPIO.LOW)
                GPIO.output(yellowLedPin, GPIO.LOW)
                GPIO.output(redLedPin, GPIO.HIGH)

        if GPIO.input(switch) == GPIO.HIGH:
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