# This Python file uses the following encoding: utf-8


#Use a JSON file to store the original copies of all cards, and then load them dynamically based on what cards are used.
#JSON files won't store python code, so there will have to be a separate dictionary of ID:effect functions while the JSON stores the effect ID to match it when the object is created
#Adding a new card to the game should be as easy as putting it's information in the JSON file, and then creating it's effect in card_effects.
#   The board should understand when those effects trigger
class Card():
    #While effect and effect_territory can be None, they are still in the JSON file so they probably won't be None.  May remove default argument
    def __init__(self, id, name, cost, value, territory, effect=None):
        self.id = id
        self.name = name
        #Replacement cards will probably have a cost of 4, and the code checking for validity of player input will need to have special rules with 4 cost cards
        self.cost = cost    #Pawn cost
        self.value = value  #Value of card
        self.territory = territory  #Set of x,y coordinates relative to the card's position of the territory the card captures (card is located at 0,0)
        #TODO: Work out the effect function parameters.  Needs at least effect territory, and since it's tied to the card it probably also needs the board and card position?
        #   Card effects are going to need to be labeled as instanteous, continuous, and trigger to determine when they trigger
        #Replacement cards will probably have the effect of destroying the card where they are placed, but effect_territory won't apply unless they do something else somewhere else
        self.effect = effect    #object that contains effect fuction, effect type, and effect territory.  Class in card_effects.py

    def __str__(self):
        return f"card id: {self.id}, name: {self.name}, value: {self.value}, territory: {self.territory}\ncard's effect: {self.effect}"


if __name__ == "__main__":
    pass
