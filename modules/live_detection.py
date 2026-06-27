import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


def show_live_detection(model, classes):

    st.title("📡 Live Signal Detection")

    st.info(
        "This module is prepared for real-time hardware signal detection."
    )

    st.success("🟢 Live Detection System Ready")

    st.markdown("---")

    if st.button("▶ Start Live Detection"):

        st.success("Generating Live Signal...")

        signal = np.random.normal(
            0,
            1,
            (128,2)
        )

        fig, ax = plt.subplots(figsize=(10,4))

        ax.plot(signal[:,0], label="I Channel")
        ax.plot(signal[:,1], label="Q Channel")

        ax.set_title("Live Signal")

        ax.legend()

        st.pyplot(fig)

        st.info(
            "Currently displaying simulated live IQ samples.\n\nLater this will read directly from your hardware."
        )
