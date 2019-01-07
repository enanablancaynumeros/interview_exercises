import pytest


class Heap:
    def __init__(self, values=None):
        self.array = [(None, None)]
        if values:
            for value in values:
                self.insert(value=value)

    def insert(self, value):
        self.array.append(value)
        if len(self.array) > 2:
            self._preserve_order_insert(position=self.last_index)

    def empty(self):
        return self.array == [(None, None)]

    @property
    def last_index(self):
        return len(self.array) - 1


class HeapMax(Heap):
    def get_max(self):
        self.array[1], self.array[-1] = self.array[-1], self.array[1]
        max_value = self.array.pop()
        self._replace_root_get(position=1)
        return max_value

    def _preserve_order_insert(self, position):
        if position == 1:
            return
        parent_index = position // 2
        if self.array[parent_index] < self.array[position]:
            self.array[parent_index], self.array[position] = (
                self.array[position],
                self.array[parent_index],
            )
            return self._preserve_order_insert(position=parent_index)

    def _replace_root_get(self, position):
        left_index = position * 2
        right_index = position * 2 + 1
        node_left_exists = left_index <= self.last_index
        right_node_exists = right_index <= self.last_index
        if (
            node_left_exists
            and self.array[position] < self.array[left_index]
            and (
                right_node_exists
                and self.array[left_index] > self.array[right_index]
                or right_node_exists is False
            )
        ):
            self.array[position], self.array[left_index] = (
                self.array[left_index],
                self.array[position],
            )
            return self._replace_root_get(position=left_index)
        elif right_node_exists and self.array[position] < self.array[right_index]:
            self.array[position], self.array[right_index] = (
                self.array[right_index],
                self.array[position],
            )
            return self._replace_root_get(position=right_index)


@pytest.mark.parametrize(
    "values,expected",
    [
        ([26, 15, 24, 12, 1, 33], sorted([26, 15, 24, 12, 1, 33], reverse=True)),
        ([], []),
        ([1, 2, 3], sorted([1, 2, 3], reverse=True)),
    ],
)
def tests_max(values, expected):
    heap = HeapMax(values=values)
    results = []
    while not heap.empty():
        results.append(heap.get_max())
    assert results == expected
