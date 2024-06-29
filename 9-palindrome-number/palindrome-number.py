class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        k = 1
        x1 = x
        if x < 0:
            x = -x
            k = -1
        y = str(x)
        re = 0
        for i in range(len(y)):
            re = re +  int(y[i]) * 10**(i) 
        if re == x1:
            return True
        else:
            return False
        