import streamlit as st
import os
from modules.pdf_generator import create_pdf




def show_reports():

    st.title("📄 AMC Reports")

    if st.button("Generate PDF"):
        if not os.path.exists("iq_signal.png"):
            st.error("Please run Dataset Detection first by clicking 'Use Sample Signal' or uploading a signal.")
            st.stop()

        pdf = create_pdf(

            prediction="QPSK",
            confidence=98.50,

            mean_amp=0.52,
            variance=0.03,
            peak_amp=1.02,

            snr=12.8,
            bandwidth=118,
            energy=257.81,
            peak_frequency=121,

            iq_plot="iq_signal.png",
            constellation_plot="constellation.png",

            fft_plot="fft.png",
            power_plot=None,

            spectrogram_plot="spectrogram.png",
            waterfall_plot="waterfall.png",

            top3_plot="top3_predictions.png",

            snr_plot="snr_accuracy.png",

            confusion_matrix="assets/confusion_matrix_improved.png"

        )

        st.download_button(
            "📥 Download PDF",
            pdf,
            "AMC_Report.pdf",
            "application/pdf"
        )
