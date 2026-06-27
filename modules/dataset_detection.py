import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


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

    st.success("✅ Signal loaded successfully.")

    fig, ax = plt.subplots(figsize=(10,4))

    ax.plot(signal[:,0], label="I Channel")
    ax.plot(signal[:,1], label="Q Channel")

    ax.set_title("Uploaded I/Q Signal")
    ax.set_xlabel("Sample Index")
    ax.set_ylabel("Amplitude")

    ax.legend()

    st.pyplot(fig)
    st.markdown("## 📊 Signal Statistics")

    mean_amp = np.mean(np.abs(signal))
    variance = np.var(signal)
    peak_amp = np.max(np.abs(signal))

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Mean Amplitude",
        f"{mean_amp:.4f}"
    )

    c2.metric(
        "Variance",
        f"{variance:.6f}"
    )

    c3.metric(
        "Peak Amplitude",
        f"{peak_amp:.4f}"
    )
    st.markdown("## ⭐ I/Q Constellation Diagram")

    fig2, ax2 = plt.subplots(figsize=(6, 6))

    ax2.scatter(
        signal[:, 0],
        signal[:, 1],
        s=20,
        alpha=0.7
    )

    ax2.set_title("I/Q Constellation")
    ax2.set_xlabel("In-phase (I)")
    ax2.set_ylabel("Quadrature (Q)")
    ax2.grid(True)
    ax2.axis("equal")

    st.pyplot(fig2)
    # ===========================
# CNN Prediction
# ===========================

    signal_input = np.expand_dims(signal, axis=0)

    prediction = model.predict(signal_input, verbose=0)

    predicted_index = np.argmax(prediction)

    confidence = prediction[0][predicted_index] * 100

    predicted_class = classes[predicted_index]

    st.markdown("## 🤖 CNN Prediction")

    st.success(
        f"Predicted Modulation: **{predicted_class}**"
    )

    st.metric(
        "Prediction Confidence",
        f"{confidence:.2f}%"
    )
