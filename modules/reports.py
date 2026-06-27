import streamlit as st
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def create_pdf():

    doc = SimpleDocTemplate("AMC_Report.pdf")
    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>AMC SYSTEM V2</b>", styles["Title"]))
    story.append(Paragraph("Automatic Modulation Classification Report", styles["Heading2"]))
    story.append(Paragraph("Predicted Modulation : QPSK", styles["BodyText"]))
    story.append(Paragraph("Confidence : 96.84%", styles["BodyText"]))
    story.append(Paragraph("Estimated SNR : 0.03 dB", styles["BodyText"]))
    story.append(Paragraph("Estimated Bandwidth : 118 bins", styles["BodyText"]))
    story.append(Paragraph("Signal Energy : 257.81", styles["BodyText"]))
    story.append(Paragraph("Peak Frequency Bin : 121", styles["BodyText"]))

    doc.build(story)


def show_reports():

    st.title("📄 RF Analysis Reports")

    st.info("Generate a professional AMC analysis report.")

    if st.button("Generate Report"):

        create_pdf()

        st.success("Report generated successfully.")

        with open("AMC_Report.pdf", "rb") as pdf_file:

            st.download_button(
                label="📥 Download PDF Report",
                data=pdf_file,
                file_name="AMC_Report.pdf",
                mime="application/pdf"
            )
