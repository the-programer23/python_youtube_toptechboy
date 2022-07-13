import cv2
import numpy as np

#np.zeros([rows|height, columns|width])    
x=np.zeros([256,720,3],dtype=np.uint8)

y=np.zeros([256,720,3],dtype=np.uint8)

#x[row-1][column-1]
# x[1][2]=(0,1,0)

for row in range(0,256,1):
    for column in range(0,720,1):
        x[row][column]=(int(column/4),row,255)
        y[row][column]=(int(column/4),255,row)

x=cv2.cvtColor(x,cv2.COLOR_HSV2BGR)   
y=cv2.cvtColor(y,cv2.COLOR_HSV2BGR)

while True:    
    cv2.imshow('my saturationWindow',x)
    cv2.moveWindow('my saturationWindow',0,0)
    cv2.imshow('my valWindow',y)
    cv2.moveWindow('my valWindow',0,286)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cv2.destroyAllWindows()    


# [[[0 0 0][0 0 0][0 0 0][0 0 0]] 
#  [[0 0 0][0 0 0][0 1 0][0 0 0]] 
#  [[0 0 0][0 0 0][0 0 0][0 0 0]]]

