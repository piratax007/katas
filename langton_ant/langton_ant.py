import board as b
import ant as a
from random import randint

if __name__ == "__main__":
    tablero = b.Board([[randint(0, 2) for _ in range(5)] for _ in range(5)])
    hormiga = a.Ant(0, 0, "N")

    tablero.draw(hormiga)

    for _ in range(10):
        hormiga.move(tablero)
        tablero.draw(hormiga)
