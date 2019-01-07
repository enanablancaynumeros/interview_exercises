import pytest


def mergesort(values):
    if not len(values) or len(values) == 1:
        return values
    if len(values) == 2:
        if values[0] > values[1]:
            values[0], values[1] = values[1], values[0]
        return values
    else:
        mergesort(values[0 : len(values) // 2])
        mergesort(values[len(values) // 2 + 1 :])
        merge()
    return values


def merge(array_1, array_2):
    return []


@pytest.mark.parametrize(
    "values,expected",
    [([], []), ([1], [1]), ([2, 1], [1, 2]), ([2, 1, 4, 3, 5], [1, 2, 3, 4, 5])],
)
def tests(values, expected):
    assert mergesort(values) == expected
