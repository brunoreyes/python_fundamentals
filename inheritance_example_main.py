# from getters_and_setters_player import Player
# tim = Player("tim")
from inheritance_example_enemy import Enemy, Troll, Vampire, VampireKing

dracula = VampireKing("Dracula")
print(dracula)
dracula.take_damage(12)
print(dracula)

a = 3
b = "tim"
c = 1, 2, 3
print(a) # a is an int, and we can subtract two it's and workout the difference
print(b) # b is a string and cannot be subtracted in python, different type of object that shares print trait
print(c)
# a and b are printable objects, objects are polymorphs b/c they have different forms
# objects can be ints, strings, list, etc. Poly: many, Morphe: from


# random_monster = Enemy("Basic enemy", 12, 1)
# print(random_monster)

# random_monster.take_damage(4)
# print(random_monster)

# random_monster.take_damage(8)
# print(random_monster)

# random_monster.take_damage(9)
# print(random_monster)

# ugly_troll = Troll("Pug")
# print("Ugly Troll - {}".format(ugly_troll))

# brother = Troll("Urg")  # when values aren't specified, the defualt values kick in
# print(brother)
()
# another_troll = Troll("Urg")
# # another_troll = Troll("Urg", 18,1) # same name, different arguments
# print("Another Troll - {}".format(another_troll), end="")

# ugly_troll.grunt()
# another_troll.grunt()
# brother.grunt()

# red_vampire = Vampire("Red")
# print(red_vampire)

# red_vampire.take_damage(2)
# print(red_vampire)

# another_troll.take_damage(3)
# print(another_troll)

# red_vampire.charisma()

# while red_vampire._alive:  # a while loop that gives red vampire damage until it dies or alive = False.
#     red_vampire.take_damage(1)
        

        #an overriding method is one that replaces another one, done by naming the method the same


# Java's a statically typed language, meaning that the type of everythin is checked when the program's compiled.
# If you try to pass a string to a method that expects an int, then the program won't compile.

# With Python, the type of something is only of interest when it's used.

# Overloading isn't possible in Python, but it is creating different versions of the methods that take in
# different parameters, and the compiler decides which ones to use based on the number and type of parameters
# passed to it.

# Python doesn't check the type of variables when it compiles the code.

# In Java, the compilier calls a certain version that accepts the type of parameter

# valueOf deligates the type to the class, not needing to no what class it's dealing with.

# In Java, you have to specify exactly what type of object you'll be dealing with - otherwise the
# code will not compile. Meaning every method knows exactly what it can do with each argument

# Python on the otherhand focuses not on what type something is but how it behaves and what it does.

# Inheritance isn't the only way to implement polymorphism

# the print function in Python doesn't have to cater for the possibility that the thing it's being
# asked to print may not have a suitable method to return a string. Every class automatically inherits the
# method from the object base class. 
