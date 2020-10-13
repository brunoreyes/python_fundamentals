#Trying to guess a number between 1 and 1000 is difficult & the guess will be wrong 999 times
# If we guess half of 1000, we would be left with 500, reducing our error to 499 times.
#If we guessed half of 500, we would be left with 250, reducing our error of being wrong by half
# so on and so forth. This is how binary search works

#When you have an ordered set of data to search through, you can split the data in half each time.
#Guessing a number is like searching through an ordered dataset
#The most effieicent way to find an item in an ordered list is a binary search/chop

#Hilo
low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("Press ENTER to start")

# it's useful to count the # of guesses. The computer should get correct answer within 10 guesses
# due to halving each time. The computer can guess to 2^10 power in 10 guesses but 1000 is user-friendly

guesses = 1
while True:
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
