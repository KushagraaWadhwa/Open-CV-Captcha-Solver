
import cv2 as cv
import os
from os import listdir
import numpy as np
from pathlib import Path

path=(r"C:\Users\KushagraWadhwa\Desktop\OpenCV\compliancecaptcha\compliancecaptcha")
captchas=os.listdir(path)
for images in captchas:
    x=path+ "\\"+images
    
    img=cv.imread(x)
    img=cv.GaussianBlur(img,(3,3),0)
    imgrey=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    
    ret, im_inv = cv.threshold(img,185,255,cv.THRESH_BINARY_INV)
    kernel = 1/25*np.array([[1,2,1], [2,4,2], [1,2,1]])
    im_blur = cv.filter2D(im_inv,-1,kernel)
   

    ret, im_res = cv.threshold(im_blur,140,255,cv.THRESH_BINARY)

    os.chdir(r"C:\Users\KushagraWadhwa\Desktop\OpenCV\Noise_reduced captcha")


    cv.imwrite(images+".png",im_res)


cv.waitKey(0)