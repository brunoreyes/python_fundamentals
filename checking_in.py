parrot = "Norwegian Blue"
letter = input("Enter a character: ")

if letter in parrot: #case sensativity matters, "B" will print if statement and "b" will print else statement.
    print("{} is in {}".format(letter, parrot))
else:
    print("I don't need the letter")

