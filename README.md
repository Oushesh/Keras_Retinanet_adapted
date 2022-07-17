## Instructions:
   * git clone https://github.com/Oushesh/Keras_Retinanet_adapted
   * pip install . --user
   * python setup.py build_ext --inplace
   * pip install --user git+https://github.com/cocodataset/cocoapi.git#subdirectory=PythonAPI
   * cd keras-retinanet/
   * pip install .
   * python setup.py build_ext --inplace
   *

## Test:
   * Place the pretrained model in the folder model
   * Place the batch image in the folder: input_img
   * python keras-retinanet/retinanet_coco_keras_test.py
   * The output image will be written in the folder of the output_img
   * 

## TODO: add the github reinanet.py get the output

## Rebuild and structure the code with dependencies.

## Next test this: https://github.com/ZFTurbo/Keras-RetinaNet-for-Open-Images-Challenge-2018
   Kaggle Comptetition for opensource.

## TODO: add visualisation service to service.

* Deploy to ec2 instance and train.
