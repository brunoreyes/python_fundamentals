# A Tuple is a mathamatical name for an ordered set of data

# For Python, being ordered is a requirement for a sequence

# Tuples are of of the sequence types we've seen; along with strings, lists and ranges.

# Tuples differ from lists b/c tuples are immutable (can't be changed after created), like strings

t = "a", "b", "c"
t = ("a", "b", "c")  #prints out exactly the same
#try to always use parentheses with tuples. 
print(t)  #('a', 'b', 'c') notice the parentheses, and not square brackets, this signifies a tuple

name = "Tim"
age = 10

print((name, age, "Python", 2020))  #must use parentheses to make this a tuple

#tuples are immutable

