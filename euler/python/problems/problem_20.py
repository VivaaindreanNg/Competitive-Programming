

def fib(n):
    if n <= 1:
        return 1
    else:
        return n * fib(n-1)

def solve(n: int) -> int:
    """
    Pseudocode:
    ```
    fib(n):
        if n <= 1:
            return 1
        else:
            return n * fib(n-1)

    result = str(fib(n))
    x := length(result)
    sum := 0

    for i <- 0 to x-1:
        sum := sum + int(result[i])
    
    return sum
    ```
    """

    result = str(fib(n))
    sum = 0
    for i in result:
        sum += int(i)

    return sum