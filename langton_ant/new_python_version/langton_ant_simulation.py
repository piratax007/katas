#!/usr/bin/env python3

from curses import wrapper
import gui


if __name__ == '__main__':
    wrapper(gui.main_window)
