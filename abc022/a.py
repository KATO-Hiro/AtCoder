'''input
5 50 100
120
-10
-20
-30
70
2

5 60 70
50
10
10
10
10
2

'''

# -*- coding: utf-8 -*-
# AtCoder Beginner Contest


if __name__ == '__main__':
    n, s, t = list(map(int, input().split()))
    w = int(input())
    a = [int(input()) for _ in range(n - 1)]
    day_count = 0

    if s <= w <= t:
        day_count += 1

    for ai in a:
        w += ai

        if s <= w <= t:
            day_count += 1

    print(day_count)
