# ============================================================
# AMC System V2
# PDF Generator - Part 1
# ============================================================

from io import BytesIO
from datetime import datetime
import os
import qrcode

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor


# ============================================================
# Footer
# ============================================================

def add_footer(pdf):

    pdf.setStrokeColor(HexColor("#BDBDBD"))
    pdf.line(40, 35, 570, 35)

    pdf.setFont("Helvetica-Oblique", 9)

    pdf.drawString(
        45,
        18,
        "AMC System V2 | Automatic Modulation Classification"
    )

    pdf.drawRightString(
        560,
        18,
        "Developed by PANDI RAJIV"
    )


# ============================================================
# QR Code
# ============================================================

def generate_qr():

    github = "https://github.com/rajiv-gowda/automatic-modulation-classification"

    qr = qrcode.make(github)

    qr_path = "github_qr.png"

    qr.save(qr_path)

    return qr_path


# ============================================================
# Create PDF
# ============================================================

def create_pdf(

        prediction,
        confidence,

        mean_amp,
        variance,
        peak_amp,

        snr,
        bandwidth,
        energy,
        peak_frequency,

        iq_plot,
        constellation_plot,

        fft_plot,
        power_plot,

        spectrogram_plot,
        waterfall_plot,

        top3_plot,

        snr_plot,

        confusion_matrix

):

    buffer = BytesIO()

    pdf = canvas.Canvas(
        buffer,
        pagesize=letter
    )

    width, height = letter

    qr_path = generate_qr()

    # ========================================================
    # PAGE 1
    # ========================================================

    pdf.setTitle(
        "AMC System V2 Report"
    )

    pdf.setFont(
        "Helvetica-Bold",
        22
    )

    pdf.drawCentredString(
        width/2,
        760,
        "Automatic Modulation Classification"
    )

    pdf.setFont(
        "Helvetica",
        14
    )

    pdf.drawCentredString(
        width/2,
        735,
        "Deep Learning Based Wireless Signal Analysis"
    )

    pdf.setStrokeColor(
        HexColor("#1565C0")
    )

    pdf.setLineWidth(2)

    pdf.line(
        40,
        720,
        570,
        720
    )

    pdf.setFont(
        "Helvetica-Bold",
        16
    )

    pdf.drawString(
        50,
        685,
        "Prediction Summary"
    )

    pdf.setFont(
        "Helvetica",
        12
    )

    pdf.drawString(
        70,
        655,
        f"Predicted Modulation : {prediction}"
    )

    pdf.drawString(
        70,
        635,
        f"Confidence : {confidence:.2f}%"
    )

    pdf.drawString(
        70,
        615,
        f"Generated : {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
    )

    pdf.setFont(
        "Helvetica-Bold",
        16
    )

    pdf.drawString(
        50,
        570,
        "Signal Statistics"
    )

    pdf.setFont(
        "Helvetica",
        12
    )

    pdf.drawString(
        70,
        545,
        f"Mean Amplitude : {mean_amp:.4f}"
    )

    pdf.drawString(
        70,
        525,
        f"Variance : {variance:.6f}"
    )

    pdf.drawString(
        70,
        505,
        f"Peak Amplitude : {peak_amp:.4f}"
    )

    pdf.drawString(
        70,
        485,
        f"Estimated SNR : {snr:.2f} dB"
    )

    pdf.drawString(
        70,
        465,
        f"Bandwidth : {bandwidth}"
    )

    pdf.drawString(
        70,
        445,
        f"Signal Energy : {energy:.2f}"
    )

    pdf.drawString(
        70,
        425,
        f"Peak Frequency : {peak_frequency}"
    )

    pdf.setFont(
        "Helvetica-Bold",
        16
    )

    pdf.drawString(
        50,
        375,
        "Project Information"
    )

    pdf.setFont(
        "Helvetica",
        12
    )

    pdf.drawString(70,350,"Dataset : RadioML 2016.10A")
    pdf.drawString(70,330,"Model : 1D CNN")
    pdf.drawString(70,310,"Framework : TensorFlow / Keras")
    pdf.drawString(70,290,"Supported Classes : 11")
    pdf.drawString(70,270,"Input Shape : (128,2)")

    pdf.drawImage(
        qr_path,
        430,
        220,
        width=90,
        height=90
    )

    pdf.setFont(
        "Helvetica",
        9
    )

    pdf.drawCentredString(
        475,
        205,
        "GitHub Repository"
    )

    pdf.setFont(
        "Helvetica-Bold",
        14
    )

    pdf.drawString(
        50,
        180,
        "Project Team"
    )

    pdf.setFont(
        "Helvetica",
        11
    )

    pdf.drawString(70,155,"Team Lead : PANDI RAJIV")
    pdf.drawString(70,138,"College : Narayana Engineering College")
    pdf.drawString(70,121,"Department : Electronics & Communication Engineering")

    add_footer(pdf)

    pdf.showPage()
    # ========================================================
    # PAGE 2
    # Uploaded Signal Analysis
    # ========================================================

    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawString(
        50,
        770,
        "Uploaded Signal Analysis"
    )

    pdf.setFont("Helvetica", 11)

    pdf.drawString(
        50,
        745,
        "The uploaded signal is analysed before CNN prediction."
    )

    pdf.drawImage(
        iq_plot,
        40,
        430,
        width=520,
        height=260,
        preserveAspectRatio=True
    )

    pdf.setFont(
        "Helvetica-Bold",
        14
    )

    pdf.drawString(
        50,
        395,
        "Description"
    )

    pdf.setFont(
        "Helvetica",
        11
    )

    pdf.drawString(
        60,
        370,
        "The waveform represents the In-phase (I) and Quadrature (Q)"
    )

    pdf.drawString(
        60,
        350,
        "components of the received wireless signal."
    )

    pdf.drawString(
        60,
        330,
        "These 128 samples are fed directly into the CNN model."
    )

    add_footer(pdf)

    pdf.showPage()


    # ========================================================
    # PAGE 3
    # Constellation Diagram
    # ========================================================

    pdf.setFont(
        "Helvetica-Bold",
        20
    )

    pdf.drawString(
        50,
        770,
        "Constellation Diagram"
    )

    pdf.drawImage(
        constellation_plot,
        90,
        260,
        width=420,
        height=420,
        preserveAspectRatio=True
    )

    pdf.setFont(
        "Helvetica-Bold",
        14
    )

    pdf.drawString(
        50,
        220,
        "Description"
    )

    pdf.setFont(
        "Helvetica",
        11
    )

    pdf.drawString(
        60,
        195,
        "Constellation diagrams visualize modulation"
    )

    pdf.drawString(
        60,
        175,
        "symbols on the I-Q plane."
    )

    pdf.drawString(
        60,
        155,
        "The CNN learns these spatial distributions"
    )

    pdf.drawString(
        60,
        135,
        "during model training."
    )

    add_footer(pdf)

    pdf.showPage()


    # ========================================================
    # PAGE 4
    # FFT Spectrum
    # ========================================================

    pdf.setFont(
        "Helvetica-Bold",
        20
    )

    pdf.drawString(
        50,
        770,
        "FFT Spectrum"
    )

    pdf.drawImage(
        fft_plot,
        40,
        260,
        width=520,
        height=380,
        preserveAspectRatio=True
    )

    pdf.setFont(
        "Helvetica",
        11
    )

    pdf.drawString(
        50,
        220,
        "Fast Fourier Transform converts the signal"
    )

    pdf.drawString(
        50,
        200,
        "from the time domain into the frequency domain."
    )

    add_footer(pdf)

    pdf.showPage()


    # ========================================================
    # PAGE 5
    # Power Spectrum
    # ========================================================

    pdf.setFont(
        "Helvetica-Bold",
        20
    )

    pdf.drawString(
        50,
        770,
        "Power Spectrum"
    )

    pdf.drawImage(
        power_plot,
        40,
        260,
        width=520,
        height=380,
        preserveAspectRatio=True
    )

    pdf.setFont(
        "Helvetica",
        11
    )

    pdf.drawString(
        50,
        220,
        "Power spectrum represents signal power"
    )

    pdf.drawString(
        50,
        200,
        "distributed across different frequencies."
    )

    add_footer(pdf)

    pdf.showPage()
    # ========================================================
    # PAGE 6
    # Spectrogram
    # ========================================================

    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawString(
        50,
        770,
        "Spectrogram Analysis"
    )

    pdf.drawImage(
        spectrogram_plot,
        40,
        250,
        width=520,
        height=400,
        preserveAspectRatio=True
    )

    pdf.setFont(
        "Helvetica",
        11
    )

    pdf.drawString(
        50,
        215,
        "The spectrogram represents frequency variation"
    )

    pdf.drawString(
        50,
        195,
        "with respect to time."
    )

    add_footer(pdf)

    pdf.showPage()


    # ========================================================
    # PAGE 7
    # Waterfall Spectrum
    # ========================================================

    pdf.setFont("Helvetica-Bold", 20)

    pdf.drawString(
        50,
        770,
        "Waterfall Spectrum"
    )

    pdf.drawImage(
        waterfall_plot,
        40,
        250,
        width=520,
        height=400,
        preserveAspectRatio=True
    )

    pdf.setFont(
        "Helvetica",
        11
    )

    pdf.drawString(
        50,
        215,
        "The waterfall plot visualizes signal evolution"
    )

    pdf.drawString(
        50,
        195,
        "across time and frequency."
    )

    add_footer(pdf)

    pdf.showPage()


    # ========================================================
    # PAGE 8
    # RF Signal Analysis
    # ========================================================

    pdf.setFont(
        "Helvetica-Bold",
        20
    )

    pdf.drawString(
        50,
        770,
        "RF Signal Analysis"
    )

    pdf.setFont(
        "Helvetica-Bold",
        14
    )

    pdf.drawString(
        50,
        720,
        "Computed Parameters"
    )

    pdf.setFont(
        "Helvetica",
        12
    )

    pdf.drawString(
        70,
        685,
        f"Estimated SNR : {snr:.2f} dB"
    )

    pdf.drawString(
        70,
        660,
        f"Estimated Bandwidth : {bandwidth}"
    )

    pdf.drawString(
        70,
        635,
        f"Signal Energy : {energy:.2f}"
    )

    pdf.drawString(
        70,
        610,
        f"Peak Frequency Bin : {peak_frequency}"
    )

    pdf.setFont(
        "Helvetica-Bold",
        14
    )

    pdf.drawString(
        50,
        560,
        "Analysis Summary"
    )

    pdf.setFont(
        "Helvetica",
        11
    )

    summary = [

        "The uploaded signal was analysed using",

        "advanced Digital Signal Processing",

        "techniques including FFT, Spectrogram,",

        "Waterfall Spectrum and Energy Analysis.",

        "",

        "The extracted features were classified",

        "using the trained CNN model."

    ]

    y = 530

    for line in summary:

        pdf.drawString(
            60,
            y,
            line
        )

        y -= 22

    add_footer(pdf)

    pdf.showPage()
    # ========================================================
    # PAGE 9
    # Top-3 Predictions
    # ========================================================

    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawString(50, 770, "CNN Prediction Analysis")

    pdf.drawImage(
        top3_plot,
        80,
        280,
        width=430,
        height=320,
        preserveAspectRatio=True
    )

    pdf.setFont("Helvetica", 11)

    pdf.drawString(
        50,
        240,
        "The CNN predicts the most probable modulation"
    )

    pdf.drawString(
        50,
        220,
        "scheme based on learned I/Q signal features."
    )

    add_footer(pdf)

    pdf.showPage()


    # ========================================================
    # PAGE 10
    # Accuracy vs SNR
    # ========================================================

    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawString(50,770,"Model Performance")

    pdf.drawImage(
        snr_plot,
        40,
        250,
        width=520,
        height=380,
        preserveAspectRatio=True
    )

    pdf.setFont("Helvetica",11)

    pdf.drawString(
        50,
        220,
        "Model accuracy generally improves as the"
    )

    pdf.drawString(
        50,
        200,
        "Signal-to-Noise Ratio increases."
    )

    add_footer(pdf)

    pdf.showPage()


    # ========================================================
    # PAGE 11
    # Confusion Matrix
    # ========================================================

    pdf.setFont("Helvetica-Bold",20)

    pdf.drawString(
        50,
        770,
        "Confusion Matrix"
    )

    pdf.drawImage(
        confusion_matrix,
        50,
        150,
        width=500,
        height=500,
        preserveAspectRatio=True
    )

    pdf.setFont(
        "Helvetica",
        11
    )

    pdf.drawString(
        50,
        120,
        "The confusion matrix summarizes model"
    )

    pdf.drawString(
        50,
        100,
        "classification performance for all 11 classes."
    )

    add_footer(pdf)

    pdf.showPage()


    # ========================================================
    # PAGE 12
    # Conclusion
    # ========================================================

    pdf.setFont(
        "Helvetica-Bold",
        22
    )

    pdf.drawString(
        50,
        760,
        "Project Conclusion"
    )

    pdf.setFont(
        "Helvetica",
        12
    )

    lines = [

        "AMC System V2 successfully classifies",

        "wireless modulation schemes using",

        "Deep Learning and Digital Signal Processing.",

        "",

        "Implemented Features:",

        "• CNN Based Modulation Classification",

        "• FFT Spectrum",

        "• Power Spectrum",

        "• Spectrogram",

        "• Waterfall Spectrum",

        "• Signal Statistics",

        "• SNR Estimation",

        "• Bandwidth Estimation",

        "• Signal Energy",

        "• Peak Frequency Detection",

        "• Professional PDF Report",

        "",

        "Future Scope:",

        "• RTL-SDR Integration",

        "• PlutoSDR Integration",

        "• GNU Radio Support",

        "• Real-Time RF Monitoring",

        "• Embedded Deployment"

    ]

    y = 720

    for line in lines:

        pdf.drawString(
            60,
            y,
            line
        )

        y -= 22

    pdf.setFont(
        "Helvetica-Bold",
        14
    )

    pdf.drawString(
        60,
        90,
        "Developed By : PANDI RAJIV"
    )

    pdf.drawString(
        60,
        70,
        "Narayana Engineering College"
    )

    add_footer(pdf)


    # ========================================================
    # SAVE PDF
    # ========================================================

    pdf.save()

    buffer.seek(0)

    return buffer

