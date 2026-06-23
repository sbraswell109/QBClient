# This Python file uses the following encoding: utf-8

from random import shuffle

#This class contains all of the information pertaining to the client's active deck (Deck info will have to be stored in a file somewhere and this class generated at runtime)
#   The Game Manager class is what will glue everything together like Deck, Board, and client's hand, as well as storing necessary information like objects for the opponent's deck.

#Ultimately, this class really just needs to be a way to draw cards randomly from the player's deck.
#   The question is, should this class contain the card objects, or should it just return IDs for the game manager to put objects into the player's hand?
#       The opponent's deck_list is known to create card objects, but they don't have a constructed deck, so having the player's deck contain objects but the opponent not having a deck would
#           create inconsistencies with where the objects are stored when not on the board
#       Unless the deck also had a function to pull a card out of the deck by ID, then we could have an opposing player's deck be constructed, but then where do we keep the card objects
#           that are created and placed into the hand by card effects (EX: Moogle Trio)
class Deck:
    def __init__(self, deck_list):
        self.deck_list = deck_list
        #shuffle the deck
        self.deck = deck_list
        self.shuffle()

    #This is basically just a way to say deck.shuffle() instead of shuffle(deck.deck)
    def shuffle(self):
        shuffle(self.deck)

    def draw(self):
        return self.deck.pop(0)

    def cards_left(self):
        return len(self.deck)

if __name__ == '__main__':
    deck = Deck(['001', '001', '123', '123', '456', '789'])
    deck.shuffle()
    print(deck.deck)

    drawn = deck.draw()
    print(drawn)
    print(deck.deck)
