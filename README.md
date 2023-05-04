#### git clone repo

    git clone https://github.com/LibraryDetection/data_analysis.git

#### go to yolov5 folder

    cd data_analysis/build_model/yolov5

#### installation

    pip install -r requirements.txt

#### train custom model

    python train.py --img 416 --batch 16 --epochs 15 --data dataset.yaml --weights yolov5s.pt --name library_detection_yolov5s_result

---

#### reference

- In build_model folder
  - dataset(images,labels,tests) is in the dataset folder
  - build_model_using_colab : when you want to build the model in google Colab, you can use this code
  - label_problem_solving : you can use it when you want to detect some errors in dataset
- In model_testing folder
  - This is the folder and jupyter notebook file which I used to test the model. You can add weights on model_testing/yolov5/runs/train/exp()/weights/, and then change the code in model_testing.ipynb file
- object_detection_refcode : You can refer to this code when you try to add objects only what we need (ex. backpack, book ...). Please note that the code is not yet completed
