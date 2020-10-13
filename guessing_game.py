answer = 5
print("Please guess number between 1 and 10: ")
guess = int(input())

if guess == answer:
    print("You guessed it right the first time!")
else:
    if guess < answer:
        print("Please guess higher")
    else:  #guess must be greater than answer
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you have guessed it")
    else:
        print("Sorry, you have not guessed correctly")


if guess != answer: #here is the guess isn't == answer, then it will run children, otherwise run else
    if guess < answer:
        print("Please guess higher")
    else:  #guess must be greater than answer
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you have guessed it")
    else:
        print("Sorry, you have not guessed correctly")
else: print("You got it right the first time")

# if guess < answer:
#     print("Please guess higher")
#     guess = int(input()) # here we allow another guess if the guess was lower than 5
#     if guess == answer: # a single equal is for binding a variable to a value, a double equal is to compare
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input()) # here we allow another guess if the guess was higher than 5
#     if guess == answer:
#         print("Well done you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else: #Here else picks up everything else, which is guess = answer
#     print("You got it right the first time")  #else box will be evaluated when nothing else matches
    
#Assign the name of two trees to to variables called tree1 and tree2
#if the values are the same, print that they are,
#if not print they are not

tree1 = "Bark"
tree2 = "Oak"
# add the code to compare the trees
# tree1 = input("Please write the name of tree 1:  ")
# tree2 = input("Please write the name of tree 2:  ") 
if tree1 == tree2: #Remember for comparing two values, use "=="
    print("The trees are the same")
else:
    print("The trees are different")


x = 5
y = 7

if x > y:
    print("x is greater than y")
elif x < y:
    print("x is smaller than y")
else:
    print("x equals y")

