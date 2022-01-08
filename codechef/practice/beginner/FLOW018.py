class Solution:
    def solve(self, num: int) -> int:
        # Implement factorial with memoization
        if num <= 1:
            factorial[num] = 1
        else:
            factorial[num] = num * self.solve(num - 1)

        return factorial[num]


s = Solution()
t = int(input())

for tc in range(t):
    factorial = [i for i in range(21)]
    num = int(input())
    print(s.solve(num))
