from vpython import vector,box,sphere,rate
import serial
import time

ser=serial.Serial('com3',115200)
roomX=12
roomY=10
roomZ=16
wallT=.5
wallColor=vector(1,1,1)
wallOpacity=.8
frontOpacity=.1
marbleR=.5
ballColor=vector(0,0,1)

myFloor=box(size=vector(roomX,wallT,roomZ),pos=vector(0,-roomY/2,0),color=wallColor,opacity=wallOpacity)
myCeiling=box(size=vector(roomX,wallT,roomZ),pos=vector(0,roomY/2,0),color=wallColor,opacity=wallOpacity)
leftWall=box(size=vector(wallT,roomY,roomZ),pos=vector(-roomX/2,0,0),color=wallColor,opacity=wallOpacity)
rightWall=box(size=vector(wallT,roomY,roomZ),pos=vector(roomX/2,0,0),color=wallColor,opacity=wallOpacity)
backWall=box(size=vector(roomX,roomY,wallT),pos=vector(0,0,-roomZ/2),color=wallColor,opacity=wallOpacity)
frontWall=box(size=vector(roomX,roomY,wallT),pos=vector(0,0,roomZ/2),color=wallColor,opacity=frontOpacity)
marble=sphere(color=ballColor,radius=marbleR)

marbleX=0
deltaX=.1

marbleY=0
deltaY=.1

marbleZ=0
deltaZ=.1

paddleX=2
paddleY=2
paddleZ=-2
paddleOpacity=.8
paddleColor=vector(0,.8,.6)
paddle=box(size=vector(paddleX,paddleY,paddleZ),pos=vector(0,0,roomZ/2),color=paddleColor,opacity=paddleOpacity)
time.sleep(1)
while True:
    while ser.in_waiting>0:
        arduinoData=ser.readline().decode('utf-8').strip().split(',')
        # print(arduinoData)
        xVal=float(arduinoData[0])
        yVal=float(arduinoData[1])
        # zVal=arduinoData[2]
        print(xVal,yVal)
        padX=(roomX/1023.)*xVal-roomX/2
        padY=(-roomY/1023.)*yVal+roomY/2
       
        marbleX=marbleX+deltaX
        marbleY=marbleY+deltaY
        marbleZ=marbleZ+deltaZ


        if marbleX+marbleR>(roomX/2-wallT/2) or marbleX-marbleR<(-roomX/2+wallT/2):
            deltaX=deltaX*(-1)
            marbleX=marbleX+deltaX

        if marbleY+marbleR>(roomY/2-wallT/2) or marbleY-marbleR<(-roomY/2+wallT/2):
            deltaY=deltaY*(-1)
            marbleY=marbleY+deltaY

        if marbleZ+marbleR>(roomZ/2-wallT/2) or marbleZ-marbleR<(-roomZ/2+wallT/2):
            deltaZ=deltaZ*(-1)
            marbleZ=marbleZ+deltaZ

        marble.pos=vector(marbleX,marbleY,marbleZ)
        paddle.pos=vector(padX,padY,roomZ/2)