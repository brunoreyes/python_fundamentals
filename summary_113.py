# Lists are mutable, unlike strings, which are a sequence type. The content of list can be changed (mutalated)

# Indexing and slicing in lists are common sequence operations such as min, max, index, count, and len
# Append, a method used to add new values, can only be used with a mutable sequence type such as list,

# Various ways to create lists, which include a list literal, slice, concatenation, and list comprehensions

#the sorted function will sort any iterable or literal object and return a new list

#the list function can be used to create a list from any iterable, with the items in the
# string appearing in the same order

# iterating over an object changes the size of the object

# The example we used was removing the outlying numbers from an ordered list.

# Testing for scenarios is vital to ensure there are no bugs

# Make sure to test for edge and corner cases.

# An edge case is a problem or situation that occurs at an extreme operation parameter.

#A corner case is similar, but when there's more than one parameter involved.

# We can iterate backwards to remove items from either a sorted or unsorted list

# The reversed function is one of the ways of doing this, with the advantage we can use enumerate

# We compared performance and saw the longer code that accounted for multiple things at multiple times
# was ultimately the most efficent code. 