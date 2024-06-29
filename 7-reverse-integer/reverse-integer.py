class Solution:
    def reverse(self, x: int) -> int: 
        k = 1
        if x < 0:
            x = -x
            k = -1
        y = str(x)
        re = 0
        for i in range(len(y)):
            re = re +  int(y[i]) * 10**(i) 
        if re > -(2**31) and re < 2**31 - 1:
            return k*re
        else:
            return 0