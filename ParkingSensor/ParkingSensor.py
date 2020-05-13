from gpiozero import DistanceSensor,LED,Button
import time

#Initializaiton of variables
TRIG = 17
ECHO = 27
redled = LED(2)
yellowled = LED(3)
greenled = LED(4)
state = Button(22)
sensor = DistanceSensor(ECHO,TRIG)
try:
    while True:
        if state.value == False:#The parking space is not reserved (Green LED should be HIGH)
            greenled.on()
            yellowled.off()
            redled.off()
            if sensor.distance <= 0.5:
                redled.on()
                greenled.off()
                yellowled.off()
        if state.value == True: #The parking space is reserved (Yellow LED should be HIGH)
            greenled.off()
            yellowled.on()
            redled.off()
            if sensor.distance <= 0.5:
                redled.on()
                greenled.off()
                yellowled.off()
        
        print('Distance to nearest object is ', sensor.distance, 'm')
        time.sleep(0.05)
except KeyboardInterrupt:
    print("Measurement stopped by User")
