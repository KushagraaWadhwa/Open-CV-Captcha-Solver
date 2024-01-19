import cv2
import numpy as np
import os

path=(r"C:\Users\KushagraWadhwa\Desktop\OpenCV\compliancecaptcha\compliancecaptcha")
captchas=os.listdir(path)

for images in captchas:
    x=path+ "\\"+images
    img = cv2.imread(x)


    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    img = cv2.GaussianBlur(img, (1, 1), 0)
    img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    ret, im_inv = cv2.threshold(img,190,255,cv2.THRESH_BINARY_INV)
    kernel = 1/25*np.array([[1,2,1], [2,4,2], [1,2,1]])
    im_blur = cv2.filter2D(im_inv,-1,kernel)
      

    ret, im_res = cv2.threshold(im_blur,160,255,cv2.THRESH_BINARY)
    cv2.imwrite(f"C:/Users/KushagraWadhwa/Desktop/OpenCV/Noise_reduced_captcha_3/{images[:-4]}.png", im_res)
