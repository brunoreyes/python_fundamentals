numbers = (0, 1, 2, 3, 4, 5)

print(numbers, sep=";")
print(*numbers, sep=";")  # * unpacks a list
print(0, 1, 2, 3, 4, 5, sep=";")

def test_star(*args): #args stand for arguments
    print(args)
    for x in args:
        print(x)

test_star(0, 1, 2, 3, 4, 5)
# here "(0 to 5)"" is a tuple that prints out like:
# 0
# 1
# 2
# 3
# 4
# 5

print()
# args without the * is a tupple.
