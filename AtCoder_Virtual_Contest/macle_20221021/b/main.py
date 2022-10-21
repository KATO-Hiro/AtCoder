# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    d = sorted(a)
    b = d[n // 2 - 1]
    c = d[n // 2]

    for ai in a:
        if ai >= c:
            print(b)
        else:
            print(c)


if __name__ == "__main__":
    main()
