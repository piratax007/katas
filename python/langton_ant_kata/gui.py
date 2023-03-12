import curses
from random import randint

import board as b
import ant as a


def running_handler() -> bool:
    return True


def set_colors() -> dict:
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_RED)

    return {
        "white": curses.color_pair(1),
        "black": curses.color_pair(2),
        "red": curses.color_pair(3),
    }


def main_window(stdsrc):
    stdsrc.clear()
    curses.curs_set(False)

    colors = set_colors()
    rows = curses.LINES - 1
    cols = curses.COLS - 1
    b_ = b.Board(rows, cols)

    for row in b_.grid:
        for cell in row:
            stdsrc.addch(cell.position[0], cell.position[1], " ", colors[cell.current_color])

    ant = a.Ant([randint(0, rows-1), randint(0, cols-1)], ("N", "E", "S", "W")[randint(0, 3)])

    while running_handler():
        current_cell = b_.grid[ant.position[0]][ant.position[1]]
        current_direction = ant.direction
        current_position = ant.position
        ant.direction, ant.position = b_.apply_rules(current_direction, current_position)
        stdsrc.addch(current_cell.position[0], current_cell.position[1], " ", colors[current_cell.current_color])
        stdsrc.refresh()
        curses.delay_output(250)
