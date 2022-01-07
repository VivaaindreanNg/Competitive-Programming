class Solution:
    def solve(self, a: int, b: int) -> int:
        return a + b


s = Solution()
# Read the number of test cases.
t = int(input())
for tc in range(t):
    a, b = map(int, input().split(" "))
    print(s.solve(a, b))
