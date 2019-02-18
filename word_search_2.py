import copy

import pytest


class TrieNode:
    def __init__(self):
        self.flag = False
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, words):
        for word in words:
            root = self.root
            for char in word:
                root = root.children.setdefault(char, TrieNode())
            root.flag = True


big_map = [
    ["b", "a", "a", "b", "a", "b"],
    ["a", "b", "a", "a", "a", "a"],
    ["a", "b", "a", "a", "a", "b"],
    ["a", "b", "a", "b", "b", "a"],
    ["a", "a", "b", "b", "a", "b"],
    ["a", "a", "b", "b", "b", "a"],
    ["a", "a", "b", "a", "a", "b"],
]
big_words = [
    "bbaabaabaaaaabaababaaaaababb",
    "aabbaaabaaabaabaaaaaabbaaaba",
    "babaababbbbbbbaabaababaabaaa",
    "bbbaaabaabbaaababababbbbbaaa",
    "babbabbbbaabbabaaaaaabbbaaab",
    "bbbababbbbbbbababbabbbbbabaa",
    "babababbababaabbbbabbbbabbba",
    "abbbbbbaabaaabaaababaabbabba",
    "aabaabababbbbbbababbbababbaa",
    "aabbbbabbaababaaaabababbaaba",
    "ababaababaaabbabbaabbaabbaba",
    "abaabbbaaaaababbbaaaaabbbaab",
    "aabbabaabaabbabababaaabbbaab",
    "baaabaaaabbabaaabaabababaaaa",
    "aaabbabaaaababbabbaabbaabbaa",
    "aaabaaaaabaabbabaabbbbaabaaa",
    "abbaabbaaaabbaababababbaabbb",
    "baabaababbbbaaaabaaabbababbb",
    "aabaababbaababbaaabaabababab",
    "abbaaabbaabaabaabbbbaabbbbbb",
    "aaababaabbaaabbbaaabbabbabab",
    "bbababbbabbbbabbbbabbbbbabaa",
    "abbbaabbbaaababbbababbababba",
    "bbbbbbbabbbababbabaabababaab",
    "aaaababaabbbbabaaaaabaaaaabb",
    "bbaaabbbbabbaaabbaabbabbaaba",
    "aabaabbbbaabaabbabaabababaaa",
    "abbababbbaababaabbababababbb",
    "aabbbabbaaaababbbbabbababbbb",
    "babbbaabababbbbbbbbbaabbabaa",
]


class SolutionTrie:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie = Trie()
        trie.insert(words)

        results = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.check(trie.root, board, i, j, results, "")

        return list(results)

    def check(self, trie, board, i, j, results, temp):
        char = board[i][j]
        node = trie.children.get(char)
        if node is None:
            return
        elif node.flag:
            results.add(temp + char)

        board[i][j] = None
        for pos in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            x, y = i + pos[0], j + pos[1]
            if (
                len(board) > x >= 0
                and len(board[0]) > y >= 0
                and board[x][y] in node.children
            ):
                self.check(node, board, x, y, results, temp + char)

        board[i][j] = char


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        found_words = set()
        if not len(words):
            return list(found_words)

        memory = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                index_word = 0
                while index_word < len(words):
                    if board[i][j] == words[index_word][0]:
                        if self.search(board, i, j, words[index_word], set(), memory):
                            found_words.add(words.pop(index_word))
                            if not len(words):
                                return list(found_words)
                            continue
                    index_word += 1
        return list(found_words)

    def search(self, board, i, j, word, visited, memory):
        visited.add((i, j))
        if len(visited) == len(word):
            return True

        precalculated = memory.get((i, j, len(visited), word))
        if precalculated is not None:
            return precalculated

        for near in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            near = (i + near[0], j + near[1])
            if (
                len(board) > near[0] >= 0
                and len(board[0]) > near[1] >= 0
                and near not in visited
                and word[len(visited)] == board[near[0]][near[1]]
            ):
                if self.search(
                    board, near[0], near[1], word, copy.copy(visited), memory
                ):
                    return True

        memory[(i, j, len(visited), word)] = False
        return False


@pytest.mark.parametrize(
    "board,words,expected",
    [
        (
            [
                ["o", "a", "a", "n"],
                ["e", "t", "a", "e"],
                ["i", "h", "k", "r"],
                ["i", "f", "l", "v"],
            ],
            ["oath", "pea", "eat", "rain"],
            ["eat", "oath"],
        ),
        (
            [["a", "b"], ["a", "a"]],
            ["aba", "baa", "bab", "aaab", "aaa", "aaaa", "aaba"],
            ["aaa", "aaab", "aaba", "aba", "baa"],
        ),
        (
            big_map,
            big_words,
            [
                "aabbbbabbaababaaaabababbaaba",
                "abaabbbaaaaababbbaaaaabbbaab",
                "ababaababaaabbabbaabbaabbaba",
            ],
        ),
    ],
)
def tests(board, words, expected):
    assert set(SolutionTrie().findWords(board, words)) == set(expected)


if __name__ == "__main__":
    SolutionTrie().findWords(big_map, big_words)
