# -*- coding: utf-8 -*-
# AtCoder Beginner Contest


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    count = 0

    # See:
    # https://beta.atcoder.jp/contests/abc100/submissions/2675457
    for ai in a:
        while ai % 2 == 0:
            ai //= 2
            count += 1

    print(count)
