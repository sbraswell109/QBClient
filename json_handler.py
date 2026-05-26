# Author: Christos Georgakopoulos

import json
from card import Card
from card_effects import Effect
from card_effects import card_effects

# Reads json file, selecting specific card information we want based on card_array
def read_cards(card_array):
    with open("cards.json", "r") as file:
        data = json.load(file)
        selected_data = {key: data[key] for key in card_array}
    # With this implementation, selected_data will be a Dict that looks EXACTLY like the json file ("id#":{rest of data}
    return selected_data


# This function is responsible for actually creating card data objects (for testing, of course)
# Given a card's id and a dictionary with the rest of its data (from the JSON file), generates the corresponding card object
def create_card(id, data):
    effect = Effect(card_effects[data["effect"]]["function"], card_effects[data["effect"]]["type"], data["effect_territory"])
    return Card(id, data["name"], data["cost"], data["value"], data["territory"], effect)

#Function that takes an array of card ids and returns an array of the corresponding card objects
def generate_cards(card_array):
    card_data = read_cards(card_array)
    #Dictionaries can't have duplicate keys, so we need to account for that
    return [create_card(id, card_data[id]) for id in card_array]

if __name__ == '__main__':
    grenadier, mandragora = generate_cards(['003', '010'])
    print(grenadier)
    print(mandragora)
