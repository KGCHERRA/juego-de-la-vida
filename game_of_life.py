import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class GameOfLife:
    def __init__(self, rows, cols, initial_state=None):
        self.rows = rows
        self.cols = cols
        if initial_state is not None:
            self.board = np.array(initial_state)
        else:
            self.board = np.random.randint(2, size=(rows, cols))

    def step(self):
        new_board = np.copy(self.board)
        for i in range(self.rows):
            for j in range(self.cols):
                total = np.sum(
                    self.board[max(i-1, 0):min(i+2, self.rows),
                               max(j-1, 0):min(j+2, self.cols)]
                ) - self.board[i, j]

                if self.board[i, j] == 1:
                    if total < 2 or total > 3:
                        new_board[i, j] = 0
                else:
                    if total == 3:
                        new_board[i, j] = 1
        self.board = new_board

    def run(self, steps):
        """Ejecuta `steps` generaciones."""
        for _ in range(steps):
            self.step()

    def get_state(self):
        """Devuelve el estado actual del tablero."""
        return self.board


def animate_game(game, steps=100, interval=200):
    """Muestra una animación de la evolución del juego."""
    fig, ax = plt.subplots()
    img = ax.imshow(game.get_state(), cmap='binary', interpolation='nearest')

    def update(_):
        game.step()
        img.set_data(game.get_state())
        return [img]

    ani = animation.FuncAnimation(fig, update, frames=steps, interval=interval, blit=True)
    plt.show()


def glider_pattern(size=32):
    """Glider en una grilla size x size."""
    pattern = np.zeros((size, size), int)
    g = np.array([[0, 1, 0],
                  [0, 0, 1],
                  [1, 1, 1]])
    pattern[1:4, 1:4] = g
    return pattern


def blinker_pattern(size=32):
    """Oscilador Blinker."""
    pattern = np.zeros((size, size), int)
    mid = size // 2
    pattern[mid, mid-1:mid+2] = 1
    return pattern


def toad_pattern(size=32):
    """Oscilador Toad."""
    pattern = np.zeros((size, size), int)
    mid = size // 2
    pattern[mid, mid-2:mid+1] = 1
    pattern[mid+1, mid-1:mid+2] = 1
    return pattern


def block_pattern(size=32):
    """Estructura estática Block."""
    pattern = np.zeros((size, size), int)
    mid = size // 2
    pattern[mid:mid+2, mid:mid+2] = 1
    return pattern


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Juego de la Vida de Conway")
    parser.add_argument("--pattern", choices=["glider", "blinker", "toad", "block"], default="glider")
    parser.add_argument("--size", type=int, default=32, help="Tamaño de la grilla")
    parser.add_argument("--steps", type=int, default=100, help="Número de generaciones")
    parser.add_argument("--interval", type=int, default=200, help="Intervalo de animación (ms)")
    args = parser.parse_args()

    patterns = {
        "glider": glider_pattern,
        "blinker": blinker_pattern,
        "toad": toad_pattern,
        "block": block_pattern
    }

    initial = patterns[args.pattern](args.size)
    game = GameOfLife(rows=args.size, cols=args.size, initial_state=initial)
    animate_game(game, steps=args.steps, interval=args.interval)

