'''input
1000000000 1000000000
0
100 17
83
48 58
0
'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    X, t = list(map(int, input().split()))

    result = X - t

    if result >= 0:
        print(result)
    else:
        print(0)
