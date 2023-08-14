# -*- coding: utf-8 -*-


def f(i):
    return i * (i + 1) // 2


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ans = 0

    for _ in range(n):
        ai, bi = map(int, input().split())
        ans += f(bi) - f(ai - 1)

    print(ans)


if __name__ == "__main__":
    main()
