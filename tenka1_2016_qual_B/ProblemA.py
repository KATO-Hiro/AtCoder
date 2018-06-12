'''input

'''

# -*- coding: utf-8 -*-

# tenka1 2016 qual B
# Problem A


def f(n: int):
    from math import floor
    return floor((n ** 2 + 4.0) / 8.0)


if __name__ == '__main__':
    # See:
    # https://beta.atcoder.jp/contests/tenka1-2016-qualb/submissions/1991012
    print(f(f(f(20))))
