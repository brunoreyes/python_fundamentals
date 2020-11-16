# from __future__ import division

# def average(first_value, *args, last_value):  # here we are inputting muptiple arguments or '*args'
#     print("args is {}:".format(args))
#     print("*args is", *args)
#     mean = 0
#     for arg in args:
#         mean += arg
#     return mean / len(args)
    
# print(average(1, 2, 3, 4))


# def build_tuple(*args):
#     return args

# message_tuple = build_tuple("hello", "planet", "earth", "take", "me", "to", "your", "leader")
# print(type(message_tuple))
# print(message_tuple)

# number_tuple = build_tuple(1,2,3,4,5,6)
# print(type(number_tuple))
# print(number_tuple)

# def print_backwards(*args, end=' ', **kwargs): 
# # def print_backwards(*args, end=' ', **kwargs): # ** allows us to pass any number of keyword arguments
#     print(kwargs)
#     kwargs.pop('end', None)
#     for word in args[::-1]:
#         print(word[::-1], end=' ', **kwargs)

def print_backwards(*args, **kwargs): 
# def print_backwards(*args, end=' ', **kwargs): # ** allows us to pass any number of keyword arguments
    end_character = kwargs.pop('end', '\n')
    sep_character = kwargs.pop('sep',' ')
    for word in args[::-1]: # change the range
        print(word[::-1], end=sep_character, **kwargs) 
    print(args[0][::-1], end=end_character, **kwargs)  # and print first word seperately
    # print(end=end_character) # rendering this line unnecessary

def backwards_print(*args, **kwargs):
    sep_character = kwargs.pop('sep', ' ')
    print(sep_character.join(word[::-1] for word in args[::-1]), **kwargs)

with open("backwards.txt", 'w') as backwards:
    print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", file=backwards, end='\n')
    print('Another String')
    
print()
print("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='', sep='\n**\n')
print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='\n', sep='\n**\n')
print("=" * 10)

    

