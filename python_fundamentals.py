print("Today is a good day to learn Python")
print("Python is fun")
print("We can even include 'quotes' in strings")
print( "Python's string are easy to use")
print("hello" + " world")  
# if we want a place we can add that too!

#the \n splits lines on text
splitString = "This string has been\nsplit over \nseveral \nlines"
print(splitString)
greeting = "Hello"
# name = input("Please enter your name ")
# print(greeting + ' ' + name)
# output: 
# This string has been
# split over 
# several 
# lines

# the \t tabs out lines of text
tabbedString = "1\t2\t3\t4\t5\t6\t7"
# output: 1   2   3   4   5   6   7

#you can either use two backslashes or put r for raw before the string
# to ensure that the backslashes aren't confused for commands
print("C:\\Users\\timbuchalka\\notes.txt")
print(r"C:\Users\timbuchalka\notes.txt")

age = 24
print(age)
#Variales in python can begin with either a lowercase or uppercase letter or _ but nut a number

#type(whatever) tells us what type of variable it is, the kind of info we are storing
print(type(greeting))
print(type(age))

#Python allows you to change the type of variable, not the case for C or JAVA
age = 24
print(age)
print(type(age))
name = "bob"

age_in_words = "2 years"

# print(name + "is" + age + "years old")
# we cannot concatenate a string with an integer
#Python will not convert this integer into a string like Java

print(type(age))
print(age_in_words)
