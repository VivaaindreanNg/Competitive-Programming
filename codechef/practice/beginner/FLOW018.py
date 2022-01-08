class Solution:
    def solve(self, num: int) -> int:
        # Implement fibonacci with memoization
        if num <= 1:
            fib[num] = 1
        else:
            fib[num] = num * self.solve(num - 1)

        return fib[num]


s = Solution()
t = int(input())

for tc in range(t):
    fib = [i for i in range(21)]
    num = int(input())
    print(s.solve(num))
