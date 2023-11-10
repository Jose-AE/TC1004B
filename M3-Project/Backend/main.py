from flask import Flask, jsonify, request
from threading import Thread
from flask_socketio import SocketIO, emit
import bmp280_module 
import time
import hcsr04_module
import motor_module 

app = Flask(__name__)
app.debug = True
app.config["SECRET_KEY"] = "secret!"
socketio = SocketIO(app, cors_allowed_origins="*", )


##setup modules
motor_module.setup()
hcsr04_module.setup()




def read_sensors():
    while True:
        time.sleep(1)
        socketio.emit('sensors_updated', {"temperature": bmp280_module.get_pressure(), 
                                            "pressure" : bmp280_module.get_temperature(),
                                            "distance" : hcsr04_module.get_distance()})


#root route 
@app.route("/", methods=["GET"])
def ReturnJSON():
    if request.method == "GET":
        data = {
            "IOT CAR API VERSION ": 1,
        }
        return jsonify(data)


@socketio.on("direction_event")
def handle_direction_event(data):
    dir = data.get("direction", "No direction received")
    print(f"Moving motors: {dir}")

    if dir == "Up":
        motor_module.forward()
    elif dir == "Down":
        motor_module.backward()
    elif dir == "Left":
        motor_module.left()
    elif dir == "Right":
        motor_module.right()
    else:
        motor_module.stop()





@socketio.on("connect")
def test_connect():
    print("Client Connected")


@socketio.on("disconnect")
def test_disconnect():
    print("Client disconnected")



if __name__ == "__main__":
    # Start the sensors task in a separate thread
    thread = Thread(target=read_sensors)
    thread.daemon = True
    thread.start()

    # Run the Flask application 
    socketio.run(app)
