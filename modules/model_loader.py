import tensorflow as tf
import numpy as np
import streamlit as st


MODEL_PATH = "amc_cnn_improved.keras"
LABEL_PATH = "label_classes.npy"


@st.cache_resource
def load_model():
    """
    Load CNN model only once.
    """
    return tf.keras.models.load_model(MODEL_PATH)


@st.cache_data
def load_classes():
    """
    Load modulation class labels.
    """
    return np.load(LABEL_PATH, allow_pickle=True)


def initialize():
    """
    Returns:
        model
        classes
        model_status
    """

    try:
        model = load_model()
        status = "✅ Loaded"
    except Exception:
        model = None
        status = "❌ Not Loaded"

    try:
        classes = load_classes()
    except Exception:
        classes = []

    return model, classes, status
