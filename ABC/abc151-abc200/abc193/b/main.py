# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ans = float("inf")

    for i in range(n):
        ai, pi, xi = map(int, input().split())
        diff = max(0, xi - ai)

        if diff > 0:
            ans = min(ans, pi)

    if ans == float("inf"):
        ans = -1

    print(ans)


if __name__ == "__main__":
    main()
