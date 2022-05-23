from vpython import *
import numpy as np


glassBulb1 = sphere(radius = 1.25, color = color.white, opacity = .3)
mercurySphere1 = sphere(radius = 1, color = color.red)

cylinder1 = cylinder(radius = .5, length = 6, color = color.white, opacity = .3, axis = vector(0, 4, 0))
mercuryColumn1 = cylinder(radius = .45, length = 6, color = color.red, axis = vector(0, 4, 0))

for tick in np.linspace(1,6,25):
    print(tick)
    box(size=vector(.5,.1,.1), pos=vector(0,tick,.5), color = color.white)

while True:
    for myTemp in np.linspace(1,6,100):
        rate(20)
        mercuryColumn1.length = myTemp
    for myTemp in np.linspace(6,1,100):
        rate(20)
        mercuryColumn1.length = myTemp



