import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from modules.rtl_receiver import RTLReceiver

receiver = RTLReceiver()


def show_live_detection(model, classes):

    st.title("📡 Live Signal Detection")

    st.info(
        "This module is prepared for real-time hardware signal detection."
    )

    st.success("🟢 Live Detection System Ready")

    st.markdown("---")

    signal_type = st.selectbox(
        "Select Modulation",
        ["BPSK", "QPSK"]
    )

    if st.button("▶ Start Live Detection"):

        if signal_type == "BPSK":
            signal = receiver.capture_signal()
        else:
            signal = receiver.capture_signal()
        generator.save_signal(signal)

        st.success("Generating Live Signal...")

    # Rest of your existing code...)

        fig, ax = plt.subplots(figsize=(10,4))

        ax.plot(signal[:,0], label="I Channel")
        ax.plot(signal[:,1], label="Q Channel")

        ax.set_title("Live Signal")

        ax.legend()

        st.pyplot(fig)

        st.info(
            "Currently displaying simulated live IQ samples.\n\nLater this will read directly from your hardware."
        )
        signal_input = np.expand_dims(signal, axis=0)

        prediction = model.predict(signal_input, verbose=0)

        predicted_index = np.argmax(prediction)

        confidence = prediction[0][predicted_index] * 100

        predicted_class = classes[predicted_index]

        st.markdown("---")

        st.subheader("🤖 Live CNN Prediction")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Prediction",
            predicted_class
        )

        col2.metric(
            "Confidence",
            f"{confidence:.2f}%"
        )

        col3.metric(
            "Last Updated",
            datetime.now().strftime("%H:%M:%S")
        )
