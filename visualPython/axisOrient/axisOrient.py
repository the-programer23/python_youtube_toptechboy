from vpython import *
import numpy as np
arrowLength = 1.6
arrowThickness = .02
#theta=np.pi/4 # theta = angle - np.pi/4 is = to 45°
#theta= 65/360 * 2 * np.pi #65°
theta=0
print(theta)
#z is 1 or -1, 1 points towards us while -1 points towards the opposite direction
Xarrow = arrow(axis=vector(1,0,0), color=color.red, length = arrowLength, shaftwidth = arrowThickness)
Yarrow = arrow(axis=vector(0,1,0), color=color.green, length=arrowLength, shaftwidth = arrowThickness)
Zarrow = arrow(axis=vector(0,0,1), color=color.blue, length=arrowLength, shaftwidth= arrowThickness)
pointerArrow = arrow(axis=vector(arrowLength*np.cos(theta),arrowLength*np.sin(theta),0), color=color.orange, length=arrowLength, shaftwidth = arrowThickness)
while True:
    for myAngle in np.linspace(0,2*np.pi,1000):
        rate(50)
        pointerArrow.axis = vector(arrowLength*np.cos(myAngle),arrowLength*np.sin(myAngle),0)
        pointerArrow.length = arrowLength
    for myAngle in np.linspace(0,2*np.pi,1000):
        rate(50)
        pointerArrow.axis = vector(0,0,)  