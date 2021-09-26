"""
This program is to see how OCR works by implementing basic 
program
Courtesy:   1. https://www.youtube.com/watch?v=ZVKaWPW9oQY
            2. https://www.youtube.com/watch?v=9nUNPrvCFAE&t=660s
            
"""

# For visualization import opencv
# import cv2 
# For OCR processing import easyocr
# import easyocr
# from matplotlib import pyplot as plt 
# import numpy as np  

# IMAGE_PATH = 'testimage_5.png'

# reader = easyocr.Reader(['en'], gpu=False) 
# result = reader.readtext(IMAGE_PATH)

# The result will be visualized as a list

# print (result)

# For testimage.png
# [([[21, 56], [281, 56], [281, 95], [21, 95]], 'Testing Tesseract OCR', 0.9993061633177647)] 
# For testimage_2.png
# [([[49, 20], [454, 20], [454, 92], [49, 92]], 'Tesseract Will', 0.901809384557269), 
# ([[21, 83], [480, 83], [480, 175], [21, 175]], 'Fail With Noisy', 0.9301844122249241), 
# ([[52, 158], [447, 158], [447, 244], [52, 244]], 'Backgrounds', 0.8528807132538547)]

"""
The first 4 things are the coordinates of the text
And, the last one is the confidence level

"""

"""
# For visualizing as image with single line we will use top-left and bottom-right coordinates
top_left = tuple(result[0][0][0])
bottom_right = tuple(result[0][0][2])
text = result[0][1]
font = cv2.FONT_HERSHEY_COMPLEX

img = cv2.imread(IMAGE_PATH)
# For drwaing rectangle around the text
img = cv2.rectangle(img, top_left, bottom_right, (0,255,0), 2)
# For showing the text on top-left corner
img = cv2.putText(img, text, top_left, font, .5, (243,15,15),1, cv2.LINE_AA)
plt.imshow(img)
plt.show()

"""

# For visualizing multiline characters 

# img = cv2.imread(IMAGE_PATH)

# Need to loop through the lines to detect

# for detection in result:
#     top_left = tuple([int(val) for val in detection[0][0]])
#     bottom_right = tuple([int(val) for val in detection[0][2]])
#     text = detection[1]
#     font = cv2.FONT_HERSHEY_COMPLEX
#     img = cv2.rectangle(img, top_left, bottom_right, (255.0,0), 1)
#     img = cv2.putText(img, text, top_left, font, 1, (0, 114,57), 1, cv2.LINE_AA)

# plt.figure(figsize=(10,10))
# plt.imshow(img)
# plt.show()

import cv2
import pytesseract

def ocr_core(img):
    text = pytesseract.image_to_string(img)
    return text 
    
img = cv2.imread('testimage_3.png')

def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def remove_noise(image):
    return cv2.medianBlur(image, 5)

def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

img = get_grayscale(img)
img = thresholding(img)
img = remove_noise(img)

print(ocr_core(img))
print(type(ocr_core(img)))



