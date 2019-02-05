import math
from collections import Counter


import pytest


class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not len(t):
            return ""
        # if len(s) == len(t):
        #     if set(s) == set(t):
        #         return s
        #     else:
        #         return ""
        minimum = math.inf
        counter_t = Counter(t)
        counter_s = Counter()
        first_ind = 0
        second_ind = 0
        while second_ind < len(s):
            if s[second_ind] in counter_t:
                counter_s[s[second_ind]] += 1

            if counter_s == counter_t:
                while first_ind < len(s):
                    if s[first_ind] not in counter_t:
                        first_ind += 1
                    else:
                        pass
                possible_minimum = second_ind - first_ind + 1
                if possible_minimum < minimum:
                    minimum = possible_minimum
                    solution = (first_ind, second_ind)
                counter_s[s[first_ind]] -= 1
                first_ind += 1
                second_ind += 1
            else:
                second_ind += 1

        if minimum != math.inf:
            return s[solution[0] : solution[1] + 1]
        else:
            return ""


@pytest.mark.parametrize(
    "s,t,expected",
    [
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("AA", "AA", "AA"),
        ("ABC", "CBA", "ABC"),
        ("BBAA", "ABA", "BAA"),
    ],
)
def tests_substring(s, t, expected):
    assert Solution().minWindow(s, t) == expected
