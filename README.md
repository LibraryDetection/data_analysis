### Train model

#### git clone repo

    git clone https://github.com/LibraryDetection/data_analysis.git

#### go to build_model folder

    cd data_analysis/build_model

#### clone yolov5

    git clone https://github.com/ultralytics/yolov5.git

#### installation

    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

#### dataset.yaml

    move dataset.yaml file into yolov5 folder

#### go to yolov5 folder

    cd yolov5

#### installation

    pip install -r requirements.txt

#### train custom model

    python train.py --img 416 --batch 16 --epochs 15 --data dataset.yaml --weights yolov5s.pt --name library_detection_yolov5s_result

---

### Test model

#### go to model_testing folder

    cd data_analysis/model_testing

#### git clone yolov5

    git clone https://github.com/ultralytics/yolov5.git

#### go to yolov5 folder

    cd yolov5

#### make weight folder

    mkdir runs/train/exp(number)/weights

#### copy weight file (ex.best.pt) in yolov5/runs/train/exp(number)/weights folder. you can use the best15.pt (15epoch training) file and best66.pt (66epoch training) file.

#### change the code in model_testing.ipynb file to use the weight file to test the model

---

### reference

- In build_model folder
  - dataset(images,labels,tests) is in the dataset folder
  - build_model_using_colab : when you want to build the model in google Colab, you can use this code
  - label_problem_solving : you can use it when you want to detect some errors in dataset<br>
- In model_testing folder
  - This is the folder and jupyter notebook file which I used to test the model.
  - You can add more weights on model_testing/yolov5/runs/train/exp(change number)/weights/, and then change the code in model_testing.ipynb file<br>
- object_detection_refcode : You can refer to this code when you try to add objects only what we need (ex. backpack, book ...). Please note that the code is not yet completed
