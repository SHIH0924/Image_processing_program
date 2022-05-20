import cv2 as cv
import numpy as np
from tkinter import messagebox as msgbox
from tkinter import filedialog
import im
def cv_imread(filePath):                    # 讀取檔案路徑
    cv_img=cv.imdecode(np.fromfile(filePath,dtype=np.uint8),-1)
    return cv_img                           # 回傳路徑

def Harris_Corner_Detector():#哈里斯邊角偵測
    try:
        # 將輸入圖像轉換為灰度色彩空間
        operatedImage = cv.cvtColor(im.im, cv.COLOR_BGR2GRAY)
        #修改數據類型設置為 32 位浮點數
        operatedImage = np.float32(operatedImage)
        # 應用 cv2.cornerHarris 方法
        dest = cv.cornerHarris(operatedImage, 2, 5, 0.07)
        # 結果通過擴張的角標記
        dest = cv.dilate(dest, None)
        # 恢復到原始圖像
        im.im[dest > 0.01 * dest.max()]=[0, 0, 255]
        return im.im
    except Exception:
        msgbox.showerror("Error", "Median Filter error!!!")


