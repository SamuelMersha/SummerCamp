class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        y = str(x)
        y1 = y[::-1]
        if y == y1:
            return True
        else:
            return False
        