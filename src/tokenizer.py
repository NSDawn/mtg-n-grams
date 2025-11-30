class Tokens(): 
    END_OF_STRING = "$EOS"
    BEGINNING_OF_STRING = "$BOS"
    CARD_NAME = "$CARDNAME"
    PERIOD = "$PERIOD"
    COMMA = "$COMMA"
    COLON = "$COLON"
    EM_DASH = "$EMDASH"
    SLASH = "$SLASH"
    NEWLINE = "$NEWLINE"
    BULLET = "$BULLET"
    LEFT_PARENTHESIS = "$LPARENS"
    RIGHT_PARENTHESIS = "$RPARENS"
    
    GENERIC_MANA_1 = "$1"
    GENERIC_MANA_2 = "$2"
    GENERIC_MANA_3 = "$3"
    GENERIC_MANA_4 = "$4"
    GENERIC_MANA_5 = "$5"
    GENERIC_MANA_6 = "$6"
    GENERIC_MANA_7 = "$7"
    GENERIC_MANA_8 = "$8"
    GENERIC_MANA_9 = "$9"
    GENERIC_MANA_10 = "$10"
    GENERIC_MANA_11 = "$11"
    GENERIC_MANA_12 = "$12"
    GENERIC_MANA_13 = "$13"
    GENERIC_MANA_14 = "$14"
    GENERIC_MANA_15 = "$15"
    GENERIC_MANA_16 = "$16"
    GENERIC_MANA_17 = "$17"
    GENERIC_MANA_18 = "$18"
    GENERIC_MANA_19 = "$19"
    GENERIC_MANA_20 = "$20"
    WHITE_MANA = "$W"
    BLUE_MANA = "$U"
    BLACK_MANA = "$B"
    RED_MANA = "$R"
    GREEN_MANA = "$G"
    COLORLESS_MANA = "$C"
    TAP = "$T"
    ENERGY_COUNTER = "$E"
    
punctuation = {
    ".": Tokens.PERIOD,
    ",": Tokens.COMMA,
    ":": Tokens.COLON,
    "—": Tokens.EM_DASH,
    "/": Tokens.SLASH,
    "•": Tokens.BULLET,
    "(": Tokens.LEFT_PARENTHESIS,
    ")": Tokens.RIGHT_PARENTHESIS,
    "\n": Tokens.NEWLINE
}

mtg_symbols = {
    "{1}": Tokens.GENERIC_MANA_1,
    "{2}": Tokens.GENERIC_MANA_2,
    "{3}": Tokens.GENERIC_MANA_3,
    "{4}": Tokens.GENERIC_MANA_4,
    "{5}": Tokens.GENERIC_MANA_5,
    "{6}": Tokens.GENERIC_MANA_6,
    "{7}": Tokens.GENERIC_MANA_7,
    "{8}": Tokens.GENERIC_MANA_8,
    "{9}": Tokens.GENERIC_MANA_9,
    "{10}": Tokens.GENERIC_MANA_10,
    "{11}": Tokens.GENERIC_MANA_11,
    "{12}": Tokens.GENERIC_MANA_12,
    "{13}": Tokens.GENERIC_MANA_13,
    "{14}": Tokens.GENERIC_MANA_14,
    "{15}": Tokens.GENERIC_MANA_15,
    "{16}": Tokens.GENERIC_MANA_16,
    "{17}": Tokens.GENERIC_MANA_17,
    "{18}": Tokens.GENERIC_MANA_18,
    "{19}": Tokens.GENERIC_MANA_19,
    "{20}": Tokens.GENERIC_MANA_20,
    "{W}": Tokens.WHITE_MANA,
    "{U}": Tokens.BLUE_MANA,
    "{B}": Tokens.BLACK_MANA,
    "{R}": Tokens.RED_MANA,
    "{G}": Tokens.GREEN_MANA,
    "{C}": Tokens.COLORLESS_MANA,
    "{T}": Tokens.TAP,
    "{E}": Tokens.ENERGY_COUNTER,
}

def parse_clean(input: str) -> str:
    if type(input) != str : return ""
    output = input.strip().upper()
    return output

def replace_over(string: str, dictionary: dict[str, str], pad_with_spaces = False) -> str:
    out = string
    for k, v in dictionary.items():
        v2 = v
        if pad_with_spaces: v2 = " " + v + " "
        out = out.replace(k, v2)
    return out

def tokenize(input: str, card_name: str = "") -> list[str]:
    cleaned_input = parse_clean(input)
    cleaned_cardname = parse_clean(card_name)
    cleaned_input = cleaned_input.replace(cleaned_cardname, Tokens.CARD_NAME)
    cleaned_input = replace_over(cleaned_input, punctuation, True)
    cleaned_input = replace_over(cleaned_input, mtg_symbols, True)
    cleaned_input = cleaned_input.replace("  ", " ")
    
    output = cleaned_input.split(" ")
    output = [token for token in output if token != ""]
    output = [Tokens.BEGINNING_OF_STRING] + output + [Tokens.END_OF_STRING]
    return output


def main():
    out = tokenize("{t}: Deal 3 damage to any target.", "lightning bolt")
    print(out)

if __name__ == "__main__":
    main()