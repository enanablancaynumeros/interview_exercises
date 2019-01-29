import pytest


class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        mid_position = len(nums) // 2
        if nums[0] > nums[mid_position]:
            if nums[1] < nums[0]:
                return nums[1]
            else:
                return self.findMin(nums[: mid_position + 1])
        elif nums[mid_position] > nums[-1]:
            if nums[mid_position] > nums[mid_position + 1]:
                return nums[mid_position + 1]
            else:
                return self.findMin(nums[mid_position - 1 :])
        else:
            return nums[0]


@pytest.mark.parametrize(
    "values,expected",
    [
        ([3, 4, 5, 1, 2], 1),
        ([4, 5, 6, 7, 0, 1, 2], 0),
        ([5, 0, 1, 2, 3], 0),
        ([0], 0),
        ([1, 2], 1),
        ([4, 5, 1, 2, 3], 1),
    ],
)
def tests_a(values, expected):
    assert Solution().findMin(values) == expected
