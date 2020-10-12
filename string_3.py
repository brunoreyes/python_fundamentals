#A sequence is an ordered set of items
#"Hello World" contains 11 intems, and each item is a character, thus it is an ordered set of items

#A list such as the one below is a sequence type
# A sequence is a list of strings, each item is considered a sequence as well,
# a list is comprised of multiple sequences within a sequence
#since a sequence is ordered, we can use indexes to access individual items in the sequence.
computer_parts = ["pc", "mouse", "monitor"]
computer_parts[1]  # this is the string mouse bc it is index[1]

#recall that you can obtain values from an index of a sequence as well as shown below
print(computer_parts[0][1])  # this should produce the letter c
print(computer_parts[2][-3:-6:-1])  #tin

#this sequence type can be multiplied and concatenated but some sequence types can't be concatenated like ranges
string1 = "he's "
string2 = "probably "
string3 = "pining "
string4 = "for the "
string5 = "fjords "
print(string1 + string2 + string3 + string4 + string5)
print("he's " "probably " "pining " "for the " "fjords ")

#strings can be multiplied, this prints Hello 5 times on the same line
print("Hello " * 5)

print("Hello " * (5 + 4))
print("Hello" * 5 + " 4")

today = "friday"
print("day" in today)  #since day is in today, it prints true
print("fri" in today) #since fri is in today, it prints true
print("thurs" in today) #since thurs isn't in today, it prints false
print("parrot" in "fjord")  #since parrot isn't in fjord, it prints false

#every datatype can be conversed into a string concatenation
age = 24
print("My age is " + str(age) + " years")  # prints a string saying My age is 24 years
print("My age is {0} years".format(age))  #this takes age and formats the string, replacing the array with the first
# value of the format list, which in this case is 24, {0}, with it.

#now we can straight input values into their areas, based on their order index within the sequence
print("These are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}".format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec",))

print("There are {0} days in Jan, Mar, May, Jul, Aug, Oct and Dec".format(31))

#here we are finding the squared and cubed version of numbers 1-13
for i in range(1, 13):
    print("No. {0} squared is {1} and cubed is {2}".format(i, i ** 2, i ** 3))  # i**2 = i^2
    
#Now lets try formatting
for i in range(1, 13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))  # the # in {1:#}
# makes the field formatted to as long as the # is, so if {2:4} there would be 4 spots in index 2
# like this, thus easier to read:
# No.  8 squared is  64 and cubed is  512
# No.  9 squared is  81 and cubed is  729
# No. 10 squared is 100 and cubed is 1000

for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))
    #< makes left aligned, othervise it is defaulted to right align, ^ makes it center aligned.

# f-strings work for Python 3.4 and above, not any previous editions
print("Pi is approximately {0:12}".format(22 / 7))  #general format defaults to printing 15 decimals points
print("Pi is approximately {0:12f}".format(22 / 7)) # with f, we create a floating point value, defaulting to a max of 6 decimal points
print("Pi is approximately {0:12.50f}".format(22 / 7))#python ignores the field width: 12 & goes for 50 decimal points bc it values precision 
print("Pi is approximately {0:52.50f}".format(22 / 7))#field width of 52 but the greatest precision decimal point is 50  
print("Pi is approximately {0:62.50f}".format(22 / 7))#field width of 62 but the greatest precision decimal point is 50 
print("Pi is approximately {0:72.50f}".format(22 / 7))  #field width of 72 but the greatest precision decimal point is 50


print("Pi is approximately {0:<72.54f}".format(22 / 7))
#left-aligned field width of 72 but the greatest precision decimal point is 54, but we only get one other digit
# Pi is approximately 3.142857142857142793701541449991054832935333251953125000 

for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))
    #here we inputted a field width of 4 w/o the # of the index, and still, the same indexs are utilized. (i, i ** 2, i ** 3)
    #so w/o providing a field # we can't use an index # more than once or change the order of the index #'s



print(f"Pi is appoximately {22 / 7:12.50f}") \
# here we are calculating pie, giving a field width of 12, but python will go to 50 decimal points bc it values presision more
pi = 22 / 7
print(f"Pi is appoximately {pi:12.50f}")
# Pi is appoximately 3.14285714285714279370154144999105483293533325195312
# Pi is appoximately 3.14285714285714279370154144999105483293533325195312

