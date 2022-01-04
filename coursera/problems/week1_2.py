def solve(nums: list) -> int:
    max_prod = 0

    for i, _ in enumerate(nums):
        for j, _ in enumerate(nums):
            if i < j:
                prod = nums[i] * nums[j]
                if prod > max_prod:
                    max_prod = prod

    return max_prod
