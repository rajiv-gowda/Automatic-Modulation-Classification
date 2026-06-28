import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft
from matplotlib import mlab
from matplotlib.colors import LogNorm
print("Loaded signal_analysis.py")


def show_signal_analysis():

    st.title("📊 Signal Analysis")

    st.info(
        "This module provides advanced RF signal analysis."
    )

    st.success("Signal Analysis Module Ready")

    st.markdown("---")

    st.write(
        "FFT Spectrum, Power Spectrum, SNR Estimation and Bandwidth Analysis will be displayed here."
    )
    signal = np.load("sample_signal.npy")
    fft_data = np.abs(fft(signal[:, 0]))

    fig, ax = plt.subplots(figsize=(10, 4))

    ax.plot(fft_data, label="FFT Spectrum")

    threshold = np.max(fft_data) * 0.1
    indices = np.where(fft_data > threshold)[0]

    if len(indices) > 0:
        ax.axvspan(
            indices[0],
            indices[-1],
            color="orange",
            alpha=0.3,
            label="Estimated Bandwidth"
        )

    ax.set_title("FFT Spectrum")
    ax.set_xlabel("Frequency Bin")
    ax.set_ylabel("Magnitude")
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)
    # ===========================
# Power Spectrum
# ===========================

    st.subheader("Power Spectrum")

    power = fft_data ** 2

    fig_power, ax_power = plt.subplots(figsize=(10, 4))

    ax_power.plot(power, color="red")

    ax_power.set_title("Power Spectrum")

    ax_power.set_xlabel("Frequency Bin")

    ax_power.set_ylabel("Power")

    ax_power.grid(True)

    plt.tight_layout()

    fig_power.savefig(
        "power_spectrum.png",
        dpi=300,
        bbox_inches="tight"
    )

    st.pyplot(fig_power)
    fig.savefig("fft.png")

    st.session_state["fft_plot"] = "fft.png"
    st.subheader("Signal Quality")

    signal_power = np.mean(signal[:, 0] ** 2)
    noise_power = np.var(signal[:, 0] - np.mean(signal[:, 0]))

    snr = 10 * np.log10(signal_power / (noise_power + 1e-10))

    st.metric("Estimated SNR", f"{snr:.2f} dB")
    st.session_state["snr"] = snr
    st.subheader("Spectrogram")

    fig4, ax4 = plt.subplots(figsize=(10, 4))

    ax4.specgram(
        signal[:, 0],
        NFFT=32,
        Fs=1,
        noverlap=16
    )

    ax4.set_title("Signal Spectrogram")
    ax4.set_xlabel("Time")
    ax4.set_ylabel("Frequency")

    st.pyplot(fig4)
    fig4.savefig("spectrogram.png")

    st.session_state["spectrogram_plot"] = "spectrogram.png"
    st.subheader("Bandwidth Estimation")

    threshold = np.max(fft_data) * 0.1

    indices = np.where(fft_data > threshold)[0]

    if len(indices) > 0:
        bandwidth = indices[-1] - indices[0]
    else:
        bandwidth = 0

    st.metric("Estimated Bandwidth", f"{bandwidth} bins")
    st.session_state["bandwidth"] = bandwidth
    st.subheader("Signal Energy")

    energy = np.sum(signal[:, 0]**2 + signal[:, 1]**2)

    st.metric("Total Signal Energy", f"{energy:.2f}")
    st.session_state["energy"] = energy
    st.subheader("Peak Frequency")

    peak_index = np.argmax(fft_data)
    peak_value = fft_data[peak_index]
    st.session_state["peak_frequency"] = peak_index

    col1, col2 = st.columns(2)

    col1.metric("Peak Frequency Bin", peak_index)
    col2.metric("Peak Magnitude", f"{peak_value:.2f}")
    st.subheader("Waterfall Spectrum")

    fig5, ax5 = plt.subplots(figsize=(10, 5))

    ax5.specgram(
        signal[:, 0],
        NFFT=16,
        Fs=1,
        noverlap=8,
        scale="dB"
    )

    ax5.set_title("Waterfall Spectrum")
    ax5.set_xlabel("Time")
    ax5.set_ylabel("Frequency")

    st.pyplot(fig5)
    fig5.savefig("waterfall.png")

    st.session_state["waterfall_plot"] = "waterfall.png"

