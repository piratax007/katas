from unittest import TestCase
from unittest.mock import patch, call, Mock
import gui


class Test(TestCase):
    def test_set_colors_returns_a_dict_with_the_colors_to_use_in_the_cells(self):
        with patch('gui.curses') as mock_curses:
            init_pair_calls = [
                call(1, mock_curses.COLOR_CYAN, mock_curses.COLOR_WHITE),
                call(2, mock_curses.COLOR_CYAN, mock_curses.COLOR_BLACK),
                call(3, mock_curses.COLOR_CYAN, mock_curses.COLOR_RED)
            ]

            color_pair_calls = [
                call(1),
                call(2),
                call(3)
            ]

            gui.set_colors()

            mock_curses.init_pair.assert_has_calls(init_pair_calls)
            mock_curses.color_pair.assert_has_calls(color_pair_calls)

    def test_main_window_makes_the_graphic_board_representation(self):
        with patch("gui.curses") as mock_curses:
            real = gui.set_colors

            mock_stdsrc = Mock()
            gui.set_colors = Mock(return_value={
                "white": mock_curses.color_pair(1),
                "black": mock_curses.color_pair(2),
                "red": mock_curses.color_pair(3),
            })
            gui.main_window(mock_stdsrc)

            mock_stdsrc.clear.assert_called_once()
            gui.set_colors.assert_called_once()
            mock_stdsrc.addch.assert_called()
            mock_stdsrc.refresh.assert_called_once()
            mock_stdsrc.getkey.assert_called_once()
            gui.set_colors = real

# TODO
# Once implemented the while to run the simulation the last test does not run
