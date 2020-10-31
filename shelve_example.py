# Pickling is great for serialization but it's drawback is that all objects have to be
# loaded back into the computer's memory, which isn't good for large objects or dictionaries.

# Shelve module provides a shelf (file) which it stores the values in and not the computer's memory.

# Shelves, hold key value pairs, and keys must be strings but are immutable objects like in dictionaries,
# but the values can be anything that can also be pickled.

# Dictionaries can have any immutable object as a key, meaning they aren't confined to just strings.

import shelve # Make sure anything imported and the file aren't sharing the same name.


# with shelve.open('ShelfTest') as fruit:  # Here I'm opening a shelve with 'with' like opening a file.
# Shelves are read & write by nature so there is no need to specify the mode.
fruit = shelve.open("ShelfTest")

# COMMENTED OUT ALL FRUIT['FRUIT-ITEM'], B/C EVERYTIME THE CODE IS RAN, ITS RESAVING THE VALUES.
# fruit['orange'] = "a sweet, oragnem citrus fruit"
# fruit['apple'] = "good for making cider"
# fruit['lemon'] = "a sour, yellow citrus fruit"
# fruit['grape'] = "a small, sweet purple fruit, growing in bunches"
# fruit['lime'] = "a sour, green citrus fruit"

# CODE COMMENTED OUT BC IT'S ALREADY BEEN RUN.
    # print(fruit["lemon"]) # Make sure to be inside the "with" block to print items
    # print(fruit["grape"])  # with will close automatically after the "with" block runs

    # fruit["lime"] = "great with tequila" # Updating the value of the key lime

    # for snack in fruit: # for loop through fruit
    #     print(snack + ": " + fruit[snack])



# while True: # in shelves and dictionaries, keys are unordered
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
    
#     if dict_key in fruit:
#         description = fruit[dict_key]
#         print(description)
        
#     else:
#         print("We don't have a " +dict_key)


# ordered_keys = list(fruit.keys())
# ordered_keys.sort()

# for f in ordered_keys:
#     print(f + " - " + fruit[f])


# Most code that works for "dictionaries" works for "shelves" as well.

for v in fruit.value():
    print(v) # here we are printing out an immutable value 

print(fruit.values())

for f in fruit.items():
    print(f)

print(fruit.items())


fruit.close()  # This manually closes the file and allows anything to print before it


# print(fruit) 