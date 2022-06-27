import cv2
import numpy as np
print(cv2.__version__)

boardSize = int(input('What size is your board, boss? '))
numSquares = int(input('How many squares? '))
squareSize = int(boardSize/numSquares)

darkColor=(0,0,0)
lightColor=(175,175,175)
nowColor=darkColor 

def flip():
    global nowColor 
    if  nowColor == darkColor:
        nowColor = lightColor
    else:
        nowColor = darkColor 

x=np.zeros([boardSize, boardSize, 3], np.uint8)
while True:
    for row in range(0,numSquares):
        for column in range(0,numSquares):
            x[squareSize*row:squareSize*(row+1) , squareSize*column:squareSize*(column+1)] = nowColor
            flip()
        flip()      

    cv2.imshow('My Checkerboard', x)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break           