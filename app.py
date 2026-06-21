import streamlit as st
import tensorflow as tf

st.title("Automatic Modulation Classification")

@st.cache_resource
def load_model():
    return tf.keras.models.load_model("amc_cnn_filtered.keras")

model = load_model()
st.write("Model input shape:", model.input_shape)
uploaded_file = st.file_uploader("Upload a .npy signal file", type=["npy"])

st.success("Model loaded successfully!")
