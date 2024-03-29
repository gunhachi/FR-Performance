
#Membuat file YML training pada folder training dan melakukan proses training data yang sudah masuk

import os
import cv2
import numpy as np 
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()
path = 'dataset'

if not os.path.exists('./model'):
    os.makedirs('./model')
 
def getImagesWithID(path):
  imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
  faces = []
  IDs = []
  for imagePath in imagePaths:
    faceImg = Image.open(imagePath).convert('L')
    faceNp = np.array(faceImg,'uint8')
    ID = int(os.path.split(imagePath)[-1].split('.')[1])
    faces.append(faceNp)
    IDs.append(ID)
    cv2.imshow("Latih",faceNp)
    cv2.waitKey(10)
  return np.array(IDs), faces
Ids, faces = getImagesWithID(path)
recognizer.train(faces,Ids)
recognizer.save('model/trainingData.yml')
print("\n [INFO] Training selesai")
cv2.destroyAllWindows()

