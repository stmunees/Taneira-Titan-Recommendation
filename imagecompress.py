#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 12:28:27 2019

@author: stejasmunees
"""

#Reducing the file Size.
import os
import string
count=0
nonimage=0
#source='/Volumes/Samsung_T5/Files/Contrast'


#dest1='/Volumes/Samsung_T5/Files/Contrast_Min 90T10'
#dest3='/Volumes/Samsung_T5/Files/Contrast_Min 90F10'
#dest5='/Volumes/Samsung_T5/Files/Contrast_Min 95T10'
#dest7='/Volumes/Samsung_T5/Files/Contrast_Min 95F10'
#
#dest2='/Volumes/Samsung_T5/Files/Contrast_Min 90T20'
#dest4='/Volumes/Samsung_T5/Files/Contrast_Min 90F20'
#dest6='/Volumes/Samsung_T5/Files/Contrast_Min 95T20'
#dest8='/Volumes/Samsung_T5/Files/Contrast_Min 95F20'

source='/Volumes/Samsung_T5/Files/allinoneplace'
dest='/Volumes/Samsung_T5/Files/allinoneplace_min'

#source='/Volumes/Samsung_T5/Files/all'
#dest='/Volumes/Samsung_T5/Files/all min'


source_dir=os.listdir(source)
#dest_dir=os.listdir(dest)

foo_size={}
i=0
from PIL import Image
for files in source_dir:
    if(((files[-4:]).lower()=='.jpg') or ((files[-5:]).lower()=='.jpeg') or 
       ((files[-4:]).lower()=='.png')):
        if(files[0]!='.'):
            i=i+1
            foo = Image.open(source+'/'+files)
            foo_size[i]=foo.size
            count=count+1
        else:
            nonimage=nonimage+1
    else:
        nonimage=nonimage+1   

foo_ratio={}    
for i in range(len(foo_size)):
    temp=foo_size[i+1]
    foo_ratio[i+1]=temp[0]/temp[1]

new_size_10={}
#new_size_20={}
i=0
for i in range(len(foo_ratio)):
    temp_old=foo_size[i+1]
    height=temp_old[0]
    height=height/10
    width=height/foo_ratio[i+1]
    new_size_10[i+1]=(round(height),round(width))
    
#    temp_old=foo_size[i+1]
#    height=temp_old[0]
#    height=height/20
#    width=height/foo_ratio[i+1]
#    new_size_20[i+1]=(round(width),round(height))
    
#from PIL import ImageFile
#ImageFile.LOAD_TRUNCATED_IMAGES = True

import PIL.Image
PIL.Image.LOAD_TRUNCATED_IMAGES = True
PIL.Image.LOAD_TRUNCATED_IMAGE = True


i=0
for files in source_dir:
    if(((files[-4:]).lower()=='.jpg') or ((files[-5:]).lower()=='.jpeg') or 
       ((files[-4:]).lower()=='.png')):
        if(files[0]!='.'):
            i=i+1
#            print(i)
#            print(files)
            foo = PIL.Image.open(source+'/'+files)
            foo1 = foo.resize(new_size_10[i],PIL.Image.ANTIALIAS)
            foo1.save(dest+'/'+files,quality=95)
#    foo2 = foo.resize(new_size_20[i+1],Image.ANTIALIAS)
    
#    foo1.save(dest1+'/'+files,optimize=True,quality=90)
#    foo1.save(dest3+'/'+files,quality=90)
#    foo1.save(dest5+'/'+files,optimize=True,quality=95)
#    foo1.save(dest7+'/'+files,quality=95)
#    foo2.save(dest2+'/'+files,optimize=True,quality=90)
#    foo2.save(dest4+'/'+files,quality=90)
#    foo2.save(dest6+'/'+files,optimize=True,quality=95)
#    foo2.save(dest8+'/'+files,quality=95)


#Compression Sizes
#    
#90F10=34.2 for 832 (1.09GB x6)
#90F20=10.2 for 832 (325MB x6)
#90T10=34   for 832 (1.08GB x6)
#90T20=9.8  for 832 (312MB x6)
#95F10=51.8 for 832 (1.65GB x6)
#95F20=14.7 for 832 (468MB x6)
#95T10=50.5 for 832 (1.6GB x6)
#95T20=14.1 for 832 (449MB x6)
