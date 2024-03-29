import cv2
import numpy as np
print(cv2.__version__)

def onTrack1(val):
    global hueLow
    hueLow = val
    print("hueLow: ",hueLow)
def onTrack2(val):
    global hueHigh
    hueHigh = val
    print("hueHigh: ",hueHigh)
def onTrack3(val):
    global satLow
    satLow = val
    print("satLow: ",satLow)
def onTrack4(val):
    global satHigh
    satHigh = val
    print("satHigh: ",satHigh)
def onTrack5(val):
    global valLow
    valLow = val
    print("valLow: ",valLow)
def onTrack6(val):
    global valHigh
    valHigh = val
    print("valHigh: ",valHigh)  
def onTrack7(val):
    global hueLow2
    hueLow2 = val
    print("hueLow2: ",hueLow2)
def onTrack8(val):
    global hueHigh2
    hueHigh2 = val      
    print("hueHigh2: ",hueHigh2)            


width=640
height=360

cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow('myTracker')
cv2.moveWindow('myTracker',width,0)
cv2.resizeWindow('myTracker',int(width/2),height-30)

hueLow=10
hueHigh=20

satLow=10
satHigh=250

valLow=10
valHigh=250

cv2.createTrackbar('Hue low','myTracker',90,179,onTrack1)
#the callback function is called automatically after running the program.
cv2.createTrackbar('Hue high','myTracker',152,179,onTrack2)
cv2.createTrackbar('Hue low 2','myTracker',10, 179,onTrack7)
cv2.createTrackbar('Hue high 2','myTracker',20, 179,onTrack8)
cv2.createTrackbar('Sat low','myTracker',165,255,onTrack3)
cv2.createTrackbar('Sat high','myTracker',255,255,onTrack4)
cv2.createTrackbar('Val low','myTracker',111,255,onTrack5)
# if the start value send to createTrackbar func is 0 the callback func is no called automatically after clicking the run btn
cv2.createTrackbar('Val high','myTracker',255,255,onTrack6)

while True:
    ignore, frame = cam.read()

    frameHSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
   
    lowerBound=np.array([hueLow,satLow,valLow])
    #creates triple [ 90 165  10]
    upperBound=np.array([hueHigh,satHigh,valHigh])
    #[135 255 255]

    lowerBound2=np.array([hueLow2,satLow,valLow])
    upperBound2=np.array([hueHigh2,satHigh,valHigh])

    myMask=cv2.inRange(frameHSV,lowerBound,upperBound)
    # myMask=cv2.bitwise_not(myMask) 
    #bitwise_not function turns off the pixels within the lowerBound and upperBound range
    #the turned off pixels are black and the turned on pixels are white
    myMaskSmall=cv2.resize(myMask,(int(width/2),int(height/2)))
    cv2.imshow('my mask',myMaskSmall)
    cv2.moveWindow('my mask',0,height+30) 

    myMask2=cv2.inRange(frameHSV,lowerBound2,upperBound2)
    # myMask2=cv2.bitwise_not(myMask2)
    myMask2Small=cv2.resize(myMask2,(int(width/2),int(height/2)))
    cv2.imshow('My Mask2',myMask2Small)
    cv2.moveWindow('My Mask2',int((width/2*2)),height+30)

    # myMaskComposite = myMask | myMask2
    # using a pipe or calling the add function produce the same result.
    myMaskComposite = cv2.add(myMask,myMask2)

    myObject=cv2.bitwise_and(frame,frame,mask=myMaskComposite)
    myObjectSmall=cv2.resize(myObject,(int(width/2),int(height/2)))  
    cv2.imshow('My Object',myObjectSmall)
    cv2.moveWindow('My Object',int(width/2),height+30)
 
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)

    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()