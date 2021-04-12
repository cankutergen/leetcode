# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:      
        if head is None:
            return False
        
        walker = head
        runner = head
        
        while walker and runner and walker.next and runner.next and runner.next.next:
            walker = walker.next
            runner = runner.next.next
            
            if walker == runner:
                return True
        
        return False
