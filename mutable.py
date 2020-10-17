# For more mutable sequences check out python 3 docs for mutable sequences

# A mutable object is one whose value can be changed
#Python has the floowing mutable objects built in:
# list
# dict
# set
# bytearray


# we can change the value of mutable objects, w/o destroying and recreating.

shopping_list = ['milk', 'orange juice', 'chicken']
another_list = shopping_list
print(id(shopping_list))
print(id(another_list))
# here both ids are the same, nothing has been changed

shopping_list += ['cookies']
print(shopping_list)
print(id(shopping_list))  #even w/ concatenation, the id remains unchanged, with this mutable object
print(id(another_list))  #so far there is only one list, b/c both names have been bounded to one list
a = b = c = d = e = f = another_list #now we have 8 references to the same 1 list
print(a)
print("Adding cream")
b.append("cream")  #.append adds cream to the end of the list
print(c)
print(d)  # now we got cream in the list no matter from where we refer to it
print("mississipi".count("iss"))  #prints out 2

# a method is the same as a function, except for the fact that it's bound to an object.
# methods are usually introduced using dot notation like list.length

#list.append(x)
# list is the onject we are calling the method on
# .append is the method "append" we call
# x is the argument for the method. The value of x will be appended to the list