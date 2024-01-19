import cv2 as cv
import numpy as np
import os
from matplotlib import pyplot as plt
counter =0 
path=(r"C:\Users\KushagraWadhwa\Desktop\OpenCV\compliancecaptcha\compliancecaptcha")
captchas=os.listdir(path)
for images in captchas:
    x=path+ "\\"+images
    img=cv.imread(x)
    img1=cv.imread(x)


    img=cv.medianBlur(img,3)
    imgrey=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    threshold, threshImage=cv.threshold(imgrey,170,255,cv.THRESH_BINARY_INV)
    min_connected_len = 15
    numLabel, labelImage, stats, centroids = cv.connectedComponentsWithStats(threshImage, 8, cv.CV_32S)
    foreComps = [i for i in range(1, numLabel) if stats[i, cv.CC_STAT_AREA] >= min_connected_len]
        
    binaryImage = np.zeros_like(img)
    labelImage = np.array(labelImage)
    for k in [np.where(labelImage == i) for i in foreComps]:
            binaryImage[k] = 255
    minCol = 20
    array = np.array([stats[i, cv.CC_STAT_LEFT] + stats[i, cv.CC_STAT_WIDTH]  for i in foreComps])
    maxCol = max(array[np.where(array < 200)]) 
    minRow = min([stats[i, cv.CC_STAT_TOP] for i in foreComps])
    maxRow = max([stats[i, cv.CC_STAT_TOP] + stats[i, cv.CC_STAT_HEIGHT] for i in foreComps])
    subImage = threshImage[minRow:maxRow, minCol:maxCol]
       
    cv.imwrite(f"C:/Users/KushagraWadhwa/Desktop/OpenCV/Noise_reduced_captcha_2/{images[:-4]}.png",subImage)



print(counter)
cv.waitKey(0)