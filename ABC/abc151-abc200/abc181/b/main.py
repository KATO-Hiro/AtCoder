# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ans = 0

    for i in range(n):
        ai, bi = map(int, input().split())
        ans += (ai + bi) * (bi - ai + 1) // 2

    print(ans)


if __name__ == "__main__":
    main()
