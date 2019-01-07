import collections

import pytest


class Tree:
    def __init__(self, initial_values=None):
        self.root_node = None
        if initial_values is not None:
            for initial_value in initial_values:
                self.insert(initial_value)

    def insert(self, value):
        if self.root_node is None:
            self.root_node = Node(value)
        else:
            if self._insert(value, node=self.root_node) is None:
                return False
        return True

    def _insert(self, value, node):
        if value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                return self._insert(value, node=node.right)
        elif value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                return self._insert(value, node=node.left)

    def is_balanced_tree(self):
        if self.root_node is None:
            return True
        else:
            value = self._traverse_tree_for_balance_calculation(
                node=self.root_node, set_of_levels=set(), current_level=0
            )
            if value is not False:
                return True
            else:
                return False

    def _traverse_tree_for_balance_calculation(
        self, node, set_of_levels, current_level
    ):
        if node.is_leaf():
            if current_level not in set_of_levels:
                set_of_levels.add(current_level)
            if abs(min(set_of_levels) - max(set_of_levels)) > 1:
                return False
            return True
        else:
            if node.left is not None:
                left_child_value = self._traverse_tree_for_balance_calculation(
                    node=node.left,
                    set_of_levels=set_of_levels,
                    current_level=current_level + 1,
                )
                if left_child_value is False:
                    return False
            if node.right is not None:
                return self._traverse_tree_for_balance_calculation(
                    node=node.right,
                    set_of_levels=set_of_levels,
                    current_level=current_level + 1,
                )


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def is_leaf(self):
        return self.left is None and self.right is None


def findBottomLeftValue(tree):
    left_most = tree.root_node.value
    queue = [tree.root_node]
    while len(queue):
        left_most = queue[0].value
        queue = [leaf for node in queue for leaf in (node.left, node.right) if leaf]
    return left_most


@pytest.mark.parametrize("values,expected", [([3, 4, 5, 1, 7], 7)])
def tests_bfs_2(values, expected):
    tree = Tree(values)
    results = findBottomLeftValue(tree)
    assert results == expected
