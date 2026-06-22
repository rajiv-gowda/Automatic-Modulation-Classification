# Automatic Modulation Classification Using Deep Learning

A deep learning-based Automatic Modulation Classification (AMC) system that identifies wireless signal modulation schemes directly from raw I/Q samples using a 1D Convolutional Neural Network (CNN).

The project includes an interactive Streamlit web application for real-time prediction, signal visualization, and confidence analysis.

## 🚀 Live Demo

Streamlit App : https://automatic-modulation-classification-tsut6ltx9hyw8vupt6pynv.streamlit.app

---

## 📌 Features

* Classifies **11 wireless modulation schemes**
* Supports `.npy` I/Q signal file uploads
* Visualizes uploaded signals using:

  * I/Q waveform plots
  * Constellation diagrams
* Displays prediction confidence scores
* Shows **Top-3 predicted modulation classes**
* Handles invalid input shapes gracefully
* Deployed using Streamlit Cloud

---

## 🧠 Model Overview

* **Model:** 1D CNN with Batch Normalization
* **Framework:** TensorFlow / Keras
* **Dataset:** RadioML 2016.10A
* **Input Shape:** `(128, 2)`
* **Number of Classes:** `11`
* **Training Strategy:**

  * SNR filtering (`SNR ≥ 0 dB`)
  * Batch Normalization
  * Dropout (`0.5`)
  * Early Stopping
  * Model Checkpointing

---

## 📊 Results

| Model                  | Test Accuracy |
| ---------------------- | ------------- |
| Baseline CNN           | 46.24%        |
| CNN with SNR Filtering | 73.84%        |
| Improved CNN           | **83.11%**    |

---

## 📡 Supported Modulation Schemes

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

---

## 📂 Dataset

**RadioML 2016.10A Dataset**

https://www.deepsig.ai/datasets

> Note: The dataset was preprocessed to include only samples with **SNR ≥ 0 dB** to improve classification performance.

---

## 🖥️ Application Preview

The Streamlit application provides:

1. Signal upload interface
2. I/Q waveform visualization
3. Constellation diagram generation
4. Top-3 prediction confidence chart
5. Final modulation prediction with confidence score

---

## 🛠️ Tech Stack

* Python
* TensorFlow
* Keras
* NumPy
* Matplotlib
* Pandas
* Streamlit
* Google Colab

---

## 📁 Project Structure

```text
Automatic-Modulation-Classification/
├── app.py
├── requirements.txt
├── README.md
├── amc_cnn_improved.keras
├── label_classes.npy
├── sample_signal.npy
└── assets/
```

---

## ⚙️ Installation

```bash
git clone https://github.com/YOUR_USERNAME/Automatic-Modulation-Classification.git

cd Automatic-Modulation-Classification

pip install -r requirements.txt

streamlit run app.py
```

---

## 📥 Input Format

Upload a NumPy `.npy` file containing I/Q samples with the following format:

```python
signal.shape == (128, 2)
```

Where:

* Column 0 → In-phase (I) channel
* Column 1 → Quadrature (Q) channel

---

## 🔮 Future Enhancements

* Support variable-length signals
* Real-time SDR integration
* Transformer-based AMC models
* Low-SNR classification improvements
* Multi-signal batch prediction

---

**Developed by Rajiv P**
