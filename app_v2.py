import streamlit as st
from modules.dataset_detection import show_dataset_detection
from modules.model_loader import initialize
from modules.dashboard import show_dashboard
from modules.live_detection import show_live_detection
from modules.signal_analysis import show_signal_analysis
from modules.reports import show_reports
from modules.about import show_about


# ===================================
# Page Configuration
# ===================================

st.set_page_config(
    page_title="Automatic Modulation Classification System V2",
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

st.sidebar.title("📡 Automatic Modulation Classification System V2")

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
    show_dataset_detection(model, classes)

elif page == "📡 Live Signal Detection":
    show_live_detection(model, classes)

elif page == "📊 Signal Analysis":
    show_signal_analysis()

elif page == "📄 Reports":
    show_reports()

elif page == "ℹ️ About":
    show_about()
