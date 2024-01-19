import os
import numpy as np 

import cv2 as cv
import time

count = 0

start_time=time.time()
path=(r"C:\Users\KushagraWadhwa\Desktop\OpenCV\compliancecaptcha\compliancecaptcha")
captchas=os.listdir(path)

for images in captchas:
    x=path+ "\\"+images
    img = cv.imread(x)

  
  
    ret, im_inv = cv.threshold(img,184,255,cv.THRESH_BINARY_INV)
    kernel = 1/25*np.array([[1,2,1], [2,4,2], [1,2,1]])
    im_blur = cv.filter2D(im_inv,-1,kernel)
   

    ret, im_res = cv.threshold(im_blur,133,255,cv.THRESH_BINARY_INV)
    contrast=10
    brightness=2
    
    out = cv.addWeighted( im_res, contrast, im_res, 0, brightness)
    
    # ret, im_res = cv2.threshold(im_res,210,255,cv.THRESH_BINARY)
    # stretch_near = cv2.resize(im_res, (784,500),
    #            interpolation = cv2.INTER_LINEAR)
    # sharpening_filter=1/4*np.array([[-1,-1,-1],
    #                             [-1,9,-1],
    #                             [-1,-1,-1]])
    # sharpened_image=cv.filter2D(img,-1,sharpening_filter)
    cv.imwrite(f"C:/Users/KushagraWadhwa/Desktop/OpenCV/Noise_reduced_captcha_1/{images[:-4]}.png",out)
    count += 1
    
    
end_time=time.time()
t=end_time-start_time
print(f"Done. Solved {count} captchas in {t} seconds")