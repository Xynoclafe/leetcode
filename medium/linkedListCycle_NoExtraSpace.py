# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from collections import defaultdict
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        fp = head
        sp = head
        
        while sp is not None:
            
            fp = fp.next
            
            sp = sp.next
            if sp is None:
                return None
            else:
                sp = sp.next
            
            if sp == fp:
                fp = head
                while(fp != sp):
                    sp = sp.next
                    fp = fp.next
                return fp
            
        return None