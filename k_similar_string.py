from collections import defaultdict
import copy

import pytest


class Solution:
    big_number = 999999999999

    def kSimilarity(self, A: "str", B: "str") -> "int":
        indexes_a = defaultdict(list)
        indexes_b = defaultdict(list)
        for i, char in enumerate(A):
            indexes_a[char].append(i)
        for i, char in enumerate(B):
            indexes_b[char].append(i)

        if set(indexes_a) != set(indexes_b):
            return self.big_number

        for char in indexes_a:
            if len(indexes_a[char]) != len(indexes_b[char]):
                return self.big_number

        memory = {}
        return self.differences(A, B, indexes_a, memory)

    def differences(self, A, B, indexes_a, memory, i=0):
        smallest = 0
        while i < len(A):
            if A[i] != B[i]:
                valid_options = [x for x in indexes_a[B[i]] if x > i]
                if not valid_options:
                    return self.big_number

                best_path = self.big_number
                for swap in valid_options:
                    new_a = A[:i] + B[i] + A[i + 1 : swap] + A[i] + A[swap + 1 :]
                    new_indexes = copy.deepcopy(indexes_a)
                    new_indexes[A[i]] = [x for x in new_indexes[A[i]] if x > i] + [swap]
                    new_indexes[B[i]] = [x for x in new_indexes[B[i]] if x != swap]
                    precalculated = memory.get((new_a, B))
                    if precalculated:
                        path = precalculated
                    else:
                        path = self.differences(new_a, B, new_indexes, memory, i + 1)
                        memory[(new_a, B)] = path
                    best_path = min(best_path, path)

                return 1 + best_path
            i += 1
        return smallest


@pytest.mark.parametrize(
    "A,B,expected",
    [
        ("ab", "ba", 1),
        ("abc", "bca", 2),
        ("bccaba", "abacbc", 3),
        ("abbcac", "abcbca", 2),
    ],
)
def tests(A, B, expected):
    assert Solution().kSimilarity(A, B) == expected


mapa = [
    [
        0,
        0,
        1,
        0,
        1,
        0,
        1,
        1,
        1,
        0,
        0,
        0,
        0,
        1,
        0,
        0,
        1,
        0,
        0,
        1,
        1,
        1,
        0,
        1,
        1,
        1,
        0,
        0,
        0,
        1,
        1,
        0,
        1,
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        0,
        0,
        0,
        0,
        1,
        1,
        1,
        1,
        0,
    ],
    [
        0,
        0,
        1,
        0,
        0,
        1,
        1,
        1,
        0,
        0,
        1,
        0,
        1,
        0,
        0,
        1,
        1,
        0,
        0,
        1,
        0,
        0,
        0,
        1,
        0,
        1,
        1,
        1,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        1,
        1,
        1,
        0,
        0,
        0,
        1,
        0,
        1,
        1,
        0,
        1,
        0,
        0,
        0,
    ],
    [
        0,
        1,
        0,
        1,
        0,
        1,
        1,
        1,
        0,
        0,
        1,
        1,
        0,
        0,
        0,
        0,
        1,
        0,
        1,
        0,
        1,
        1,
        1,
        0,
        1,
        1,
        1,
        0,
        0,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        0,
        0,
        1,
        1,
        1,
        1,
        1,
        0,
        0,
        1,
        0,
        0,
        1,
        0,
    ],
    [
        1,
        0,
        1,
        0,
        0,
        1,
        0,
        1,
        0,
        0,
        1,
        0,
        0,
        1,
        1,
        1,
        0,
        1,
        0,
        0,
        0,
        0,
        1,
        0,
        1,
        0,
        0,
        1,
        0,
        1,
        1,
        1,
        0,
        1,
        0,
        0,
        0,
        1,
        1,
        1,
        0,
        0,
        0,
        0,
        1,
        1,
        1,
        1,
        1,
        1,
    ],
]
