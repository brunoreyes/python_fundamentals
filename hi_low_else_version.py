low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("Press ENTER to start")

# it's useful to count the # of guesses. The computer should get correct answer within 10 guesses
# due to halving each time. The computer can guess to 2^10 power in 10 guesses but 1000 is user-friendly

guesses = 1
while low != high:
    print("\tGuessing in the range of {} to {}".format(low,high)) #current range the computer can guess
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should I guess higher or lower?"
                    "Enter h, l, or c if if my guess was correct "
                    .format(guess)).casefold()
    
    if high_low == "h":  #Guess higher. The low end of range becomes 1 greater than the guess.
        low = guess + 1 #Must have valid codes inside each code block, or else you'll get a confusing error
    elif high_low == "l":  #Guess  lower. The high end of the range becomes 1 less than the guess
        high = guess - 1
    elif high_low == "c":
        print("I got it in {} guesses!".format(guesses))
        break #now that you've got thr correct guess, the while loop breaks
    else:
        print("Please enter h, l, or c")

    guesses = guesses + 1
else:
    print("You thought of the number {}".format(low))
    print("I got it in {} guesses!".format(guesses))

#The program only knows the correct answer when high and low converge to the same value