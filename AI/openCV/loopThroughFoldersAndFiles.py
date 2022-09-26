import os
import cv2
import face_recognition as FR

imageDir='C:/Users/nfabi/Documents/projects/python/topTechBoy/AI/openCV/demoImages/known'

for root,dirs,files in os.walk(imageDir):
    print('root: ', root)
    print('dirs: ', dirs)
    print('files: ', files)
    for file in files:
        print('name: ', file)
        # fullPathName=os.path.join(root,file)
        fullPathName=root+'/'+file
        print(fullPathName)
        name=os.path.splitext(file)[0]
        print(name)
        myPic=FR.load_image_file(fullPathName)
        myPic=cv2.cvtColor(myPic,cv2.COLOR_RGB2BGR)
        cv2.imshow(name,myPic)
        cv2.moveWindow(name,0,0)
        cv2.waitKey(2500)
        cv2.destroyAllWindows()