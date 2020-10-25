def banner_text(text: str = " ", screen_width: int = 80) -> None:  #screen-width, the second parameter is
    # set to the default value of 80, but can be changed when entering another value
    # screen_width = 50, the first parameter is set to default value of " "
    
    # banner_text's docstring format
    """ Print a string centered, with ** either side.
  
    :param text: The string to print.
        An asterisk (*) will result in a row of asterisks.
        The default will print a blank line, with a ** border at
        the left and right edges.
    :param screen_width: The overall width to print within
        (including the 4 spaces for the ** either side).
    :raises ValueError: if the supplied string is too long to fit.
    """

    if len(text) > screen_width - 4:
        # raising an exception by using raise TypeOfError(),
        # TypeError() function excepts integer but passed string
        # ValueError() function excepts right type but wrong value
        raise ValueError("String {0} is larger than specified width {1}".format(text, screen_width))
        # specifically tells user the string and width lengths
        # print("Eek!!")
        # print("THE TEXT IS TOO LONG TO FIT IN THIS SPECIFIED WIDTH")
        
    if text == "*":
        print("*" * screen_width)
    else:
        output_string = "**{0}**".format(text.center(screen_width - 4))
        print(output_string)


#the function banner_text() does not return a function, instead it preforms an action
# as hinted by not explicitely having a return statement within the function

banner_text("*",60) # Recall when the function recieves an asterisk, it prints a row of asterisks
banner_text("Always look on the bright side of life...",60)
banner_text("If life seems jolly rotten,",60)
banner_text("There's something you've forgotten!",60)
banner_text("And that's to laugh and smile and dance and sing,",60)
banner_text(" ") #This is a blank line that is centered
banner_text("When you're feeling in the dumps,",60)
banner_text("Don't be silly chumps,",60)
banner_text("Just purse your lips and whistle - that's the thing!",60)
banner_text("And... always look on the bright side of life...",60)
banner_text("*",60)

result = banner_text("Nothing is returned",60)
print(result)  # Here we will show that result prints out none automatically

numbers = [4, 2, 7, 5, 8, 3, 9, 6, 1]
print(numbers.sort()) #here the function also preforms an action instead of returning a result

#SUMMARY
# We learned how to define parameters, and passing corresponding arguments to
# call out functions.

# Positional arguments are used to provide a value for the parameter in the same
# position like cat_amount in: def cat_hotel(cat_amount=0)

# keyword parameters can be used by speciying the parameter name when
# you pass an argument like dog_type in the following: def dog(dog_type):