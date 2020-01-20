# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        node = head
        prev = None
        
        while node:
            if node.val == val:
                if node == head:
                    head = node.next
                elif node.next is None:
                    prev.next = None
                else:
                    prev.next = node.next
            else:
                prev = node
            node = node.next
        
        return head