# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        node = head
        prev = None
        
        while node:
            node2 = node.next
            if node2:
                if head == node:
                    head = node2
                swap = node2.next
                node2.next = node
                node.next = swap
                if prev:
                    prev.next = node2
            else:
                break
            prev = node
            node = node.next
            
        
        return head
