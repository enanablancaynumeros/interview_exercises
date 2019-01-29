import pytest

from collections import deque


class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            results = deque([1, 2])
            for i in range(2, n - 1):
                a = results.popleft()
                results.append(a + results[-1])
        return results[0] + results[1]


@pytest.mark.parametrize("values,expected", [(1, 1), (2, 2), (3, 3), (4, 5)])
def tests_a(values, expected):
    assert Solution().climbStairs(values) == expected
