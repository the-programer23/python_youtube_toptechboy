import cv2
import mediapipe as mp
print(cv2.__version__)

width=1280
height=720
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

faceMesh=mp.solutions.face_mesh.FaceMesh(static_image_mode=False,max_num_faces=3,refine_landmarks=True,min_detection_confidence=.5)
mpDraw=mp.solutions.drawing_utils

font=cv2.FONT_HERSHEY_SIMPLEX
fontZise=.5
fontColor=(0,255,255)
fontThick=1

while True:
    ignore,  frame = cam.read()
    frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results=faceMesh.process(frameRGB)
    if results.multi_face_landmarks != None:
        for faceLandmarks in results.multi_face_landmarks:                                                   
            mpDraw.draw_landmarks(image=frame,landmark_list=faceLandmarks,connections=mp.solutions.face_mesh.FACEMESH_CONTOURS)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()