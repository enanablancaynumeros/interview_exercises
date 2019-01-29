import pytest


class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(len(A)):
            len_row = len(A[i])
            for j in range(len_row // 2):
                temp = A[i][len_row - j - 1]
                A[i][len_row - j - 1] = 1 if A[i][j] == 0 else 0
                A[i][j] = 1 if temp == 0 else 0
            if len_row % 2 != 0:
                A[i][(len_row // 2)] = 1 if A[i][(len_row // 2)] == 0 else 0
        return A


@pytest.mark.parametrize(
    "values,expected",
    [
        ([[1, 1, 0], [1, 0, 1], [0, 0, 0]], [[1, 0, 0], [0, 1, 0], [1, 1, 1]]),
        (
            [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]],
            [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]],
        ),
    ],
)
def tests_a(values, expected):
    assert Solution().flipAndInvertImage(values) == expected
