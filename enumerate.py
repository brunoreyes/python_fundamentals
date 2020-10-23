# for index, character in enumerate("abcedfgh"):
    # print(index, character)  #here we print a number that is tied to character
    # using enumerate is much more efficient to get index and values than going by the index() is
for t in enumerate("abcdefgh"):
   # print(t)  # Now we have 8 tuples, we need to remember to unpack tuples
    index, character = t #here we are unpacking all of abcdefgh
    print(index,character)
    
# index, character = (0, 'a') #here we are unpacking both
# print(index)
# print(character)
