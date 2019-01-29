from collections import Counter


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

counter = Counter()

class Solution:
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        self._findFrequentTreeSum(root)
        most_frequent = []
        highest_frequency = 0
        for total_sum, frequency in counter.items():
            if frequency > highest_frequency:
                most_frequent = [total_sum]
                highest_frequency = frequency
            elif frequency == highest_frequency:
                most_frequent.append(total_sum)
        return most_frequent
    
    def _findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        left_sum = 0
        right_sum = 0
        if root.left is None and root.right is None:
            counter[root.val] += 1
            return root.val
        if root.left is not None:
            left_sum = self._findFrequentTreeSum(root.left)
        if root.right is not None:
            right_sum = self._findFrequentTreeSum(root.right)
            
        counter[root.val + left_sum + right_sum] += 1
        return root.val + left_sum + right_sum


def tests_a():
    root = TreeNode(5)
    root.left = TreeNode(2)
    root.right = TreeNode(-3)
    assert Solution().findFrequentTreeSum([]) == []
    assert set(Solution().findFrequentTreeSum(root)) == set([2, -3, 4])
