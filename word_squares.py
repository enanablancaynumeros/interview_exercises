from typing import List, Dict, Iterator

import pytest

from data import many_words


class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        if not len(words):
            return []
        len_final = len(words[0])
        solutions = []
        words_map = self.build_words_map(words)
        for starting_node in words:
            if len(starting_node) != len_final:
                return []
            else:
                sub_solutions = self.find_subsolutions(
                    [starting_node], len_final, words_map
                )
                solutions.extend(sub_solutions)
        return solutions

    def find_subsolutions(
        self, solution: List[str], len_final: int, words_map: Dict[str, List[str]]
    ):
        all_solutions = []
        if len(solution) == len_final:
            return [solution]
        for option in self.get_options(solution, words_map):
            sub_solutions = self.find_subsolutions(
                solution + [option], len_final, words_map
            )
            all_solutions.extend(sub_solutions)
        return all_solutions

    def get_options(
        self, solution: List[str], words_map: Dict[str, List[str]]
    ) -> Iterator[str]:
        len_sol = len(solution)
        index = "".join([x[len_sol] for x in solution])
        for option in words_map[index]:
            yield option

    def build_words_map(self, words: List[str]) -> Dict[str, List[str]]:
        from collections import defaultdict

        words_map = defaultdict(list)
        for word in words:
            for i in range(len(words[0])):
                words_map[word[: i + 1]].append(word)
        return words_map


@pytest.mark.parametrize(
    "values,expected",
    [
        (
            ["abat", "baba", "atan", "atal"],
            [["baba", "abat", "baba", "atal"], ["baba", "abat", "baba", "atan"]],
        ),
        (
            ["area", "lead", "wall", "lady", "ball"],
            [["ball", "area", "lead", "lady"], ["wall", "area", "lead", "lady"]],
        ),
        (["a"], [["a"]]),
    ],
)
def tests_a(values, expected):
    solutions = Solution().wordSquares(values)
    for solution in solutions:
        assert solution in expected
    assert len(expected) == len(solutions)


if __name__ == "__main__":
    Solution().wordSquares(many_words)
