# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 08:44:33 2019

@author: Bence Sipos
"""


import threading
import paho.mqtt.client as mqtt
import time
import cv2
import math
import numpy as np

def dotproduct(v1, v2):
  return sum((a*b) for a, b in zip(v1, v2))

print('1')
vcap = cv2.VideoCapture("rtsp://hackathon:!Hackath0n@192.168.0.2:554/2")
#vcap = cv2.VideoCapture(0)

broker_url = "192.168.0.1"
broker_port = 1883
user_name = "hackatlon"
password = "!Hackathl0n"

client = mqtt.Client()
client.username_pw_set (user_name, password)
client.connect(broker_url, broker_port)

print('2')
dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
#client.publish(topic="freq", payload="13", qos=0, retain=False)
#client.publish(topic="move", payload="left", qos=0, retain=False)
#time.sleep(2.5)

client.publish(topic="move", payload="stop", qos=0, retain=False)
task_list = []
value_list = []

def angle(vcap):
    print('k')
    ret, frame = vcap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    res = cv2.aruco.detectMarkers(gray,dictionary)
    if len(res[0]) > 0:
        
        porgovektor = res[0][0][0,0]-res[0][0][0,1]
        porgovektor = porgovektor/np.linalg.norm(porgovektor)
        print(np.linalg.norm(porgovektor))
        v2 = np.array([0,1])
        #cv2.aruco.drawDetectedMarkers(frame,res[0],res[1])  
        #cv2.imshow('VIDEO', frame)
        #cv2.waitKey(1)   
        print(porgovektor)
        return(math.acos(np.dot(porgovektor, v2))* 180 / math.pi)


def control(task_list, value_list):
    if task_list[-1] == 1:#turn
        client.publish(topic="move", payload="stop", qos=0, retain=False)
        if value_list[-1] < 0:
            client.publish(topic="move", payload="left", qos=0, retain=False)
        else:
            client.publish(topic="move", payload="right", qos=0, retain=False)
        if angle(vcap)<value_list[-1]:
            client.publish(topic="freq", payload="1", qos=0, retain=False)
        elif abs(angle(vcap)-value_list[-1])<3:
            client.publish(topic="move", payload="stop", qos=0, retain=False)
            task_list[] = task_list[:-1]
            value_list[-1] = value_list[:-1]
        else:
            client.publish(topic="move", payload="stop", qos=0, retain=False)
            
    if task_list[-1] == 2:# stop
        client.publish(topic="move", payload="stop", qos=0, retain=False)
    
    if task_l == 4:# pause
        client.publish(topic="move", payload="stop", qos=0, retain=False)
    if task_list[-1]==5:
        value_list[-1] = 0
    #print(vcap)

while(1):

    ret, frame = vcap.read()
    cv2.imshow('VIDEO', frame)
    cv2.waitKey(1)
'''

while(1):
    print(angle(vcap))
