# Image Processing Using Scratch Python (Without OpenCV)

This directory contains Python scripts that perform various image processing tasks from scratch, without using OpenCV. Below is a summary of each script and the process it follows to achieve the respective tasks.

## Files and Descriptions

### 1. `convert_gray_scale.py`
This script converts a color image to grayscale.

**Process:**
- Load the image using a custom function.
- Iterate through each pixel of the image.
- Calculate the grayscale value using the formula: `gray = 0.299 * R + 0.587 * G + 0.114 * B`.
- Replace the original pixel values with the grayscale value.
- Save or display the grayscale image.

### 2. `convolve3d.py`
This script performs 3D convolution on an image.

**Process:**
- Load the image using a custom function.
- Define a 3D kernel for convolution.
- Iterate through each pixel of the image.
- Apply the convolution operation by multiplying the kernel with the corresponding pixel values and summing the results.
- Replace the original pixel values with the convolved values.
- Save or display the convolved image.

### 3. `dilation.py`
This script performs dilation on a binary image.

**Process:**
- Load the binary image using a custom function.
- Define a structuring element (kernel) for dilation.
- Iterate through each pixel of the image.
- Apply the dilation operation by checking if any pixel under the kernel is set to 1.
- If any pixel is set to 1, set the corresponding output pixel to 1.
- Save or display the dilated image.

### 4. `padding.py`
This script adds padding to an image.

**Process:**
- Load the image using a custom function.
- Define the padding size.
- Create a new image with the increased size.
- Copy the original image pixels to the center of the new image.
- Fill the padding areas with a specified value (e.g., 0 for black).
- Save or display the padded image.

## Requirements

- Python 3.x
- NumPy

## How to Run

To run any of the scripts, use the following command:

```bash
python <script_name>.py
```