# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        
        node1 = l1
        node2 = l2
        carry = 0
        head = ListNode(None)
        node = head
        
        while(node1 and node2):
            curSum = node1.val + node2.val + carry
            curVal = curSum % 10
            carry = curSum // 10
            if node1 == l1 and node2 == l2:
                head = ListNode(curVal)
                node = head
            else:
                node.next = ListNode(curVal)
                node = node.next
            node1 = node1.next
            node2 = node2.next
        
        while(node1):
            curSum = node1.val + carry
            curVal = curSum % 10
            carry =  curSum // 10
            if node1 == l1:
                head = ListNode(curVal)
                node = head
            else:
                node.next = ListNode(curVal)
                node = node.next
            node1 = node1.next
            
        while(node2):
            curSum = node2.val + carry
            curVal = curSum % 10
            carry =  curSum // 10
            if node2 == l1:
                head = ListNode(curVal)
                node = head
            else:
                node.next = ListNode(curVal)
                node = node.next
            node2 = node2.next
        
        if carry != 0:
            node.next = ListNode(carry)
            node = node.next
        
        return head
                