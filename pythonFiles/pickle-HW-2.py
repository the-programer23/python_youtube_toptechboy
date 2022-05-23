import pickle;

with open('studentData.pkl','rb') as SData:
    names=pickle.load(SData)
    grades=pickle.load(SData)
    numStudents=pickle.load(SData)
while (1==1):
    name=input('Which student do you want to check? ')
    for i in range(0,numStudents,1):
        if (name==names[i]):
            print(str(name)+"'s grade is "+str(grades[i]))
        