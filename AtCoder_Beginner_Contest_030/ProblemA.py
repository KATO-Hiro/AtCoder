'''input
66 30 55 25
DRAW

5 2 6 3
AOKI

100 80 100 73
TAKAHASHI

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    a, b, c, d = list(map(int, input().split()))

    if ((b / a) - (d / c)) > 0.0:
        print('TAKAHASHI')
    elif ((d / c) - (b / a)) > 0.0:
        print('AOKI')
    elif abs((b / a) - (d / c)) < 10 ** (-8):
        print('DRAW')
