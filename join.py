myList = ["a", "b", "c", "d"]

newString = ", ".join(myList) #.join creates a new string with ", " inserted between each item
print(newString)

letters = "abcdefghijklmnopqrstuvwxyz"
newString = ", ".join(letters) # here we can use .join to put a ", " between each letter witin a string
print(newString)

numbers = "123456789"
newString = " mississippi ".join(numbers) #you can input any type of string between each item in a string
print(newString)

# a list of dictionary items, a list b/c it's ordered
locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

#             5 forest
#    2 Hill    1 Road     3 Building
#             4 Valley

exits = [{"Q": 0}, # here we are giving the appropriate directions a user can take
         {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         {"N": 5, "Q": 0},
         {"W": 1, "Q": 0},
         {"N": 1, "W": 2, "Q": 0},
         {"W": 2, "S": 1, "Q": 0}]

loc = 1
while True: # keep looping, letting the player go to valid directions or warning them or leaving with 0
    availableExits = ", ".join(exits[loc].keys())
    # here we are joining the exits with a ', ' like so: W, E, N .. = the string
    print(locations[loc])

    if loc == 0:
        break # ending the game

    direction = input("Available exits are " + availableExits + " ").upper() #makes the exits uppercase
    print()
    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You cannot go in that direction")