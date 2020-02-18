# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 09:57:59 2020
@author: loren

Description: converting rgb images to greyscale and saving them
"""

from PIL import Image
import os

def rgb2gray(path,image):
        
   #fname = os.path.basename(image)  
   #basename_noExtension = os.path.splitext(fname)[0] 
   #extension = os.path.splitext(fname)[1]
   img = Image.open(path + image).convert('L')
   img.save(path + image)	
	

KnownImages_dir_path = "./data/Known-Images"
UnknownImages_dir_path = "./data/To-Verify"
rgb2gray(UnknownImages_dir_path,'/person3.jpg')



