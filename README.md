# Bangla-Spoken-Number-Recognition

## Table of content

- [Motivation](#motivation)
- [Introduction](#introduction)
- [Objectives](#objectives)
- [Quick Start Guide](#quick-starting-the-project)
- [Methodology](#methodology)
    - [Vehicle Classification](#vehicle-classification)
    - [Violation Detection](#violation-detection)
- [Implementation](#implementation)
    - [Computer Vision](#computer-vision)
    - [Graphical User Interface](#graphical-user-interface)
- [Contribution](#contribution)
- [Links and References](#links-and-references)
- [Author](#author)
- [Licensing](#licensing)

## Motivation
Speech is a very convenient way to interact with machines. At present, most features of the electronic devices are controlled through speech signals. Bangla speech based system lags behind in this human-machine interaction field. In order to create such speech controlled based systems, we first need to teach machines to recognize Bangla speech.

## Introduction
Speech recognition is a technique that converts human speech signals into text or words or in any form that can be easily understood by computers or other machines. There have been a few studies on Bangla digit recognition systems, the majority of which used small datasets with few variations in genders, ages, dialects, and other variables. Audio recordings of Bangladeshi people of various genders, ages, and dialects were used to create a large speech dataset of spoken '০-৯' Bangla digits in this study. Here, 400 noisy and noise-free samples per digit have been recorded for creating the dataset. Mel Frequency Cepstrum Coefficients (MFCCs) have been utilized for extracting meaningful features from the raw speech data. Then, to detect Bangla numeral digits, Convolutional Neural Networks (CNNs) were utilized. The suggested technique recognizes '০-৯' Bangla spoken digits with 97.1% accuracy throughout the whole dataset. The efficiency of the model was also assessed using 10-fold cross validation, which yielded a 96.7% accuracy.

## Objectives
Creating a human-machine interaction system for Bangla spoken numbers. In order to achieve that, extract meaningful features from the Bangla numerical speech data and measure the performance of recognizing bangla spoken digits from audio data.

## Quick Start Guide
1. clone this repo `https://github.com/PiasRoY/Bangla-Spoken-Number-Recognition.git`
2. collect our own developed dataset from here: `https://www.kaggle.com/piasroy/bangla-spoken-099-numbers`
3. copy all the folders labelled from "0-99" and paste them into the `Bangla_Spoken_Numbers` folder of this repo.
4. install required python dependencies from `requirements.txt`.
5. open and run `100_class_CNN.ipynb`.

## Methodology
### Vehicle Classification
From the given video footage, moving objects are detected. An object detection model YOLOv3 is used to classify those moving objects into respective classes. YOLOv3 is the third object detection algorithm in YOLO (You Only Look Once) family. It improved the accuracy with many tricks and is more capable of detecting objects. The classifier model is built with Darknet-53 architecture. Table-1 shows how the neural network architecture is designed. 

![Darknet Architecture](Images/Darknet-53.png)


### Violation detection

The vehicles are detected using YOLOv3 model. After detecting the vehicles, violation cases are checked. A traffic line is drawn over the road in the preview of the given video footage by the user. The line specifies that the traffic light is red. Violation happens if any vehicle crosses the traffic line in red state.

The detected objects have a green bounding box. If any vehicle passes the traffic light in red state, violation happens. After detecting violation, the bounding box around the vehicle becomes red.


## Implementation
### Computer Vision
OpenCV is an open source computer vision and machine learning software library which is used in this project for image processing purpose. Tensorflow is used for implementing the vehicle classifier with darknet-53. 


### Graphical User Interface (GUI)
The graphical user interface has all the options needed for the software. The software serves administration and other debugging purposes. We don’t need to edit code for any management. For example, if we need to open any video footage, we can do it with the Open item (Figure-2). 

![Figure 2](Images/Initial_View.jpg)

     Figure-2: Initial user interface view.

Primarily, for the start of the project usage, the administrator needs to open a video footage using ‘Open’ item that can be found under ‘File’ (Figure-2). The administrator can open any video footage from the storage files (Figure-3).

![Figure 3](Images/Open_Video.JPG)

     Figure-3: Opening a video footage from storage.

After opening a video footage from storage, the system will get a preview of the footage. The preview contains a frame from the given video footage. The preview is used to identify roads and draw a traffic line over the road. The traffic line drawn by administrator will act as a traffic signal line. To enable the line drawing feature, we need to select ‘Region of interest’ item from the ‘Analyze’ option (Figure-4). After that administrator will need to select two points to draw a line that specifies traffic signal.

![Figure 4](Images/Select_Region_of_Interest.jpg)

     Figure-4: Region of Interest (Drawing signal line)

Selecting the region of interest will start violation detection system. The coordinates of the line drawn will be shown on console (Figure-5). The violation detection system will start immediately after the line is drawn. At first the weights will be loaded. Then the system will detect objects and check for violations. The output will be shown frame by frame from the GUI (Figure-6). 

![Figure 5](Images/Line_Coordinates.JPG)

     Figure-5: Line Coordinates (from console)

![Figure 6](Images/Violation_Detection_Frame.jpg)

     Figure-6: Final Output (on each frame)

The system will show output until the last frame of the footage. In background a ‘output.mp4’ will be generated. The file will be in ‘output’ folder of ‘Resources’. The process will be immediately terminated by clicking ‘q’.

After processing a video footage, the administrator can add another video footage from the initial file manager (Figure-2). If the work is complete the administrator can quit using ‘Exit’ item from File option.


## Contribution
There aren't many open source project on speech recognition systems, specially on Bangla Language. Therefore, it will be helpful for those who want to work on speech recognition and create their own unique project. Good Luck to you and give a star to this repo. 👍

## Links and References
- M. Shuvo, S. A. Shahriyar, and M. Akhand, “Bangla numeral recognition from speech signal using convolutional neural network,” in 2019 International Conference on Bangla Speech and Language Processing (ICBSLP). IEEE, 2019, pp. 1–4.
- R. Sharmin, S. K. Rahut, and M. R. Huq, “Bengali spoken digit classification: A deep learning approach using convolutional neural network,” Procedia Computer Science, vol. 171, pp. 1381–1388, 2020
- B. Paul, S. Bera, R. Paul, and S. Phadikar, “Bengali spoken numerals recognition by mfcc and gmm technique,” in Advances in Electronics, Communication and Computing. Springer, 2021, pp. 85–96.
- http://www.practicalcryptography.com/miscellaneous/machine-learning/guide-mel-frequency-cepstral-coefficients-mfccs


## Author
Pias Roy, Ovishake Sen<br>
pias.kuet@gmail.com<br>
ovishake_sample@gmail.com<br>
Department of Computer Science and Engineering<br>
Khulna University of Engineering & Technology, Khulna<br>
Bangladesh

## Licensing
The code in this project is licensed under MIT License.
      
