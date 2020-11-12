def factorial(n):
    #  n! can also be defined as  n * (n-1)!
    if n <= 1:
        return 1
    else:
        print( n / 0)
        return n * factorial(n - 1)

# hanlding 2 errors instead of crashing the program
try:
    print(factorial(900))
except (RecursionError, OverflowError, MemoryError):
    print("This program calculate factories that large")
except ZeroDivisionError:
    print("What are doing dividing by zero???")

print("Programming terminating")

# OverflowError, is when there is an incredibly large number to handle