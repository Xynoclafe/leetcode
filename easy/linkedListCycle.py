# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from collections import defaultdict
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        seen = defaultdict(lambda: False)
        
        node = head
        
        while node != None:
            if seen[node]:
                return True
            else:
                seen[node] = True
            node = node.next
            
        return False