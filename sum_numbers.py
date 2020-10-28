def sum_numbers(*args: float) -> float: #we want to use floats to get exact numbers like 8.8
    '''
    must takes in variable arguments and add them together
    :param test: variable number/s. 
    :param effects: the sum of all the variable numbers
        defuned at the start of this module.'''
    result = 0
    for arg in args:
        result += arg
    return result
    
    print(sum_numbers(1,2,3))
    print(sum_numbers(1.2, 0, 1))
    
