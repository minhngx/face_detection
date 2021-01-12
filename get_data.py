import cv2
import numpy as np
import sqlite3
import os

def InsertOrUpdate(id, name):
    conn = sqlite3.connect(r'C:\Users\vanminh1\OneDrive - Intel Corporation\Desktop\NDKM\data.db')
    query = 'SELECT * FROM people WHERE ID=' + str(id)
    cusror = conn.execute(query)

    IsRecordExist = 0

    for row in cusror:
        IsRecordExist = 1
    if(IsRecordExist == 0):
        query = "INSERT INTO people(ID, Name) VALUES(" + str(id) + ",'" + str(name) + "')"
    else:
        query = "UPDATE people SET Name='"+ str(name) + "' WHERE ID=" + str(id)

    conn.execute(query)
    conn.commit()
    conn.close()
    
#load tv
face_cascade = cv2.CascadeClassifier(r'C:\Users\vanminh1\OneDrive - Intel Corporation\Desktop\Cody\Minhne\Python Tutorial\OpenCV\haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

#insert to db
id = input("Enter your ID:")
name = input("Enter your Name:")
InsertOrUpdate(id, name)

sampleNum = 0

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h) , (0, 255, 0), 2)
        if not os.path.exists(r'C:\Users\vanminh1\OneDrive - Intel Corporation\Desktop\NDKM\dataSet'):
            os.makedirs(r'C:\Users\vanminh1\OneDrive - Intel Corporation\Desktop\NDKM\dataSet')
    
        sampleNum += 1

        cv2.imwrite(r'C:\Users\vanminh1\OneDrive - Intel Corporation\Desktop\NDKM\dataSet\User.' + str(id) +'.' + str(sampleNum) + '.jpg', gray[y: y + h, x: x + w])

    cv2.imshow('frame', frame)
    cv2.waitKey(1)

    if sampleNum > 99:
        break

cap.release()
cv2.destroyAllWindows()

        

