# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        walker = runner = head

        while runner is not None:
            runner = runner.next
            if runner is None:
                return None
            
            runner = runner.next
            walker = walker.next
            
            if walker == runner:
                break
                
        if runner is None:
            return None
        
        walker = head
        while walker != runner:
            walker = walker.next
            runner = runner.next
            
        return walker
