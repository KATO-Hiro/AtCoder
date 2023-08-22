# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    diff = 10**18
    ans = -1

    for i, hi in enumerate(h, 1):
        candidate = abs(a - (t - hi * 0.006))

        if candidate < diff:
            ans = i
            diff = candidate

    print(ans)


if __name__ == "__main__":
    main()
