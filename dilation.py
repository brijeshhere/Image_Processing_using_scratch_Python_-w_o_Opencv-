import numpy as np
import cv2
import os

kernel=np.ones((5,5))
kernel_size=kernel.shape[0]
pad_size=kernel_size//2
os.chdir(os.path.dirname(os.path.abspath(__file__)))
image=cv2.imread("sample.jpg")
h,w,c=image.shape
padded=np.pad(image,((pad_size,pad_size),(pad_size,pad_size),(0,0)),mode='constant',constant_values=255)
output=np.zeros_like(image)
for i in range(h):
    for j in range(w):
        for k in range(c):
            region=padded[i:i+kernel_size,j:j+kernel_size,k]
            output[i,j,k]=np.min(region[kernel==1])
cv2.imshow("image",output)
cv2.waitKey(0)
cv2.destroyAllWindows()