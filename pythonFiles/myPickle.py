import pickle
fruits=['apple', 'orange', 'banana']
x=7
y=10
nuts=['pecans','almond']
grades=[60,70,90]
dataSet=[fruits,x,y,nuts,grades]

with open('myData.pkl','wb') as f:
    pickle.dump(dataSet,f)

with open('myData.pkl','rb') as f2:
    payload=pickle.load(f2)

for dt in payload:
    print(dt)    
  