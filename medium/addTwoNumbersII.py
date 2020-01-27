# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def convertToNum(self, head):
        num = 0
        while(head is not None):
            num *= 10
            num += head.val
            head = head.next
        return num
    
    def convertToList(self, num):
        power = len(str(num)) - 1
        head = ListNode(num // (10 ** power))
        prevNode = head
        num = num % (10 ** power)
        power -= 1
        while(power >= 0):
            curNum = num // (10 ** power)
            num = num % (10 ** power)
            power -= 1
            node = ListNode(curNum)
            prevNode.next = node
            prevNode = node
        return head
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = self.convertToNum(l1)
        num2 = self.convertToNum(l2)
        num = num1 + num2
        return self.convertToList(num)
