import streamlit as st
import tensorflow as tf

st.title("Automatic Modulation Classification")
st.markdown("""
Upload an I/Q signal file (`.npy`) to classify one of 11 wireless modulation schemes.

**Supported modulations:** 8PSK, AM-DSB, AM-SSB, BPSK, CPFSK, GFSK, PAM4, QAM16, QAM64, QPSK, WBFM

**Expected input shape:** `(128, 2)`
""")

@st.cache_resource
def load_model():
    return tf.keras.models.load_model("amc_cnn_improved.keras")
model = load_model()

classes = ['8PSK', 'AM-DSB', 'AM-SSB', 'BPSK', 'CPFSK',
           'GFSK', 'PAM4', 'QAM16', 'QAM64', 'QPSK', 'WBFM']

st.sidebar.header("Model Information")

st.sidebar.markdown("""
- **Dataset:** RadioML 2016.10A
- **Model:** 1D CNN + Batch Normalization
- **Classes:** 11
- **Input Shape:** (128, 2)
- **Test Accuracy:** 83.11%
- **Framework:** TensorFlow / Keras
""")

uploaded_file = st.file_uploader("Upload a .npy signal file", type=["npy"])

if uploaded_file is not None:

    import numpy as np

    signal = np.load(uploaded_file)
    if signal.shape != (128, 2):
        st.error(f"Invalid signal shape: {signal.shape}. Expected (128, 2).")
        st.stop()

    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(10, 4))

    ax.plot(signal[:, 0], label="I Channel")
    ax.plot(signal[:, 1], label="Q Channel")

    ax.set_title("Uploaded I/Q Signal")
    ax.set_xlabel("Sample Index")
    ax.set_ylabel("Amplitude")
    ax.legend()

    st.pyplot(fig)

    st.caption(
        "Each uploaded signal contains 128 I/Q samples, matching the RadioML 2016.10A dataset format used during training."
    )

fig2, ax2 = plt.subplots(figsize=(5, 5))
    fig2, ax2 = plt.subplots(figsize=(5, 5))

    ax2.scatter(signal[:, 0], signal[:, 1], s=20, alpha=0.7)

    ax2.set_title("I/Q Constellation Diagram")
    ax2.set_xlabel("In-phase (I)")
    ax2.set_ylabel("Quadrature (Q)")
    ax2.grid(True)
    ax2.axis("equal")

    st.pyplot(fig2)

    signal = np.expand_dims(signal, axis=0)

    prediction = model.predict(signal)
    confidence = prediction.max() * 100
    predicted_class = prediction.argmax(axis=1)[0]

    st.success(
        f"Predicted Modulation: {classes[predicted_class]} ({confidence:.2f}% confidence)"
    )
