data = [4, 5, 104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185, 187, 188, 191, 350, 360] #original test
#data = [104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185, 187, 188, 191, 350, 360]  #test w/o low values
#data = [4, 5, 104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185, 187, 188, 191] #test w/o high values
#data = [104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185, 187, 188, 191] #test w/o low & high values
#data = [1041, 1051, 1101, 1201, 1301, 1301, 1501, 1601, 1701, 1831, 1851, 1871, 1881, 1911] #test w only high values = []
#data = [] #testing for an empty list dataset, we get []
# del data[0:2] #starts the deletion at index 0 and ends at but not including 2, so 4,5 deleted
# print(data)
# del data[14:]  #this deletes 350 and 360, recall that index has been condensed to 16

min_valid = 100
max_valid = 200

# for index, value in enumerate(data):
#     if (value < min_valid) or (value > max_valid):
#         del data[index]

print(data)

#SAFELY REMOVING THE LOWER VALUES FROM THE LIST
#Process the low values in the list
stop = 0
for index, value in enumerate(data):
    stop = index
    break

print(stop)  #for debugging
del data[:stop] #this deletes all data and index's that are = stop only after the loop terminates
print(data)  #the new data without the low data values deleted


#Safely removing the higher values from the list
start = 0
for index in range(len(data) - 1, -1, -1):  #last value in a range isn't included, start,stop, and by
    #print(index)
    if data[index] <= max_valid:
        # We have the index of the last item to keep.
        # Set 'start' to the position of the first item to delete, which is 1 after 'index'
        start = index + 1 #we want to delete starting deleting from position 14 not 13
        break

print(start) #for debugging
del data[start:]
print(data)  #now the list prints out without 350,360
#data = [104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185, 187, 188, 191]

# An edge cas can be expected or unexpected.In engineering, the process of planning
# for and gracefully addressing edge cases can be a significant task, and
# yet this task may be overlooked or underestimated.

#Corner case is like an edge case, but where there is more than one paremeter involved.
#For example, how to handle dividing, when both values are zero
#anything divided by 0 is undefined but divided by itself is one

#Consider outlying value both the low and high ends
#outlying values at low or at high end only
#not outlying values
#empty dataset

# In this example we saw that removing rouge or unexpected values from an unsorted list can be done

# We've seen that we can;t remove items from a list, white iterating forwards over it. If the
# size of the list changes, things go wrong

#When an item is removed from the list, all the later items are shuffled down, to fill in the gap
# Which messes up the index value when working forward through a list

