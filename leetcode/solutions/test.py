from typing import List


def get_fib_list() -> List[int]:
    fib = [0, 1]
    MAX_N = 10000

    for n in range(2, MAX_N + 1):
        val = fib[n - 1] + fib[n - 2]
        fib.append(val)

    return fib


def solve(num: int, fibs: List[int]) -> int:
    for idx, val in enumerate(fibs):
        if val > 0 and val % num == 0:
            return idx


print("input data:")
input()
nums = map(int, input().split(" "))
nums = list(nums)
ans = ""
fibs = get_fib_list()

for num in nums:
    ans += f"{solve(num, fibs)} "

print()
print(ans)
