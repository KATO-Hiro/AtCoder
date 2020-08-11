'''input
6
1 2 3 4 5 6
1

2
10 -10
20

2
0 10
10

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C

if __name__ == '__main__':
    from itertools import accumulate

    n = int(input())
    a = list(map(int, input().split()))

    # See:
    # https://atcoder.jp/img/arc078/editorial.pdf
    # total_a = sum(a)
    summed_a = [0] + list(accumulate(a))
    total_a = sum(a)
    diff = float('inf')

    for i in range(1, n):
        diff = min(diff, abs(total_a - 2 * summed_a[i]))

    print(diff)
