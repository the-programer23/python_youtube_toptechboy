import serial
arduinoData=serial.Serial('com3',115200)

while True:
    cmd=input('Please Enter Your Command: ')
    cmd=cmd+'\r'
    arduinoData.write(cmd.encode())