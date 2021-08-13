"""Blackjack, by Al Sweigart al@inventwithpython.com
The classic card game also known as 21. (This version doesn't have
splitting or insurance.)
More info at: https://en.wikipedia.org/wiki/Blackjack
View this code at https://nostarch.com/big-book-small-python-projects
Tags: large, game, card game"""

import random, sys

# Set up the constants:
HEARTS = chr(9829) # Character 9829 is '♥'.
DIAMONDS = chr(9830) # Character 9830 is '♦'.
SPADES = chr(9824) # Character 9824 is '♠'.
CLUBS = chr(9827) # Character 9827 is '♣'.
 
# (A list of chr codes is at https://inventwithpython.com/charactermap)
BACKSIDE = 'backside'

def main():
    pass

def getBet(maxBet):
    """Ask the player how much they want to bet for this round."""
    # Keep asking until they enter a valid amount.
    while True:
        print('How much do you bet? (1-{}, or QUIT)'.format(maxBet))
        bet = input('> ').upper().strip()
        if bet == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if not bet.isdecimal():
            # If the player didn't enter a number, ask again.
            continue

        bet = int(bet)
        if 1 <= bet <= maxBet:
            # Player entered a valid bet.
            return bet
    

def getDeck():
    """Return a list of (rank, suit) tuples for all 52 cards."""
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            # Add the numbered cards.
            deck.append((str(rank), suit))
        for rank in ('J', 'Q', 'K', 'A'):
            # Add the face and ace cards.
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck

def displayHands(playerHand, dealerHand, showDealerHand):
    """Show the player's and dealer's cards. Hide the dealer's first
    card if showDealerHand is False."""
    print()
    if showDealerHand:
        print('DEALER:', getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print('DEALER: ???')
        # Hide the dealer's first card:
        displayCards([BACKSIDE] + dealerHand[1:])

    # Show the player's cards:
    print('PLAYER:', getHandValue(playerHand))
    displayCards(playerHand)

def getHandValue(cards):
    """Returns the value of the cards. Face cards are worth 10, aces are
    worth 11 or 1 (this function picks the most suitable ace value)."""
    value = 0
    numberOfAces = 0

    # Add the value for the non-ace cards:
    for card in cards:
        # card is a tuple like (rank, suit)
        rank = card[0]
        if rank == 'A':
            numberOfAces += 1
        # Face cards are worth 10 points.    
        elif rank in ('K', 'Q', 'J'):
            value += 10
        else:
            # Numbered cards are worth their number.
            value += int(rank)

    # Add the value for the aces:
    # Add 1 per ace.
    value += numberOfAces
    for i in range(numberOfAces):
        # If another 10 can be added with busting, do so:
        if value + 10 <= 21:
            value += 10

    return value

def displayCards(cards):
    """Display all the cards in the cards list."""
    # The text to display on each row.
    rows = ['', '', '', '', '']

    for i, card in enumerate(cards):
        # Print the top line of the card.
        rows[0] += ' ___  '
        if card == BACKSIDE:
            # Print a card's back:
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            # Print the card's front:
            # The card is a tuple data structure.
            rank, suit = card
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} |'.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, '_'))

    # Print each row on the screen:
    for row in rows:
        print(row)
        

def getMove(playerHand, money):
    """Asks the player for their move, and returns 'H' for hit, 'S' for
    stand, and 'D' for double down."""
    # Keep looping until the player enters a correct move.
    while True:
        # Determine what moves the player can make:
        moves = ['(H)it', '(S)tand']

        # The player can double down on their first move, which we can
        # tell because they'll have exactly two cards:
        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble down')

        # Get the player's move:
        movePrompt = ', '.join(moves) + '> '
        move = input(movePrompt).upper()
        if move in ('H', 'S'):
            # Player has entered a valid move.
            return move
        if move == 'D' and '(D)ouble down' in moves:
            # Player has entered a valid move.
            return move

# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()       
 
