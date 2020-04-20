from gpiozero import DistanceSensor,LED,Button
import time

#Initializaiton of variables
TRIG = 17
ECHO = 27
redled = LED(2)
yellowled = LED(3)
greenled = LED(4)
state = Button(0, active_state=False)
sensor = DistanceSensor(ECHO,TRIG)

while True:

    if state.value() == 0:#The parking space is not reserved (Green LED should be HIGH)
        greenled.on()
        yellowled.off()
        if sensor.distance <= 0.5:
            redled.on()
            greenled.off()
            yellowled.off()
    if state.value == 1: #The parking space is reserved (Yellow LED should be HIGH)
        greenled.off()
        yellowled.on()
        if sensor.distance <= 0.5:
            redled.on()
            greenled.off()
            yellowled.off()

    time.sleep(1)
    redled.off()
    print('Distance to nearest object is ', sensor.distance, 'm')
