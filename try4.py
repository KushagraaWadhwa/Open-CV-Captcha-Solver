import cv2
import os


path=(r"C:\Users\KushagraWadhwa\Desktop\OpenCV\compliancecaptcha\compliancecaptcha")
captchas=os.listdir(path)
for images in captchas:
    x=path+ "\\"+images
    img = cv2.imread(x)
    gry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    (h, w) = gry.shape[:2]
    gry = cv2.resize(gry, (w*2, h*2))

    cls = cv2.morphologyEx(gry, cv2.MORPH_CLOSE, None)
    val, thr = cv2.threshold(cls, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    val,thr = cv2.threshold(cls, 0, 255, cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)

    val, thr = cv2.threshold(cls, 140, 255, cv2.THRESH_BINARY_INV)
    # val, thr = cv2.threshold(cls, 0, 255, 8 )

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (4,8))
    morph_img = cv2.morphologyEx(thr, cv2.MORPH_CLOSE, kernel)
    cv2.imwrite(f"C:/Users/KushagraWadhwa/Desktop/OpenCV/test4/{images[:-4]}.png",morph_img)

cv2.waitKey(0)