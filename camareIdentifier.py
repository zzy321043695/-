# -*- coding: utf-8 -*-

import cv2
import face_recognition
import pickle

path = "./face"

data = open("./FaceDataSet.txt",'rb')
dict = pickle.load(data)
data.close()

studentsName = list(dict.keys())
studentsFace = list(dict.values())

cap = cv2.VideoCapture(0)
total_image_name = studentsName
total_face_encoding = studentsFace

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    ret, frame = cap.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]
    if process_this_frame:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(total_face_encoding, face_encoding,0.5)
            name = "Unknown"
            # If a match was found in known_face_encodings, just use the first one.
            first_match_index = matches.index(True)
            name = total_image_name[first_match_index]
            face_names.append(name)
    process_this_frame = not process_this_frame
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255),
                      cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0,
                    (255, 255, 255), 1)
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()