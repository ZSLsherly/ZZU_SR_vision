import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

sets=[('2024', 'train')]

classes = ["biscuit","chip","cookie","handwash","dishsoap","water","sprite","cola","orange juice"]


wd = getcwd()

for year, image_set in sets:
    if not os.path.exists('/home/srobot/darknet-cyj/OurData/VOC%s/labels/'%(year)):
        os.makedirs('/home/srobot/darknet-cyj/OurData/VOC%s/labels/'%(year))
    image_ids = open('/home/srobot/darknet-cyj/OurData/VOC%s/ImageSets/Main/%s.txt'%(year, image_set)).read().strip().split()
    list_file = open('%s_%s.txt'%(year, image_set), 'w')
    for image_id in image_ids:
        list_file.write('/home/srobot/darknet-cyj/OurData/VOC%s/JPEGImages/%s.png\n'%( year, image_id))
        # convert_annotation(year, image_id)
    list_file.close()

os.system("cat 2024_train.txt 2024_train.txt> train.txt")
# os.system("cat 2024_train.txt 2024_val.txt 2024_test.txt 2024_train.txt 2024_val.txt > train.all.txt")
