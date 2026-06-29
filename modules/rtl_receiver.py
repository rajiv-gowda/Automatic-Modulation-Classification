import numpy as np


class RTLReceiver:
    """
    RTL-SDR Receiver Module
    (Hardware integration will be added later.)
    """

    def __init__(self):
        self.sample_rate = 2.4e6
        self.center_frequency = 100e6
        self.gain = "auto"

    def capture_signal(self):
        """
        Temporary placeholder.

        Later this function will capture
        live I/Q samples from the RTL-SDR.
        """

        signal = np.random.randn(128, 2).astype(np.float32)

        return signal
