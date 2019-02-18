from typing import Set, List, Dict

import pytest


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        if not len(word_set) or not len(s):
            return False
        self.storage: Dict[int, bool] = dict()
        return self.rec(s, word_set, 0, 0)

    def rec(self, s: str, word_set: Set[str], i: int, j: int) -> bool:
        while j < len(s):
            precalculated = self.storage.get(i)
            if precalculated is not None:
                return precalculated
            if s[i : j + 1] in word_set:
                if j + 1 == len(s):
                    self.storage[i] = True
                    return True
                else:
                    if self.rec(s, word_set, j + 1, j + 1):
                        self.storage[j + 1] = True
                        return True
                    self.storage[j + 1] = False
            j += 1
        self.storage[i] = False
        return False


input_a = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
word_dict = [
    "a",
    "aa",
    "aaa",
    "aaaa",
    "aaaaa",
    "aaaaaa",
    "aaaaaaa",
    "aaaaaaaa",
    "aaaaaaaaa",
    "aaaaaaaaaa",
]


@pytest.mark.parametrize("s,wordDict,expected", [(input_a, word_dict, False)])
def test_a(s, wordDict, expected):
    assert Solution().wordBreak(s=s, wordDict=wordDict) == expected


if __name__ == "__main__":
    Solution().wordBreak(input_a, word_dict)
