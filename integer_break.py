from functools import reduce

import operator

import pytest


class Solution:
    def integerBreak(self, n: 'int') -> 'int':
        ones = [1 for _ in range(n)]
        combinations = self.calculate(ones)
        biggest = 0
        print(combinations)
        for combination in combinations:
            if len(combination) > 1:
                biggest = max(biggest, reduce(operator.mul, combination))
        return biggest

    def calculate(self, numbers) -> 'List[List[int]]':
        if len(numbers) == 1:
            return [numbers]
        elif len(numbers) == 2:
            return [numbers, [sum(numbers)]]
        else:
            results = []
            for i in range(1, len(numbers) // 2 + 1):
                lefts = self.calculate(numbers[:i + 1])
                rights = self.calculate(numbers[i + 1:])
                for left in lefts:
                    for right in rights:
                        new = [x for x in left]
                        new.extend(right)
                        results.append(new)
                if not len(lefts) and len(rights):
                    results.extend(rights)
                if not len(rights) and len(lefts):
                    results.extend(lefts)

        return results


@pytest.mark.parametrize("n,expected", [
    # (2, 1),
    # (3, 2),
    # (4, 4),
    (5, 6)
])
def tests(n, expected):
    assert Solution().integerBreak(n) == expected

