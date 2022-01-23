class Solution:
    def solve(self, n1: int, n2: int) -> int:
        if n1 > n2:
            return n1 - n2
        else:
            return n1 + n2


s = Solution()

n1 = int(input())
n2 = int(input())

ans = s.solve(n1, n2)
print(ans)
