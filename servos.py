#eye movement
import RPi.GPIO as GPIO
import time
import random

# Servo positions
LEFT = 150
RIGHT = 40
MIDDLE = 95
OPEN = 160
CLOSED = 80

# GPIO pins
SERVO_LEFTRIGHT_PIN = 35
SERVO_EYELID_PIN = 37

# Variables
eyeballPos = MIDDLE
eyeballSpeed = 20
eyelidPos = OPEN
eyelidSpeed = 100
blinkTime = time.time() + 0.2
eyeballTurnTime = time.time() + 0.2
crazy = False
isEyeballMoving = False
isEyelidMoving = False

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(SERVO_EYELID_PIN, GPIO.OUT)
GPIO.setup(SERVO_LEFTRIGHT_PIN, GPIO.OUT)
GPIO.setup(SERVO_EYELID_PIN, GPIO.OUT)
servoLeftRight = GPIO.PWM(SERVO_LEFTRIGHT_PIN, 50)
servoEyelid = GPIO.PWM(SERVO_EYELID_PIN, 50)
servoLeftRight.start(0)
servoEyelid.start(0)

def move_eyelid(pos, velocity):
    duty = (pos -RIGHT) /(LEFT -RIGHT)* (12 - 2) + 2
    servoEyelid.ChangeDutyCycle(duty)
    time.sleep(velocity / 1000.0)

def move_eyeball(pos, velocity):
    print(pos)
    duty = (pos -RIGHT) /(LEFT -RIGHT)* (12 - 2) + 2
    print(duty)
    servoLeftRight.ChangeDutyCycle(duty)
    time.sleep(velocity / 1000.0)

def blink_once(velocity):
    move_eyelid(CLOSED, velocity)
    move_eyelid(OPEN, velocity)

try:
    while True:
        if time.time() > eyeballTurnTime and not isEyeballMoving:
            move_eyeball(eyeballPos, eyeballSpeed)
            isEyeballMoving = True
            eyeballPos = random.randint(RIGHT, LEFT)
            if not crazy:
                eyeballSpeed = random.randint(20, 60)
                eyeballTurnTime = time.time() + random.uniform(0.5, 1)
            else:
                eyeballSpeed = 100
                eyeballTurnTime = time.time() + random.uniform(0.1, 0.3)
        if time.time() > blinkTime and not isEyelidMoving:
            move_eyelid(CLOSED, eyelidSpeed)
            isEyelidMoving = True
            move_eyelid(OPEN, eyelidSpeed)
            if not crazy:
                eyelidSpeed = random.randint(100, 255)
                blinkTime = time.time() + random.uniform(1, 5)
            else:
                eyelidSpeed = 255
                blinkTime = time.time() + random.uniform(0.5, 2)
except KeyboardInterrupt:
    servoLeftRight.stop()
    servoEyelid.stop()
    time.sleep(0.1)
    GPIO.cleanup()

#right eye horizontal moveme

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(35, GPIO.OUT)
GPIO.setwarnings(False)
pwm=GPIO.PWM(35, 50)

pwm.start(0)

def SetAngle(angle):
        duty = angle / 18 + 2
        GPIO.output(35, True)
        pwm.ChangeDutyCycle(duty)
        sleep(1)
        GPIO.output(35, False)
        pwm.ChangeDutyCycle(0)
while True:
       SetAngle(0)
       sleep(1)
       #SetAngle(90)
       #sleep(2)
       SetAngle(180)

# right eye vertical movement
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.OUT)
GPIO.setwarnings(False)
pwm=GPIO.PWM(37, 50)

pwm.start(0)

def SetAngle(angle):
        duty = angle / 18 + 2
        GPIO.output(37, True)
        pwm.ChangeDutyCycle(duty)
        sleep(1)
        GPIO.output(37, False)
        pwm.ChangeDutyCycle(0)
while True:
       SetAngle(0)
       sleep(1)
       SetAngle(90)
       #sleep(2)
       #SetAngle(180)

#sweep.py
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(35, GPIO.OUT)
pwm = GPIO.PWM(35, 50)

pwm.start(0)

def set_angle(angle):
    duty_cycle = angle / 18 + 2
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.5)  # Adjust the delay as needed

try:
    while True:
        # From 0 to 180 degrees
        for angle in range(0, 181, 10):
            set_angle(angle)

        # From 180 to 0 degrees
        for angle in range(180, -1, -10):
            set_angle(angle)

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()


#test_pos.py
from gpiozero import Servo
from time import sleep

servo = Servo(35)
val = -1
try:
   while True:
        servo.min()
        sleep(1)
        servo.mid()
        sleep(1)
        servo.max()
        sleep(1)

        """servo.value = val
        sleep(0.1)
        val = val + 0.1
        if val > 1:
          val = -1"""
except KeyboardInterrupt:
        print("Program stopped")



    
    











    
                                                           
