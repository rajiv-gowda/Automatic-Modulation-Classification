# Automatic Modulation Classification Using Deep Learning

An end-to-end deep learning system for **Automatic Modulation Classification (AMC)** using raw I/Q signal samples from the **RadioML 2016.10A** dataset.

This project uses an improved **1D Convolutional Neural Network (CNN)** with **Batch Normalization**, **Early Stopping**, and **Model Checkpointing** to classify **11 wireless modulation schemes**. The trained model is deployed as an interactive **Streamlit web application** for real-time modulation prediction.

---

## 🚀 Live Demo

**Streamlit App:** https://automatic-modulation-classification-tsut6ltx9hyw8vupt6pynv.streamlit.app

---

## ✨ Features

* Classifies **11 modulation schemes** from raw I/Q signals
* Interactive **Streamlit web application**
* Real-time prediction from uploaded `.npy` files
* I/Q waveform visualization
* Constellation diagram visualization
* Prediction confidence score
* Publicly deployed web application

---

## 📊 Dataset

**Dataset:** RadioML 2016.10A

* 11 modulation classes
* Signal-to-Noise Ratio (SNR): **-20 dB to +18 dB**
* Each sample contains **128 I/Q points**
* Input shape: **(128, 2)**

### Supported Modulation Schemes

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

## 📈 Model Evolution

| Model Version | Technique                                                  | Accuracy   |
| ------------- | ---------------------------------------------------------- | ---------- |
| Baseline CNN  | All SNR values (-20 dB to +18 dB)                          | 46.24%     |
| Filtered CNN  | SNR ≥ 0 dB                                                 | 73.84%     |
| Improved CNN  | Batch Normalization + Early Stopping + Model Checkpointing | **83.11%** |

---

## 🧠 Model Architecture

* Conv1D (64 filters, kernel size = 3)
* Batch Normalization
* MaxPooling1D
* Conv1D (128 filters, kernel size = 3)
* Batch Normalization
* MaxPooling1D
* Flatten
* Dense (128 units)
* Dropout (0.5)
* Output Layer (11 classes, Softmax)

---

## 🛠️ Technology Stack

* Python
* TensorFlow
* Keras
* Streamlit
* NumPy
* Matplotlib
* Google Colab
* GitHub

---

## 🔄 Project Workflow

```text
RadioML 2016.10A Dataset
            ↓
     Data Preprocessing
            ↓
      SNR Filtering
            ↓
 Improved 1D CNN Training
            ↓
      Model Optimization
            ↓
   Streamlit Deployment
            ↓
     Real-Time Prediction
```

---

## 🌐 Web Application

The application allows users to:

1. Upload a `.npy` I/Q signal file
2. Visualize the I/Q waveform
3. View the constellation diagram
4. Predict the modulation type
5. Display prediction confidence

> **Note:** The application currently accepts only signals with shape **(128, 2)**.

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/rajiv-gowda/Automatic-Modulation-Classification.git
cd Automatic-Modulation-Classification
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 📁 Repository Structure

```text
Automatic-Modulation-Classification/
│
├── app.py
├── requirements.txt
├── .python-version
├── README.md
├── amc_cnn_improved.keras
├── label_classes.npy
└── sample_signal.npy
```

---

## 🔮 Future Scope

* Support variable-length I/Q signals
* Improve low-SNR classification performance
* Integrate with Software Defined Radio (SDR) hardware
* Deploy on edge devices such as Raspberry Pi
* Explore Transformer-based AMC models

---

## 👨‍💻 Author

**PANDI RAJIV**
