import pandas as pd
import streamlit as st
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
from datetime import datetime
import qrcode
st.set_page_config(
    page_title="AMC",
    page_icon="📡",
    layout="centered",
    initial_sidebar_state="expanded"
)
# ==============================
# Sidebar Navigation
# ==============================

st.sidebar.title("📡 AMC System V2")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "📂 Dataset Detection",
        "📡 Live Signal Detection",
        "📊 Signal Analysis",
        "📄 Reports",
        "ℹ️ About"
    ]
)
# ==============================
# Load CNN Model
# ==============================

@st.cache_resource
def load_model():
    return tf.keras.models.load_model("amc_cnn_improved.keras")


# ==============================
# Load CNN Model
# ==============================

@st.cache_resource
def load_model():
    return tf.keras.models.load_model("amc_cnn_improved.keras")


try:
    model = load_model()
    model_status = "✅ Loaded"
except Exception:
    model = None
    model_status = "❌ Not Loaded"


# ==============================
# Dashboard
# ==============================

if page == "🏠 Dashboard":

    st.title("📡 Automatic Modulation Classification System")

    st.caption("AI-Based Wireless Signal Analysis & Real-Time Modulation Detection")

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    col1.metric("Model", model_status)
    col2.metric("Dataset", "RadioML 2016.10A")
    col3.metric("Hardware", "Disconnected")

    st.markdown("---")

    st.subheader("Project Overview")

    st.write("""
This application supports:

- 📂 Dataset-based Modulation Classification
- 📡 Live Hardware Signal Detection (Coming Soon)
- 📊 Signal Analysis
- 📄 PDF Report Generation
- 🤖 CNN-based Automatic Modulation Classification
""")

elif page == "📂 Dataset Detection":

    st.title("📂 Dataset Detection")

    st.info("Upload a .npy signal or use the sample signal.")

    uploaded_file = st.file_uploader(
        "📂 Upload .npy Signal",
        type=["npy"]
    )

    use_sample = st.button("🚀 Use Sample Signal")

    if use_sample:
        signal = np.load("sample_signal.npy")
    elif uploaded_file is not None:
        signal = np.load(uploaded_file)
    else:
        signal = None

    if signal is not None:

        st.success("✅ Signal loaded successfully")

        fig, ax = plt.subplots(figsize=(10, 4))

        ax.plot(signal[:, 0], label="I Channel")
        ax.plot(signal[:, 1], label="Q Channel")

        ax.set_title("Uploaded I/Q Signal")
        ax.set_xlabel("Sample Index")
        ax.set_ylabel("Amplitude")
        ax.legend()

        st.pyplot(fig)
