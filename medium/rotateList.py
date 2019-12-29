# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if(head is None or k == 0):
            return head
        node = head
        length = 1
        while(node.next is not None):
            node = node.next
            length += 1
        node.next = head
        steps = 0
        reqSteps = length - (k % length)
        node = head
        while(steps < reqSteps):
            prevNode = node
            node = node.next
            steps += 1
        head = node
        prevNode.next = None
        return head
        
