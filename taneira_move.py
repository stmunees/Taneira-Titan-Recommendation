#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 01:15:58 2019

@author: stejasmunees
"""

import os
from shutil import copyfile
import shutil
import random
counter=0

#zari_faux='/Volumes/Samsung_T5/Files/Dataset/Zari/Faux'
#zari_nil='/Volumes/Samsung_T5/Files/Dataset/Zari/NIL'
#zari_tested='/Volumes/Samsung_T5/Files/Dataset/Zari/Tested'
#zari_pure='/Volumes/Samsung_T5/Files/Dataset/Zari/Pure'

pallu_running='/Volumes/Samsung_T5/Files/Dataset/Pallu Pattern/Running'
pallu_contrast='/Volumes/Samsung_T5/Files/Dataset/Pallu Pattern/Contrast'

#zari_dest='/Volumes/Samsung_T5/Files/DS_Zari'
pallu_dest='/Volumes/Samsung_T5/Files/DS_Pallu'

src=pallu_running
dest=pallu_dest+'/running'
source_dir=os.listdir(src)

for files in source_dir:
    if files[0]!='.':
        counter+=1
        shutil.move(src+'/'+files,dest+'/'+files)
        

#source_dir=os.listdir(source)

#for folders in source_dir:
#    if folders[0]!='.':
#        for sub_folder in os.listdir(source+'/'+folders):
#            if sub_folder[0]!='.':
#                for files in os.listdir(source+'/'+folders+'/'+sub_folder):
#                    if files[0]!='.':
#                        counter+=1
#                        copyfile(source+'/'+folders+'/'+sub_folder+'/'+files, dest+'/'+sub_folder+'/'+files)

#yes_source='/Users/stejasmunees/Desktop/TEAL/dat_2/untitled folder/yes'
no_source='//Users/stejasmunees/Desktop/TEAL/dat_2/untitled folder/no'
#yes_source_dir=os.listdir(yes_source)
no_source_dir=os.listdir(no_source)
#yes_test_samples=random.sample(yes_source_dir, 400)
no_test_samples=random.sample(no_source_dir, 116)

no_dest='/Users/stejasmunees/Desktop/TEAL/dat_2/training_set/no'
#yes_dest='/Users/stejasmunees/Desktop/TEAL/dat_2/test_set/yes'
for no_files in no_test_samples:
    src=no_source+'/'+no_files
    dest=no_dest+'/'+no_files
    shutil.move(src,dest)
#for yes_files in yes_test_samples:
#    src=yes_source+'/'+yes_files
#    dest=yes_dest+'/'+yes_files
#    shutil.move(src,dest)

