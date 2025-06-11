# Juego de la Vida de Conway

- Este proyecto es una implementación del **Juego de la Vida**, un autómata celular propuesto por John Conway en 1970. Simula la evolución de una población en una grilla bidimensional, siguiendo reglas locales simples que producen comportamientos emergentes complejos.

---
## ¿Qué incluye este proyecto?

- Implementación orientada a objetos en Python.
- Animaciones de patrones clásicos: **Glider**, **Blinker**, **Toad**, **Block**.
- Visualización de la evolución del sistema con `matplotlib.animation`.
- Pruebas de rendimiento empíricas variando el tamaño de la grilla.
- Gráficas de rendimiento (lineal y log-log).
- Análisis y discusión de resultados.

---
## Requisitos

- Python 3.10 o superior
- Librerías:
  - `numpy`
  - `matplotlib`
- venv

## Instalación rápida:

```bash
pip install -r requirements.tx

```
---
### Cómo ejecutar la simulación:

( python game_of_life.py --pattern glider --size 64 --steps 100 --interval 200 ) 

- Parámetros disponibles:
  - pattern	Patrón inicial: glider, blinker, toad, block
  - size	Tamaño de la grilla (por ejemplo: 32, 128, 512)
  - steps	Número de generaciones a simular
  - interval	Velocidad de la animación en milisegundos

---
### Cómo generar las visualizaciones de rendimiento:

( python graficos.py )

- Se generarán dos gráficas:
   - Tiempo promedio por iteración según el tamaño de la grilla.
   - Gráfica log-log comparando el rendimiento empírico con complejidades teóricas:
     - O(n)
     - O(n log n)
     - O(n²)

---
### Capturas de pantalla y animaciones:

Puedes guardar tus animaciones como GIF dentro de la carpeta capturas/.
- Ejemplo de cómo guardar la animación desde el código:
    ( ani.save("capturas/glider.gif", writer='pillow'))

- Instala la librería necesaria si no la tienes:
    ( pip install pillow )

---
### Discusión de resultados:

- El tiempo de ejecución aumenta exponencialmente con el tamaño de la grilla, lo que concuerda con una complejidad O(n²).
- En la gráfica log-log, los datos empíricos se alinean con la curva teórica de O(n²).
- El principal cuello de botella es el método step(), que recorre cada celda en cada iteración.
- En grillas grandes (512×512 y 1024×1024), el rendimiento se reduce significativamente, indicando la necesidad de optimización.

---
### Conclusiones

- El Juego de la Vida es un excelente ejemplo de cómo reglas locales simples generan comportamientos globales complejos.
- Python permite implementar y visualizar fácilmente este tipo de sistemas dinámicos.
- Las pruebas empíricas confirmaron que el algoritmo tiene una complejidad cuadrática, acorde al análisis teórico.
- Como trabajo futuro, se podría implementar una versión paralela o vectorizada para mejorar el rendimiento, usando librerías como numba, multiprocessing o cupy.

Autores: Kristely Gabriela Carvajal Herra, Sophia Céspedes
Ingeniería en Ciencias de Datos — Universidad LEAD