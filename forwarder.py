import paho.mqtt.client as mqtt
import os

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("Capture/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    #Receives the message and forwards it to cloud
    client.publish("Forward",payload=msg.payload,qos=2,retain=False)
    

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("174.130.55.179", 1883, 60)
# full connect example
# connect(host, port=1883, keepalive=60, bind_address="")

client.loop_forever()
