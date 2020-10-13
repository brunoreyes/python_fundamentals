name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
if 18 < age < 31:
    print("welcome to the 18 to 30 club holiday, {}".format(name))
else:
    print("sorry, you are not eligible to go on holiday")
#  isinstance(name,str) :