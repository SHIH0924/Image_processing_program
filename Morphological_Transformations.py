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

def Skeletonize():#骨架化
    img = cv.cvtColor(im.im, cv.COLOR_BGR2GRAY)
    size = np.size(img)
    skel = np.zeros(img.shape,np.uint8)
    ret,img = cv.threshold(img,127,255,0)
    element = cv.getStructuringElement(cv.MORPH_CROSS,(3,3))
    done = False

    while( not done):
        eroded = cv.erode(img,element)
        temp = cv.dilate(eroded,element)
        temp = cv.subtract(img,temp)
        skel = cv.bitwise_or(skel,temp)
        img = eroded.copy()
        zeros = size - cv.countNonZero(img)
        if zeros==size:
            done = True
    return skel

def perim():#邊緣
    try:
        input_image = im.im
        img = cv.cvtColor(input_image, cv.COLOR_BGR2GRAY) 
        cv.namedWindow('image')# 新建視窗
        cv.createTrackbar('x','image',10,200,nothing)
        cv.createTrackbar('y','image',10,200,nothing)
        while(1):
            x = cv.getTrackbarPos('x','image')
            y = cv.getTrackbarPos('y','image')
            kernel = np.ones((x,y),np.uint8)
            dilation = cv.dilate(img,kernel,iterations = 1)
            diff2 = dilation - img
            cv.imshow("image", diff2)
            k = cv.waitKey(1) & 0xFF
            if k == 13:
                cv.destroyWindow('image')
                return diff2
            elif k==32:
                cv.destroyWindow('image')
                return im.im
    except Exception:
        msgbox.showerror("Error", "Median Filter error!!!")

