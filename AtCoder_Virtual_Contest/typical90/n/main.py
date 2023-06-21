# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    ans = 0

    for ai, bi in zip(a, b):
        ans += abs(ai - bi)

    print(ans)


if __name__ == "__main__":
    main()
