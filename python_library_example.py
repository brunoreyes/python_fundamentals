import shelve # hover over shelve and hold command on mac to read more about shelve

print(dir())  # Prints all the properties and methods: ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
# Anything starting with an underscrore (_) shouldn't be changed & 2 underscores (__) shouldn't be changed at all

# print(dir(__builtins__)) #hard to read
for function in dir(__builtins__):
    print(function)


print(dir(shelve))

for obj in dir(shelve.Shelf):  #gives us the full list of shelve's builtin functions
    if obj[0] != '_':
        print(obj)

help(shelve) #we can pull up help docs on most things using help() after we've installed something
