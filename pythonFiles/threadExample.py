from time import *
from threading import Thread 

def myBox(delayT):
    while True:
        print('---The box is opened')
        sleep(delayT)
        print("---The box is closed")
        sleep(delayT)
def myLED(delayT):
    while True:
        print('The LED is ON')
        sleep(delayT)
        print("The LED is OFF")
        sleep(delayT) 

myBoxThread=Thread(target=myBox, args=(5))
myLEDThread=Thread(target=myLED, args=(1))

# #with the line of code below we can stop the program after pression ctrl+c
myBoxThread.daemon=True
myLEDThread.daemon=True

myBoxThread.start()
myLEDThread.start()

count=0

while True:
    count+=1
    print(count)
    sleep(.1)
    # pass



