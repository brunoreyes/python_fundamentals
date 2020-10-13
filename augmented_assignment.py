# Augemented assignment sounds fancy, but it's just a shorthand way of assignming values to a variable.
# Fancy definition: the combination, in a single statement, of a binary operation and assignment statement

#Augmented assignment is more efficient, instead of creating a new variable,
#It binds the new variable to the result of performing the calculation, and destroy the original variable.
# guesses = guesses + 1   inefficient way, creating a new variable
# guesses += 1            efficient Augmented Assignment way

x = 23

x += 1
print(x) #24

x -= 4
print(x) #20

x *= 5
print(x) #100

x //= 4
print(x) #25 dividing an int

x /= 5
print(x) #5.0  converting an int to float 

x **= 2  # 25.0 to the power of
print(x)

x %= 5 # 0.0 25 is exactly divisible by 5 with no remiander left
print(x)

greeting = "Good "

greeting += "morning" 
print(greeting) #output: Good morning

greeting *= 5
print(greeting)  #output: Good morningGood morningGood morningGood morningGood morning
# all binary operators found on pg 6 in docs for python 3

#Use a for loop & augmented assignment to give answer the result of multiplying number by multiplier
number = 5
multiplier = 8
answer = 0
 
# add your loop after this comment
for i in range(multiplier): #here we are getting adding 5, 1-8 times, getting 40
    answer += number #here were using augmented assignment to add the number to the aswer
 
print(answer) #after 8 5's have been added, printing answer will print: 40
