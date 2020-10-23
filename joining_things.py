#don't call any python files the name of functions

flowers = [
    "Daffadil",
    "Evening Primrose",
    "Hydrangea",
    "Iris",
    "Lavender",
    "Sunflower",
    "Tiger Lily"
]

#for flower in flowers: # a list is an iterable, like flowers
    #print(flower)

separator = ' | '
output = separator.join(flowers)
print(output)  #output: Daffadil | Evening Primrose | Hydrangea | Iris | Lavender | Sunflower | Tiger Lily
#this output is much cleaner, with a ' | ' between each item, an all items on the same line using .join

separator = ', '
output = separator.join(flowers)
print(output)  #now the output hase a ", " between each value within the object
# you can either use seperator as an argument/ variable or just insert the comma within the join like so:
print(", ".join(flowers)) #if you want to join items, all of the items most be strings and nothing else
