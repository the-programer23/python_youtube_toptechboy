class Students:
    def __init__(self,first,last):
        self.first=first
        self.last=last
    def gradesInput(self,numGrades):
        self.numGrades=numGrades
        self.grades=[]
        for i in range(0,numGrades,1):
            grade=float(input("Please enter student's grade: "))
            self.grades.append(grade)
        return self.grades
    def printGrades(self):
        print(self.first+"'s grades are:")
        for i in range(0,self.numGrades):
            print(self.grades[i])
        print("")
    def avgGrades(self):
        bucket=0
        for i in range(0,self.numGrades,1):
            bucket+=self.grades[i]
        print(self.first+"'s average grade is",bucket/self.numGrades)
    def highLow(self):
        highG=max(self.grades)
        lowG=min(self.grades)
        return highG, lowG                       

student1=Students('Joe','Rogan')
student2=Students('Shirly','Baker')
print(student1.first,student1.last)
print(student2.first,student2.last)
print(student1.gradesInput(3))
student1.printGrades()
student1.avgGrades()
highG,lowG=student1.highLow()
print(student1.first+"'s highest grade is",highG)
print(student1.last+"'s lowest grade is",lowG)