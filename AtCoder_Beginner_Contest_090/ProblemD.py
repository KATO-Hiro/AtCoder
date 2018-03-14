'''input
31415 9265
287927211
10 0
100
5 2
7
'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem D

if __name__ == '__main__':
    number, k = list(map(int, input().split()))
    count = 0

    # See:
    # https://img.atcoder.jp/arc091/editorial.pdf
    # https://beta.atcoder.jp/contests/abc090/submissions/2193514
    for b in range(1, number + 1):
        p, r = divmod(number, b)
        count += p * max(0, b - k) + max(0, r - k + 1)

    if k == 0:
        count -= number

    print(count)
