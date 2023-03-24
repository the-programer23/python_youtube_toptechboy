import time
import serial
from vpython import sphere, cylinder, vector, text, label

bulb=sphere(radius=1,color=vector(1,0,0),pos=vector(0,-3,0))
mercury=cylinder(radius=.6,color=vector(1,0,0),axis=vector(0,1,0),length=6,pos=vector(0,-3,0))
bulbGlass=sphere(radius=1.2,color=vector(1,1,1),opacity=.2,pos=vector(0,-3,0))
mercuryGlass=cylinder(radius=.8,color=vector(1,1,1),opacity=.2,axis=vector(0,1,0),length=6,pos=vector(0,-3,0))
digValue=label(text='45',pos=vector(0,-3,1),box=False,height=20)
for temp in range(0,46,5):
    tickPos=(4.5/46)*temp+1.5
    cylinder(radius=.7,axis=vector(0,1,0),length=.1,pos=vector(0,tickPos-3,0),color=vector(0,0,0))
    text(text=str(temp),color=vector(1,1,1),pos=vector(-1.4,tickPos-3,0),height=.24)

arduinoData=serial.Serial('com5',115200)
time.sleep(.5)
while True:
    while arduinoData.inWaiting()==0: # type: ignore
        pass
    dataPacket=arduinoData.readline()
    dataPacket=str(dataPacket,'utf-8')
    # removes new line
    dataPacket=dataPacket.strip('\r\n')
    dataPacket=dataPacket.split(',')
    temp=float(dataPacket[0])
    humidity=float(dataPacket[1])
    length=(4.5/46)*temp+1.5
    mercury.length=length
    digValue.text=str(temp)
