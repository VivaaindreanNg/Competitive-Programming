
def check_palin(input_str: str) -> bool:
    mid = len(input_str)//2

    first = input_str[:mid]
    second = reversed(input_str[mid:])

    for i, j in zip(first, second):
        if i != j:
            return False
    
    return True


def solve(n: int) -> int:
    num = 10 ** n
    greatest_palin = 0
    
    for i in range(num):
        for j in range(num):
            prod = i * j 
            if check_palin(str(prod)):
                if prod > greatest_palin:
                    greatest_palin = prod

    return greatest_palin