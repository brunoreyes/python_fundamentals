import sys

def getint(prompt):  # getting int from input instead of a string from input
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Invalid number entered, please try again")
        except EOFError:
            sys.exit(1)

first_number = getint('input first number ')
second_number = getint('input second number ')
# divided number has to be inputted within the format rather than here

try:
    print("{} divided by {} is {}".format(first_number, second_number, first_number / second_number))
except ZeroDivisionError:
    print("What are doing dividing by zero???")
    sys.exit(2)
