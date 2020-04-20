#!/usr/bin/env python

import cv2
import time
import argparse

if __name__ == '__main__' :

    ap = argparse.ArgumentParser()
    ap.add_argument("-l","--location", help="Lokasi File")
    ap.add_argument("-f","--frames", help="Jumlah Frame untuk dianalisa")
    args = ap.parse_args()

    video = cv2.VideoCapture(args.location or 0);
    

    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
    
    if int(major_ver)  < 3 :
        fps = video.get(cv2.cv.CV_CAP_PROP_FPS)
        print ("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
    else :
        fps = video.get(cv2.CAP_PROP_FPS)
        print ("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))
    

    num_frames = int(args.frames) ;
    
    print ("Capturing {0} frames".format(num_frames))

    start = time.time()
    xrange = (0,num_frames)

    for i in xrange :
        ret, frame = video.read()

    end = time.time()

    seconds = end - start
    print ("Time taken : {0} seconds".format(seconds))

    proc_time  = num_frames / seconds
    fps = proc_time / 100
    print ("Estimated frames per second : {0}".format(fps))

    video.release()