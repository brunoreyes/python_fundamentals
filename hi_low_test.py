LOW = 1
HIGH = 2047
# 2^11 = 2048, so the # should be guessed in 11 guesses or less


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

correct_count = 0
max_guesses = 0
for number in range(LOW, HIGH + 1):
    number_of_guesses = guess_binary(number, LOW, HIGH)
    print("{} guesses in {}".format(number, number_of_guesses))

    if number_of_guesses > max_guesses:
        max_guesses, correct_count = number_of_guesses, 1
    elif number_of_guesses == max_guesses:
        correct_count += 1

print("I guessed correctly {} times. Max {} guesses."
    .format(correct_count, max_guesses))

    #The program only knows the correct answer when high and low converge to the same value