import streamlit as st
import tensorflow as tf

st.title("Automatic Modulation Classification")

@st.cache_resource
def load_model():
    return tf.keras.models.load_model("amc_cnn_filtered.keras")

model = load_model()

st.success("Model loaded successfully!")
