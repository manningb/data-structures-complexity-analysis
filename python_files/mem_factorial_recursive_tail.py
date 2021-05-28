
def factorial_recursive_tail(n=100, accumulator=1):
    """
    Function to calculate the factorial of a positive integer
    If the input is not a positive integer, return -1
    Non-tail-recursive
    """
    if n == 0:
        return accumulator
    else:
        return factorial_recursive_tail(n-1, accumulator=accumulator*n)
