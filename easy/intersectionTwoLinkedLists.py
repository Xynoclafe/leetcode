# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from collections import deque
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        list1 = deque()
        list2 = deque()
        head = headA
        while(head is not None):
            list1.append(head)
            head = head.next
        node = headB
        while(node is not None):
            list2.append(node)
            node = node.next
        set1 = set(list1).intersection(set(list2))
        index = 10 ** 10
        if len(set1) == 0:
            return None
        else:
            for item in set1:
                curIndex = list1.index(item)
                if curIndex < index:
                    index = curIndex
            return list1[index]
