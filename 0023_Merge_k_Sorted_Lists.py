# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists):
        dummy = curr = ListNode(0)
        heap = []
        for ind, el in enumerate(lists):
            if el: heappush(heap, (el.val, ind))
                
        while heap:
            val, ind = heappop(heap)
            curr.next = ListNode(val)
            curr = curr.next
            if lists[ind].next:
                lists[ind] = lists[ind].next
                heappush(heap, (lists[ind].val, ind))
                
        return dummy.next
