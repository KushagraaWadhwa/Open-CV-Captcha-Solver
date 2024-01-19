import cv2
import os
import subprocess
import time
import numpy as np


count = 0
start_time=time.time()
path=(r"C:\Users\KushagraWadhwa\Desktop\OpenCV\compliancecaptcha\compliancecaptchatest")
captchas=os.listdir(path)
kernel = np.ones((3,3), np.uint8)

for images in captchas:
    x=path+ "\\"+images
    img = cv2.imread(x, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, None, fx=10, fy=10, interpolation=cv2.INTER_LINEAR)
    # img = cv2.medianBlur(img, 9)
    img=cv2.GaussianBlur(img,(5,5),0)
    # th, img = cv2.threshold(img, 169, 255, cv2.THRESH_BINARY)
    # img=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,17,2)
    ret2, th2 = cv2.threshold(img, 10, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    img = cv2.erode(th2, kernel, iterations=1)
    img = cv2.dilate(img, kernel, iterations=1)
    cv2.imwrite(f"C:/Users/KushagraWadhwa/Desktop/OpenCV/Noise_reduced_captcha_2/{images[:-4]}.png", img)
    # command = ['tesseract', 'image.png', 'stdout', '--psm', '8', '--oem', '0', '-c', 'tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyz', '--dpi', '70']
    # captcha_text = subprocess.check_output(command).decode().replace(" ", "").rstrip().lower()

    count += 1
end_time=time.time()
t=end_time-start_time
print(f"Done. Solved {count} captchas in {t} seconds")