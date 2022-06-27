import cv2

print(cv2.__version__)

myWindowCam1 = 'my Webcam 1'
myWindowCam2 = 'my Webcam 2'
myWindowCam3 = 'my Webcam 3'
myWindowCam4 = 'my Webcam 4'

width=160
height=90
# width=320
# height=180
# width=640
# height=360

#0 is the port
#CAP_DSHOW makes it launch faster
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
#FPS IS frames per second
cam.set(cv2.CAP_PROP_FPS, 30)
#this cmd let us set the codec so the video runs smooth on windows
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
while True:
    ignore, frame = cam.read()
    grayFrame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cv2.imshow(myWindowCam1, frame)
    cv2.moveWindow(myWindowCam1,0,0)

    cv2.imshow(myWindowCam2,grayFrame)
    cv2.moveWindow(myWindowCam2,width,0)

    cv2.imshow(myWindowCam3,grayFrame)
    cv2.moveWindow(myWindowCam3,0,height)

    cv2.imshow(myWindowCam4,frame)
    cv2.moveWindow(myWindowCam4,width,height)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
    
cam.release()    