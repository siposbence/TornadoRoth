import threading
import paho.mqtt.client as mqtt
import time
import cv2
import math
import numpy as np
from graphics import *

#open gui
win=GraphWin("Bosch servo control GUI", 800, 700)
win.setBackground("white")

pause = Entry(Point(200,50),10)
pause.draw(win)
pauseButton = Rectangle(Point(150,100),Point(250,200))
pauseButton.setFill(color_rgb(0,255,255))
pauseButton.draw(win)
pauseText = Text(Point(200,150),"pause")
pauseText.draw(win)

turn = Entry(Point(400,50),10)
turn.draw(win)
turnButton = Rectangle(Point(350,100),Point(450,200))
turnButton.setFill(color_rgb(0,255,255))
turnButton.draw(win)
turnText = Text(Point(400,150),"turn")
turnText.draw(win)


speed = Entry(Point(600,50),10)
speed.draw(win)
speedButton = Rectangle(Point(550,100),Point(650,200))
speedButton.setFill(color_rgb(0,255,255))
speedButton.draw(win)
speedText = Text(Point(600,150),"speed")
speedText.draw(win)

baseButton = Rectangle(Point(350,300),Point(450,400))
baseButton.setFill(color_rgb(0,255,255))
baseButton.draw(win)
baseText = Text(Point(400,350),"base")
baseText.draw(win)

stopButton = Rectangle(Point(150,300),Point(250,400))
stopButton.setFill(color_rgb(255,0,0))
stopButton.draw(win)
stopText = Text(Point(200,350),"stop")
stopText.draw(win)

runButton = Rectangle(Point(150,500),Point(250,600))
runButton.setFill(color_rgb(0,255,0))
runButton.draw(win)
runText = Text(Point(200,550),"run")
runText.draw(win)

deleteButton = Rectangle(Point(350,500),Point(450,600))
deleteButton.setFill(color_rgb(255,255,0))
deleteButton.draw(win)
deleteText = Text(Point(400,550),"delete")
deleteText.draw(win)


inputData = 0
line = 240
commandList = []
while True:  
    p = win.getMouse()
    if p.x < 250 and p.x > 150 and p.y >100 and p.y < 200:
        inputData = pause.getText()
        newText = Text(Point(550,line),"pause "+inputData+" ms")
        newText.draw(win)
        line += 20
        commandList.append((4,int(inputData)))
        print("pause",inputData)
    if p.x < 450 and p.x > 350 and p.y >100 and p.y < 200:
        inputData = turn.getText()
        newText = Text(Point(550,line),"turn "+inputData+"°")
        newText.draw(win)
        line += 20
        commandList.append((1,int(inputData)))
        print("turn",inputData)
    if p.x < 650 and p.x > 550 and p.y >100 and p.y < 200:
        inputData = speed.getText()
        newText = Text(Point(550,line),"speed "+inputData+" Hz")
        newText.draw(win)
        line += 20
        commandList.append((3,int(inputData)))
        print("speed",inputData)
    if p.x < 450 and p.x > 350 and p.y >300 and p.y < 400:
        newText = Text(Point(550,line),"base")
        newText.draw(win)
        line += 20
        commandList.append((5,0))
        print("base")
    if p.x < 250 and p.x > 150 and p.y >300 and p.y < 400:
        newText = Text(Point(550,line),"stop")
        newText.draw(win)
        line += 20
        commandList.append((2,0))
        print("stop")
    if p.x < 250 and p.x > 150 and p.y >500 and p.y < 600:
        newText = Text(Point(550,line),"run")
        newText.draw(win)
        line += 20
        print("Run")
        print(commandList)
        break
    if p.x < 450 and p.x > 350 and p.y >500 and p.y < 600:
        newText.undraw()
        line -= 20
        commandList.pop()
        print("delete")
    

win.getMouse()
win.close()
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
