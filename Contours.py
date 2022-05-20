import cv2 as cv
import numpy as np
from tkinter import messagebox as msgbox
import im
def nothing(x):
    pass

def Simple_Contour():#簡單輪廓
    try:
        image = im.im
        # 將圖像轉換為灰階格式
        img_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        # 應用二進制閾值
        ret, thresh = cv.threshold(img_gray, 150, 255, cv.THRESH_BINARY)
        # 使用 cv2.CHAIN_APPROX_NONE 檢測二值圖像上的輪廓
        contours, hierarchy = cv.findContours(image=thresh, mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_NONE)
        # 在原始圖像上繪製輪廓
        cv.namedWindow('image')# 新建視窗
        cv.createTrackbar('B','image',0,255,nothing)   #線體顏色
        cv.createTrackbar('G','image',0,255,nothing)   #線體顏色
        cv.createTrackbar('R','image',0,255,nothing)   #線體顏色
        cv.createTrackbar('L','image',0,20,nothing)    #線體粗細
        while(1):
            B = cv.getTrackbarPos('B','image')         #獲取數值
            G = cv.getTrackbarPos('G','image')
            R = cv.getTrackbarPos('R','image')
            L = cv.getTrackbarPos('L','image')
            image_copy = image.copy()
            cv.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(B, G, R), thickness=L, lineType=cv.LINE_AA)
            cv.imshow('image',image_copy)
            k = cv.waitKey(1) & 0xFF
            if k == 13:
                cv.destroyWindow('image')
                return image_copy
            elif k==32:
                cv.destroyWindow('image')
                return im.im
    except Exception:
        msgbox.showerror("Error", "Median Filter error!!!")

def Convex_Hull():#凸包
    try:
        image = im.im
        # 將圖像轉換為灰度格式
        img_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        # 應用二進制閾值
        ret, thresh = cv.threshold(img_gray, 150, 255, cv.THRESH_BINARY)
        # 使用 cv2.CHAIN_APPROX_NONE 檢測二值圖像上的輪廓
        contours, hierarchy = cv.findContours(image=thresh, mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_NONE)
        hull = []
        # 計算每個輪廓的點
        for i in range(len(contours)):
            # creating convex hull object for each contour
            hull.append(cv.convexHull(contours[i], False))
        # 創建一個空的黑色圖像
        drawing = np.zeros((thresh.shape[0], thresh.shape[1], 3), np.uint8)
        # 繪製輪廓和船體點
        for i in range(len(contours)):
            color_contours = (0, 255, 0) # green - 輪廓顏色
            color = (255, 0, 0) # blue - 凸包顏色
            # draw ith contour
            cv.drawContours(drawing, contours, i, color_contours, 1, 8, hierarchy)
            # 繪製凸包對象
            cv.drawContours(drawing, hull, i, color, 1, 8)
        # 查看結果
        cv.imshow('Convex Hull', drawing)
        while(1):
            k = cv.waitKey(1) & 0xFF
            if k == 13:
                cv.destroyWindow('Convex Hull')
                return drawing
            elif k==32:
                cv.destroyWindow('Convex Hull')
                return im.im
    except Exception:
        msgbox.showerror("Error", "Median Filter error!!!")