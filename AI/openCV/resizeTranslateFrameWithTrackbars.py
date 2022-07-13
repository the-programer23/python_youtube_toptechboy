import cv2

def myCallback(val):
    global xPos
    print(val)
    xPos=val
def myCallback2(val):
    global yPos
    yPos=val    
def myCallback3(val):
    global width, height
    width=val
    height=int((width*9)/16)    
    # cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
    # cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)

width=640
height=360
maxRes=1920

xPos=0
yPos=0

cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow('my Trackbars')
cv2.moveWindow('my Trackbars',width,0)
cv2.resizeWindow('my Trackbars',400,150)
cv2.createTrackbar('xPos','my Trackbars',0,2000,myCallback)
cv2.createTrackbar('yPos','my Trackbars',0,1000,myCallback2)
cv2.createTrackbar('Width','my Trackbars',width,maxRes,myCallback3)

while True:
    ignore,  frame = cam.read()
    frame=cv2.resize(frame,(width,height))
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',xPos,yPos)
    
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()