import ctypes
import cv2 
import numpy as np

def onTrack1(val):
    global hueLow
    hueLow = val
def onTrack2(val):
    global hueHigh
    hueHigh = val
def onTrack3(val):
    global satLow
    satLow = val
def onTrack4(val):
    global satHigh
    satHigh = val
def onTrack5(val):
    global valLow
    valLow = val
def onTrack6(val):
    global valHigh
    valHigh = val                    

user32=ctypes.windll.user32
screenWidth, screenHeight = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
width=640
height=360
xPos=0
yPos=0
hueLow=0
hueHigh=0
satLow=0
satHigh=0
valLow=0
valHigh=0

cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

cv2.namedWindow('myTracker')
cv2.namedWindow('MyWebcam')
cv2.moveWindow('MyWebcam',0,0)


#the callback function is called automatically after running the program.
# if the start value send to createTrackbar func is 0 the callback func is not called automatically after clicking the run btn
cv2.createTrackbar('Hue Low','myTracker',30,179,onTrack1)
cv2.createTrackbar('Hue High','myTracker',58,179,onTrack2)
cv2.createTrackbar('Sat Low','myTracker',69,255,onTrack3)
cv2.createTrackbar('Sat High','myTracker',183,255,onTrack4)
cv2.createTrackbar('Val Low','myTracker',63,255,onTrack5)
cv2.createTrackbar('Val High','myTracker',188,255,onTrack6)

while True:
    ignore, frame = cam.read()
    frame=cv2.flip(frame,1)
    frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lowerBound=np.array([hueLow,satLow,valLow])
    upperBound=np.array([hueHigh,satHigh,valHigh])
    myMask=cv2.inRange(frameHSV,lowerBound,upperBound)
    contours,junk=cv2.findContours(myMask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area=cv2.contourArea(contour)
        if area >= 200:
            x,y,w,h=cv2.boundingRect(contour)
            print(x,y)
            #(colStart,rowStart),(colEnd,rowEnd)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
            xPos=x
            yPos=y
            xPos=int(xPos/width*screenWidth)
            yPos=int(yPos/height*screenHeight)
            cv2.moveWindow('MyWebcam',xPos,yPos)

    cv2.imshow('MyWebcam',frame)
   

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()    

