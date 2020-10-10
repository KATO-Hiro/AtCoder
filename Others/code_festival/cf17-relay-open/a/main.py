# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    k, a, b = map(int, input().split())

    if a >= k:
        print(1)
    elif (a - b) <= 0:
        print(-1)
    else:
        # See:
        # https://atcoder.jp/contests/cf17-relay-open/submissions/1812697
        # 切り捨ての扱い
        count = (k - a - 1) // (a - b) + 1
        print(2 * count + 1)


if __name__ == "__main__":
    main()
