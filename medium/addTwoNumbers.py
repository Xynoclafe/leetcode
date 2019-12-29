# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = self.getNums(l1)
        num2 = self.getNums(l2)
        num = num1 + num2
        num = str(num)
        returnList = []
        for i in range(len(num)):
            newItem = ListNode(num[i])
            returnList.append(newItem)
        returnList.reverse()
        for i in range(len(num)-1):
            returnList[i].next = returnList[i + 1]
        return returnList[0]
        
    def getNums(self, list):
        multiplier = 1
        num = 0
        item = list
        while item != None:
            num += item.val * multiplier
            multiplier *= 10
            item = item.next
        return num
            
