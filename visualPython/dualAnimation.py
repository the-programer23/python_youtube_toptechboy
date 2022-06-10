from vpython import *
myCylOrange=cylinder(radius=1,color=color.orange,length=6)
myCylCyan=cylinder(radius=1,color=color.cyan,length=6,pos=vector(0,3,0))

myCylOrangeLength = 1
myCylCyanLength = 1

myCylOrangeDelta = .01
myCylCyanDelta = .02

while True:
    rate(80)
    myCylOrangeLength += myCylOrangeDelta 
    myCylCyanLength += myCylCyanDelta

    myCylOrange.length = myCylOrangeLength
    myCylCyan.length = myCylCyanLength

    if myCylOrangeLength >= 6 or myCylOrangeLength <= .1:
        myCylOrangeDelta *= -1 
    if myCylCyanLength >= 6 or myCylCyanLength <= .1:
        myCylCyanDelta *= -1
