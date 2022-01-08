def solve(num: int) -> int:
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return solve(num - 1) + solve(num - 2)


if __name__ == "__main__":
    num = int(input())
    print(solve(num))
