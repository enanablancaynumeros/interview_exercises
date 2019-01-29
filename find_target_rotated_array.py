import pytest


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        mid_position = len(nums) // 2
        if nums[0] == target:
            return 0
        elif target == nums[mid_position]:
            return mid_position
        elif target == nums[-1]:
            return len(nums) - 1

        if (
            
            nums[0] < target > nums[mid_position]
            or nums[0] > target > nums[mid_position]
            or nums[0] < target < nums[mid_position]
            or nums[0] > target < nums[mid_position]
        ):
            left_search = self.search(nums[:mid_position], target=target)
            if left_search >= 0:
                return left_search
            else:
                return -1
        elif (
            nums[-1] > target > nums[mid_position]
            or nums[-1] > target < nums[mid_position]
            or nums[-1] < target > nums[mid_position]
            or nums[-1] < target > nums[mid_position]
        ):
            right_search = self.search(nums[mid_position + 1:], target=target)
            if right_search >= 0:
                return right_search + mid_position + 1
            else:
                return -1
        return -1
        


@pytest.mark.parametrize(
    "values,target,expected",
    [
        ([3, 4, 5, 1, 2], 1, 3),
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([5, 0, 1, 2, 3], 3, 4),
        ([0], 0, 0),
        ([1, 2], 1, 0),
        ([4, 5, 1, 2, 3], 7, -1),
        ([], 0, -1),
        ([4,5,6,7,0,1,2], 5, 1),
        ([7,8,1,2,3,4,5,6], 2, 3)

    ],
)
def tests_a(values, target, expected):
    assert Solution().search(values, target) == expected
