'''input
4 8 2
3

0 5 1
6

9 9 2
0

1 1000000000000000000 3
333333333333333333

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B

if __name__ == '__main__':
    a, b, x = list(map(int, input().split()))

    # See:
    # https://atcoder.jp/img/arc064/editorial.pdf
    fb = (b // x) + 1
    fa = ((a - 1) // x) + 1

    if a == 0:
        print(fb)
    else:
        print(fb - fa)
