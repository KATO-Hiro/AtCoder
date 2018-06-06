'''input
15
6

100000
10

'''

# -*- coding: utf-8 -*-

# AtCoder Grand Contest
# Problem A


if __name__ == '__main__':
    n = list(map(int, list(input())))

    # See:
    # https://www.youtube.com/watch?v=Ommfmx2wtuY
    # https://beta.atcoder.jp/contests/agc025/submissions/2607113
    if n[0] == 1 and sum(n) == 1:
        print(10)
    else:
        print(sum(n))
