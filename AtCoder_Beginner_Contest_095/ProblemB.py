'''input
5 3000
150
130
150
130
110
26

3 1000
120
100
140
9

4 360
90
90
90
90
4

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B

if __name__ == '__main__':
    from math import floor

    n, x = list(map(int, input().split()))
    m = [int(input()) for _ in range(n)]
    at_least_g = sum(m)
    diff = x - at_least_g

    if diff == 0:
        print(len(m))
    else:
        print(len(m) + floor(diff / min(m)))
