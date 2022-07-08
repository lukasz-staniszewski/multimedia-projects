import numpy as np
import matplotlib.pyplot as plt


def signal(n, A, periodN):
    """Returns the value of a signal with amplitude A and period N for argument n.

    Args:
        n (int): argument
        A (int): amplitude
        periodN (int): period of signal

    Returns:
        int: signals value
    """
    return A * (1 - (n % periodN) / periodN)


def normalize(phase):
    """Transformation normalising function

    Args:
        phase (np.array): transformation vector

    Returns:
        np.array: normalized transformation vector
    """
    for ind in range(phase.shape[0]):
        if np.abs(phase[ind]) < 1e-06:
            phase[ind] = 0
    return phase


def task_3():
    """Function checks effect of zero padding on the form of the amplitude spectrum and phase spectrum
    of a discrete signal."""
    # amplitude, period, domain and signal definition
    A = 4
    periodN = 12
    domain0 = np.linspace(0, periodN - 1, periodN)
    values0 = signal(domain0, A, periodN)

    # zero padding
    valuesN = np.append(values0, np.zeros(periodN))
    values4N = np.append(values0, np.zeros(4 * periodN))
    values9N = np.append(values0, np.zeros(9 * periodN))

    # transformations
    spectrum_0 = np.fft.fft(values0) / periodN
    spectrum_N = np.fft.fft(valuesN) / (2 * periodN)
    spectrum_4N = np.fft.fft(values4N) / (5 * periodN)
    spectrum_9N = np.fft.fft(values9N) / (10 * periodN)

    # normalizations
    normalize(spectrum_0)
    normalize(spectrum_N)
    normalize(spectrum_4N)
    normalize(spectrum_9N)

    # spectrum
    spectrum_amp_0 = np.abs(spectrum_0)
    spectrum_faz_0 = np.angle(spectrum_0)

    spectrum_amp_N = np.abs(spectrum_N)
    spectrum_faz_N = np.angle(spectrum_N)

    spectrum_amp_4N = np.abs(spectrum_4N)
    spectrum_faz_4N = np.angle(spectrum_4N)

    spectrum_amp_9N = np.abs(spectrum_9N)
    spectrum_faz_9N = np.angle(spectrum_9N)

    # plotting
    plt.figure(5)
    plt.title("spectrumO AMPLITUDOWE s[n] BEZ DOPEŁNIENIA:")
    plt.xlabel("indeks spectruma (k)")
    plt.ylabel("amplituda spectruma")
    plt.stem(spectrum_amp_0)

    plt.figure(6)
    plt.title("spectrumO FAZOWE s[n] BEZ DOPEŁNIENIA:")
    plt.stem(spectrum_faz_0)
    plt.xlabel("indeks spectruma (k)")
    plt.ylabel("faza spectruma")

    plt.figure(7)
    plt.title("spectrumO AMPLITUDOWE s[n] Z DOPEŁNIENIEM N:")
    plt.xlabel("indeks spectruma (k)")
    plt.ylabel("amplituda spectruma")
    plt.stem(spectrum_amp_N)

    plt.figure(8)
    plt.title("spectrumO FAZOWE s[n] Z DOPEŁNIENIEM N:")
    plt.stem(spectrum_faz_N)
    plt.xlabel("indeks spectruma (k)")
    plt.ylabel("faza spectruma")

    plt.figure(9)
    plt.title("spectrumO AMPLITUDOWE s[n] Z DOPEŁNIENIEM 4N:")
    plt.stem(spectrum_amp_4N)
    plt.xlabel("indeks spectruma (k)")
    plt.ylabel("amplituda spectruma")

    plt.figure(10)
    plt.title("spectrumO FAZOWE s[n] Z DOPEŁNIENEM 4N:")
    plt.stem(spectrum_faz_4N)
    plt.xlabel("indeks spectruma (k)")
    plt.ylabel("faza spectruma")

    plt.figure(11)
    plt.title("spectrumO AMPLITUDOWE s[n] Z DOPEŁNIENIEM 9N:")
    plt.stem(spectrum_amp_9N)
    plt.xlabel("indeks spectruma (k)")
    plt.ylabel("amplituda spectruma")

    plt.figure(12)
    plt.title("spectrumO FAZOWE s[n] Z DOPEŁNIENIEM 9N:")
    plt.stem(spectrum_faz_9N)
    plt.xlabel("indeks spectruma (k)")
    plt.ylabel("faza spectruma")
    plt.show()


if __name__ == "__main__":
    task_3()
