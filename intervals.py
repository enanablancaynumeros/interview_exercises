import pytest


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def insert(
        self, intervals: "List[Interval]", newInterval: "Interval"
    ) -> "List[Interval]":
        if not len(intervals):
            intervals.append(newInterval)
            return intervals
        i = 0
        while i < len(intervals):
            # start or end is within range of current node
            if (
                intervals[i].start <= newInterval.start <= intervals[i].end
                or intervals[i].start <= newInterval.end <= intervals[i].end
                or newInterval.start <= intervals[i].start <= newInterval.end
                or newInterval.end <= intervals[i].end <= newInterval.end
            ):
                intervals[i].end = max(newInterval.end, intervals[i].end)
                intervals[i].start = min(newInterval.start, intervals[i].start)
                while i + 1 < len(intervals):
                    if intervals[i + 1].end <= intervals[i].end:
                        del intervals[i + 1]
                    elif (
                        intervals[i + 1].end
                        >= intervals[i].end
                        >= intervals[i + 1].start
                    ):
                        intervals[i].end = intervals[i + 1].end
                        del intervals[i + 1]
                    else:
                        return intervals
                return intervals
            # potentially next
            elif intervals[i].end < newInterval.start:
                if i + 1 == len(intervals) or intervals[i + 1].start > newInterval.end:
                    intervals.insert(i + 1, newInterval)
                    return intervals
            elif intervals[i].start > newInterval.end:
                intervals.insert(i, newInterval)
                return intervals
            i += 1
        else:
            intervals.append(newInterval)
            return intervals


@pytest.mark.parametrize(
    "values,new,expected",
    [
        (
            [Interval(1, 3), Interval(6, 9)],
            Interval(2, 5),
            [Interval(1, 5), Interval(6, 9)],
        ),
        (
            [Interval(1, 2), Interval(6, 9)],
            Interval(3, 5),
            [Interval(1, 2), Interval(3, 5), Interval(6, 9)],
        ),
        ([], Interval(3, 5), [Interval(3, 5)]),
        (
            [
                Interval(1, 2),
                Interval(3, 5),
                Interval(6, 7),
                Interval(8, 10),
                Interval(12, 16),
            ],
            Interval(4, 8),
            [Interval(1, 2), Interval(3, 10), Interval(12, 16)],
        ),
        ([Interval(1, 5)], Interval(0, 3), [Interval(0, 5)]),
        ([Interval(1, 5)], Interval(0, 8), [Interval(0, 8)]),
        ([Interval(1, 5)], Interval(0, 0), [Interval(0, 0), Interval(1, 5)]),
        (
            [Interval(0, 5), Interval(9, 12)],
            Interval(7, 16),
            [Interval(0, 5), Interval(7, 16)],
        ),
    ],
)
def tests_a(values, new, expected):
    results = Solution().insert(values, newInterval=new)
    assert len(results) == len(expected)
    for i, result in enumerate(results):
        assert result.end == expected[i].end
        assert result.start == expected[i].start
