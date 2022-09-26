import pickle
fruits=['apple', 'orange', 'banana']
x=7
y=10
nuts=['pecans','almond']
grades=[60,70,90]
dataSet=[fruits,x,y,nuts,grades]

# creates file and save data to the file
with open('myData.pkl','wb') as f:
    pickle.dump(dataSet,f)

# opens file and save data to payload 
with open('myData.pkl','rb') as f2:
    payload=pickle.load(f2)

for dt in payload:
    print(dt)    
  