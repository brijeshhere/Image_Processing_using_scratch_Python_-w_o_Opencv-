import numpy as np
import cv2
from padding import padding
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
image=cv2.imread("sample.jpg")
random_kernel=np.random.randint(-10,10,size=(3,3))
gaussian_kernel=np.ones((3,3))

def convolve3d(image,kernel):
    h,w,c=image.shape
    kernel_size=kernel.shape[0]
    pad_size=kernel.shape[0]//2
    # padded=padding(image,pad_size)
    padded=np.pad(image,((pad_size,pad_size),(pad_size,pad_size),(0,0)),mode='edge')
    output_image=np.zeros_like(image)
    for i in range(h):
        for j in range(w):
            region=padded[i:i+kernel_size,j:j+kernel_size,:]
            for c in range(3):
                rgb_value=np.sum(kernel*region[:,:,c])
                output_image[i,j,c]=rgb_value
    return output_image
cv2.imshow("colv",convolve3d(image,random_kernel))
cv2.waitKey(0)
cv2.destroyAllWindows()
            
            
            