
from vpython import *

# ball=sphere(color=color.green)
# sleep(5)
# ball.color=color.blue
# sleep(5)
# ball.color=color.red

# myBox=box(color=color.yellow)

# myRuler=box(color=color.cyan,length=12,width=1,height=.2)
# myTube=cylinder(color=color.cyan,length=6,radius=1)
# myElipseStick=cylinder(color=color.red,length=12,width=1,height=.5)
# pos=vector(x,y,z)
#size(x,y,z)
mRadius=.5
wallThickness=.1
roomWidth=12
roomDepth=20
roomHeight=2
floor=box(pos=vector(0,-roomHeight/2,0),size=vector(roomWidth,wallThickness,roomDepth),color=color.white, opacity=.5)
ceiling=box(pos=vector(0,roomHeight/2,0),size=vector(roomWidth,wallThickness,roomDepth),color=color.white, opacity=.5)
backWall=box(pos=vector(0,0,-roomDepth/2),size=vector(roomWidth,roomHeight,wallThickness),color=color.white, opacity=.5)
leftWall=box(pos=vector(-roomWidth/2,0,0),size=vector(wallThickness,roomHeight,roomDepth),color=color.white, opacity=.5)
rightWall=box(pos=vector(roomWidth/2,0,0),size=vector(wallThickness,roomHeight,roomDepth),color=color.white, opacity=.5)
ball=sphere(radius=mRadius,color=color.green)
deltaX=0.1
deltaY=0.1
deltaZ=0.1

xPos=0
yPos=0
zPos=0

while True:
    rate(80)

    xPos += deltaX
    yPos += deltaY
    zPos -= deltaZ

    Xrme = xPos + mRadius #this keeps track of the position of the xRightMarbleEdge
    Xlme = xPos - mRadius
    Ytme = yPos + mRadius #YTopMarbleEdge
    Ybme = yPos - mRadius
    Zbme = zPos - mRadius
    Zfme = zPos + mRadius
   
    Rwe = roomWidth/2-wallThickness/2 #rightWallEdge
    Lwe = -roomWidth/2+wallThickness/2 #LeftWallEdge
    Cwe = roomHeight/2 - wallThickness/2 #Ceiling wall edge 
    Fwe = -roomHeight/2 + wallThickness/2  #FloorWallEdge
    Bwe = -roomDepth/2 #BackWallEdge
    Frwe = roomDepth/2 #FrontWallEdge

    if Xrme >= Rwe or Xlme <= Lwe:
        deltaX*=-1
    if Ytme >= Cwe or Ybme <= Fwe:
        deltaY*=-1

    if Zbme <= Bwe or Zfme >= Frwe:
        deltaZ*=-1       
   
    ball.pos=vector(xPos,yPos,zPos)      
    # pass