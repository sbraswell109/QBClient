# This Python file uses the following encoding: utf-8

#This file contains the board class used to represent and modify the game board

from card import Card
from utilities import TurnPlayer

#TODO: think about this
#   This class was intended to be the board, but the functions are so closely tied to the board as well as the steps of the general game loop since everything happens when a card is place
#       Maybe this class should be renamed to Game Manager or something?
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
    #If the opponent is placing a card, we can assume the territory and effect territory is already flipped, since we can do that when we generate their decklist of card objects
    #BIG TODO: At some point, this is going to need to take the opposing player into account too for when they add cards to the board (flipped territory, pawn_val adjustments, etc)
    def add_card(self, pos, card, turnplayer):
        #Put card in the correct node
        self.board[pos[0]][pos[1]].card = card
        #Some cards add extra pawns to territory (EX: Titan), so may want to consider making this it's own function for ease of use,
        #   but also need to double check rules regarding those and opponent's territory
        #Capture Territory of correct area
        for square in card.territory:
            #Need to check all the territory within the bounds of the board (0-2y , 0-4x) and then adjust pawn_value accordingly
            target_x, target_y = [pos[0]+square[0], pos[1]+square[1]] #[x,y] which is used to go directly on the board
            if target_x >= 0 and target_x <= 4 and target_y >= 0 and target_y <= 2: #Check the bounds of the board
                target = self.board[target_x][target_y]
                if target.card == None:
                    if (target.pawn_value < 3 and turnplayer == TurnPlayer.SELF) or (target.pawn_value > -3 and turnplayer == TurnPlayer.OPPONENT): #Check the pawn_value
                        #TODO: Double check rules that if spot is controlled by opp, taking control only flips instead of flipping and adding
                        if (target.pawn_value < 0 and turnplayer == TurnPlayer.SELF) or (target.pawn_value > 0 and turnplayer == TurnPlayer.OPPONENT): #Spot needs to be flipped
                            target.pawn_value *= -1
                        elif turnplayer == TurnPlayer.SELF:     #Spot empty or controlled by self
                            target.pawn_value += 1
                        elif turnplayer == TurnPlayer.OPPONENT: #Spot empty or controlled by opponent
                            target.pawn_value -= 1
        #BIG TODO: Finalize card effect function signatures before writing any code actually calling the cards
        #TODO: Card's effect should occur before territory is captured since if the effect destroys a card and takes the space, the space will be taken which requires the effec to occur first
        #Apply the card's effect (How do Instant and Continuous effects differ in how they are applied? When a continuous card leaves the field, it's effect needs to be unapplied)
        #   Idea: Instanteous effects modify the card object, continuous effects modify the affected nodes' point_modifiers,
        #       and when a card is removed, remove it from applicable nodes' point_modifiers
        #TODO: Worry about trigger effects and where those are applied (maybe update_board?).  Will probably need to check the board after each action has taken place in the game loop

    #TODO: Write function
    #A function that checks the board for the proper board state, making sure cards that need to be destroyed are done so and trigger effects are applied if needed, etc
    #NOTE: THERE ARE SPECIAL RULES FOR THE PAWN VALUE OF A SPACE WHEN A UNIT IS DESTROYED ON IT.  RESEARCH IT
    def update_board(self):
        pass

    def __str__(self):
        str = ''
        for y in range(len(self.board[0])):
            for x in range(len(self.board)):
                str += f"({self.board[x][y].pawn_value},{self.board[x][y].card.name if self.board[x][y].card != None else 'None'})\t"
            str += "\n"
        return str

    def __eq__(self, other_board):
        if other_board == None:
            return False
        bool = True
        for x in range(len(self.board)):
            for y in range(len(self.board[0])):
                if self.board[x][y] != other_board.board[x][y]:
                    bool = False
                    break
        return bool


class Node():
    def __init__(self, pawn_val, card=None):
        #The value of the pawn being positive or negative indicates who has control over the square.  A helper fuction can be made to return which player has control for readability
        self.pawn_value = pawn_val
        #card will be a card object, which has yet to be implemented, or can be None.  I can also make a "None" card if necessary
        self.card = card
        #Point modifiers is the sum of all continuous number modifications for that slot, because these will need to be applied even if the slot is empty
        #   Maybe this should be a set instead of a list?
        #TODO: Figure out exactly what point_modifiers consists of.  If a card modifying another card is destroyed, how do we stop keeping track of their modifier?  Pointers?
        #   Duh, cards have effect_territory which say which cards they are modifying.  I just need to figure out how to single out their own modifier in the list
        self.point_modifiers = []

    def __eq__(self, other_node):
        if other_node == None:
            return False
        return self.pawn_value == other_node.pawn_value and self.card == other_node.card and set(self.point_modifiers) == set(other_node.point_modifiers)

#TODO: Write tests in a dedicated board test file
if __name__ == "__main__":
    pass
