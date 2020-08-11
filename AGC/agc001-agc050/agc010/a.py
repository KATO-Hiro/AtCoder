'''input
5
1 2 3 4 5
NO

1
1
YES

3
1 2 3
YES

'''

# -*- coding: utf-8 -*-

# AtCoder Grand Contest
# Problem A


if __name__ == '__main__':
    n = int(input())

    # https://atcoder.jp/img/agc010/editorial.pdf
    if sum(list(map(int, input().split()))) % 2 == 0:
        print('YES')
    else:
        print('NO')
