class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dict_stones = {}
        
        for jewel in jewels:
            if jewel not in dict_stones:
                dict_stones[jewel] = 1
        
        count = 0
        for stone in stones:
            if stone in dict_stones:
                count += 1
                
        return count
