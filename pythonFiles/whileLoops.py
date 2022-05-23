grades=[]
numGrades=int(input("How many grades do you have? "))

while (len(grades)<numGrades):
    grade=int(input("Please input your grade: "))
    grades.append(grade)

print("Your grades are: ")
i=0
while(i<len(grades)):
    print(grades[i])
    i+=1