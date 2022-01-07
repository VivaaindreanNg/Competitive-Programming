class Solution:
    def solve(self, a: int, b: int) -> int:
        return a % b


s = Solution()
t = int(input())

for i in range(t):
    a, b = map(int, input().split(" "))
    print(s.solve(a, b))
