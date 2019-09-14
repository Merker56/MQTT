import paho.mqtt.client as mqtt
import os
import time
#Timer to be used later
starttime = time.time()

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("174.130.55.179", 1883, 60)
# full connect example
# connect(host, port=1883, keepalive=60, bind_address="")

# Look for file in directory and publish a message to the broker to pick-up the file
# Checks every moment for files
# The broker will move the files to a new location after it sends them out 
while True:
    for file in os.listdir("/Documents"):
        if file.endswith(".png"):
            client.publish("Capture", file, qos = 2)
            time.sleep(60.0 - ((time.time() - starttime) % 60.0))

client.loop_forever()




