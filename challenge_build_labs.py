def averaging(*numbers: int) -> int:
    '''averaging is a function that takes in an input list of numbers
    For ex: user input: 1,2,3
    :param number: the number to check.
    :returns the average: the sum divided by the length of the numbers.'''
    sum = 0
    for number in numbers:
        sum += number
    average = (sum // len(numbers))
    return average
    

print(averaging(2,3,4))