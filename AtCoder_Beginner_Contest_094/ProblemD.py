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
    diff = float('inf')
    center = 0

    for ai in a:
        current_diff = abs(a_max / 2 - ai)

        if current_diff < diff:
            diff = current_diff
            center = ai

    print(str(a_max) + ' ' + str(center))
