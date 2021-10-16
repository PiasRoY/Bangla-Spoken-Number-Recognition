# Bangla-Spoken-Number-Recognition

## Table of content

- [Motivation](#motivation)
- [Introduction](#introduction)
- [Quick Start Guide](#quick-start-guide)
- [Methodology](#methodology)
- [Experimental Result & Analysis](#implementation)
- [Contribution](#contribution)
- [Links and References](#links-and-references)
- [Author](#author)
- [Licensing](#licensing)

## Motivation
Speech is a very convenient way to interact with machines. At present, most features of the electronic devices are controlled through speech signals. Bangla speech based system lags behind in this human-machine interaction field. In order to create such speech controlled based systems, we first need to teach machines to recognize Bangla speech.

## Introduction
Speech recognition is a technique that converts human speech signals into text or words or in any form that can be easily understood by computers or other machines. There have been a few studies on Bangla digit recognition systems, the majority of which used small datasets with few variations in genders, ages, dialects, and other variables. Audio recordings of Bangladeshi people of various genders, ages, and dialects were used to create a large speech dataset of spoken '০-৯' Bangla digits in this study. Here, 400 noisy and noise-free samples per digit have been recorded for creating the dataset. Mel Frequency Cepstrum Coefficients (MFCCs) have been utilized for extracting meaningful features from the raw speech data. Then, to detect Bangla numeral digits, Convolutional Neural Networks (CNNs) were utilized. The suggested technique recognizes '০-৯' Bangla spoken digits with 97.1% accuracy throughout the whole dataset. The efficiency of the model was also assessed using 10-fold cross validation, which yielded a 96.7% accuracy.

## Quick Start Guide
1. clone this repo `https://github.com/PiasRoY/Bangla-Spoken-Number-Recognition.git`
2. collect our own developed dataset from here: `https://www.kaggle.com/piasroy/bangla-spoken-099-numbers`
3. copy all the folders labelled from "0-99" and paste them into the `Bangla_Spoken_Numbers` folder of this repo.
4. install required python dependencies from `requirements.txt`.
5. open and run `100_class_CNN.ipynb`.

## Methodology

## Experimental Result & Analysis


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
      
