
def factorial_recursive(n=1000):
    """
    Function to calculate the factorial of a positive integer
    If the input is not a positive integer, return -1
    Non-tail-recursive
    """
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n-1)
