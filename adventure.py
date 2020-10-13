available_exits = ["north", "south", "east", "west"]

chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: ")
    if chosen_exit.casefold() == "quit": #this makes any input lowercase
        print("Game over")
        break

print("aren't you glad you got out of there")

#in a while loop you don;t need to know how many times you will exucute a loop
#in a for loop, it will only execute for how many items there is in a sequence


