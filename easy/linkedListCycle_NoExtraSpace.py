# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        fp = head
        sp = head
        
        while sp is not None:
            
            fp = fp.next
            
            sp = sp.next
            if sp is None:
                return False
            else:
                sp = sp.next
            
            if sp == fp:
                return True
            
        return False