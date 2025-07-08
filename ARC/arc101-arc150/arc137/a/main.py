# -*- coding: utf-8 -*-


def main():
    import sys
    from math import gcd

    input = sys.stdin.readline

    l, r = map(int, input().split())
    ans = 1

    for x in range(l, l + 1501):
        for y in range(r - 1500, r + 1):
            if gcd(x, y) != 1:
                continue

            ans = max(ans, y - x)

    print(ans)


if __name__ == "__main__":
    main()
