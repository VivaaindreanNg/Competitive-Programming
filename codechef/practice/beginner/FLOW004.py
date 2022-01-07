class Solution:
    def solve(self, input_str: str) -> int:
        input_str_list = list(input_str)
        n = len(input_str_list)

        return int(input_str_list[0]) + int(input_str_list[n - 1])


s = Solution()
t = int(input())

for i in range(t):
    print(s.solve(input()))
