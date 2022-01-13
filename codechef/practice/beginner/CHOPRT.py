class Solution:
    def solve(self, a: int, b: int) -> str:
        if a < b:
            return "<"
        elif a > b:
            return ">"
        else:
            return "="


s = Solution()
t = int(input())
answers = []

for tc in range(t):
    a, b = map(int, input().split(" "))
    answer = s.solve(a, b)
    answers.append(answer)

print(*answers, sep="\n")
