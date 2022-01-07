class Solution:
    def solve(self, input_str: str) -> int:
        input_str_list = list(input_str)
        total = 0

        for i in input_str_list:
            if i == "4":
                total += 1

        return total


s = Solution()
t = int(input())

for i in range(t):
    print(s.solve(input()))
