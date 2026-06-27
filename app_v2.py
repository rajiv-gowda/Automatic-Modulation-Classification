# ==========================================================
# Automatic Modulation Classification System V2
# Final Year Project
# Part 1
# ==========================================================

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import tensorflow as tf

from io import BytesIO
from datetime import datetime

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

import qrcode

# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="Automatic Modulation Classification",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# Custom CSS
# ==========================================================

st.markdown("""
<style>

.main{
    padding-top:1rem;
}

.block-container{
    padding-top:2rem;
}

.metric-container{
    border-radius:10px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# Sidebar
# ==========================================================

st.sidebar.image(
    "https://img.icons8.com/color/96/radar.png",
    width=70
)

st.sidebar.title("AMC System V2")

page = st.sidebar.radio(

    "Navigation",

    [

        "🏠 Dashboard",

        "📂 Dataset Detection",

        "📡 Live Signal Detection",

        "📊 Signal Analysis",

        "📄 Reports",

        "ℹ About"

    ]

)

st.sidebar.markdown("---")

st.sidebar.success("Version 2.0")

# ==========================================================
# Load CNN Model
# ==========================================================

@st.cache_resource

def load_model():

    return tf.keras.models.load_model(
        "amc_cnn_improved.keras"
    )

# ==========================================================
# Load Label Classes
# ==========================================================

@st.cache_data

def load_classes():

    return np.load(
        "label_classes.npy",
        allow_pickle=True
    )

# ==========================================================
# Load Everything
# ==========================================================

try:

    model = load_model()

    model_status = "🟢 Loaded"

except Exception:

    model = None

    model_status = "🔴 Not Loaded"

try:

    classes = load_classes()

except Exception:

    classes = []

# ==========================================================
# PDF Generator
# ==========================================================

def create_pdf(

    modulation,

    confidence,

    mean_amp,

    variance,

    peak_amp

):

    buffer = BytesIO()

    pdf = canvas.Canvas(
        buffer,
        pagesize=letter
    )

    pdf.setFont(
        "Helvetica-Bold",
        18
    )

    pdf.drawString(
        60,
        760,
        "AMC Prediction Report"
    )

    pdf.setFont(
        "Helvetica",
        12
    )

    pdf.drawString(
        60,
        720,
        f"Prediction : {modulation}"
    )

    pdf.drawString(
        60,
        700,
        f"Confidence : {confidence:.2f}%"
    )

    pdf.drawString(
        60,
        680,
        f"Mean Amplitude : {mean_amp:.4f}"
    )

    pdf.drawString(
        60,
        660,
        f"Variance : {variance:.6f}"
    )

    pdf.drawString(
        60,
        640,
        f"Peak Amplitude : {peak_amp:.4f}"
    )

    pdf.drawString(
        60,
        600,
        f"Generated : {datetime.now()}"
    )

    pdf.save()

    buffer.seek(0)

    return buffer

# ==========================================================
# Dashboard
# ==========================================================

if page == "🏠 Dashboard":

    st.title(
        "📡 Automatic Modulation Classification System"
    )

    st.caption(
        "AI Powered Wireless Signal Classification"
    )

    st.markdown("---")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "CNN Model",
        model_status
    )

    c2.metric(
        "Dataset",
        "RadioML2016.10A"
    )

    c3.metric(
        "Hardware",
        "Disconnected"
    )

    c4.metric(
        "Signals",
        "11 Classes"
    )

    st.markdown("---")

    st.subheader("Project Overview")

    st.info("""

This application provides

✅ Dataset Detection

✅ Live Hardware Detection

✅ Signal Analysis

✅ CNN Prediction

✅ Report Generation

✅ Future RTL-SDR Support

""")

    st.markdown("---")

    st.subheader("Workflow")

    st.write("""

Dataset / Live Signal

↓

Preprocessing

↓

CNN Model

↓

Prediction

↓

Analysis

↓

PDF Report

""")
