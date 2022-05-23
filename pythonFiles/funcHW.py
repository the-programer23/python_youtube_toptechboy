def inputGrades(ng):
    grades=[]
    for i in range(0,ng,1):
        grade=float(input('Please enter your grade: '))
        grades.append(grade)
    return grades    
def printGrades(ng,grades):
    for i in range(0,ng,1):
        print(grades[i])
def avgGrades(grades):
    sum=0
    for i in range(0,len(grades),1):
        sum += grades[i]
    avg = sum / len(grades)
    return avg 
def highLow(ng, grades):
    highG=0
    lowG=100
    for i in range(0,ng,1):
        if(grades[i]<lowG):
            lowG=grades[i] #10
        if(grades[i]>highG):
            highG=grades[i] #30
    return highG, lowG                       

numGrades=int(input('How many grades? '))
myGrades=inputGrades(numGrades)
printGrades(numGrades,myGrades)
print("")
avg=avgGrades(myGrades)
print("avg of grades is", round(avg,1))
#long way
highG, lowG=highLow(numGrades,myGrades)
print('Your high grade is',highG)
print('Your low grade is',lowG)
#short way
print("")
print("Lowest Grade: ",min(myGrades))
print("Highest Grade: ",max(myGrades))
