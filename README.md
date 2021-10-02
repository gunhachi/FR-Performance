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

### Hasil Percobaan

#### 1 Realtime Test Sequential

Tahap ini menguji keberhasilan rekognisi wajah secara bertahap dari 1 - 5 wajah dalam bersamaan dalam satu frame. Data pengujian dapat diakses melalui local file ataupun webcam dengan resolusi VGA berkisar 640x480 piksel.

| Jumlah Wajah |      Metode      | Keberhasilan |
| :----------: | :--------------: | :----------: |
|      1       | Realtime + Local |    100 %     |
|      2       | Realtime + Local |    100 %     |
|      3       | Realtime + Local |   90 -99 %   |
|      4       | Realtime + Local |     81 %     |
|      5       |     Realtime     |     56 %     |

#### 2 Interval Test

Pengujian dengan jeda waktu ditujukan untuk mengetahui performa fungsi rekognisi wajah ketika berjalan secara realtime dengan acuan angka frame per second (FPS). Uji dilakukan pada fungsi rekognisi untuk 10 frame pertama yang berhasil direkognisi.

| Interval Time | Rerata FPS 10 Frame |
| :-----------: | :-----------------: |
|    1 detik    |        3.58         |
|    2 detik    |        2.68         |
|    3 detik    |        2.08         |
|    4 detik    |        1.74         |
|    5 detik    |        1.46         |

---

## Flow Program

![](/asset/FCProg.png)

## Cara Menggunakan

```
ditunggu saja lah ya
```

### Addition changing to modular