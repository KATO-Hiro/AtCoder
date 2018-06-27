'''input
3
3
5
7
105

4
3
5
7
10
210

2
999999999999999999
1000000000000000000

3
3
2
3
6

2
2
3
6

5
2
5
10
1000000000000000000
1000000000000000000
1000000000000000000

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C


# See:
# https://note.nkmk.me/python-gcd-lcm/
# https://docs.python.jp/3/library/functools.html
# https://docs.python.jp/3/library/fractions.html
def lcm_for_list(numbers):
    from functools import reduce
    return reduce(lcm, numbers, 1)


def lcm(x, y):
    from fractions import gcd  # for Ver.3.4 or lower.
    return (x * y) // gcd(x, y)


if __name__ == '__main__':
    n = int(input())
    t = [int(input()) for _ in range(n)]
    print(lcm_for_list(t))
