# This Python file uses the following encoding: utf-8

#This file contains the board class used to represent and modify the game board

from card import Card

class GameBoard():
    def __init__(self):
        #Board is represented like this so I can write [x,y] coordinates and have the board behave properly with them
        self.board = [
        [Node(1), Node(1), Node(1)],
        [Node(0), Node(0), Node(0)],
        [Node(0), Node(0), Node(0)],
        [Node(0), Node(0), Node(0)],
        [Node(-1), Node(-1), Node(-1)]
        ]
        #self.board = [
        #[Node(1), Node(0), Node(0), Node(0), Node(-1)],
        #[Node(1), Node(0), Node(0), Node(0), Node(-1)],
        #[Node(1), Node(0), Node(0), Node(0), Node(-1)]]   #3 rows 5 columns

        #pos is an x,y coordinate of where to place the given card in the board
        #TODO: At some point, this is going to need to take the opposing player into account too for when they add cards to the board (flipped territory, pawn_val adjustments, etc)
        def add_card(self, pos, card):
            #Put card in the correct node
            self.board[pos[0]][pos[1]].card = card
            #Capture Territory of correct area
            for square in card.territory:
                #Need to check all the territory within the bounds of the board (0-2y , 0-4x) and then adjust pawn_value accordingly
                spot = [pos[0]+square[0], pos[1]+square[1]] #[x,y] which is used to go directly on the board
                if spot[0] >= 0 and spot[0] <= 4 and spot[1] >= 0 and spot[1] <= 2:
                    #TODO: This should only adjust the pawn values of squares that don't already have a card on them
                    if self.board[spot[0]][spot[1]].pawn_val < 3:
                        self.board[spot[0]][spot[1]].pawn_val += 1
        #TODO: Card's effect should occur before territory is captured since if the effect destroys a card and takes the space, the space will be taken which requires the effec to occur first
        #Apply the card's effect (How do Instant and Continuous effects differ in how they are applied? When a continuous card leaves the field, it's effect needs to be unapplied)
        #   Idea: Instanteous effects modify the card object, continuous effects modify the affected nodes' point_modifiers,
        #       and when a card is removed, remove it from applicable nodes' point_modifiers
        #TODO: Worry about trigger effects and where those are applied (maybe update_board?).  Will probably need to check the board after each action has taken place in the game loop

    #TODO: Write function
    #A function that checks the board for the proper board state, making sure cards that need to be destroyed are done so and trigger effects are applied if needed, etc
    def update_board(self):
        pass

    #TODO: Write a string representation to easily print for testing purposes


class Node():
    def __init__(self, pawn_val, card=None):
        #The value of the pawn being positive or negative indicates who has control over the square.  A helper fuction can be made to return which player has control for readability
        self.pawn_value = pawn_val
        #card will be a card object, which has yet to be implemented, or can be None.  I can also make a "None" card if necessary
        self.card = card
        #Point modifiers is the sum of all continuous number modifications for that slot, because these will need to be applied even if the slot is empty
        self.point_modifiers = []

#TODO: Write tests in a dedicated board test file
if __name__ == "__main__":
    board = GameBoard()
    crab = CREATE_CRAB
    board.add_card((1, 2), crab)
    print(board)
