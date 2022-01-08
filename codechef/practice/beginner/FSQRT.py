class Solution:
    def solve(self, num: int) -> int:
        return int(num ** 0.5)


s = Solution()
t = int(input())

for tc in range(t):
    num = int(input())
    print(s.solve(num))
