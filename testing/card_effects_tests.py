# This Python file uses the following encoding: utf-8

from game.GameManager import GameManager
#from game.json_handler import generate_cards
from game.utilities import TurnPlayer


# ID: '003'
def grenadier_effect_test():
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
    assert gm.board[3][0].card.value == 2

#Test the crab
def basic_continuous_effect_test():
    pass

#Test ???
def basic_trigger_effect_test():
    pass



def run_effects_tests():
    grenadier_effect_test()
    basic_continuous_effect_test()
    basic_trigger_effect_test()

if __name__ == "__main__":
    run_effects_tests()
