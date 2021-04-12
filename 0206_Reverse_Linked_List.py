# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        stack = []
        
        while head is not None:
            stack.append(head)
            head = head.next
            
        dummy = ListNode(-1)
        head = dummy
        
        while len(stack) is not 0:
            current = stack.pop()
            head.next = ListNode(current.val)
            head = head.next
            
        return dummy.next
