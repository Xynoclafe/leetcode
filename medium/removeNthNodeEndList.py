# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        count = 0
        node = head
        
        while node.next != None:
            count += 1
            node = node.next
        count += 1
        
        
        node = head
        i = 0
        while i < (count - n - 1):
            node = node.next
            i += 1
        print(node.val)
        
        if(n == count):
            head = head.next
            return head
        elif(n != 1):
            remNode = node.next
            nextNode = remNode.next
            node.next = nextNode
            return head
        else:
            remNode = node.next
            nextNode = None
            node.next = nextNode
            return head
        
