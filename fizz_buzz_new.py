def fizz_buzz(number: int) -> str:
    ''' fizz_buzz is a function that checks if a user's input is
    divisible by either 3 & 5, 5, or 3, and returns specified keywords for each scenario.
    
     :param number: The number to check.
    :return: 'fizz' if the number is divisible by 3.
        'buzz' if it's divisible by 5.
        'fizz buzz' if it's divisible by both 3 and 5.
        The number, as a string, otherwise.
    '''
    # if (number % 3 == 0) and (number % 5 == 0): 15 is the 1st # divisible by 3 & 5
    if number % 15 == 0:
        return "fizz buzz"
    elif (number % 3 == 0):
        return "fizz"
    elif (number % 5 == 0):
        return "buzz"
    else: #if neither are true return the number
        return str(number)
        

input("Play Fizz Buzz. Press ENTER to start")
print()

next_number = 0  # starts at 0
# Since we increment next_number twice, while loop is more suitable than a for loop
while next_number < 99:
    next_number += 1 #incrementing once
    print(fizz_buzz(next_number))
    next_number += 1 #incrementing twice, before calling the fizz_buzz function
    correct_answer = fizz_buzz(next_number)
    players_answer = input("Your go: ")
    if players_answer != correct_answer:
        print("You lose, the correct answer was {}".format(correct_answer))
        break
    else:
        print("Well done, you reached {}".format(next_number))
# for i in range(1,101):
    # print(fizz_buzz(i))


# Pseudocode is code that you write in a simplified language - usually a simple version
# of your native language.

# It's simplified, bc computer languages are much simplier than human languages
# and don;t have to follow as many gramatical rules or deal with so many words.

# So the computer and programer take turns.


# BASIC STEPS

# 1. Calculate the computer's "number" (which may be a number, or be "fizz", "buzz", or "fizz buzz")

# 2. Print the computer's response

# 3. Calculate the player's correct answer

# 4. Get input from the player

# 5. Compare the correct answer to the players input

# 6. Repeat the process, until the player makes a mistake or we reach 100

# 7. Print a suitable message: "Congratulations" or "Wrong"
