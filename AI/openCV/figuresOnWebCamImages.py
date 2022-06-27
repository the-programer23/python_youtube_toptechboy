import cv2
import time
print(cv2.__version__)

width=640
height=360
myRadius=25
myColor=(255,255,255)
myThick=2
myText="Fabian Pinzon"
myFont=cv2.FONT_HERSHEY_DUPLEX
fontHeight=1
fontThickness=1
startColumn=250
endColumn=390
startRow=140
endRow=220
lineThick=2

startTime=time.time()
count = 0
elapsedSecs=0
fps = 0

cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    ignore, frame = cam.read()
    frame[140:220,250:390]=(0,0,0) #solid rectangle

    #rectangle(frame,(startColumn,startRow),(endColumn,endRow),color,thickness)
    cv2.rectangle(frame,(startColumn,startRow),(endColumn,endRow),(0,255,0),lineThick)
    # cv2.rectangle(frame,(250,140),(390,220),(0,255,0),-1) #solid rectangle

    #cv2.circle(frame,(x,y),radius,color, thickness)
    cv2.circle(frame,(int(width/2),int(height/2)),myRadius,myColor,myThick)
    cv2.putText(frame, myText, (200,60), myFont, fontHeight, (0,0,255), fontThickness)

    #fps start
    count +=1
    elapsedSecs = int(time.time() - startTime)  

    cv2.putText(frame, str(fps)+"FPS", (80,60), myFont, fontHeight, (255,0,0), fontThickness)

    if elapsedSecs == 1:
        print("1 sec elapsed")
        fps=count
        count = 0
        startTime = time.time()
    #fps end

    cv2.imshow('my webcam', frame)
    cv2.moveWindow('my webcam',0,0)

    
    if cv2.waitKey(1) & 0xff == ord('q'):
        break;
cam.release()        