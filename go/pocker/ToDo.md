- INPUT
  -[X] Separate from the given string the two player's hand
  -[ ] Player
    -[x] Hand
      -[X] A slice of ordered values
      -[x] A slice of unordered suits

- CLASSIFICATION
  - Each player has a hand classified in one of these categories:
    -[X] Straight flush (suit, values): 5 cards of the same suit with consecutive values.
    -[X] Four of a kind (values): 4 cards of the same value.
    -[X] Full house (values): 3 cards of the same value and a _pair_.
    -[X] Flush (suit): 5 cards of the same suit.
    -[X] Straight (values): 5 cards with consecutive values.
    -[X] Three of a kind (values): 3 cards of the same value. 
    -[X] Two pairs (values): 2 different _pairs_.
    -[X] Pair (values): 2 cards of the same value.
    -[ ] High card (values): ordered values.

- RULES
  -[ ] Straight flush: if only one of the players has _straight flush_ WINS. If both of theme has _straight flush_, WINS
    the player with the highest card in the hand.
  -[ ] Four of a kind: if only one of the players has _four of a kind_ and the other one has a lower hand, WINS the first
    one. If both of theme has _four of a kind_, WINS the player with the highest value of the "four". If both of theme has 
    the same value of the "four", WINS the player with the highest five value card.
  -[ ] Full house: If only one of the players has _full house_ and the other one has a lower hand, WINS the first one. If
    both of theme has _full house_, WINS the player with the highest value of the "three". If both of theme has the same
    "three" value, WINS the player with the highest pair.
  -[ ] Straight: If only one of the players has _straight_ and the other one has a lower hand, WINS the first one. If both
    of theme has _straight_ WINS the player with the highest card in the straight.
  -[ ] Three of a kind: If only one of the players has _three_ and the other one has a lower hand, WINS the first one. If
    both of theme has _three_, WINS the player with the highest _three_. If both of theme has the same _three_, WINS the
    player with the highest card from the rest two.
  -[ ] Two pairs: If only one of the players has _two pairs_ and the other one has a lower hand, WINS the first one. If
    both of theme has _two pairs_, WINS the player with the highest pair. If both of theme has one same pair, WINS the
    player with the highest other pair. If both of theme has the same _two pairs_, WINS the player with the highest last
    card.
  -[ ] Pair: If only one of the player has a _pair_ and the other one has a lower hand, WINS the first one. If both of 
    theme has a _pair_, WINS the player with the highest _pair_. If both of theme has the same _pair_, WINS the player
    with the highest card from the rest in decreasing order.
  -[ ] High Card: If either player has a highest ranked hand, WINS the player with the highest card in decreasing order.