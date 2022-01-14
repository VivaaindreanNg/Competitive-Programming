class Solution:
    def solve(self, num: int) -> int:
        if num % 4 == 0:
            return num + 1
        else:
            return num - 1


s = Solution()
num = int(input())
print(s.solve(num))
