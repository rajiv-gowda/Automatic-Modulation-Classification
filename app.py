import pandas as pd
import streamlit as st
import tensorflow as tf
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
from datetime import datetime
import qrcode
st.set_page_config(
    page_title="AMC",
    page_icon="📡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.title("Automatic Modulation Classification")
st.markdown("""
Upload an I/Q signal file (`.npy`) to classify one of 11 wireless modulation schemes.

**Supported modulations:** 8PSK, AM-DSB, AM-SSB, BPSK, CPFSK, GFSK, PAM4, QAM16, QAM64, QPSK, WBFM

**Expected input shape:** `(128, 2)`
""")

@st.cache_resource
def load_model():
    return tf.keras.models.load_model("amc_cnn_improved.keras")
model = load_model()

def add_footer(pdf):
    pdf.setFont("Helvetica-Oblique", 9)
    pdf.drawCentredString(
        300,
        20,
        "AMC Deep Learning System v1.0 | Developed by PANDI RAJIV"
    )

def create_pdf(
    prediction,
    confidence,
    mean_amp,
    variance,
    peak_amp,
    iq_plot_path,
    constellation_path,
    top3_path,
    snr_path
):
    buffer = BytesIO()
    qr = qrcode.make(
        "https://github.com/rajiv-gowda/automatic-modulation-classification"
    )
    qr.save("github_qr.png")

    pdf = canvas.Canvas(buffer, pagesize=letter)

    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(50, 750, "Automatic Modulation Classification Report")
    
    

    pdf.setFont("Helvetica", 12)
    pdf.drawString(
        50,
        720,
        f"Generated on: {datetime.now().strftime('%d-%m-%Y')}"
    )
    pdf.drawString(50, 680, f"Predicted Modulation: {prediction}")
    pdf.drawString(50, 660, f"Confidence: {confidence:.2f}%")
    
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(50, 620, "Signal Statistics")
    pdf.setFont("Helvetica", 12)
    pdf.drawString(70, 600, f"Mean Amplitude: {mean_amp:.4f}")
    pdf.drawString(70, 580, f"Variance: {variance:.6f}")
    pdf.drawString(70, 560, f"Peak Amplitude: {peak_amp:.4f}")
    
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(50, 520, "Model Information")
    
    pdf.setFont("Helvetica", 12)
    pdf.drawString(70, 500, "Dataset: RadioML 2016.10A")
    pdf.drawString(70, 480, "Model: 1D CNN + Batch Normalization")
    pdf.drawString(70, 460, "Classes: 11")
    pdf.drawString(70, 440, "Test Accuracy: 83.11%")
    
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(50, 420, "Project Team Details")

    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, 400, "TEAM LEAD: PANDI RAJIV")
    pdf.drawString(50, 380, "College: Narayana Engineering College, Nellore")
    pdf.drawString(50, 360, "Project Guide: Dr.SUKUMAR SIR")
    pdf.drawImage(
        "github_qr.png",
        420,
        320,
        width=100,
        height=100
    )

    pdf.setFont("Helvetica", 9)
    pdf.drawString(
        418,
        305,
        "Scan for GitHub Repository"
    )
    add_footer(pdf)

    pdf.showPage()

    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(50, 770, "Signal Visualizations")

# I/Q waveform
    pdf.drawImage(
        iq_plot_path,
        40, 500,
        width=520,
        height=180,
        preserveAspectRatio=True
    )

# Constellation diagram
    pdf.drawImage(
        constellation_path,
        40, 240,
        width=240,
        height=180,
        preserveAspectRatio=True
    )

# Top 3 predictions
    pdf.drawImage(
        top3_path,
        320, 240,
        width=240,
        height=180,
        preserveAspectRatio=True
    )
    add_footer(pdf)

# SNR chart
    pdf.showPage()

    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(50, 770, "Model Accuracy vs SNR")

    pdf.drawImage(
        snr_path,
        40, 300,
        width=520,
        height=320,
        preserveAspectRatio=True
    )
    pdf.showPage()

    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(50, 770, "Confusion Matrix")

    pdf.drawImage(
        "assets/confusion_matrix_improved.png",
        40,
        180,
        width=520,
        height=520,
        preserveAspectRatio=True
)
    pdf.showPage()

    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(50, 750, "Project Conclusion")

    pdf.setFont("Helvetica", 12)

    pdf.drawString(
        50,
        700,
        "The Automatic Modulation Classification system"
    )

    pdf.drawString(
        50,
        680,
        "successfully identifies 11 wireless modulation schemes"
    )

    pdf.drawString(
        50,
        660,
        "using a Deep Learning based 1D CNN model."
    )

    pdf.drawString(
        50,
        620,
        "Dataset Used: RadioML 2016.10A"
    )

    pdf.drawString(
        50,
        600,
        "Model Accuracy: 83.11%"
    )

    pdf.drawString(
        50,
        580,
        "Framework: TensorFlow / Keras"
    )

    pdf.drawString(
        50,
        540,
        "Future Scope:"
    )

    pdf.drawString(
        70,
        520,
        "- Support additional modulation schemes"
    )

    pdf.drawString(
        70,
        500,
        "- Real-time SDR integration"
    )

    pdf.drawString(
        70,
        480,
        "- Deployment on embedded systems"
    )
    
    add_footer(pdf)

    pdf.save()

    buffer.seek(0)
    return buffer

classes = ['8PSK', 'AM-DSB', 'AM-SSB', 'BPSK', 'CPFSK',
           'GFSK', 'PAM4', 'QAM16', 'QAM64', 'QPSK', 'WBFM']


st.sidebar.header("Model Information")

st.sidebar.markdown("""
- **Dataset:** RadioML 2016.10A
- **Model:** 1D CNN + Batch Normalization
- **Classes:** 11
- **Input Shape:** (128, 2)
- **Test Accuracy:** 83.11%
- **Framework:** TensorFlow / Keras
""")
st.sidebar.subheader("Model Performance")

st.sidebar.image(
    "assets/confusion_matrix_improved.png",
    caption="Confusion Matrix",
    use_container_width=True
)
with open("sample_signal.npy", "rb") as f:
    st.download_button(
        label="📥 Download Sample Signal",
        data=f,
        file_name="sample_signal.npy",
        mime="application/octet-stream"
    )
    st.markdown("### 📱 Mobile Users")
    st.info(
        "If upload fails, enable Desktop Site in Chrome and refresh the page."
    )
    import numpy as np

use_sample = st.button("🚀 Use Sample Signal")

if use_sample:
    uploaded_file = "sample"
    signal = np.load("sample_signal.npy")

uploaded_file = st.file_uploader(
    "📂 Select a .npy Signal File",
    type=["npy"],
    help="Upload one RadioML signal sample"
)

st.info("⚠️ Upload only ONE .npy file at a time.")

if uploaded_file is not None or use_sample:
    st.success("Signal loaded successfully")

    import numpy as np

    if not use_sample:
        signal = np.load(uploaded_file)
    if signal.shape != (128, 2):
        st.error(f"Invalid signal shape: {signal.shape}. Expected (128, 2).")
        st.stop()

    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(10, 4))

    ax.plot(signal[:, 0], label="I Channel")
    ax.plot(signal[:, 1], label="Q Channel")

    ax.set_title("Uploaded I/Q Signal")
    ax.set_xlabel("Sample Index")
    ax.set_ylabel("Amplitude")
    ax.legend()

    fig.savefig("iq_signal.png", bbox_inches="tight")
    st.pyplot(fig)

    st.caption(
        "Each uploaded signal contains 128 I/Q samples, matching the RadioML 2016.10A dataset format used during training."
    )
    st.markdown("### Signal Statistics")

    mean_amp = np.mean(np.abs(signal))
    variance = np.var(signal)
    peak_amp = np.max(np.abs(signal))

    col1, col2, col3 = st.columns(3)

    col1.metric("Mean Amplitude", f"{mean_amp:.4f}")
    col2.metric("Variance", f"{variance:.6f}")
    col3.metric("Peak Amplitude", f"{peak_amp:.4f}")

    fig2, ax2 = plt.subplots(figsize=(5, 5))

    ax2.scatter(signal[:, 0], signal[:, 1], s=20, alpha=0.7)

    ax2.set_title("I/Q Constellation Diagram")
    ax2.set_xlabel("In-phase (I)")
    ax2.set_ylabel("Quadrature (Q)")
    ax2.grid(True)
    ax2.axis("equal")
    ax2.locator_params(axis='x', nbins=5)
    ax2.locator_params(axis='y', nbins=5)

    fig2.savefig("constellation.png", bbox_inches="tight")
    st.pyplot(fig2)

    signal = np.expand_dims(signal, axis=0)

    prediction = model.predict(signal)
    confidence = prediction.max() * 100
    predicted_class = prediction.argmax(axis=1)[0]
    import pandas as pd

    top3_idx = prediction[0].argsort()[-3:][::-1]

    top3 = pd.DataFrame({
        "Modulation": [classes[i] for i in top3_idx],
        "Confidence (%)": [prediction[0][i] * 100 for i in top3_idx]
    })

    st.success(
        f"Predicted Modulation: {classes[predicted_class]} ({confidence:.2f}% confidence)"
    )

    

    top3_fig, top3_ax = plt.subplots(figsize=(6, 4))
    top3 = top3.set_index("Modulation")

    top3_ax.bar(
        top3.index,
        top3["Confidence (%)"]
    )
    for i, value in enumerate(top3["Confidence (%)"]):
        top3_ax.text(
            i,
            value + 0.5,
            f"{value:.2f}%",
            ha="center",
            fontsize=9
        )

    top3_ax.set_ylim(0, max(top3["Confidence (%)"]) * 1.1)

    top3_ax.set_ylabel("Confidence (%)")
    top3_ax.set_xlabel("Modulation")
    top3_ax.tick_params(axis="x", rotation=45)

    top3_fig.savefig("top3_predictions.png", bbox_inches="tight")
    pdf_buffer = create_pdf(
        classes[predicted_class],
        confidence,
        mean_amp,
        variance,
        peak_amp,
        "iq_signal.png",
        "constellation.png",
        "top3_predictions.png",
        "snr_accuracy.png"
    )
    st.download_button(
        label="📄 Download Prediction Report (PDF)",
        data=pdf_buffer,
        file_name="amc_prediction_report.pdf",
        mime="application/pdf"
    )

    st.pyplot(top3_fig)

    per_class_df = pd.read_csv("data/per_class_accuracy.csv")

    st.dataframe(
    per_class_df,
    use_container_width=True,
    hide_index=True,
    height=420
)
    st.subheader("Model Accuracy vs SNR")

    snr_df = pd.read_csv("data/snr_accuracy.csv")
    snr_fig, snr_ax = plt.subplots(figsize=(6, 4))

    snr_ax.plot(
        snr_df["SNR (dB)"],
        snr_df["Accuracy (%)"],
        marker="o"
    )

    snr_ax.set_title("Model Accuracy vs SNR")
    snr_ax.set_xlabel("SNR (dB)")
    snr_ax.set_ylabel("Accuracy (%)")
    snr_ax.grid(True)

    snr_fig.savefig("snr_accuracy.png", bbox_inches="tight")

    st.line_chart(
    snr_df.set_index("SNR (dB)")
)
    st.subheader("Top 3 Predictions")


    st.bar_chart(top3, y_label="Confidence (%)")
