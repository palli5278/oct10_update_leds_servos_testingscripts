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
SERVO_LEFTRIGHT_PIN = 18
SERVO_EYELID_PIN = 17

# Variables
eyeballPos = MIDDLE
eyeballSpeed = 20
eyelidPos = OPEN
eyelidSpeed = 100
blinkTime = time.time() + 0.2
eyeballTurnTime = time.time() + 0.2
crazy = False

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_LEFTRIGHT_PIN, GPIO.OUT)
GPIO.setup(SERVO_EYELID_PIN, GPIO.OUT)
servoLeftRight = GPIO.PWM(SERVO_LEFTRIGHT_PIN, 50)
servoEyelid = GPIO.PWM(SERVO_EYELID_PIN, 50)
servoLeftRight.start(0)
servoEyelid.start(0)

def move_eyelid(pos, velocity):
    duty = pos / 18 + 2
    servoEyelid.ChangeDutyCycle(duty)
    time.sleep(velocity / 1000.0)

def move_eyeball(pos, velocity):
    duty = pos / 18 + 2
    servoLeftRight.ChangeDutyCycle(duty)
    time.sleep(velocity / 1000.0)

def blink_once(velocity):
    move_eyelid(CLOSED, velocity)
    move_eyelid(OPEN, velocity)

try:
    while True:
        if time.time() > eyeballTurnTime and not servoLeftRight.is_moving():
            move_eyeball(eyeballPos, eyeballSpeed)
            eyeballPos = random.randint(RIGHT, LEFT)
            if not crazy:
                eyeballSpeed = random.randint(20, 60)
                eyeballTurnTime = time.time() + random.uniform(0.5, 1)
            else:
                eyeballSpeed = 100
                eyeballTurnTime = time.time() + random.uniform(0.1, 0.3)
        
        if time.time() > blinkTime and not servoLeftRight.is_moving():
            blink_once(eyelidSpeed)
            if not crazy:
                eyelidSpeed = random.randint(100, 255)
                blinkTime = time.time() + random.uniform(1, 5)
            else:
                eyelidSpeed = 255
                blinkTime = time.time() + random.uniform(0.5, 2)
        
except KeyboardInterrupt:
    servoLeftRight.stop()
    servoEyelid.stop()
    GPIO.cleanup()
