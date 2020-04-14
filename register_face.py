
import cv2
import sqlite3
import numpy as np
import os
import argparse

# connect database
conn = sqlite3.connect('datawajah.db')
c = conn.cursor()

if not os.path.exists('./dataset'):
    os.makedirs('./dataset')

# load cascade classifier file
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

ap = argparse.ArgumentParser()
ap.add_argument("-l","--location", help="Lokasi File")
args = ap.parse_args()

cap = cv2.VideoCapture(args.location or 0)

u_name = input("Masukkan nama pengguna : ")
c.execute('INSERT INTO users (name) VALUES (?)', (u_name,))
uid = c.lastrowid
sampleNum = 0

# -------------------------------------------------------------------------------------------------------------
# Dipake untuk bikin folder berdasarkan nama - but skip cause train function directly from image not dir hehe
# dirname = "dataset/"+str(u_name)
# os.mkdir(dirname)
# os.chdir(dirname)
# -------------------------------------------------------------------------------------------------------------


while True:
  _,img = cap.read()
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  equ = cv2.equalizeHist(gray)
  medblu = cv2.medianBlur(equ,3)

  faces = face_cascade.detectMultiScale(medblu, 1.3, 5)

  for (x,y,w,h) in faces:

    sampleNum = sampleNum+1
    cv2.imwrite("dataset/User."+str(uid)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
    # -----------------------------------------------------------------------------------
    # Kalo yang ini polosan ketika udah akuisisi per directory hehe
    # cv2.imwrite("User."+str(uid)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
    # -----------------------------------------------------------------------------------
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
    cv2.waitKey(100)
  cv2.imshow('img',img)
  cv2.waitKey(1);
  if sampleNum > 60: #Dibuat agak banyak biar ada variasi jarak akuisisi
    break

print("\n [INFO] Program Selesai")
cap.release()
conn.commit()
conn.close()
cv2.destroyAllWindows()
