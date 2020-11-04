def python_food():
    width = 80
    text = "spam and eggs"
    left_margin = (width - len(text)) // 2  # integer divide by 2; here we are creating an indent
    print(" " * left_margin,text)
    

# all python functions return something, if nothing is specified, it will return none
# functions make code managable
print(python_food())  #calling the function and printing the output of the function

# def center_text(*args, sep=' ', end='\n', file=None, flush=False):  # parameters refer to the type of input coming in
#     # text=str(text) # this is a way to get around a user inputing an int
#     text = ""
#     for arg in args:
#         text += str(arg) + sep
#     left_margin = (80 - len(text)) // 2
#     print(" " * left_margin, text, end=end, file=file, flush=flush)

def center_text(*args, sep=' '):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    return " " * left_margin + text

# with open("centered", mode='w') as centered_file: #write 

#     # signatures are ways of referring to a set of parameters in a function definition,
#     # two functions that take the same parameter have the same signature
#     # calling center_text with the argument "spam and eggs" just like in JS
#     center_text("spam and eggs",file=centered_file) # "spam and eggs" is the argument, while (text) is the parameter
#     center_text("spam, spam and eggs",file=centered_file)
#     center_text("spam, spam, spam and eggs",file=centered_file)

#     # center_text(12) # inputting an int argument within a function that only accepts text parameter
#     # results in an error

#     center_text("first","second",3,4,"spam",sep=":", file=centered_file)

# call the function
# s1 = centre_text("spam and eggs")
# print(s1)
# s2 = centre_text("spam, spam and eggs")
# print(s2)
# s3 = centre_text(12)
# print(s3)
# s4 = centre_text("spam, spam, spam and spam")
# print(s4)
# s5 = centre_text("first", "second", 3, 4, "spam", sep=":")
# print(s5)

with open("menu", "w") as menu: # Creating and Writing all of the arguments below into the file 'menu'
    s1 = center_text("spam and eggs")
    print(s1, file=menu)
    s2 = center_text("spam, spam and eggs") #printing the text, centered within the file 'menu'
    print(s2, file=menu)
    print(center_text(12), file=menu)
    print(center_text("spam, spam, spam and spam"), file=menu)
    s5 = center_text("first", "second", 3, 4, "spam", sep=":")
    print(s5, file=menu)