# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, a = map(int, input().split())
    t = list(map(int, input().split()))
    prev = 0

    for ti in t:
        ans = max(prev, ti) + a
        print(ans)
        prev = ans


if __name__ == "__main__":
    main()
