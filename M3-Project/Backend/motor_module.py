# Right Motor
en_a = 4 #7 BOARD
in1 = 17 #11 BOARD
in2 = 27 #13 BOARD

# Left Motor
in3 = 5 #29 BOARD
in4 = 6 #31 BOARD
en_b = 13 #33 BOARD

DEBUG_MODE = True

try:
    import RPi.GPIO as GPIO
    GPIO.setwarnings(False)
    GPIO_IMPORTED = True

except ImportError:
    print("Error importing RPi.GPIO in motor_module")
    GPIO_IMPORTED = False


def setup():
    if GPIO_IMPORTED:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(in1,GPIO.OUT)
        GPIO.setup(in2,GPIO.OUT)
        GPIO.setup(en_a,GPIO.OUT)

        GPIO.setup(in3,GPIO.OUT)
        GPIO.setup(in4,GPIO.OUT)
        GPIO.setup(en_b,GPIO.OUT)

        q=GPIO.PWM(en_a,100) #100 hertz
        p=GPIO.PWM(en_b,100) #100 hertz
        p.start(75) #75% duty cycle
        q.start(75) #75% duty cycle

        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)




def forward():
    if GPIO_IMPORTED:
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)

        GPIO.output(in4,GPIO.HIGH)
        GPIO.output(in3,GPIO.LOW)

    if DEBUG_MODE:
        print("Moving motors forward")

def backward():
    if GPIO_IMPORTED:
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)

        GPIO.output(in4,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)

    if DEBUG_MODE:
        print("Moving motors backward")


def right():
    if GPIO_IMPORTED:
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)

        GPIO.output(in4,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)

    if DEBUG_MODE:
        print("Moving motors right")


def left():
    if GPIO_IMPORTED:
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)

        GPIO.output(in4,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)

    if DEBUG_MODE:
        print("Moving motors left")


def stop():
    if GPIO_IMPORTED:
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)

        GPIO.output(in4,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)

    if DEBUG_MODE:
        print("Stopping motors")


def set_speed():
    pass



#GPIO.cleanup()


