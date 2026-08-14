# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, r = map(int, input().split())
    a = list(map(int, input().split()))
    a_min = min(a)
    ans = 0

    for ai in a:
        ans += ai - a_min

    print(ans)


if __name__ == "__main__":
    main()
