# Prototype Rekognisi Wajah ![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")

---

### Rincian Repo

> Repo ini berisi prototyping metode Pengenalan atau Identifikasi Wajah menggunakan pengembangan algoritam LBPH yang tersedia pada pustaka OpenCV. Program dikembangkan dengan bahasa pemrograman Python dengan beberapa pustaka pendukung.

### Pustaka Pendukung

```pyt
cv2
argparse
numpy
os
sys
PIL
sqlite3
time
```

---

### Riwayat Percobaan

#### 1 Realtime Test Sequential

| Jumlah Wajah |      Metode      | Keberhasilan |
| :----------: | :--------------: | :----------: |
|      1       | Realtime + Local |    100 %     |
|      2       | Realtime + Local |    100 %     |
|      3       | Realtime + Local |   90 -99 %   |
|      4       | Realtime + Local |     81 %     |
|      5       |     Realtime     |     76 %     |

#### 2 Interval Test

| Interval Time | Kondisi FPS |
| :-----------: | :---------: |
|    1 detik    |     20+     |
|    2 detik    |    -+ 20    |
|    3 detik    |   15 - 20   |
|    4 detik    |   10 - 15   |
|    5 detik    |    -+ 10    |

---

### Pengujian Tambahan(Belum Dilakukan) :arrow_down_small:

2. Penambahan fitur untuk peningkatan model
3. Peningkatan Uji Algoritma