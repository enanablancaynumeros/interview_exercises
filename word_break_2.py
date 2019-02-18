from typing import List

import pytest


class Solution:
    def wordBreak(self, s: "str", wordDict: "List[str]") -> "List[str]":
        words_set = set(wordDict)
        if not len(words_set) or not len(s):
            return []
        else:
            solutions = self.rec(s, words_set, 0, 0)
            return [" ".join(x) for x in solutions]

    def rec(self, s, words, i, j):
        all_solutions = []
        while j < len(s):
            if s[i : j + 1] in words:
                sub_solutions = self.rec(s, words, j + 1, j + 1)
                for sub_sol in sub_solutions:
                    all_solutions.append([s[i : j + 1]] + sub_sol)
            j += 1
        if s[i : j + 1] in words and j == len(s):
            all_solutions.append([s[i : j + 1]])
        return all_solutions


@pytest.mark.parametrize(
    "s,wordDict,expected",
    [
        (
            "aaaaaaa",
            ["aaaa", "aa", "a"],
            [
                "a a a a a a a",
                "aa a a a a a",
                "a aa a a a a",
                "a a aa a a a",
                "aa aa a a a",
                "aaaa a a a",
                "a a a aa a a",
                "aa a aa a a",
                "a aa aa a a",
                "a aaaa a a",
                "a a a a aa a",
                "aa a a aa a",
                "a aa a aa a",
                "a a aa aa a",
                "aa aa aa a",
                "aaaa aa a",
                "a a aaaa a",
                "aa aaaa a",
                "a a a a a aa",
                "aa a a a aa",
                "a aa a a aa",
                "a a aa a aa",
                "aa aa a aa",
                "aaaa a aa",
                "a a a aa aa",
                "aa a aa aa",
                "a aa aa aa",
                "a aaaa aa",
                "a a a aaaa",
                "aa a aaaa",
                "a aa aaaa",
            ],
        )
    ],
)
def test_a(s, wordDict, expected):
    res = Solution().wordBreak(s=s, wordDict=wordDict)
    # assert len(res) == len(expected)
    assert set(res) == set(expected)
