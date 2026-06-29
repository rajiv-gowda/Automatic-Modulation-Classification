import numpy as np


class SignalGenerator:
    def __init__(self, num_symbols=128):
        self.num_symbols = num_symbols
    def generate_bpsk(self):
        """
        Generate BPSK I/Q samples
        """

        bits = np.random.randint(0, 2, self.num_symbols)

        symbols = 2 * bits - 1

        I = symbols.astype(np.float32)

        Q = np.zeros(self.num_symbols, dtype=np.float32)

        iq = np.column_stack((I, Q))

        return iq
    def generate_qpsk(self):
        """
        Generate QPSK I/Q samples
        """

        bits = np.random.randint(0, 4, self.num_symbols)

        mapping = {
            0: (1, 1),
            1: (-1, 1),
            2: (-1, -1),
            3: (1, -1)
        }

        iq = np.array([mapping[b] for b in bits], dtype=np.float32)

        return iq
    def save_signal(self, signal, filename="live_signal.npy"):
        np.save(filename, signal)

        print(f"Signal saved as {filename}")
if __name__ == "__main__":

    generator = SignalGenerator()

    print("1. Generate BPSK")
    print("2. Generate QPSK")

    choice = input("Enter choice: ")

    if choice == "1":
        signal = generator.generate_bpsk()

    elif choice == "2":
        signal = generator.generate_qpsk()

    else:
        print("Invalid choice")
        exit()

    generator.save_signal(signal)

    print(signal[:10])
