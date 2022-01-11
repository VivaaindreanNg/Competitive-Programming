from typing import List, Tuple


class Solution:
    def solve(self, scores1: List[int], scores2: List[int]) -> Tuple[int, int]:
        sum1, sum2 = 0, 0
        list1, list2 = [], []

        for i, j in zip(scores1, scores2):
            sum1 += i
            sum2 += j

            list1.append(sum1)
            list2.append(sum2)

        lead_score = 0
        winner = None
        for cumsum1, cumsum2 in zip(list1, list2):
            # Compare cumulative scores
            if cumsum1 > cumsum2:
                if (cumsum1 - cumsum2) > lead_score:
                    lead_score = cumsum1 - cumsum2
                    winner = 1
            else:
                if (cumsum2 - cumsum1) > lead_score:
                    lead_score = cumsum2 - cumsum1
                    winner = 2

        return (winner, lead_score)


s = Solution()
t = int(input())

scores1, scores2 = [], []

for _ in range(t):
    score1, score2 = map(int, input().split(" "))
    scores1.append(score1)
    scores2.append(score2)

winner, lead = s.solve(scores1, scores2)
print(winner, lead)
