import deck as dk, deal_cards as dc
def main():
    deck = dk.create_deck()
    num_cards = int(input('Cкoлькo карт раздать? '))
    dc.deal_cards(deck, num_cards)

if __name__ == '__main__': main()