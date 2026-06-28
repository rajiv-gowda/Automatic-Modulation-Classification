import streamlit as st

from modules.pdf_generator import create_pdf

def show_reports():
    st.title("Reports")
    st.success("Imported pdf_generator successfully!")
