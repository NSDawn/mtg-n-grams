import data_reader as dr
import tokenizer as tk

def main():
    oracletext_pathname = input("\nRelative path to data file:\n   $>")
    # ../data/slimified_oracle_cards_data.json
    D = dr.read_in_json(oracletext_pathname)
    while 1:
        card_query = input("\nChoose a card name:\n$> ")
        card_match = [card for card in D if card_query.upper().replace(" ", "") in card['name'].upper().replace(" ", "")]
        if (len(card_match) == 0):
            print("Sorry, no matches!")
        else: 
            for card in card_match:
                print(card['name'], ":", tk.tokenize(card['oracle_text'], card['name']))


if __name__ == '__main__':
    main()