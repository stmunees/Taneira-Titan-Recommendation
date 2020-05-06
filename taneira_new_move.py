#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 16:08:29 2019

@author: stejasmunees
"""

import os
from shutil import copyfile
import shutil
import random
counter=0

##zari_faux='/Volumes/Samsung_T5/Files/Dataset/Zari/Faux'
##zari_nil='/Volumes/Samsung_T5/Files/Dataset/Zari/NIL'
##zari_tested='/Volumes/Samsung_T5/Files/Dataset/Zari/Tested'
##zari_pure='/Volumes/Samsung_T5/Files/Dataset/Zari/Pure'
#
#pallu_running='/Volumes/Samsung_T5/Files/Dataset/Pallu Pattern/Running'
#pallu_contrast='/Volumes/Samsung_T5/Files/Dataset/Pallu Pattern/Contrast'
#
##zari_dest='/Volumes/Samsung_T5/Files/DS_Zari'
#pallu_dest='/Volumes/Samsung_T5/Files/DS_Pallu'
#
#src=pallu_running
#dest=pallu_dest+'/running'
#source_dir=os.listdir(src)
#
#for files in source_dir:
#    if files[0]!='.':
#        counter+=1
#        shutil.move(src+'/'+files,dest+'/'+files)
        
#
#no_training='/Volumes/Samsung_T5/Files/zari_floydhub/training_set/no'
#no_testing='/Volumes/Samsung_T5/Files/zari_floydhub/test_set/no'
#yes_training='/Volumes/Samsung_T5/Files/zari_floydhub/training_set/yes'
#yes_testing='/Volumes/Samsung_T5/Files/zari_floydhub/test_set/yes'
#yes_source='/Volumes/Samsung_T5/Files/DS_Zari/yes'
#no_source='/Volumes/Samsung_T5/Files/DS_Zari/no'

#yes_source_dir=os.listdir(yes_source)
#no_source_dir=os.listdir(no_source)

#stuck=0
#
#for yes_files in yes_test_samples:
#    if yes_files[0]!='.':
#        src=yes_source+'/'+yes_files
#        dest=yes_testing+'/'+yes_files
#        shutil.move(src,dest)
#        
#for no_files in no_test_samples:
#    if no_files[0]!='.':
#        src=no_source+'/'+no_files
#        dest=no_testing+'/'+no_files
#        shutil.move(src,dest)

#yes_source_dir=os.listdir(yes_source)
#no_source_dir=os.listdir(no_source)
#
#for yes_files in yes_source_dir:
#    if yes_files[0]!='.':
#        src=yes_source+'/'+yes_files
#        dest=yes_training+'/'+yes_files
#        shutil.move(src,dest)
#
#for no_files in no_source_dir:
#    if no_files[0]!='.':
#        src=no_source+'/'+no_files
#        dest=no_training+'/'+no_files
#        dest_copy=dest+' copy'
#        copyfile(src,dest_copy)
#        shutil.move(src,dest)
#
#for no_files in no_source_dir:
#    if no_files[0]!='.':
#        src=no_source+'/'+no_files
#        dest=no_training+'/'+no_files
#        dest_copy=no_training+'/copy '+no_files
#        copyfile(src,dest_copy)
#        shutil.move(src,dest)

yes_test_samples=random.sample(yes_source_dir,2000)
no_test_samples=random.sample(no_source_dir,2000)

running_training='/Volumes/Samsung_T5/Files/pallu_floydhub/training_set/running'
running_testing='/Volumes/Samsung_T5/Files/pallu_floydhub/test_set/running'
contrast_training='/Volumes/Samsung_T5/Files/pallu_floydhub/training_set/contrast'
contrast_testing='/Volumes/Samsung_T5/Files/pallu_floydhub/test_set/contrast'

contrast_source='/Volumes/Samsung_T5/Files/DS_Pallu/contrast'
running_source='/Volumes/Samsung_T5/Files/DS_Pallu/running'

contrast_source_dir=os.listdir(contrast_source)
running_source_dir=os.listdir(running_source)



#yes_counter=0
#for files in yes_source_dir:
#    if files[0]!='.':
#        src=yes_source+'/'+files
#        dest=yes_training+'/'+files
#        copyfile(src,dest)
#        yes_counter+=1
#
#no_counter=0
#for files in no_source_dir:
#    if files[0]!='.':
#        src=no_source+'/'+files
#        copyfile(src,dest)
#        no_counter+=1


contrast_test_samples=random.sample(contrast_source_dir,2000)
running_test_samples=random.sample(running_source_dir,2000)

stuck=0

for contrast_files in contrast_test_samples:
    if contrast_files[0]!='.':
        src=contrast_source+'/'+contrast_files
        dest=contrast_testing+'/'+contrast_files
        shutil.move(src,dest)
        
for running_files in running_test_samples:
    if running_files[0]!='.':
        src=running_source+'/'+running_files
        dest=running_testing+'/'+running_files
        shutil.move(src,dest)

contrast_source_dir=os.listdir(contrast_source)
running_source_dir=os.listdir(running_source)

for running_files in running_source_dir:
    if running_files[0]!='.':
        src=running_source+'/'+running_files
        dest=running_training+'/'+running_files
        shutil.move(src,dest)
        
contrast_test_samples=random.sample(contrast_source_dir,5728)
for contrast_files in contrast_test_samples:
    if contrast_files[0]!='.':
        src=contrast_source+'/'+contrast_files
        dest_copy=contrast_training+'/copy '+contrast_files
        copyfile(src,dest_copy)
        

for contrast_files in contrast_source_dir:
    if contrast_files[0]!='.':
        src=contrast_source+'/'+contrast_files
        dest=contrast_training+'/'+contrast_files
        shutil.move(src,dest)

#for no_files in no_source_dir:
#    if no_files[0]!='.':
#        src=no_source+'/'+no_files
#        dest=no_training+'/'+no_files
#        dest_copy=no_training+'/copy '+no_files
#        copyfile(src,dest_copy)
#        shutil.move(src,dest)

#mistake='/Volumes/Samsung_T5/Files/mistake'
mistake='/Volumes/Samsung_T5/Files/zari_floydhub/training_set/no'
mistake_dir=os.listdir(mistake)

for mis_files in mistake_dir:
    if mis_files[0]!='.':
        if mis_files[-4:]=='copy':
            corrected_name='copy '+mis_files[:-5]
            src=mistake+'/'+mis_files
            dest=mistake+'/'+corrected_name
            shutil.move(src,dest)
            

##yes_source='/Users/stejasmunees/Desktop/TEAL/dat_2/untitled folder/yes'
#no_source='//Users/stejasmunees/Desktop/TEAL/dat_2/untitled folder/no'
##yes_source_dir=os.listdir(yes_source)
#no_source_dir=os.listdir(no_source)
##yes_test_samples=random.sample(yes_source_dir, 400)
#no_test_samples=random.sample(no_source_dir, 116)

#no_dest='/Users/stejasmunees/Desktop/TEAL/dat_2/training_set/no'
##yes_dest='/Users/stejasmunees/Desktop/TEAL/dat_2/test_set/yes'
#for no_files in no_test_samples:
#    src=no_source+'/'+no_files
#    dest=no_dest+'/'+no_files
#    shutil.move(src,dest)
#for yes_files in yes_test_samples:
#    src=yes_source+'/'+yes_files
#    dest=yes_dest+'/'+yes_files
#    shutil.move(src,dest)