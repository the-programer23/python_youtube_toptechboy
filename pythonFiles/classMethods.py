class Rectangle:
    def __init__(self,c,l,w):
        self.color=c
        self.length=l 
        self.width=w
    def area(self):
        return self.length*self.width
    def perimeter(self):
        return 2*self.length+2*self.width 
    def diagonal(self):
        return (self.width**2+self.length**2)**(1/2)       

myRect1=Rectangle('red',6,2)
myRect2=Rectangle('blue',4,2)
print(myRect1.color)
print('myRect1 length is', myRect1.length)
print('myRect1 area is',myRect1.area())
print('myRect2 area is',myRect2.area())
print('myRect1 perimeter is',myRect1.perimeter())
print('The diagonal is myRect1 is',myRect1.diagonal())
print(myRect2.color)