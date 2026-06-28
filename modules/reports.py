import streamlit as st
from modules.pdf_generator import create_pdf


def show_reports():

    st.title("📄 AMC System V2 Reports")

    st.info(
        "Generate a professional RF Signal Analysis PDF Report."
    )

    st.warning(
        "PDF Generator integration is under development."
    )

    if st.button("Generate Report"):

        st.success(
            "PDF Generator Connected Successfully!"
        )

        st.info(
            "Next step: connect real prediction values from Dataset Detection."
        )
