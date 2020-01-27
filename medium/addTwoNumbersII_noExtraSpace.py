class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        
        def reverse(l1):
            prev = None
            node = l1
            while node:
                nxt = node.next
                node.next = prev
                prev = node
                node = nxt
            return prev

        node1 = reverse(l1)
        node2 = reverse(l2)
        h1 = node1
        h2 = node2
        carry = 0
        head = ListNode(None)
        node = head

        while(node1 and node2):
            curSum = node1.val + node2.val + carry
            curVal = curSum % 10
            carry = curSum // 10
            if node1 == h1 and node2 == h2:
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
            if node1 == h1:
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
            if node2 == h2:
                head = ListNode(curVal)
                node = head
            else:
                node.next = ListNode(curVal)
                node = node.next
            node2 = node2.next

        if carry != 0:
            node.next = ListNode(carry)
            node = node.next
        
        return reverse(head)


