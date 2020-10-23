# The term function signature maens the definition of a function.
# This includes the functions name and the parameter that it defines

# for ex: print(*object, sep='', end='\n', file-sys.stdout, flush= False)

# The function name is print

# The name's follwed by parentheses, with parameters inside the parentheses.
# Not all functions have parameters but they are needed when defining and calling a function

# an asterisk like * before objects, this means you can provide zero or more values.
# which we've only provided one value or none when we want to print a blank line.

#em: sep='' is a named argument and keyword argument,

name = "Tim"
age = 10

print(name,age,"Python", 2020)
print(name, age, "Python", 2020, sep=", ")  #sep = seperator which adds seperators for each value with a ', '
#sep won;t be printed if only just one value is printed
#end = " " puts the items on one line each if seperated like with the eggs, bacon, not spam example
