#Generate train.txt file for darknet yolov3 model training from directory of annotation files

from os import listdir

files = listdir("C:/Users/Shahzaib/Desktop/yolo/darknet/build/darknet/x64/data/mylabels/") #folder containing .txt annotation files
path_from_root = "build/darknet/x64/data/obj/" #path of folder containing images
image_type = "jpg" 

#Change above fields as required

f = open("train.txt", "w+")
for file in files:
        ending = file[:-3]
        f.write(path_from_root+ending+image_type+"\n")