def fib(n):
    if n <= 1:
        return 1
    else:
        return n * fib(n - 1)


def solve(n: int) -> int:
    result = str(fib(n))
    sum = 0
    for i in result:
        sum += int(i)

    return sum
