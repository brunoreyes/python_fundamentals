# Due to Python 3.6 update, no longer see random behaviour, when printing the dictionary keys.
# Dictionaries and sets are unordered collections, so an index is meaningless in a dictionaries.
# Dictionaries and sets cannot contain any duplicate items. Dictionary items are accessed by a key.
# in the example below, the key would be the first part of the item or the names of the fruit

numbers = {
    1: 'one',
    3: 'three',
    5: 'five',
    7: 'seven',
    9: 'nine',
}
 
print("I can count odd numbers in order")
for key in numbers:
    print(numbers[key])
 
numbers[8] = 'eight'
numbers[2] = 'two'
numbers[6] = 'six'
numbers[4] = 'four'
 
print()
print("I can count to 9 in order")
for key in numbers:
    print(numbers[key])
 
# If your code relies on the keys being sorted, sort them first
print()
print("I really can")
for key in sorted(numbers):
    print(numbers[key])


bike = {"make": "Honda", "model": "250 dream", "colour": "red", "engine_size": 250}
print(bike["engine_size"])

# dictionary = {"key:value"}
fruit = {"orange": "a sweet orange citrus fruit", "apple": "good for making cider", "lemon": "a sour, yellow citrus fruit", "grape": "a small, sweet purple fruit growing in bunches", "lime": "a sour, green citrus fruit"}
# a bad way to update a value is to put another apple item in there with another value.

for i in range(3): # printing the list 3 times
    for snack in fruit: # In a dictionary, we can still iterate over items, but the order changes each time
        print(snack + " is " + fruit[snack]) # snack is the key and fruit[snack] is the value
    print('-' * 40) #here we are making a line
# print(fruit)
print(fruit["apple"])
fruit["pear"] = "an odd shaped apple"  # how to add an item to a dictionary
print(fruit)
fruit["pear"] = "great with tequila"  # how to update an item in a dictionary
del fruit["lemon"]  # this is how to delete an item in a dictionary
# with del make sure to solely delete the one entry or else risk deleting the whole dictionary
# fruit.clear() #here we can turn a full dictionary into an empty dictionary like this: {}
# print(fruit["tomato"]) #here we get an error bc they key: tomato doesn't exist
while True:
    dict_key = input("Please enter a fruit: ") #here we are asking for an input = dict_key
    if dict_key == "quit":  #if the input is quit, we choose to break below
        break
    description = fruit.get(dict_key, "We don't have a " + dict_key)
    print(description)

    # Lengthy way of doing it
    # if dict_key in fruit:  #if the dict_key is in the dictionary fruit, we print out it's description
    #     description = fruit.get(dict_key)
    #     print(description)
    # else:
    #     print( dict_key + " not available") # Otherwise we say the dict_key is not available



