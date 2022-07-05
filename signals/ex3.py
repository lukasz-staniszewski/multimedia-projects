import numpy as np
import matplotlib.pyplot as plt


def signal(n, A, okresN):
    """Zwraca wartosc sygnalu o amplitudzie A i okresie N dla argumentu n

    Args:
        n (int): argument
        A (int): amplituda
        okresN (int): okres

    Returns:
        int: wartosc sygnalu
    """
    return A * (1 - (n % okresN) / okresN)


def normalize(widm):
    """Funkcja normalizująca przekształcenie

    Args:
        widm (np.array): wektor przekształceń

    Returns:
        np.array: znormalizowany wektor przekształceń
    """
    for ind in range(widm.shape[0]):
        if np.abs(widm[ind]) < 1e-06:
            widm[ind] = 0
    return widm


if __name__ == "__main__":
    # zdefiniowanie amplitudy, okresu, dziedziny i sygnalu
    A = 4
    okresN = 12
    domain0 = np.linspace(0, okresN - 1, okresN)
    values0 = signal(domain0, A, okresN)

    # plt.figure(1)
    # plt.title("SYGNAŁ s[n] BEZ DOPEŁNIENIA:")
    # plt.stem(domain0, values0)

    # plt.figure(2)
    # plt.title("SYGNAŁ s[n] Z DOPEŁNIENIEM N:")
    # domainN = np.linspace(0, okresN * 2 - 1, okresN * 2)
    valuesN = np.append(values0, np.zeros(okresN))     # dopelnienie zerami
    # plt.stem(domainN, valuesN)

    # plt.figure(3)
    # plt.title("SYGNAŁ s[n] Z DOPEŁNIENIEM 4N:")
    # domain4N = np.linspace(0, okresN * 5 - 1, okresN * 5)
    values4N = np.append(values0, np.zeros(4 * okresN))    # dopelnienie zerami
    # plt.stem(domain4N, values4N)

    # plt.figure(4)
    # plt.title("SYGNAŁ s[n] Z DOPEŁNIENIEM 9N:")
    # domain9N = np.linspace(0, okresN * 10 - 1, okresN * 10)
    values9N = np.append(values0, np.zeros(9 * okresN))     # dopelnienie zerami
    # plt.stem(domain9N, values9N)

    # transformaty
    widm_0 = np.fft.fft(values0) / okresN
    widm_N = np.fft.fft(valuesN) / (2 * okresN)
    widm_4N = np.fft.fft(values4N) / (5 * okresN)
    widm_9N = np.fft.fft(values9N) / (10 * okresN)
    # normalizacje
    normalize(widm_0)
    normalize(widm_N)
    normalize(widm_4N)
    normalize(widm_9N)
    # wyznaczenie widm
    widm_amp_0 = np.abs(widm_0)
    widm_faz_0 = np.angle(widm_0)

    widm_amp_N = np.abs(widm_N)
    widm_faz_N = np.angle(widm_N)

    widm_amp_4N = np.abs(widm_4N)
    widm_faz_4N = np.angle(widm_4N)

    widm_amp_9N = np.abs(widm_9N)
    widm_faz_9N = np.angle(widm_9N)
    # plotowanie
    plt.figure(5)
    plt.title("WIDMO AMPLITUDOWE s[n] BEZ DOPEŁNIENIA:")
    plt.xlabel("indeks widma (k)")
    plt.ylabel("amplituda widma")
    plt.stem(widm_amp_0)

    plt.figure(6)
    plt.title("WIDMO FAZOWE s[n] BEZ DOPEŁNIENIA:")
    plt.stem(widm_faz_0)
    plt.xlabel("indeks widma (k)")
    plt.ylabel("faza widma")

    plt.figure(7)
    plt.title("WIDMO AMPLITUDOWE s[n] Z DOPEŁNIENIEM N:")
    plt.xlabel("indeks widma (k)")
    plt.ylabel("amplituda widma")
    plt.stem(widm_amp_N)

    plt.figure(8)
    plt.title("WIDMO FAZOWE s[n] Z DOPEŁNIENIEM N:")
    plt.stem(widm_faz_N)
    plt.xlabel("indeks widma (k)")
    plt.ylabel("faza widma")

    plt.figure(9)
    plt.title("WIDMO AMPLITUDOWE s[n] Z DOPEŁNIENIEM 4N:")
    plt.stem(widm_amp_4N)
    plt.xlabel("indeks widma (k)")
    plt.ylabel("amplituda widma")

    plt.figure(10)
    plt.title("WIDMO FAZOWE s[n] Z DOPEŁNIENEM 4N:")
    plt.stem(widm_faz_4N)
    plt.xlabel("indeks widma (k)")
    plt.ylabel("faza widma")

    plt.figure(11)
    plt.title("WIDMO AMPLITUDOWE s[n] Z DOPEŁNIENIEM 9N:")
    plt.stem(widm_amp_9N)
    plt.xlabel("indeks widma (k)")
    plt.ylabel("amplituda widma")

    plt.figure(12)
    plt.title("WIDMO FAZOWE s[n] Z DOPEŁNIENIEM 9N:")
    plt.stem(widm_faz_9N)
    plt.xlabel("indeks widma (k)")
    plt.ylabel("faza widma")
    plt.show()
