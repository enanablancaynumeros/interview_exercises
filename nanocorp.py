import timeit
from functools import partial


import numpy as np
from matplotlib import pyplot


def compute_original(rows, columns):
    X = np.ones((rows, columns))
    P = np.ones((rows, columns))
    Y = np.ones((rows, columns))
    M = np.zeros((rows, rows))

    for i in range(rows):
        for j in range(rows):
            M[i, j] = ((X[i] - P[i] * Y[j]) ** 2).sum()


def compute_a(rows, columns):
    X = np.ones((rows, columns))
    P = np.ones((rows, columns))
    Y = np.ones((rows, columns))
    M = np.zeros((rows, rows))

    for i in range(rows):
        M[i] = np.sum((X[i] - Y * P[i]) ** 2, axis=1)


def plot(function, args):
    """
    Run timer and plot time complexity
    """
    x = []
    y = []
    for i, arg in enumerate(args):
        testNTimer = timeit.Timer(partial(function, *arg))
        t = testNTimer.timeit(number=10)
        x.append(i)
        y.append(t)
    p1 = pyplot.plot(x, y, 'o')
    pyplot.legend([p1,], [function.__name__, ])


if __name__ == '__main__':
    # plot(compute, [(10, 10), (100, 100), (1000, 1000)])
    # pyplot.show()
    compute_original(5000, 1000)
