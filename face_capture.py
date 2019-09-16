import numpy as np
import cv2
import datetime
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

client = mqtt.Client()
client.on_connect = on_connect
client.connect("174.130.55.179", 1883, 60)

#Search for faces
face_cascade = cv2.CascadeClassifier('/usr/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')
# 1 should correspond to /dev/video1 , your USB camera. The 0 is reserved for the TX2 onboard camera
cap = cv2.VideoCapture(1)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # We don't use the color information, so might as well save space
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # face detection and other logic goes here
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    # when a face is found, crop it and save it
    for (x,y,w,h) in faces:
        # crop down to just the face
        cropped_face = frame[y:y+h, x:x+w].copy()
        # save image copy
        print("Face detected")
        rc, jpg = cv2.imencode('.png', cropped_face)
        msg = jpg.tobytes()
        client.publish("Capture/#", payload=msg, qos=2)
        print("Published to Capture")

