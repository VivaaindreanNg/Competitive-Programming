from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        out = []
        sums = 0

        for i in nums:
            sums += i
            out.append(sums)
        return out
