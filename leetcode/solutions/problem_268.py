from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        duplicate_nums = [i for i in range(n + 1)]

        for i in duplicate_nums:
            if i not in nums:
                return i
