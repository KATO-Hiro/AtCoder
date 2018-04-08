'''input
31 41 5
23

2 6 3
5

2 5 4
2

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C

if __name__ == '__main__':
    a, b, c = list(map(int, input().split()))

    # See:
    # https://www.youtube.com/watch?v=HDRfgn_UXLE
    # https://img.atcoder.jp/arc094/editorial.pdf
    count_min = max(a, b, c)

    if ((count_min % 2) != ((a + b + c) % 2)):
        count_min += 1

    print((3 * count_min - (a + b + c)) // 2)
