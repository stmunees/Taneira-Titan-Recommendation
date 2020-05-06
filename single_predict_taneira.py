#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 18:14:42 2019

@author: stejasmunees
"""
from keras.models import model_from_json
import pandas as pd
import numpy as np
import os
from shutil import copyfile
from PIL import Image
import matplotlib.pyplot as plt

def copy (old_source,old_source_dir,new_source):
    for files in old_source_dir:
        if files[0]!='.':
            copyfile(old_source+'/'+files,new_source+'/'+files)

def compress (old_source,old_source_dir,new_source):
    foo_size={}
    i=0
    count=0
    nonimage=0
    for files in old_source_dir:
        if(((files[-4:]).lower()=='.jpg') or ((files[-5:]).lower()=='.jpeg') or 
       ((files[-4:]).lower()=='.png')):
            if(files[0]!='.'):
                i=i+1
                foo = Image.open(old_source+'/'+files)
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
    i=0
    for i in range(len(foo_ratio)):
        temp_old=foo_size[i+1]
        height=temp_old[0]
        height=height/10
        width=height/foo_ratio[i+1]
        new_size_10[i+1]=(round(height),round(width))
        
    import PIL.Image
    PIL.Image.LOAD_TRUNCATED_IMAGES = True
    PIL.Image.LOAD_TRUNCATED_IMAGE = True
    
    i=0
    for files in old_source_dir:
        if(((files[-4:]).lower()=='.jpg') or ((files[-5:]).lower()=='.jpeg') or 
       ((files[-4:]).lower()=='.png')):
            if(files[0]!='.'):
                i=i+1
                foo = PIL.Image.open(old_source+'/'+files)
                foo1 = foo.resize(new_size_10[i],PIL.Image.ANTIALIAS)
                foo1.save(new_source+'/'+files,quality=95)
                

#Attributes Data
df = pd.read_csv('attributes_model.csv') 
sku=df.iloc[:,0].values
sku=list(sku)
base_colour=df.iloc[:,1].values
base_colour=list(base_colour)
craft=df.iloc[:,3].values
craft=list(craft)
zari=df.iloc[:,4].values
zari=list(zari)
body_pattern=df.iloc[:,5].values
body_pattern=list(body_pattern)
pallu_pattern=df.iloc[:,6].values
pallu_pattern=list(pallu_pattern)


# Loading Pallu Classifier
json_file = open('/Users/stejasmunees/Desktop/Trained Models/pallu/taneira_pallu_03.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
classifier_pallu = model_from_json(loaded_model_json)
# load weights into new model
classifier_pallu.load_weights('/Users/stejasmunees/Desktop/Trained Models/pallu/taneira_pallu_03.h5')
print("Loaded model from disk")

#Loading Zari Classifier
json_file = open('/Users/stejasmunees/Desktop/Trained Models/zari/taneira_01.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
classifier_zari = model_from_json(loaded_model_json)
# load weights into new model
classifier_zari.load_weights('/Users/stejasmunees/Desktop/Trained Models/zari/taneira_01.h5')
print("Loaded model from disk")

############################## Zari Subplot classifier #################

import PIL
image_list={}
image_dat={}
i=0
mob='/Users/stejasmunees/Desktop/test/zari'
mob_dir=os.listdir(mob)
for moby in mob_dir:
    if moby[0]!='.':
        image_list[i+1]=mob+'/'+moby
        image_dat[i+1]=PIL.Image.open(mob+'/'+moby)
        i+=1

from keras.preprocessing import image

zari_class={}
zari_prob={}
file_list={}

i=0

old_source='/Users/stejasmunees/Desktop/test/zari'
old_source_dir=os.listdir(old_source)
new_source='/Users/stejasmunees/Desktop/test/compressed/zari'


for files in os.listdir(new_source):
    os.unlink(new_source+'/'+files)

#var=input("Is the source image(s) compressed? \n")
#if(str.lower(var)=='no'):
#    compress(old_source,old_source_dir,new_source)
#else:
#    copy(old_source,old_source_dir,new_source)

copy(old_source,old_source_dir,new_source)
    
new_source_dir=os.listdir(new_source)

for files in new_source_dir:
    if files[0]!='.':
        i=i+1
        test_image_luna=image.load_img(new_source+'/'+files,target_size=(64,64))
        test_image2=image.img_to_array(test_image_luna)/255.
        test_image2=np.expand_dims(test_image2,axis=0)
        zari_prob[i]=classifier_zari.predict_proba(test_image2)[0]
        zari_class[i]=classifier_zari.predict_classes(test_image2)[0]
        file_list[i]=files
        

zari_eng=['No Zari','Zari Present']
pallu_eng=['Contrast','Running']
def display_images(img_list, cmap='gray', cols = 2, fig_size = (50, 50) ):
    """
    Display images in img_list
    """

#    plt.figure(figsize=fig_size)     
    
    f, axarr = plt.subplots(3,2)
    axarr[0,0].imshow(image_dat[1])
    axarr[0,0].title.set_text('Database: Zari Present,\n Prediction: '+zari_eng[zari_class[1]])
    axarr[0,1].imshow(image_dat[2])
    axarr[0,1].title.set_text('Database: Zari Present,\n Prediction: '+zari_eng[zari_class[2]])
    axarr[1,0].imshow(image_dat[3])
    axarr[1,0].title.set_text('Database: Zari Present,\n Prediction: '+zari_eng[zari_class[3]])
    axarr[1,1].imshow(image_dat[4])
    axarr[1,1].title.set_text('Database: Zari Present,\n Prediction: '+zari_eng[zari_class[4]])
    axarr[2,0].imshow(image_dat[5])
    axarr[2,0].title.set_text('Database: No Zari,\n Prediction: '+zari_eng[zari_class[5]])
    axarr[2,1].imshow(image_dat[6])
    axarr[2,1].title.set_text('Database: Zari Present,\n Prediction: '+zari_eng[zari_class[6]])
    
    f.suptitle('Testing Zari')
    plt.show()
    
display_images(image_list)

############################## Pallu Subplot classifier #################

import PIL
image_list={}
image_dat={}
i=0
mob='/Users/stejasmunees/Desktop/test/running'
mob_dir=os.listdir(mob)
for moby in mob_dir:
    if moby[0]!='.':
        image_list[i+1]=mob+'/'+moby
        image_dat[i+1]=PIL.Image.open(mob+'/'+moby)
        i+=1

from keras.preprocessing import image

pallu_class={}
pallu_prob={}
file_list={}

i=0

old_source='/Users/stejasmunees/Desktop/test/running'
old_source_dir=os.listdir(old_source)
new_source='/Users/stejasmunees/Desktop/test/compressed/running'


for files in os.listdir(new_source):
    os.unlink(new_source+'/'+files)

#var=input("Is the source image(s) compressed? \n")
#if(str.lower(var)=='no'):
#    compress(old_source,old_source_dir,new_source)
#else:
#    copy(old_source,old_source_dir,new_source)

copy(old_source,old_source_dir,new_source)
    
new_source_dir=os.listdir(new_source)

for files in new_source_dir:
    if files[0]!='.':
        i=i+1
        test_image_luna=image.load_img(new_source+'/'+files,target_size=(64,64))
        test_image2=image.img_to_array(test_image_luna)/255.
        test_image2=np.expand_dims(test_image2,axis=0)
        pallu_prob[i]=classifier_pallu.predict_proba(test_image2)[0]
        pallu_class[i]=classifier_pallu.predict_classes(test_image2)[0]
        file_list[i]=files
        

zari_eng=['No Zari','Zari Present']
pallu_eng=['Contrast','Running']
def display_images_pallu(img_list, cmap='gray', cols = 2, fig_size = (50, 50) ):
    """
    Display images in img_list
    """

#    plt.figure(figsize=fig_size)     
    
    f, axarr = plt.subplots(3,2)
    axarr[0,0].imshow(image_dat[1])
    axarr[0,0].title.set_text('Database: Running Pallu,\n Prediction: '+pallu_eng[pallu_class[1]])
    axarr[0,1].imshow(image_dat[2])
    axarr[0,1].title.set_text('Database: Running Pallu,\n Prediction: '+pallu_eng[pallu_class[2]])
    axarr[1,0].imshow(image_dat[3])
    axarr[1,0].title.set_text('Database: Contrast Pallu,\n Prediction: '+pallu_eng[pallu_class[3]])
    axarr[1,1].imshow(image_dat[4])
    axarr[1,1].title.set_text('Database: Running Pallu,\n Prediction: '+pallu_eng[pallu_class[4]])
    axarr[2,0].imshow(image_dat[5])
    axarr[2,0].title.set_text('Database: Contrast Pallu,\n Prediction: '+pallu_eng[pallu_class[5]])
    axarr[2,1].imshow(image_dat[6])
    axarr[2,1].title.set_text('Database: Running Pallu,\n Prediction: '+pallu_eng[pallu_class[6]])
    
    f.suptitle('Testing Pallu')
    plt.show()
    
display_images_pallu(image_list)

################# Mobile Directory, Live Recommendations ######################

from keras.preprocessing import image

zari_class={}
zari_prob={}
pallu_class={}
pallu_prob={}
file_list={}
i=0

mob='/Users/stejasmunees/Desktop/test/mobile_dir'
mob_dir=os.listdir(mob)
new_src='/Users/stejasmunees/Desktop/test/compressed/mobile'
for files in os.listdir(new_src):
    os.unlink(new_src+'/'+files)

var=input("Is the source image(s) compressed? \n")
if(str.lower(var)=='no'):
    compress(mob,mob_dir,new_src)
else:
    copy(mob,mob_dir,new_src)

#compress(mob,mob_dir,new_src)
    
new_src_dir=os.listdir(new_src)
filename=new_src_dir[0]
filename=filename.split('_')[0]

for files in new_src_dir:
    if files[0]!='.':
        i=i+1
        test_image_luna=image.load_img(new_src+'/'+files,target_size=(64,64))
        test_image2=image.img_to_array(test_image_luna)/255.
        test_image2=np.expand_dims(test_image2,axis=0)
        zari_prob[i]=classifier_zari.predict_proba(test_image2)[0]
        zari_class[i]=classifier_zari.predict_classes(test_image2)[0]
        pallu_prob[i]=classifier_pallu.predict_proba(test_image2)[0]
        pallu_class[i]=classifier_pallu.predict_classes(test_image2)[0]
        file_list[i]=files

try:
    color=int(input("Please enter the option for base colour as below, \n"
            "01. Beige \n"
            "02. Black \n"
            "03. Blue \n"
            "04. Brown \n"
            "05. Gold \n"
            "06. Green \n"
            "07. Grey \n"
            "08. Orange \n"
            "09. Red \n"
            "10. Violet \n"
            "11. Yellow \n\n"
            ))
    if (color>11):
        raise Exception('Please enter an integer less than 11')
except ValueError:
    #Handle the exception
    print ('Please enter a valid option')
    
colour_list={
        1: 'Beige',
        2: 'Black',
        3: 'Blue',
        4: 'Brown',
        5: 'Gold',
        6: 'Green',
        7: 'Grey',
        8: 'Orange',
        9: 'Red',
        10: 'Violet',
        11: 'Yellow'}

sim=0;
sim_index={}
indices={}
pallu_eng=['Contrast','Running']

for index in range(len(sku)):
    if (base_colour[index]==colour_list[color]):
        if (pallu_pattern[index]==pallu_eng[pallu_class[1]]):
            if (zari[index] == "Tested" or zari[index] == "Pure" or zari[index] == "Faux"):
                if (zari_class[1]==1):
                    if(sku[index]!=filename):
                        sim_index[sim+1]=sku[index]
                        indices[sim+1]=index
                        sim+=1
            if (zari[index]=="NIL"):
                if (zari_class[1]==0):
                    if(sku[index]!=filename):
                        sim_index[sim+1]=sku[index]
                        indices[sim+1]=index
                        sim+=1
    if(sim>=30):
        break

all_files_dup='/Volumes/Samsung_T5/Files/allinoneplace_min'
all_files_dup_dir=os.listdir(all_files_dup)

import PIL
image_list={}
image_dat={}
sku_id={}
i=0

for file in new_src_dir:
    if file[0]!='.':
        image_list[i]=new_src+'/'+file
        image_dat[i]=PIL.Image.open(new_src+'/'+file)
flag=0
for lol in sim_index:
    for rofl in all_files_dup_dir:
        if rofl[0]!='.':
            for repeats in sku_id:
                if (sku_id[repeats]==rofl[0:len(sim_index[lol])]):
                    flag=1
            if (flag!=1):
                if (sim_index[lol]==rofl[0:len(sim_index[lol])]):
                    sku_id[i+1]=rofl[0:len(sim_index[lol])]
                    image_list[i+1]=all_files_dup+'/'+rofl
                    image_dat[i+1]=PIL.Image.open(all_files_dup+'/'+rofl)
                    i+=1
            flag=0

def display_images_sim(img_list, cmap='gray', cols = 2, fig_size = (50, 50) ):
    """
    Display images in img_list
    """

#    plt.figure(figsize=fig_size)
    f, axarr = plt.subplots(4,3)
#    plt.title("Similar Sarees", fontdict=None, loc='center', pad=None)
#    axarr.canvas.set_window_title('Window Title')
    zari_engg=['no zari','zari']
    pallu_engg=['contrast','running']
    
    axarr[0,0].imshow(img_list[0])
    axarr[0,0].title.set_text('Original Image (Taneira Product) \nIt has '+zari_engg[zari_class[1]]+' and has '+pallu_engg[pallu_class[1]]+' pallu')
    axarr[1,0].imshow(img_list[1])
    axarr[1,0].title.set_text('SKU: '+sku_id[1])
    axarr[1,1].imshow(img_list[2])
    axarr[1,1].title.set_text('SKU: '+sku_id[2])
    axarr[1,2].imshow(img_list[3])
    axarr[1,2].title.set_text('SKU: '+sku_id[3])
    axarr[2,0].imshow(img_list[4])
    axarr[2,0].title.set_text('SKU: '+sku_id[4])
    axarr[2,1].imshow(img_list[5])
    axarr[2,1].title.set_text('SKU: '+sku_id[5])
    axarr[2,2].imshow(img_list[6])
    axarr[2,2].title.set_text('SKU: '+sku_id[6])
    axarr[3,0].imshow(img_list[7])
    axarr[3,0].title.set_text('SKU: '+sku_id[7])
    axarr[3,1].imshow(img_list[8])
    axarr[3,1].title.set_text('SKU: '+sku_id[8])
    axarr[3,2].imshow(img_list[9])
    axarr[3,2].title.set_text('SKU: '+sku_id[9])

    f.delaxes(axarr[0,1])
    f.delaxes(axarr[0,2])
    f.suptitle('Similar Sarees')
    plt.show()
    
display_images_sim(image_dat)


################# Non Taneira Live Recommendations ######################

from keras.preprocessing import image

zari_class={}
zari_prob={}
pallu_class={}
pallu_prob={}
file_list={}
i=0

mob='/Users/stejasmunees/Desktop/test/nontaneira'
mob_dir=os.listdir(mob)
new_src='/Users/stejasmunees/Desktop/test/compressed/nontan'
for files in os.listdir(new_src):
    os.unlink(new_src+'/'+files)

var=input("Is the source image(s) compressed? \n")
if(str.lower(var)=='no'):
    compress(mob,mob_dir,new_src)
else:
    copy(mob,mob_dir,new_src)

#compress(mob,mob_dir,new_src)
    
new_src_dir=os.listdir(new_src)
filename=new_src_dir[0]
filename=filename.split('_')[0]

for files in new_src_dir:
    if files[0]!='.':
        i=i+1
        test_image_luna=image.load_img(new_src+'/'+files,target_size=(64,64))
        test_image2=image.img_to_array(test_image_luna)/255.
        test_image2=np.expand_dims(test_image2,axis=0)
        zari_prob[i]=classifier_zari.predict_proba(test_image2)[0]
        zari_class[i]=classifier_zari.predict_classes(test_image2)[0]
        pallu_prob[i]=classifier_pallu.predict_proba(test_image2)[0]
        pallu_class[i]=classifier_pallu.predict_classes(test_image2)[0]
        file_list[i]=files

try:
    color=int(input("Please enter the option for base colour as below, \n"
            "01. Beige \n"
            "02. Black \n"
            "03. Blue \n"
            "04. Brown \n"
            "05. Gold \n"
            "06. Green \n"
            "07. Grey \n"
            "08. Orange \n"
            "09. Red \n"
            "10. Violet \n"
            "11. Yellow \n"
            "12. Pink \n\n"
            ))
    if (color>12):
        raise Exception('Please enter an integer less than 11')
except ValueError:
    #Handle the exception
    print ('Please enter a valid option')
    
colour_list={
        1: 'Beige',
        2: 'Black',
        3: 'Blue',
        4: 'Brown',
        5: 'Gold',
        6: 'Green',
        7: 'Grey',
        8: 'Orange',
        9: 'Red',
        10: 'Violet',
        11: 'Yellow',
        12: 'Pink'}

sim=0;
sim_index={}
indices={}
pallu_eng=['Contrast','Running']
flag=0

for index in range(len(sku)):
    if (base_colour[index]==colour_list[color]):
        if (pallu_pattern[index]==pallu_eng[pallu_class[1]]):
            if (zari[index] == "Tested" or zari[index] == "Pure" or zari[index] == "Faux"):
                if (zari_class[1]==1):
                    if(sku[index]!=filename):
                        for repeats in sim_index:
                            if (sim_index[repeats]==sku[index]):
                                flag=1
                        if (flag!=1):
                            sim_index[sim+1]=sku[index]
                            indices[sim+1]=index
                            sim+=1
                flag=0
            if (zari[index]=="NIL"):
                if (zari_class[1]==0):
                    if(sku[index]!=filename):
                        for repeats in sim_index:
                            if (sim_index[repeats]==sku[index]):
                                flag=1
                        if (flag!=1):
                            sim_index[sim+1]=sku[index]
                            indices[sim+1]=index
                            sim+=1
                flag=0
                            
    if(sim>=20):
        break

all_files_dup='/Volumes/Samsung_T5/Files/allinoneplace_min'
all_files_dup_dir=os.listdir(all_files_dup)

import PIL
image_list={}
image_dat={}
sku_id={}
i=0

for file in new_src_dir:
    if file[0]!='.':
        image_list[i]=new_src+'/'+file
        image_dat[i]=PIL.Image.open(new_src+'/'+file)
flag=0
for lol in sim_index:
    for rofl in all_files_dup_dir:
        if rofl[0]!='.':
            for repeats in sku_id:
                if (sku_id[repeats]==rofl[0:len(sim_index[lol])]):
                    flag=1
            if (rofl[0:len(sim_index[lol])]=="SHT03I00827"):
                flag=1
            if (flag!=1):
                if (sim_index[lol]==rofl[0:len(sim_index[lol])]):
                    sku_id[i+1]=rofl[0:len(sim_index[lol])]
                    image_list[i+1]=all_files_dup+'/'+rofl
                    image_dat[i+1]=PIL.Image.open(all_files_dup+'/'+rofl)
                    i+=1
            flag=0

def display_images_sim(img_list, cmap='gray', cols = 2, fig_size = (50, 50) ):
    """
    Display images in img_list
    """

#    plt.figure(figsize=fig_size)
    f, axarr = plt.subplots(4,3)
#    plt.title("Similar Sarees", fontdict=None, loc='center', pad=None)
#    axarr.canvas.set_window_title('Window Title')
    zari_engg=['no zari','zari']
    pallu_engg=['contrast','running']
    
    axarr[0,0].imshow(img_list[0])
    axarr[0,0].title.set_text('Original Image (Non-Taneira Product) \nIt has '+zari_engg[zari_class[1]]+' and has '+pallu_engg[pallu_class[1]]+' pallu')
    axarr[1,0].imshow(img_list[1])
    axarr[1,0].title.set_text('SKU: '+sku_id[1])
    axarr[1,1].imshow(img_list[2])
    axarr[1,1].title.set_text('SKU: '+sku_id[2])
    axarr[1,2].imshow(img_list[3])
    axarr[1,2].title.set_text('SKU: '+sku_id[3])
    axarr[2,0].imshow(img_list[4])
    axarr[2,0].title.set_text('SKU: '+sku_id[4])
    axarr[2,1].imshow(img_list[5])
    axarr[2,1].title.set_text('SKU: '+sku_id[5])
    axarr[2,2].imshow(img_list[6])
    axarr[2,2].title.set_text('SKU: '+sku_id[6])
    axarr[3,0].imshow(img_list[7])
    axarr[3,0].title.set_text('SKU: '+sku_id[7])
    axarr[3,1].imshow(img_list[8])
    axarr[3,1].title.set_text('SKU: '+sku_id[8])
    axarr[3,2].imshow(img_list[9])
    axarr[3,2].title.set_text('SKU: '+sku_id[9])

    f.delaxes(axarr[0,1])
    f.delaxes(axarr[0,2])
    f.suptitle('Similar Sarees')
    plt.show()
    
display_images_sim(image_dat)
    
#Zari
#0 No
#1 Yes
#
#Pallu
#0 Contrast
#1 Running

#for files in new_source_dir:
#    if files[0]!='.':
#        i=i+1
#        test_image_luna=image.load_img(new_source+'/'+files,target_size=(64,64))
#        test_image2=image.img_to_array(test_image_luna)/255.
#        test_image2=np.expand_dims(test_image2,axis=0)
#        zari_prob[i]=classifier_pallu.predict_proba(test_image2)[0]mem
#        zari_class[i]=classifier_pallu.predict_classes(test_image2)[0]
#        file_list[i]=files
    
    
    
    
#    /Volumes/Samsung_T5/Files/pics_in_excel