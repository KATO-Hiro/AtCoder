# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, r = map(int, input().split())
    ans = 0

    for _ in range(n):
        xi, yi, pi, qi = map(int, input().split())

        if (xi - pi) ** 2 + (yi - qi) ** 2 > r**2:
            continue

        ans += 1

    print(ans)


if __name__ == "__main__":
    main()
