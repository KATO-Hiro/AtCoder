# -*- coding: utf-8 -*-
# AtCoder Beginner Contest


def main():
    n, t = list(map(int, input().split()))
    a = [int(input()) for _ in range(n)]
    duration = t

    # See:
    # https://beta.atcoder.jp/contests/abc024/submissions/2841120
    for i in range(1, n):
        duration += min(t, a[i] - a[i - 1])

    print(duration)


if __name__ == '__main__':

    main()
