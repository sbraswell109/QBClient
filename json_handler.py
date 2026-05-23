# Author: Christos Georgakopoulos

import json


# Reads json file, selecting specific cards we want based on card_array
def read_cards(card_array):
    with open("cards.json", "r") as file:
        selected_data = {key: json.load(file)[key] for key in card_array}
    # With this implementation, selected_data will be a Dict that looks EXACTLY like the json file
    return selected_data


# This function is responsible for actually creating card data objects (for testing, of course)
# NOTE: With the new setup (id: {dict}), cards can be accessed like jData['001']['sub_key']
def create_card(card_data):
    jData = json.loads(card_data)
    for key, value in jData.items():
        print(f"Key: {key}")
        print(f"Value: {value}")
