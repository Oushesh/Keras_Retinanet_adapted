## Instructions:
   * conda env create -f retinanet.yml
   * pip install -r requirements.txt
   * pip install . --user
   * python setup.py build_ext --inplace
   * pip install --user git+https://github.com/cocodataset/cocoapi.git#subdirectory=PythonAPI
   * cd keras-retinanet/
   * pip install .
   * python setup.py build_ext --inplace

## Dataset Preparation + Preprocessing:
    * For the use case of open images dataset Download or Copy the folder (from the google drive or s3 and place it under keras_retinanet)
    ├── keras_retinanet
    ├── └── ...
    ├── └── Bathtub (example category class)
    * The folder should ideally contain test,train, validation and info.json
    * cd keras_retinanet/preprocessing (oid:open images dataset)

      python run preprocess_oid.py to get the

## Train:
    * Download the model from here: https://s3.console.aws.amazon.com/s3/upload/machine-learning-pretrained-models-dev?region=eu-central-1&prefix=Keras-Retina-Net/ and put it the folder snapshots
    then run:

    python keras_retinanet/bin/train.py --freeze-backbone --random-transform --weights keras_retinanet/snapshots/resnet50_coco_best_v2.1.0.h5 --batch-size 8 --steps 500 --epochs 1 csv keras_retinanet/preprocessing/annotations_bathtub_corrected.csv keras_retinanet/preprocessing/classes_bathroom_corrected.csv

## Test:
   * Place the pretrained model in the folder "pretrained model" and run: python retinanet_coco_keras_test.py


   * Each column contains the name of the folder:    
   * Place the batch image in the folder: input_img
   * classes.csv contains the class definition and class number.
     example:
     classID, 0
     classID, 1
     classID, 2
     classID, 3

   * cd keras-retinanet
   * 
   * The output image will be written in the folder of the "output_img"

## Sample Test Results are:
   "C:\Users\oushe\Documents\WORKSPACE\RealEstate\Concular\Keras_Retinanet_adapted\keras-retinanet\keras_retinanet\Bathtub\test\Results"

## Rebuild and structure the code with dependencies.

## Next test this: https://github.com/ZFTurbo/Keras-RetinaNet-for-Open-Images-Challenge-2018
   Kaggle Comptetition for opensource.

## TODO: add visualisation service to service.
* Deployed to aws and train
* https://storage.googleapis.com/openimages/challenge_2018/bbox_labels_500_hierarchy_visualizer/circle.html
* Build in the hierarchy circle

## Sample Results of the Bahtroom Tubs:
  ![Bathroom001](keras_retinanet/Bathtub/test/Results/2cb84e34527db533_output_Bathroom accessory.jpg)

## inspiration: https://nn-box.com/box/
