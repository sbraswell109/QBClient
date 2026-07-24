# This Python file uses the following encoding: utf-8

from Deck import Deck
from GameBoard import GameBoard
from json_handler import generate_cards
from utilities import TurnPlayer

STARTING_HAND_SIZE = 5

#This class contains all of the necessary information to run the game, like the board, player's hand information, both players' decklists (in their object forms), player's deck, etc
class GameManager:
    #Only the decklists are required outside information.  Everything else can be constructed on its own
    def __init__(self, player_deck_list, opp_deck_list):
        self.board = GameBoard()
        #Important to remember that player hand and deck are just lists of ids, while player_cards is a list of card objects
        self.player_deck = Deck(player_deck_list)
        self.player_hand = []
        self.opp_hand_size = STARTING_HAND_SIZE
        #TODO: Figure this out
        #NOTE: The input for these 2 might need to be changed once it's been decided how cards that add cards to hand work
        self.player_cards = generate_cards(player_deck_list)
        self.opp_cards = generate_cards(opp_deck_list)
        #By reversing the territories of the opponent's cards here, we can really easily just give the board an already modified card object so no special player/opponent logic is needed for territory locations
        self._reverse_territories(self.opp_cards)

    #Draw the opening 5 cards and mulligan if needed
    #TODO: figure out how to implement mulligan
    def draw_opening(self):
        for i in range(STARTING_HAND_SIZE):
            self.player_hand.append(self.player_deck.draw())

    def draw(self):
        #Draw from deck and add the card to hand, if there are cards left.  Otherwise, drawing needs to be skipped
        if self.player_deck.cards_left() > 0:
            self.player_hand.append(self.player_deck.draw())

    #GameBoard is assuming that it's being given a card object, and this is given a card ID, so we need to get the corresponding card object
    #Placing a card should only be done from hand, so we should deal with hand changes too
    def place_card(self, pos, card_id, turnplayer):
        #Remove card from hand & Grab card object
        card = None
        if turnplayer == TurnPlayer.SELF:
            self.player_hand.remove(card_id)
            card = self.player_cards.pop(self._find_index_by_card_id(self.player_cards, card_id))
        elif turnplayer == TurnPlayer.OPPONENT:
            self.opp_hand_size -= 1
            card = self.opp_cards.pop(self._find_index_by_card_id(self.opp_cards, card_id))
        #Have the board place the object
        self.board.add_card(pos, card, turnplayer)

    #Returns the index of a specific card given a list of card objects.
    def _find_index_by_card_id(self, cards, card_id):
        for i in range(len(cards)):
            if cards[i].id == card_id:
                return i
        raise ValueError("Card with specified ID not found in list")

    #Reverses the x-coordinate only of territories and effect territories given a list of card objects
    def _reverse_territories(self, card_list):
        for card in card_list:
            for i in range(len(card.territory)):
                card.territory[i][0] *= -1
            for i in range(len(card.effect.territory)):
                card.effect.territory[i][0] *= -1

