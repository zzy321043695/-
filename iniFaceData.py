# -*- coding: utf-8 -*-

import face_recognition
import pickle
import os

facePath = "./face/"
dataPath = "./FaceDataSet.txt"

for root, dirs, files in os.walk(facePath):
  
      for name in files:
          ID = name
          ID = ID[:(len(ID) - 4)]
          image = face_recognition.load_image_file(facePath + name)
          image_new = image[:, :, ::-1]
        
          face_encoding = face_recognition.face_encodings(image_new)[0]
        
          sizeOfFaceset = os.path.getsize(dataPath)
          if sizeOfFaceset == 0:
              dict={ID:face_encoding}
          else:
              data = open(dataPath,'rb')
              dict = pickle.load(data)
              data.close()
              dict[ID]=face_encoding
        
          data = open(dataPath,'wb')
          pickle.dump(dict,data)
          data.close()