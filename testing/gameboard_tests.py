# This Python file uses the following encoding: utf-8
from game.GameBoard import GameBoard
from game.GameManager import GameManager
from game.json_handler import generate_cards
from game.utilities import TurnPlayer

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


def get_inbounds_positions_test():
    board = GameBoard()
    test_territory = [[0,1],[0,-1],[1,0],[-1,0]]
    res1 = board.get_nodes_in_range((0,2), test_territory)
    assert set(res1) == set((((1,2),(0,1))))
    res2 = board.get_nodes_in_range((4,0), test_territory)
    assert set(res2) == set((((3,0),(4,1))))


#TODO: CREATE NODE.IS_ENEMY_OF() TESTS

#TODO: MOVE THESE TO A CARD EFFECT TESTING FILE
#Test the grenadier
def basic_instant_effect_test():
    player_deck = ['003']
    opp_deck = ['001']
    gm = GameManager(player_deck, opp_deck)
    gm.draw_opening()
    #Need to manually place pawns on the board so that the Node correctly recognizes who controls it
    gm.board[3][0].pawn_value = -1
    gm.board[1][0].pawn_value = 1
    gm.place_card((3,0), '001', TurnPlayer.OPPONENT)
    gm.board[3][0].card.value = 6
    gm.place_card((1,0), '003', TurnPlayer.SELF)
    print(gm.board[3][0].card.value)
    assert gm.board[3][0].card.value == 2

#Test the crab
def basic_continuous_effect_test():
    pass

#Test ???
def basic_trigger_effect_test():
    pass


def run_board_tests():
    basic_pawn_value_incrementations_test()
    pawn_value_flip_test()
    get_inbounds_positions_test()
    basic_instant_effect_test()
    basic_continuous_effect_test()
    basic_trigger_effect_test()

if __name__ == "__main__":
    #Very basic adding cards to various spots on the board to test pawn_value incrementations
    run_board_tests()
    
