#Arduino file name = ReadPotentiometerVolts (it's the file where arduinoData is coming from)
import time
import serial
from vpython import *
import numpy as np
arduinoData=serial.Serial('com5',9600)
time.sleep(2)
arrowLength=1
arrowWidth=.02
boxX=2.5
boxY=2
boxZ=.1

#.9 removes 10% to boxY/2
boxGap=.9*boxY/2
myCase=box(color=color.white,size=vector(boxX,boxY,boxZ),pos=vector(0,boxGap,-boxZ/2-arrowWidth/2))
myArrow=arrow(length=arrowLength,shaftwidth=arrowWidth,color=color.red,axis=vector(1,1,0))

tickX=.1
tickY=.02
tickZ=.02

minorTickX=tickX/2

labelText=0
for thetha in np.linspace(0,6,6):
    print(thetha)
labelFactor=1.1
for theta in np.linspace(5*np.pi/6,np.pi/6,6):
    tickMajor=box(
        color=color.black,
        size=vector(tickX,tickY,tickZ),
        pos=vector(np.cos(theta)*arrowLength,np.sin(theta)*arrowLength,0),
        axis=vector(np.cos(theta),np.sin(theta),0))
    text(color=color.black,
        height=.1,align='center',
        text=str(labelText),
        axis=vector(np.cos(theta-np.pi/2)*arrowLength,np.sin(theta-np.pi/2)*arrowLength,0),
        pos=vector(np.cos(theta)*arrowLength*labelFactor,np.sin(theta)*arrowLength*labelFactor,0))    
    labelText+=1   
    # for thetaMinor in np.linspace(theta,,9)
tickFraction=.5    
for theta in np.linspace(5*np.pi/6,np.pi/6,51):
    tickMinor=box(
        color=color.black,
        size=vector(minorTickX*tickFraction,tickY*tickFraction,tickZ*tickFraction),
        pos=vector(np.cos(theta),np.sin(theta),0),
        axis=vector(np.cos(theta)*arrowLength,np.sin(theta)*arrowLength,0))
pivotRadius=.02
pivotLength=.02
cylinder(length=pivotLength,radius=pivotRadius,color=color.red,axis=vector(0,0,1),pos=vector(0,0,-pivotLength/2))
text(text='voltOmeter',color=color.green,pos=vector(0,1.5,0),height=.25,align='center')
while True:
    while arduinoData.inWaiting()==0:
        pass
    potVal=arduinoData.readline()
    potVal=str(potVal,'utf-8')
    potVal=int(potVal.strip('\r\n'))
    # label.text=str(potVal)
    theta=-2*np.pi/3069*potVal+5*np.pi/6
    myArrow.axis=vector(arrowLength*np.cos(theta),arrowLength*np.sin(theta),0)
    # for theta in np.linspace(5*np.pi/6,np.pi/6,150):
    #     rate(25)
    #     myArrow.axis=vector(arrowLength*np.cos(theta),arrowLength*np.sin(theta),0)
    # for theta in np.linspace(np.pi/6,5*np.pi/6,150):
    #     rate(25)
    #     myArrow.axis=vector(arrowLength*cos(theta),arrowLength*sin(theta),0)    