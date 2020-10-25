# A method is a function that is bould to an instance of a class
# print() is a function, but .sort() is a method.
# there is also string methods such as str.casefold.

# You can use methods in the same way as you use functions,
# but specify the objeect that they will act on, before the dot.

def multiply(x,y):
    result = x * y
    return result


def is_palindrome(string):
    # backwards = string[::-1] #slicing the code and looping through it backwards
    # return backwards == string #checking to see if the backward version of string == string
    # return backwards == string will evaluate to return either true or false
    
    return string[::-1].casefold() == string.casefold()  #this is a condensed version of the two lines above
    #remember with . methods have the parentheses at the end like: .casefold()

    # Make sure if a function is meant to return a value, expicitely use use the return keyword

# word = input("Please enter a word to check: ")
# if is_palindrome(word):
#     print("'{}' is a palindrome".format(word)
# else:
#     print("'{}' is not a palindrome".format(word))

def palindrome_sentence(string):
    return is_palindrome(string) #call a function from within another function


sentence = input("Please enter a sentence to check: ")
if is_palindrome(sentence):
    print("'{}' is a palindrome".format(sentence))
else:
    print("'{}' is not a palindrome".format(sentence))

answer = multiply(2, 4)
fortytwo = multiply(6,7)
print(answer)
print(fortytwo)




# Functions are seperated from each other with two blank lines
# A function definition starts with the keyword: def
# multiply is the name of the function
# within the () is where the paremeters go

for val in range(1, 5): #Here we are multiplying numbers 1 up to but not including 5, twice
    two_times = multiply(2, val)
    print(two_times)  # 2,4,6,8
    
# A palindrome is a word that reads the same backwards and forwards like tot,
# Palindromes are used within genetics. Work on DNA sequencing generates vast qunatities of data,
# But standard compression algorithims often don't work well with DNA sequences, ofter making them larger

# Palindromes have been used within DNA sequences to provide a more efficient compression of data

