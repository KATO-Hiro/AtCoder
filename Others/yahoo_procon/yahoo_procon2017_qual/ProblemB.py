'''input
5 3
6 3 2 4 7
12

3 2
1 3 5
5

'''

# -*- coding: utf-8 -*-

# yahoo procon2017 qual
# Problem B


if __name__ == '__main__':
    from itertools import accumulate

    n, k = list(map(int, input().split()))
    a = sorted(list(map(int, input().split())))
    print(max(accumulate(a[:k])) + (k * (k - 1) // 2))
