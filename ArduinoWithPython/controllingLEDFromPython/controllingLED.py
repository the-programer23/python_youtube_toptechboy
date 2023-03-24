# serial == pyserial library
import serial
arduinoData=serial.Serial('com3',115200)

while True:
    myCmd=input('Enter your color R:G:B 0-255: ')
    myCmd+='\r'
    arduinoData.write(myCmd.encode())