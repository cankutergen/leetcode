
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = {}

        for char in tasks:
            if char not in task_counts:
                task_counts[char] = 1
            else:
                task_counts[char] += 1
                
        char_list = list(task_counts.values())
        char_list.sort(reverse = True)
        max_val = char_list[0]
        
        i = 0
        counter = 0
        while i < len(char_list) and char_list[i] == max_val:
            counter += 1
            i += 1
        
        ret = (max_val - 1) * (n + 1) + counter 
        return max(ret, len(tasks))
        
        
        
        
