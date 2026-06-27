import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


def show_dataset_detection(model, classes):

    st.title("📂 Dataset Detection")

    st.info("Upload a .npy signal or use the sample signal.")

    uploaded_file = st.file_uploader(
        "Upload Signal",
        type=["npy"]
    )

    use_sample = st.button("🚀 Use Sample Signal")

    signal = None

    if uploaded_file is not None:

        signal = np.load(uploaded_file)

    elif use_sample:

        signal = np.load("sample_signal.npy")

    if signal is None:
        return

    st.success("Signal loaded successfully.")
