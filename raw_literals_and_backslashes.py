a_string = "this is\na string split\t\tand tabbed"
print(a_string)

raw_string = r"this is\na string split\t\tand tabbed" #ignoring the \n, \t and any other \ character
print(raw_string)

b_string = "this is" + chr(10) + "a string split"  + chr(9) + chr(9) + "and tabbed"
print(a_string)  # char(10) = \n & char(9) = \t these are different values from windows chars(#)

backslash_string = "this is a backslash \\followed by some text"  #to show the \, use two
print(backslash_string)

error_string = r"this string ends with \\"  # if you want to show a blackslash, you must double it: \\
print(error_string)