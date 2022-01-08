class Solution:
    def solve(self, num: int) -> int:
        if num <= 0:
            return 1
        else:
            return num * self.solve(num - 1)


s = Solution()
t = int(input())

for tc in range(t):
    num = int(input())
    print(s.solve(num))
