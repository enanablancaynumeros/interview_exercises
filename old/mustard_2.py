import nose
from functools import wraps


def stack_exceptions(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        try:
            return f(*args, **kwds)
        except IndexError:
            return -1
        except OverflowError:
            return -1

    return wrapper


def perform_operation(string, stack):
    value1 = stack.pop()
    value2 = stack.pop()
    if string == "*":
        result = value1 * value2
    else:
        result = value1 + value2

    if result > 2 ** 12:
        raise OverflowError
    else:
        return result


@stack_exceptions
def solution(given_string):
    stack = []
    for x in given_string:
        if x.isdigit():
            stack.append(int(x))
        else:
            stack.append(perform_operation(x, stack))
    return stack.pop()


def test_1():
    test_string = "13+62*7+*"
    nose.tools.assert_equal(solution(test_string), 76)

    test_string = "13+"
    nose.tools.assert_equal(solution(test_string), 4)

    test_string = "1+"
    nose.tools.assert_equal(solution(test_string), -1)

    test_string = "99999***"
    nose.tools.assert_equal(solution(test_string), -1)


#
# def test_2():
#     nose.tools.assert_equal(get_price_from_seconds(301), 900)
#     nose.tools.assert_equal(get_price_from_seconds(0), 0)
#     nose.tools.assert_equal(get_price_from_seconds(4), 12)
