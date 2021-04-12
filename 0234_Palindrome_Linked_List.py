# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True
        
        fast = head
        slow = head
        
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            
        second_half_head = self.reverse(slow.next)
        first_half_head = head
        
        while second_half_head and first_half_head:
            if second_half_head.val != first_half_head.val:
                return False
            
            second_half_head = second_half_head.next
            first_half_head = first_half_head.next
            
        return True
    
    def reverse(self, head):
        dummy_head = None
        
        while head:
            next_node = head.next
            head.next = dummy_head
            dummy_head = head
            head = next_node
    
        return dummy_head
