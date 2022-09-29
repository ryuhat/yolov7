import glob
import random
import os
import subprocess
import shutil
import sys
import re

#python create_yolo_format.py [path]

obj = sys.argv[1]
#  "D:\dev\rush_swimming\annotated\1008\1008_2_1\obj_train_data"
# parent = 'C:\\Users\\ryuki\\Desktop\\rush_swimming\\annotated\\'
parent = obj  #.rstrip('22')
# obj = parent + '1008\\1008_2\\obj_train_data'
filelist  = glob.glob(obj +'/*.txt')

# dir = 'dataset_1008_2'
dir = sys.argv[2]
# +re.sub(r'[^0-9]', '', obj)
# dir = dir[9:]
# .rstrip('obj_train_data')

test_images = os.makedirs(dir+'/test/'+'images', exist_ok=True) 
test_labels = os.makedirs(dir+'/test/'+'labels', exist_ok=True) 
train_images = os.makedirs(dir+'/train/'+'images', exist_ok=True) 
train_labels = os.makedirs(dir+'/train/'+'labels', exist_ok=True) 
val_images = os.makedirs(dir+'/val/'+'images', exist_ok=True) 
val_labels = os.makedirs(dir+'/val/'+'labels', exist_ok=True) 

with open(dir+'/data.yaml', 'w') as f:
    f.write('train: ./'+dir+'/train/'+'images\n')
    f.write('val: ./'+dir+'/val/'+'images\n\n')
    f.write('nc: 1\nnames: [\'tuna\']')

# test_path = dir+'/test/'
train_path = dir+'/train/'
val_path = dir+'/val/' 

list_path = [train_path, val_path]

for output_path in list_path:
    if output_path == train_path:
        train = random.sample(filelist, int(len(filelist)*0.9))
        data = train
    if output_path == val_path:
        val = filelist
        data = val
    
    for file in data:
        txtpath = file
        impath = file[:-4] + '.PNG'
        out_text = os.path.join(output_path + '/labels/', os.path.basename(txtpath))
        out_image = os.path.join(output_path + '/images/', os.path.basename(impath))
        print(txtpath,impath,out_text,out_image)
        shutil.move(txtpath, out_text)
        shutil.move(impath, out_image)
        filelist  = glob.glob(obj +'/*.txt')