# This Python file uses the following encoding: utf-8

#This is the file where the main game loop is handled.  It does turn control, manipulates the board based on input received, etc
# When the game is started by hitting the "Play" button on the home screen, this file will take over after switching to the game_ui


from ui.game_ui import GameUI
from game.GameManager import GameManager

#I was debating if I should incorporate run_game into GameManager, but I think having the game loop be its own separate function might be a good choice
#   Because the main game loop will have to deal with networking, which allows GameManager to just be all of the game-related information
#       TODO: Think about this
#       Though does that mean GameManager should be renamed to something more appropriate if it's not managing the game loop?

def run_game(game_ui: GameUI):
    #Create the GameManager
    #Draw cards from Deck
    #Game loop starts
    #   Just start with being able to place cards on the board for the player first.  Worry about adding in a second player and networking later
    pass

if __name__ == "__main__":
    pass
