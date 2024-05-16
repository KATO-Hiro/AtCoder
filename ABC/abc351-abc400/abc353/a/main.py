# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    h = list(map(int, input().split()))
    base = h[0]
    ans = -1

    if n >= 2:
        for i, hi in enumerate(h[1:], 2):
            if hi > base:
                ans = i
                break

    print(ans)


if __name__ == "__main__":
    main()
