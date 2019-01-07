import pytest


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if not len(nums1):
            return self.get_median(nums2)
        elif not len(nums2):
            return self.get_median(nums1)

        index_1 = 0
        index_2 = 0
        new_array = []

        while True:
            index_1 = self.copy_while_value_is_lower(
                new_array=new_array,
                source_array=nums1,
                index_array=index_1,
                other_value=nums2[index_2],
            )
            if len(nums1) == index_1:
                new_array.extend(nums2[index_2:])
                break

            index_2 = self.copy_while_value_is_lower(
                new_array=new_array,
                source_array=nums2,
                index_array=index_2,
                other_value=nums1[index_1],
            )
            if len(nums2) == index_2:
                new_array.extend(nums1[index_1:])
                break

        return self.get_median(new_array)

    def copy_while_value_is_lower(
        self, new_array, source_array, index_array, other_value
    ):
        while (
            index_array < len(source_array) and source_array[index_array] <= other_value
        ):
            new_array.append(source_array[index_array])
            index_array += 1
        return index_array

    def get_median(self, nums):
        if len(nums) % 2 == 0:
            return (nums[(len(nums) - 1) // 2] + nums[((len(nums) - 1) // 2) + 1]) / 2
        else:
            return float(nums[len(nums) // 2])


@pytest.mark.parametrize(
    "nums1,nums2,expected",
    [
        ([], [2], 2.0),
        ([1], [], 1.0),
        ([1, 3], [2], 2.0),
        ([2], [1, 3], 2.0),
        ([2, 2], [1, 3], 2.0),
    ],
)
def tests(nums1, nums2, expected):
    assert Solution().findMedianSortedArrays(nums1=nums1, nums2=nums2) == expected
