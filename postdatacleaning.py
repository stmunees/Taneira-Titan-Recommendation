#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 09:11:01 2019

@author: stejasmunees
"""
#import os
#dataset_old='/Volumes/SSD/Dataset_Old'
#dataset_new='/Volumes/SSD/Dataset_New'
#dataset_olddir=os.listdir(dataset_old)
#dataset_newdir=os.listdir(dataset_new)
#
#for folder1 in dataset_olddir:
#    if(folder1[:1]!='.'):
#        folder1dir=os.listdir(dataset_old+'/'+folder1)
#        for folder2 in folder1dir:
#            if(folder2[:1]!='.'):
#                folder2dir=os.listdir(dataset_old+'/'+folder1+'/'+folder2)
#                for files in folder2dir:
#                    if(files[:1]!='.' ):
#                        path=dataset_old+'/'+folder1+'/'+folder2+'/'+files
#                        dest=dataset_new+'/'+folder1+'/'+folder2+'/'+files
#                        os.rename(path,dest)

import os
dataset_old='/Volumes/My Passport/destall'
dataset_new='/Volumes/My Passport/allinoneplace'

dataset_olddir=os.listdir(dataset_old)
dataset_newdir=os.listdir(dataset_new)

for files in dataset_olddir:
    if(files[:1]!='.' ):
        path=dataset_old+'/'+files
        dest=dataset_new+'/'+files
        os.rename(path,dest)
