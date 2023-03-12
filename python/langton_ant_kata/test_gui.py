from unittest import TestCase
from unittest.mock import patch, Mock
import gui


class Test(TestCase):
    def test_main_window_makes_the_graphic_board_representation(self):
        with patch("gui.curses") as mock_curses:

            mock_curses.curs_set().return_value = 0
            mock_curses.configure_mock(LINES=10)
            mock_curses.configure_mock(COLS=10)
            mock_curses.delay_output()

            real_colors = gui.set_colors
            real_running_handler = gui.running_handler()

            mock_stdsrc = Mock()
            mock_stdsrc.clear()
            mock_stdsrc.addch()
            mock_stdsrc.refresh()
            gui.set_colors = Mock(return_value={
                "white": mock_curses.color_pair(1),
                "black": mock_curses.color_pair(2),
                "red": mock_curses.color_pair(3),
            })
            gui.running_handler = Mock(side_effect=[True, True, False])
            gui.main_window(mock_stdsrc)

            mock_stdsrc.clear.assert_called()
            gui.set_colors.assert_called()
            gui.running_handler.assert_called()
            mock_stdsrc.addch.assert_called()
            mock_stdsrc.refresh.assert_called()
            gui.set_colors = real_colors
            gui.running_handler = real_running_handler
