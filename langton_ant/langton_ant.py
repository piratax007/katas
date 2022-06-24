import board as b
import ant as a
from random import randint
from curses import wrapper
from time import sleep


def screen(stdscr):
    stdscr.clear()
    for _ in range(10):
        stdscr.clear()
        hormiga.move(tablero)
        tablero.draw(hormiga)
        stdscr.refresh()
        sleep(.5)

    stdscr.refresh()
    stdscr.getkey()


if __name__ == "__main__":
    tablero = b.Board([[randint(0, 2) for _ in range(5)] for _ in range(5)])
    hormiga = a.Ant(0, 0, "N")

    tablero.draw(hormiga)
    wrapper(screen)
    # for _ in range(10):
    #     hormiga.move(tablero)
    #     tablero.draw(hormiga)
