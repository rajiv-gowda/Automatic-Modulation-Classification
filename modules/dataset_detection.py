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
    fig.savefig("iq_signal.png")
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
    fig2.savefig("constellation.png")
    # ===========================
# CNN Prediction
# ===========================

    signal_input = np.expand_dims(signal, axis=0)

    prediction = model.predict(signal_input, verbose=0)

    predicted_index = np.argmax(prediction)

    confidence = prediction[0][predicted_index] * 100

    predicted_class = classes[predicted_index]
    # ===========================
# Save values for PDF Report
# ===========================

    st.session_state["prediction"] = predicted_class
    st.session_state["confidence"] = confidence

    st.session_state["mean_amp"] = mean_amp
    st.session_state["variance"] = variance
    st.session_state["peak_amp"] = peak_amp

    st.markdown("## 🤖 CNN Prediction")

    st.success(
        f"Predicted Modulation: **{predicted_class}**"
    )

    st.metric(
        "Prediction Confidence",
        f"{confidence:.2f}%"
    )
    # ===========================
# Top 3 Predictions
# ===========================

    top3_idx = prediction[0].argsort()[-3:][::-1]

    top3_df = pd.DataFrame({
        "Modulation": [classes[i] for i in top3_idx],
        "Confidence (%)": [prediction[0][i] * 100 for i in top3_idx]
    })

    st.markdown("## 🏆 Top 3 Predictions")

    st.dataframe(
        top3_df,
        use_container_width=True,
        hide_index=True
    )

    st.bar_chart(
        top3_df.set_index("Modulation")
    )

    fig3, ax3 = plt.subplots(figsize=(6,4))

    ax3.bar(
        top3_df["Modulation"],
        top3_df["Confidence (%)"]
    )

    ax3.set_title("Top 3 Predictions")

    fig3.tight_layout()

    fig3.savefig("top3_predictions.png") 
    # ===========================
# Accuracy vs SNR
# ===========================

    st.markdown("## 📈 Model Accuracy vs SNR")

    snr_df = pd.read_csv("data/snr_accuracy.csv")

    st.line_chart(
        snr_df.set_index("SNR (dB)")
    )
    fig4, ax4 = plt.subplots(figsize=(7,4))

    ax4.plot(
        snr_df["SNR (dB)"],
        snr_df["Accuracy (%)"]
    )

    ax4.set_title("Accuracy vs SNR")

    fig4.tight_layout()

    fig4.savefig("snr_accuracy.png")
