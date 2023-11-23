import paho.mqtt.client as mqtt
import time
broker_adress= "192.168.1.127"
move=0

def on_message(client, userdata, message):
    move= message.payload.decode ("utf-8")
    print ("message recieved",str(move))
    if move=="0":
        print ("correct number")
        
    else:
     print("incorrect")
    print ("message topic=",message.topic)
    print ("message qos=",message.qos)
    print ("message retain flag=",message.retain)
      
print ("creating new instance")
client=mqtt.Client("Equipo 9")
client.on_message=on_message

print("connecting to broker")
client.connect(broker_adress)
client.loop_start()

temper=36.8
press=600
dist=200
axisz=1

client.publish("iot/car9/temp",temper)
client.publish("iot/car9/press",press)
client.publish("iot/car9/dist",dist)
client.publish("iot/car9/axisz",axisz)



while True:
    print("1")
    print("2")
    print("3")
    time.sleep(2)
     
