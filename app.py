import streamlit as st
import tensorflow as tf

st.title("Automatic Modulation Classification")

@st.cache_resource
def load_model():
    return tf.keras.models.load_model("amc_cnn_filtered.keras")

model = load_model()
classes = ['8PSK', 'AM-DSB', 'AM-SSB', 'BPSK', 'CPFSK',
           'GFSK', 'PAM4', 'QAM16', 'QAM64', 'QPSK', 'WBFM']
st.write("Model input shape:", model.input_shape)
uploaded_file = st.file_uploader("Upload a .npy signal file", type=["npy"])

if uploaded_file is not None:
    st.success("File uploaded successfully!")

    import numpy as np

    signal = np.load(uploaded_file)

    st.write("Signal shape:", signal.shape)
    signal = np.expand_dims(signal, axis=0)

prediction = model.predict(signal)
predicted_class = prediction.argmax(axis=1)[0]

st.write("Predicted class index:", predicted_class)

st.write("Prediction shape:", prediction.shape)

st.success("Model loaded successfully!")
