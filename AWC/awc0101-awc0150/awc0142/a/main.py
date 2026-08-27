# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    t = list(map(float, input().split()))
    ans = 0

    for ti in t:
        ti *= 10
        ans += max(0, int(ti) - 370)

    print(ans)


if __name__ == "__main__":
    main()
