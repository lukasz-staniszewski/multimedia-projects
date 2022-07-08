import numpy as np
import matplotlib.pyplot as plt


def px_per_sig_disc(sig, periodN):
    """Function returns the power calculated for periodic signals in the discrete domain.

    Args:
        sig [np.array]: signal as sample values
        periodN [int]: signal's period

    Returns:
        [int]: signal's power
    """
    summ = 0
    for val in sig:
        summ += abs(val) ** 2
    return summ / periodN


def parseval_dft(sig):
    """Function returns signal power using sum of the dft power spectra.

    Args:
        sig [np.array]: signal transform of a vector of complex numbers

    Returns:
        int: signal's power
    """
    summ = 0
    for val in sig:
        summ += np.abs(sig) ** 2
    return summ


def task_1a():
    """Function calculates and plots amplitude and phase spectrum, calculates power and checks Parseval's theorem."""
    # sig and period definition
    sig1 = np.array([2, 3, 1, 0])
    sig2 = np.array([0, 3, 1, 0])
    periodN = 4

    # transforms
    sig1_fft = np.fft.fft(sig1) / periodN
    sig2_fft = np.fft.fft(sig2) / periodN

    # determination of spectra
    spec_amp_sig1 = np.abs(sig1_fft)
    spec_amp_sig2 = np.abs(sig2_fft)
    spec_phase_sig1 = np.angle(sig1_fft)
    spec_phase_sig2 = np.angle(sig2_fft)

    # plotting
    plt.figure(1)
    plt.title("WIDMO AMPLITUDOWE SYGNAŁU s1={2, 3, 1, 0}")
    plt.xlabel("indeks widma (k)")
    plt.ylabel("amplituda widma (|S1N(K)|")
    plt.stem(spec_amp_sig1)

    plt.figure(2)
    plt.title("WIDMO FAZOWE SYGNAŁU s1={2, 3, 1, 0}")
    plt.xlabel("indeks widma (k)")
    plt.ylabel("faza widma (arg(S1N(K))")
    plt.stem(spec_phase_sig1)

    plt.figure(3)
    plt.title("WIDMO AMPLITUDOWE SYGNAŁU s2={0, 3, 1, 0}")
    plt.xlabel("indeks widma (k)")
    plt.ylabel("amplituda widma (|S2N(K)|")
    plt.stem(spec_amp_sig2)

    plt.figure(4)
    plt.title("WIDMO FAZOWE SYGNAŁU s2={0, 3, 1, 0}")
    plt.xlabel("indeks widma (k)")
    plt.ylabel("faza widma (arg(S2N(K))")
    plt.stem(spec_phase_sig2)
    plt.show()

    # power comparison
    print(
        "Power of sig1 based on signal:"
        f" {px_per_sig_disc(sig1, periodN)}"
    )
    print(
        "Power of sig1 based on power's spectrum: "
        f" {parseval_dft(sig1_fft)}"
    )
    print(
        "Power of sig2 based on signal:"
        f" {px_per_sig_disc(sig2, periodN)}"
    )
    print(
        "Power of sig2 based on power's spectrum:"
        f" {parseval_dft(sig2_fft)}"
    )


def task_1b():
    """Function checks discrete Fourier transform theorem of circular convolution."""
    # sig and period definition
    sig1 = np.array([2, 3, 1, 0])
    sig2 = np.array([0, 3, 1, 0])
    periodN = 4

    # transforms
    sig1_fft = np.fft.fft(sig1) / periodN
    sig2_fft = np.fft.fft(sig2) / periodN

    # convolution = transformation multiplication
    conv = sig1_fft * sig2_fft

    # reverse fft
    reverse_fft = np.fft.ifft(conv) * periodN
    for ind, number in enumerate(reverse_fft):
        print(f"s[{ind}] = {number}")


if __name__ == "__main__":
    task_1a()
    task_1b()
