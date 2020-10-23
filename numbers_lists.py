even = [2, 4, 6, 8]
odd = [1,3,5,7,9]
# even.extend(odd) #.extend(odd) adds the odd list to the end of the even list

numbers = [even,odd] 
print(numbers) # output: [[2, 4, 6, 8], [1, 3, 5, 7, 9]]

for number_list in numbers:
    print(number_list)

    for value in number_list:
        print(value)

# bracket, 


# another_even = even #here we've just created another list of even which is now even + odd
# print(another_even) 

# even.sort()  #.sort() will sort out the now combined list and print 1 to 9
# even.sort(reverse=True)  # .sort(reverse=True) reverses the order from top to bottom
# .sort doesn't create a copy of the list, instead it mutilates a list and rearranges indexes
# print(even)


