# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, d = map(int, input().split())
    ans = 0

    for _ in range(n):
        ai, bi = map(int, input().split())
        ans += ai + bi * d

    print(ans)


if __name__ == "__main__":
    main()
