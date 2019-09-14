import paho.mqtt.client as mqtt
import os
import datetime

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("Receive/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" message received!")
    #Gets the image and saves it to disk
    f=open("/data/" + time.time() + ".png")
    f.write(msg.payload)
    f.close()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("52.117.216.245", 1883, 60)

client.loop_forever()
