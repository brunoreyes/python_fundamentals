LOW = 1
HIGH = 1000



# it's useful to count the # of guesses. The computer should get correct answer within 10 guesses
# due to halving each time. The computer can guess to 2^10 power in 10 guesses but 1000 is user-friendly


def guess_binary(answer, LOW, HIGH):
    guesses = 1
    while True:
        guess = LOW + (HIGH - LOW) // 2
        if guess < answer: 
            LOW = guess + 1 #Must have valid codes inside each code block, or else you'll get a confusing error
        elif guess > answer:   
            HIGH = guess - 1
        elif guess == answer:
            

            return guesses


        guesses += 1


for number in range(LOW, HIGH + 1):
    number_of_guesses = guess_binary(number, LOW, HIGH)
    print("{} guesses in {}".format(number, number_of_guesses))
    

    #The program only knows the correct answer when high and low converge to the same value