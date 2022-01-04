from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
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
