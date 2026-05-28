# This Python file uses the following encoding: utf-8
from board import GameBoard
from json_handler import generate_cards
from utilities import TurnPlayer

if __name__ == "__main__":
    board = GameBoard()
    sec_officer0, sec_officer1, sec_officer2, sec_officer3, sec_officer4 = generate_cards(['001', '001', '001', '001', '001'])
    #TODO: These need turnplayer added to the calls
    board.add_card((0,1), sec_officer0, TurnPlayer.SELF)
    print(board)
    board.add_card((1,0), sec_officer1, TurnPlayer.SELF)
    print(board)
    board.add_card((2,1), sec_officer2, TurnPlayer.SELF)
    print(board)
    board.add_card((1,2), sec_officer3, TurnPlayer.SELF)
    print(board)
    board.add_card((4,1), sec_officer4, TurnPlayer.OPPONENT)
    print(board)
    
