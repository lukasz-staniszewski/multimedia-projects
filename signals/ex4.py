import numpy as np
import matplotlib.pyplot as plt


def signal(t):
    """Funkcja zwraca wartosc sygnalu dla argumentu t

    Args:
        t (int): argument - czas

    Returns:
        int: wartosc sygnalu w danym t
    """
    return 0.1 * np.sin(2 * np.pi * 3000 * t) + 0.7 * np.sin(2 * np.pi * 8000 * t) + 0.9 * np.sin(2 * np.pi * 11000 * t)


def przykladN1():
    """Obliczenia dla przykladu z liczba probek = N1
    """
    # zdefiniowanie okresu, czestotliwosci probkowania
    N = 2048
    fs = 48000
    # przeksztalcenie na Ts
    Ts = 1.0 / fs
    # zdefiniowanie dziedzny probek w kontekscie czasow probkowania
    dziedzina_probek = np.arange(N) / fs
    # wyliczenie sygnalu
    sygnal = signal(dziedzina_probek)
    # dziedzina indeksow
    dziedzina_n = dziedzina_probek * fs
    # plotowanie sygnalu
    plt.figure(1)
    plt.title("Sygnał s(nTs) dla liczby probek = N1 i fs = 48000Hz")
    plt.xlabel("Kolejne próbki (n)")
    plt.ylabel("Wartości sygnału s(nTs)")
    plt.plot(dziedzina_n, sygnal)
    # liczenie widma rzeczywistego sygnalu sprobkowanego
    widmo_sprobkowanego = np.fft.rfft(sygnal) / (N / 2)
    # widmo amplitudowe
    widmo_amp_sprobkowanego = np.abs(widmo_sprobkowanego)
    # wyznaczenie dziedziny czestotliwosci
    dziedzina_f = np.fft.rfftfreq(N, Ts)
    # plot widma amplitudowego
    plt.figure(2)
    plt.title("Widmo amplitudowe sygnału rzeczywistego s(t) spróbkowanego na N1 próbek z fs=48kHz")
    plt.ylabel("Amplituda widma")
    plt.xlabel("Częstotliwość [Hz]")
    plt.stem(dziedzina_f, widmo_amp_sprobkowanego)
    # plot widma mocy
    plt.figure(3)
    plt.title("Widmo mocy sygnału rzeczywistego s(t) spróbkowanego na N1 próbek z fs=48kHz")
    plt.xlabel("Częstotliwość[Hz]")
    plt.ylabel("Amplituda widma")
    plt.stem(dziedzina_f, widmo_amp_sprobkowanego**2)
    plt.show()


def przykladN2():
    """Obliczenia dla przykladu z liczba probek = N2
    """
    # okres, czestotliwosc probkowania, odstep miedzy probkami
    N = 3072
    fs = 48000
    Ts = 1 / fs
    # dziedzina czasu dla probek:
    dziedzina_probek = np.arange(N) / fs
    # sygnal
    sygnal = signal(dziedzina_probek)
    # dziedzina probek
    dziedzina_n = dziedzina_probek * fs
    # plotowanie sygnalu
    plt.figure(1)
    plt.title("Sygnał s(nTs) dla liczby próbek = N2 i fs = 48000Hz")
    plt.xlabel("Kolejne próbki (n)")
    plt.ylabel("Wartości sygnału s(nTs)")
    plt.plot(dziedzina_n, sygnal)
    # transformata sprobkowanego sygnalu rzeczywistego
    widmo_sprobkowanego = np.fft.rfft(sygnal) / (N / 2)
    # widmo amplitudowe 
    widmo_amp_sprobkowanego = np.abs(widmo_sprobkowanego)
    # dziedzina czestotliwości
    dziedzina_f = np.fft.rfftfreq(N, Ts)
    # plotowanie widma amplitudowego
    plt.figure(2)
    plt.title("Widmo amplitudowe sygnału rzeczywistego s(t) spróbkowanego na N2 próbek z fs=48kHz")
    plt.ylabel("Amplituda widma")
    plt.xlabel("Częstotliwość [Hz]")
    plt.stem(dziedzina_f, widmo_amp_sprobkowanego)
    # plotowanie widma mocy
    plt.figure(3)
    plt.title("Widmo mocy sygnału rzeczywistego s(t) spróbkowanego na N2 próbek z fs=48kHz")
    plt.xlabel("Częstotliwość[Hz]")
    plt.ylabel("Amplituda widma")
    plt.stem(dziedzina_f, widmo_amp_sprobkowanego**2)
    plt.show()


def okresy():
    """Funkcja wykonuje niezbedne obliczenia: sprawdza czy czas probkowania jest wielokrotnoscia okresow sinusow
    """
    probki = [2048, 3072]
    fs = 48000
    for N in probki:
        for fsin in ([3000, 8000, 11000]):
            print(f"Liczba okresów sinusa o f={fsin}Hz dla {N} probek wynosi: {(N / fs) / (1.0 / fsin)}")


if __name__ == "__main__":
    przykladN1()
    przykladN2()
    okresy()
