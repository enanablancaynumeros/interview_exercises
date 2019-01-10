from collections import Counter

import pytest


# def max_points(points):
#     existing = {tuple(point) for point in points}
#     visited = set()
#     max_len = 0
#     if not len(existing):
#         return max_len
#     for point in existing:
#         for direction in Direction:
#             sub_len = 1
#             while
#         if point not in visited:
#             for adjacent in get_valid_adjacent(point, existing, visited):
#                     pass

#             visited.add(point)
#     return max_len


class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        points_counter = Counter([(point.x, point.y) for point in points])
        max_len = 0 if not len(points_counter) else max(points_counter.values())
        for point_a in points_counter:
            for point_b in points_counter:
                if point_a != point_b:
                    num_points = self.points_in_the_line(
                        point_a, point_b, points_counter
                    )
                    if num_points > max_len:
                        max_len = num_points
        return max_len

    def points_in_the_line(self, point_a, point_b, points_set):
        x_axis_diff = point_a[0] - point_b[0]
        y_axis_diff = point_a[1] - point_b[1]
        total_intermediary_points = points_set[point_a] + points_set[point_b]
        if abs(x_axis_diff) == abs(y_axis_diff) or y_axis_diff == 0 or x_axis_diff == 0:
            for i in range(1, max((abs(x_axis_diff)), abs(y_axis_diff))):
                if x_axis_diff > 0:
                    x_value = point_a[0] - i
                elif x_axis_diff < 0:
                    x_value = point_a[0] + i
                else:
                    x_value = point_a[0]

                if y_axis_diff > 0:
                    y_value = point_a[1] - i
                elif y_axis_diff < 0:
                    y_value = point_a[1] + i
                else:
                    y_value = point_a[1]

                intermediary_point = (x_value, y_value)
                if intermediary_point in points_set:
                    total_intermediary_points += points_set[intermediary_point]
            return total_intermediary_points
        else:
            return 0


@pytest.mark.parametrize(
    "point_a,point_b,points_set,expected",
    [
        ((1, 1), (2, 2), Counter([(1, 1), (2, 2), (3, 3)]), 2),
        ((1, 1), (3, 3), Counter([(1, 1), (2, 2), (3, 3)]), 3),
        ((0, 1), (0, 3), Counter([(0, 1), (0, 2), (0, 3)]), 3),
        ((0, 1), (2, 2), Counter([(0, 1), (2, 2)]), 0),
        ((1, 4), (4, 1), Counter([(1, 4), (2, 3), (3, 2), (4, 1)]), 4),
        ((4, 1), (1, 4), Counter([(1, 4), (2, 3), (3, 2), (4, 1)]), 4),
        ((-1, -1), (2, 2), Counter([(-1, -1), (0, 0), (2, 2)]), 3),
    ],
)
def tests_points_connected(point_a, point_b, points_set, expected):
    assert Solution().points_in_the_line(point_a, point_b, points_set) == expected


@pytest.mark.parametrize(
    "values,expected",
    [
        ([Point(0, 0), Point(0, 0)], 2),
        ([Point(1, 1), Point(2, 2), Point(3, 3)], 3),
        (
            [
                Point(1, 1),
                Point(3, 2),
                Point(5, 3),
                Point(4, 1),
                Point(2, 3),
                Point(1, 4),
            ],
            4,
        ),
        ([Point(1, 1), Point(1, 1), Point(2, 3)], 3),
    ],
)
def tests_max_points(values, expected):
    assert Solution().maxPoints(values) == expected
