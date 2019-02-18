import pytest


class Solution:
    def largestIsland(self, grid: "List[List[int]]") -> "int":
        biggest_island = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                previous_value = grid[i][j]
                grid[i][j] = 1
                size = self.get_island_size(grid, i, j)
                biggest_island = max(size, biggest_island)
                grid[i][j] = previous_value
        return biggest_island

    def get_island_size(self, grid, i, j, visited=None):
        if visited is None:
            visited = set()

        visited.add((i, j))
        for cell in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            x, y = i + cell[0], j + cell[1]
            if (
                len(grid) > x >= 0
                and len(grid[0]) > y >= 0
                and grid[x][y] == 1
                and (x, y) not in visited
            ):
                self.get_island_size(grid, x, y, visited)

        return len(visited)


@pytest.mark.parametrize("board,expected", [([[1, 0], [0, 1]], 3)])
def tests(board, expected):
    assert Solution().largestIsland(board) == expected

