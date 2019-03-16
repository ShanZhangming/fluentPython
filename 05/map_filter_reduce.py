def fact(i):
    return i*i

#map的替代
print(list(map(fact, range(6))))
print([fact(n) for n in range(6)])

def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)

#filter替代
print(list(filter(lambda n: n % 2, range(6))))
print(list(map(factorial, filter(lambda n: n % 2, range(6)))))
print([factorial(n) for n in range(6) if n % 2 == 1])

#reduce的替代
from functools import reduce
from operator import add
print(reduce(add, range(100)))
print(sum(range(100)))

#all
print(all([1,2,3,4,0]))

#any
print(any([1,2,3,4,0]))