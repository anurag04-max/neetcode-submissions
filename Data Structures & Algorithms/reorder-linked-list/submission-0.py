# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseLinkedList(self, head: Optional[ListNode]):
        temp = head
        prev = None
        while(temp):
            nxt = temp.next
            temp.next = prev
            prev = temp
            temp = nxt
        return prev    
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = self.reverseLinkedList(slow.next)
        slow.next = None
        temp = head
        while temp and mid:
            nxt = temp.next
            temp.next = mid
            x = None
            if mid.next:
                x = mid.next
            temp = temp.next
            temp.next  = nxt
            temp = nxt
            mid = x        