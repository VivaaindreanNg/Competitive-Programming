from typing import Union


class Solution:
    def solve(self, num: int) -> Union[str, int]:
        if num < 10:
            return "Thanks for helping Chef!"
        else:
            return -1


s = Solution()
t = int(input())
output = []

for tc in range(t):
    num = int(input())
    ans = str(s.solve(num))
    output.append(ans)

print(*output, sep="\n")
