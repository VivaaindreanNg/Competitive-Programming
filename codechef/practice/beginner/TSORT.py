from typing import List


class Solution:
    def solve(self, nums: List[int]) -> List[int]:
        return nums


s = Solution()
t = int(input())

nums = []
for tc in range(t):
    num = int(input())
    nums.append(num)

ans = s.solve(nums)
for a in ans:
    print(a)
