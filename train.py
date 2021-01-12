import cv2
import numpy as np
import os
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()
path = r'C:\Users\vanminh1\OneDrive - Intel Corporation\Desktop\NDKM\dataSet'
def getImageWithId(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)] #truy cập vào các file trong dataSet >> có được đường dẫn trong thu mục dataSet
    #print(imagePaths)

    faces = []
    IDs = []

    for imagePath in imagePaths:
        faceImg = Image.open(imagePath).convert('L')
        faceNp = np.array(faceImg, 'uint8')
        print(faceNp)
        Id = int(imagePath.split('\\')[7].split('.')[1])
        faces.append(faceNp)
        IDs.append(Id)
        cv2.imshow('Training', faceNp)
        cv2.waitKey(10)
    return faces, IDs

faces, IDs = getImageWithId(path)
recognizer.train(faces, np.array(IDs))

if not os.path.exists(r'C:\Users\vanminh1\OneDrive - Intel Corporation\Desktop\NDKM\reconizer'):
    os.makedirs(r'C:\Users\vanminh1\OneDrive - Intel Corporation\Desktop\NDKM\reconizer')

recognizer.save(r'C:\Users\vanminh1\OneDrive - Intel Corporation\Desktop\NDKM\reconizer\trainingData.yml')
cv2.destroyAllWindows()