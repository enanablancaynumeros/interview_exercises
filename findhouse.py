import math
from collections import deque
import heapq

import pytest

from data import big_map, second_big_map


class Solution:
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.min_distance = math.inf
        if not grid:
            return -1
        self.grid = grid
        self.num_rows = len(self.grid)
        self.num_columns = len(self.grid[0])
        self.buildings = {
            (i, j)
            for i in range(len(grid))
            for j, point in enumerate(grid[i])
            if point == 1
        }
        self.calculated_paths = {}
        for i in range(len(grid)):
            for j, point in enumerate(grid[i]):
                if point == 0:
                    x_min = sum(
                        [
                            (building[0] - i) + abs(building[1] - j)
                            for building in self.buildings
                        ]
                    )
                    if x_min < self.min_distance:
                        real_distance = self.acum_distance_all_buildings(pos=(i, j))
                        if real_distance > 0 and real_distance < self.min_distance:
                            self.min_distance = real_distance
                            # print(f'shortest is {i, j}')
        return self.min_distance if self.min_distance is not math.inf else -1

    def acum_distance_all_buildings(self, pos):
        acum = 0
        for building in self.buildings:
            path_len = self.find_path(pos, building)
            if path_len is not None:
                acum += path_len
            else:
                return -1
        return acum

    def find_path(self, pos, target):
        if (pos, target) in self.calculated_paths:
            return self.calculated_paths[(pos, target)]
        children = deque([[pos], None])
        visited = set()
        while True:
            path = children.popleft()
            if path is None:
                if not children:
                    # print(f'path not found from {pos} to {target}')
                    return None
                else:
                    children.append(None)
                    continue
            last_node = path[-1]
            visited.add(last_node)

            adjs = []
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                adj = (last_node[0] + dx, last_node[1] + dy)
                if (
                    self.num_rows > adj[0] >= 0
                    and self.num_columns > adj[1] >= 0
                    and adj not in visited
                ):
                    if adj == target:
                        total_len = len(path)
                        for i, step_path in enumerate(path):
                            self.calculated_paths[(step_path, target)] = total_len - i
                        return total_len
                    elif self.grid[adj[0]][adj[1]] == 0:
                        euclidean_distance = math.sqrt(
                            (adj[0] - target[0]) ** 2 + (adj[1] - target[1]) ** 2
                        )
                        heapq.heappush(adjs, (euclidean_distance, adj))

            if not adjs:
                self.calculated_paths[(last_node, target)] = None

            while len(adjs):
                _, adj = heapq.heappop(adjs)
                if (pos, target) in self.calculated_paths:
                    precalculated_value = self.calculated_paths[(pos, target)]
                    if precalculated_value is not None:
                        return precalculated_value + len(path)
                    else:
                        continue
                else:
                    children.append(path + [adj])


@pytest.mark.parametrize(
    "values,expected",
    [
        ([[0, 0], [0, 1]], 1),
        ([[0, 0, 0], [0, 1, 0]], 1),
        ([[0, 2, 1, 2, 0], [0, 2, 1, 2, 0], [0, 2, 1, 2, 0]], -1),
        ([[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]], 7),
        (
            [
                [1, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 1],
                [0, 1, 1, 0, 0, 1],
                [1, 0, 0, 1, 0, 1],
                [1, 0, 1, 0, 0, 1],
                [1, 0, 0, 0, 0, 1],
                [0, 1, 1, 1, 1, 0],
            ],
            88,
        ),
        (
            [
                [1, 1, 1, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [0, 1, 1, 1, 1, 0, 0, 1],
                [1, 0, 0, 0, 0, 1, 0, 1],
                [1, 0, 0, 1, 0, 1, 0, 1],
                [1, 0, 1, 0, 0, 1, 0, 1],
                [1, 0, 0, 1, 1, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 1],
                [0, 1, 1, 1, 1, 1, 1, 0],
            ],
            226,
        ),
        (
            [
                [1, 1, 1, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 0, 1],
                [1, 0, 0, 0, 0, 1, 0, 1],
                [1, 0, 1, 1, 0, 1, 0, 1],
                [1, 0, 1, 0, 0, 1, 0, 1],
                [1, 0, 1, 1, 1, 1, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 1],
                [0, 1, 1, 1, 1, 1, 1, 0],
            ],
            269,
        ),
        ([[2, 0, 2, 0, 0], [1, 1, 0, 0, 1], [0, 2, 0, 0, 0], [0, 0, 0, 0, 0]], 9),
        (big_map, -1),
        (second_big_map, -1),
    ],
)
def tests_a(values, expected):
    assert Solution().shortestDistance(values) == expected


if __name__ == "__main__":
    Solution().shortestDistance(second_big_map)
