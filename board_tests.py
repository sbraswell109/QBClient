# This Python file uses the following encoding: utf-8
from board import GameBoard
from json_handler import generate_cards

if __name__ == "__main__":
    board = GameBoard()
    sec_officer0, sec_officer1, sec_officer2, sec_officer3, sec_officer4 = generate_cards(['001', '001', '001', '001', '001'])
    board.add_card((0,1), sec_officer0)
    print(board)
    board.add_card((1,0), sec_officer1)
    print(board)
    board.add_card((2,1), sec_officer2)
    print(board)
    board.add_card((1,2), sec_officer3)
    print(board)
    board.add_card((3,1), sec_officer4)
    print(board)
    
