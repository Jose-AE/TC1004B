import paho.mqtt.client as mqtt
import time
import bmp280_module
import time
import hcsr04_module
import motor_module
import db_manager
import gyro_module

BROKER_ADRESS = "192.168.68.120"  # 192.168.1.127

PRINT_SENSORS = False


def manage_distance():
    dist = hcsr04_module.get_distance()

    if dist < 13:
        motor_module.backward()
        time.sleep(2)
        motor_module.left()
        time.sleep(2)
        motor_module.stop()


def read_sensors():
    temp = bmp280_module.get_temperature()
    press = bmp280_module.get_pressure()
    dist = hcsr04_module.get_distance()
    axisz = gyro_module.read_z()

    client.publish("iot/car9/temp", temp)
    client.publish("iot/car9/press", press)
    client.publish("iot/car9/dist", dist)
    client.publish("iot/car9/axisz", axisz)

    # Insert into db
    db_manager.insert_into_BMP280_table(temp, press)
    db_manager.insert_into_HC_SR04_table(dist)
    db_manager.insert_into_GY_61_table(axisz)

    if PRINT_SENSORS:
        print(f"Temperature: {temp} °C")
        print(f"Pressure: {press} Pa")
        print(f"Distance: {dist} cm")
        print(f"Z-axis Gyro: {axisz}")


def on_message(client, userdata, message):
    move = message.payload.decode("utf-8")
    print(f"message recieved [{str(move)}]")

    if move == "0":
        motor_module.stop()
    elif move == "1":
        motor_module.forward()
    elif move == "2":
        motor_module.backward()
    elif move == "3":
        motor_module.right()
        time.sleep(2)
        motor_module.forward()
    elif move == "4":
        motor_module.left()
        time.sleep(2)
        motor_module.forward()
    elif move == "5":
        motor_module.set_speed(50)
    elif move == "6":
        motor_module.set_speed(75)
    elif move == "7":
        motor_module.set_speed(100)
    else:
        print("incorrect value")

    # print("message topic=", message.topic)
    # print("message qos=", message.qos)
    # print("message retain flag=", message.retain)


if __name__ == "__main__":
    ##setup modules
    motor_module.setup()
    hcsr04_module.setup()
    db_manager.connect_to_db()

    print("creating new instance")
    client = mqtt.Client("Equipo 9")
    client.on_message = on_message

    print("connecting to broker")
    client.connect(BROKER_ADRESS)
    client.subscribe("iot/car9/move")
    client.loop_start()

    while True:
        print(f"MQTT Running-[{time.ctime()}]")
        read_sensors()
        manage_distance()
        time.sleep(1)
