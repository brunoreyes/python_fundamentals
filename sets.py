# a Set in python is Unordered and doesn't contain duplicates like dictionaries.
# However unlike a dictionary, an item in a set can't be accessed by a key
# Set elements are hashed like dictionary keys and are also immutable

# you can define a set using curly braces like a dictionary: {}

# 1st way to create sets using curly braces
farm_animals = {"sheep", "cow", "hen"} 
print(farm_animals)

for animal in farm_animals:
    print(animal)

print("=" * 40)

# 2nd way to create sets by passing a list in a built in set building function
wild_animals = set({"lion", "tiger", "panther", "elephant", "hare"}) 
print(wild_animals)

for animal in wild_animals:
    print(animal)
    
farm_animals.add("horse")
wild_animals.add("horse")
print(farm_animals)
print(wild_animals)

# empty_set = set()
# empty_set_2 = {}
# empty_set.add("a") #easy way to add on to a set
# # empty_set_2.add = ("a")

# even = set(range(0, 40, 2))  #start, end but not including so (39), increase by 2
# print(even)

# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple) # it's possible to convert a tuple into a set and we'll must likely do so
# print(squares)

even = set(range(0, 40, 2))
print(even)
print(len(even))
squares_tuple = (4, 6, 9, 16, 25)
squares = set(squares_tuple)
print(squares)
print(len(squares))

print(even.union(squares))  # with .union() we are adding the square tuple values,
# however if the value that is added is a duplicate item, it is left behind,
# b/c sets do not allow duplicate items

print(len(even.union(squares)))

print(even.intersection(squares)) # with .intersection() we can get the same values that are in both list
print(even & squares) # the & can help print multiple list
print(squares.intersection(squares)) # for ex: if start ={1,2} & finish ={2,3} the same value would be 2

print(sorted(even)) # just like dictionaries, sets can be sorted as well
print(sorted(squares))

print("even minus squares")
print(sorted(even.difference(squares))) #here we are getting only the values which are different in each
print(sorted(even - squares)) # we are subtracting sets! and most cancel out accept the values in common

print("squares minus even")
print(squares.difference(even))
print(squares - even)

print("=" * 40)
print(sorted(even))
print(squares)
even.difference_update(squares) #difference_update prints out what is different in even from squares
print(sorted(even))  # for ex: if even ={1,2} & squares ={2,3}, the value 1 from even would be printed
#b/c it's the only value in even that is not in squares.

# It works the same way for squares.difference_update(even) where only the different values from square prints

print("symmetric even minus squares")
print(sorted(even.symmetric_difference(squares))) # symmetric difference returns all of the same values they both contain

print("symmetric squares minus even")
print(sorted(squares.symmetric_difference(even)))

# there is two ways to remove an item from a set
# 1. Discard, will not rainse an error if the item doesn't exist
# 2. Remove, will raise an error if the item doesn't exist

# squares.discard(4)
# squares.remove(16)
# squares.discard(8)  # will not get an error, b/c the
#squares.remove(8) # will get an error, so make sure the item is in the set before using remove
# try: #we try here, meaning it might not work
#     squares.remove(8)  #we use remove when we want an indication or error that something wasn't removed.
# except KeyError: #with except, we've trapped the error and are printing out a statement
    # print("Item 8 is not a member of the set")

# is_subset test if a set is a subset of another if all the members are contained in the other set
# is_superset is the superset of another if it contains all of the set's members
if squares.issubset(even):
    print("squares is a subset of even")

if even.issubset(squares):
    print("even is a subset of squares")


even = frozenset(range(0, 100, 2))
print(even)
even.add(3)