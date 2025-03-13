"""
game: https://en.wikipedia.org/wiki/Set_(card_game)#
4 features: count, shape, fill, color
# count: ['one', 'two', 'three']
# fill: ['solid', 'striped', 'open'] 
# color: ['red', 'green', 'purple'] 
# shape: ['diamond', 'squiggle', 'oval'] 

each comb exists in the deck
three cards make a set if for each of the features: 
values are all the same 
or all different
"""

import random
import itertools

# Q1: Define card representation (Tuple, etc) and a function to generate a random card

def generate_random_card():
    """
    Generates a random Set card represented as a tuple:
    (number, fill, color, shape)
    
    Each feature is an integer from 0 to 2:
      - number: 0->'one', 1->'two', 2->'three'
      - fill:   0->'solid', 1->'striped', 2->'open'
      - color:  0->'red', 1->'green', 2->'purple'
      - shape:  0->'diamond', 1->'squiggle', 2->'oval'
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    return tuple(random.randint(0, 2) for _ in range(4))

# Q2: Generate n random cards

def generate_n_random_cards(n):
    """
    Generates a list of n random Set cards.
    Time Complexity: O(n)
    Space Complexity: O(n)
    Parameters:
    - n: The number of random cards to generate.
     Returns:
    - A list of n cards, each represented as a 4-tuple.
    """
    return [generate_random_card() for _ in range(n)]

# Q3: Generate n unique cards

def generate_deck():
    """
    Generates the complete deck of 81 unique Set cards.
    
    Each card is represented as a tuple (number, fill, color, shape), where
    each feature is an integer from 0 to 2.
    
    Time Complexity: O(81) which is constant.
    Space Complexity: O(81)
    """
    return [
        (number, fill, color, shape)
        for number in range(3)
        for fill in range(3)
        for color in range(3)
        for shape in range(3)
    ]

def generate_n_unique_random_cards(n):
    """
    Generates n unique random cards from the full deck.
    
    Parameters:
    - n: Number of cards to generate (must be <= 81).
    
    Returns:
    - A list of n unique cards.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    deck = generate_deck()
    if n > len(deck):
        raise ValueError(f"n cannot be greater than {len(deck)}, the number of unique cards available.")
    # random.sample ensures unique selection from the deck.
    return random.sample(deck, n)

# Q4: Take 3 cards, check if they represent a set

def is_set(card1, card2, card3):
    """
    Determines if three cards form a valid set.
    
    Each card is a 4-tuple in the order:
    (number, fill, color, shape)
    
    For each feature, the cards form a valid set if the values
    are either all the same or all different. Using integer values (0, 1, 2)
    for each feature, the sum modulo 3 equals 0 when the feature values
    are either all the same (e.g., 0+0+0) or all different (0+1+2).
    
    Parameters:
      card1, card2, card3: Tuples representing the cards.
    
    Returns:
      True if the cards form a valid set; False otherwise.
    
    Time Complexity: O(1) since we check exactly 4 features.
    """
    for i in range(4):
        if (card1[i] + card2[i] + card3[i]) % 3 != 0:
            return False
    return True

# Q5: given 12 unique cards, find all valid sets

def find_sets(cards):
    """
    Given a list of cards, finds and returns all valid sets.
    
    Parameters:
      cards: List of cards (each a 4-tuple).
      
    Returns:
      A list of tuples, each containing 3 cards that form a valid set.
      
    Time Complexity: O(n³) in the number of cards (for 12 cards, 220 combinations).
    """
    valid_sets = []
    for combo in itertools.combinations(cards, 3):
        if is_set(*combo): # * is needed to unpack the tuple into individual components 
            # equal to writing is_set(card1, card2, card3)
            valid_sets.append(combo)
    return valid_sets

# without the asteryx, it can be 
def find_sets_another(cards):
    valid_sets = []
    for combo in itertools.combinations(cards, 3):
        if is_set(combo[0], combo[1], combo[2]):
            valid_sets.append(combo)
    return valid_sets 