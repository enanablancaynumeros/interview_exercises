import pytest


class Solution:
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        i = 0
        asteroids_moving_right = []
        while i < len(asteroids):
            if asteroids[i] < 0:
                if len(asteroids_moving_right):
                    if abs(asteroids[i]) > abs(asteroids_moving_right[-1]):
                        value = asteroids_moving_right.pop()
                        index = i - 1 - asteroids[:i][::-1].index(value)
                        del asteroids[index]
                        i -= 1
                        continue
                    elif abs(asteroids[i]) < abs(asteroids_moving_right[-1]):
                        del asteroids[i]
                        continue
                    else:
                        value = asteroids_moving_right.pop()
                        index = i - 1 - asteroids[:i][::-1].index(value)
                        del asteroids[i]
                        del asteroids[index]
                        i -= 1
                        continue
            else:
                asteroids_moving_right.append(asteroids[i])
            i += 1
        return asteroids


@pytest.mark.parametrize(
    "values,expected",
    [
        ([5, 10, -5], [5, 10]),
        ([8, -8], []),
        ([-2, -1, 1, 2], [-2, -1, 1, 2]),
        ([10, 2, -5], [10]),
        ([-2, 2, 1, -2], [-2]),
        ([-2, 1, -2, 1], [-2, -2, 1]),
    ],
)
def tests_asteroids(values, expected):
    assert Solution().asteroidCollision(values) == expected
