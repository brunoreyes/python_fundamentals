print(__file__)
numbers = [1, 2, 3, 4, 5, 6]

numbers = int(input("Please input a number and I'll give you it's square"))

squares = [number ** 2 for number in numbers]
# squares = [number ** 2 for number in range(1, 7)]
# here theres 2 list comprehensions,
# an expression: number ** 2
# followed by an iteration that's identical to a for loop

index_position = numbers.index(number)
print(squares[index_position])


text = "what have the romans ever done for us"

capitals = [char.upper() for char in text]
# list comprehensions are like multiple functions
# on one line

print(capitals)

words = [word.upper() for word in text.split(' ')]
print(words)

lc_words = text.split(' ')
print(lc_words)

lc_words = [word for word in text.split(' ')]
print(lc_words)
