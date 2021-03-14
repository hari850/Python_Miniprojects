# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 01:03:57 2021

@author: admin
"""
""" Code for copying files with specific extension to another folder """



import os
import shutil
print(os.getcwd())
os.chdir("C:\\Users\\admin\\Downloads") # change cwd to where files located
print(os.getcwd())

os.mkdir("test") # creating a new folder 

for f in os.listdir():
    file_name,file_ext = os.path.splitext(f)
    if file_ext == ".pdf" :  # I am using .Pdf it can be change to .mp4 etc as per use
        shutil.copy(f,"C:\\Users\\admin\\Downloads\\test")
