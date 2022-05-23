from vpython import *
# import numpy as np
import numpy

# Piston1=cylinder(radius=1, length=3, color=color.red, opacity=.5)
mySphere=sphere(radius=1, color=color.red, opacity=.5)
while True:
    # for myLength in np.linspace(1,6,1000):
    #     rate(250)
    #     Piston1.length = myLength
    # for myLength in np.linspace(6,1,1000):
    #     rate(250)
    #     Piston1.length = myLength

    # for myOpacity in numpy.linspace(1,0,1000):
    #     rate(250)
    #     Piston1.opacity = myOpacity
    # for myOpacity in numpy.linspace(0,1,1000):
    #     rate(250)
    #     Piston1.opacity = myOpacity

    for myRadius in numpy.linspace(.1,1,1000):
        rate(250)
        mySphere.radius = myRadius
    for myRadius in numpy.linspace(1,.1,1000):
        rate(250)
        mySphere.radius = myRadius     