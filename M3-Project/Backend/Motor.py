import RPi.GPIO as gpio
import time

MOTOR1_IN1 = 11
MOTOR1_IN2 = 13
MOTOR2_IN1 = 19
MOTOR2_IN2 = 21


def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(MOTOR1_IN1, gpio.OUT)
    gpio.setup(MOTOR1_IN2, gpio.OUT)
    gpio.setup(MOTOR2_IN1, gpio.OUT)
    gpio.setup(MOTOR2_IN2, gpio.OUT)


def forward(sec):
    init()
    gpio.output(MOTOR1_IN1, False)
    gpio.output(MOTOR1_IN2, True)
    gpio.output(MOTOR2_IN1, True)
    gpio.output(MOTOR2_IN2, False)
    time.sleep(sec)
    gpio.cleanup()


def reverse(sec):
    init()
    gpio.output(MOTOR1_IN1, True)
    gpio.output(MOTOR1_IN2, False)
    gpio.output(MOTOR2_IN1, False)
    gpio.output(MOTOR2_IN2, True)
    time.sleep(sec)
    gpio.cleanup()


def left_turn(sec):
    init()
    gpio.output(MOTOR1_IN1, True)
    gpio.output(MOTOR1_IN2, False)
    gpio.output(MOTOR2_IN1, True)
    gpio.output(MOTOR2_IN2, False)
    time.sleep(sec)
    gpio.cleanup()


def right_turn(sec):
    init()
    gpio.output(MOTOR1_IN1, False)
    gpio.output(MOTOR1_IN2, True)
    gpio.output(MOTOR2_IN1, False)
    gpio.output(MOTOR2_IN2, True)
    time.sleep(sec)
    gpio.cleanup()


seconds = 3
time.sleep(seconds)
print("forward")
forward(seconds)
time.sleep(seconds - 2)
print("right")
right_turn(seconds)
time.sleep(seconds - 2)
time.sleep(seconds)
print("forward")
forward(seconds)
time.sleep(seconds - 2)
print("right")
right_turn(seconds)
time.sleep(seconds - 2)
