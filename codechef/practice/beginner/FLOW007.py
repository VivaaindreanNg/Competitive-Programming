class Solution:
    def solve(self, num: str) -> int:
        num_list = list(num)
        n = len(num_list)
        mid = n // 2

        for i in range(mid):
            num_list[i], num_list[n - 1 - i] = num_list[n - 1 - i], num_list[i]

        return int("".join(num_list))


s = Solution()
t = int(input())

for tc in range(t):
    print(s.solve(input()))
