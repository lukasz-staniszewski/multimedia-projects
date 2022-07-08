import numpy as np
import matplotlib.pyplot as plt


def signal(t):
    """The function returns the signal value for the argument t.

    Args:
        t (int): argument - time

    Returns:
        int: signal's value in given t
    """
    return (
        0.1 * np.sin(2 * np.pi * 3000 * t)
        + 0.7 * np.sin(2 * np.pi * 8000 * t)
        + 0.9 * np.sin(2 * np.pi * 11000 * t)
    )


def perform_example(N):
    """Calculations when number of samples equals N

    Args:
        N (int): period
    """
    # sampling frequency definition
    fs = 48000

    # fs to Ts
    Ts = 1.0 / fs

    # samples and indexes domain
    domain_sample = np.arange(N) / fs
    domain_idx = domain_sample * fs

    sig = signal(domain_sample)

    # plotting sig
    plt.figure(1)
    plt.title(f"Sygnał s(nTs) dla liczby probek = {N} i fs = 48000Hz")
    plt.xlabel("Kolejne próbki (n)")
    plt.ylabel("Wartości sygnału s(nTs)")
    plt.plot(domain_idx, sig)

    # counting the spectrum of the real sampled signal
    spectrum_sampled = np.fft.rfft(sig) / (N / 2)

    # amplitude spectrum
    spectrum_sampled_amp = np.abs(spectrum_sampled)

    # frequency domain definitoion
    domain_f = np.fft.rfftfreq(N, Ts)

    # plotting amplitude spectrum
    plt.figure(2)
    plt.title(
        "Widmo amplitudowe sygnału rzeczywistego s(t) spróbkowanego na"
        f" {N} próbek z fs=48kHz"
    )
    plt.ylabel("Amplituda widma")
    plt.xlabel("Częstotliwość [Hz]")
    plt.stem(domain_f, spectrum_sampled_amp)

    # plotting power spectrum
    plt.figure(3)
    plt.title(
        f"Widmo mocy sygnału rzeczywistego s(t) spróbkowanego na {N}"
        " próbek z fs=48kHz"
    )
    plt.xlabel("Częstotliwość[Hz]")
    plt.ylabel("Amplituda widma")
    plt.stem(domain_f, spectrum_sampled_amp ** 2)
    plt.show()


def periods():
    """Function performs the necessary calculations - it checks whether the sampling time is a multiple of the sine periods."""
    probki = [2048, 3072]
    fs = 48000
    for N in probki:
        for fsin in [3000, 8000, 11000]:
            print(
                f"Liczba okresów sinusa o f={fsin}Hz dla {N} probek"
                f" wynosi: {(N / fs) / (1.0 / fsin)}"
            )


if __name__ == "__main__":
    N1 = 2048
    N2 = 3072
    perform_example(N1)
    perform_example(N2)
    periods()
