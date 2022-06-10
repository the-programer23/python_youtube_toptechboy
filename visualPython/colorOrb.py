from numpy import greater_equal
from vpython import *
myOrb=sphere(radius=1)

redChannel=0
greenChannel=0
blueChannel=0

rInc=.001
gInc=.002
bInc=.0015

while True:
    rate(100)
    redChannel += rInc
    greenChannel += gInc
    blueChannel += bInc
    print(redChannel,greenChannel,blueChannel)
    
    myOrb.color = vector(redChannel,greenChannel,blueChannel)

    if redChannel >= 1 or redChannel <= 0:
        rInc *= -1
    if greenChannel >=1 or greenChannel <= 0:
        gInc *= -1    
    if blueChannel >=1 or blueChannel <= 0:
        bInc *= -1    