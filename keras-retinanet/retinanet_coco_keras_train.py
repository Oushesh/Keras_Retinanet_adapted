"""
python keras_retinanet/bin/train.py --freeze-backbone --random-transform --weights keras_retinanet/snapshots/resnet50_coco_best_v2.1.0.h5 --batch-size 8 --steps 500 --epochs 1 csv keras_retinanet/preprocessing/annotations_bathtub.csv keras_retinanet/preprocessing/classes_bathroom_corrected.csv

Next step: deploy ec2 instance and run the training on it.
conda activate zind 
"""
