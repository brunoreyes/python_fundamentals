#function annotations and type hints
#The Fibonacci numbers, often called the Fibonacci sequence is such that each number
# is the sum of the two preceding ones, starting from 0 and 1.
# such as 0,1,1,2,3,5,8,13,21,34,55,89,144...



def fibonacci(n):
    """Return the 'n'th Fibonacci number, for positive `n`."""
    if 0 <= n <= 1:
      return n

    n_minus1, n_minus2 = 1, 0

    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result  #adding the 1st and the 2nd number become the 1st number
    
    return result

for i in range(36):
    print(i, fibonacci(i))
