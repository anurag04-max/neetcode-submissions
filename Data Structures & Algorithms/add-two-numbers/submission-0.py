# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        dummy = ans
        carry = 0
        while(l1 is not None and l2 is not None):
            val = l1.val + l2.val + carry
            carry = val // 10
            val = val % 10
            dummy.next = ListNode(val)
            dummy = dummy.next
            l1 = l1.next
            l2 = l2.next
        while(l1 is not None):
            val = l1.val + carry
            carry = val // 10
            val = val % 10
            dummy.next = ListNode(val)
            dummy = dummy.next
            l1 = l1.next
        while(l2 is not None):
            val = l2.val + carry
            carry = val // 10
            val = val % 10
            dummy.next = ListNode(val)
            dummy = dummy.next 
            l2 = l2.next   
        if carry != 0:
            dummy.next = ListNode(carry)
        return ans.next    

            