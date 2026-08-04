# This Python file uses the following encoding: utf-8

#This file contains the board class used to represent and modify the game board

from game.Card import Card
from game.utilities import TurnPlayer

#TODO: think about this
#   This class was intended to be the board, but the functions are so closely tied to the board as well as the steps of the general game loop since everything happens when a card is place
#       Maybe this class should be renamed to Game Manager or something?
class GameBoard():
    def __init__(self, parent=None):
        #NOTE: tbh I don't really like this being called "board" because it means that I have to type stuff like board.board but I'm not sure of a better name
        #   Though actually we shouldn't really be directly accessing GameBoard.board from GameManager so it should be fine
        #Board is represented like this so I can write [x,y] coordinates and have the board behave properly with them
        #[0,0] is top left of board when facing it as a 3x5
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
        self.parent = parent


    #pos is an x,y coordinate of where to place the given card in the board
    #If the opponent is placing a card, we can assume the territory and effect territory is already flipped, since we can do that when we generate their decklist of card objects
    def add_card(self, pos, card, turnplayer):
        #TODO: The effect function needs to be given everything it needs to do its job
        card.effect.function(self._generate_context(pos, card))
        self.update_board() #To trigger destruction of any cards necessary and to handle the results of any trigger/continuous effects

        #Put card in the correct node
        self.board[pos[0]][pos[1]].card = card
        #Some cards add extra pawns to territory (EX: Titan), so may want to consider making this it's own function for ease of use,
        #   but also need to double check rules regarding those and opponent's territory
        #Capture Territory of correct area
        #TODO: Update this to use get_nodes_in_range()
        for square in card.territory:
            #Need to check all the territory within the bounds of the board (0-2y , 0-4x) and then adjust pawn_value accordingly
            target_x, target_y = [pos[0]+square[0], pos[1]+square[1]] #[x,y] which is used to go directly on the board
            if target_x >= 0 and target_x <= 4 and target_y >= 0 and target_y <= 2: #Check the bounds of the board
                target = self.board[target_x][target_y]
                if target.card == None:
                    if (target.pawn_value < 3 and turnplayer == TurnPlayer.SELF) or (target.pawn_value > -3 and turnplayer == TurnPlayer.OPPONENT): #Check the pawn_value
                        if (target.pawn_value < 0 and turnplayer == TurnPlayer.SELF) or (target.pawn_value > 0 and turnplayer == TurnPlayer.OPPONENT): #Spot needs to be flipped
                            target.pawn_value *= -1
                        elif turnplayer == TurnPlayer.SELF:     #Spot empty or controlled by self
                            target.pawn_value += 1
                        elif turnplayer == TurnPlayer.OPPONENT: #Spot empty or controlled by opponent
                            target.pawn_value -= 1


    #TODO: Write function
    #A function that checks the board for the proper board state, making sure cards that need to be destroyed are done so and trigger effects are applied if needed, etc
    # This also adds up continuous modifiers on a card for these checks
    #NOTE: When a card is destroyed, the pawn value of the square is equivalent to the pawn cost of the destroyed card (so I suppose pawn_val is capped at the card's cost when placed
    def update_board(self):
        # Trigger effects need to be checked for activation and if they trigger.  This could change whether cards are marked for destruction or not so it should probably occur before we mark cards for destruction
        #   TODO: If a trigger effect happens, it needs to not happen again if it should only happen once.  Probably add a new variable in the Effect class that the card effect can check
        #   Some effects trigger when a specific condition happens (like a card played, a card is destroyed).  When certain events happen, we can add information to the context dictionary and then wipe the counter later (probably the end of this function) (EX: #32 Sea Devil & #35 Tonberry King
        #       This involves creating a context dictionary as a member variable in the GM and the function that currently constructs one would just modify some of the parameters and return the modified dictionary
        #       PROBLEM: Where do we wipe counter contexts for certain triggers?, but we'll need to keep track of new triggers to keep and old triggers to get rid of
        #       PROBLEM: How do add certain contexts regarding inside card effect functions?  (EX: Should the grenadier effect add to some 'enfeebled' context somehow? If not, how do we keep track of it?)
        #           I would really like to keep card effects as simple as possible, with all the update/results of the effects outside of it, so if we can 'figure out' what happened after a card effect, like an enfeeble or buff, it would be nice
        #   How do we handle trigger effects that are "When this card is destroyed?" (EX: #30 Flametrooper)
        #       We can check for trigger effects when destroying the card
        #   Signals would be a really nice way of doing trigger effects, but I'm not sure how possible they are
        # All effects are active simultaneously, so we need to go through the board and mark all cards at 0 value for destruction, then destroy them at the end and call update_board again
        #   PROBLEM: Triggers can require the board to update, but updating the board can activate more triggers.  How should this cycle be formatted?
        #       IDEA: check_triggers -> update_board but only if a trigger goes off, then update_board -> check_triggers but only if cards are removed from the board
        #           checking triggers will require checking final card values anyway, so we don't need to always call check_triggers after update_board
        # gdscript-like signals would be really nice for doing this, but I don't think python has non-system related equivalents
        pass

    #Given an origin position on the board and a list of territories to check, return the node coordinates (origin + territory) coordinates that are within the bounds of the board
    def get_nodes_in_range(self, origin: tuple[int, int], territory: list[list[int, int]]) -> tuple[tuple[int, int]]:
        in_bounds = []
        x_len = len(self.board)
        y_len = len(self.board[0])
        for offset in territory:
            target = [origin[0] + offset[0], origin[1] + offset[1]]
            if target[0] > -1 and target[0] < x_len and target[1] > -1 and target[1] < y_len:
                in_bounds.append(tuple(target))
        return tuple(in_bounds)

    def _generate_context(self, pos: tuple[int, int], central_card: Card) -> dict:
        return dict(gm=self.parent, position=pos, card=central_card)

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

    def __getitem__(self, item):
        return self.board[item]


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

    # Given another node, returns if that node is controlled by a different player than the current node.  Returns False if either node's pawn_value is 0
    def is_enemy_of(self, other_node) -> bool:
        if self.pawn_value < 0 and other_node.pawn_value > 0 or self.pawn_value > 0 and other_node.pawn_value < 0:
            return True
        return False

    def __eq__(self, other_node):
        if other_node == None:
            return False
        return self.pawn_value == other_node.pawn_value and self.card == other_node.card and set(self.point_modifiers) == set(other_node.point_modifiers)

if __name__ == "__main__":
    pass
