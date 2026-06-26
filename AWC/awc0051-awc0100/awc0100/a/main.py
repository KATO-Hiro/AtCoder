# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ans = 0

    for _ in range(n):
        ai, ti = map(int, input().split())
        ans += ai * ti

    print(ans)


if __name__ == "__main__":
    main()
