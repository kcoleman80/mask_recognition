#!/usr/bin/env python
# coding: utf-8

# In[1]:


pwd


# In[2]:


get_ipython().system('pip install opencv-python')


# In[3]:


get_ipython().system('pip install cvlib')


# In[2]:


#import libraries
import cv2
import matplotlib.pyplot as plt
import cvlib as cv


# In[3]:


#image_path = 'IMG_PATH'


# In[4]:


image_path = '/IMG_PATH/IMG_5744.PNG'


# In[5]:


im = cv2.imread(image_path)
plt.imshow(im)
plt.show()


# In[6]:


faces, confidences = cv.detect_face(im)


# In[7]:


#loop through detected faces via cvlib and add bounding boxes
for face in faces:
    (startX, startY) = face[0], face[1]
    (endX, endY) = face[2], face[3]
    
    #draw rectangle for bounding box
    cv2.rectangle(im, (startX, startY), (endX, endY), (0,255,0), 2)
    
    #display output
    plt.imshow(im)
    plt.show()


# In[ ]:




