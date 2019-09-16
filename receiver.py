import paho.mqtt.client as mqtt


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("Forward/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    #Gets the image and passes to Saver
    client.publish("Receive",payload=msg.payload)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("174.130.55.179", 1883, 60)
# full connect example
# connect(host, port=1883, keepalive=60, bind_address="")

client.loop_forever()
