# a List in Python, is an ordered sequence of values, enclosed in square brackets. Such as a shopping list with food items
shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]  # In python, lists items could be strings, numbers, booleans, etc.

#for item in shopping_list:
#    if item != "spam": 
#    print("Buy " + item) #This will give the user a reminder to buy each item on the list

for item in shopping_list:
    if item == "spam":
        continue  #here continue skips over any item =="spam" and continue with the rest of the list items
        #break #here break will end the loop and stop right before spam
    
    print("Buy " + item)
    
item_to_find = "spam"
found_at = None  #None is a constant that shows something doesn't have a value, its equivalent to null
#found_at now exist but has no value

#for index in range(6);
# for index in range(len(shopping_list)): #len is short for length, letting us know how many items are in the list
    # if shopping_list[index] == item_to_find: #here each index or item of the shopping list, if equal to "spam" then = null
        # found_at = index
        # break #now, once we found the item not to buy, let's break the code to stop it
if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)
    
if found_at is not None:
    print("Item found at position {}".format(found_at))
else:
    print("{} not found".format(item_to_find))

