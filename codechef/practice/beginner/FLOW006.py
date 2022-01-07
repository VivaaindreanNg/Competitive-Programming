class Solution:
    def solve(self, num: str) -> str:
        num_list = list(num)
        num_list_int = [int(j) for j in num_list]
        return f"{sum(num_list_int)}"


s = Solution()
t = int(input())

for i in range(t):
    print(s.solve(input()))
