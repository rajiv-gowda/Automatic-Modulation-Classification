```python
import streamlit as st

from modules.pdf_generator import create_pdf


def show_reports():

    st.title("📄 AMC System V2 Reports")

    st.info(
        "Generate a complete RF Signal Analysis PDF."
    )

    if "prediction" not in st.session_state:

        st.warning(
            "Please run Dataset Detection first."
        )

        return

    if st.button("Generate PDF Report"):

        pdf = create_pdf(

            prediction=st.session_state["prediction"],

            confidence=st.session_state["confidence"],

            mean_amp=st.session_state["mean_amp"],

            variance=st.session_state["variance"],

            peak_amp=st.session_state["peak_amp"],

            snr=st.session_state["snr"],

            bandwidth=st.session_state["bandwidth"],

            energy=st.session_state["energy"],

            peak_frequency=st.session_state["peak_frequency"],

            iq_plot="iq_signal.png",

            constellation_plot="constellation.png",

            fft_plot="fft.png",

            power_plot="power_spectrum.png",

            spectrogram_plot="spectrogram.png",

            waterfall_plot="waterfall.png",

            top3_plot="top3_predictions.png",

            snr_plot="snr_accuracy.png",

            confusion_matrix="assets/confusion_matrix_improved.png"

        )

        st.success(
            "PDF generated successfully."
        )

        st.download_button(

            label="📥 Download AMC Report",

            data=pdf,

            file_name="AMC_System_Report.pdf",

            mime="application/pdf"

        )
```
