# Author: Christos Georgakopoulos

import json
from Card import Card
from card_effects import Effect
from card_effects import card_effects

# Reads json file, selecting specific card information we want given an array of IDs
def _read_cards(card_array):
    with open("cards.json", "r") as file:
        data = json.load(file)
        selected_data = {key: data[key] for key in card_array}
    # With this implementation, selected_data will be a Dict that looks EXACTLY like the json file ("id#":{rest of data}
    return selected_data

# This function is responsible for actually creating card data objects
# Given a card's id and a dictionary with the rest of its data (from the JSON file), generates the corresponding card object
def _create_card(id, data):
    effect = Effect(card_effects[data["effect"]]["function"], card_effects[data["effect"]]["type"], data["effect_territory"])
    return Card(id, data["name"], data["cost"], data["value"], data["territory"], effect)

#Function that takes an array of card ids and returns an array of the corresponding card objects.  This is the main function used to create cards from the JSON
def generate_cards(card_array):
    card_data = _read_cards(card_array)
    #Dictionaries can't have duplicate keys, so we need to account for that
    return [_create_card(id, card_data[id]) for id in card_array]

if __name__ == '__main__':
    grenadier, mandragora = generate_cards(['003', '010'])
    print(grenadier)
    print(mandragora)
