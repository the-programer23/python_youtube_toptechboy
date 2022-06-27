import cv2
import time
print(cv2.__version__)

width=640
height=360
myColor=(255,255,255)
myText="Fabian Pinzon"
myFont=cv2.FONT_HERSHEY_DUPLEX
fontHeight=1
fontThickness=1

cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

timeLast=time.time()
time.sleep(.1)

fpsFilter= 30;

while True:
    delayTime=time.time() - timeLast
    fps=1/delayTime 
    fpsFilter=fpsFilter*.8+fps*.2
    timeLast=time.time()

    ignore, frame = cam.read()

    cv2.putText(frame, myText, (200,60), myFont, fontHeight, (0,0,255), fontThickness)
    cv2.rectangle(frame, (0,0), (120,40), (255,0,255), -1)
    cv2.putText(frame, str(int(fps))+' fps', (5,30), myFont, fontHeight, (0,255,0), 2)

    cv2.imshow('my webcam', frame)
    cv2.moveWindow('my webcam',0,0)

    
    if cv2.waitKey(1) & 0xff == ord('q'):
        break;
cam.release()        