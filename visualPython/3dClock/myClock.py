from vpython import *
import numpy as np
import time

clockRadius = 2
clockThickness = clockRadius/10

majorThickLength = clockRadius/7
majorThickWidth = 2*np.pi*clockRadius/400
majorThickThickness = clockThickness

minorThickLength = clockRadius/12 
minorThickWidth = 2*np.pi*clockRadius/700
minorThickThickness = clockThickness

minuteHandLength = clockRadius-majorThickLength
minuteHandThickness = minuteHandLength/40
minuteHandOffset = clockThickness + minuteHandThickness/2

hourHandLength = minuteHandLength*.75
hourHandThickness = minuteHandThickness*1.25
hourHandOffset = clockThickness + hourHandThickness/2 + minuteHandThickness

secondHandOffset = hourHandOffset + hourHandThickness
secondHandLength = minuteHandLength

hourAngle=np.pi/2
minuteAngle=np.pi/2
secondAngle=np.pi/2
secondInc=2*np.pi/60
minInc=secondInc/60
hourInc=minInc/12


minuteHand = arrow(pos=vector(0,0,minuteHandOffset), length = minuteHandLength, shaftwidth=minuteHandThickness, color=color.red)   
hourHand = arrow(pos=vector(0,0,hourHandOffset), length = hourHandLength, shaftwidth=hourHandThickness, color=color.red)               
secondHand = arrow(pos=vector(0,0,secondHandOffset), length = secondHandLength, shaftwidth = minuteHandThickness, color = color.magenta)

for theta in np.linspace(0,2*np.pi,13):
    majorThick = box(size=vector(majorThickLength,majorThickWidth,majorThickThickness),
                     pos=vector((clockRadius-majorThickLength/2)*np.cos(theta),(clockRadius-majorThickLength/2)*np.sin(theta), clockThickness),
                     axis=vector(clockRadius*np.cos(theta), clockRadius*np.sin(theta),0), color=color.black)

for theta in np.linspace(0,2*np.pi,61):
    minorThick = box(size = vector(minorThickLength,minorThickWidth,minorThickThickness),
                     pos = vector((clockRadius-minorThickLength/2)*np.cos(theta), (clockRadius-minorThickLength/2)*np.sin(theta), clockThickness),
                     axis = vector(clockRadius*np.cos(theta), clockRadius*np.sin(theta),0), color=color.black)

clockFace = cylinder(axis=vector(0,0,1), color=vector(0,1,.8), length=clockThickness, radius=clockRadius, opacity=.5)

while True:
    rate(5000)
    hour=time.localtime(time.time())[3]
    minute=time.localtime(time.time())[4]
    second=time.localtime(time.time())[5]

    if hour>12:
        hour-=12
    # hourAngle-=hourInc
    # minuteAngle-=minInc
    # secondAngle-=secondInc

    secondAngle=-(second/60)*2*pi+pi/2
    minuteAngle=-((minute+second/60)/60)*2*pi+pi/2
    hourAngle=-((hour+minute/60)/12)*2*pi+pi/2
    
    print(second)
    
    hourHand.axis = vector(hourHandLength*cos(hourAngle),hourHandLength*sin(hourAngle),0)
    minuteHand.axis = vector(minuteHandLength*cos(minuteAngle),minuteHandLength*sin(minuteAngle),0)
    secondHand.axis = vector(secondHandLength*cos(secondAngle),secondHandLength*sin(secondAngle),0)