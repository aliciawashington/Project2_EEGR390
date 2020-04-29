#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import psycopg2

# Connection to the database
conn = psycopg2.connect(
    host="localhost",
    database="test",
    user="pi",
    password="henny")

# Creation of the cursor
cur = conn.cursor()

# The following lines of code implement the function of the parking sensor
GPIO.setmode(GPIO.BCM)
# Initalization of pins
greenLedPin = 4
yellowLedPin = 3
redLedPin = 2
trigPin = 17
echoPin = 27
switch = 22

# Setting each pin as an input or output
GPIO.setup(greenLedPin, GPIO.OUT)
GPIO.setup(yellowLedPin, GPIO.OUT)
GPIO.setup(redLedPin, GPIO.OUT)
GPIO.setup(trigPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)
GPIO.setup(switch, GPIO.IN)

i=time.time()+60
while (time.time()<i):
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
    distance = round(pulse_duration * 17150, 2)
    print("Distance: ", distance, " cm")

    if GPIO.input(switch) == GPIO.LOW:
        GPIO.output(greenLedPin, GPIO.HIGH)
        GPIO.output(yellowLedPin, GPIO.LOW)
        GPIO.output(redLedPin, GPIO.LOW)
        if (distance <= 10):
            GPIO.output(greenLedPin, GPIO.LOW)
            GPIO.output(yellowLedPin, GPIO.LOW)
            GPIO.output(redLedPin, GPIO.HIGH)
            cur.execute("insert into project_test (spaceid,availabilty,now_date,now_time) values (1,'OCCUPIED' , NOW()::DATE, NOW()::TIMETZ)")
        cur.execute("insert into project_test (spaceid,availabilty,now_date,now_time) values (1,'AVAILABLE' , NOW()::DATE, NOW()::TIMETZ)")

    if GPIO.input(switch) == GPIO.HIGH:
        GPIO.output(greenLedPin, GPIO.LOW)
        GPIO.output(yellowLedPin, GPIO.HIGH)
        GPIO.output(redLedPin, GPIO.LOW)
        if (distance <= 10):
            GPIO.output(greenLedPin, GPIO.LOW)
            GPIO.output(yellowLedPin, GPIO.LOW)
            GPIO.output(redLedPin, GPIO.HIGH)
            cur.execute("insert into project_test (spaceid,availabilty,now_date,now_time) values (1,'OCCUPIED' , NOW()::DATE, NOW()::TIMETZ)")
        cur.execute("insert into project_test (spaceid,availabilty,now_date,now_time) values (1,'Reserved' , NOW()::DATE, NOW()::TIMETZ)")
    time.sleep(5)

cur.execute("select rownumber,spaceid,availabilty,now_date,now_time from project_test")

# Fetches the rows in the table
rows = cur.fetchall()

for r in rows:
    print(f"rownumber {r[0]} spaceid {r[1]} availability {r[2]} date {r[3]} time {r[4]}")

# Commit changes to the database
conn.commit()
# Closes the cursor
cur.close()
# Close the connection
conn.close()


