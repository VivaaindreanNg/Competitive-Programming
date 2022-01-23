from typing import List


class Solution:
    def solve(self, angles: List[int]) -> str:
        return "YES" if sum(angles) == 180 else "NO"


s = Solution()
t = int(input())
answers = []

for tc in range(t):
    angles = list(map(int, input().split(" ")))
    answer = s.solve(angles)
    answers.append(answer)

print(*answers, sep="\n")
