"""
Implement a function to check if a tree is balanced. For the purposes of this question,
a balanced tree is defined to be a tree such that no two leaf nodes differ in distance
from the root by more than one
"""
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
                node=self.root_node,
                set_of_levels=set(),
                current_level=0)
            if value is not False:
                return True
            else:
                return False

    def _traverse_tree_for_balance_calculation(self, node, set_of_levels, current_level):
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
                    current_level=current_level + 1)
                if left_child_value is False:
                    return False
            if node.right is not None:
                return self._traverse_tree_for_balance_calculation(
                    node=node.right,
                    set_of_levels=set_of_levels,
                    current_level=current_level + 1)


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def is_leaf(self):
        return self.left is None and self.right is None


@pytest.mark.parametrize('given_tree,expected', [
    (Tree(), True),
    (Tree([1]), True),
    (Tree([1, 1]), True),
    (Tree([2, 3, 1]), True),
    (Tree([2, 4, 3, 1, 5]), True),
    (Tree([2, 4, 3, 1, 5, 0, -1, -2, -3]), False),
    (Tree([2, 4, 3, 1, 5, 0, -1, -3]), False),
])
def test_balanced_tree(given_tree, expected):
    assert given_tree.is_balanced_tree() == expected


"""
Given a sorted (increasing order) array, write an algorithm to create a binary tree with
minimal height.
"""


def create_minimum_height_tree(sorted_array, tree=None):
    if tree is None:
        tree = Tree()

    if not len(sorted_array):
        return tree
    mid_position = len(sorted_array) // 2
    tree.insert(sorted_array[mid_position])
    create_minimum_height_tree(sorted_array[:mid_position], tree=tree)
    create_minimum_height_tree(sorted_array[mid_position+1:], tree=tree)
    return tree


@pytest.mark.parametrize('given_array', [
    ([]),
    ([1]),
    (sorted([1, 1])),
    (sorted([2, 3, 1])),
    (sorted([2, 4, 3, 1, 5])),
    (sorted([2, 4, 3, 1, 5, 0, -1, -2, -3])),
    (sorted([2, 4, 3, 1, 5, 0, -1, -3])),
])
def test_balanced_tree(given_array):
    tree = create_minimum_height_tree(given_array)
    assert tree.is_balanced_tree() is True


"""
You have two very large binary trees: T1, with millions of nodes, and T2, with hun-
dreds of nodes. Create an algorithm to decide if T2 is a subtree of T1
"""


def t2_subtree_t1(given_tree, subtree):
    if subtree.root_node is None and given_tree.root_node is None:
        return True
    elif subtree.root_node is None or given_tree.root_node is None:
        return False

    nodes_like_subtree_root = find_nodes_equal_to(
        tree=given_tree,
        value=subtree.root_node.value
    )
    for node_like_subtree_root in nodes_like_subtree_root:
        if is_subtree_from_node(
                bigger_tree_current_node=node_like_subtree_root,
                subtree_current_node=subtree.root_node):
            return True
    return False


def is_subtree_from_node(bigger_tree_current_node, subtree_current_node):
    if bigger_tree_current_node.value == subtree_current_node.value:
        if bigger_tree_current_node.left is not None and subtree_current_node.left is not None:
            left_inspection = is_subtree_from_node(
                bigger_tree_current_node=bigger_tree_current_node.left,
                subtree_current_node=subtree_current_node.left)
            if left_inspection is False:
                return False

        if bigger_tree_current_node.right is not None and subtree_current_node.right is not None:
            return is_subtree_from_node(
                bigger_tree_current_node=bigger_tree_current_node.right,
                subtree_current_node=subtree_current_node.right)
        return True
    else:
        return False


def find_nodes_equal_to(tree, value, current_node=None):
    if current_node is None:
        current_node = tree.root_node

    if current_node.value == value:
        yield current_node
    else:
        if current_node.left is not None:
            yield from find_nodes_equal_to(tree, value, current_node=current_node.left)
        elif current_node.right is not None:
            yield from find_nodes_equal_to(tree, value, current_node=current_node.right)


@pytest.mark.parametrize('given_tree,subtree,expected', [
    (Tree(), Tree(), True),
    (Tree([1, 2]), Tree([1, 2]), True),
    (Tree([5, 3, 4, 2, 9, 7, 8, 6]), Tree([3, 4, 2]), True),
    (Tree([5, 3, 4, 2, 9, 7, 8, 6]), Tree([4, 3, 2]), False),
])
def test_balanced_tree(given_tree, subtree, expected):
    assert t2_subtree_t1(given_tree=given_tree, subtree=subtree) == expected
