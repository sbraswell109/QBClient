import json_handler
import card
import json

card_test = json_handler.read_cards(["001", "002"])

json_handler.create_card(card_test)
