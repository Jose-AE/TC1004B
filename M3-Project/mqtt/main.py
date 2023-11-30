from flask import Flask, jsonify, request
from threading import Thread
from flask_socketio import SocketIO, emit
import bmp280_module
import time
import hcsr04_module
import RPi.GPIO as GPIO

app = Flask(__name__)
app.debug = False
app.config["SECRET_KEY"] = "secret!"
socketio = SocketIO(app, cors_allowed_origins="*")

# Configuración de los pines GPIO para los motores
en_a = 4  # 7 BOARD - Right Motor Enable
in1 = 27  # 13 BOARD - Right Motor In1
in2 = 17  # 11 BOARD - Right Motor In2
in3 = 5  # 29 BOARD - Left Motor In3
in4 = 6  # 31 BOARD - Left Motor In4
en_b = 13  # 33 BOARD - Left Motor Enable

DEBUG_MODE = True

try:
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(in1, GPIO.OUT)
    GPIO.setup(in2, GPIO.OUT)
    GPIO.setup(en_a, GPIO.OUT)
    GPIO.setup(in3, GPIO.OUT)
    GPIO.setup(in4, GPIO.OUT)
    GPIO.setup(en_b, GPIO.OUT)

    q = GPIO.PWM(en_a, 100)  # 100 hertz
    p = GPIO.PWM(en_b, 100)  # 100 hertz
    p.start(75)  # 75% duty cycle
    q.start(75)  # 75% duty cycle

except ImportError:
    print("Error importing RPi.GPIO")
    GPIO_IMPORTED = False


def forward():
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in4, GPIO.HIGH)
    GPIO.output(in3, GPIO.LOW)


def right():
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)
    GPIO.output(in3, GPIO.HIGH)


def rotate_180():
    right()
    time.sleep(2)  # Ajustar el tiempo


def read_sensors():
    while True:
        time.sleep(1)
        distance = hcsr04_module.get_distance()
        socketio.emit(
            "sensors_updated",
            {
                "temperature": bmp280_module.get_temperature(),
                "pressure": bmp280_module.get_pressure(),
                "distance": distance,
            },
        )

        if distance <= 10:
            rotate_180()
            forward()


if __name__ == "__main__":
    hcsr04_module.setup()
    # Start the sensors task in a separate thread
    thread = Thread(target=read_sensors)
    thread.daemon = True
    thread.start()

    # Run the Flask application
    socketio.run(app, host="0.0.0.0", allow_unsafe_werkzeug=True)
