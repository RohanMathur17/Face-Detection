# Face-Detection

This repository contains source code for a simple face detection project that is made over OpenCV's built in module known as ```dnn```, which stands for deep neural networks. It is built upon a number of deep learning frameworks, including Caffe, TensorFlow, and PyTorch.

The pre built models & resources for this can be found [here](https://github.com/opencv/opencv/tree/master/samples/dnn) or [within this repository](https://github.com/RohanMathur17/Face-Detection/tree/main/cv-models)

## Using Images

Here is how the model performed for a sample input image

<img src = "https://github.com/RohanMathur17/Face-Detection/blob/main/images/harry-modelled.jpeg">

## Using Video

Here is how the model performed when using own video

<img src = "https://github.com/RohanMathur17/Face-Detection/blob/main/images/rohan-video-modelled.jpeg">


## How to run 

* Clone the repository in your local machine

```
 git clone https://github.com/RohanMathur17/Face-Detection.git
 ```
 
 * Change your current directory
 ```
 cd Your-Path\Face-Detection
 ```
 
 * Use a virtual environment before proceeding. Install it using
 ```
 pip install virtualenv
 ```
 
 * Install requirements.txt using pip
 ```
 pip install -r requirements.txt
 ```
 
 * To run your & test on your own sample image, put it under the directory of Face-Detection/images, after that using argument parsing specify the paths for the required files
 ```
 python face-detect-image.py --image images\harry.jpeg --prototxt cv-models\deploy.prototxt.txt --model cv-models\res10_300x300_ssd_iter_140000.caffemodel
 ```
 
 * Similarly, for running on your own video, run face-detect-video.py
 ```
python face-detect-video.py --prototxt cv-models\deploy.prototxt.txt --model cv-models\res10_300x300_ssd_iter_140000.caffemodel
 ```
