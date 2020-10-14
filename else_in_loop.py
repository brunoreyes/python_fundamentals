#Else in Loop

#else in a loop causes a block of code to be executed if the loop was allowed to contunie to the end.
# In other words, if the loop wasn't broken out of

numbers = [1, 45, 31, 12, 60]
    
for number in numbers:
    if number % 8 == 0:
        #reject the list if any number within the list is divisible by 8
        print("The numbers are unacceptable") 
        break
    else:
        print("The numbers are okay")
        break