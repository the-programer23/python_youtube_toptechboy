import cv2
import face_recognition as FR
font = cv2.FONT_HERSHEY_SIMPLEX

donaldFace=FR.load_image_file('C:/Users/nfabi/Documents/projects/python/topTechBoy/AI/openCV/demoImages/known/Donald Trump.jpg')
# faceLocation=FR.face_locations(donaldFace)[0]
donaldFaceEncode=FR.face_encodings(donaldFace)[0]

nancyFace=FR.load_image_file('C:/Users/nfabi/Documents/projects/python/topTechBoy/AI/openCV/demoImages/known/Nancy Pelosi.jpg')
# faceLocation=FR.face_locations(nancyFace)[0]
nancyFaceEncode=FR.face_encodings(nancyFace)[0]

penceFace=FR.load_image_file('C:/Users/nfabi/Documents/projects/python/topTechBoy/AI/openCV/demoImages/known/Mike Pence.jpg')
# faceLocation=FR.face_locations(penceFace)[0]
penceFaceEncode=FR.face_encodings(penceFace)[0]

fabianFace=FR.load_image_file('C:/Users/nfabi/Documents/projects/python/topTechBoy/AI/openCV/demoImages/known/Fabian Pinzon.png')
fabianFaceEncode=FR.face_encodings(fabianFace)[0]

knownEncodings=[donaldFaceEncode,nancyFaceEncode,penceFaceEncode,fabianFaceEncode]
names=['Donald Trump', 'Nancy Pelosi','Mike Pence','Fabian Pinzon']

unknownFace=FR.load_image_file('C:/Users/nfabi/Documents/projects/python/topTechBoy/AI/openCV/demoImages/unknown/u14.jpg')
unknownFaceBGR=cv2.cvtColor(unknownFace,cv2.COLOR_RGB2BGR)
faceLocations=FR.face_locations(unknownFace)
print(faceLocations)
unknownEncodings=FR.face_encodings(unknownFace,faceLocations)

for faceLocation,unknownEncoding in zip(faceLocations,unknownEncodings):
    top,right,bottom,left=faceLocation
    print(faceLocation)
    cv2.rectangle(unknownFaceBGR,(left,top),(right,bottom),(255,0,0),3)
    name='Unknown Person'
    matches=FR.compare_faces(knownEncodings,unknownEncoding)
    print(matches)
    if True in matches:
        matchIndex=matches.index(True)
        name=names[matchIndex]
        print(matchIndex)
        print(names[matchIndex])
    cv2.putText(unknownFaceBGR,name,(left,top),font,.75,(0,0,255),2)    


imgHeight,imgWidth=unknownFaceBGR.shape[:2]
cv2.namedWindow('my window',cv2.WINDOW_NORMAL)
cv2.resizeWindow('my window',int(imgWidth/1.6),int(imgHeight/1.6))
cv2.moveWindow('my window',0,0)

while(True):
    cv2.imshow('my window',unknownFaceBGR)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        #closes the window
        cv2.waitKey(5000)
        break