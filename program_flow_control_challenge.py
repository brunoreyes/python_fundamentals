# Write a program to print a number of options and allow the user to select an option from the list.
#The options should be numbers 1 to 9, but you can use less than 9 options with a min of 4 options

#Please choose your option from the list below:
# 1. Learn Python
# 2. Learn Java
# 3. Go Swimming
# 4. Have Dinner
# 5. Go to bed
# 0. Exit

#The program should continue looping, allowing the user to chose one of the options each time
#The loop should only terminate when the user chooses 0.
#If the user makes a valid choice, the program should print a short message.
#The message should include the value that they typed
# only the number typed should change for the message
# if they input a number that isn;t avaiable, let them know and also print the menu again
#Make sure not to reduplicate the lines
choice = "-"
while choice != "0":
    if choice in "12345": #here we check if choice is any number between 1 to 5
        print("You chose {}".format(choice))
    else:
        print("Please choose your option from the list below:")
        print("1:\tLearn Python")  #\t is to tab
        print("2:\tLearn Java")
        print("3:\tGo Swimming")
        print("4:\tHave Dinner")
        print("5:\tGo to bed")
        print("0:\tExit")

    choice = input()


