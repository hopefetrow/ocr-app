from django.shortcuts import render

# for pytesseract import 
import pytesseract
# End of pytesseract import   

# import the necessary packages
from easyocr import Reader
import argparse
import cv2

import os
from .forms import ImageUpload
from PIL import Image 
from django.conf import settings  

# Create your views here.

# For the home views
def home(request):
    return render(request, 'home.html', {})

# For the ImageToText views
# This has been done with pytesseract
# This function may explode, DO NOT TOUCH!!
def textConversions(request):
    text = ""
    if request.method == 'POST':
        form = ImageUpload(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            image = request.FILES['image']
            image = image.name 
            path = settings.MEDIA_ROOT 
            pathz = path + '/images/' + image 

            text = pytesseract.image_to_string(Image.open(pathz))
            text = text.encode("ascii", "ignore")
            text = text.decode()

    context = {
        'text': text
    }   
    return render(request, 'text.html', context)
# End of the Bomb Explosion


# For the license reader views 
def license(request):
  
    def cleanup_text(text):
	# strip out non-ASCII text so we can draw the text on the image
	# using OpenCV
	    return "".join([c if ord(c) < 128 else "" for c in text]).strip()

    image = cv2.imread("../license_2.jpg")

    reader = Reader(['en'], gpu=True)
    results = reader.readtext(image)
        
        # loop over the results

        
    text1 = list()
    for (bbox, text, prob) in results:
        clean_txt = cleanup_text(text)
        text1.append(clean_txt)
        # print(clean_txt)
        
        # return render(request, 'license.html', {'text':text1})
    return render(request, 'license.html', {'text':text1})

        # cv2.rectangle(image, tl, br, (0, 255, 0), 2)
        # cv2.putText(image, text, (tl[0], tl[1] - 10),
        # cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        # show the output image
        # cv2.imshow("Image", image)
        # cv2.waitKey(0)