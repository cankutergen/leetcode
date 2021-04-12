class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        i = len(num1) - 1
        j = len(num2) - 1
        sum = 0
        
        k = 0
        
        while i >= 0:
            sum += (10**k) * int(num1[i])
            i -= 1
            k += 1
            
        k = 0
        while j >= 0:
            sum += (10**k) * int(num2[j])
            j -= 1
            k += 1
            
        return str(sum)
            
