import torch
from matplotlib import pyplot as plt
import numpy as np
import cv2
import os
# os.environ['KMP_DUPLICATE_LIB_OK']='True'

#cd yolov5 & pip install -r requirements.txt
#학습코드 : cd yolov5 & python train.py --img 416 --batch 16 --epochs 100 --data dataset.yaml --weights yolov5s.pt --name library_detection_yolov5s_result