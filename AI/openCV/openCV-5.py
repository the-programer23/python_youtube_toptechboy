import cv2
print(cv2.__version__)
import numpy as np

while True:
    # Black and white box
    # frame=np.zeros([250,250],dtype=np.uint8)
    # frame[:125,:]=0
    # frame[126:,:]=
    
    frame=np.zeros([360,640,3],dtype=np.uint8)
    frame[:,:]=[0,0,255]
    frame[:,:125]=[0,255,0]
    cv2.imshow('my window', frame)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break;
