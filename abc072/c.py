'''input
11
0 3 1 2 3 4 5 6 7 8 9
4

1
99999
1

7
3 1 4 1 5 9 2
4

10
0 1 2 3 4 5 6 7 8 9
3

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C

if __name__ == '__main__':
    from bisect import bisect_left
    from bisect import bisect_right

    n = int(input())
    a = sorted(list(map(int, input().split())))
    count = 0

    for i in range(max(a) + 1):
        left = bisect_left(a, i - 1)
        right = bisect_right(a, i + 1)
        count = max(count, max(0, right - left))

    print(count)
