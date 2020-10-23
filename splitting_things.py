panagram = "The quick brown fox jumps over the lazy dog"
panagram = """The quick brown
 fox jumps\tover
the lazy dog"""
words = panagram.split()
print(words)  #['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
# We get a list containing all of the words in a string
#.split, splits values that have any whitespace

numbers = "0,223,372,036,854,775,807"
print(numbers.split(","))

# values = ''.join(char if char not in separators else ' ' for char in numbers).split()
generated_list = ['9', ' ', '2', '2', '3', ' ', '3', '7', '2', ' ', '0', '3', '6', ' ', '8', '5', '4', ' ', '7', '7', '5', ' ', '8', '0', '7']
values = ''.join(generated_list)
print(values)
values_list = values.split()
print(values_list)

# join will let you create a string from a sequence
# split will split the string up again and creating a list

# Use a for loop to produce a list of ints, rather than strings.
# You can either modify the contents of the 'value_list' list in place,
# or create a new list of ints

# Creating a new list
integer_values = []
for value in values_list:
    integer_values.append(int(value))

print(integer_values)

# or 

# Mutalating an existing list by converting the values into integers
for index in range(len(values_list)): #len of values_list gives us the length of the list
    values_list[index] = int(values_list[index])  #this prints out the same list but changes
    # the value to it's integer equivelent 

print(values_list)