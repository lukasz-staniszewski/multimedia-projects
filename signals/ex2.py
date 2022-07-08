import numpy as np
import matplotlib.pyplot as plt


def signal(n, A, periodN, n0=0):
    """Calculates signal value.

    Args:
        n (int): function argument
        A (int): amplitude
        periodN (int): period of signal
        n0 (int, optional): argument shift, defaults to 0

    Returns:
        int: signal value for n
    """
    return A * np.sin(2 * np.pi * (n - n0) / periodN)


def task_2():
    """Function checks effect of time shift on the form of the amplitude spectrum and phase spectrum of a discrete harmonic signal."""

    # amplitude and period definition
    periodN = 88
    A = 2

    # domain definition
    domain = np.linspace(0, periodN - 1, periodN)

    # determination of signal samples
    signal0 = signal(domain, A, periodN)
    signalN4 = signal(domain, A, periodN, periodN / 4)
    signalN2 = signal(domain, A, periodN, periodN / 2)
    signal3N4 = signal(domain, A, periodN, 3 * periodN / 4)

    # signals transform
    signal0_fft = np.fft.fft(signal0) / periodN
    signalN4_fft = np.fft.fft(signalN4) / periodN
    signalN2_fft = np.fft.fft(signalN2) / periodN
    signal3N4_fft = np.fft.fft(signal3N4) / periodN

    # normalization
    for ind in range(signal0_fft.shape[0]):
        if np.abs(signal0_fft[ind]) < 1e-06:
            signal0_fft[ind] = 0.0
        if np.abs(signalN4_fft[ind]) < 1e-06:
            signalN4_fft[ind] = 0.0
        if np.abs(signalN2_fft[ind]) < 1e-06:
            signalN2_fft[ind] = 0.0
        if np.abs(signal3N4_fft[ind]) < 1e-06:
            signal3N4_fft[ind] = 0.0

    # plotting
    plt.figure(5)
    plt.title("WIDMO AMPLITUDOWE s[n]")
    wid_amp_0 = np.abs(signal0_fft)
    plt.xlabel("indeks widma (k)")
    plt.ylabel("amplituda widma")
    plt.stem(wid_amp_0)

    plt.figure(6)
    plt.title("WIDMO FAZOWE s[n]")
    wid_faz_0 = np.angle(signal0_fft)
    plt.xlabel("indeks widma (k)")
    plt.ylabel("faza widma")
    plt.stem(wid_faz_0)

    plt.figure(7)
    plt.title("WIDMO AMPLITUDOWE s[n-N/4]")
    wid_amp_N4 = np.abs(signalN4_fft)
    plt.xlabel("indeks widma (k)")
    plt.ylabel("amplituda widma")
    plt.stem(wid_amp_N4)

    plt.figure(8)
    plt.title("WIDMO FAZOWE s[n-N/4]")
    wid_faz_N4 = np.angle(signalN4_fft)
    plt.xlabel("indeks widma (k)")
    plt.ylabel("faza widma")
    plt.stem(wid_faz_N4)

    plt.figure(9)
    plt.title("WIDMO AMPLITUDOWE s[n-N/2]")
    wid_amp_N2 = np.abs(signalN2_fft)
    plt.xlabel("indeks widma (k)")
    plt.ylabel("amplituda widma")
    plt.stem(wid_amp_N2)

    plt.figure(10)
    plt.title("WIDMO FAZOWE s[n-N/2]")
    wid_faz_N2 = np.angle(signalN2_fft)
    plt.xlabel("indeks widma (k)")
    plt.ylabel("faza widma")
    plt.stem(wid_faz_N2)

    plt.figure(11)
    plt.title("WIDMO AMPLITUDOWE s[n-3N/4]")
    wid_amp_3N4 = np.abs(signal3N4_fft)
    plt.xlabel("indeks widma (k)")
    plt.ylabel("amplituda widma")
    plt.stem(wid_amp_3N4)

    plt.figure(12)
    plt.title("WIDMO FAZOWE s[n-3N/4]")
    wid_faz_3N4 = np.angle(signal3N4_fft)
    plt.xlabel("indeks widma (k)")
    plt.ylabel("faza widma")
    plt.stem(wid_faz_3N4)
    plt.show()


if __name__ == "__main__":
    task_2()
