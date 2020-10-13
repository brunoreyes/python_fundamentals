day = "Friday"
temperature = 30
raining = True

if (day == "Saturday" and temperature > 27) or not raining:
    print("go swimming")
else:
    print("Learn Python")

#The following are considered false:
#constants defined to be false: None and False
#zero of any numeric time: 0, 0,0, 0j, Decimal(0), Fraction(0,1)
#empyty sequences and collections: '', (),[],{},set(),range(0)
# to summarize any 0's, empty arrays: {} or objects: [], false or none, are considered False

if 0: # so 0 is evaluated to false when represented in a boolean expression like so
    print("True")
else:  #since 0 isn't true it will default to this else statement, printing out false
    print("False")

name = input("Please enter your name: ") #if you input any non-empty string, "Hello, name" appears
# if name: this isn't so obvious to mean if string is empty
if name !="": #This is more obvious, write code like so
    print("Hello, {}".format(name)) #when you just press enter without adding a string, it goes to else
else:
    print("are you the man with no name?")