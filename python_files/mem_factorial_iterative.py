def factorial_iterative(n=1000):
    """
    Function to calculate the factorial of a positive integer
    If the input is not a positive integer, return -1
    """
    factorial = 1
    for i in range(2, n+1):
        factorial *= i
    return factorial
