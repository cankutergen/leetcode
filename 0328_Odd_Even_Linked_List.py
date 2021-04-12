# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        
        head_odd = head
        head_even = head.next
        even = head_even
        
        while head_even and head_even.next:
            head_odd.next = head_even.next
            head_odd = head_odd.next
            
            head_even.next = head_odd.next
            head_even = head_even.next
            
        head_odd.next = even
        return head
