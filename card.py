# This Python file uses the following encoding: utf-8


#Use a JSON file to store the original copies of all cards, and then load them dynamically based on what cards are used.  Ask Christos he knows about them
#JSON files won't store python code, so there will have to be a separate dictionary of ID:effect functions while the JSON stores the effect ID to match it when the object is created
class Card():
    def __init__(self, id, cost, value, territory, effect=None, effect_territory=None):
        self.id = id
        #Replacement cards will probably have a cost of 4, and the code checking for validity of player input will need to have special rules with 4 cost cards
        self.cost = cost    #Pawn cost
        self.value = value  #Value of card
        self.territory = territory  #Set of x,y coordinates relative to the card's position of the territory the card captures (card is located at 0,0)
        #TODO: Work out the effect function parameters.  Needs at least effect territory, and since it's tied to the card it probably also needs the board and card position?
        #   Card effects are going to need to be labeled as instanteous, continuous, and trigger to determine when they trigger
        #Replacement cards will probably have the effect of destroying the card where they are placed, but effect_territory won't apply unless they do something else somewhere else
        self.effect = effect    #Function the effect applies.  Exact parameters of the function needs to be worked out
        self.effect_territory = effect_territory    #Set of x,y coordinates relative to the card's position where the effect applies if applicable


if __name__ == "__main__":
    pass
