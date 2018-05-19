import nose

from collections import Counter
from math import ceil
import itertools as it


def get_total_seconds_from_string(duration_string):
    hours, minutes, seconds = map(int, duration_string.split(":"))
    return hours * 3600 + minutes * 60 + seconds


def get_price_from_seconds(duration_in_seconds):
    if duration_in_seconds < 5 * 60:
        return duration_in_seconds * 3
    else:
        return int(ceil(float(duration_in_seconds) / 60)) * 150


def get_index_free_call(hash_map_time):
    max_value = max(hash_map_time.values())
    top_numbers = list(it.ifilter(lambda x: hash_map_time[x] == max_value, hash_map_time))
    return sorted(top_numbers, key=lambda x: sum(map(int, x.split("-"))))[0]


def solution(given_string):
    hash_map_price = Counter()
    hash_map_time = Counter()
    for line in given_string.split("\n"):
        duration_string, number_string = line.split(",")
        duration_in_seconds = get_total_seconds_from_string(duration_string)
        hash_map_time[number_string] += duration_in_seconds
        hash_map_price[number_string] += get_price_from_seconds(duration_in_seconds)
    index_to_ignore = get_index_free_call(hash_map_time=hash_map_time)

    return sum([hash_map_price[x] for x in hash_map_price if x != index_to_ignore])


def test_1():
    test_string = "00:01:07,400-234-090\n00:05:01,701-080-080\n00:05:00,400-234-090"
    nose.tools.assert_equal(solution(test_string), 900)

    test_string = "00:01:07,400-234-090\n00:05:01,701-080-080\n00:05:00,400-234-090\n00:01:06,701-080-080"
    nose.tools.assert_equal(solution(test_string), 1098)

#
# def test_2():
#     nose.tools.assert_equal(get_price_from_seconds(301), 900)
#     nose.tools.assert_equal(get_price_from_seconds(0), 0)
#     nose.tools.assert_equal(get_price_from_seconds(4), 12)
