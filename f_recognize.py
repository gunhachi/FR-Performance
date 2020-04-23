import cv2
import numpy as np 
import sqlite3
import os
import time
import argparse

conn = sqlite3.connect('datawajah.db')
c = conn.cursor()

fname = "model/trainingData.yml"

if not os.path.isfile(fname):
  print("Model training salah")
  exit(0)
  
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Buat fungsi argument disini

ap = argparse.ArgumentParser()
ap.add_argument("-l","--location", help="Lokasi File")
ap.add_argument("-f","--frame",type=int, help="Jumlah Frame yang ingin dideteksi")
ap.add_argument("-t","--time",type=int, help="Waktu Jeda Rekognisi")
args = ap.parse_args()


tdl = args.time
nfr = args.frame

start_time = time.time()
cap = cv2.VideoCapture(args.location or 0)

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read(fname)

count = 0 #inisiasi counter

while True:
  _,img = cap.read()
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  
  #penambahan Equalization dan filter Median Blur
  # equ = cv2.equalizeHist(gray)
  # medblu = cv2.medianBlur(equ,3)
  
  faces = face_cascade.detectMultiScale(gray, 1.2, 5)

  #sesuai sumbu kartesius -->top left corner(x,y) 
  #right (x+w) dan bottom (y+h)
  #dari titik deteksi wajah


  if time.time() - start_time >= tdl :
    for (x,y,w,h) in faces: 
      
      count = count+1

      ids,conf = recognizer.predict(gray[y:y+h,x:x+w])
      c.execute("select name from users where id = (?);", (ids,))
      result = c.fetchall()
      name = result[0][0]

      if conf < 50:
        conf = "  {0}%".format(round(100 - conf)) 

        #Condition untuk timer disini
        # if time.time() - start_time >= 5:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),1)    
        cv2.rectangle(img, (x,y-30),(x+w,y), (0, 255, 0), cv2.FILLED)
        cv2.rectangle(img, (x,y+h+18),(x+w-80,y+h), (255, 0, 0), cv2.FILLED)
        cv2.putText(img, name, (x+5,y-5), cv2.FONT_HERSHEY_DUPLEX, 1, (255,255,255),2)
        cv2.putText(img,str(conf),(x,y+h+15),cv2.FONT_HERSHEY_PLAIN,1,(255,255,255),2)
          
#     k = cv2.waitKey(30) & 0xff
#     if k == 32 :
    if count >= nfr :
      count = 0
      start_time = time.time()

    # else:
    #   cv2.putText(img, 'Tidak Cocok', (x+2,y+h-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2)
    
  cv2.imshow('Rekognisi Wajah',img)

    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #       break

  k = cv2.waitKey(30) & 0xff
  if k == 27: # keyboard id 27 = ESC cari di keyboard id js
    break

print("\n [INFO] Keluar Program")
cap.release()
cv2.destroyAllWindows()
