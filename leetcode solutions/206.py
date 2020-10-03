# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev,curr,nxt = None,head,None
        while curr:
            nxt = curr.next
            curr.next = prev 
            prev = curr
            curr = nxt
        return prev