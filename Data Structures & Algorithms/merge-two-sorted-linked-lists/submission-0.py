# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = list1
        s2 = list2
        if not s1:
            return s2
        if not s2:
            return s1
        mergeHead = ListNode()    
        if s1.val <= s2.val:    
            mergeHead.val = s1.val
            s1 = s1.next
        else:
            mergeHead.val = s2.val
            s2 = s2.next
        temp = mergeHead
        while (s1 is not None and s2 is not None):
            if s1.val <= s2.val:
                x = ListNode(s1.val)
                temp.next = x
                s1 = s1.next
            else:
                x = ListNode(s2.val)
                temp.next = x
                s2 = s2.next
            temp = temp.next    
        
        while(s2 is not None):
            x = ListNode(s2.val)
            temp.next = x
            s2 = s2.next
            temp = temp.next
        
        while(s1 is not None):
            x = ListNode(s1.val)
            temp.next = x
            s1 = s1.next
            temp = temp.next

        return mergeHead        




