# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        firstNode = None
        prev = None
        count = 0
        node = head
        while node is not None:
            count += 1
            if count == m - 1:
                prev = node
                node = node.next
            elif count == n + 1:
                firstNode.next = node
                node = node.next
            elif count == m:
                prevNode = node
                firstNode = node
                node = node.next
                firstNode.next = None
            elif count == n:
                if prev:
                    prev.next = node
                else:
                    head = node
                nextn = node.next
                node.next = prevNode
                node = nextn
            elif count > m  and count < n:
                nextn = node.next
                node.next = prevNode
                prevNode = node
                node = nextn
            else:
                node = node.next
        return head
                