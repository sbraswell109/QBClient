# This Python file uses the following encoding: utf-8

from GameManager import GameManager, STARTING_HAND_SIZE
from GameBoard import GameBoard
from json_handler import generate_cards
from utilities import TurnPlayer
from Card import Card

#GM initialization setup
def reverse_opp_territory_tests():
    player_deck = ['001']
    opp_deck = ['001', '003', '005', '010']
    gm = GameManager(player_deck, opp_deck)

    assert gm.opp_cards[0].territory == [[1,0], [-1,0], [0,-1], [0,1]]
    assert gm.opp_cards[0].effect.territory == []
    assert gm.opp_cards[1].territory == []
    assert gm.opp_cards[1].effect.territory == [[-2,0]]
    assert gm.opp_cards[2].territory == [[0,2], [0,-2]]
    assert gm.opp_cards[2].effect.territory == []
    assert gm.opp_cards[3].territory == [[0,1], [-1,0]]
    assert gm.opp_cards[3].effect.territory == []

def setup_tests():
    reverse_opp_territory_tests()



#Opening hand tests
def draw_opening_tests():
    player_deck = ['001', '002', '003', '004', '005']
    opp_deck = ['001', '001', '001', '001', '001']
    gm = GameManager(player_deck, opp_deck)
    gm.draw_opening()

    #After draw_opening(), player_deck is empty because it IS gm.player_deck.deck
    assert set(gm.player_hand) == set(['001', '002', '003', '004', '005'])
    assert gm.player_deck.deck == []
    assert gm.player_deck.cards_left() == 0



#Standard draw tests
def draw_with_cards_left_in_deck():
    player_deck = ['001', '002']
    opp_deck = ['001', '001']
    gm = GameManager(player_deck, opp_deck)

    gm.draw()
    assert gm.player_hand == ['001'] and gm.player_deck.deck == ['002'] or gm.player_hand == ['002'] and gm.player_deck.deck == ['001']
    assert gm.player_deck.cards_left() == 1

def draw_with_no_cards_left_in_deck():
    player_deck = ['001', '002', '003', '004', '005']
    opp_deck = ['001', '001', '001', '001', '001']
    gm = GameManager(player_deck, opp_deck)
    gm.draw_opening()

    assert set(gm.player_hand) == set(['001', '002', '003', '004', '005'])
    assert gm.player_deck.deck == []
    assert gm.player_deck.cards_left() == 0
    gm.draw()
    assert set(gm.player_hand) == set(['001', '002', '003', '004', '005'])
    assert gm.player_deck.deck == []
    assert gm.player_deck.cards_left() == 0

def standard_draw_tests():
    draw_with_cards_left_in_deck()
    draw_with_no_cards_left_in_deck()



#Placing card on the board tests
def place_player_card():
    player_deck = ['001', '002', '003', '004', '005']
    opp_deck = ['001', '001', '001', '001', '001']
    gm = GameManager(player_deck, opp_deck)
    gm.draw_opening()
    gm.place_card((0,1), '001', TurnPlayer.SELF)

    test_card = generate_cards(['001'])[0]
    test_board = GameBoard()
    test_board.add_card((0,1), test_card, TurnPlayer.SELF)

    assert gm.board.board == test_board.board
    assert set(gm.player_hand) == set(['002', '003', '004', '005'])

#Before this can be written, how territory is handled when it is the opponent's card needs to be figured out in GameManager and GameBoard
def place_opp_card():
    player_deck = ['001', '001', '001', '001', '001']
    opp_deck = ['001', '002', '003', '004', '005']
    gm = GameManager(player_deck, opp_deck)
    gm.opp_cards[gm._find_index_by_card_id(gm.opp_cards, '004')].effect = None  #Need to manually set this effect to None or the custom card we're using as a reference won't be equivalent to this
    assert gm.opp_hand_size == STARTING_HAND_SIZE
    gm.place_card((4,0),'001',TurnPlayer.OPPONENT)
    assert gm.opp_hand_size == STARTING_HAND_SIZE - 1
    gm.place_card((4,1),'004',TurnPlayer.OPPONENT)
    assert gm.opp_hand_size == STARTING_HAND_SIZE - 2

    reversed_sweeper = Card('004', 'J-Unit Sweeper', 2, 2, [[0,1],[-1,1],[0,-1],[-1,-1]])
    sec_off = generate_cards(['001'])[0]
    test_board = GameBoard()
    test_board.add_card((4,0), sec_off, TurnPlayer.OPPONENT)
    test_board.add_card((4,1), reversed_sweeper, TurnPlayer.OPPONENT)

    assert gm.board.board == test_board.board

def place_card_tests():
    place_player_card()
    place_opp_card()



#Full testing
def run_gm_tests():
    setup_tests()
    draw_opening_tests()
    standard_draw_tests()
    place_card_tests()

if __name__ == "__main__":
    run_gm_tests()
