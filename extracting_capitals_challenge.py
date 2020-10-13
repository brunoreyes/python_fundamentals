#Write a program to print out the capital letters in a string

quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""
 
# Use a for loop and an if statement to print just the capitals in the quote above.

for character in quote:
    if character.isupper(): # .isupper() checks if a character is uppercase, which if it is, it's true, else false
        print(character) #for every character that is uppercase, we will print it out