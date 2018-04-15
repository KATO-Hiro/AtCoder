'''input
6
6 9 4 2 11 10000000
10000000 11

2
100 0
100 0

6
6 9 4 2 11 8
11 6

5
6 9 4 2 11
11 6

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem D

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    a_max = max(a)
    a.remove(a_max)
    a = sorted(a)

    # See:
    # https://www.youtube.com/watch?v=RwWljbtCrPA
    # https://img.atcoder.jp/arc095/editorial.pdf
    # https://beta.atcoder.jp/contests/abc094/submissions/2354745
    k = [abs(a_max / 2 - ai) for ai in a]
    center = k.index(min(k))
    print(a_max, a[center])
