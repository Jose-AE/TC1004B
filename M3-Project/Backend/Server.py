from flask import Flask, jsonify, request
from flask_socketio import SocketIO, emit


app = Flask(__name__)
app.debug = True
app.config["SECRET_KEY"] = "secret!"
socketio = SocketIO(app, cors_allowed_origins="*", )



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


@socketio.on("connect")
def test_connect():
    print("Client Connected")


@socketio.on("disconnect")
def test_disconnect():
    print("Client disconnected")



if __name__ == "__main__":
    socketio.run(app)
