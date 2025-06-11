import time
import numpy as np
import matplotlib.pyplot as plt
from game_of_life import GameOfLife

def medir_rendimiento(tamanos, pasos=10):
    """Mide el tiempo promedio de `pasos` iteraciones para cada tamaño de grilla."""
    tiempos = []
    for n in tamanos:
        juego = GameOfLife(n, n)
        inicio = time.perf_counter()
        juego.run(pasos)
        fin = time.perf_counter()
        tiempos.append((fin - inicio) / pasos)
    return np.array(tiempos)

def graficar(tamanos, tiempos):
    """Grafica resultados empíricos junto a curvas teóricas."""
    # Curvas de referencia
    teoricos = {
        "O(n)": tiempos[0] * (tamanos / tamanos[0]),
        "O(n log n)": tiempos[0] * (tamanos * np.log(tamanos) / (tamanos[0] * np.log(tamanos[0]))),
        "O(n²)": tiempos[0] * (tamanos**2 / tamanos[0]**2)
    }

    # Gráfica lineal
    plt.figure(figsize=(10, 5))
    plt.plot(tamanos, tiempos, 'o-', label='Empírico')
    for label, curve in teoricos.items():
        plt.plot(tamanos, curve, '--', label=label)
    plt.xlabel('n (lado de la grilla)')
    plt.ylabel('Tiempo medio por iteración (s)')
    plt.title('Rendimiento vs complejidad teórica')
    plt.grid(True)
    plt.legend()
    plt.show()

    # Gráfica log-log
    plt.figure(figsize=(10, 5))
    plt.loglog(tamanos, tiempos, 'o-', label='Empírico')
    for label, curve in teoricos.items():
        plt.loglog(tamanos, curve, '--', label=label)
    plt.xlabel('n (log scale)')
    plt.ylabel('Tiempo medio (log scale)')
    plt.title('Complejidad empírica (log-log)')
    plt.grid(True, which="both", ls="--")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    # Incluimos hasta 1024×1024
    tamanos = [32, 64, 128, 256, 512, 1024]
    tiempos = medir_rendimiento(tamanos, pasos=10)
    graficar(np.array(tamanos), tiempos)