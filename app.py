import streamlit as st
import tensorflow as tf

st.title("Automatic Modulation Classification")

@st.cache_resource
def load_model():
    return tf.keras.models.load_model("amc_cnn_filtered.keras")

model = load_model()
classes = ['8PSK', 'AM-DSB', 'AM-SSB', 'BPSK', 'CPFSK',
           'GFSK', 'PAM4', 'QAM16', 'QAM64', 'QPSK', 'WBFM']
uploaded_file = st.file_uploader("Upload a .npy signal file", type=["npy"])

if uploaded_file is not None:

    import numpy as np

    signal = np.load(uploaded_file)

    signal = np.expand_dims(signal, axis=0)

    prediction = model.predict(signal)
    predicted_class = prediction.argmax(axis=1)[0]

    st.success(f"Predicted Modulation: {classes[predicted_class]}")

