#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 11:32:56 2019

@author: stejasmunees
"""

import os
import shutil

source_path='/Volumes/Samsung_T5/Files/pallu_floydhub'
dest_path='/Volumes/Samsung_T5/Files/pallu_floydhub_again'

source_path_dir=os.listdir(dest_path)


#for folder1 in source_path_dir:
#    if folder1[0]!='.':
#        for folder2 in os.listdir(source_path+'/'+folder1):
#            if folder2[0]!='.':
#                for images in os.listdir(source_path+'/'+folder1+'/'+folder2):
#                    if images[0]!='.':
#                        src=source_path+'/'+folder1+'/'+folder2+'/'+images
#                        dest=dest_path+'/'+folder1+'/'+folder2+'/'+images
#                        shutil.move(src,dest)

counter=0
for folder1 in source_path_dir:
    if folder1[0]!='.':
        for folder2 in os.listdir(dest_path+'/'+folder1):
            if folder2[0]!='.':
                for images in os.listdir(dest_path+'/'+folder1+'/'+folder2):
                    if images[0]=='.':
                        src=dest_path+'/'+folder1+'/'+folder2+'/'+images
                        os.unlink(src)
                        counter+=1


running_training=os.listdir('/Volumes/Samsung_T5/Files/pallu_floydhub_again/training_set/running')
contrast_training=os.listdir('/Volumes/Samsung_T5/Files/pallu_floydhub_again/training_set/contrast')
running_testing=os.listdir('/Volumes/Samsung_T5/Files/pallu_floydhub_again/test_set/running')
contrast_testing=os.listdir('/Volumes/Samsung_T5/Files/pallu_floydhub_again/test_set/contrast')
