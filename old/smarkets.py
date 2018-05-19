import nose
from collections import Counter


def test_1():
    def test(f, st, ex):
        nose.tools.assert_equal(f(st), ex)

    strings = [
        'hhpddlnnsjfoyxpciioigvjqzfbpllssuj',
        'xulkowreuowzxgnhmiqekxhzistdocbnyozmnqthhpievvlj',
        'dnqaurlplofnrtmh',
        'aujteqimwfkjoqodgqaxbrkrwykpmuimqtgulojjwtukjiqrasqejbvfbixnchzsahpnyayutsgecwvcqngzoehrmeeqlgknnb',
        'lbafwuoawkxydlfcbjjtxpzpchzrvbtievqbpedlqbktorypcjkzzkodrpvosqzxmpad',
        'drngbjuuhmwqwxrinxccsqxkpwygwcdbtriwaesjsobrntzaqbe',
        'ubulzt',
        'vxxzsqjqsnibgydzlyynqcrayvwjurfsqfrivayopgrxewwruvemzy',
        'xtnipeqhxvafqaggqoanvwkmthtfirwhmjrbphlmeluvoa',
        'gqdvlchavotcykafyjzbbgmnlajiqlnwctrnvznspiwquxxsiwuldizqkkaawpyyisnftdzklwagv',
        'abc',
        'abcdefg'
    ]
    expected_outputs = [10, 13, 5, 26, 15, -1, 3, 13, 13, -1, -1, -1]
    for string, expected_output in zip(strings, expected_outputs):
        yield test, function, string, expected_output


def main():
    n = int(raw_input())
    if n > 100:
        raise Exception("n greater than 100")
    for i in range(n):
        new_string = raw_input()
        if len(new_string) > 10000:
            raise Exception("n greater than 10000")
        print(function(new_string))


def function(string):
    if len(string) < 2:
        return -1
    if len(string) % 2:
        first_partition, second_partition = string[:(len(string) / 2)], string[(len(string) / 2):]
        third_partition, fourth_partition = string[:(len(string) / 2) + 1], string[(len(string) / 2) + 1:]
        option_1 = difference(first_partition, second_partition)
        option_2 = difference(third_partition, fourth_partition)
        if option_1 >= max([len(first_partition)/2, len(second_partition)/2]):
            return -1
        if option_2 >= max([len(third_partition)/2, len(fourth_partition)/2]):
            return -1
        return min(option_1, option_2)
    else:
        return difference(string[:len(string) / 2], string[len(string) / 2:])


def difference(string_a, string_b):
    counter_a = Counter(string_a)
    counter_b = Counter(string_b)
    diff_1 = counter_b - counter_a
    return sum(diff_1.values())


if __name__ == "__main__":
    main()


