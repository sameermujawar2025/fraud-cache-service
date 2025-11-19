import pandas as pd

def normalize_card_number(card):
    """
    Safely convert card numbers to string format.

    Handles:
    - int (4051935252595755)
    - float (4.051935252595755e+15)
    - floats ending with .0 (4051935252595755.0)
    - scientific notation
    - already-correct strings
    """

    if pd.isna(card):
        return None

    # Convert to string
    card_str = str(card).strip()

    # Remove trailing .0 from floats
    if card_str.endswith(".0"):
        card_str = card_str[:-2]

    # Fix scientific notation
    if "e" in card_str.lower():
        try:
            card_str = "{:.0f}".format(float(card))
        except:
            pass

    return card_str
