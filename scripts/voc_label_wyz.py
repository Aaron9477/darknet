import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

# sets=[('2012', 'train'), ('2012', 'val'), ('2007', 'train'), ('2007', 'val'), ('2007', 'test')]
sets = ['train', 'val']
dataset_dir = '/media/zq610/2C9BDE0469DC4DFC/ubuntu/dl_dataset/turtlebot/VOC_type/turtlebot_test2'
classes = ["t", "car"]
dataset_name = 'turtlebot'

def convert(size, box):
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def convert_annotation(image_id):
    in_file = open('%s/Annotations/%s.xml'%(dataset_dir, image_id))
    out_file = open('%s/labels/%s.txt'%(dataset_dir, image_id), 'w')
    tree=ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

# return the current dir
wd = getcwd()

for image_set in sets:
    if not os.path.exists(dataset_dir):
        raise IOError('There is no dataset!!')
        # os.makedirs('VOCdevkit/VOC%s/labels/'%(year))
    if not os.path.exists('%s/labels'%dataset_dir):
        os.makedirs('%s/labels'%dataset_dir)
    image_ids = open('%s/ImageSets/Main/%s.txt'%(dataset_dir, image_set)).read().strip().split()
    list_file = open('%s_%s.txt'%(dataset_name, image_set), 'w')
    for image_id in image_ids:
        list_file.write('%s/JPEGImages/%s.jpg\n'%(dataset_dir, image_id))
        convert_annotation(image_id)
    list_file.close()

os.system("cat %s_train.txt %s_val.txt > train.txt"%(dataset_name, dataset_name))
# os.system("cat %s_train.txt %s_val.txt 2007_test.txt 2012_train.txt 2012_val.txt > train.all.txt")

