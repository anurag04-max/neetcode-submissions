# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        while (fast is not None and slow is not None):
            if slow.next is None:
                return False
            else:
                slow = slow.next
            if fast.next is None or fast.next.next is None:
                return False
            else:
                fast = fast.next.next
            if fast == slow:
                return True
        return False                        
        