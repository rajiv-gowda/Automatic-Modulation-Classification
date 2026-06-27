import streamlit as st


def show_dashboard(model_status):

    st.title("📡 Automatic Modulation Classification System")

    st.caption(
        "AI-Based Wireless Signal Analysis & Real-Time Modulation Detection"
    )

    st.markdown("---")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "CNN Model",
        model_status
    )

    col2.metric(
        "Dataset",
        "RadioML2016.10A"
    )

    col3.metric(
        "Hardware",
        "Disconnected"
    )

    col4.metric(
        "Classes",
        "11"
    )

    st.markdown("---")

    st.subheader("Project Overview")

    st.info("""
This application provides:

✅ Dataset Detection

✅ Live Signal Detection

✅ Signal Analysis

✅ CNN Prediction

✅ PDF Report Generation

✅ Future RTL-SDR Support
""")

    st.markdown("---")

    st.subheader("Workflow")

    st.write("""
Dataset / Live Signal

↓

Preprocessing

↓

CNN Model

↓

Prediction

↓

Analysis

↓

PDF Report
""")
