def fibonacci_series(n: int) -> list:
    x, y = -1, 1
    fibo = []
    for i in range(n):
        y, x = abs(x), abs(x + y)
        fibo.append(x)
    return fibo


def fibonacci_series_generator(n: int):
    x, y = -1, 1
    for i in range(n):
        y, x = abs(x), abs(x + y)
        yield x


def get_nth_fibonacci_number_iterative(n: int) -> int:
    x, y = -1, 1
    for i in range(n):
        y, x = abs(x), abs(x + y)
    return x


def get_nth_fibonacci_number_recursive(n: int) -> int:
    if n == 0:
        return -1
    if n == 1:
        return 0
    return abs(get_nth_fibonacci_number_recursive(n - 2)) + abs(get_nth_fibonacci_number_recursive(n-1))


def is_a_num_in_fibonacci_series(n: int) -> bool:
    x = 0
    while x < n:
        fib_x = get_nth_fibonacci_number_iterative(x)
        if fib_x == n:
            return True
        x += 1
    return False


if __name__ == "__main__":
    print(fibonacci_series(10))
    print([num for num in fibonacci_series_generator(10)])
    print(get_nth_fibonacci_number_iterative(10))
    print(get_nth_fibonacci_number_recursive(10))
    print(is_a_num_in_fibonacci_series(34))
    print(is_a_num_in_fibonacci_series(35))