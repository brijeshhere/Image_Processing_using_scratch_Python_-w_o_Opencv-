import os
import numpy as np
import cv2

os.chdir(os.path.dirname(os.path.abspath(__file__)))
image=cv2.imread("sample.jpg")
h,w,c=image.shape
output=np.zeros((h,w),dtype=np.uint8)
for i in range(h):
    for j in range(w):
        r,b,g=image[i,j]
        gray_value=int(0.2898*r+0.5870*b+0.114*g)
        output[i,j]=gray_value
cv2.imshow("image",output)
cv2.waitKey(0)
cv2.destroyAllWindows()
        