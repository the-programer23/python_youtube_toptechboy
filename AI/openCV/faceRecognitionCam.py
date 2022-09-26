import os
import cv2
import face_recognition as FR
import pickle

font=cv2.FONT_HERSHEY_SIMPLEX

imageDir='C:/Users/nfabi/Documents/projects/python/topTechBoy/AI/openCV/demoImages/known'
facesFilePath='C:/Users/nfabi/Documents/projects/python/topTechBoy/faces.pkl'
knownEncodings=[]
names=[]

if os.path.exists(facesFilePath):
    with open('faces.pkl','rb') as f2:
        data=pickle.load(f2)
        knownEncodings=data[0]
        names=data[1]
else:
    for root,dirs,files in os.walk(imageDir):
        for file in files:
            fullPathName=root+'/'+file
            name=os.path.splitext(file)[0]
            face=FR.load_image_file(fullPathName)
            faceEncode=FR.face_encodings(face)[0]
            knownEncodings.append(faceEncode)
            names.append(name)
    dataSet=[knownEncodings,names]
    #create file and save dataSet to it
    with open('faces.pkl','wb') as f:
        pickle.dump(dataSet,f) 

#Camera Setup ***********
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
# cv2.namedWindow("my window", cv2.WND_PROP_FULLSCREEN)
# cv2.setWindowProperty("my window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

faceCascade=cv2.CascadeClassifier('haar\haarcascade_frontalface_default.xml')

while(True):
    ignore,frame=cam.read()

    # frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    faceLocations=FR.face_locations(frame) #find all faces in frameRGB

    unknownEncodings=FR.face_encodings(frame,faceLocations)
    # print(unknownEncodings)

    for faceLocation,unknownEncoding in zip(faceLocations,unknownEncodings):
        top,right,bottom,left=faceLocation
        cv2.rectangle(frame,(left,top),(right,bottom),(255,0,0),3)
        name='Desconocido'
        matches=FR.compare_faces(knownEncodings,unknownEncoding)
        if True in matches:
            matchIndex=matches.index(True)
            name=names[matchIndex]
        cv2.putText(frame,name,(left,top),font,.85,(0,0,255),2)    
    cv2.imshow('my window',frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()   
cv2.destroyAllWindows() 