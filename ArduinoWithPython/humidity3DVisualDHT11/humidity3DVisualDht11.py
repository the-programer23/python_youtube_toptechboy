import time
import serial
from vpython import cylinder, vector, color, arrow, box, text
import numpy as np

myCaseRadius=1.4
myCaseLength=.4
arrowLength=1.2
arrowWidth=.1
tickX=.1
tickY=.02
tickZ=.02
ser=serial.Serial('com3',115200)
myCase=cylinder(
    radius=myCaseRadius,
    length=myCaseLength,
    color=color.blue,
    axis=vector(0,0,1))
myArrow=arrow(
    length=arrowLength,
    shaftWidth=arrowWidth,
    color=color.red,
    pos=vector(0,0,myCaseLength+(arrowWidth)),
    axis=vector(np.cos(5*np.pi/6),np.sin(5*np.pi/6),0))
labelText=0
for theta in np.linspace(5*np.pi/6,np.pi/6,11):
    box(
        color=color.black,
        size=vector(tickX,tickY,tickZ),
        pos=vector(np.cos(theta)*arrowLength,np.sin(theta)*arrowLength,myCaseLength),
        axis=vector(np.cos(theta),np.sin(theta),0)
    )
    text(
        color=color.white,
        height=.1,
        align="center",
        text=str(labelText),
        pos=vector(np.cos(theta)*arrowLength,np.sin(theta)*arrowLength,myCaseLength),
        axis=vector(np.cos(theta)*arrowLength,np.sin(theta)*arrowLength,0)
    )
    labelText+=10
time.sleep(.5)
while True:
    while ser.in_waiting>0:
        arduinoData=ser.readline().decode('utf-8').strip()
        humidity=float(arduinoData)
        print(humidity)
        theta=-np.pi/150*humidity+5*np.pi/6
        myArrow.axis=vector(np.cos(theta),np.sin(theta),0)