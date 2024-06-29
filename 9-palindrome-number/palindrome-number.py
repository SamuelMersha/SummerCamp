class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x1 = x
        y = str(x)
        re = 0
        for i in range(len(y)):
            re = re +  int(y[i]) * 10**(i) 
        if re == x1:
            return True
        else:
            return False
        