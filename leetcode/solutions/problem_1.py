from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Approach 1: Below works, using 2D array, but TLE.
        Time complexity: O(n^2)

        output = []

        n = len(nums)
        for i, _ in enumerate(nums):
            for j, _ in enumerate(nums):
                if i < j:
                    sums = nums[i] + nums[j]
                    if sums == target:
                        output.append(i)
                        output.append(j)

        return output


        Approach 2: Using hashmap. Iterate through all elements
        only once to find out if there's already value that matches
        (target - val) in the hashmap.

        Time complexity: O(n)
        """

        hashmap = {}
        for idx, val in enumerate(nums):
            if val in hashmap.values():
                idx_by_existing_val = list(hashmap.values()).index(val)
                return [idx_by_existing_val, idx]
            else:
                hashmap[idx] = target - val
