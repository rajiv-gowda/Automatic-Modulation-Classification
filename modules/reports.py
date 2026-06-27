import streamlit as st
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


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
