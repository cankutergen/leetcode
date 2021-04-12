class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n <= 0:
            return False
        
        num = 0
        power = 0
        
        while num <= n:
            num = 2 ** power
            if num == n:
                return True
            
            power += 1
            
        return False
