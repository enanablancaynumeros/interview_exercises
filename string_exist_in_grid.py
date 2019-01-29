from collections import deque
from copy import copy

import pytest


class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word:
            return False
        for i, row in enumerate(board):
            for j in range(len(row)):
                if self.search_from_letter((i, j), board, word):
                    return True
        return False
    
    def search_from_letter(self, coordinates, grid, word, visited=None):
        if visited is None:
            visited = set()
        if grid[coordinates[0]][coordinates[1]] != word[0]:
            return False
        elif len(word) == 1:
            return True
        
        visited.add(coordinates)
        for neighbour in ((0, 1), (0, -1), (-1, 0), (1, 0)):
            neighbour = (coordinates[0] + neighbour[0], coordinates[1] + neighbour[1])
            if 0 <= neighbour[0] < len(grid) and 0 <= neighbour[1] < len(grid[0]) and neighbour not in visited:
                if self.search_from_letter(neighbour, grid, word[1:], visited=copy(visited)):
                    return True
        return False


@pytest.mark.parametrize(
    "board,word,expected",
    [
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED", True),
        ([["a","a"]], "aaa", False)
    ],
)
def tests_a(board, word, expected):
    assert Solution().exist(board, word) == expected
