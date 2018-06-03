"""
Implement an algorithm to determine if a string has all unique characters. What if you
can not use additional data structures?
"""
from collections import Counter

import pytest


def unique_string_using_hash(input_string):
    temp_hash = set()
    for character in input_string:
        if character not in temp_hash:
            temp_hash.add(character)
        else:
            return False
    return True


def unique_string_not_using_hash(input_string):
    for i, fixed_character in enumerate(input_string):
        if i < len(input_string) - 2:
            for char_to_compare in input_string[i+1:]:
                if char_to_compare == fixed_character:
                    return False
    return True


@pytest.mark.parametrize('input_string,expected', [
    ('experiment', False),
    ('', True),
    ('a', True),
    ('abcd', True),
])
def test_a(input_string, expected):
    assert unique_string_using_hash(input_string) == expected
    assert unique_string_not_using_hash(input_string) == expected


"""
Write code to reverse a C-Style String. (C-String means that “abcd” is represented as
five characters, including the null character.)
"""


def reverse_c_style_string(input_string):
    return ''.join(sorted(input_string, reverse=True))


@pytest.mark.parametrize('input_string,expected', [
    ('abcd\0', 'dcba\0'),
    ('\0', '\0'),
])
def test_b(input_string, expected):
    assert reverse_c_style_string(input_string) == expected


"""
Design an algorithm and write code to remove the duplicate characters in a string
without using any additional buffer. NOTE: One or two additional variables are fine.
An extra copy of the array is not.
FOLLOW UP
Write the test cases for this method.
"""


def remove_duplicates(input_string):
    first = 0
    while first < len(input_string):
        second = first + 1
        while second < len(input_string):
            if input_string[first] == input_string[second]:
                input_string = input_string[:second] + input_string[second+1:]
            else:
                second += 1
        first += 1

    return input_string


@pytest.mark.parametrize('input_string,expected', [
    ('abcd', 'abcd'),
    ('', ''),
    ('aaa', 'a'),
    ('abca', 'abc'),
    ('abcabbbbad', 'abcd'),
])
def test_c(input_string, expected):
    assert remove_duplicates(input_string) == expected


"""
Write a method to decide if two strings are anagrams or not.
"""


def anagrams(string_a, string_b):
    if string_a == string_b:
        return False

    def convert(convert_x):
        convert_x = convert_x.replace(' ', '').lower()
        return Counter(convert_x)

    return convert(string_a) == convert(string_b)


@pytest.mark.parametrize('string_a,string_b,expected', [
    ('', '', False),
    ('abcd', 'abcd', False),
    ('ab', 'ba', True),
    ('alpha', 'palh', False),
    ('rail safety', 'fairy tales', True),
    ('restful', 'fluster', True),
    ('customers', 'store scum', True),
    ('Ars magna', 'Anagrams', True),
    ('I am a weakish speller', 'William Shakespeare', True),
])
def test_d(string_a, string_b, expected):
    assert anagrams(string_a, string_b) == expected


"""
Write an algorithm such that if an element in an MxN matrix is 0, its entire row is set to 0
"""


def rows_to_zero(matrix):
    for index_row in range(len(matrix)):
        if any([True for x in matrix[index_row] if x == 0]):
            matrix[index_row] = [0] * len(matrix[index_row])

    return matrix


@pytest.mark.parametrize('matrix,expected', [
    ([
         [1, 2, 0],
         [2, 3, 1],
         [2, 0, 0],
     ],
     [
         [0, 0, 0],
         [2, 3, 1],
         [0, 0, 0],
     ])
])
def test_e(matrix, expected):
    assert rows_to_zero(matrix) == expected


"""
Write an algorithm where a string s2 is reordered following the order of the letters of another string s1.
if one of the characters does not appear in s2, then it should go at the end.
"""


def order_s1_with_s2(string_to_order, order_string):
    alphabet_size = 26

    positions_hash = {}
    for i, character in enumerate(order_string):
        if character not in positions_hash:
            positions_hash[character] = i

    positions_array = ['' for _ in range(alphabet_size + 1)]
    for character in string_to_order:
        if character not in positions_hash:
            positions_array[-1] += character
        else:
            positions_array[positions_hash[character]] += character

    return ''.join([y for x in positions_array for y in x])


@pytest.mark.parametrize('string_a,string_b,expected', [
    ('', '', ''),
    ('abcd', 'abcd', 'abcd'),
    ('program', 'grapfo', 'grrapom'),
])
def test_order_str(string_a, string_b, expected):
    assert order_s1_with_s2(string_a, string_b) == expected
