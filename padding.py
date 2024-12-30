import numpy as np
import cv2
import os

def padding(image,pad_size):
    h,w,c=image.shape
    padded_blank=np.ones((h+2*pad_size,w+2*pad_size,c),dtype=np.uint8)*255
    padded_blank[pad_size:pad_size+h,pad_size:pad_size+w,:]=image
    return padded_blank
# os.chdir(os.path.dirname(os.path.abspath(__file__)))
# image=cv2.imread("sample.jpg")
# cv2.imshow("image",padding(image,100))
# cv2.waitKey(0)
# cv2.destroyAllWindows()
