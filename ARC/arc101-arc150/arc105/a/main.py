# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline
    a, b, c, d = sorted(map(int, input().split()))

    # KeyInsight:
    # 一般性が失われなければ、昇順を仮定しても良い
    if (a + d == b + c) or (a + b + c == d):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
