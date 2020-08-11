'''input
5 500
35 44
28 83
46 62
31 79
40 43
9

3 20
5 50
4 60
3 100
1

1 10
3 5
3

2 10
4 3
3 2
3

2 10
3 5
2 6
2

4 1000000000
1 1
1 10000000
1 30000000
1 99999999
860000004

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem D

if __name__ == '__main__':
    from math import ceil

    n, h = list(map(int, input().split()))
    a = list()
    b = list()

    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)

    a_max = max(a)
    bs = sorted([bi for bi in b if bi > a_max], reverse=True)
    remain_hp = h - sum(bs)

    # See:
    # https://img.atcoder.jp/abc085/editorial.pdf
    # https://beta.atcoder.jp/contests/abc085/submissions/1970488
    # https://docs.python.jp/3/library/math.html
    if remain_hp > 0:
        print(ceil(remain_hp / a_max) + len(bs))
    else:
        for index, bi in enumerate(bs):
            h -= bi

            if h <= 0:
                print(index + 1)
                break
