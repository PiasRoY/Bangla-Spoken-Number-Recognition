import os
import librosa
import numpy as np
from tqdm import tqdm
import noisereduce as nr
from pydub import AudioSegment


# extracting mfccs from audio file

def wav2m(file_path, n_mfcc=13, max_len=39):
    
    wave, sr = librosa.load(file_path, mono=True, sr=None)

    noisy_part = wave[:]
    wave = nr.reduce_noise(y=wave, sr=sr)
    wave = np.asfortranarray(wave[::3])
    
    mfcc = librosa.feature.mfcc(y=wave, sr=sr, n_mfcc=n_mfcc, n_fft=2048, hop_length=512)

    if (max_len > mfcc.shape[1]):
        pad_width = max_len - mfcc.shape[1]
        mfcc = np.pad(mfcc, pad_width=((0, 0), (0, pad_width)), mode='constant')
    else:
        mfcc = mfcc[:, :max_len]

    # concatenating delta and delta2 coefficients
    delta_mfcc = librosa.feature.delta(mfcc, width=3)
    delta2_mfcc = librosa.feature.delta(mfcc, width=3, order=1)
    mfccs = np.concatenate((mfcc, delta_mfcc, delta2_mfcc))
    
    return mfccs


# extracting mfccs and storing them as numpy-array in destination folder

def save(path, dest, labels, feature, max_len=39, coefficients=13):

    for label in labels:
        
        vectors = []

        wavfiles = [path + label + '/' + wavfile for wavfile in os.listdir(path + label)]

        for wavfile in tqdm(wavfiles, "Saving vectors of label - '{}'".format(label)):
            mfcc = wav2m(wavfile)
            vectors.append(mfcc)
            
        np.save(dest + label + '.npy', vectors)


# loading mfccs from numpy-arrays

def load_data(path, labels, val_size, test_size):

    X = np.load(path + labels[0] + '.npy')
    y = np.full(X.shape[0], fill_value= labels[0])


    for i, label in enumerate(labels[1:]):
        x = np.load(path + label + '.npy')

        X = np.vstack((X, x))
        y = np.append(y, np.full(x.shape[0], fill_value=i+1))

    return (X, y)

