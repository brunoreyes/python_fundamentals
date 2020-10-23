#Removing Items Form A List Backwards

#Working through a list backwards

# If we remove an item at position q0, all the items above that would be shuffled down,
# but the indexes from 9 to 0 down wouldn't be affected.

#A way to be careful when changing your list is to iterate backwards

#iterating backwards is a valuable technique, and allows the size of your sequence to be changed
# without causing problems

data = [104, 101, 4, 105, 308, 103, 5, 107, 100, 306, 106, 102, 108]
#Testing for edge cases
# data = [104, 101, 4, 105, 103, 5, 107, 100, 106, 102, 108] w/o max val
# data = [104, 101, 105, 308 ,103 , 107, 100 , 306, 106, 102, 108] w/o min val
# data = [104, 101, 105, 103, 107, 100, 106, 102, 108] w/o max & min val
# data = [306,203, 1] only max & min val
# data = [] empty list

min_val = 100
max_val = 200
#We will try to remove: 4, 5, 308, and 206

# for index in range(len(data) - 1, - 1, - 1):  #starting from -1, ending at -1, going down by 1
#     if data[index] < min_val or data[index] > max_val:
#         print(index, data)  #checking we are getting what we expect
#         del data[index]

top_index = len(data) - 1
for index, value in enumerate(reversed(data)):  # this reverses the data but keeps indexes in the same place
    if value < min_val or value > max_val:
        # print(index,value) #output: 0 108   1 102   3 306 and so on..
        print(top_index - index, value)  #here we get the code coming out in the real index
        del data[top_index - index]

print(data)
        