'''input
7 3 2
4 5 6
0

10 7 5
1 2 3 4 6 8 9
3

5 3 3
1 2 4
1

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B

if __name__ == '__main__':
    from bisect import bisect_left

    n, m, x = list(map(int, input().split()))
    a = list(map(int, input().split()))
    low = bisect_left(a, x)
    print(min(len(a[:low]), len(a[low:])))
