# -*- coding: utf-8 -*-

import face_recognition
import pickle
import os
import cv2
import numpy as np


testPath = "./faceTest/"
dataPath = "./FaceDataSet.txt"

data = open(dataPath,'rb')
dict = pickle.load(data)
data.close()

studentsName = list(dict.keys())
studentsFace = list(dict.values())

attend=[]
absent = studentsName
img=[]

l = os.listdir(testPath) #列出文件夹下所有的目录与文件
for i in range(0,len(l)):

    #for root, dirs, files in os.walk(testPath):
    
    #for name in files:
      path = os.path.join(testPath,l[i])
      image = face_recognition.load_image_file(path)
      image_new = image[:, :, ::-1]
      face_locations = face_recognition.face_locations(image_new)
      face_locations2 = face_recognition.face_locations(image)
      face_encodings = face_recognition.face_encodings(image_new,face_locations)


      imgNew = cv2.imread(path)
      faceNum = len(face_locations2)
      for i in range(0, faceNum):
          top =  face_locations2[i][0]
          right =  face_locations2[i][1]
          bottom = face_locations2[i][2]
          left = face_locations2[i][3]
            
          start = (left, top)
          end = (right, bottom)
            
          color = (55,255,155)
          thickness = 3
          cv2.rectangle(imgNew, start, end, color, thickness)
      cols = 300
      rows = 300
      imgNew2 = cv2.resize(imgNew,(cols,rows),interpolation=cv2.INTER_CUBIC) #缩放图像
      img.append(imgNew2)


      i=0
      for face_encoding in studentsFace:
          matches = face_recognition.compare_faces(face_encoding, face_encodings,0.5)
          if True in matches:
            j = studentsName[i]
            p=0
            if(j in attend):
                p=1
            else:
                attend.append(j)
          i=i+1

print("attend:\n")
for i in attend:
    print(i+"\n")

print("absent:\n")
for j in absent:
    if (j in attend):
        continue
    print(j+"\n")
    
htitch= np.hstack(img)

cv2.imshow("faces",htitch)
cv2.waitKey(0)
cv2.destroyAllWindows() 
