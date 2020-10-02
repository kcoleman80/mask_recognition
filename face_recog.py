#!/usr/bin/env python
# coding: utf-8

get_ipython().system('pip install opencv-python')


get_ipython().system('pip install cvlib')


#import libraries
import cv2
import matplotlib.pyplot as plt
import cvlib as cv


image_path = '/IMG_PATH/IMG_5744.PNG'


im = cv2.imread(image_path)
plt.imshow(im)
plt.show()



faces, confidences = cv.detect_face(im)


#loop through detected faces via cvlib and add bounding boxes
for face in faces:
    (startX, startY) = face[0], face[1]
    (endX, endY) = face[2], face[3]
    
    #draw rectangle for bounding box
    cv2.rectangle(im, (startX, startY), (endX, endY), (0,255,0), 2)
    
    #display output
    plt.imshow(im)
    plt.show()



