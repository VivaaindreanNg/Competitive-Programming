from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Approach 1: Create a duplicated_nums that includes
        n, and then loop through the original array by
        doing comparison/checking.


        n = len(nums)
        duplicate_nums = [i for i in range(n + 1)]

        for i in duplicate_nums:
            if i not in nums:
                return i



        Approach 2: Find the sum of duplicated_nums that
        includes n, and subtract it with sum of original
        array. Return that result.
        """
        n = len(nums)
        duplicated_nums = [i for i in range(n + 1)]

        return sum(duplicated_nums) - sum(nums)
