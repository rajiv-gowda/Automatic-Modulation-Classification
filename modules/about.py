import streamlit as st


def show_about():

    st.title("ℹ️ About AMC System V2")

    st.markdown("---")

    st.header("📡 Automatic Modulation Classification System")

    st.write("""
AMC System V2 is a Deep Learning based Automatic Modulation Classification
application developed for intelligent wireless signal recognition.

The system classifies radio modulation schemes directly from raw IQ samples
using a Convolutional Neural Network (CNN) trained on the RadioML 2016.10A
dataset.
""")

    st.markdown("---")

    st.subheader("🎯 Project Features")

    st.markdown("""
- 📂 Dataset Signal Detection
- 📡 Live Signal Detection
- 📈 FFT Spectrum Analysis
- 🌊 Waterfall Spectrum
- 📊 Spectrogram Analysis
- 📉 Power Spectrum
- 📶 Signal-to-Noise Ratio (SNR) Estimation
- 📏 Bandwidth Estimation
- ⚡ Signal Energy Measurement
- 📡 Peak Frequency Detection
- 📄 PDF Report Generation
- 🤖 CNN-based Modulation Classification
""")

    st.markdown("---")

    st.subheader("🧠 Deep Learning Model")

    st.write("""
Model : 1D Convolutional Neural Network (CNN)

Dataset : RadioML 2016.10A

Supported Modulations:
""")

    st.code("""
BPSK
QPSK
8PSK
QAM16
QAM64
PAM4
CPFSK
GFSK
AM-DSB
AM-SSB
WBFM
""")

    st.markdown("---")

    st.subheader("🛠 Technology Stack")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
- Python
- TensorFlow
- Keras
- NumPy
- Matplotlib
- Streamlit
""")

    with col2:
        st.markdown("""
- RadioML Dataset
- ReportLab
- CNN
- FFT
- Digital Signal Processing
""")

    st.markdown("---")

    st.subheader("📊 Model Performance")

    st.metric("Supported Modulations", "11")
    st.metric("Deep Learning Model", "CNN")
    st.metric("Dataset", "RadioML 2016.10A")

    st.markdown("---")

    st.success("Developed as a Final Year Engineering Project")

    st.caption("© 2026 AMC System V2")
