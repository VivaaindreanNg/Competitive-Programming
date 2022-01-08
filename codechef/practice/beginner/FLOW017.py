from typing import List


class Solution:
    def solve(self, nums: List[int]) -> int:
        if nums[0] > nums[1]:
            nums[0], nums[1] = nums[1], nums[0]

        if nums[1] > nums[2]:
            nums[1], nums[2] = nums[2], nums[1]

        if nums[0] > nums[1]:
            nums[0], nums[1] = nums[1], nums[0]

        return nums[1]


s = Solution()
t = int(input())

for tc in range(t):
    a, b, c = map(int, input().split(" "))
    print(s.solve([a, b, c]))
