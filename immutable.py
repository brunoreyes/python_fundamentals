# immutable meaning cannot be changed
# the following are immutable types:
# int
# float
# bool (True 1 and False 0): a subclass of integers
# str (string)
# tuple
# frozenset
# bytes

# the documentation doesn;t state that it should be the object's address, just that it must be
# "guranteed to be unique and constant for this object during its lifetime."

# the ID for an object may be different everytime you run the program but
# whitle the program is running, the object will have the same ID

# unless the object is destroyed and recreated then it's ID will change.

# so with a boolean, if the value changes so does the id
result = True
another_result = result
print(id(result))
print(id(another_result))

result = False 
print(id(result)) # the id changed due to a change in the variable's value

result = "Co"
print(id(result))

result += "rrect"
print(id(result)) # the id changed again due to concatenation 
