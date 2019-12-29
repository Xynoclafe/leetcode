# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        node1 = l1
        node2 = l2
        if(node1 is None):
            return node2
        if(node2 is None):
            return node1
        if(node1.val < node2.val):
            head = node1
            node1 = node1.next
        else:
            head = node2
            node2 = node2.next
        node = head
        while(True):
            if(node1 == None and node2 == None):
                break
            if(node1 == None):
                node.next = node2
                node = node.next
                node2 = node2.next
            elif(node2 == None):
                node.next = node1
                node = node.next
                node1 = node1.next
            elif(node1.val < node2.val):
                node.next = node1
                node = node.next
                node1 = node1.next
            else:
                node.next = node2
                node = node.next
                node2 = node2.next
        return head
            
            
        
