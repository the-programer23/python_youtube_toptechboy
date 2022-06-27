import cv2
print(cv2.__version__)

width=640
height=360


cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    ignore, frame = cam.read()
    frameROI=frame[150:210,250:390]
    frameROIGRAY=cv2.cvtColor(frameROI,cv2.COLOR_BGR2GRAY)
    frameROIGRAYBGR=cv2.cvtColor(frameROIGRAY,cv2.COLOR_GRAY2BGR)
   
    # frame[150:210,250:390]=frameROIGRAYBGR
    frame[0:60,0:140]=frameROIGRAYBGR

    cv2.imshow('my webcam', frame)
    cv2.moveWindow('my webcam',0,0)

    cv2.imshow('my ROI', frameROI)
    cv2.moveWindow('my ROI',650,0)

    cv2.imshow('my GRAY ROI',frameROIGRAY)
    cv2.moveWindow('my GRAY ROI',650,90)

    cv2.imshow('MY GRAY ROI BGR', frameROIGRAYBGR)
    cv2.moveWindow('MY GRAY ROI BGR', 650,180)
    
    if cv2.waitKey(1) & 0xff == ord('q'):
        break;
cam.release()        