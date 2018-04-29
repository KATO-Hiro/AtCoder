'''input
5
1 -2 3 -4 5
0

6
1 3 -4 2 2 -2
3

7
1 -1 1 -1 1 -1 1
12

'''

# -*- coding: utf-8 -*-

# AtCoder Grand Contest
# Problem A


if __name__ == '__main__':
    from itertools import accumulate
    from collections import Counter

    n = int(input())
    a = [0] + list(map(int, input().split()))

    # See:
    # https://www.youtube.com/watch?v=8BHBFMrZ8VM
    # https://beta.atcoder.jp/contests/agc023/submissions/2431021
    s = list(accumulate(a))

    print(sum([si * (si - 1) // 2 for si in Counter(s).values()]))
