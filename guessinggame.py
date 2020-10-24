import random


def get_integer(prompt):
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)


highest = 10 #this sets 10 guesses 
answer = random.randint(1, highest)
print(answer)   # TODO: Remove after testing
guess = 0 # initialize to any number that can't equal the number
print("Please guess number between 1 and {} or quit by entering 0: ".format(highest))


while guess != answer:
    guess = get_integer(": ")
    if guess == 0:
        break
    if guess == answer:
        print("Well done, you guessed it")
    else:
        if guess == answer:
            print("Please guess higher")
        else:   # guess must be greater than answer
            print("Please guess lower")
        guess = int(input())
        if guess == answer:
            print("Well done, you guessed it")
        else:
            print("Sorry, you have not guessed correctly")
