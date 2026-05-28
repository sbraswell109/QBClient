# This Python file uses the following encoding: utf-8

from enum import Enum

#Used to determine which player's actions/cards we want to handle
class TurnPlayer(Enum):
    SELF = 0
    OPPONENT = 1


#EffectType is used by the board to determine when the effect triggers.
class EffectType(Enum):
    INSTANT = 1
    CONTINUOUS = 2
    TRIGGER = 3

# if __name__ == "__main__":
#     pass
