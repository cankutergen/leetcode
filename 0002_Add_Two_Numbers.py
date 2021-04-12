# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        result = ListNode(0)
        lr = result
        
        while l1 or l2 or carry > 0:
            num_one, num_two = 0, 0
            if l1:
                num_one = l1.val
                l1 = l1.next
            if l2: 
                num_two = l2.val
                l2 = l2.next
            val = num_one + num_two + carry
            carry = 0
            if val >= 10: 
                val = val - 10
                carry = 1
            lr.val = val
            if l2 or l1 or carry > 0:
                lr.next = ListNode(0)
                lr = lr.next
        return result
