# See also: https://leetcode.com/problems/coin-change/


def solve(num: int, counter: int) -> int:
    """
    Output the minimum number of coins
    with denominations 1, 5, 10 that changes num.
    """
    denom = reversed([1, 5, 10])

    if num > 0:
        for i in denom:
            if i <= num:
                num -= i
                break
        counter += 1
        return solve(num, counter)
    else:
        return counter
