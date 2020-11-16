a = 2
b = 3
print("a is {}, b is {}".format(a, b))

a, b = b, a # here we switch the assignments, where a now has the value of b and vice-versa
print("a is {}, b is {}".format(a, b))

def fibonacci():
    current, previous = 0, 1
    while True:
        yield current
        current, previous = current + previous, current


fib = fibonacci()


# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))


# Creating generators
def odd_numbers():
    n = 1
    while True:
        yield n
        n += 2


def pi_series():
    odds = odd_numbers()
    approximation = 0
    while True:
        approximation += (4 / next(odds))
        yield approximation
        approximation -= (4 / next(odds))
        yield approximation


approx_pi = pi_series()

for x in range(1000000):
    print(next(approx_pi))

# the generator decides when to terminate rather than the calling function
