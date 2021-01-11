# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# This function returns the Nth number in the fibonacci sequence.
# https://en.wikipedia.org/wiki/Fibonacci_number
# For this function, the first two fibonacci numbers are 1 and 1

from functools import lru_cache
@lru_cache

def fib(n):
    if type(n) != int:
        raise TypeError('Value must be an integer')
    if n < 1:
        return 0
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fib(n -1) + fib(n - 2)
    pass

# print(fib(-1))
# => 0
# print(fib(0))
# => 0
# print(fib(1))
# => 1
# print(fib(2))
# => 1
print(fib(7))
# => 13