import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def senoidal(fs: "Hz", fo: "Hz", amp: "[0,1]", muestras: int, fase: "rad"):
    dominio = np.arange(muestras)
    imagen = amp * np.sin((2 * np.pi * fs * dominio / fo) + fase)
    return (imagen + amp) / 2


def triangular(fs: "Hz", fo: "Hz", amp: "[0,1]", muestras: int, fase: "rad"):
    forma_triangulo = 0.5
    dominio = np.arange(muestras)
    imagen = amp * signal.sawtooth((2 * np.pi * fs * dominio / fo) + fase, forma_triangulo)
    return (imagen + amp)/2


def cuadrada(fs: "Hz", fo: "Hz", amp: "[0,1]", muestras: int, fase: "rad"):
    forma_cuadrada = 0.5
    dominio = np.arange(muestras)
    imagen = amp * signal.square((2 * np.pi * fs * dominio / fo) + fase, forma_cuadrada)
    return (imagen + amp)/2


if __name__ == "__main__":
    print("SIMULACIONES")
    seno = senoidal(500, 100000, 1, 1000, 0)
    triangulo = triangular(2000, 100000, 0.5, 1000, np.pi)
    cuadrado = cuadrada(1000, 100000, 1, 1000, 0)
    plt.title("Ejercicio 1")
    plt.plot(seno, label='senoidal')
    plt.plot(triangulo, label='triangular')
    plt.plot(cuadrado, label='cuadrada')
    plt.grid()
    plt.legend()
    plt.ylabel('Imagen')
    plt.show()

    print("Experimentos")
    fs = 1000
    N = 1000
    fase = 0
    amp = 1
    sin01 = senoidal(0.1*fs, fs, amp, N, fase)
    sin11 = senoidal(1.1*fs, fs, amp, N, fase)
    plt.title("Ejercicio 2.1")
    plt.plot(sin01, label='0.1fs')
    plt.plot(sin11, label='1.1fs')
    plt.grid()
    plt.legend()
    plt.ylabel('Imagen')
    plt.show()

    sin101 = senoidal(0.49*fs, fs, amp, N, fase)
    sin111 = senoidal(1.51*fs, fs, amp, N, fase)
    plt.title("Ejercicio 2.2")
    plt.plot(sin101, label='0.49fs')
    plt.plot(sin111, label='1.51fs')
    plt.grid()
    plt.legend()
    plt.ylabel('Imagen')
    plt.show()
