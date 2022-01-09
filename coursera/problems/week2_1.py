def solve1(num: int) -> int:
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return solve1(num - 1) + solve1(num - 2)


def solve2(num: int) -> int:
    """With memoization."""
    fib = [0, 1]

    if num == 0:
        return fib[0]
    elif num == 1:
        return fib[1]
    else:
        for n in range(2, num + 1):
            val = fib[n - 1] + fib[n - 2]
            fib.append(val)

        return fib[num]
