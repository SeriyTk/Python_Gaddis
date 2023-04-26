import random as rd
def deal_cards(deck, number):
    hand_value = 0
    if number > len(deck): number = len(deck)
    for count in range(number):
        card = rd.choice(list(deck))
        print(card)
        hand_value += deck[card]
    print(f'Величина карт на руках: {hand_value}')