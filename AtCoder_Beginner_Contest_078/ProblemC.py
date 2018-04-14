'''input
100 5
608000

1 1
3800

10 2
18400

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C

if __name__ == '__main__':
    n, m = map(int, input().split())

    # See:
    # https://img.atcoder.jp/arc085/editorial.pdf
    x = 1900 * m + 100 * (n - m)
    q = 2 ** m
    result = x * q
    print(result)
