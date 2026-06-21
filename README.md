# Automatic Modulation Classification Using Deep Learning

This project implements Automatic Modulation Classification (AMC) using a 1D Convolutional Neural Network (CNN) on the RadioML 2016.10A dataset.

## Project Overview

Automatic Modulation Classification is a key technology in modern wireless communication systems, including:

* Cognitive Radio
* Spectrum Sensing
* Electronic Warfare
* 5G and 6G Networks

The objective is to classify different modulation schemes directly from raw I/Q signal samples.

## Dataset

* Dataset: RadioML 2016.10A
* Number of classes: 11
* Total samples: 220,000
* SNR range: -20 dB to +18 dB

Dataset link: https://www.kaggle.com/datasets/nolasthitnotomorrow/radioml2016-deepsigcom

## Modulation Types

* 8PSK
* AM-DSB
* AM-SSB
* BPSK
* CPFSK
* GFSK
* PAM4
* QAM16
* QAM64
* QPSK
* WBFM

## Model

* Architecture: 1D CNN
* Framework: TensorFlow / Keras
* Training Platform: Google Colab (T4 GPU)

## Results

| Model        | Dataset        | Test Accuracy |
| ------------ | -------------- | ------------- |
| Baseline CNN | All SNR values | 46.24%        |
| Filtered CNN | SNR ≥ 0 dB     | 73.84%        |

## Files

* `AMC_CNN_Baseline.ipynb` — Complete training notebook
* `amc_cnn_filtered.keras` — Trained model

## Future Scope

* CNN + LSTM architecture
* Transformer-based AMC
* Real-time Software Defined Radio (SDR) implementation
* Deployment as a web application

 ## Live Demo

Streamlit App: https://automatic-modulation-classification-tsut6ltx9hyw8vupt6pynv.streamlit.app

## Author

Rajiv

