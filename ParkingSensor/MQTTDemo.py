#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
import RPi.GPIO as gpio
import time



def gpioSetup():
	gpio.setmode(gpio.BCM)
	#Initalization of pins
	greenLedPin = 4
	yellowLedPin = 3
	redLedPin = 2
	trigPin = 17
	echoPin = 27

	gpio.setup(redLedPin, gpio.OUT)
	gpio.setup(yellowLedPin, gpio.OUT)
	gpio.setup(greenLedPin, gpio.OUT)
	gpio.setup(trigPin, gpio.OUT)
	gpio.setup(echoPin, gpio.IN)


def connectionStatus(client, userdata, flags, rc):
	mqttClient.subscribe("rpi/gpio")

def messageDecoder(client, userdata, msg):
	message = msg.payload.decode(encoding='UTF-8')
	gpio.output(17, gpio.LOW)
	time.sleep(2)
	gpio.output(17, gpio.HIGH)
	time.sleep(0.00001)
	gpio.output(17, gpio.LOW)
	while gpio.input(27) == 0:
		pulse_start_time = time.time()
	while gpio.input(27) == 1:
		pulse_end_time = time.time()
	pulse_duration = pulse_end_time - pulse_start_time
	distance = round(pulse_duration*17150, 2)

	if message == "reserved":
		gpio.output(4, gpio.LOW)
		gpio.output(3, gpio.HIGH)
		gpio.output(2, gpio.LOW)
		print("Space is reserved")
		if distance <= 10:
			gpio.output(4, gpio.LOW)
			gpio.output(3, gpio.LOW)
			gpio.output(2,gpio.HIGH)
			print("Space is occupied")

	elif message == "available":
		gpio.output(4, gpio.HIGH)
		gpio.output(3, gpio.LOW)
		gpio.output(2, gpio.LOW)
		print("Space is available")
		if distance <= 10:
			gpio.output(4, gpio.LOW)
			gpio.output(3, gpio.LOW)
			gpio.output(2, gpio.HIGH)
			print("Space is occupied")
	else:
		print("Unknown message!")
#Set up RPi GPIO Pins
gpioSetup()

#Call ultrasonic sensor function
#distance = ultrasonicSensor(17, 27)

#Set client name
clientName = "hennypi0"

#Set MQTT Server address
serverAddress = "10.0.1.18"

#Instantiate Eclipse Paho as mqttClient
mqttClient = mqtt.Client(clientName)

#Set calling functions to mqttClient
mqttClient.on_connect = connectionStatus
mqttClient.on_message = messageDecoder

#Connect Client to Server
mqttClient.connect(serverAddress)

#Monitor Client activity forever
mqttClient.loop_forever()
