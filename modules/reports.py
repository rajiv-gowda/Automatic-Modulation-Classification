```python
# ============================================================
# reports.py (Part 1)
# AMC System V2
# ============================================================

import os
from io import BytesIO
from datetime import datetime

import qrcode

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor


# ============================================================
# Footer
# ============================================================

def add_footer(pdf):

    pdf.setStrokeColor(HexColor("#888888"))
    pdf.line(40, 35, 570, 35)

    pdf.setFont("Helvetica-Oblique", 9)

    pdf.drawString(
        45,
        20,
        "AMC System V2 | Automatic Modulation Classification"
    )

    pdf.drawRightString(
        560,
        20,
        "Developed by PANDI RAJIV"
    )


# ============================================================
# QR Code
# ============================================================

def create_qr():

    url = "https://github.com/rajiv-gowda/automatic-modulation-classification"

    qr = qrcode.make(url)

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

    qr_path = create_qr()

    # ========================================================
    # PAGE 1
    # ========================================================

    pdf.setFont(
        "Helvetica-Bold",
        22
    )

    pdf.drawCentredString(
        width / 2,
        760,
        "Automatic Modulation Classification"
    )

    pdf.setFont(
        "Helvetica",
        14
    )

    pdf.drawCentredString(
        width / 2,
        735,
        "Deep Learning Based RF Signal Classification"
    )

    pdf.setStrokeColor(
        HexColor("#1F77B4")
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
        15
    )

    pdf.drawString(
        50,
        680,
        "Prediction Summary"
    )

    pdf.setFont(
        "Helvetica",
        12
    )

    pdf.drawString(
        70,
        650,
        f"Predicted Modulation : {prediction}"
    )

    pdf.drawString(
        70,
        630,
        f"Prediction Confidence : {confidence:.2f}%"
    )

    pdf.drawString(
        70,
        610,
        f"Generated : {datetime.now().strftime('%d-%m-%Y %H:%M')}"
    )

    pdf.setFont(
        "Helvetica-Bold",
        15
    )

    pdf.drawString(
        50,
        560,
        "Signal Statistics"
    )

    pdf.setFont(
        "Helvetica",
        12
    )

    pdf.drawString(
        70,
        530,
        f"Mean Amplitude : {mean_amp:.4f}"
    )

    pdf.drawString(
        70,
        510,
        f"Variance : {variance:.6f}"
    )

    pdf.drawString(
        70,
        490,
        f"Peak Amplitude : {peak_amp:.4f}"
    )

    pdf.drawString(
        70,
        470,
        f"Estimated SNR : {snr:.2f} dB"
    )

    pdf.drawString(
        70,
        450,
        f"Estimated Bandwidth : {bandwidth}"
    )

    pdf.drawString(
        70,
        430,
        f"Signal Energy : {energy:.2f}"
    )

    pdf.drawString(
        70,
        410,
        f"Peak Frequency Bin : {peak_frequency}"
    )

    pdf.setFont(
        "Helvetica-Bold",
        15
    )

    pdf.drawString(
        50,
        360,
        "Project Information"
    )

    pdf.setFont(
        "Helvetica",
        12
    )

    pdf.drawString(
        70,
        335,
        "Dataset : RadioML 2016.10A"
    )

    pdf.drawString(
        70,
        315,
        "Model : 1D CNN"
    )

    pdf.drawString(
        70,
        295,
        "Framework : TensorFlow / Keras"
    )

    pdf.drawString(
        70,
        275,
        "Supported Classes : 11"
    )

    pdf.drawString(
        70,
        255,
        "Input Shape : (128,2)"
    )

    pdf.drawImage(
        qr_path,
        430,
        210,
        width=90,
        height=90
    )

    pdf.setFont(
        "Helvetica",
        9
    )

    pdf.drawCentredString(
        475,
        195,
        "GitHub Repository"
    )

    add_footer(pdf)

    pdf.showPage()
```
```python
    # ========================================================
    # PAGE 2
    # Waveform + Constellation
    # ========================================================

    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(50, 770, "Signal Visualization")

    pdf.setFont("Helvetica", 11)
    pdf.drawString(
        50,
        745,
        "Uploaded I/Q Signal and Constellation Diagram"
    )

    pdf.drawImage(
        iq_plot,
        40,
        480,
        width=520,
        height=210,
        preserveAspectRatio=True
    )

    pdf.drawImage(
        constellation_plot,
        130,
        170,
        width=320,
        height=230,
        preserveAspectRatio=True
    )

    add_footer(pdf)

    pdf.showPage()


    # ========================================================
    # PAGE 3
    # FFT + Power Spectrum
    # ========================================================

    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(50, 770, "Frequency Domain Analysis")

    pdf.drawImage(
        fft_plot,
        40,
        420,
        width=520,
        height=260,
        preserveAspectRatio=True
    )

    pdf.drawImage(
        power_plot,
        40,
        110,
        width=520,
        height=240,
        preserveAspectRatio=True
    )

    add_footer(pdf)

    pdf.showPage()


    # ========================================================
    # PAGE 4
    # Spectrogram + Waterfall
    # ========================================================

    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(
        50,
        770,
        "Time Frequency Analysis"
    )

    pdf.drawImage(
        spectrogram_plot,
        40,
        420,
        width=520,
        height=250,
        preserveAspectRatio=True
    )

    pdf.drawImage(
        waterfall_plot,
        40,
        120,
        width=520,
        height=220,
        preserveAspectRatio=True
    )

    add_footer(pdf)

    pdf.showPage()


    # ========================================================
    # PAGE 5
    # Top 3 Predictions
    # ========================================================

    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(
        50,
        770,
        "CNN Prediction Analysis"
    )

    pdf.drawImage(
        top3_plot,
        80,
        280,
        width=430,
        height=320,
        preserveAspectRatio=True
    )

    pdf.setFont("Helvetica", 12)

    pdf.drawString(
        50,
        240,
        "The CNN predicts the modulation class with the"
    )

    pdf.drawString(
        50,
        220,
        "highest confidence after analysing the I/Q samples."
    )

    pdf.drawString(
        50,
        200,
        "The Top-3 graph shows the confidence distribution"
    )

    pdf.drawString(
        50,
        180,
        "among the most probable modulation schemes."
    )

    add_footer(pdf)

    pdf.showPage()
```
```python
    # ========================================================
    # PAGE 6
    # Accuracy vs SNR
    # ========================================================

    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(
        50,
        770,
        "Model Performance"
    )

    pdf.drawString(
        50,
        740,
        "Accuracy vs Signal-to-Noise Ratio"
    )

    pdf.drawImage(
        snr_plot,
        40,
        270,
        width=520,
        height=380,
        preserveAspectRatio=True
    )

    add_footer(pdf)

    pdf.showPage()


    # ========================================================
    # PAGE 7
    # Confusion Matrix
    # ========================================================

    pdf.setFont("Helvetica-Bold", 18)
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

    add_footer(pdf)

    pdf.showPage()


    # ========================================================
    # PAGE 8
    # Conclusion
    # ========================================================

    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawString(
        50,
        760,
        "Project Conclusion"
    )

    pdf.setFont("Helvetica", 12)

    y = 720

    conclusion = [

        "AMC System V2 successfully classifies digital",
        "wireless modulation schemes using a trained",
        "1D Convolutional Neural Network.",

        "",

        "The application performs:",

        "• Automatic Modulation Classification",
        "• FFT Spectrum Analysis",
        "• Power Spectrum Analysis",
        "• Spectrogram Analysis",
        "• Waterfall Spectrum",
        "• Signal Energy Estimation",
        "• Bandwidth Estimation",
        "• Peak Frequency Detection",
        "• PDF Report Generation",

        "",

        "Future Scope",

        "• RTL-SDR Integration",
        "• PlutoSDR Support",
        "• GNU Radio Interface",
        "• Real-time RF Signal Monitoring",
        "• Cloud Deployment",
        "• Embedded FPGA Implementation"

    ]

    for line in conclusion:

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
        120,
        "Developed By"
    )

    pdf.setFont(
        "Helvetica",
        12
    )

    pdf.drawString(
        60,
        95,
        "PANDI RAJIV"
    )

    pdf.drawString(
        60,
        75,
        "Narayana Engineering College"
    )

    pdf.drawString(
        60,
        55,
        "Department of Electronics and Communication Engineering"
    )

    add_footer(pdf)

    pdf.save()

    buffer.seek(0)

    return buffer
```
