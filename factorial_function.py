def factorial(number: int) -> int:
    '''factorial is a function that takes a user's input
    as a number and return the input's factorial
    
    For ex: user input: 4, factorial is 1*2*3*4
    :param number: the number to check.
    :return: the factorial of the inputted number and 
    if the number happens to be 0, then return 1
    Valid for `n` in the range 0 to 998 (inclusive).
    Larger values of `n` will cause a RecursionError.'''
    if  -1 < number <= 1:
        return 1
    elif number < 0:
        return input("Please input a positive number")
    else:
        return number * factorial(number - 1)
 
 
for i in range(36):
    print(i, factorial(i))
  
