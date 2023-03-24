import time
#pip install pyserial to import serial
import serial
arduinoData=serial.Serial('com4',115200)
time.sleep(1)
while True:
    while arduinoData.inWaiting()==0:
        pass
    dataPacket=arduinoData.readline() 
    dataPacket=str(dataPacket,'utf-8')
    dataPacket=dataPacket.strip('\r\n')
    splitPacket=dataPacket.split(",")
    x=float(splitPacket[0])
    y=float(splitPacket[1])
    z=float(splitPacket[2])
    print("x = ",x," y = ",y," z = ",z)