# MQTT

## Spin-up code for each docker container
### Jetson Docker Containers
#### Mosquitto docker container

This sets-up the mosquitto server and exposes port 1883 for other systems to connect. It will be the channel that allows other containers to do their work.
```
docker run --name mosquitto --network hw03 -v /home/deeplearner/Documents/mosquitto.py:/mosquitto.py -v /home/deeplearner/Documents:/Documents -p 1883:1883 -ti python:3.7-alpine sh 
apk update && apk add mosquitto
/usr/sbin/mosquitto
```

#### Forwarder docker container

After an image is captured, this container will take the image and 'forward' it over to the virtual machine. This is done using python code to automate the process (`forwarder.py`).
```
docker run --name forwarder --network hw03 -v /home/deeplearner/Documents/forwarder.py:/forwarder.py -v /home/deeplearner/Documents:/Documents -ti python:3.7-alpine sh 
apk update && apk add mosquitto-clients
pip install paho-mqtt
python forwarder.py
```

#### Capture docker container

#### Receiver docker container
This docker container is on the virtual server and will receive messages off of the 'forwarder' container. This is done via the `receiver.py` script.

```

```
#### Saver docker container
This docker container has access to the virtual Object Based Storage location. It will take the image message and turn it into a `.png` file on the storage. This is done via the saver.py script.
```

```
