import cv2
print(cv2.__version__);

def myCallback(val):
    global xPos
    xPos=val
    print('xPos: ', val)
def myCallback2(val):
    global yPos
    yPos=val
    print('yPos: ', val)    
def myCallback3(val):
    global radius
    radius=val    
def myCallback4(val):
    global myThick
    myThick=val    

width=640
height=360
radius=24
myThick=1
xPos=int(width/2)
yPos=int(height/2)
trackbarWindowName='myTrackbars'
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow(trackbarWindowName)
cv2.resizeWindow(trackbarWindowName,400,200)
cv2.moveWindow(trackbarWindowName,width,0)
cv2.createTrackbar('xPos',trackbarWindowName,xPos,width-radius,myCallback)
cv2.createTrackbar('yPos',trackbarWindowName,yPos,height-radius,myCallback2)
cv2.createTrackbar('radius',trackbarWindowName,radius,int(height/2),myCallback3)
cv2.createTrackbar('myThick',trackbarWindowName,myThick,10,myCallback4)

while True:
    ignore,  frame = cam.read()
    if myThick==0:
        myThick=(-1)
    cv2.circle(frame,(xPos,yPos),radius,(255,0,0),myThick)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
 
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()