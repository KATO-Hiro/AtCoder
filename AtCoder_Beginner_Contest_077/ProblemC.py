'''input
3
1 1 1
2 2 2
3 3 3
27

6
3 14 159 2 6 53
58 9 79 323 84 6
2643 383 2 79 50 288
87

2
1 5
2 4
3 6
3

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C

if __name__ == '__main__':
    n = int(input())
    a = sorted(list(map(int, input().split())))
    b = list(map(int, input().split()))
    c = sorted(list(map(int, input().split())))
    count = 0

    # See:
    # https://img.atcoder.jp/arc084/editorial.pdf
    # https://docs.python.jp/3/library/bisect.html
    # https://beta.atcoder.jp/contests/abc077/submissions/1740764
    from bisect import bisect_left
    from bisect import bisect_right

    for number in b:
        a_count = bisect_left(a, number)
        c_count = n - bisect_right(c, number)
        count += a_count * c_count

    print(count)
