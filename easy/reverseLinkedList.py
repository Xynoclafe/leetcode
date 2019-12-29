# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node = head
        prevNode = None
        while(node is not None):
            nextNode = node.next
            node.next = prevNode
            prevNode = node
            node = nextNode
        return prevNode
        
