from vpython import *
import numpy as np
arrowLength = 2
arrowThickness = .02
pointerThickness = .04
ballRadius = .05

xArrow = arrow(axis=vector(1,0,0), color=color.red, length=arrowLength, shaftwidth= arrowThickness)
yArrow = arrow(axis=vector(0,1,0), color=color.green, length=arrowLength, shaftwidth= arrowThickness)
zArrow = arrow(axis=vector(0,0,1), color=color.blue, length=arrowLength, shaftwidth= arrowThickness)
pArrow = arrow(axis=vector(1,0,0), color=color.orange, length=arrowLength, shaftwidth= pointerThickness)
myBall = sphere(make_trail=True, trail_color=color.cyan, pos=vector(arrowLength,0,0), color=color.orange, radius=ballRadius)

while True: 
    for myAngle in np.linspace(0,2*np.pi,1000):
        rate(150)
        pArrow.axis = vector(arrowLength*np.cos(myAngle),arrowLength*np.sin(myAngle),0)
        pArrow.length = arrowLength
        myBall.pos = vector(arrowLength*np.cos(myAngle),arrowLength*np.sin(myAngle),0)
    for myAngle in np.linspace(0,5*np.pi/2,1000):
        rate(150)
        pArrow.axis = vector(arrowLength*np.cos(myAngle),0,arrowLength*np.sin(myAngle))    
        pArrow.length = arrowLength
        myBall.pos = vector(arrowLength*np.cos(myAngle),0,arrowLength*np.sin(myAngle))
    for myAngle in np.linspace(0,2*np.pi,1000):
        rate(150)
        pArrow.axis = vector(0,arrowLength*np.sin(myAngle),arrowLength*np.cos(myAngle))
        pArrow.length = arrowLength   
        myBall.pos = vector(0,arrowLength*np.sin(myAngle),arrowLength*np.cos(myAngle))
    for myAngle in np.linspace(np.pi/2,2*np.pi,1000):
        rate(100)
        pArrow.axis = vector(arrowLength*np.cos(myAngle),0,arrowLength*np.sin(myAngle))
        pArrow.length = arrowLength    
        myBall.pos = vector(arrowLength*np.cos(myAngle),0,arrowLength*np.sin(myAngle))
 