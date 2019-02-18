import pytest


class Tree:
    def __init__(self, initial_values=None):
        self.root_node = None
        if initial_values is not None:
            for initial_value in initial_values:
                self.insert(initial_value)

    def insert(self, value):
        if self.root_node is None:
            self.root_node = TreeNode(value)
        else:
            if self._insert(value, node=self.root_node) is None:
                return False
        return True

    def _insert(self, value, node):
        if value > node.val:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                return self._insert(value, node=node.right)
        elif value < node.val:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                return self._insert(value, node=node.left)


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if root.val == p.val:
            if root.right is not None:
                return root.right
            else:
                return None
        else:
            if root.val < p.val:
                if root.right is not None:
                    return self.inorderSuccessor(root.right, p)
            elif root.left is not None:
                value = self.inorderSuccessor(root.left, p)
                if value is not None:
                    return value
                else:
                    if root.val > p.val:
                        return root


@pytest.mark.parametrize(
    "values,p,expected",
    [
        ([6, 2, 8, 0, 4, 7, 9, 3, 5], 5, 6),
        ([6, 2, 8, 0, 4, 7, 9, 3, 5], 6, 8),
        ([6, 2, 8, 0, 4, 7, 9, 3, 5], 7, 8),
        ([6, 2, 8, 0, 4, 7, 9, 3, 5], 2, 3),
        ([2, 1, 3], 2, 3),
    ],
)
def tests(values, p, expected):
    tree = Tree(values)
    p = TreeNode(p)
    assert Solution().inorderSuccessor(tree.root_node, p).val == expected
