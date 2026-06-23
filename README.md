Automatic Modulation Classification using Deep Learning
🚀 Live Application

Streamlit Deployment:

App Link : https://automatic-modulation-classification-tsut6ltx9hyw8vupt6pynv.streamlit.app

Upload a .npy I/Q signal and instantly:

Predict modulation type
Visualize signal characteristics
View performance metrics
Generate a professional PDF report

📌 Project Overview

Automatic Modulation Classification (AMC) is a Deep Learning-based wireless communication system that identifies modulation schemes directly from I/Q signal samples.

The system is built using a 1D Convolutional Neural Network (CNN) trained on the RadioML 2016.10A dataset and deployed as an interactive Streamlit Web Application.

The application allows users to upload signal files, analyze waveform characteristics, classify modulation types, and generate multi-page PDF reports.

✨ Key Features
Deep Learning Classification
1D CNN-based classifier
Batch Normalization
Softmax output layer
11 modulation classes
Signal Analysis
I/Q waveform visualization
Constellation diagram generation
Signal statistics calculation
Mean amplitude
Variance
Peak amplitude
Prediction Analytics
Top-3 modulation predictions
Confidence score visualization
Accuracy vs SNR analysis
Per-class performance evaluation
PDF Report Generation

Automatically generates a professional multi-page report containing:

Prediction summary
Confidence score
Signal statistics
Model information
Team information
GitHub QR code
I/Q waveform
Constellation diagram
Top-3 prediction chart
Accuracy vs SNR graph
Confusion matrix
Conclusion & Future Scope
📊 Supported Modulation Schemes
Modulation Classes
8PSK
AM-DSB
AM-SSB
BPSK
CPFSK
GFSK
PAM4
QAM16
QAM64
QPSK
WBFM

Total Classes: 11

📂 Dataset
RadioML 2016.10A

Features:

11 modulation schemes
Multiple SNR levels
I/Q signal representation
Realistic wireless channel impairments

Input Shape:

(128, 2)
🧠 Proposed Deep Learning Model
Input Signal (128×2)
          ↓
      Conv1D
          ↓
 Batch Normalization
          ↓
     Softmax (11)
          ↓
 Predicted Modulation

Frameworks Used:

TensorFlow
Keras
Final Test Accuracy
83.11%
🔄 System Architecture
RadioML 2016.10A Dataset
            ↓
      Data Preprocessing
            ↓
      I/Q Signal Input
        (128 × 2)
            ↓
 Proposed Deep Learning Model
            ↓
      Conv1D Layer
            ↓
 Batch Normalization
            ↓
    Softmax Classifier
            ↓
 Predicted Modulation
            ↓
 Streamlit Web Application
            ↓
 Signal Visualization
            ↓
 PDF Report Generation
📄 Generated PDF Report

The application automatically generates a detailed project report containing:

Page 1
Prediction summary
Confidence score
Signal statistics
Model information
Team details
GitHub QR code
Page 2
I/Q waveform
Constellation diagram
Top-3 predictions
Page 3
Accuracy vs SNR graph
Page 4
Confusion matrix
Page 5
Conclusion & Future Scope
📈 Results
Test Accuracy
83.11%
Performance Evaluation
Accuracy vs SNR analysis
Confusion matrix visualization
Top-3 prediction confidence analysis
Per-class performance evaluation
🛠 Technologies Used
Machine Learning
TensorFlow
Keras
NumPy
Pandas
Visualization
Matplotlib
Web Application
Streamlit
Report Generation
ReportLab
QRCode
📁 Project Structure
Automatic-Modulation-Classification/
│
├── app.py
├── amc_cnn_improved.keras
├── sample_signal.npy
├── requirements.txt
├── README.md
│
├── assets/
│   └── confusion_matrix_improved.png
│
├── data/
│   ├── per_class_accuracy.csv
│   └── snr_accuracy.csv
│
└── generated_reports/
🔮 Future Scope
Real-time SDR integration
Support for additional modulation schemes
Embedded deployment
Edge AI optimization
5G/6G communication applications
Improved classification accuracy
👨‍🎓 Project Information

Project Title:

Automatic Modulation Classification using Deep Learning

Team Lead:

P. Rajiv

College:

Narayana Engineering College, Nellore

Project Guide:

Dr. Sukumar

🎯 Applications
Cognitive Radio
Software Defined Radio (SDR)
Spectrum Monitoring
Electronic Warfare
Wireless Communication Systems
Signal Intelligence Systems
📜 License

This project is developed for academic, research, and educational purposes.
