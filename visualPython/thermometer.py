from vpython import *
import numpy as np


glassBulb = sphere(radius = 1.25, opacity = .3)
cylinderGlass = cylinder(radius = .5, length = 6, opacity = .3, axis = vector(0, 4, 0))

mercurySphere = sphere(radius = 1, color = color.red, opacity=.5)
mercuryColumn = cylinder(radius = .45, length = 6, color = color.red, axis = vector(0, 4, 0))

for tick in np.linspace(1,6,15):
    box(size=vector(.5,.05,.1), pos=vector(0,tick,.5))

while True:
    for myTemp in np.linspace(1,6,100):
        rate(20)
        mercuryColumn.length = myTemp
    for myTemp in np.linspace(6,1,100):
        rate(20)
        mercuryColumn.length = myTemp



