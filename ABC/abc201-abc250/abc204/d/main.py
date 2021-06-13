# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    t = list(map(int, input().split()))
    dp = set([0])

    for ti in t:
        dp2 = set()

        for d in dp:
            dp2.add(d + ti)

        dp |= dp2

    total = sum(t)
    ans = float("inf")

    for t in dp:
        ans = min(ans, max(t, total - t))

    print(ans)


if __name__ == "__main__":
    main()
