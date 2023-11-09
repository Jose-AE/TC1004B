from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO, emit


app = Flask(__name__)


socketio = SocketIO(app, cors_allowed_origins="*")


values = {
    "slider1": 25,
    "slider2": 0,
}


@app.route("/", methods=["GET"])
def ReturnJSON():
    if request.method == "GET":
        data = {
            "Modules": 15,
            "Subject": "Data Structures and Algorithms",
        }

        return jsonify(data)


@socketio.on("connect")
def test_connect():
    emit("after connect", {"data": "Lets dance"})


@socketio.on("custom_event_name")
def handle_custom_event(data):
    mess = data.get("message", "no direction received")
    print(f"Direction: {mess}")


@socketio.on("direction_event")
def handle_direction_event(data):
    dir = data.get("direction", "No message received")
    print(f"Received message from React: {dir}")

    # You can send a response back to the React app if needed
    response = {"response_message": "Message received on the server"}
    emit("custom_event_response", response)


if __name__ == "__main__":
    socketio.run(app)
