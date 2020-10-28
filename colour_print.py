# Some ANSI escape sequences for colours and effects
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'
 
BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'

print(RED, "this will be in red")
print(MAGENTA, 'this will print in magenta')
print("this is now magenta because the changes we made to color will stay enabled until disabled")

def colour_print(text: str, *effects: str) -> None: #changed effect to *effects to add multiple
    """
    Print `text` usnging the ANSI sequences to change colour, etc.

    :param test: The text to print. 
    :param effects: The effect we want. One of the constants
        defuned at the start of this module.
    """
    effect_string = "".join(effects) #effects is a tuple containing # of ANSY strings
    output_string = "{0}{1}{2}".format(effect_string, text, RESET)
    print(output_string)


colour_print("Hello, Red", RED)
colour_print("Hello, Red Bold", RED, BOLD)
colour_print("Hello, Blue-reversed-underline-bold", BLUE, BOLD, UNDERLINE, REVERSE)
# test that the colur was reset
print("This should be in the default terminal colour")

#to run functions on local terminal use "python project_name.py"