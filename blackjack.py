import random

try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter
    
#TK_SILENCE_DEPRECATION = 1

def load_images(card_images):
    suits = ['heart','spade', 'club', 'diamond' ]
    face_cards = ['jack', 'queen', 'king']
    
    if tkinter.TkVersion >= 8.6:
        extension = 'ppm'
    else:
        extension = 'ppm'

    # for each suit, retireve the image for the cards
    for suit in suits:
        # first the number cards 1 to 10
        for card in range(1, 11):  # up to but not including 11 (so 1-10)
            name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image))

        # next, the face cards
        for card in face_cards:
            name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image))

            
# dealing cards to player after "deal" button is clicked
def deal_card(frame): # with Python 3 every widget is it's own thing, don't mix a frame and grid in same window
    # pick (pop) the top card off the top of the deck
    next_card = deck.pop(0)  # pop retrieves an item from a list and removes the first item "deck[0]" as well
    # adding the image to a label and displaying the label
    # if 52 cards are picked, there will be an error bc it's not allowed to use .pop() on an empty list
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')
    # now return the card's face value
    return next_card

def score_hand(hand):
    # Calculate the total score of all cards within a list.
    # Only one ace can have the value 11, and this will be reduced to 1 if the hand would bust.
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        # if we would bust, check if there is an ace and subtract 10
        if score > 21 and ace:
            score -= 10
            ace = False
    return score

# checking if dealer wins
def deal_dealer(): 
    dealer_score = score_hand(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(deal_card(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)

    player_score = score_hand(player_hand)
    dealer_score_label.set(dealer_score)
    if dealer_score > 21 or dealer_score < player_score:
        result_text.set("Player wins!")
    elif dealer_score > player_score:
        result_text.set("Dealer wins!")
    else:
        result_text.set("Draw!")

# checking if player wins
def deal_player():
    player_hand.append(deal_card(player_card_frame))
    player_score = score_hand(player_hand)
    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("Dealer wins!")

    # # player_score = 0 just to check if each card's value is correct, now we need a key for the local var.
    # global player_score # the keyword "global" allows us to access the global var: player_score
    # global player_ace

    # card_value = deal_card(player_card_frame)[0]
    # # checking for the first ace = 11, all other ace's afterwards = 1
    # if card_value == 1 and not player_ace:
    #     player_ace = True
    #     card_value = 11
    # player_score += card_value
    # # if we bust, check if there is an ace and subtract
    # if  player_score > 21 and player_ace: # local var:"player_ace" is created, no longer linked to global var
    #     player_score -= 10 # accounting for player_ace already chosen, now ace = 1 instead of 11
    #     player_ace = False
    # player_score_label.set(player_score)
    # if player_score > 21:
    #     result_text.set("Dealer wins!")  # if the player score over 21, they lose the game and dealer wins
    # print(locals())

def initial_deal():
    deal_player() # Draws the player a card
    dealer_hand.append(deal_card(dealer_card_frame))  # Deal out the first card for the dealer
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player() # Draws another card for the player

def restart_game():
    global player_card_frame
    global dealer_card_frame
    player_score = 0
    dealer_score = 0
    global dealer_hand
    global player_hand
    # embedded frame to hold the card images
    dealer_card_frame.destroy()
    dealer_card_frame = tkinter.Frame(card_frame, background="green")
    dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)
    # embedded frame to hold the card images
    player_card_frame.destroy()
    player_card_frame = tkinter.Frame(card_frame, background="green")
    player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)

    result_text.set("")
    
    # Create the list to store dealer's & player's hands
    dealer_hand = []
    player_hand = []
    initial_deal()
    


def shuffle_deck():
    random.shuffle(deck)


def play():
    initial_deal()
    mainWindow.mainloop() #loop that runs the game


mainWindow = tkinter.Tk()

# Set up the screen and frames for the dealer and player
mainWindow.title("Black Jack") # Header of pop-up window
mainWindow.geometry("640x480")  # Size of pop-up window
mainWindow.configure(background='green')

# Card space!
result_text = tkinter.StringVar() # .StringVar() Holds a string, and has a default of an empty string: ""
result = tkinter.Label(mainWindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3) # columnspan=3 builds out 3 columns: | col 1 | col 2 | col 3 |

# Background Setup - Green Table
card_frame = tkinter.Frame(mainWindow, relief="sunken", borderwidth=1, background="green") # .Frame creates background
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

# Dealer's score
dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", background="green", fg='white').grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background="green", fg="white").grid(row=1, column=0)

# Embedded frame hold the card images for dealer
dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

# Players's score (below dealers)
player_score_label = tkinter.IntVar()

# player_score = 0 # global vars no longer needed, replaced with local vars
# player_ace = False
tkinter.Label(card_frame, text="Player", background="green", fg="white").grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background="green", fg="white").grid(row=3, column=0)

# Embedded frame to hold the 2nd row of card images for player
player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)

button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0, sticky="w", rowspan=3)

dealer_button = tkinter.Button(button_frame, text="Dealer", command=deal_dealer) 
dealer_button.grid(row=0, column=0) #command sets an action for a button

player_button = tkinter.Button(button_frame, text="Player", command=deal_player)
player_button.grid(row=0, column=1)

restart_button = tkinter.Button(button_frame, text="Restart Game", command=restart_game)
restart_button.grid(row=0, column=2)  #command sets an action for a button

shuffle_button = tkinter.Button(button_frame, text="Shuffle Deck", command=shuffle_deck)
shuffle_button.grid(row=0, column=3)  #command sets an action for a button

#load cards
cards = []
load_images(cards)
# print(cards)

# Creating a new deck of cards & shuffling them
# Create a new and separate list prevents issues with cards being dealt and being removed from the list 

# deck = list(cards) + list(cards) + list(cards) # Adding multiple decks
deck = list(cards) + list(cards) + list(cards)

shuffle_deck()

# Create the list to store dealer's & player's hands
dealer_hand = []
player_hand = []

restart_game()

# Code moved from global to local within restart_game()
# deal_player() # Draws the player a card
# dealer_hand.append(deal_card(dealer_card_frame))  # Deal out the first card for the dealer
# dealer_score_label.set(score_hand(dealer_hand))
# deal_player() # Draws another card for the player

# print(__name__)
if __name__ == "__main__": # test to see if we are within the right scope
    play()
