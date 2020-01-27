# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        nodeList = []
        for item in lists:
            while(item is not None):
                nodeList.append(item)
                item = item.next
        nodeList = sorted(nodeList, key = lambda x: x.val)
        if(len(nodeList) == 0):
            return None
        head = nodeList.pop(0)
        node = head
        while(len(nodeList) > 0):
            node.next = nodeList.pop(0)
            node = node.next
        return head
