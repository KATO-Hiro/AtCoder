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

    # See:
    # https://www.slideshare.net/chokudai/abc030
    if (b * c) - (d * a) > 0:
        print('TAKAHASHI')
    elif (d * a) - (b * c) > 0:
        print('AOKI')
    else:
        print('DRAW')
