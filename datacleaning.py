#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 09:44:07 2019

@author: stejasmunees
"""

#import os
#
#source='/Volumes/My Passport/test'
#batch=os.listdir(source)
#y=55152
#
#for files in batch:
#    y=y+1
#    digit=str(y).zfill(5)
#    path = os.path.join(source, files)
#    target = os.path.join(source, files[:-4]+"_%s"%digit+files[-4:])
#    os.rename(path,target)
    
    
import os
source='/Volumes/My Passport/testall'
dest='/Volumes/My Passport/destall'
batch=os.listdir(source)
y=0

for folders in batch:
    path1=os.path.join(source,folders)
    path2=os.listdir(path1)
    for files in path2:
        if(os.path.isfile(path1+'/'+files)):
            y=y+1
            digit=str(y).zfill(5)
            path=os.path.join(path1,files)
            target=os.path.join(dest,files[:-4]+"_%s"%digit+files[-4:])
            os.rename(path,target)
        if(os.path.isdir(path1+'/'+files)):
            path3=os.path.join(path1,files)
            path4=os.listdir(path3)
            for morefiles in path4:
                y=y+1
                digit=str(y).zfill(5)
                anotherpath=os.path.join(path3,morefiles)
                anothertarget=os.path.join(dest,morefiles[:-4]+"_%s"%digit+morefiles[-4:])
                os.rename(anotherpath,anothertarget)