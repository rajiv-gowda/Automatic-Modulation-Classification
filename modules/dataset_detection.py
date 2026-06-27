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
