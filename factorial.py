import operator
import functools
import math


def factorial_recursive(n: int) -> int:
    if n <= 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


def factorial_iterative(n: int) -> int:
    factorial = 1
    while n > 1:
        factorial *= n
        n -= 1
    return factorial


def factorial_reduce(n: int) -> int:
    return functools.reduce(operator.mul, range(1, n + 1), 1)


def factorial_math(n: int) -> int:
    return math.factorial(n)


if __name__ == "__main__":
    print(factorial_iterative(100))
    print(factorial_recursive(100))
    print(factorial_reduce(100))
    print(factorial_math(100))
