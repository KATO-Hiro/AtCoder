# -*- coding: utf-8 -*-
# AtCoder Beginner Contest


def main():
    from math import pi

    n = int(input())
    r = sorted([int(input()) ** 2 for _ in range(n)], reverse=True)

    # See:
    # https://beta.atcoder.jp/contests/abc026/submissions/2761208
    print((sum(r[::2]) - sum(r[1::2])) * pi)


if __name__ == '__main__':
    main()
