import paho.mqtt.client as mqtt
import os
import time

global i
i = 0
print("initiated count")
os.chdir("/data")
print("Directory changed")
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("Receive/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" message received!")
    #Gets the image and saves it to disk
    global i
    i = i + 1
    print("Incremented count")
    f=open(f"face_{i}.png", "w+")
    print("File Opened!")
    f.write(msg.payload)
    print("Content written")
    f.close()
    print("File saved!")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("174.130.55.179", 1883, 60)

client.loop_forever()
