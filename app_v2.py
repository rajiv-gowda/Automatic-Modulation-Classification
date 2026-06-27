import streamlit as st

from modules.model_loader import initialize
from modules.dashboard import show_dashboard

# ===================================
# Page Configuration
# ===================================

st.set_page_config(
    page_title="AMC System V2",
    page_icon="📡",
    layout="wide"
)

# ===================================
# Load Model
# ===================================

model, classes, model_status = initialize()

# ===================================
# Sidebar
# ===================================

st.sidebar.title("📡 AMC System V2")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "📂 Dataset Detection",
        "📡 Live Signal Detection",
        "📊 Signal Analysis",
        "📄 Reports",
        "ℹ️ About"
    ]
)

# ===================================
# Navigation
# ===================================

if page == "🏠 Dashboard":
    show_dashboard(model_status)

elif page == "📂 Dataset Detection":
    st.title("📂 Dataset Detection")
    st.info("Coming in Part 2")

elif page == "📡 Live Signal Detection":
    st.title("📡 Live Signal Detection")
    st.info("Coming Soon")

elif page == "📊 Signal Analysis":
    st.title("📊 Signal Analysis")
    st.info("Coming Soon")

elif page == "📄 Reports":
    st.title("📄 Reports")
    st.info("Coming Soon")

elif page == "ℹ️ About":
    st.title("ℹ️ About")
    st.info("Coming Soon")
