# -*- coding: utf-8 -*-

import cv2

testPath = "./faceTest/"

camera=cv2.VideoCapture(0)
i =0
while(10):
    ret,frame = camera.read()
    wait = cv2.waitKey(100)
    if(wait ==27):       #按下esc退出
        break
    elif (wait ==32):    #按下空格拍照
        cv2.imwrite(testPath + str(i) +'.jpg',frame) 
        i=i+1
    cv2.imshow("capture",frame)

camera.release()
cv2.destroyAllWindows()