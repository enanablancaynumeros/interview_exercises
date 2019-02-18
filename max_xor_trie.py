import pytest


class TrieNode:
    def __init__(self):
        self.flag = False
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        root = self.root
        for char in word:
            root = root.children.setdefault(char, TrieNode())
        root.flag = True


class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        trie = Trie()
        for num in nums:
            trie.insert(f"{num:031b}")

        maximum = 0
        for number in nums:
            res = self.find_maximum_xor(f"{number:031b}", trie.root, "")
            if res is not None:
                maximum = max(res, maximum)
        return maximum

    def find_maximum_xor(self, number, node, res):
        if len(res) == len(number):
            return int(res, 2) ^ int(number, 2)
        char = number[len(res)]
        best_next, worst_next = ("0", "1") if char == "1" else ("1", "0")
        solution = None
        if best_next in node.children:
            solution = self.find_maximum_xor(
                number, node.children[best_next], res + best_next
            )
        if worst_next in node.children and solution is None:
            solution = self.find_maximum_xor(
                number, node.children[char], res + worst_next
            )
        return solution
