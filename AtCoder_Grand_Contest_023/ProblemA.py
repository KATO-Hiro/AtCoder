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
    from collections import Counter

    n = int(input())
    a = [0] + list(map(int, input().split()))
    s = [0] * len(a)

    # See:
    # https://www.youtube.com/watch?v=8BHBFMrZ8VM
    for i in range(1, n + 1):
        s[i] += s[i - 1] + a[i]

    print(sum([si * (si - 1) // 2 for si in Counter(s).values()]))
