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
    gm.board[3][0].card.base_value = 6
    gm.place_card((1,0), '003', TurnPlayer.SELF)
    assert gm.board[3][0].card.base_value == 2

def grenadier_effect_out_of_bounds_test():
    pass

#Test the crab
def crystalline_crab_effect_test():
    player_deck = ['001', '013', '013']
    opp_deck = ['001']
    gm = GameManager(player_deck, opp_deck)
    gm.draw_opening()
    gm.place_card((0, 2), '013', TurnPlayer.SELF)
    gm.place_card((0, 1), '001', TurnPlayer.SELF)
    #Testing that the crab boosts the value of allied cards
    #TODO: Replace this with what this should be
    assert gm.board[0][1].point_modifiers == None
    assert gm.board[0][1].card.final_value == 2

    #Testing that the crab does not boost the value of enemy cards
    gm.board[4][2].pawn_value = 1
    gm.place_card((4,2), '013', TurnPlayer.SELF)
    gm.place_card((4,1), '001', TurnPlayer.OPPONENT)
    #TODO: Replace this with whatever format point_modifiers should be in
    assert gm.board[4][1].point_modifiers == None
    assert gm.board[4][1].card.final_value == 1

#Test ???
def basic_trigger_effect_test():
    pass



def run_effects_tests():
    grenadier_effect_test()
    grenadier_effect_out_of_bounds_test()
    crystalline_crab_effect_test
    basic_trigger_effect_test()

if __name__ == "__main__":
    run_effects_tests()
