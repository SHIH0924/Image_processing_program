import cv2 as cv
import numpy as np
from tkinter import messagebox as msgbox
import im

def nothing(x):
    pass

def Basic_morphology(x):
    cv.x=x
    try:
        cv.namedWindow('image')# 新建視窗
        cv.createTrackbar('frequency','image',0,20,nothing)
        cv.createTrackbar('x','image',0,20,nothing)
        cv.createTrackbar('y','image',0,20,nothing)
        while(1):
            frequency = cv.getTrackbarPos('frequency','image')
            x = cv.getTrackbarPos('x','image')
            y = cv.getTrackbarPos('y','image')
            img=im.im
            kernal=np.ones((x,y),np.uint8)
            des=cv.x(img,kernal,iterations=frequency)
            cv.imshow('image',des)
            k = cv.waitKey(1) & 0xFF
            if k == 13:
                cv.destroyWindow('image')
                return des
            elif k==32:
                cv.destroyWindow('image')
                return im.im
    except Exception:
        msgbox.showerror("Error", "Median Filter error!!!")

