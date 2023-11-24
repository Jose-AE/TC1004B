import time


GPIO_TRIGGER = 18 #12 board
GPIO_ECHO = 24 #18 board

try:
    import RPi.GPIO as GPIO
    GPIO.setwarnings(False)
    GPIO_IMPORTED = True

except ImportError:
    print("Error importing RPi.GPIO in hcsr04_module")
    GPIO_IMPORTED = False





def setup():
    if GPIO_IMPORTED:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(GPIO_ECHO, GPIO.IN)



def get_distance():
    if GPIO_IMPORTED:
        # set trigger to HIGH
        GPIO.output(GPIO_TRIGGER, True)

        # set trigger after 0.01 ms to LOW
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER, False)

        startTime = time.time()
        arrivalTime = time.time()

        # store startTime
        while GPIO.input(GPIO_ECHO) == 0:
            startTime = time.time()

        # store arrivalTime
        while GPIO.input(GPIO_ECHO) == 1:
            arrivalTime = time.time()

        # Time difference between start and arrival
        timeElapsed = arrivalTime - startTime
        # multiply by the speed of sound (34300 cm/s)
        # and divide by 2, there and back again
        distance = (timeElapsed * 34300) / 2

        return distance
    else:
        return 0

# if __name__ == '__main__':
#     try:
#         while True:
#             d = get_distance()
#             print ("Measured distance = %.1f cm" % d)
#             time.sleep(1)

#         # When canceling with CTRL+C, resetting
#     except KeyboardInterrupt:
#         print("Measurement stopped by user")
#         GPIO.cleanup()
