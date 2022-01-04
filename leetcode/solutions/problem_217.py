from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Approach 1: Using 2D table for comparison.
        Results: TLE (Time Limit Exceeded)
        
        for i, _ in enumerate(nums):
            for j, _ in enumerate(nums):
                if i < j:
                    if nums[i] == nums[j]:
                        return True
        return False
        ---------------------------------------------------


        Approach 2: Use the input list to form key in hashmap.
        If the length of keys created from hashmap is lesser than
        length of input list, then return True since there's duplication
        when inserting existing key in hashmap.
        """
        n = len(nums)
        hashmap = {}

        for i in nums:
            hashmap[i] = i

        check = True if len(hashmap.keys()) < n else False
        return check
