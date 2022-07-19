"""
Input: classes.csv containing encryptedstringID, classname
Output: class_dict
"""

import numpy as np
from PIL import Image
from six import raise_from
import cv2
import csv
import sys
import os.path
from collections import OrderedDict,deque

def _get_classes(classess_csv_path):
    class_dict = {}
    # opening the CSV file
    with open(classes_csv_path, mode ='r')as file:
      # reading the CSV file
      csvFile = csv.reader(file)
      # displaying the contents of the CSV file
      for lines in csvFile:
            #print(lines)
            try:
                encryptedID = lines[0]
                classID = lines[1]
                #Add the information to the dictionary:
                if encryptedID not in class_dict:
                    class_dict[encryptedID]=classID
            except ValueError:
                raise_from(ValueError('line {}: format should be \'encryptedID,classID\''.format(lines)), None)
    return class_dict

#Build the annotations_bathtub.csv (here as a test:)
#Build it in the same format:
def img_dataloader(dir):
    img_paths = deque()
    for root,directory,folders in os.walk(dir):
        for files in folders:
            if files.endswith(".jpg") or files.endswith(".png") or files.endswith(".jpeg"):
                img_paths.append(os.path.join(root,files))
    return img_paths

def get_imgname(url):
    img_name = url.split("/")
    return img_name

#CSV writer:
#Write all the entries to csv format.

def write_out_annotations_csv(csv_filename,data):
    with open(csv_filename, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        # write the header
        #writer.writerow(header)
        # write multiple rows
        writer.writerows(data)
    return None



def _get_xy(detections_csv_path,class_dict,img_folder):
    #opening the csv file:
    csv_file_entries = []
    visited_ImageID = []
    #img_url from the present images
    img_urls = img_dataloader(img_folder)
    img_name_urls = [i.split("/")[-1] for i in img_urls]
    img_name_urls = [i.split("\\")[-1] for i in img_name_urls]
    img_name_urls = [i.split(".")[0] for i in img_name_urls]

    assert (len(img_urls)==len(img_name_urls))

    print (img_name_urls)
    with open(detections_csv_path,mode="r") as file:
        # reading the csv file
        csvFile = csv.reader(file)
        # displaying the contents of the csv file

        for lines in csvFile:
            csv_line = []
            try:
                ImageID=lines[0]
                Source=lines[1]
                LabelName=lines[2]
                Confidence=lines[3]
                XMin=lines[4]
                XMax=lines[5]
                YMin=lines[6]
                YMax=lines[7]
                IsOccluded=lines[8]
                IsTruncated=lines[9]
                IsGroupOf=lines[10]
                IsDepiction=lines[11]
                IsInside=lines[12]

                if ImageID in img_name_urls:
                    idx = img_name_urls.index(ImageID)
                    img = cv2.imread(img_urls[idx])

                    h,w,c = img.shape

                    x1 = int(float(XMin)*int(w))
                    y1 = int(float(YMin)*int(h))
                    x2 = int(float(XMax)*int(w))
                    y2 = int(float(YMax)*int(h))

                    start_point = (x1,y1)
                    end_point = (x2,y2)
                    class_name = class_dict[LabelName]
                    print ("img_url",img_urls[idx],"start_point",start_point,"end_point",end_point,"class Name",class_name)

                    #Write the rectangle output
                    #Write out the image_output with its corresponding:

                    color = (255, 0, 0)
                    thickness = 2
                    img = cv2.rectangle(img,start_point,end_point,color,thickness)
                    output_path  = img_urls[idx].split(".jpg")[0]+"_output_"+str(class_name)+".jpg"  #Add support for other img types here as well
                    cv2.imwrite(output_path,img)

                    #write the annotations_csv in the desired format.
                    csv_line.append(img_urls[idx])
                    csv_line.append(x1)
                    csv_line.append(y1)
                    csv_line.append(x2)
                    csv_line.append(y2)
                    csv_line.append(class_name)

                    csv_file_entries.append(csv_line)
            except ValueError:
                raise_from(ValueError('line {}: format should be \'encryptedID,classID\''.format(lines)),None)


            csv_line = []

    #"dataset/20190220_160752.jpg,202,10,640,476,goat"

    return csv_file_entries

if __name__ == '__main__':
    img_folder = "../Bathtub/test/data"
    classes_csv_path = "../Bathtub/test/metadata/classes.csv"

    class_dict = _get_classes(classes_csv_path)
    #print (class_dict)
    detection_csv_path = "../Bathtub/test/labels/detections.csv"

    csv_file_entries = _get_xy(detection_csv_path,class_dict,img_folder)

    print ("annotation_list",csv_file_entries)

    #write out to a specific csv file
    csv_filename = "annotations_bathtub.csv"
    #annotation_list is a list of list with each list representing a line entry in the csv file
    write_out_annotations_csv(csv_filename,csv_file_entries)

#TODO: Write csv, get 1 training iteration done --> git status
#Wrtie out the csv file --> Test out.
#
