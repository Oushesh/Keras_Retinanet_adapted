## Instructions:
   * git clone https://github.com/Oushesh/Keras_Retinanet_adapted
   * pip install . --user
   * python setup.py build_ext --inplace
   * pip install --user git+https://github.com/cocodataset/cocoapi.git#subdirectory=PythonAPI
   * cd keras-retinanet/
   * pip install .
   * python setup.py build_ext --inplace

## Train:
    python keras_retinanet/bin/train.py --freeze-backbone --random-transform --weights keras_retinanet/model/resnet50_coco_best_v2.1.0.h5 --batch-size 8 --steps 500 --epochs 1 csv keras_retinanet/preprocessing/annotations.csv keras_retinanet/preprocessing/classes.csv



## Test:
   * Place the pretrained model in the folder model
   * Each column contains the name of the folder:    
   * Place the batch image in the folder: input_img
   * classes.csv contains the class definition and class number.
     example:
     classID, 0
     classID, 1
     classID, 2
     classID, 3

   * python keras-retinanet/retinanet_coco_keras_test.py
   * The output image will be written in the folder of the output_img


## Rebuild and structure the code with dependencies.

## Next test this: https://github.com/ZFTurbo/Keras-RetinaNet-for-Open-Images-Challenge-2018
   Kaggle Comptetition for opensource.

## TODO: add visualisation service to service.

* Deploy to ec2 instance and train.
