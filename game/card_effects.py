# This Python file uses the following encoding: utf-8


# This file is all of the card effects.  The Effect class is a part of Card.py
from game.utilities import EffectType

# I really don't like how importing GameManager causes a circular import so I can't put type annotations.  The alternative is to have GM put in a context dictionary but the GM should probably be told to do stuff like add cards to the player's hand.
#   TODO: Find a better way to do this
# Maybe a wrapper dictionary would work with gm as one of the components and other components including things like position the card is played and the card itself.  Then these functions would be able to modify their own effect territory,
#       and the Board would just need to call the function with the wrapper and not worry about doing extra things.

#NOTE: context does not contain which player has their card being activated, but we can figure that out based on who controls the pawns at the origin and who controls the pawns at the target destination
# context contains
#   "gm": GameManager
#   "position": (int, int) position on the GameBoard of the card who is activating the effect
#   "card": Card, the actual card object itself that is activating its effect
def no_effect(context: dict):
    pass

# -4 to enemy card
def grenadier(context: dict):
    x = context["position"][0]
    y = context["position"][1]
    self_node = context["gm"].board[x][y]
    for spot in context["gm"].board.get_nodes_in_range(context["position"], context["card"].effect.territory):
        other_node = context["gm"].board[spot[0]][spot[1]]
        if other_node.card != None and self_node.is_enemy_of(other_node):
            other_node.card.value -= 4

#BIG TODO: Figure out how to add cards to the player's hand.  I have a feeling the effect signatures are going to change as a result
#   The JSON file is probably going to need a "related_cards" field consisting of IDs of cards that are added to hand or whatever
#   Then go through all the different cards that exist and make sure that whatever signature we give the functions, is probably possible
def mandragora(context: dict):
    pass

def crystalline_crab(context: dict):
    pass

#Key is the effect id found in the json file, and corresponds to a dictionary of information of the corresponding effect.
#   Keeping effect territory separate in the JSON file allows us to reuse effects for cards with the same effect but different territory
card_effects = {
    0:{"type": EffectType.INSTANT, "function": no_effect}, #No effect
    3:{"type": EffectType.INSTANT, "function": grenadier},  #Grenadier
    10:{"type": EffectType.INSTANT, "function": mandragora}, #Mandragora
    13:{"type": EffectType.CONTINUOUS, "function": crystalline_crab},   #Crystalline Crab
    }




# if __name__ == "__main__":
#     pass
