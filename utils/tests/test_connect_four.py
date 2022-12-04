import pytest, numpy as np
from unittest.mock import patch, call, Mock
import builtins
import sys
from utils.connect_four import ConnectFour


class TestConnectFour:
    def test_init(self):
        """
        Test that the game is initialized correctly
        :return:
        """
        game = ConnectFour()
        assert (game.player_one_board == np.zeros((6,7))).all()
        assert (game.player_two_board == np.zeros((6,7))).all()

    def test_make_move(self):
        """
        Test that user input is correctly converted to a move, and that the move is valid and applied to the board.
        :return:
        """
        game = ConnectFour()
        assert game.make_move(game.player_one_board, 0) == (0, 5)
        assert game.make_move(game.player_one_board, 1) == (1, 5)
        assert game.make_move(game.player_one_board, 2) == (2, 5)

    def test_check_win_condition(self):
        """
        Test that the game correctly identifies a set of moves as a win condition
        :return:
        """
        game = ConnectFour()
        game.player_one_board[0][0] = 1
        game.player_one_board[1][0] = 1
        game.player_one_board[2][0] = 1
        game.player_one_board[3][0] = 1
        assert game.check_win_condition(game.player_one_board) == True
        game.player_one_board[0][0] = 0
        game.player_one_board[1][0] = 0
        game.player_one_board[2][0] = 0
        game.player_one_board[3][0] = 0
        assert game.check_win_condition(game.player_one_board) == False

    def test_check_horizontal_win(self):
        """
        Test that the game identifies a horizontal win condition with a set of horizontal moves.
        :return:
        """
        game = ConnectFour()
        game.player_one_board[0][0] = 1
        game.player_one_board[0][1] = 1
        game.player_one_board[0][2] = 1
        game.player_one_board[0][3] = 1
        assert game.check_win_condition(game.player_one_board) == True

    def test_check_diagonal_win(self):
        """
        Test that the game identifies a diagonal win condition with a set of diagonal moves.
        :return:
        """
        game = ConnectFour()
        game.player_one_board[0][0] = 1
        game.player_one_board[1][1] = 1
        game.player_one_board[2][2] = 1
        game.player_one_board[3][3] = 1
        assert game.check_win_condition(game.player_one_board) == True

    def test_move_selection(self):
        """
        Test that an invalid move is rejected and the make_move function returns None
        :return:
        """
        game = ConnectFour()
        illegal_row = 7
        assert game.make_move(game.player_one_board, illegal_row) == None

    def test_get_merged_board(self):
        """
        Test that the merged board is correctly generated
        :return:
        """
        game = ConnectFour()
        game.player_one_board[0][0] = 1
        game.player_two_board[0][1] = 1
        merged_board = game.get_merged_board()
        assert merged_board[0][0] == 1
        assert merged_board[0][1] == 2

    @patch('builtins.input', side_effect=['ff'])
    def test_forfeit(self, mock_input):
        """
        Test that the game ends when player 1 forfeits
        :param mock_input:
        :return:
        """
        game = ConnectFour()
        game.start_game()
        assert game.winning_player == 2

    def test_player_2_forfeit(self):
        """
        Test that the game ends when player 2 forfeits.
        :return:
        """
        mock = Mock()
        mock.side_effect = ['0', 'ff']
        with patch('builtins.input', mock):
            game = ConnectFour()
            game.start_game()
            assert game.winning_player == 1



