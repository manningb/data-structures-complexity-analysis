def factorial_recursive(n=1000):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n-1)


factorial_recursive()
