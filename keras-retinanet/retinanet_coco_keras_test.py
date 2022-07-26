import os
import keras
import tensorflow as tf
import keras_retinanet

from keras_retinanet import models
from keras_retinanet.utils.image import read_image_bgr, preprocess_image, resize_image
from keras_retinanet.utils.visualization import draw_box, draw_caption
from keras_retinanet.utils.colors import label_color

from keras_retinanet.utils.image import read_image_bgr, preprocess_image, resize_image
from keras_retinanet.utils.visualization import draw_box, draw_caption
from keras_retinanet.utils.colors import label_color
import matplotlib.pyplot as plt
import cv2
import os
import time
import pandas
from collections import deque
import numpy as np
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--img_dir',default='input_img',help='path to image directory')
    parser.add_argument('--model_path', default=os.path.join("pretrained_model","resnet50_coco_best_v2.1.0.h5"),help='path to load pretrained retinanet Keras model')
    #parser.add_argument('--annotations_file',default=os.path.join("annotations_classes","annotations.csv"),help='path to the annotations file')
    parser.add_argument('--annotations_file',default="annotations_classes/annotations.csv",help='path to the annotations file')

    #parser.add_argument('--classes_file',default=os.path.join("annotations_classes","classes.csv"),help='path to the class dictionary')
    parser.add_argument('--classes_file',default="annotations_classes/classes.csv",help='path to the class dictionary')

    parser.add_argument('--threshold_score',default=0.8,help="threshold for the detection")
    parser.add_argument('--output_img_dir',default='output_img',help='path to output img dir')
    args = parser.parse_args()
    return args


def get_session():
    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True
    return tf.Session(config=config)

#TODO: add support for file splitting in linux as well
def get_img_name(url):
    if url.endswith(".jpg"):
        img_name = url.split("\\")[-1].split(".jpg")[0]
    elif url.endswith(".jpeg"):
        img_name = url.split("\\")[-1].split(".jpeg")[0]
    elif url.endswith(".png"):
        img_name = url.split("\\")[-1].split(".png")[0]
    else:
        img_name = None
    return img_name

def img_inference(img_path,output_img_path,threshold_score):
    img_name = get_img_name(img_path)
    print ("img_name",img_name)
    assert (not img_name==None)

    image = read_image_bgr(img_path)
    # copy to draw on
    draw = image.copy()
    draw = cv2.cvtColor(draw, cv2.COLOR_BGR2RGB)
    # preprocess image for network
    image = preprocess_image(image)
    image, scale = resize_image(image)
    # process image
    start = time.time()
    boxes, scores, labels = model.predict_on_batch(np.expand_dims(image, axis=0))
    print("processing time: ", time.time() - start)
    # correct for image scale
    boxes /= scale
    # visualize detections
    for box, score, label in zip(boxes[0], scores[0], labels[0]):
        # scores are sorted so we can break
        if score < threshold_score:
            break
        color = label_color(label)
        b = box.astype(int)
        draw_box(draw, b, color=color)
        print ("labels",labels)
        #Test the dictionary:
        print ("labels_to_names dictionary", labels_to_names)
        #caption = "{} {:.3f}".format(labels_to_names[label], score)
        caption = "{} {:.3f}".format(label, score)
        draw_caption(draw, b, caption)
        print (os.path.join(output_img_path,img_name+"_output.png"))
        cv2.imwrite(os.path.join(output_img_path,img_name+"_output.png"),draw)
        return draw

#Add the path where the images are going to be downloaded here:
def img_dataloader(dir):
    img_paths = deque()
    for root,directory,folders in os.walk(dir):
        for files in folders:
            if files.endswith(".jpg") or files.endswith(".png") or files.endswith(".jpeg"):
                img_paths.append(os.path.join(root,files))
    return img_paths

if __name__ == "__main__":
    args = parse_args()
    model_path = args.model_path
    classes_file = args.classes_file
    annotations_file = args.annotations_file
    img_urls = img_dataloader(args.img_dir)
    output_img_dir = args.output_img_dir
    threshold_score = args.threshold_score

    # load label to names mapping for visualization purposes
    labels_to_names = pandas.read_csv(classes_file,header=None).T.loc[0].to_dict()

    # load retinanet model
    model = models.load_model(model_path, backbone_name='resnet50')

    for url in img_urls:
        print ('img_url',url)
        img_inference(url,output_img_dir,threshold_score)


"""
#TODO:
add support for other backbones as well
Change from .xml to .json file
add .yml file for configuration
add support for CPU or GPU os.environ["CUDA_VISIBLE_DEVICES"]
"""
