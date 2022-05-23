def tally(myArray):
    tot=0
    for i in range(0,len(myArray),1):
        tot+=myArray[i]
    return tot

x=[2,5,10,20]
mySum=tally(x)
print(mySum)