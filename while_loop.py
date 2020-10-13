# Python has for and while loops
#We've seen how a for loop can be used to iterate through an iterable.
# In our examples, we used the items in a sequence and the numbers in a range.

#Sometimes we need to keep looping as lang as some condition is True, and stop
#when it becomes False

i = 0
while i < 10: #printing 1-9
    print("i is now {}".format(i))
    i += 1  #when the condition is greater than 9, it ends, i should end, the loop should not run forever
    
