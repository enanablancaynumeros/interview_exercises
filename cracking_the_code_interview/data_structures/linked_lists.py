import pytest


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, initial_list=None):
        self.first_item = None
        if initial_list is not None:
            for item in initial_list:
                self.add(item)

    def as_list(self):
        list_to_return = []
        if self.first_item is None:
            return []
        else:
            current_item = self.first_item
            while current_item is not None:
                list_to_return.append(current_item.value)
                current_item = current_item.next
            return list_to_return

    def add(self, other):
        new_node = Node(other)
        if self.first_item is None:
            self.first_item = new_node
        else:
            current_item = self.first_item
            while current_item.next is not None:
                current_item = current_item.next
            current_item.next = new_node

    def remove(self, value_to_remove):
        if self.first_item is not None:
            if self.first_item.value == value_to_remove:
                self.first_item = self.first_item.next
            else:
                current_node = self.first_item
                while current_node.next is not None:
                    if current_node.next.value == value_to_remove:
                        current_node.next = current_node.next.next
                        return None
                    else:
                        current_node = current_node.next


@pytest.mark.parametrize(
    "item_to_remove,given_linked_list,expected",
    [(1, [1], []), (1, [], []), (1, [2, 3, 1], [2, 3]), (1, [2, 3], [2, 3])],
)
def test_basics(item_to_remove, given_linked_list, expected):
    own_linked_list = LinkedList()
    for linked_item in given_linked_list:
        own_linked_list.add(linked_item)
    own_linked_list.remove(item_to_remove)
    assert own_linked_list.as_list() == expected


"""
Write code to remove duplicates from an unsorted linked list.
"""


def remove_duplicates(given_linked_list):
    seen_items = set()
    current_node = given_linked_list.first_item
    if current_node is None:
        return
    seen_items.add(current_node.value)
    while current_node.next is not None:
        if current_node.next.value in seen_items:
            current_node.next = current_node.next.next
        else:
            seen_items.add(current_node.next.value)
            current_node = current_node.next


@pytest.mark.parametrize(
    "given_linked_list,expected",
    [
        (LinkedList([1]), [1]),
        (LinkedList([1, 1]), [1]),
        (LinkedList([2, 3, 2]), [2, 3]),
        (LinkedList([]), []),
        (LinkedList([2, 2, 2, 2, 3, 2]), [2, 3]),
    ],
)
def test_remove_duplicates(given_linked_list, expected):
    remove_duplicates(given_linked_list)
    assert given_linked_list.as_list() == expected
