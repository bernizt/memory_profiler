# .. an example with a for loop ..

import time

def test_1():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b

    for i in range(2):
        a = [1] * (10 ** 6)
        b = [2] * (2 * 10 ** 7)
        del b
    return a


def test_2():
    a = {}
    for i in range(10000):
        a[i] = i + 1
    return

if __name__ == '__main__':
    test_1()
    time.sleep(1)
    test_2()
    time.sleep(1)
