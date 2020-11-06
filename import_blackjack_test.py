import blackjack
# from blackjact import * # everything in the blackjack module is accessed through "*"

g = sorted(globals())

for x in g:
    print(x)


# print(__name__) # do not change value of any __value__ starting and ending with double underscores

# underscores like "__" are used to differentiate variables, they are differentiate private or protected
# do not name an object that starts with "_" bc you can accidentally change something.
# any variable that starts with "_", isn't imported
# python3 -m blackjack



# blackjack.deak_card(blackjack.dealer_card_frame) # this only works with an "import blackjack" w/o *
# blackjack.play()
# print(blackjack.cards)