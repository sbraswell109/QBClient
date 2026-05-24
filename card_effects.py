# This Python file uses the following encoding: utf-8

from enum import Enum

class EffectType(Enum):
    INSTANT = 1
    CONTINUOUS = 2
    TRIGGER = 3

class Effect():
    def __init__(self, function, type, territory):
        self.function = function    #Actual function that gets called
        self.type = type    #Type of effect, (Instant, Continuous, Trigger)
        self.territory = territory  #The territory the effect acts on

    def __str__(self):
        return f"type: {self.type}, territory: {self.territory}, function: {self.function}"

#Card effect function needs board, position of card, and effect territory
#TODO: How do effects that add cards to hand work?
def no_effect(board, pos, effect_territory):
    pass

def grenadier(board, pos, effect_territory):
    pass

#TODO: Figure out how to add cards to the player's hand.  I have a feeling the effect signatures are going to change as a result
def mandragora(board, pos, effect_territory):
    pass

#Key is the effect id found in the json file, and corresponds to list of information of the corresponding effect.
#   Keeping effect territory separate in the JSON file allows us to reuse effects for cards with the same effect but different territory
card_effects = {
    0:{"type": EffectType.INSTANT, "function": no_effect}, #No effect
    3:{"type": EffectType.INSTANT, "function": grenadier},  #Grenadier
    10:{"type": EffectType.INSTANT, "function": mandragora} #Mandragora
    }




# if __name__ == "__main__":
#     pass
