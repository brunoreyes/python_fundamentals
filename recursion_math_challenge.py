import sys

def getint(prompt):  # getting int from input instead of a string from input
    while True:
        try:
            number = int(input(prompt))
            return number
        except EOFError: # an instance of exception
            sys.exit(1)
        except:  # Exception #ValueError: # not all exceptions have to be derived from exception
            # for instance 'except:' above takes on all exceptions.
            print("Invalid number entered, please try again")
        finally: # finally will always execute even if there is an exception
            print("The final clause always executes") # control + d exits the python session

first_number = getint('input first number ')
second_number = getint('input second number ')
# divided number has to be inputted within the format rather than here

try:
    print("{} divided by {} is {}".format(first_number, second_number, first_number / second_number))
except ZeroDivisionError: # exceptions are objects and must be derived from the base exception class or subclass
    print("What are doing dividing by zero???") 
    sys.exit(2)
finally: # else:  else is intended to not accidentally catch an exception that wasn't raised by the code we're trying to protect. 
    print("Division preformed successfully")