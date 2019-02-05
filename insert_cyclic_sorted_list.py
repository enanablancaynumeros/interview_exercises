class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        if head is None:
            head = Node(insertVal, None)
            head.next = head
            return head

        if head.next is head:
            head.next = Node(insertVal, head.next)
            return head

        if head.val == insertVal:
            head.next = Node(insertVal, head.next)
            return head

        node = head.next
        while node is not head:
            if node.val < insertVal:
                if node.next.val >= insertVal:
                    node.next = Node(insertVal, node.next)
                    return head
                else:
                    if node.next.val >= node.val:
                        node = node.next
                    else:
                        node.next = Node(insertVal, node.next)
                        return head
            elif node.val > insertVal:
                if node.next.val > insertVal:
                    if node.val <= node.next.val:
                        node = node.next
                    else:
                        node.next = Node(insertVal, node.next)
                        return head
                else:
                    node = node.next
            else:
                node.next = Node(insertVal, node.next)
                return head

        node.next = Node(insertVal, node.next)
        return head


def tests():
    head = Node(3, None)
    head.next = Node(3, Node(5, head))
    Solution().insert(head, 0)
