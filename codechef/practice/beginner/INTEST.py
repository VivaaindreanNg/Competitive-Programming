class Solution:
    def solve(self, i: int, k: int) -> bool:
        return True if i % k == 0 else False


s = Solution()
n, k = map(int, input().split(" "))
total = 0

for _ in range(n):
    if s.solve(int(input()), k) is True:
        total += 1

print(total)
