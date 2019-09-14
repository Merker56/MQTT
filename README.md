# MQTT

##Spin-up code for each docker container
###Mosquitto docker container
This sets-up the mosquitto server and exposes port 1883 for other systems to connect.
```
docker run --name mosquitto --network hw03 -v /home/deeplearner/Documents/mosquitto.py:/mosquitto.py -v /home/deeplearner/Documents:/Documents -p 1883:1883 -ti python:3.7-alpine sh 
apk update && apk add mosquitto
/usr/sbin/mosquitto
```
###Forwarder docker container
```
docker run --name forwarder --network hw03 -v /home/deeplearner/Documents/forwarder.py:/forwarder.py -v /home/deeplearner/Documents:/Documents -ti python:3.7-alpine sh 
apk update && apk add mosquitto-clients
pip install paho-mqtt
python forwarder.py
```

###
