# Author: Christos Georgakopoulos

import json
import card


# At this point this just creates a simple json data object for testing, we'll be using a file late
def read_cards():
    blah = {
        "id": "013",
        "name": "Crystalline Crab",
        "cost": 1,
        "value": [[-1, 0], [0, -1], [1, 0]],
        "effect": "013",
        "effect_territory": [0, -1],
    }
    data = json.dumps(blah)
    return data


# This function is responsible for actually creating card data objects (for testing, of course)
def create_card(card_data):
    jData = json.loads(card_data)
    crab_test = card.Card(
        jData["id"],
        jData["name"],
        jData["cost"],
        jData["value"],
        jData["effect"],
        jData["effect_territory"],
    )
    print(crab_test)
