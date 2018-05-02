'''input
12 100
9

12 36
3

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    from math import ceil

    a, b = list(map(int, input().split()))
    print(ceil(b / a))
