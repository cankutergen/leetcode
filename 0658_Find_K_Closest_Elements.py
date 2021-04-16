class Solution:
    def findClosestElements(self, arr, k: int, x: int):
       dict = {}
    
       for i, num in enumerate(arr):
           dist = abs(num - x)
           if i not in dict:
               dict[i] = (dist, num)

       sorted_dict = sorted(dict.values(), key = lambda x: x[0])
       res = []
       for key in sorted_dict:
           if len(res) == k: break
           res.append(key[1])

       return sorted(res)
