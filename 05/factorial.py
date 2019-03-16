
def factorial(n):
    '''
    return n
    '''
    return 1 if n <= 1 else  n*factorial(n-1)

fact = factorial
print(list(map(fact, range(10))))