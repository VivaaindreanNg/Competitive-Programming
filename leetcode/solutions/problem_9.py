class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            x_str = str(x)
            mid = len(x_str) // 2
            
            first_half = x_str[:mid]
            second_half = reversed(x_str[mid:])
            
            for i, j in zip(first_half, second_half):
                if i != j:
                    return False
            return True