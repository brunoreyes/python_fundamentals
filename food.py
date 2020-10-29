fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

print(fruit)

veg = {"cabbage": "every child's favourite",
       "sprouts": "mmmmm, lovely",
       "spinach": "can I have some more fruit, please"}

print(veg)

# veg.update(fruit) # with .update() we can add one list to the oter
# print(veg)
#
# print(fruit.update(veg))
# print(fruit)

nice_and_nasty = fruit.copy() #create a new dictionary with the same items using .copy()
nice_and_nasty.update(veg)
print(nice_and_nasty)
print(veg)
print(fruit)