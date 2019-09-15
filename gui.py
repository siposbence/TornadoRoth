# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 06:14:24 2019
"""

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
