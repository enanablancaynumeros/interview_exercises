import pytest


def max_points(points):
    return 0


@pytest.mark.parametrize("values,expected", [([[1, 1], [2, 2], [3, 3]], 3)])
def tests_max_points(values, expected):
    assert max_points(values) == expected
