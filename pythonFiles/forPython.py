# fruits=['apple', 'orange', 'mango', 'pear']
# print(fruits[1:3])

# for fruit in fruits:
#     print(fruit)
#     for char in fruit:
#         print(char)

# for num in range(1,11,1):
#     print(num)

# print all even numbers between 10 and 20

# for num in range(10,21,2):
#     print(num)

# print from 10 to 0 one step at a time

# for num in range(10,-1,-1):
#     print(num)

# Read 5 grades from the user

grades=[] 
bucket=0

for num in range(1,4,1):
    grade = float(input('Please enter your grade number ' + str(num) + ': '))
    grades.append(grade)

for i in range(0, len(grades), 1):
    bucket+=grades[i]

avg=bucket/len(grades)

print("avg =",avg)
print("Your high grade was ",max(grades))
print("Your low grade was ",min(grades))
print("Your grades in descending order are: ")

#short way

# for grade in sorted(grades,reverse=True):
#     print(grade)

#long way
#[80,70,60]
                    #2
for i in range(0,len(grades)-1,1):#1
                        #2
    for i in range(0,len(grades)-1,1):#1
            #70<60
        if grades[i]<grades[i+1]:
            swp=grades[i]#70
            grades[i]=grades[i+1] 
            grades[i+1]=swp
for i in range(0,len(grades),1):
    print(grades[i])
