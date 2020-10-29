# dictionary = {"key:value"}
fruit = {"orange": "a sweet orange citrus fruit", "apple": "good for making cider", "lemon": "a sour, yellow citrus fruit", "grape": "a small, sweet purple fruit growing in bunches", "lime": "a sour, green citrus fruit"}

print(fruit)

# lengthy way
# ordered_keys = sorted(list(fruit.keys()))
  # here is how we are making an unordered list ordered by keys
# for f in ordered_keys:
#     print(f + " - " + fruit[f]) # here we are printing the key(f) and it's corresponding value(fruit[f])

# condensed way of printing out an onordered dictionary, ordered, by key.
for f in sorted(fruit.keys()):
    print(f + " - " + fruit[f])
    

# condensed way of just printing out an onordered dictionary
for f in fruit:
    print(f + " - " + fruit[f])


for val in fruit.values(): # less efficient to print by values for key: value but is an option
    print(val)

# fruit_keys = fruit.keys()

# print(fruit.keys()) # how to print just keys

# print(fruit.values())  # how to print just values

# fruit["tomato"] = "not nice with ice cream"
# print(fruit_keys)  # tomatoes was added to the dictionary

print(fruit.items())  # here we get, similiar to a tuple ([(key: value),(k:v),(k:v)])

f_tuple = tuple(fruit.items()) # here we get a tuple: ((key: value),(k:v),(k:v))
print(f_tuple)

for snack in f_tuple:
    item, description = snack  #here we are able to label the key as an item, and value as a description
    print(item + " is " + description)

print(dict(f_tuple)) #here is how we convert a tuple into a dictionary
