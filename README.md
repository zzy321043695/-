# 课堂点名
一、项目名称：自动点名

二、设计需求

	实现课堂人脸点名功能。
	
三、实现环境

	anaconda 3
	
	python 3.6
	
	import face_recognition
	
	import cv2
	
	import pickle
	
四、设计方案

	1 整体说明
	
		1.1 项目路径下的文件夹face里存储所有的学生的人脸照片。以学号命名。
		
		1.2 项目路径下的文件夹faceTest里存放上课时学生出勤的照片。可以放置多张照片。多张照片里的学生可重复。
		
		1.3项目路径下的FaceDataSet.txt文件里存储所有学生的人脸数据。初始时为空。
		
	2 细节说明
	
		2.1 iniFaceData.py
		
			初始化人脸数据。调用face_recognition模块将face文件夹下的照片转化成人脸数据存入FaceDataSet.txt里面。
			
		2.2 recognize.py
		
			识别人脸。调用face_recognition模块将faceTest文件夹下的学生出勤照片识别成人脸数据并和faceDataset.txt里的数据进行对比。记录匹配成功的人脸对应的学生的学号并存入数组attend[]里面。同时将出勤照片里的所有的能识别出来的人脸用方框框出来并在窗口faces里显示。
			
		2.3 takePhotos.py
		
			调用摄像头对学生进行拍照。按空格键拍照，照片最终被存入faceTest文件夹下。按esc键退出。
			
		2.4 camareIdentifier.py
		
			调用摄像头将识别出来的人脸数据和faceDatSet.txt里的人脸数据进行匹配。并将视频里的人脸和匹配的学生学号标注出来在窗口video显示。
			
		2.5 faceDataSet.txt
		
			存放iniFaceData.py运行后生成的人脸数据。
			
	3 如何使用
	
		3.1 初始化人脸数据
		
			开始前确保faceDatSet.txt里数据为空；face文件夹里存放了所有人的人脸照片。然后运行iniFaceData.py程序将所有人的人脸数写入faceDatSet.txt。如果需要增加、更新、删除学生的人脸照片，那么需要先清空faceDatSet.txt里的所有数据，然后再运行一遍iniFaceData.py。
			
		3.2 离线点名
		
			可以先用手机或者其他拍摄工具对出勤的学生拍照，然后再将照片存入工程目录下的face文件夹。或者直接运行takePhotos.py对学生进行拍照。照片可以拍很多张。最后再运行recognize.py。程序会输出出勤（attend[]）和缺勤（absent[]）的学生的学号。
			
		3.3 实时点名
		
			运行camareIdentifier.py程序会自动调用摄像头对在场的学生进行识别并在视频上标注出他们的学号。

