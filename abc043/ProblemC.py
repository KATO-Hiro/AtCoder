'''input
3
-100 0 96
19211

1
3
0

3
1 0 3
5

4
-100 -100 -100 -100
0

3
1 1 3
3

3
4 2 5
5

1
-3
0

2
4 8
8

3
-1 -3 -5
8

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    cost = float('inf')

    # See:
    # http://arc059.contest.atcoder.jp/data/arc/059/editorial.pdf
    # https://beta.atcoder.jp/contests/abc043/submissions/2228108
    for z in range(-100, 100 + 1):
        tmp_cost = sum(((x - z) ** 2 for x in a))
        cost = min(cost, tmp_cost)

    print(cost)
