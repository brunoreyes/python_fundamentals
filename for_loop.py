parrot = "Norwegian Blue"

for character in parrot:
    print(character)
#prints each character in the variable parrot on a seperate line

# number = "9,223;372:036 854,775:807"
number = input("Please enter a series of numbers, using any separators you like:")
separators = ""  #separators now are ',;: ,:'

for char in number: 
    if not char.isnumeric():  #0,and negative numbers don't work w/ is numeric
        separators = separators + char
#number[1::4]
print(separators)
values = "".join(char if char not in separators else " " for char in number).split()
print(sum([int(val) for val in values])) # takes the list of numbers and adds them together
