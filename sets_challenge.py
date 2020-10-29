# Create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in alphabetical order.

# You can either enter the text from the keyboard or initialize a string variable with the string.


# Instead of for loops we can print the differences between the sample text and vowels, leaving vowels.
sampleText ="Python is a very powerful language"
vowels = frozenset("aeiou") #frozen set makes a set immutable so you can't add, discard or remove from it.
finalSet = set(sampleText).difference(vowels)
print(finalSet) 

finalList = sorted(finalSet)
print(finalList) #we want to create a new variable called finalList bc list are ordered while sets aren't