class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,      "f":4,"n":9,"F":40,"N":90,"A":400,"B":900,'O':0}
        num = 0
        i = 0
        while(i<len(s)):
            if i < len(s)-1:    
                if s[i] == 'I' and s[i+1] == "V":
                    num += 4
                    i+= 2
                    continue
                elif s[i] == 'I' and s[i+1] == "X":
                    num += 9
                    i += 2
                    continue
                elif s[i] == 'X' and s[i+1] == "L":
                    num += 40
                    i += 2
                    continue
                elif s[i] == 'X' and s[i+1] == "C":
                    num += 90
                    i += 2
                    continue
                elif s[i] == 'C' and s[i+1] == "D":
                    num += 400
                    i += 2
                    continue
                elif s[i] == 'C' and s[i+1] == "M":
                    num += 900
                    i += 2
                    continue
                elif s[i] in roman:
                    num += int(roman.get(s[i]))
                    i +=1
                    continue    
            else:
                if s[i] in roman:
                    num += int(roman.get(s[i]))  
                    i +=1   
        return num