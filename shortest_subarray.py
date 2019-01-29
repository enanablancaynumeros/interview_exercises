import pytest


class Solution:
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        shortest = 10 ** 10
        for i in range(len(A)):
            sub_sum = 0
            for j in range(i, len(A)):
                sub_sum += A[j]
                if sub_sum >= K:
                    new_shortest = j - i + 1
                    if new_shortest < shortest:
                        shortest = new_shortest
                        break
        if shortest > len(A):
            return -1
        return shortest


class SolutionOptimal:
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        shortest = 10 ** 10
        if not len(A):
            return -1

        sums = dict()
        i = 0
        acum = A[i]
        for j in range(i + 1, len(A)):
            acum += A[j]
            sums[(i, j)] = acum
        return shortest
