class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        odd = []
        even = []
        res = []
        
        for num in A:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
                
        odd.sort()
        even.sort()
        
        for num in even:
            res.append(num)
            
        for num in odd:
            res.append(num)
            
        return res
