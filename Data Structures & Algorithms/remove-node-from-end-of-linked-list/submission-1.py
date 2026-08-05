# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        temp = head
        while(temp is not None):
            count +=1
            temp = temp.next
        d = count - n 
        x = 0
        temp = head
        prev = None
        while(temp is not None):
            if x == d:
                if prev is None:
                    return temp.next
                else:
                    prev.next = temp.next
                    del temp
                    break
            x+=1
            prev = temp
            temp = temp.next   
        return head             

