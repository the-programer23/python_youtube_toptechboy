#Arduino file name = ReadPotentiometerVolts (it's the file where arduinoData is coming from)
import time
import serial
from vpython import *
arduinoData=serial.Serial('com4',9600)
time.sleep(2)
tube=cylinder(color=color.blue,radius=1,length=5,axis=vector(0,1,0))
label=label(text='5',box=False,pos=vector(0,.2,0))
while True:
    while arduinoData.inWaiting()==0:
        pass
    potVal=arduinoData.readline()
    potVal=str(potVal,'utf-8')
    potVal=int(potVal.strip('\r\n'))
    voltage=(5./1023.)*potVal
    if voltage == 0:
        voltage=0.001
    tube.length=voltage
    voltage=round(voltage,1)
    label.text=str(voltage)
