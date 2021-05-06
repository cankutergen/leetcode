class Item:
    def __init__(self, value, label):
        self.value = value
        self.label = label

class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        items = []
        item_dict = {}
        
        for i in range(len(labels)):
            items.append(Item(values[i], labels[i]))
            item_dict[labels[i]] = 0
            
        items.sort(key = lambda x: x.value, reverse = True)

        numbers = 0
        total = 0
        for i in range(len(values)):
            val = items[i].value
            used_times = item_dict[items[i].label]
                
            if used_times < use_limit:
                total += val
                item_dict[items[i].label] = used_times + 1
                numbers += 1
                
            if numbers >= num_wanted:
                break
                
        return total
