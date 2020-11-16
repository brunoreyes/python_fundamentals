# list comporehension

print(__file__)

numbers = [1, 2, 3, 4, 5, 6]

numbers = int(input("Please input a number and I'll give you it's square"))

squares = []
for number in numbers:
    squares.append(number ** 2)

index_position = numbers.index(number)
print(squares[index_position])

