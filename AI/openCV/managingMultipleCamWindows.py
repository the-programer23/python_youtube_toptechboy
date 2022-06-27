import ctypes
import cv2

user32= ctypes.windll.user32

screenWidth, screenHeight = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
# print(screenWidth, screenHeight)
rows=int(input('Boss, how many rows do you want? '))
columns=int(input('And how many columns? '))

# camWindowWidth=160
# camWindowHeight=90

cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    ignore, frame = cam.read()
    # print(frame)
    # print(ignore)
    frame = cv2.resize(frame, (int(screenWidth/columns), int(screenHeight/columns-50)))
    print("frame width: ",int(screenWidth/columns))
    print("frame height: ",int(screenHeight/columns))
    # cam.set(cv2.CAP_PROP_FRAME_WIDTH, int(screenWidth/columns))
    # cam.set(cv2.CAP_PROP_FRAME_HEIGHT, int(screenHeight/columns))
    for i in range(0,rows):
        print("i: ",i)
        for j in range(0, columns):
            print("j:", j)
            windowName='Window'+str(i) + str(j)
            cv2.imshow(windowName,frame)
            cv2.moveWindow(windowName, int(screenWidth/columns)*j, int(screenHeight/columns-20)*i)
            print(windowName+"- x: ", int(screenWidth/columns*j))
            print(windowName+"- y: ", int(screenHeight/columns)*i)
            print("=============")
    if cv2.waitKey(1) & 0xff == ord('q'):
        break;
cam.release()        