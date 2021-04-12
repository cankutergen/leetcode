# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        dummy_head = None

        while head:
            next_node = head.next
            head.next = dummy_head
            dummy_head = head
            head = next_node

        return dummy_head
