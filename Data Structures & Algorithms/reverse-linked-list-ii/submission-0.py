# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reversedLinkedList(self,head: Optional[ListNode]):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev    
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev = None
        temp = head
        nxt = head
        prev_right = None
        while right > 0 and nxt:
            prev_right = nxt
            nxt = nxt.next  
            right-=1
        while left > 1:
            prev = temp
            temp = temp.next
            print(temp.val,end =' ')
            left -=1  
        prev_right.next = None  
        x = self.reversedLinkedList(temp)
        temp = x
        while temp.next:
           temp = temp.next
        temp.next = nxt  
        if prev is not None:
            prev.next = x
            return head        
        return x
