from gpiozero import DistanceSensor,LED
import time

TRIG = 17
ECHO = 27

sensor = DistanceSensor(ECHO,TRIG,threshold_distance=0.5)

redled = LED(2)
yellowled = LED(3)
greenled = LED(4)
redled.on()
time.sleep(2)
redled.off()
yellowled.on()
time.sleep(2)
yellowled.off()
greenled.on()
time.sleep(2)
greenled.off()

while True:
    print('Distance to nearest object is ', sensor.distance, 'm')



