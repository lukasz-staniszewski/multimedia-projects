import numpy as np
import matplotlib.pyplot as plt


def signal(n, A, okresN, n0=0):
    """Oblicza wartosc sygnalu z zadania

    Args:
        n (int): argument funkcji
        A (int): amplituda
        okresN (int): okres sygnalu
        n0 (int, optional): przesuniecie argumentu, domyslnie 0

    Returns:
        int: wartosc sygnalu dla danego n
    """
    return A * np.sin(2 * np.pi * (n - n0) / okresN)


if __name__ == "__main__":
    # wyznaczenie okresu i amplitudy
    okresN = 88
    A = 2
    # zdefiniowanie dziedziny
    domain = np.linspace(0, okresN - 1, okresN)
    # wyznaczenie próbek sygnalow
    signal0 = signal(domain, A, okresN)
    signalN4 = signal(domain, A, okresN, okresN / 4)
    signalN2 = signal(domain, A, okresN, okresN / 2)
    signal3N4 = signal(domain, A, okresN, 3 * okresN / 4)
    # plt.figure(1)
    # plt.title("SYGNAŁ s[n]:")
    # plt.stem(domain, signal0)
    # plt.figure(2)
    # plt.title("SYGNAŁ s[n-N/4]:")
    # plt.stem(domain, signalN4)
    # plt.figure(3)
    # plt.title("SYGNAŁ s[n-N/2]:")
    # plt.stem(domain, signalN2)
    # plt.figure(4)
    # plt.title("SYGNAŁ s[n-3N/4]:")
    # plt.stem(domain, signal3N4)
    # plt.show()
    # transformaty sygnalow
    signal0_fft = np.fft.fft(signal0) / okresN
    signalN4_fft = np.fft.fft(signalN4) / okresN
    signalN2_fft = np.fft.fft(signalN2) / okresN
    signal3N4_fft = np.fft.fft(signal3N4) / okresN
    # normalizacja
    for ind in range(signal0_fft.shape[0]):
        if np.abs(signal0_fft[ind]) < 1e-06:
            signal0_fft[ind] = 0.0
        if np.abs(signalN4_fft[ind]) < 1e-06:
            signalN4_fft[ind] = 0.0
        if np.abs(signalN2_fft[ind]) < 1e-06:
            signalN2_fft[ind] = 0.0
        if np.abs(signal3N4_fft[ind]) < 1e-06:
            signal3N4_fft[ind] = 0.0
    # plotowanie
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
