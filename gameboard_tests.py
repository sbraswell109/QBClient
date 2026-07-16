# This Python file uses the following encoding: utf-8
from GameBoard import GameBoard
from json_handler import generate_cards
from utilities import TurnPlayer

def basic_pawn_value_incrementations_test():
    board = GameBoard()
    test_board = GameBoard()
    sec_officer0, sec_officer1, sec_officer2, sec_officer3 = generate_cards(['001', '001', '001', '001'])
    assert sec_officer0 == sec_officer1
    board.add_card((0,1), sec_officer0, TurnPlayer.SELF)
    test_board.board[0][1].card = sec_officer0
    test_board.board[0][0].pawn_value = 2
    test_board.board[0][2].pawn_value = 2
    test_board.board[1][1].pawn_value = 1
    assert board == test_board
    board.add_card((1,0), sec_officer1, TurnPlayer.SELF)
    test_board.board[1][0].card = sec_officer1
    test_board.board[0][0].pawn_value = 3
    test_board.board[2][0].pawn_value = 1
    test_board.board[1][1].pawn_value = 2
    assert board == test_board
    board.add_card((2,1), sec_officer2, TurnPlayer.SELF)
    test_board.board[2][1].card = sec_officer2
    test_board.board[2][0].pawn_value = 2
    test_board.board[1][1].pawn_value = 3
    test_board.board[2][2].pawn_value = 1
    test_board.board[3][1].pawn_value = 1
    assert board == test_board
    board.add_card((1,2), sec_officer3, TurnPlayer.SELF)
    test_board.board[1][2].card = sec_officer3
    test_board.board[0][2].pawn_value = 3
    test_board.board[1][1].pawn_value = 3
    test_board.board[2][2].pawn_value = 2
    assert board == test_board

def pawn_value_flip_test():
    board = GameBoard()
    test_board = GameBoard()
    sec_officer0, sec_officer1 = generate_cards(['001', '001'])
    board.add_card((2,1), sec_officer0, TurnPlayer.SELF)
    test_board.board[2][1].card = sec_officer0
    test_board.board[1][1].pawn_value = 1
    test_board.board[2][0].pawn_value = 1
    test_board.board[2][2].pawn_value = 1
    test_board.board[3][1].pawn_value = 1
    assert board == test_board
    board.add_card((4,1), sec_officer1, TurnPlayer.OPPONENT)
    test_board.board[4][1].card = sec_officer1
    test_board.board[4][0].pawn_value = -2
    test_board.board[4][2].pawn_value = -2
    test_board.board[3][1].pawn_value = -1
    assert board == test_board


def run_board_tests():
    basic_pawn_value_incrementations_test()
    pawn_value_flip_test()

if __name__ == "__main__":
    #Very basic adding cards to various spots on the board to test pawn_value incrementations
    run_board_tests()
    
